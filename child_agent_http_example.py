from __future__ import annotations

from fastapi import FastAPI

from department_agent_audit.distributed import ChildAgentAuditRunner

app = FastAPI(title="merchant-diagnosis-child-agent")
runner = ChildAgentAuditRunner()


@app.post("/invoke")
async def invoke(payload: dict) -> dict:
    async def handler(context, audit_logger, request_payload: dict) -> dict:
        query = request_payload["query"]
        async with audit_logger.tool_step(
            context,
            step_name="query_diagnosis_data",
            sequence_no=1,
            target_name="merchant_metric_service",
            input_payload={"query": query},
            step_type="tool_call",
        ) as finish_step:
            tool_result = {
                "facts": [
                    {"metric": "gmv", "delta_pct": -12.6, "segment": "核心商户"},
                    {"metric": "pay_success_rate", "delta_pct": -1.9, "segment": "华东餐饮"},
                ]
            }
            await finish_step(tool_result, success=True, status="success")

        return {
            "reply": "昨日核心商户GMV下滑主要集中在华东餐饮，支付成功率也有同步下降，建议先查支付链路和曝光变化。",
            "evidence": list(tool_result["facts"]),
        }

    return await runner.run(
        request_payload=payload,
        agent_name="merchant_diagnosis_child_agent",
        handler=handler,
        source_name="merchant-diagnosis-service",
        workflow_name="merchant_diagnosis_child_workflow",
        scenario_name="diagnosis",
        tags=["child-agent", "diagnosis"],
    )
