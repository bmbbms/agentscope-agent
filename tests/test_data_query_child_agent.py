from __future__ import annotations

import unittest
from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from data_query_child_agent_http_api import app
from superset_data_query_agent import DataQueryWorkflowResult


class DataQueryChildAgentTests(unittest.TestCase):
    def test_invoke_returns_audit_bundle_for_schema_search(self) -> None:
        payload = {
            "query": "merchant_order",
            "schema_keyword": "merchant_order",
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
                "scenario_name": "data_query",
                "user_id": "demo.user",
                "tenant_id": "merchant-data",
                "tags": [],
                "meta": {},
            },
        }

        fake_result = DataQueryWorkflowResult(
            action="schema_search",
            should_execute=False,
            planner_output={"action": "schema_search", "reason": "safe schema discovery"},
            guard_output=None,
            service_result={
                "action": "schema_search",
                "keyword": "merchant_order",
                "count": 1,
                "items": [
                    {
                        "table_file": "merchant_order+shop_order.md",
                        "table_name": "merchant_order",
                        "description": "shop_order",
                        "path": "C:/tmp/merchant_order.md",
                    }
                ],
            },
        )

        with patch("data_query_child_agent_http_api.workflow.run", new_callable=AsyncMock, return_value=fake_result):
            with TestClient(app) as client:
                response = client.post("/invoke", json=payload)

        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["route"], "data_query")
        self.assertIn("audit_bundle", body)
        self.assertEqual(body["query_result"]["count"], 1)

    def test_invoke_supports_sql_query_action(self) -> None:
        payload = {
            "query": "please run this sql",
            "action": "sql_query",
            "sql": "select 1 as ok",
            "database_name": "demo_db",
            "export_excel": True,
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
                "scenario_name": "data_query",
                "user_id": "demo.user",
                "tenant_id": "merchant-data",
                "tags": [],
                "meta": {},
            },
        }

        fake_result = DataQueryWorkflowResult(
            action="sql_query",
            should_execute=True,
            planner_output={"action": "sql_query"},
            guard_output={"approved": True, "reason": "safe"},
            service_result={
                "action": "sql_query",
                "database_name": "demo_db",
                "row_count": 1,
                "column_count": 1,
                "columns": ["ok"],
                "preview": [{"ok": 1}],
                "export_path": "C:/tmp/query.xlsx",
                "mask_enabled": True,
            },
        )

        with patch("data_query_child_agent_http_api.workflow.run", new_callable=AsyncMock, return_value=fake_result) as run:
            with TestClient(app) as client:
                response = client.post("/invoke", json=payload)

        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["query_result"]["row_count"], 1)
        self.assertIn("C:/tmp/query.xlsx", body["reply"])
        run.assert_called_once()

    def test_invoke_returns_plan_when_guard_blocks_execution(self) -> None:
        payload = {
            "query": "run risky sql",
            "action": "sql_query",
            "sql": "select * from huge_table",
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
                "scenario_name": "data_query",
                "user_id": "demo.user",
                "tenant_id": "merchant-data",
                "tags": [],
                "meta": {},
            },
        }

        fake_result = DataQueryWorkflowResult(
            action="sql_query",
            should_execute=False,
            planner_output={"action": "sql_query", "reason": "need guard approval"},
            guard_output={"approved": False, "reason": "select_star"},
            service_result=None,
        )

        with patch("data_query_child_agent_http_api.workflow.run", new_callable=AsyncMock, return_value=fake_result):
            with TestClient(app) as client:
                response = client.post("/invoke", json=payload)

        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["query_result"]["action"], "sql_query_plan")
        self.assertIn("not executed", body["reply"])


if __name__ == "__main__":
    unittest.main()
