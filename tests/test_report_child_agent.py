from __future__ import annotations

import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from merchant_data_agent.app import _route_by_rule
from report_child_agent_http_api import app


class ReportChildAgentTests(unittest.TestCase):
    def test_route_rule_supports_chinese_report_queries(self) -> None:
        self.assertEqual(_route_by_rule("请生成商户月报"), "report")
        self.assertEqual(_route_by_rule("帮我出一个看板"), "report")

    def test_report_child_agent_returns_audit_bundle(self) -> None:
        fake_result = {
            "query": "请生成商户月报",
            "stat_month": "202605",
            "artifacts": [
                {
                    "dashboard_type": "large_pos",
                    "title": "商户收款看板（大POS）",
                    "latest_month": "202605",
                    "update_time": "2026-05-21 18:00:00",
                    "summary": {"交易总金额": {"display_value": 100}},
                    "html_path": "C:/tmp/large.html",
                    "pdf_path": "C:/tmp/large.pdf",
                    "pdf_error": None,
                }
            ],
            "playwright_status": {"can_generate_pdf": True},
        }

        payload = {
            "query": "请生成商户月报",
            "audit_context": {
                "session_id": "session-1",
                "trace_id": "trace-1",
                "task_id": "task-1",
                "request_id": "request-1",
                "parent_run_id": "parent-run-1",
                "source_type": "remote_agent",
                "source_name": "parent-service",
                "trigger_type": "delegated",
                "workflow_name": "wf",
                "scenario_name": "report",
                "user_id": "demo.user",
                "tenant_id": "merchant-data",
                "tags": [],
                "meta": {},
            },
        }

        with patch("report_child_agent_http_api.generator.generate", return_value=fake_result):
            with TestClient(app) as client:
                response = client.post("/invoke", json=payload)

        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["route"], "report")
        self.assertIn("audit_bundle", body)
        self.assertIn("reply", body)
        self.assertEqual(body["artifacts"][0]["pdf_path"], "C:/tmp/large.pdf")

    def test_report_child_agent_defaults_to_large_pos(self) -> None:
        captured = {}

        def fake_generate(spec):
            captured["dashboard_type"] = spec.dashboard_type
            return {
                "query": spec.query,
                "stat_month": "202605",
                "artifacts": [],
                "playwright_status": None,
            }

        payload = {
            "query": "请生成商户月报",
            "audit_context": {
                "session_id": "session-1",
                "trace_id": "trace-1",
                "task_id": "task-1",
                "request_id": "request-1",
                "parent_run_id": "parent-run-1",
                "source_type": "remote_agent",
                "source_name": "parent-service",
                "trigger_type": "delegated",
                "workflow_name": "wf",
                "scenario_name": "report",
                "user_id": "demo.user",
                "tenant_id": "merchant-data",
                "tags": [],
                "meta": {},
            },
        }

        with patch("report_child_agent_http_api.generator.generate", side_effect=fake_generate):
            with TestClient(app) as client:
                response = client.post("/invoke", json=payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(captured["dashboard_type"], "large_pos")


if __name__ == "__main__":
    unittest.main()
