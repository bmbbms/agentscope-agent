from __future__ import annotations

from typing import Any

from .audit import AuditContext, AuditLogger


async def invoke_agentscope_agent(
    *,
    audit_logger: AuditLogger,
    context: AuditContext,
    agent_name: str,
    user_query: str,
    agent: Any,
) -> dict[str, Any]:
    """
    Thin adapter for wrapping an AgentScope agent call with audit logging.

    The concrete return shape should be normalized by your integration layer.
    """

    input_payload = {"query": user_query}

    async def _call() -> dict[str, Any]:
        reply = await agent(user_query)
        return {
            "reply": getattr(reply, "content", str(reply)),
            "raw_reply": str(reply),
        }

    return await audit_logger.invoke_with_audit(
        context,
        agent_name=agent_name,
        input_payload=input_payload,
        agent_call=_call,
    )
