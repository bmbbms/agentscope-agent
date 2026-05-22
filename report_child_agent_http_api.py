from __future__ import annotations

from typing import Any

from fastapi import FastAPI, HTTPException

from department_agent_audit.distributed import ChildAgentAuditRunner
from report_dashboard_agent import ReportDashboardGenerator, ReportRequestSpec


app = FastAPI(title="merchant-report-child-agent")
runner = ChildAgentAuditRunner()
generator = ReportDashboardGenerator()


def _build_request_spec(payload: dict[str, Any]) -> ReportRequestSpec:
    output_format = str(payload.get("format", "pdf")).lower()
    generate_pdf = output_format in {"pdf", "both"}
    generate_html = bool(payload.get("generate_html", output_format in {"html", "both"}))
    dashboard_type = str(payload.get("dashboard_type", "large_pos")).lower()
    return ReportRequestSpec(
        query=payload["query"],
        stat_month=payload.get("stat_month"),
        generate_pdf=generate_pdf,
        generate_html=generate_html or not generate_pdf,
        dashboard_type=dashboard_type,
        output_dir=payload.get("output_dir"),
    )


def _build_reply(result: dict[str, Any]) -> str:
    artifact_parts: list[str] = []
    for artifact in result["artifacts"]:
        title = artifact.get("title") or artifact["dashboard_type"]
        month = artifact.get("latest_month") or result.get("stat_month") or "unknown"
        outputs = []
        if artifact.get("pdf_path"):
            outputs.append(f"PDF={artifact['pdf_path']}")
        if artifact.get("html_path"):
            outputs.append(f"HTML={artifact['html_path']}")
        if artifact.get("pdf_error") and not artifact.get("pdf_path"):
            outputs.append(f"PDF unavailable ({artifact['pdf_error']})")
        artifact_parts.append(f"{title} {month}: " + ", ".join(outputs))
    return "Report generation completed. " + " | ".join(artifact_parts)


async def _handle_report(context, audit_logger, request_payload: dict[str, Any]) -> dict[str, Any]:
    spec = _build_request_spec(request_payload)
    async with audit_logger.tool_step(
        context,
        step_name="prepare_report_request",
        sequence_no=1,
        target_name="report_dashboard_skill",
        input_payload={
            "query": spec.query,
            "stat_month": spec.stat_month,
            "dashboard_type": spec.dashboard_type,
            "generate_pdf": spec.generate_pdf,
            "generate_html": spec.generate_html,
        },
        step_type="tool_call",
    ) as finish_prepare:
        prepare_output = {
            "dashboard_type": spec.dashboard_type,
            "stat_month": spec.stat_month,
            "generate_pdf": spec.generate_pdf,
            "generate_html": spec.generate_html,
        }
        await finish_prepare(prepare_output, success=True, status="success")

    async with audit_logger.tool_step(
        context,
        step_name="generate_report_artifacts",
        sequence_no=2,
        target_name="report_dashboard_generator",
        input_payload={
            "query": spec.query,
            "stat_month": spec.stat_month,
            "dashboard_type": spec.dashboard_type,
        },
        step_type="tool_call",
    ) as finish_generate:
        generation_result = generator.generate(spec)
        await finish_generate(
            {
                "artifact_count": len(generation_result["artifacts"]),
                "stat_month": generation_result.get("stat_month"),
                "artifacts": [
                    {
                        "dashboard_type": artifact["dashboard_type"],
                        "html_path": artifact.get("html_path"),
                        "pdf_path": artifact.get("pdf_path"),
                        "pdf_error": artifact.get("pdf_error"),
                    }
                    for artifact in generation_result["artifacts"]
                ],
            },
            success=True,
            status="success",
        )

    return {
        "route": "report",
        "reply": _build_reply(generation_result),
        "report_result": generation_result,
        "artifacts": generation_result["artifacts"],
    }


@app.post("/invoke")
async def invoke(payload: dict[str, Any]) -> dict[str, Any]:
    if "query" not in payload:
        raise HTTPException(status_code=400, detail="Missing query")
    return await runner.run(
        request_payload=payload,
        agent_name="merchant_report_child_agent",
        handler=_handle_report,
        source_name="merchant-report-service",
        workflow_name="merchant_report_child_workflow",
        scenario_name="report",
        tags=["child-agent", "report"],
    )


@app.post("/a2a")
async def a2a_invoke(body: dict[str, Any]) -> dict[str, Any]:
    method = body.get("method")
    if method != "tasks/send":
        raise HTTPException(status_code=400, detail="Unsupported method")
    params = body.get("params")
    if not isinstance(params, dict):
        raise HTTPException(status_code=400, detail="Missing params")
    result = await invoke(params)
    return {
        "jsonrpc": "2.0",
        "id": body.get("id"),
        "result": result,
    }
