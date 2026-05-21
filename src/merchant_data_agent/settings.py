from __future__ import annotations

import json
import os
from dataclasses import dataclass, field

from department_agent_audit.event_ingest import AuditIngestEndpoint


@dataclass(slots=True)
class RemoteAgentEndpoint:
    name: str
    protocol: str
    url: str
    timeout_seconds: float = 30.0
    auth_token: str | None = None
    a2a_method: str = "tasks/send"
    meta: dict[str, str] = field(default_factory=dict)


@dataclass(slots=True)
class MerchantAgentSettings:
    model_name: str = "gpt-4o-mini"
    api_key: str = ""
    base_url: str | None = None
    app_name: str = "merchant-data-department-agent"
    enable_studio: bool = False
    studio_url: str | None = None
    remote_agents: dict[str, RemoteAgentEndpoint] = field(default_factory=dict)
    audit_ingest_endpoint: AuditIngestEndpoint | None = None

    @classmethod
    def from_env(cls) -> "MerchantAgentSettings":
        remote_agents = _load_remote_agents_from_env()
        return cls(
            model_name=os.getenv("AGENTSCOPE_MODEL_NAME", "gpt-4o-mini"),
            api_key=os.getenv("OPENAI_API_KEY", ""),
            base_url=os.getenv("OPENAI_BASE_URL"),
            app_name=os.getenv("MERCHANT_AGENT_APP_NAME", "merchant-data-department-agent"),
            enable_studio=os.getenv("AGENTSCOPE_ENABLE_STUDIO", "false").lower() == "true",
            studio_url=os.getenv("AGENTSCOPE_STUDIO_URL"),
            remote_agents=remote_agents,
            audit_ingest_endpoint=_load_audit_ingest_endpoint_from_env(),
        )


def _load_remote_agents_from_env() -> dict[str, RemoteAgentEndpoint]:
    raw = os.getenv("MERCHANT_REMOTE_AGENTS_JSON", "").strip()
    if not raw:
        return {}
    items = json.loads(raw)
    endpoints: dict[str, RemoteAgentEndpoint] = {}
    for item in items:
        endpoint = RemoteAgentEndpoint(
            name=item["name"],
            protocol=item["protocol"],
            url=item["url"],
            timeout_seconds=float(item.get("timeout_seconds", 30.0)),
            auth_token=item.get("auth_token"),
            a2a_method=item.get("a2a_method", "tasks/send"),
            meta=item.get("meta", {}),
        )
        endpoints[endpoint.name] = endpoint
    return endpoints


def _load_audit_ingest_endpoint_from_env() -> AuditIngestEndpoint | None:
    url = os.getenv("AUDIT_INGEST_URL", "").strip()
    if not url:
        return None
    return AuditIngestEndpoint(
        url=url,
        auth_token=os.getenv("AUDIT_INGEST_TOKEN"),
        timeout_seconds=float(os.getenv("AUDIT_INGEST_TIMEOUT_SECONDS", "10")),
    )
