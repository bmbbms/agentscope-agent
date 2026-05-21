from __future__ import annotations

import uuid
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any

from .storage import AuditRepository
from .storage import dumps_json

try:
    import httpx
except ImportError:  # pragma: no cover - optional dependency
    httpx = None


@dataclass(slots=True)
class AuditIngestEndpoint:
    url: str
    auth_token: str | None = None
    timeout_seconds: float = 10.0

    def to_payload(self) -> dict[str, Any]:
        return asdict(self)


def _ensure_httpx() -> None:
    if httpx is None:
        raise RuntimeError("httpx is required for audit ingest over HTTP. Install it with `pip install httpx`.")


def _headers(endpoint: AuditIngestEndpoint) -> dict[str, str]:
    headers = {"Content-Type": "application/json"}
    if endpoint.auth_token:
        headers["Authorization"] = f"Bearer {endpoint.auth_token}"
    return headers


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _parse_datetime(value: Any) -> Any:
    if not isinstance(value, str):
        return value
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        return datetime.fromisoformat(normalized)
    except ValueError:
        return value


def _normalize_event_payload(value: Any) -> Any:
    if isinstance(value, dict):
        normalized: dict[str, Any] = {}
        for key, item in value.items():
            child = _normalize_event_payload(item)
            if key.endswith("_at"):
                child = _parse_datetime(child)
            normalized[key] = child
        return normalized
    if isinstance(value, list):
        return [_normalize_event_payload(item) for item in value]
    return value


class HttpAuditIngestRepository(AuditRepository):
    """
    AuditRepository implementation for child-agent services.

    Each audit write becomes an HTTP event sent to the main platform's ingest API.
    """

    def __init__(self, endpoint: AuditIngestEndpoint, producer_service: str = "child-agent-service"):
        self.endpoint = endpoint
        self.producer_service = producer_service

    async def insert_invocation_start(self, payload: dict[str, Any]) -> None:
        await self._post_event("invocation.start", payload)

    async def update_invocation_finish(self, run_id: str, payload: dict[str, Any]) -> None:
        await self._post_event("invocation.finish", {"run_id": run_id, "fields": payload})

    async def save_completed_invocation(self, payload: dict[str, Any]) -> None:
        await self._post_event("invocation.upsert", payload)

    async def insert_step(self, payload: dict[str, Any]) -> None:
        await self._post_event("step.upsert", payload)

    async def enqueue_eval(self, payload: dict[str, Any]) -> None:
        await self._post_event("eval.enqueue", payload)

    async def save_eval_result(self, payload: dict[str, Any]) -> None:
        await self._post_event("eval.result", payload)

    async def _post_event(self, event_type: str, payload: dict[str, Any]) -> None:
        _ensure_httpx()
        body = build_audit_event(
            event_type=event_type,
            payload=payload,
            producer_service=self.producer_service,
        )
        async with httpx.AsyncClient(timeout=self.endpoint.timeout_seconds) as client:
            response = await client.post(
                self.endpoint.url,
                content=dumps_json(body),
                headers=_headers(self.endpoint),
            )
            response.raise_for_status()


def build_audit_event(
    *,
    event_type: str,
    payload: dict[str, Any],
    producer_service: str,
    event_id: str | None = None,
    occurred_at: str | None = None,
) -> dict[str, Any]:
    trace_id = payload.get("trace_id")
    run_id = payload.get("run_id")
    if run_id is None and event_type == "invocation.finish":
        run_id = payload.get("run_id")
        if run_id is None:
            run_id = payload.get("fields", {}).get("run_id")
    if trace_id is None and event_type == "invocation.finish":
        trace_id = payload.get("fields", {}).get("trace_id")
    return {
        "event_id": event_id or uuid.uuid4().hex,
        "event_type": event_type,
        "trace_id": trace_id,
        "run_id": run_id,
        "producer_service": producer_service,
        "occurred_at": occurred_at or utc_now_iso(),
        "payload": payload,
    }


class AuditIngestService:
    """
    Central ingest handler that applies audit events to a concrete repository.
    """

    def __init__(self, repository: AuditRepository):
        self.repository = repository

    async def ingest_event(self, event: dict[str, Any]) -> None:
        event = _normalize_event_payload(event)
        should_process = await self.repository.register_ingest_event(event)
        if not should_process:
            return

        event_id = event["event_id"]
        event_type = event["event_type"]
        payload = event["payload"]

        try:
            await self._apply_event(event_type, payload)
            await self.repository.mark_ingest_event_status(event_id, "processed")
        except Exception as exc:
            await self.repository.mark_ingest_event_status(event_id, "failed", error_message=str(exc))
            await self.repository.upsert_dead_letter_event(event, error_message=str(exc))
            raise

    async def replay_event(self, event_id: str) -> dict[str, Any]:
        event = await self.repository.fetch_dead_letter_event(event_id)
        if not event:
            raise ValueError(f"Dead-letter event not found: {event_id}")

        event_type = event["event_type"]
        payload = event["payload"]

        try:
            await self._apply_event(event_type, payload)
            await self.repository.mark_ingest_event_status(event_id, "processed")
            await self.repository.resolve_dead_letter_event(event_id)
            return {"event_id": event_id, "status": "replayed"}
        except Exception as exc:
            await self.repository.mark_ingest_event_status(event_id, "failed", error_message=str(exc))
            await self.repository.mark_dead_letter_replay(event_id, "replay_failed", error_message=str(exc))
            raise

    async def _apply_event(self, event_type: str, payload: dict[str, Any]) -> None:
        if event_type == "invocation.start":
            await self.repository.insert_invocation_start(payload)
            return
        if event_type == "invocation.finish":
            await self.repository.update_invocation_finish(payload["run_id"], payload["fields"])
            return
        if event_type == "invocation.upsert":
            await self.repository.save_completed_invocation(payload)
            return
        if event_type == "step.upsert":
            await self.repository.insert_step(payload)
            return
        if event_type == "eval.enqueue":
            await self.repository.enqueue_eval(payload)
            return
        if event_type == "eval.result":
            await self.repository.save_eval_result(payload)
            return
        raise ValueError(f"Unsupported audit ingest event type: {event_type}")
