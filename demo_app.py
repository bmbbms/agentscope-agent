from __future__ import annotations

import asyncio
import os
from typing import Any

from department_agent_audit.audit import AuditContext, AuditLogger
from department_agent_audit.eval_agent import AgentScopeLLMJudge
from department_agent_audit.eval_worker import EvalWorker
from department_agent_audit.postgres_repository import PostgresAuditRepository


class DemoMerchantAgent:
    async def __call__(self, user_query: str) -> dict[str, Any]:
        if "异常" in user_query:
            return {
                "reply": "近24小时发现12个核心商户GMV异常下滑，主要集中在华东餐饮，建议优先排查曝光和支付链路。",
                "evidence": [
                    {"metric": "gmv", "delta_pct": -13.4, "segment": "华东餐饮"},
                    {"metric": "pay_success_rate", "delta_pct": -2.1, "segment": "核心商户"},
                ],
                "prompt_tokens": 680,
                "completion_tokens": 185,
                "total_tokens": 865,
                "estimated_cost": 0.0215,
            }
        return {
            "reply": "未发现明显异常。",
            "evidence": [],
            "prompt_tokens": 420,
            "completion_tokens": 80,
            "total_tokens": 500,
            "estimated_cost": 0.011,
        }


class DemoEvaluatorAgent:
    async def __call__(self, prompt: str) -> str:
        del prompt
        return """
        {
          "scores": {
            "task_completion": 18,
            "factual_grounding": 17,
            "metric_consistency": 18,
            "actionability": 17,
            "safety_compliance": 20
          },
          "issue_tags": [],
          "findings": ["The answer includes concrete evidence and a clear next action."],
          "suggestions": ["Add merchant count by city for a stronger operational handoff."],
          "evidence": [{"type": "metric", "detail": "GMV and pay success rate deltas are cited."}]
        }
        """.strip()


async def main() -> None:
    dsn = os.getenv("AGENT_AUDIT_PG_DSN")
    if not dsn:
        raise RuntimeError("Set AGENT_AUDIT_PG_DSN before running demo_app.py")

    repository = await PostgresAuditRepository.create(dsn)
    audit_logger = AuditLogger(repository)
    business_agent = DemoMerchantAgent()

    context, agent_name = AuditContext.new(
        source_type="web_app",
        trigger_type="manual",
        agent_name="merchant_diagnosis_agent",
        workflow_name="merchant_anomaly_workflow",
        scenario_name="merchant_gmv_diagnosis",
        user_id="demo.analyst",
        tenant_id="merchant-data",
        tags=["demo", "anomaly"],
    )

    query = "帮我分析昨天核心商户GMV异常下滑原因"

    async def _call_business_agent() -> dict[str, Any]:
        return await business_agent(query)

    result = await audit_logger.invoke_with_audit(
        context,
        agent_name=agent_name,
        input_payload={"query": query},
        agent_call=_call_business_agent,
    )
    print("Business result:", result["reply"])

    judge_backend = DemoEvaluatorAgent()
    judge = AgentScopeLLMJudge(judge_backend)
    worker = EvalWorker(repository, judge)
    eval_result = await worker.run_once(worker_id="demo-worker-1")
    if eval_result:
        print("Eval total score:", eval_result.scores.total)
        print("Eval passed:", eval_result.overall_passed)
    else:
        print("No eval queue item found.")

    await repository.close()


if __name__ == "__main__":
    asyncio.run(main())
