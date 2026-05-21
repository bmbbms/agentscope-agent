from __future__ import annotations

from dataclasses import asdict
from typing import Any, Awaitable, Callable

from .audit import AuditContext, AuditLogger, utc_now
from .event_ingest import AuditIngestEndpoint, HttpAuditIngestRepository
from .storage import CollectingAuditRepository


class ChildAgentAuditRunner:
    """
    Helper for child-agent services.

    The child agent receives a parent audit envelope from the main platform,
    runs locally with an in-memory audit repository, and returns the collected
    invocation + step bundle to the caller.
    """

    def __init__(self, default_sink: AuditIngestEndpoint | None = None) -> None:
        self.default_sink = default_sink

    async def run(
        self,
        *,
        request_payload: dict[str, Any],
        agent_name: str,
        handler: Callable[[AuditContext, AuditLogger, dict[str, Any]], Awaitable[dict[str, Any]]],
        source_name: str,
        workflow_name: str | None = None,
        scenario_name: str | None = None,
        tags: list[str] | None = None,
        meta: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        parent_audit = request_payload["audit_context"]
        context, resolved_agent_name = AuditContext.from_parent(
            parent_audit,
            agent_name=agent_name,
            source_type="remote_agent",
            trigger_type="delegated",
            source_name=source_name,
            workflow_name=workflow_name,
            scenario_name=scenario_name,
            tags=tags,
            meta=meta,
        )

        input_payload = {
            key: value
            for key, value in request_payload.items()
            if key != "audit_context"
        }

        repository, returns_bundle = self._build_repository(request_payload)
        audit_logger = AuditLogger(repository)

        async def _call() -> dict[str, Any]:
            return await handler(context, audit_logger, input_payload)

        result = await audit_logger.invoke_with_audit(
            context,
            agent_name=resolved_agent_name,
            input_payload=input_payload,
            agent_call=_call,
        )

        result["child_audit_context"] = {
            **asdict(context),
            "agent_name": resolved_agent_name,
            "exported_at": utc_now().isoformat(),
        }
        if returns_bundle:
            bundle_repository = repository
            assert isinstance(bundle_repository, CollectingAuditRepository)
            result["audit_bundle"] = bundle_repository.export_run_bundle(context.run_id)
        return result

    def _build_repository(self, request_payload: dict[str, Any]) -> tuple[CollectingAuditRepository | HttpAuditIngestRepository, bool]:
        sink_payload = request_payload.get("audit_sink")
        if sink_payload:
            endpoint = AuditIngestEndpoint(
                url=sink_payload["url"],
                auth_token=sink_payload.get("auth_token"),
                timeout_seconds=float(sink_payload.get("timeout_seconds", 10.0)),
            )
            service_name = request_payload.get("agent_service_name", "child-agent-service")
            return HttpAuditIngestRepository(endpoint, producer_service=service_name), False
        if self.default_sink is not None:
            return HttpAuditIngestRepository(self.default_sink, producer_service="child-agent-service"), False
        return CollectingAuditRepository(), True
