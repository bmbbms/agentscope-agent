from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class MerchantDataTools:
    """
    Thin business tool layer.

    Replace these stubs with real integrations to SQL engines, metric APIs,
    merchant master-data systems, and notification channels.
    """

    async def explain_metric_definition(self, metric_name: str) -> dict[str, Any]:
        return {
            "metric_name": metric_name,
            "definition": f"{metric_name} 的正式口径定义尚未接入真实知识库，这里是占位返回。",
            "scope_notes": ["需要接入指标知识库后替换"],
        }

    async def diagnose_metric_drop(self, query: str) -> dict[str, Any]:
        return {
            "query": query,
            "summary": "检测到商户经营波动，但当前仍是占位数据。",
            "facts": [
                {"metric": "gmv", "delta_pct": -9.8},
                {"metric": "pay_success_rate", "delta_pct": -1.7},
            ],
            "hypotheses": ["曝光下降", "支付链路异常"],
            "next_actions": ["核对曝光漏斗", "排查支付链路日志"],
        }

    async def build_report(self, topic: str, facts: list[dict[str, Any]]) -> dict[str, Any]:
        return {
            "topic": topic,
            "report": f"{topic}：当前为报告生成占位结果，请接入真实模板与业务数据。",
            "facts": facts,
        }
