from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from enum import StrEnum
from typing import Any


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class RunStatus(StrEnum):
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    TIMEOUT = "timeout"
    CANCELLED = "cancelled"


class TaskStatus(StrEnum):
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    WAITING_USER = "waiting_user"
    WAITING_HUMAN = "waiting_human"
    SCHEDULED_PENDING = "scheduled_pending"
    CANCELLED = "cancelled"


class SessionStatus(StrEnum):
    ACTIVE = "active"
    IDLE = "idle"
    WAITING_USER = "waiting_user"
    WAITING_HUMAN = "waiting_human"
    COMPLETED = "completed"
    CLOSED = "closed"
    ARCHIVED = "archived"


class SessionCloseReason(StrEnum):
    USER_CLOSED = "user_closed"
    TIMEOUT_CLOSED = "timeout_closed"
    TASK_COMPLETED = "task_completed"
    SUPERSEDED = "superseded"
    SYSTEM_CLOSED = "system_closed"


@dataclass(slots=True)
class SessionRecord:
    session_id: str
    tenant_id: str | None
    user_id: str | None
    topic: str | None
    status: SessionStatus
    waiting_state: str | None
    current_task_id: str | None
    opened_at: datetime
    last_active_at: datetime
    closed_at: datetime | None = None
    close_reason: SessionCloseReason | None = None
    meta: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class TaskRecord:
    task_id: str
    session_id: str
    title: str | None
    task_type: str | None
    status: TaskStatus
    waiting_state: str | None
    started_at: datetime
    last_active_at: datetime
    completed_at: datetime | None = None
    closed_reason: str | None = None
    meta: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class RunRecord:
    run_id: str
    session_id: str | None
    task_id: str
    status: RunStatus
    started_at: datetime
    finished_at: datetime | None = None
    trigger_type: str | None = None


@dataclass(slots=True)
class SessionClosureDecision:
    should_close_session: bool
    next_session_status: SessionStatus
    close_reason: SessionCloseReason | None
    should_complete_task: bool
    next_task_status: TaskStatus
    note: str


def decide_lifecycle_transition(
    *,
    session: SessionRecord,
    task: TaskRecord,
    latest_run: RunRecord,
    pending_tasks: int = 0,
    pending_human_actions: int = 0,
    pending_user_actions: int = 0,
    pending_schedules: int = 0,
    user_explicitly_closed: bool = False,
    idle_timeout: timedelta = timedelta(hours=24),
    now: datetime | None = None,
) -> SessionClosureDecision:
    now = now or utc_now()

    if user_explicitly_closed:
        return SessionClosureDecision(
            should_close_session=True,
            next_session_status=SessionStatus.CLOSED,
            close_reason=SessionCloseReason.USER_CLOSED,
            should_complete_task=task.status not in {TaskStatus.SUCCESS, TaskStatus.CANCELLED},
            next_task_status=TaskStatus.CANCELLED if task.status == TaskStatus.RUNNING else task.status,
            note="User explicitly closed the session.",
        )

    if latest_run.status in {RunStatus.RUNNING}:
        return SessionClosureDecision(
            should_close_session=False,
            next_session_status=SessionStatus.ACTIVE,
            close_reason=None,
            should_complete_task=False,
            next_task_status=TaskStatus.RUNNING,
            note="Latest run is still in progress.",
        )

    if pending_human_actions > 0:
        return SessionClosureDecision(
            should_close_session=False,
            next_session_status=SessionStatus.WAITING_HUMAN,
            close_reason=None,
            should_complete_task=False,
            next_task_status=TaskStatus.WAITING_HUMAN,
            note="Task is waiting on human action.",
        )

    if pending_user_actions > 0:
        return SessionClosureDecision(
            should_close_session=False,
            next_session_status=SessionStatus.WAITING_USER,
            close_reason=None,
            should_complete_task=False,
            next_task_status=TaskStatus.WAITING_USER,
            note="Task is waiting on user input.",
        )

    if pending_schedules > 0:
        return SessionClosureDecision(
            should_close_session=False,
            next_session_status=SessionStatus.ACTIVE,
            close_reason=None,
            should_complete_task=False,
            next_task_status=TaskStatus.SCHEDULED_PENDING,
            note="Scheduled follow-up work is still pending.",
        )

    if pending_tasks > 0:
        return SessionClosureDecision(
            should_close_session=False,
            next_session_status=SessionStatus.ACTIVE,
            close_reason=None,
            should_complete_task=False,
            next_task_status=TaskStatus.RUNNING,
            note="There are unfinished sibling or child tasks.",
        )

    if latest_run.status == RunStatus.FAILED:
        return SessionClosureDecision(
            should_close_session=False,
            next_session_status=SessionStatus.ACTIVE,
            close_reason=None,
            should_complete_task=True,
            next_task_status=TaskStatus.FAILED,
            note="Latest run failed; keep session open for retry or follow-up.",
        )

    if latest_run.status in {RunStatus.SUCCESS, RunStatus.CANCELLED, RunStatus.TIMEOUT}:
        if latest_run.status == RunStatus.SUCCESS:
            if now - session.last_active_at >= idle_timeout:
                return SessionClosureDecision(
                    should_close_session=True,
                    next_session_status=SessionStatus.CLOSED,
                    close_reason=SessionCloseReason.TASK_COMPLETED,
                    should_complete_task=True,
                    next_task_status=TaskStatus.SUCCESS,
                    note="Task completed and session has been idle long enough to close.",
                )
            return SessionClosureDecision(
                should_close_session=False,
                next_session_status=SessionStatus.COMPLETED,
                close_reason=None,
                should_complete_task=True,
                next_task_status=TaskStatus.SUCCESS,
                note="Task completed, but session remains open for continued conversation.",
            )

        return SessionClosureDecision(
            should_close_session=False,
            next_session_status=SessionStatus.IDLE,
            close_reason=None,
            should_complete_task=True,
            next_task_status=TaskStatus.CANCELLED if latest_run.status == RunStatus.CANCELLED else TaskStatus.FAILED,
            note="Latest run ended without success; session remains idle for next action.",
        )

    if now - session.last_active_at >= idle_timeout:
        return SessionClosureDecision(
            should_close_session=True,
            next_session_status=SessionStatus.CLOSED,
            close_reason=SessionCloseReason.TIMEOUT_CLOSED,
            should_complete_task=False,
            next_task_status=task.status,
            note="Session timed out due to inactivity.",
        )

    return SessionClosureDecision(
        should_close_session=False,
        next_session_status=session.status,
        close_reason=None,
        should_complete_task=False,
        next_task_status=task.status,
        note="No lifecycle transition required.",
    )
