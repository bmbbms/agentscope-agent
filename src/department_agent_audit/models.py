from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class RuleCheckResult:
    name: str
    passed: bool
    reason: str
    details: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class EvalScore:
    task_completion: float
    factual_grounding: float
    metric_consistency: float
    actionability: float
    safety_compliance: float

    @property
    def total(self) -> float:
        return (
            self.task_completion
            + self.factual_grounding
            + self.metric_consistency
            + self.actionability
            + self.safety_compliance
        )


@dataclass(slots=True)
class EvalResult:
    trace_id: str
    run_id: str
    eval_id: str
    evaluator_name: str
    evaluator_version: str
    eval_mode: str
    rule_passed: bool
    llm_passed: bool
    overall_passed: bool
    scores: EvalScore
    issue_tags: list[str]
    findings: list[str]
    suggestions: list[str]
    evidence: list[dict[str, Any]]
    raw_judge: dict[str, Any]
    evaluated_at: datetime
    latency_ms: int
