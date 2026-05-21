from __future__ import annotations

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

from department_agent_audit.event_ingest import AuditIngestService
from department_agent_audit.postgres_repository import PostgresAuditRepository
from department_agent_audit.session_manager import SessionManager


@asynccontextmanager
async def lifespan(app: FastAPI):
    dsn = os.getenv("AGENT_AUDIT_PG_DSN")
    if not dsn:
        raise RuntimeError("Set AGENT_AUDIT_PG_DSN before running audit_ingest_api.py")
    repository = await PostgresAuditRepository.create(dsn)
    app.state.repository = repository
    app.state.ingest_service = AuditIngestService(repository)
    app.state.session_manager = SessionManager(repository)
    try:
        yield
    finally:
        await repository.close()


app = FastAPI(title="department-agent-audit-ingest", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


def _validate_token(authorization: str | None) -> None:
    expected = os.getenv("AUDIT_INGEST_TOKEN", "").strip()
    if not expected:
        return
    if authorization != f"Bearer {expected}":
        raise HTTPException(status_code=401, detail="Invalid audit ingest token")


@app.post("/audit/events")
async def ingest_event(request: Request, authorization: str | None = Header(default=None)) -> dict[str, bool]:
    _validate_token(authorization)
    event = await request.json()
    await app.state.ingest_service.ingest_event(event)
    return {"ok": True}


@app.get("/audit/traces/{trace_id}")
async def get_trace(trace_id: str, authorization: str | None = Header(default=None)) -> dict:
    _validate_token(authorization)
    return await app.state.repository.fetch_trace_view(trace_id)


@app.get("/audit/events/dead-letters")
async def list_dead_letters(
    authorization: str | None = Header(default=None),
    status: str = "open",
    limit: int = 100,
) -> dict:
    _validate_token(authorization)
    rows = await app.state.repository.list_dead_letter_events(status=status, limit=limit)
    return {"items": rows}


@app.post("/audit/events/replay/{event_id}")
async def replay_event(event_id: str, authorization: str | None = Header(default=None)) -> dict:
    _validate_token(authorization)
    return await app.state.ingest_service.replay_event(event_id)


@app.get("/audit/sessions/stats")
async def get_session_stats(
    authorization: str | None = Header(default=None),
    tenant_id: str | None = None,
    user_id: str | None = None,
) -> dict:
    _validate_token(authorization)
    return await app.state.session_manager.get_session_stats(
        tenant_id=tenant_id,
        user_id=user_id,
    )


@app.get("/audit/sessions/{session_id}")
async def get_session_snapshot(
    session_id: str,
    authorization: str | None = Header(default=None),
    task_limit: int = 200,
) -> dict:
    _validate_token(authorization)
    try:
        return await app.state.session_manager.get_session_snapshot(session_id, task_limit=task_limit)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@app.post("/audit/sessions/{session_id}/close")
async def close_session(
    session_id: str,
    request: Request,
    authorization: str | None = Header(default=None),
) -> dict:
    _validate_token(authorization)
    payload = await request.json() if request.headers.get("content-type", "").startswith("application/json") else {}
    closed_by = payload.get("closed_by")
    try:
        session = await app.state.session_manager.close_session(
            session_id=session_id,
            closed_by=closed_by,
        )
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    return {"session": session}


@app.get("/audit/sessions")
async def list_sessions(
    authorization: str | None = Header(default=None),
    status: str | None = None,
    tenant_id: str | None = None,
    user_id: str | None = None,
    limit: int = 100,
    offset: int = 0,
) -> dict:
    _validate_token(authorization)
    return await app.state.session_manager.list_sessions(
        status=status,
        tenant_id=tenant_id,
        user_id=user_id,
        limit=limit,
        offset=offset,
    )
