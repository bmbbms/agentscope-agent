from __future__ import annotations

import asyncio
import os

from department_agent_audit.audit import AuditLogger
from department_agent_audit.eval_worker import EvalWorker, StubLLMJudge
from department_agent_audit.postgres_repository import PostgresAuditRepository
from merchant_data_agent.app import MerchantDepartmentApp
from merchant_data_agent.remote_agents import RemoteAgentRegistry
from merchant_data_agent.settings import MerchantAgentSettings


async def main() -> None:
    dsn = os.getenv("AGENT_AUDIT_PG_DSN")
    if not dsn:
        raise RuntimeError("Set AGENT_AUDIT_PG_DSN before running remote_agents_demo.py")

    settings = MerchantAgentSettings.from_env()
    if not settings.remote_agents:
        raise RuntimeError("Set MERCHANT_REMOTE_AGENTS_JSON before running remote_agents_demo.py")

    repository = await PostgresAuditRepository.create(dsn)
    audit_logger = AuditLogger(repository)
    registry = RemoteAgentRegistry.from_settings(
        settings.remote_agents,
        audit_sink=settings.audit_ingest_endpoint,
    )
    eval_worker = EvalWorker(repository, StubLLMJudge())
    app = MerchantDepartmentApp(
        audit_logger=audit_logger,
        agents=None,
        tools=None,
        eval_worker=eval_worker,
        remote_registry=registry,
    )

    result = await app.handle_query(
        query="帮我分析昨天核心商户GMV异常下滑原因",
        user_id="demo.analyst",
    )
    print("Remote business reply:", result.get("reply", result))
    await repository.close()


if __name__ == "__main__":
    asyncio.run(main())
