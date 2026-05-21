from __future__ import annotations

import uuid
from dataclasses import asdict
from datetime import timedelta
from typing import Any

from .lifecycle import (
    RunRecord,
    RunStatus,
    SessionCloseReason,
    SessionRecord,
    SessionStatus,
    TaskRecord,
    TaskStatus,
    decide_lifecycle_transition,
    utc_now,
)
from .storage import AuditRepository


def _as_session_record(payload: dict[str, Any]) -> SessionRecord:
    return SessionRecord(
        session_id=payload["session_id"],
        tenant_id=payload.get("tenant_id"),
        user_id=payload.get("user_id"),
        topic=payload.get("topic"),
        status=SessionStatus(payload["status"]),
        waiting_state=payload.get("waiting_state"),
        current_task_id=payload.get("current_task_id"),
        opened_at=payload["opened_at"],
        last_active_at=payload["last_active_at"],
        closed_at=payload.get("closed_at"),
        close_reason=SessionCloseReason(payload["close_reason"]) if payload.get("close_reason") else None,
        meta=payload.get("meta", {}),
    )


def _as_task_record(payload: dict[str, Any]) -> TaskRecord:
    return TaskRecord(
        task_id=payload["task_id"],
        session_id=payload["session_id"],
        title=payload.get("title"),
        task_type=payload.get("task_type"),
        status=TaskStatus(payload["status"]),
        waiting_state=payload.get("waiting_state"),
        started_at=payload["started_at"],
        last_active_at=payload["last_active_at"],
        completed_at=payload.get("completed_at"),
        closed_reason=payload.get("closed_reason"),
        meta=payload.get("meta", {}),
    )


