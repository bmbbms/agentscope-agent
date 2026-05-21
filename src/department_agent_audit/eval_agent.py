from __future__ import annotations

import json
from typing import Any, Protocol


class AsyncTextAgent(Protocol):
    async def __call__(self, prompt: str) -> Any:
        ...


def build_eval_prompt(payload: dict[str, Any]) -> str:
    rubric = payload["rubric"]
    run_payload = payload["payload"]
    rule_checks = payload["rule_checks"]
    return f"""
You are an evaluation agent for a department-level merchant data assistant.

Your job is to grade one completed run.
Score each dimension from 0 to 20.
Use only the provided payload and rule checks.
Do not invent evidence that is not present.

Rubric:
{json.dumps(rubric, ensure_ascii=True, indent=2)}

Rule checks:
{json.dumps(rule_checks, ensure_ascii=True, indent=2)}

Run payload:
{json.dumps(run_payload, ensure_ascii=True, indent=2)}

Return strict JSON with this schema:
{{
  "scores": {{
    "task_completion": number,
    "factual_grounding": number,
    "metric_consistency": number,
    "actionability": number,
    "safety_compliance": number
  }},
  "issue_tags": ["string"],
  "findings": ["string"],
  "suggestions": ["string"],
  "evidence": [{{"type": "string", "detail": "string"}}]
}}
""".strip()


class AgentScopeLLMJudge:
    """
    Adapter around an async text-generating evaluator agent.

    In production, pass an AgentScope evaluator agent or workflow here and make sure
    it returns JSON text matching the expected schema.
    """

    def __init__(self, evaluator_agent: AsyncTextAgent):
        self.evaluator_agent = evaluator_agent

    async def judge(self, payload: dict[str, Any]) -> dict[str, Any]:
        prompt = build_eval_prompt(payload)
        raw_reply = await self.evaluator_agent(prompt)
        if isinstance(raw_reply, str):
            text = raw_reply
        else:
            text = getattr(raw_reply, "content", str(raw_reply))
        return json.loads(text)
