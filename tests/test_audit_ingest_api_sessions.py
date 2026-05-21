from __future__ import annotations

import os
import unittest

from department_agent_audit.event_ingest import AuditIngestService
from department_agent_audit.session_manager import SessionManager
from department_agent_audit.storage import CollectingAuditRepository
import audit_ingest_api as api_module


class AuditIngestSessionApiTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        os.environ["AUDIT_INGEST_TOKEN"] = "test-token"
        self.repository = CollectingAuditRepository()
        self.session_manager = SessionManager(self.repository)
        self.ingest_service = AuditIngestService(self.repository)

        # Bind in-memory components so tests do not need Postgres.
        api_module.app.state.repository = self.repository
        api_module.app.state.session_manager = self.session_manager
        api_module.app.state.ingest_service = self.ingest_service

    async def test_session_endpoints_contract(self) -> None:
        session, task = await self.session_manager.ensure_session_and_task(
            query="investigate merchant anomaly",
            user_id="demo.user",
            tenant_id="merchant-data",
            source_type="web_app",
            task_type="diagnosis",
            assigned_agent="merchant_diagnosis_agent",
        )
        self.assertIsNotNone(session.session_id)
        self.assertEqual(task.session_id, session.session_id)

        headers = {"Authorization": "Bearer test-token"}

        list_result = await api_module.list_sessions(
            authorization=headers["Authorization"],
            status=None,
            tenant_id="merchant-data",
            user_id="demo.user",
            limit=20,
            offset=0,
        )
        self.assertIn("items", list_result)
        self.assertIn("count", list_result)
        self.assertGreaterEqual(list_result["count"], 1)

        stats_result = await api_module.get_session_stats(
            authorization=headers["Authorization"],
            tenant_id="merchant-data",
            user_id="demo.user",
        )
        self.assertIn("total", stats_result)
        self.assertIn("by_status", stats_result)
        self.assertGreaterEqual(stats_result["total"], 1)

        snapshot_result = await api_module.get_session_snapshot(
            session_id=session.session_id,
            authorization=headers["Authorization"],
            task_limit=50,
        )
        self.assertIn("session", snapshot_result)
        self.assertIn("tasks", snapshot_result)
        self.assertEqual(snapshot_result["session"]["session_id"], session.session_id)
        self.assertGreaterEqual(len(snapshot_result["tasks"]), 1)

        task_stats_result = await api_module.get_task_stats(
            authorization=headers["Authorization"],
            tenant_id="merchant-data",
            user_id="demo.user",
        )
        self.assertIn("total", task_stats_result)
        self.assertIn("completion_rate", task_stats_result)
        self.assertGreaterEqual(task_stats_result["total"], 1)

        task_list_result = await api_module.list_tasks(
            authorization=headers["Authorization"],
            status=None,
            tenant_id="merchant-data",
            user_id="demo.user",
            limit=20,
            offset=0,
        )
        self.assertIn("items", task_list_result)
        self.assertIn("count", task_list_result)
        self.assertGreaterEqual(task_list_result["count"], 1)

    async def test_close_session_contract(self) -> None:
        session, _ = await self.session_manager.ensure_session_and_task(
            query="close me",
            user_id="demo.user",
            tenant_id="merchant-data",
            source_type="web_app",
            task_type="diagnosis",
        )

        closed = await self.session_manager.close_session(
            session_id=session.session_id,
            closed_by="ops.user",
        )
        self.assertEqual(closed["status"], "closed")
        self.assertEqual(closed["close_reason"], "user_closed")
        self.assertEqual(closed["meta"]["closed_by"], "ops.user")


if __name__ == "__main__":
    unittest.main()
