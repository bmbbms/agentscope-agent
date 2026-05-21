from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .prompts import (
    DIAGNOSIS_AGENT_PROMPT,
    EVALUATOR_AGENT_PROMPT,
    METRIC_AGENT_PROMPT,
    REPORT_AGENT_PROMPT,
    ROUTER_PROMPT,
)
from .settings import MerchantAgentSettings


@dataclass(slots=True)
class MerchantAgents:
    router: Any
    metric: Any
    diagnosis: Any
    report: Any
    evaluator: Any


def build_agentscope_agents(settings: MerchantAgentSettings) -> MerchantAgents:
    """
    Build AgentScope ReAct agents.

    This function imports AgentScope lazily so the codebase can still be imported
    in environments where AgentScope is not yet installed.
    """

    import agentscope
    from agentscope.agent import ReActAgent
    from agentscope.formatter import OpenAIChatFormatter
    from agentscope.memory import InMemoryMemory
    from agentscope.model import OpenAIChatModel
    from agentscope.tool import Toolkit

    init_kwargs: dict[str, Any] = {"project": settings.app_name}
    if settings.enable_studio and settings.studio_url:
        init_kwargs["studio_url"] = settings.studio_url
    agentscope.init(**init_kwargs)

    client_kwargs = {"base_url": settings.base_url} if settings.base_url else {}

    def build_model() -> OpenAIChatModel:
        if not settings.api_key:
            raise RuntimeError("OPENAI_API_KEY is required to build AgentScope agents.")
        return OpenAIChatModel(
            model_name=settings.model_name,
            api_key=settings.api_key,
            client_kwargs=client_kwargs,
            stream=False,
        )

    def build_agent(name: str, sys_prompt: str, toolkit: Toolkit | None = None) -> ReActAgent:
        return ReActAgent(
            name=name,
            sys_prompt=sys_prompt,
            model=build_model(),
            formatter=OpenAIChatFormatter(),
            memory=InMemoryMemory(),
            toolkit=toolkit or Toolkit(),
        )

    return MerchantAgents(
        router=build_agent("router_agent", ROUTER_PROMPT),
        metric=build_agent("metric_definition_agent", METRIC_AGENT_PROMPT),
        diagnosis=build_agent("merchant_diagnosis_agent", DIAGNOSIS_AGENT_PROMPT),
        report=build_agent("report_agent", REPORT_AGENT_PROMPT),
        evaluator=build_agent("evaluation_agent", EVALUATOR_AGENT_PROMPT),
    )
