from __future__ import annotations

import unittest
from unittest.mock import AsyncMock, Mock, patch

from superset_data_query_agent import AgentScopeDataQueryWorkflow, SupersetQueryRequestSpec


class AgentScopeDataQueryWorkflowTests(unittest.IsolatedAsyncioTestCase):
    def test_parse_json_reply_supports_list_payloads(self) -> None:
        class _FakeMsg:
            def __init__(self, content):
                self.content = content

        reply = [
            _FakeMsg("thinking..."),
            _FakeMsg('{"action":"schema_search","should_execute":false}'),
        ]

        parsed = AgentScopeDataQueryWorkflow._parse_json_reply(reply)

        self.assertEqual(parsed["action"], "schema_search")

    async def test_fallback_guard_blocks_select_star(self) -> None:
        service = Mock()
        workflow = AgentScopeDataQueryWorkflow(service)
        spec = SupersetQueryRequestSpec(
            query="run risky sql",
            action="sql_query",
            sql="select * from huge_table",
        )

        result = await workflow.run(spec)

        self.assertEqual(result.action, "sql_query")
        self.assertFalse(result.should_execute)
        self.assertIsNone(result.service_result)
        self.assertFalse(result.guard_output["approved"])
        self.assertIn("select_star", result.guard_output["risk_flags"])

    async def test_fallback_guard_executes_explicit_readonly_sql(self) -> None:
        service = Mock()
        service.handle.return_value = {"action": "sql_query", "row_count": 1}
        workflow = AgentScopeDataQueryWorkflow(service)
        spec = SupersetQueryRequestSpec(
            query="run safe sql",
            action="sql_query",
            sql="select 1 as ok",
        )

        result = await workflow.run(spec)

        self.assertTrue(result.should_execute)
        self.assertEqual(result.service_result["row_count"], 1)
        service.handle.assert_called_once()

    async def test_agentscope_runtime_uses_planner_and_guard(self) -> None:
        service = Mock()
        service.handle.return_value = {"action": "sql_query", "row_count": 2}
        workflow = AgentScopeDataQueryWorkflow(service)
        planner = AsyncMock(
            return_value='{"action":"sql_query","should_execute":true,"database_name":"demo_db","sql":"select id from merchant_order where dt = current_date","reason":"specific request","risk_flags":[],"candidate_tables":["merchant_order"],"assumptions":[]}'
        )
        guard = AsyncMock(
            return_value='{"approved":true,"reason":"safe","risk_flags":[],"required_fixes":[],"safe_sql":"select id from merchant_order where dt = current_date"}'
        )

        with patch.object(AgentScopeDataQueryWorkflow, "is_enabled", return_value=True):
            with patch.object(workflow, "_build_agent", side_effect=[planner, guard]):
                spec = SupersetQueryRequestSpec(query="query today merchant order ids", action="schema_search")
                result = await workflow.run(spec)

        self.assertTrue(result.should_execute)
        self.assertEqual(result.guard_output["approved"], True)
        service.handle.assert_called_once()


if __name__ == "__main__":
    unittest.main()
