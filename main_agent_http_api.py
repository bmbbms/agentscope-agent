from __future__ import annotations

import os
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, Header, HTTPException, Request

from department_agent_audit.audit import AuditLogger
from department_agent_audit.eval_worker import EvalWorker, StubLLMJudge
from department_agent_audit.postgres_repository import PostgresAuditRepository
from department_agent_audit.session_manager import SessionManager
from merchant_data_agent.app import MerchantDepartmentApp
from merchant_data_agent.remote_agents import RemoteAgentRegistry
from merchant_data_agent.settings import MerchantAgentSettings


@asynccontextmanager
async def lifespan(app: FastAPI):
    dsn = os.getenv("AGENT_AUDIT_PG_DSN")
    if not dsn:
        raise RuntimeError("Set AGENT_AUDIT_PG_DSN before running main_agent_http_api.py")

    settings = MerchantAgentSettings.from_env()
    if not settings.remote_agents:
        raise RuntimeError("Set MERCHANT_REMOTE_AGENTS_JSON before running main_agent_http_api.py")

    repository = await PostgresAuditRepository.create(dsn)
    audit_logger = AuditLogger(repository)
    session_manager = SessionManager(repository)
    eval_worker = EvalWorker(repository, StubLLMJudge())
    remote_registry = RemoteAgentRegistry.from_settings(
        settings.remote_agents,
        audit_sink=settings.audit_ingest_endpoint,
    )
    app.state.repository = repository
    app.state.agent_app = MerchantDepartmentApp(
        audit_logger=audit_logger,
        agents=None,
        tools=None,
        eval_worker=eval_worker,
        session_manager=session_manager,
        remote_registry=remote_registry,
    )
    try:
        yield
    finally:
        await repository.close()


app = FastAPI(title="merchant-main-agent-api", lifespan=lifespan)


def _validate_token(authorization: str | None) -> None:
    expected = os.getenv("MAIN_AGENT_API_TOKEN", "").strip()
    if not expected:
        return
    if authorization != f"Bearer {expected}":
        raise HTTPException(status_code=401, detail="Invalid main agent token")


@app.post("/main/query")
async def main_query(request: Request, authorization: str | None = Header(default=None)) -> dict[str, Any]:
    _validate_token(authorization)
    payload = await request.json()

    query = payload["query"]
    user_id = payload.get("user_id", "anonymous")
    tenant_id = payload.get("tenant_id", "merchant-data")
    session_id = payload.get("session_id")
    task_id = payload.get("task_id")
    topic = payload.get("topic")
    user_explicitly_closed = bool(payload.get("user_explicitly_closed", False))

    result = await app.state.agent_app.handle_query(
        query=query,
        user_id=user_id,
        tenant_id=tenant_id,
        source_type="http_api",
        trigger_type="manual",
        session_id=session_id,
        task_id=task_id,
        topic=topic,
        user_explicitly_closed=user_explicitly_closed,
    )
    return result


@app.post("/main/eval/run-once")
async def run_eval_once(authorization: str | None = Header(default=None)) -> dict[str, Any]:
    _validate_token(authorization)
    eval_result = await app.state.agent_app.run_eval_once("main-agent-eval-worker")
    if not eval_result:
        return {"ok": True, "message": "no pending eval items"}
    return {
        "ok": True,
        "run_id": eval_result.run_id,
        "trace_id": eval_result.trace_id,
        "overall_passed": eval_result.overall_passed,
        "score_total": eval_result.scores.total,
    }
