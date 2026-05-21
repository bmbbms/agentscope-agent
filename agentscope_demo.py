from __future__ import annotations

import asyncio
import os

from department_agent_audit.audit import AuditLogger
from department_agent_audit.postgres_repository import PostgresAuditRepository
from merchant_data_agent.agents import build_agentscope_agents
from merchant_data_agent.app import MerchantDepartmentApp, build_eval_worker
from merchant_data_agent.settings import MerchantAgentSettings
from merchant_data_agent.tools import MerchantDataTools


async def main() -> None:
    dsn = os.getenv("AGENT_AUDIT_PG_DSN")
    if not dsn:
        raise RuntimeError("Set AGENT_AUDIT_PG_DSN before running agentscope_demo.py")

    settings = MerchantAgentSettings.from_env()
    agents = build_agentscope_agents(settings)
    repository = await PostgresAuditRepository.create(dsn)
    audit_logger = AuditLogger(repository)
    tools = MerchantDataTools()
    eval_worker = build_eval_worker(repository, agents)
    app = MerchantDepartmentApp(
        audit_logger=audit_logger,
        agents=agents,
        tools=tools,
        eval_worker=eval_worker,
    )

    result = await app.handle_query(
        query="帮我分析昨天核心商户GMV异常下滑原因",
        user_id="demo.analyst",
    )
    print("Business reply:", result["reply"])

    eval_result = await app.run_eval_once()
    if eval_result:
        print("Eval total score:", eval_result.scores.total)
        print("Eval passed:", eval_result.overall_passed)

    await repository.close()


if __name__ == "__main__":
    asyncio.run(main())
