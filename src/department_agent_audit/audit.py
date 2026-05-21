from __future__ import annotations

import time
import uuid
from contextlib import asynccontextmanager
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, AsyncIterator, Awaitable, Callable

from .storage import AuditRepository


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _short_text(value: Any, limit: int = 500) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    if len(text) <= limit:
        return text
    return f"{text[: limit - 3]}..."


@dataclass(slots=True)
class AuditContext:
    session_id: str | None
    trace_id: str
    task_id: str
    request_id: str
    run_id: str
    schedule_id: str | None = None
    parent_run_id: str | None = None
    source_type: str = "api"
    source_name: str | None = None
    trigger_type: str = "manual"
    workflow_name: str | None = None
    scenario_name: str | None = None
    user_id: str | None = None
    tenant_id: str | None = None
    tags: list[str] = field(default_factory=list)
    meta: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def new(
        cls,
        *,
        session_id: str | None = None,
        source_type: str,
        trigger_type: str,
        agent_name: str,
        source_name: str | None = None,
        workflow_name: str | None = None,
        scenario_name: str | None = None,
        user_id: str | None = None,
        tenant_id: str | None = None,
        schedule_id: str | None = None,
        parent_run_id: str | None = None,
        tags: list[str] | None = None,
        meta: dict[str, Any] | None = None,
    ) -> tuple["AuditContext", str]:
        trace_id = uuid.uuid4().hex
        context = cls(
            session_id=session_id,
            trace_id=trace_id,
            task_id=uuid.uuid4().hex,
            request_id=uuid.uuid4().hex,
            run_id=uuid.uuid4().hex,
            schedule_id=schedule_id,
            parent_run_id=parent_run_id,
            source_type=source_type,
            source_name=source_name,
            trigger_type=trigger_type,
            workflow_name=workflow_name,
            scenario_name=scenario_name,
            user_id=user_id,
            tenant_id=tenant_id,
            tags=tags or [],
            meta=meta or {},
        )
        return context, agent_name

    @classmethod
    def from_parent(
        cls,
        parent_payload: dict[str, Any],
        *,
        agent_name: str,
        source_type: str,
        trigger_type: str,
        source_name: str | None = None,
        workflow_name: str | None = None,
        scenario_name: str | None = None,
        tags: list[str] | None = None,
        meta: dict[str, Any] | None = None,
    ) -> tuple["AuditContext", str]:
        context = cls(
            session_id=parent_payload.get("session_id"),
            trace_id=parent_payload["trace_id"],
            task_id=parent_payload["task_id"],
            request_id=parent_payload["request_id"],
            run_id=uuid.uuid4().hex,
            schedule_id=parent_payload.get("schedule_id"),
            parent_run_id=parent_payload["parent_run_id"],
            source_type=source_type,
            source_name=source_name or parent_payload.get("source_name"),
            trigger_type=trigger_type,
            workflow_name=workflow_name or parent_payload.get("workflow_name"),
            scenario_name=scenario_name or parent_payload.get("scenario_name"),
            user_id=parent_payload.get("user_id"),
            tenant_id=parent_payload.get("tenant_id"),
            tags=tags or list(parent_payload.get("tags", [])),
            meta={**parent_payload.get("meta", {}), **(meta or {})},
        )
        return context, agent_name

    def to_remote_parent_payload(self) -> dict[str, Any]:
        return {
            "session_id": self.session_id,
            "trace_id": self.trace_id,
            "task_id": self.task_id,
            "request_id": self.request_id,
            "schedule_id": self.schedule_id,
            "parent_run_id": self.run_id,
            "source_type": self.source_type,
            "source_name": self.source_name,
            "trigger_type": self.trigger_type,
            "workflow_name": self.workflow_name,
            "scenario_name": self.scenario_name,
            "user_id": self.user_id,
            "tenant_id": self.tenant_id,
            "tags": list(self.tags),
            "meta": dict(self.meta),
        }


@dataclass(slots=True)
class InvocationRecord:
    agent_name: str
    status: str
    system_success: bool
    execution_success: bool
    business_success: bool | None
    input_summary: str
    output_summary: str
    input_payload: dict[str, Any]
    output_payload: dict[str, Any]
    error_code: str | None
    error_message: str | None
    started_at: datetime
    finished_at: datetime | None
    latency_ms: int | None
    prompt_tokens: int | None = None
    completion_tokens: int | None = None
    total_tokens: int | None = None
    estimated_cost: float | None = None


@dataclass(slots=True)
class StepRecord:
    step_id: str
    step_type: str
    step_name: str
    sequence_no: int
    target_name: str | None
    status: str
    success: bool
    input_summary: str
    output_summary: str
    input_payload: dict[str, Any]
    output_payload: dict[str, Any]
    error_code: str | None
    error_message: str | None
    started_at: datetime
    finished_at: datetime | None
    latency_ms: int | None
    token_usage: dict[str, Any] = field(default_factory=dict)
    meta: dict[str, Any] = field(default_factory=dict)
    parent_step_id: str | None = None


