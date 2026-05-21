from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from datetime import datetime
from typing import Any


def _json_default(value: Any) -> Any:
    if isinstance(value, datetime):
        return value.isoformat()
    if is_dataclass(value):
        return asdict(value)
    raise TypeError(f"Unsupported value for JSON serialization: {type(value)!r}")


def dumps_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=True, default=_json_default)


class AuditRepository:
    """
    Minimal storage abstraction.

    Swap these stubs with real inserts through SQLAlchemy, asyncpg, psycopg,
    or your internal data access layer.
    """

    async def insert_invocation_start(self, payload: dict[str, Any]) -> None:
        del payload

    async def update_invocation_finish(self, run_id: str, payload: dict[str, Any]) -> None:
        del run_id, payload

    async def save_completed_invocation(self, payload: dict[str, Any]) -> None:
        del payload

    async def insert_step(self, payload: dict[str, Any]) -> None:
        del payload

    async def enqueue_eval(self, payload: dict[str, Any]) -> None:
        del payload

    async def save_eval_result(self, payload: dict[str, Any]) -> None:
        del payload

    async def register_ingest_event(self, event: dict[str, Any]) -> bool:
        del event
        return True

    async def mark_ingest_event_status(self, event_id: str, status: str, error_message: str | None = None) -> None:
        del event_id, status, error_message

    async def upsert_dead_letter_event(self, event: dict[str, Any], error_message: str) -> None:
        del event, error_message

    async def resolve_dead_letter_event(self, event_id: str) -> None:
        del event_id

    async def mark_dead_letter_replay(self, event_id: str, status: str, error_message: str | None = None) -> None:
        del event_id, status, error_message

    async def fetch_dead_letter_event(self, event_id: str) -> dict[str, Any] | None:
        del event_id
        return None

    async def list_dead_letter_events(self, status: str = "open", limit: int = 100) -> list[dict[str, Any]]:
        del status, limit
        return []

    async def fetch_trace_view(self, trace_id: str) -> dict[str, Any]:
        del trace_id
        return {"invocations": [], "steps": [], "eval_results": [], "ingest_events": []}

    async def upsert_session(self, payload: dict[str, Any]) -> None:
        del payload

    async def fetch_session(self, session_id: str) -> dict[str, Any] | None:
        del session_id
        return None

    async def upsert_task(self, payload: dict[str, Any]) -> None:
        del payload

    async def fetch_task(self, task_id: str) -> dict[str, Any] | None:
        del task_id
        return None

    async def count_session_tasks(
        self,
        session_id: str,
        *,
        exclude_task_id: str | None = None,
        statuses: list[str] | None = None,
    ) -> int:
        del session_id, exclude_task_id, statuses
        return 0

    async def list_session_tasks(self, session_id: str, limit: int = 200) -> list[dict[str, Any]]:
        del session_id, limit
        return []

    async def list_sessions(
        self,
        *,
        status: str | None = None,
        tenant_id: str | None = None,
        user_id: str | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[dict[str, Any]]:
        del status, tenant_id, user_id, limit, offset
        return []

    async def get_session_stats(
        self,
        *,
        tenant_id: str | None = None,
        user_id: str | None = None,
    ) -> dict[str, int]:
        del tenant_id, user_id
        return {}

    async def fetch_next_eval_queue_item(self, worker_id: str) -> dict[str, Any] | None:
        del worker_id
        return None

    async def mark_eval_queue_item(self, queue_item_id: str, status: str, error_message: str | None = None) -> None:
        del queue_item_id, status, error_message


class CollectingAuditRepository(AuditRepository):
    """
    In-memory repository for child-agent services that need to return audit bundles
    to the main platform instead of writing directly into the central database.
    """

    def __init__(self) -> None:
        self.invocations: dict[str, dict[str, Any]] = {}
        self.steps: list[dict[str, Any]] = []
        self.eval_queue: list[dict[str, Any]] = []
        self.eval_results: list[dict[str, Any]] = []

    async def insert_invocation_start(self, payload: dict[str, Any]) -> None:
        self.invocations[payload["run_id"]] = dict(payload)

    async def update_invocation_finish(self, run_id: str, payload: dict[str, Any]) -> None:
        existing = self.invocations.setdefault(run_id, {"run_id": run_id})
        existing.update(payload)

    async def save_completed_invocation(self, payload: dict[str, Any]) -> None:
        self.invocations[payload["run_id"]] = dict(payload)

    async def insert_step(self, payload: dict[str, Any]) -> None:
        self.steps.append(dict(payload))

    async def enqueue_eval(self, payload: dict[str, Any]) -> None:
        self.eval_queue.append(dict(payload))

    async def save_eval_result(self, payload: dict[str, Any]) -> None:
        self.eval_results.append(dict(payload))

    async def register_ingest_event(self, event: dict[str, Any]) -> bool:
        return True

    async def mark_ingest_event_status(self, event_id: str, status: str, error_message: str | None = None) -> None:
        del event_id, status, error_message

    async def upsert_dead_letter_event(self, event: dict[str, Any], error_message: str) -> None:
        del event, error_message

    async def resolve_dead_letter_event(self, event_id: str) -> None:
        del event_id

    async def mark_dead_letter_replay(self, event_id: str, status: str, error_message: str | None = None) -> None:
        del event_id, status, error_message

    async def fetch_dead_letter_event(self, event_id: str) -> dict[str, Any] | None:
        del event_id
        return None

    async def list_dead_letter_events(self, status: str = "open", limit: int = 100) -> list[dict[str, Any]]:
        del status, limit
        return []

    async def upsert_session(self, payload: dict[str, Any]) -> None:
        self.invocations.setdefault("__sessions__", {})
        self.invocations["__sessions__"][payload["session_id"]] = dict(payload)

    async def fetch_session(self, session_id: str) -> dict[str, Any] | None:
        sessions = self.invocations.get("__sessions__", {})
        value = sessions.get(session_id)
        return dict(value) if value else None

    async def upsert_task(self, payload: dict[str, Any]) -> None:
        self.invocations.setdefault("__tasks__", {})
        self.invocations["__tasks__"][payload["task_id"]] = dict(payload)

    async def fetch_task(self, task_id: str) -> dict[str, Any] | None:
        tasks = self.invocations.get("__tasks__", {})
        value = tasks.get(task_id)
        return dict(value) if value else None

    async def count_session_tasks(
        self,
        session_id: str,
        *,
        exclude_task_id: str | None = None,
        statuses: list[str] | None = None,
    ) -> int:
        tasks = self.invocations.get("__tasks__", {}).values()
        count = 0
        for task in tasks:
            if task["session_id"] != session_id:
                continue
            if exclude_task_id and task["task_id"] == exclude_task_id:
                continue
            if statuses and task["status"] not in statuses:
                continue
            count += 1
        return count

    async def list_session_tasks(self, session_id: str, limit: int = 200) -> list[dict[str, Any]]:
        tasks = self.invocations.get("__tasks__", {}).values()
        rows = [dict(task) for task in tasks if task["session_id"] == session_id]
        rows.sort(key=lambda item: item.get("last_active_at"), reverse=True)
        return rows[:limit]

    async def list_sessions(
        self,
        *,
        status: str | None = None,
        tenant_id: str | None = None,
        user_id: str | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[dict[str, Any]]:
        sessions = self.invocations.get("__sessions__", {}).values()
        rows = [dict(item) for item in sessions]
        if status:
            rows = [row for row in rows if row.get("status") == status]
        if tenant_id:
            rows = [row for row in rows if row.get("tenant_id") == tenant_id]
        if user_id:
            rows = [row for row in rows if row.get("user_id") == user_id]
        rows.sort(key=lambda item: item.get("last_active_at"), reverse=True)
        return rows[offset : offset + limit]

    async def get_session_stats(
        self,
        *,
        tenant_id: str | None = None,
        user_id: str | None = None,
    ) -> dict[str, int]:
        sessions = self.invocations.get("__sessions__", {}).values()
        rows = [dict(item) for item in sessions]
        if tenant_id:
            rows = [row for row in rows if row.get("tenant_id") == tenant_id]
        if user_id:
            rows = [row for row in rows if row.get("user_id") == user_id]
        stats: dict[str, int] = {}
        for row in rows:
            status = row.get("status", "unknown")
            stats[status] = stats.get(status, 0) + 1
        return stats

    def export_run_bundle(self, run_id: str) -> dict[str, Any]:
        invocation = dict(self.invocations[run_id])
        steps = [dict(step) for step in self.steps if step["run_id"] == run_id]
        return {
            "invocations": [invocation],
            "steps": steps,
        }