class SessionManager:
    def __init__(self, repository: AuditRepository, idle_timeout: timedelta = timedelta(hours=24)):
        self.repository = repository
        self.idle_timeout = idle_timeout

    async def ensure_session_and_task(
        self,
        *,
        query: str,
        user_id: str,
        tenant_id: str,
        source_type: str,
        source_name: str | None = None,
        session_id: str | None = None,
        task_id: str | None = None,
        topic: str | None = None,
        task_type: str | None = None,
        assigned_agent: str | None = None,
    ) -> tuple[SessionRecord, TaskRecord]:
        now = utc_now()
        resolved_session_id = session_id or uuid.uuid4().hex
        existing_session = await self.repository.fetch_session(resolved_session_id)
        if existing_session:
            session = _as_session_record(existing_session)
            session.status = SessionStatus.ACTIVE
            session.last_active_at = now
            if topic and not session.topic:
                session.topic = topic
        else:
            session = SessionRecord(
                session_id=resolved_session_id,
                tenant_id=tenant_id,
                user_id=user_id,
                topic=topic or query[:120],
                status=SessionStatus.ACTIVE,
                waiting_state=None,
                current_task_id=task_id,
                opened_at=now,
                last_active_at=now,
                meta={"source_type": source_type, "source_name": source_name},
            )

        resolved_task_id = task_id or session.current_task_id or uuid.uuid4().hex
        existing_task = await self.repository.fetch_task(resolved_task_id)
        if existing_task:
            task = _as_task_record(existing_task)
            task.status = TaskStatus.RUNNING
            task.waiting_state = None
            task.last_active_at = now
        else:
            task = TaskRecord(
                task_id=resolved_task_id,
                session_id=resolved_session_id,
                title=query[:120],
                task_type=task_type,
                status=TaskStatus.RUNNING,
                waiting_state=None,
                started_at=now,
                last_active_at=now,
                meta={"assigned_agent": assigned_agent} if assigned_agent else {},
            )

        session.current_task_id = task.task_id
        await self.repository.upsert_session(self._session_payload(session, source_type=source_type, source_name=source_name))
        await self.repository.upsert_task(self._task_payload(task, tenant_id=tenant_id, user_id=user_id, assigned_agent=assigned_agent))
        return session, task

    async def close_session(
        self,
        *,
        session_id: str,
        closed_by: str | None = None,
        close_reason: SessionCloseReason = SessionCloseReason.USER_CLOSED,
    ) -> dict[str, Any]:
        row = await self.repository.fetch_session(session_id)
        if not row:
            raise ValueError(f"Session not found: {session_id}")
        session = _as_session_record(row)
        now = utc_now()
        session.status = SessionStatus.CLOSED
        session.closed_at = now
        session.last_active_at = now
        session.close_reason = close_reason
        if closed_by:
            session.meta = {**session.meta, "closed_by": closed_by}

        await self.repository.upsert_session(self._session_payload(session))
        return asdict(session)

    async def get_session_snapshot(self, session_id: str, task_limit: int = 200) -> dict[str, Any]:
        row = await self.repository.fetch_session(session_id)
        if not row:
            raise ValueError(f"Session not found: {session_id}")
        tasks = await self.repository.list_session_tasks(session_id, limit=task_limit)
        return {
            "session": row,
            "tasks": tasks,
        }

    async def list_sessions(
        self,
        *,
        status: str | None = None,
        tenant_id: str | None = None,
        user_id: str | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        rows = await self.repository.list_sessions(
            status=status,
            tenant_id=tenant_id,
            user_id=user_id,
            limit=limit,
            offset=offset,
        )
        return {
            "items": rows,
            "limit": limit,
            "offset": offset,
            "count": len(rows),
        }

    async def get_session_stats(
        self,
        *,
        tenant_id: str | None = None,
        user_id: str | None = None,
    ) -> dict[str, Any]:
        by_status = await self.repository.get_session_stats(tenant_id=tenant_id, user_id=user_id)
        total = sum(by_status.values())
        return {
            "total": total,
            "by_status": by_status,
        }

    async def list_tasks(
        self,
        *,
        status: str | None = None,
        tenant_id: str | None = None,
        user_id: str | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> dict[str, Any]:
        rows = await self.repository.list_tasks(
            status=status,
            tenant_id=tenant_id,
            user_id=user_id,
            limit=limit,
            offset=offset,
        )
        return {
            "items": rows,
            "limit": limit,
            "offset": offset,
            "count": len(rows),
        }

    async def get_task_stats(
        self,
        *,
        tenant_id: str | None = None,
        user_id: str | None = None,
    ) -> dict[str, Any]:
        by_status = await self.repository.get_task_stats(tenant_id=tenant_id, user_id=user_id)
        total = sum(by_status.values())
        completed = by_status.get(TaskStatus.SUCCESS.value, 0)
        failed = by_status.get(TaskStatus.FAILED.value, 0)
        running = by_status.get(TaskStatus.RUNNING.value, 0)
        completion_rate = round((completed / total) * 100, 2) if total else 0.0
        failure_rate = round((failed / total) * 100, 2) if total else 0.0
        return {
            "total": total,
            "running": running,
            "completed": completed,
            "failed": failed,
            "completion_rate": completion_rate,
            "failure_rate": failure_rate,
            "by_status": by_status,
        }

    async def finalize_run(
        self,
        *,
        session: SessionRecord,
        task: TaskRecord,
        run_id: str,
        run_status: str,
        trigger_type: str | None = None,
        user_explicitly_closed: bool = False,
    ) -> dict[str, Any]:
        now = utc_now()
        latest_run = RunRecord(
            run_id=run_id,
            session_id=session.session_id,
            task_id=task.task_id,
            status=RunStatus(run_status),
            started_at=task.last_active_at,
            finished_at=now,
            trigger_type=trigger_type,
        )
        pending_tasks = await self.repository.count_session_tasks(
            session.session_id,
            exclude_task_id=task.task_id,
            statuses=[
                TaskStatus.RUNNING.value,
                TaskStatus.WAITING_HUMAN.value,
                TaskStatus.WAITING_USER.value,
                TaskStatus.SCHEDULED_PENDING.value,
            ],
        )
        pending_human_actions = await self.repository.count_session_tasks(
            session.session_id,
            exclude_task_id=task.task_id,
            statuses=[TaskStatus.WAITING_HUMAN.value],
        )
        pending_user_actions = await self.repository.count_session_tasks(
            session.session_id,
            exclude_task_id=task.task_id,
            statuses=[TaskStatus.WAITING_USER.value],
        )

        decision = decide_lifecycle_transition(
            session=session,
            task=task,
            latest_run=latest_run,
            pending_tasks=pending_tasks,
            pending_human_actions=pending_human_actions,
            pending_user_actions=pending_user_actions,
            pending_schedules=0,
            user_explicitly_closed=user_explicitly_closed,
            idle_timeout=self.idle_timeout,
            now=now,
        )

        session.last_active_at = now
        session.status = decision.next_session_status
        session.waiting_state = (
            "waiting_user" if decision.next_session_status == SessionStatus.WAITING_USER
            else "waiting_human" if decision.next_session_status == SessionStatus.WAITING_HUMAN
            else None
        )
        if decision.should_close_session:
            session.closed_at = now
            session.close_reason = decision.close_reason

        task.status = decision.next_task_status
        task.last_active_at = now
        task.waiting_state = (
            "waiting_user" if decision.next_task_status == TaskStatus.WAITING_USER
            else "waiting_human" if decision.next_task_status == TaskStatus.WAITING_HUMAN
            else None
        )
        if decision.should_complete_task and decision.next_task_status in {
            TaskStatus.SUCCESS,
            TaskStatus.FAILED,
            TaskStatus.CANCELLED,
        }:
            task.completed_at = now
            task.closed_reason = decision.close_reason.value if decision.close_reason else None

        await self.repository.upsert_task(self._task_payload(task, tenant_id=session.tenant_id, user_id=session.user_id))
        await self.repository.upsert_session(self._session_payload(session))
        return {
            "session": asdict(session),
            "task": asdict(task),
            "decision": {
                "should_close_session": decision.should_close_session,
                "next_session_status": decision.next_session_status.value,
                "close_reason": decision.close_reason.value if decision.close_reason else None,
                "should_complete_task": decision.should_complete_task,
                "next_task_status": decision.next_task_status.value,
                "note": decision.note,
            },
        }

    @staticmethod
    def _session_payload(
        session: SessionRecord,
        *,
        source_type: str | None = None,
        source_name: str | None = None,
    ) -> dict[str, Any]:
        return {
            "session_id": session.session_id,
            "tenant_id": session.tenant_id,
            "user_id": session.user_id,
            "topic": session.topic,
            "status": session.status.value,
            "waiting_state": session.waiting_state,
            "current_task_id": session.current_task_id,
            "opened_at": session.opened_at,
            "last_active_at": session.last_active_at,
            "closed_at": session.closed_at,
            "close_reason": session.close_reason.value if session.close_reason else None,
            "source_type": source_type or session.meta.get("source_type"),
            "source_name": source_name or session.meta.get("source_name"),
            "meta": session.meta,
        }

    @staticmethod
    def _task_payload(
        task: TaskRecord,
        *,
        tenant_id: str | None,
        user_id: str | None,
        assigned_agent: str | None = None,
    ) -> dict[str, Any]:
        meta = dict(task.meta)
        if assigned_agent:
            meta["assigned_agent"] = assigned_agent
        return {
            "task_id": task.task_id,
            "session_id": task.session_id,
            "parent_task_id": None,
            "tenant_id": tenant_id,
            "user_id": user_id,
            "title": task.title,
            "task_type": task.task_type,
            "status": task.status.value,
            "waiting_state": task.waiting_state,
            "priority": 100,
            "requested_by": user_id,
            "assigned_agent": meta.get("assigned_agent"),
            "started_at": task.started_at,
            "last_active_at": task.last_active_at,
            "completed_at": task.completed_at,
            "closed_reason": task.closed_reason,
            "meta": meta,
        }