class AuditLogger:
    def __init__(self, repository: AuditRepository):
        self.repository = repository

    async def start_invocation(
        self,
        context: AuditContext,
        agent_name: str,
        input_payload: dict[str, Any],
    ) -> None:
        payload = {
            **asdict(context),
            "agent_name": agent_name,
            "status": "running",
            "input_summary": _short_text(input_payload),
            "input_payload": input_payload,
            "started_at": utc_now(),
        }
        await self.repository.insert_invocation_start(payload)

    async def finish_invocation(self, context: AuditContext, record: InvocationRecord) -> None:
        payload = {
            "session_id": context.session_id,
            "status": record.status,
            "system_success": record.system_success,
            "execution_success": record.execution_success,
            "business_success": record.business_success,
            "output_summary": record.output_summary,
            "output_payload": record.output_payload,
            "error_code": record.error_code,
            "error_message": record.error_message,
            "finished_at": record.finished_at,
            "latency_ms": record.latency_ms,
            "prompt_tokens": record.prompt_tokens,
            "completion_tokens": record.completion_tokens,
            "total_tokens": record.total_tokens,
            "estimated_cost": record.estimated_cost,
        }
        await self.repository.update_invocation_finish(context.run_id, payload)

    async def save_completed_invocation(self, payload: dict[str, Any]) -> None:
        await self.repository.save_completed_invocation(payload)

    async def log_step(self, context: AuditContext, record: StepRecord) -> None:
        payload = {
            "trace_id": context.trace_id,
            "run_id": context.run_id,
            **asdict(record),
        }
        await self.repository.insert_step(payload)

    async def enqueue_eval(
        self,
        context: AuditContext,
        *,
        agent_name: str,
        priority: int,
        payload: dict[str, Any],
    ) -> None:
        queue_payload = {
            "queue_item_id": uuid.uuid4().hex,
            "trace_id": context.trace_id,
            "run_id": context.run_id,
            "priority": priority,
            "status": "pending",
            "attempts": 0,
            "available_at": utc_now(),
            "payload": {
                "agent_name": agent_name,
                "context": asdict(context),
                **payload,
            },
        }
        await self.repository.enqueue_eval(queue_payload)

    async def ingest_remote_audit_bundle(self, bundle: dict[str, Any]) -> None:
        for invocation in bundle.get("invocations", []):
            await self.save_completed_invocation(invocation)
        for step in bundle.get("steps", []):
            await self.repository.insert_step(step)

    @asynccontextmanager
    async def tool_step(
        self,
        context: AuditContext,
        *,
        step_name: str,
        sequence_no: int,
        target_name: str | None,
        input_payload: dict[str, Any],
        step_type: str = "tool_call",
    ) -> AsyncIterator[Callable[[dict[str, Any]], Awaitable[None]]]:
        started_at = utc_now()
        step_id = uuid.uuid4().hex
        start_monotonic = time.perf_counter()

        async def _finish(
            output_payload: dict[str, Any],
            success: bool = True,
            status: str = "success",
            error_code: str | None = None,
            error_message: str | None = None,
            token_usage: dict[str, Any] | None = None,
            meta: dict[str, Any] | None = None,
        ) -> None:
            finished_at = utc_now()
            record = StepRecord(
                step_id=step_id,
                step_type=step_type,
                step_name=step_name,
                sequence_no=sequence_no,
                target_name=target_name,
                status=status,
                success=success,
                input_summary=_short_text(input_payload),
                output_summary=_short_text(output_payload),
                input_payload=input_payload,
                output_payload=output_payload,
                error_code=error_code,
                error_message=error_message,
                started_at=started_at,
                finished_at=finished_at,
                latency_ms=int((time.perf_counter() - start_monotonic) * 1000),
                token_usage=token_usage or {},
                meta=meta or {},
            )
            await self.log_step(context, record)

        try:
            yield _finish
        except Exception as exc:
            await _finish(
                output_payload={},
                success=False,
                status="failed",
                error_code=type(exc).__name__,
                error_message=str(exc),
            )
            raise

    async def invoke_with_audit(
        self,
        context: AuditContext,
        *,
        agent_name: str,
        input_payload: dict[str, Any],
        agent_call: Callable[[], Awaitable[dict[str, Any]]],
        eval_priority: int = 100,
    ) -> dict[str, Any]:
        start_monotonic = time.perf_counter()
        started_at = utc_now()
        await self.start_invocation(context, agent_name, input_payload)

        try:
            output_payload = await agent_call()
            finished_at = utc_now()
            record = InvocationRecord(
                agent_name=agent_name,
                status="success",
                system_success=True,
                execution_success=True,
                business_success=None,
                input_summary=_short_text(input_payload),
                output_summary=_short_text(output_payload),
                input_payload=input_payload,
                output_payload=output_payload,
                error_code=None,
                error_message=None,
                started_at=started_at,
                finished_at=finished_at,
                latency_ms=int((time.perf_counter() - start_monotonic) * 1000),
                prompt_tokens=output_payload.get("prompt_tokens"),
                completion_tokens=output_payload.get("completion_tokens"),
                total_tokens=output_payload.get("total_tokens"),
                estimated_cost=output_payload.get("estimated_cost"),
            )
            await self.finish_invocation(context, record)
            await self.enqueue_eval(
                context,
                agent_name=agent_name,
                priority=eval_priority,
                payload={
                    "input_payload": input_payload,
                    "output_payload": output_payload,
                },
            )
            return output_payload
        except Exception as exc:
            finished_at = utc_now()
            record = InvocationRecord(
                agent_name=agent_name,
                status="failed",
                system_success=False,
                execution_success=False,
                business_success=False,
                input_summary=_short_text(input_payload),
                output_summary="",
                input_payload=input_payload,
                output_payload={},
                error_code=type(exc).__name__,
                error_message=str(exc),
                started_at=started_at,
                finished_at=finished_at,
                latency_ms=int((time.perf_counter() - start_monotonic) * 1000),
            )
            await self.finish_invocation(context, record)
            raise
