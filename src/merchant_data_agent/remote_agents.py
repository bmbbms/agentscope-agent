from __future__ import annotations

import json
import uuid
from dataclasses import dataclass
from typing import Any, Protocol

from department_agent_audit.audit import AuditContext, AuditLogger
from department_agent_audit.event_ingest import AuditIngestEndpoint

from .settings import RemoteAgentEndpoint

try:
    import httpx
except ImportError:  # pragma: no cover - optional dependency
    httpx = None


class RemoteAgentClient(Protocol):
    endpoint: RemoteAgentEndpoint

    async def invoke(self, payload: dict[str, Any]) -> dict[str, Any]:
        ...


def _ensure_httpx() -> None:
    if httpx is None:
        raise RuntimeError("httpx is required for remote agent calls. Install it with `pip install httpx`.")


def _auth_headers(endpoint: RemoteAgentEndpoint) -> dict[str, str]:
    if not endpoint.auth_token:
        return {}
    return {"Authorization": f"Bearer {endpoint.auth_token}"}


@dataclass(slots=True)
class HttpJsonAgentClient:
    endpoint: RemoteAgentEndpoint

    async def invoke(self, payload: dict[str, Any]) -> dict[str, Any]:
        _ensure_httpx()
        headers = {"Content-Type": "application/json", **_auth_headers(self.endpoint)}
        async with httpx.AsyncClient(timeout=self.endpoint.timeout_seconds) as client:
            response = await client.post(self.endpoint.url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()


@dataclass(slots=True)
class A2AAgentClient:
    endpoint: RemoteAgentEndpoint

    async def invoke(self, payload: dict[str, Any]) -> dict[str, Any]:
        _ensure_httpx()
        headers = {"Content-Type": "application/json", **_auth_headers(self.endpoint)}
        request_body = {
            "jsonrpc": "2.0",
            "id": uuid.uuid4().hex,
            "method": self.endpoint.a2a_method,
            "params": payload,
        }
        async with httpx.AsyncClient(timeout=self.endpoint.timeout_seconds) as client:
            response = await client.post(self.endpoint.url, json=request_body, headers=headers)
            response.raise_for_status()
            body = response.json()
        if "error" in body:
            raise RuntimeError(f"A2A remote agent error: {json.dumps(body['error'], ensure_ascii=True)}")
        return body.get("result", {})


class RemoteAgentRegistry:
    def __init__(
        self,
        clients: dict[str, RemoteAgentClient],
        audit_sink: AuditIngestEndpoint | None = None,
    ):
        self.clients = clients
        self.audit_sink = audit_sink

    @classmethod
    def from_settings(
        cls,
        endpoints: dict[str, RemoteAgentEndpoint],
        audit_sink: AuditIngestEndpoint | None = None,
    ) -> "RemoteAgentRegistry":
        clients: dict[str, RemoteAgentClient] = {}
        for name, endpoint in endpoints.items():
            protocol = endpoint.protocol.lower()
            if protocol == "http":
                clients[name] = HttpJsonAgentClient(endpoint)
            elif protocol == "a2a":
                clients[name] = A2AAgentClient(endpoint)
            else:
                raise ValueError(f"Unsupported remote agent protocol: {endpoint.protocol}")
        return cls(clients, audit_sink=audit_sink)

    def get(self, name: str) -> RemoteAgentClient:
        try:
            return self.clients[name]
        except KeyError as exc:
            raise KeyError(f"Remote agent '{name}' is not configured.") from exc

    async def invoke_with_audit(
        self,
        *,
        route: str,
        query: str,
        context: AuditContext,
        audit_logger: AuditLogger,
        extra_payload: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        client = self.get(route)
        input_payload = {
            "query": query,
            "audit_context": context.to_remote_parent_payload(),
            "audit_sink": self.audit_sink.to_payload() if self.audit_sink else None,
            "agent_service_name": f"remote-{route}-service",
            **(extra_payload or {}),
        }

        async def _call_remote() -> dict[str, Any]:
            async with audit_logger.tool_step(
                context,
                step_name=f"remote_{route}",
                sequence_no=1,
                target_name=client.endpoint.url,
                input_payload=input_payload,
                step_type="remote_agent_call",
            ) as finish_step:
                output = await client.invoke(input_payload)
                child_bundle = output.pop("audit_bundle", None)
                if child_bundle:
                    await audit_logger.ingest_remote_audit_bundle(child_bundle)
                await finish_step(output, success=True, status="success")
                return output

        return await audit_logger.invoke_with_audit(
            context,
            agent_name=f"remote_{route}_agent",
            input_payload=input_payload,
            agent_call=_call_remote,
        )
