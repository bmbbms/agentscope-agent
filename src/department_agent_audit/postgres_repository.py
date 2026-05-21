from __future__ import annotations

from typing import Any

from .storage import AuditRepository

try:
    import asyncpg
except ImportError:  # pragma: no cover - optional dependency
    asyncpg = None


def _ensure_asyncpg() -> None:
    if asyncpg is None:
        raise RuntimeError(
            "asyncpg is required for PostgresAuditRepository. Install it with `pip install asyncpg`."
        )


class PostgresAuditRepository(AuditRepository):
    def __init__(self, pool: "asyncpg.Pool"):
        _ensure_asyncpg()
        self.pool = pool

    @classmethod
    async def create(cls, dsn: str, *, min_size: int = 1, max_size: int = 10) -> "PostgresAuditRepository":
        _ensure_asyncpg()
        pool = await asyncpg.create_pool(dsn=dsn, min_size=min_size, max_size=max_size)
        return cls(pool)

    async def close(self) -> None:
        await self.pool.close()

    async def insert_invocation_start(self, payload: dict[str, Any]) -> None:
        sql = """
        insert into agent_invocation_log (
            session_id, trace_id, task_id, request_id, run_id, schedule_id, parent_run_id,
            source_type, source_name, trigger_type, agent_name, workflow_name, scenario_name,
            user_id, tenant_id, input_summary, input_payload, status, started_at, tags, meta
        ) values (
            $1, $2, $3, $4, $5, $6, $7,
            $8, $9, $10, $11, $12, $13,
            $14, $15, $16, $17::jsonb, $18, $19, $20::jsonb, $21::jsonb
        )
        """
        await self.pool.execute(
            sql,
            payload.get("session_id"),
            payload["trace_id"],
            payload["task_id"],
            payload["request_id"],
            payload["run_id"],
            payload.get("schedule_id"),
            payload.get("parent_run_id"),
            payload["source_type"],
            payload.get("source_name"),
            payload["trigger_type"],
            payload["agent_name"],
            payload.get("workflow_name"),
            payload.get("scenario_name"),
            payload.get("user_id"),
            payload.get("tenant_id"),
            payload.get("input_summary"),
            payload.get("input_payload", {}),
            payload["status"],
            payload["started_at"],
            payload.get("tags", []),
            payload.get("meta", {}),
        )

    async def update_invocation_finish(self, run_id: str, payload: dict[str, Any]) -> None:
        sql = """
        update agent_invocation_log
        set
            session_id = $2,
            status = $3,
            system_success = $4,
            execution_success = $5,
            business_success = $6,
            output_summary = $7,
            output_payload = $8::jsonb,
            error_code = $9,
            error_message = $10,
            finished_at = $11,
            latency_ms = $12,
            prompt_tokens = $13,
            completion_tokens = $14,
            total_tokens = $15,
            estimated_cost = $16
        where run_id = $1
        """
        await self.pool.execute(
            sql,
            run_id,
            payload.get("session_id"),
            payload["status"],
            payload["system_success"],
            payload["execution_success"],
            payload.get("business_success"),
            payload.get("output_summary"),
            payload.get("output_payload", {}),
            payload.get("error_code"),
            payload.get("error_message"),
            payload.get("finished_at"),
            payload.get("latency_ms"),
            payload.get("prompt_tokens"),
            payload.get("completion_tokens"),
            payload.get("total_tokens"),
            payload.get("estimated_cost"),
        )

    async def save_completed_invocation(self, payload: dict[str, Any]) -> None:
        sql = """
        insert into agent_invocation_log (
            session_id, trace_id, task_id, request_id, run_id, schedule_id, parent_run_id,
            source_type, source_name, trigger_type, agent_name, workflow_name, scenario_name,
            user_id, tenant_id, input_summary, output_summary, input_payload, output_payload,
            status, system_success, execution_success, business_success, error_code,
            error_message, started_at, finished_at, latency_ms, prompt_tokens,
            completion_tokens, total_tokens, estimated_cost, tags, meta
        ) values (
            $1, $2, $3, $4, $5, $6, $7,
            $8, $9, $10, $11, $12, $13,
            $14, $15, $16, $17, $18::jsonb, $19::jsonb,
            $20, $21, $22, $23, $24,
            $25, $26, $27, $28, $29,
            $30, $31, $32, $33::jsonb, $34::jsonb
        )
        on conflict (run_id) do update set
            session_id = excluded.session_id,
            trace_id = excluded.trace_id,
            task_id = excluded.task_id,
            request_id = excluded.request_id,
            schedule_id = excluded.schedule_id,
            parent_run_id = excluded.parent_run_id,
            source_type = excluded.source_type,
            source_name = excluded.source_name,
            trigger_type = excluded.trigger_type,
            agent_name = excluded.agent_name,
            workflow_name = excluded.workflow_name,
            scenario_name = excluded.scenario_name,
            user_id = excluded.user_id,
            tenant_id = excluded.tenant_id,
            input_summary = excluded.input_summary,
            output_summary = excluded.output_summary,
            input_payload = excluded.input_payload,
            output_payload = excluded.output_payload,
            status = excluded.status,
            system_success = excluded.system_success,
            execution_success = excluded.execution_success,
            business_success = excluded.business_success,
            error_code = excluded.error_code,
            error_message = excluded.error_message,
            started_at = excluded.started_at,
            finished_at = excluded.finished_at,
            latency_ms = excluded.latency_ms,
            prompt_tokens = excluded.prompt_tokens,
            completion_tokens = excluded.completion_tokens,
            total_tokens = excluded.total_tokens,
            estimated_cost = excluded.estimated_cost,
            tags = excluded.tags,
            meta = excluded.meta
        """
        await self.pool.execute(
            sql,
            payload.get("session_id"),
            payload["trace_id"],
            payload["task_id"],
            payload["request_id"],
            payload["run_id"],
            payload.get("schedule_id"),
            payload.get("parent_run_id"),
            payload["source_type"],
            payload.get("source_name"),
            payload["trigger_type"],
            payload["agent_name"],
            payload.get("workflow_name"),
            payload.get("scenario_name"),
            payload.get("user_id"),
            payload.get("tenant_id"),
            payload.get("input_summary"),
            payload.get("output_summary"),
            payload.get("input_payload", {}),
            payload.get("output_payload", {}),
            payload["status"],
            payload["system_success"],
            payload["execution_success"],
            payload.get("business_success"),
            payload.get("error_code"),
            payload.get("error_message"),
            payload["started_at"],
            payload.get("finished_at"),
            payload.get("latency_ms"),
            payload.get("prompt_tokens"),
            payload.get("completion_tokens"),
            payload.get("total_tokens"),
            payload.get("estimated_cost"),
            payload.get("tags", []),
            payload.get("meta", {}),
        )

    async def insert_step(self, payload: dict[str, Any]) -> None:
        sql = """
        insert into agent_step_log (
            trace_id, run_id, step_id, parent_step_id, step_type, step_name, sequence_no,
            target_name, input_summary, output_summary, input_payload, output_payload,
            status, success, error_code, error_message, started_at, finished_at,
            latency_ms, token_usage, meta
        ) values (
            $1, $2, $3, $4, $5, $6, $7,
            $8, $9, $10, $11::jsonb, $12::jsonb,
            $13, $14, $15, $16, $17, $18,
            $19, $20::jsonb, $21::jsonb
        )
        on conflict (step_id) do update set
            trace_id = excluded.trace_id,
            run_id = excluded.run_id,
            parent_step_id = excluded.parent_step_id,
            step_type = excluded.step_type,
            step_name = excluded.step_name,
            sequence_no = excluded.sequence_no,
            target_name = excluded.target_name,
            input_summary = excluded.input_summary,
            output_summary = excluded.output_summary,
            input_payload = excluded.input_payload,
            output_payload = excluded.output_payload,
            status = excluded.status,
            success = excluded.success,
            error_code = excluded.error_code,
            error_message = excluded.error_message,
            started_at = excluded.started_at,
            finished_at = excluded.finished_at,
            latency_ms = excluded.latency_ms,
            token_usage = excluded.token_usage,
            meta = excluded.meta
        """
        await self.pool.execute(
            sql,
            payload["trace_id"],
            payload["run_id"],
            payload["step_id"],
            payload.get("parent_step_id"),
            payload["step_type"],
            payload["step_name"],
            payload["sequence_no"],
            payload.get("target_name"),
            payload.get("input_summary"),
            payload.get("output_summary"),
            payload.get("input_payload", {}),
            payload.get("output_payload", {}),
            payload["status"],
            payload["success"],
            payload.get("error_code"),
            payload.get("error_message"),
            payload["started_at"],
            payload.get("finished_at"),
            payload.get("latency_ms"),
            payload.get("token_usage", {}),
            payload.get("meta", {}),
        )

    async def enqueue_eval(self, payload: dict[str, Any]) -> None:
        sql = """
        insert into agent_eval_queue (
            queue_item_id, trace_id, run_id, priority, status, attempts,
            available_at, payload
        ) values (
            $1, $2, $3, $4, $5, $6,
            $7, $8::jsonb
        )
        """
        await self.pool.execute(
            sql,
            payload["queue_item_id"],
            payload["trace_id"],
            payload["run_id"],
            payload["priority"],
            payload["status"],
            payload["attempts"],
            payload["available_at"],
            payload["payload"],
        )

    async def save_eval_result(self, payload: dict[str, Any]) -> None:
        sql = """
        insert into agent_eval_result (
            trace_id, run_id, eval_id, evaluator_name, evaluator_version, eval_mode,
            rule_passed, llm_passed, overall_passed, score_total, score_task_completion,
            score_factual_grounding, score_metric_consistency, score_actionability,
            score_safety_compliance, issue_tags, findings, suggestions, evidence,
            raw_judge, evaluated_at, latency_ms
        ) values (
            $1, $2, $3, $4, $5, $6,
            $7, $8, $9, $10, $11,
            $12, $13, $14,
            $15, $16::jsonb, $17::jsonb, $18::jsonb, $19::jsonb,
            $20::jsonb, $21, $22
        )
        """
        await self.pool.execute(
            sql,
            payload["trace_id"],
            payload["run_id"],
            payload["eval_id"],
            payload["evaluator_name"],
            payload.get("evaluator_version"),
            payload["eval_mode"],
            payload.get("rule_passed"),
            payload.get("llm_passed"),
            payload["overall_passed"],
            payload.get("score_total"),
            payload.get("score_task_completion"),
            payload.get("score_factual_grounding"),
            payload.get("score_metric_consistency"),
            payload.get("score_actionability"),
            payload.get("score_safety_compliance"),
            payload.get("issue_tags", []),
            payload.get("findings", []),
            payload.get("suggestions", []),
            payload.get("evidence", []),
            payload.get("raw_judge", {}),
            payload["evaluated_at"],
            payload["latency_ms"],
        )

    async def register_ingest_event(self, event: dict[str, Any]) -> bool:
        sql = """
        insert into audit_ingest_event (
            event_id, trace_id, run_id, event_type, producer_service,
            occurred_at, status, payload
        ) values (
            $1, $2, $3, $4, $5,
            $6, 'received', $7::jsonb
        )
        on conflict (event_id) do nothing
        """
        result = await self.pool.execute(
            sql,
            event["event_id"],
            event.get("trace_id"),
            event.get("run_id"),
            event["event_type"],
            event.get("producer_service"),
            event["occurred_at"],
            event["payload"],
        )
        return result != "INSERT 0 0"

    async def mark_ingest_event_status(self, event_id: str, status: str, error_message: str | None = None) -> None:
        sql = """
        update audit_ingest_event
        set status = $2, error_message = $3
        where event_id = $1
        """
        await self.pool.execute(sql, event_id, status, error_message)

    async def upsert_dead_letter_event(self, event: dict[str, Any], error_message: str) -> None:
        sql = """
        insert into audit_ingest_dead_letter (
            event_id, trace_id, run_id, event_type, producer_service,
            occurred_at, status, payload, error_message
        ) values (
            $1, $2, $3, $4, $5,
            $6, 'open', $7::jsonb, $8
        )
        on conflict (event_id) do update set
            trace_id = excluded.trace_id,
            run_id = excluded.run_id,
            event_type = excluded.event_type,
            producer_service = excluded.producer_service,
            occurred_at = excluded.occurred_at,
            failed_at = now(),
            status = 'open',
            payload = excluded.payload,
            error_message = excluded.error_message
        """
        await self.pool.execute(
            sql,
            event["event_id"],
            event.get("trace_id"),
            event.get("run_id"),
            event["event_type"],
            event.get("producer_service"),
            event["occurred_at"],
            event["payload"],
            error_message,
        )

    async def resolve_dead_letter_event(self, event_id: str) -> None:
        sql = """
        update audit_ingest_dead_letter
        set
            status = 'resolved',
            resolved_at = now(),
            last_replayed_at = now(),
            replay_count = replay_count + 1,
            error_message = null
        where event_id = $1
        """
        await self.pool.execute(sql, event_id)

    async def mark_dead_letter_replay(self, event_id: str, status: str, error_message: str | None = None) -> None:
        sql = """
        update audit_ingest_dead_letter
        set
            status = $2,
            replay_count = replay_count + 1,
            last_replayed_at = now(),
            error_message = $3
        where event_id = $1
        """
        await self.pool.execute(sql, event_id, status, error_message)

    async def fetch_dead_letter_event(self, event_id: str) -> dict[str, Any] | None:
        sql = """
        select
            event_id, trace_id, run_id, event_type, producer_service,
            occurred_at, payload, error_message, status, replay_count,
            last_replayed_at, resolved_at, failed_at
        from audit_ingest_dead_letter
        where event_id = $1
        """
        row = await self.pool.fetchrow(sql, event_id)
        return dict(row) if row else None

    async def list_dead_letter_events(self, status: str = "open", limit: int = 100) -> list[dict[str, Any]]:
        sql = """
        select
            event_id, trace_id, run_id, event_type, producer_service,
            occurred_at, failed_at, status, replay_count,
            last_replayed_at, resolved_at, error_message
        from audit_ingest_dead_letter
        where ($1 = '' or status = $1)
        order by failed_at desc, id desc
        limit $2
        """
        rows = await self.pool.fetch(sql, status, limit)
        return [dict(row) for row in rows]

    async def fetch_trace_view(self, trace_id: str) -> dict[str, Any]:
        async with self.pool.acquire() as conn:
            invocations = [dict(row) for row in await conn.fetch(
                """
                select * from agent_invocation_log
                where trace_id = $1
                order by started_at asc, id asc
                """,
                trace_id,
            )]
            steps = [dict(row) for row in await conn.fetch(
                """
                select * from agent_step_log
                where trace_id = $1
                order by started_at asc, id asc
                """,
                trace_id,
            )]
            eval_results = [dict(row) for row in await conn.fetch(
                """
                select * from agent_eval_result
                where trace_id = $1
                order by evaluated_at asc, id asc
                """,
                trace_id,
            )]
            ingest_events = [dict(row) for row in await conn.fetch(
                """
                select * from audit_ingest_event
                where trace_id = $1
                order by occurred_at asc, id asc
                """,
                trace_id,
            )]
            dead_letters = [dict(row) for row in await conn.fetch(
                """
                select * from audit_ingest_dead_letter
                where trace_id = $1
                order by failed_at asc, id asc
                """,
                trace_id,
            )]
        return {
            "trace_id": trace_id,
            "invocations": invocations,
            "steps": steps,
            "eval_results": eval_results,
            "ingest_events": ingest_events,
            "dead_letters": dead_letters,
        }

    async def upsert_session(self, payload: dict[str, Any]) -> None:
        sql = """
        insert into conversation_session (
            session_id, tenant_id, user_id, topic, status, waiting_state, current_task_id,
            opened_at, last_active_at, closed_at, close_reason, source_type, source_name, meta
        ) values (
            $1, $2, $3, $4, $5, $6, $7,
            $8, $9, $10, $11, $12, $13, $14::jsonb
        )
        on conflict (session_id) do update set
            tenant_id = excluded.tenant_id,
            user_id = excluded.user_id,
            topic = excluded.topic,
            status = excluded.status,
            waiting_state = excluded.waiting_state,
            current_task_id = excluded.current_task_id,
            last_active_at = excluded.last_active_at,
            closed_at = excluded.closed_at,
            close_reason = excluded.close_reason,
            source_type = excluded.source_type,
            source_name = excluded.source_name,
            meta = excluded.meta,
            updated_at = now()
        """
        await self.pool.execute(
            sql,
            payload["session_id"],
            payload.get("tenant_id"),
            payload.get("user_id"),
            payload.get("topic"),
            payload["status"],
            payload.get("waiting_state"),
            payload.get("current_task_id"),
            payload["opened_at"],
            payload["last_active_at"],
            payload.get("closed_at"),
            payload.get("close_reason"),
            payload.get("source_type"),
            payload.get("source_name"),
            payload.get("meta", {}),
        )

    async def fetch_session(self, session_id: str) -> dict[str, Any] | None:
        row = await self.pool.fetchrow(
            """
            select *
            from conversation_session
            where session_id = $1
            """,
            session_id,
        )
        return dict(row) if row else None

    async def upsert_task(self, payload: dict[str, Any]) -> None:
        sql = """
        insert into conversation_task (
            task_id, session_id, parent_task_id, tenant_id, user_id, title, task_type, status,
            waiting_state, priority, requested_by, assigned_agent, started_at, last_active_at,
            completed_at, closed_reason, meta
        ) values (
            $1, $2, $3, $4, $5, $6, $7, $8,
            $9, $10, $11, $12, $13, $14,
            $15, $16, $17::jsonb
        )
        on conflict (task_id) do update set
            session_id = excluded.session_id,
            parent_task_id = excluded.parent_task_id,
            tenant_id = excluded.tenant_id,
            user_id = excluded.user_id,
            title = excluded.title,
            task_type = excluded.task_type,
            status = excluded.status,
            waiting_state = excluded.waiting_state,
            priority = excluded.priority,
            requested_by = excluded.requested_by,
            assigned_agent = excluded.assigned_agent,
            last_active_at = excluded.last_active_at,
            completed_at = excluded.completed_at,
            closed_reason = excluded.closed_reason,
            meta = excluded.meta,
            updated_at = now()
        """
        await self.pool.execute(
            sql,
            payload["task_id"],
            payload["session_id"],
            payload.get("parent_task_id"),
            payload.get("tenant_id"),
            payload.get("user_id"),
            payload.get("title"),
            payload.get("task_type"),
            payload["status"],
            payload.get("waiting_state"),
            payload.get("priority", 100),
            payload.get("requested_by"),
            payload.get("assigned_agent"),
            payload["started_at"],
            payload["last_active_at"],
            payload.get("completed_at"),
            payload.get("closed_reason"),
            payload.get("meta", {}),
        )

    async def fetch_task(self, task_id: str) -> dict[str, Any] | None:
        row = await self.pool.fetchrow(
            """
            select *
            from conversation_task
            where task_id = $1
            """,
            task_id,
        )
        return dict(row) if row else None

    async def count_session_tasks(
        self,
        session_id: str,
        *,
        exclude_task_id: str | None = None,
        statuses: list[str] | None = None,
    ) -> int:
        sql = """
        select count(*)
        from conversation_task
        where session_id = $1
          and ($2::varchar is null or task_id <> $2)
          and ($3::varchar[] is null or status = any($3))
        """
        return int(await self.pool.fetchval(sql, session_id, exclude_task_id, statuses))

    async def list_session_tasks(self, session_id: str, limit: int = 200) -> list[dict[str, Any]]:
        sql = """
        select *
        from conversation_task
        where session_id = $1
        order by last_active_at desc, id desc
        limit $2
        """
        rows = await self.pool.fetch(sql, session_id, limit)
        return [dict(row) for row in rows]

    async def list_sessions(
        self,
        *,
        status: str | None = None,
        tenant_id: str | None = None,
        user_id: str | None = None,
        limit: int = 100,
        offset: int = 0,
    ) -> list[dict[str, Any]]:
        sql = """
        select *
        from conversation_session
        where ($1::varchar is null or status = $1)
          and ($2::varchar is null or tenant_id = $2)
          and ($3::varchar is null or user_id = $3)
        order by last_active_at desc, id desc
        limit $4
        offset $5
        """
        rows = await self.pool.fetch(sql, status, tenant_id, user_id, limit, offset)
        return [dict(row) for row in rows]

    async def get_session_stats(
        self,
        *,
        tenant_id: str | None = None,
        user_id: str | None = None,
    ) -> dict[str, int]:
        sql = """
        select status, count(*) as cnt
        from conversation_session
        where ($1::varchar is null or tenant_id = $1)
          and ($2::varchar is null or user_id = $2)
        group by status
        """
        rows = await self.pool.fetch(sql, tenant_id, user_id)
        return {row["status"]: int(row["cnt"]) for row in rows}

    async def fetch_next_eval_queue_item(self, worker_id: str) -> dict[str, Any] | None:
        sql = """
        with picked as (
            select id
            from agent_eval_queue
            where status = 'pending'
              and available_at <= now()
            order by priority asc, available_at asc
            limit 1
            for update skip locked
        )
        update agent_eval_queue q
        set
            status = 'running',
            attempts = attempts + 1,
            locked_at = now(),
            locked_by = $1,
            updated_at = now()
        from picked
        where q.id = picked.id
        returning
            q.queue_item_id,
            q.trace_id,
            q.run_id,
            q.priority,
            q.status,
            q.attempts,
            q.available_at,
            q.locked_at,
            q.locked_by,
            q.payload,
            q.error_message
        """
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                row = await conn.fetchrow(sql, worker_id)
        if row is None:
            return None
        result = dict(row)
        result["payload"] = dict(result["payload"])
        return result

    async def mark_eval_queue_item(self, queue_item_id: str, status: str, error_message: str | None = None) -> None:
        sql = """
        update agent_eval_queue
        set
            status = $2,
            error_message = $3,
            updated_at = now()
        where queue_item_id = $1
        """
        await self.pool.execute(sql, queue_item_id, status, error_message)
