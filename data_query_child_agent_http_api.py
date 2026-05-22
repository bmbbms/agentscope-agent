from __future__ import annotations

from typing import Any

from fastapi import FastAPI, HTTPException

from department_agent_audit.distributed import ChildAgentAuditRunner
from superset_data_query_agent import (
    AgentScopeDataQueryWorkflow,
    SupersetDataQueryService,
    SupersetQueryRequestSpec,
)


app = FastAPI(title="merchant-data-query-child-agent")
runner = ChildAgentAuditRunner()
service = SupersetDataQueryService()
workflow = AgentScopeDataQueryWorkflow(service)


def _resolve_action(payload: dict[str, Any]) -> str:
    action = str(payload.get("action", "")).strip().lower()
    if action:
        return action
    if payload.get("list_databases"):
        return "list_databases"
    if payload.get("sql"):
        return "sql_query"
    return "schema_search"


def _build_request_spec(payload: dict[str, Any]) -> SupersetQueryRequestSpec:
    return SupersetQueryRequestSpec(
        query=payload["query"],
        action=_resolve_action(payload),
        sql=payload.get("sql"),
        database_name=payload.get("database_name"),
        preview_rows=int(payload.get("preview_rows", 20)),
        enable_mask=bool(payload.get("enable_mask", True)),
        export_excel=bool(payload.get("export_excel", False)),
        export_name=payload.get("export_name"),
        schema_keyword=payload.get("schema_keyword"),
        search_limit=int(payload.get("search_limit", 10)),
        output_dir=payload.get("output_dir"),
        timeout_seconds=int(payload.get("timeout_seconds", 120)),
    )


def _build_reply(result: dict[str, Any]) -> str:
    action = result["action"]
    execution_mode = result.get("execution_mode")
    if action == "list_databases":
        return f"Discovered {result['count']} Superset databases."
    if action == "sql_query":
        export_note = f" Excel={result['export_path']}" if result.get("export_path") else ""
        return (
            f"SQL query completed. rows={result['row_count']}, columns={result['column_count']}."
            f"{export_note} mode={execution_mode}"
        )
    if action == "sql_query_plan":
        return (
            "SQL plan generated but not executed. "
            f"reason={result.get('guard_output', {}).get('reason') or result.get('planner_output', {}).get('reason')}"
        )
    return f"Found {result['count']} schema matches for keyword '{result['keyword']}'."


async def _handle_query(context, audit_logger, request_payload: dict[str, Any]) -> dict[str, Any]:
    spec = _build_request_spec(request_payload)

    async with audit_logger.tool_step(
        context,
        step_name="prepare_data_query_request",
        sequence_no=1,
        target_name="superset_data_query_skill",
        input_payload={
            "action": spec.action,
            "database_name": spec.database_name,
            "export_excel": spec.export_excel,
            "schema_keyword": spec.schema_keyword,
            "timeout_seconds": spec.timeout_seconds,
        },
        step_type="tool_call",
    ) as finish_prepare:
        await finish_prepare(
            {
                "action": spec.action,
                "database_name": spec.database_name,
                "export_excel": spec.export_excel,
                "preview_rows": spec.preview_rows,
            },
            success=True,
            status="success",
        )

    async with audit_logger.tool_step(
        context,
        step_name="run_data_query_workflow",
        sequence_no=2,
        target_name="superset_data_query_workflow",
        input_payload={
            "action": spec.action,
            "database_name": spec.database_name,
            "sql_present": bool(spec.sql),
            "schema_keyword": spec.schema_keyword or spec.query,
            "export_excel": spec.export_excel,
        },
        step_type="tool_call",
    ) as finish_execute:
        workflow_result = await workflow.run(spec)
        if workflow_result.service_result is None:
            result = {
                "action": "sql_query_plan" if workflow_result.action == "sql_query" else workflow_result.action,
                "planner_output": workflow_result.planner_output,
                "guard_output": workflow_result.guard_output,
                "execution_mode": "agentscope_workflow" if workflow.is_enabled() else "fallback_workflow",
            }
        else:
            result = {
                **workflow_result.service_result,
                "planner_output": workflow_result.planner_output,
                "guard_output": workflow_result.guard_output,
                "execution_mode": "agentscope_workflow" if workflow.is_enabled() else "fallback_workflow",
            }
        await finish_execute(
            {
                "action": result["action"],
                "row_count": result.get("row_count"),
                "count": result.get("count"),
                "export_path": result.get("export_path"),
                "execution_mode": result.get("execution_mode"),
            },
            success=True,
            status="success",
        )

    return {
        "route": "data_query",
        "reply": _build_reply(result),
        "query_result": result,
    }


@app.post("/invoke")
async def invoke(payload: dict[str, Any]) -> dict[str, Any]:
    if "query" not in payload:
        raise HTTPException(status_code=400, detail="Missing query")
    return await runner.run(
        request_payload=payload,
        agent_name="merchant_data_query_child_agent",
        handler=_handle_query,
        source_name="merchant-data-query-service",
        workflow_name="merchant_data_query_child_workflow",
        scenario_name="data_query",
        tags=["child-agent", "data-query"],
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
