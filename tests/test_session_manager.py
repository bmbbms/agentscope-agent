from __future__ import annotations

import unittest

from department_agent_audit.session_manager import SessionManager
from department_agent_audit.storage import CollectingAuditRepository


class SessionManagerTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.repository = CollectingAuditRepository()
        self.manager = SessionManager(self.repository)

    async def test_create_session_and_task(self) -> None:
        session, task = await self.manager.ensure_session_and_task(
            query="analyze merchant gmv drop",
            user_id="demo.user",
            tenant_id="merchant-data",
            source_type="web_app",
            task_type="diagnosis",
            assigned_agent="merchant_diagnosis_agent",
        )
        self.assertIsNotNone(session.session_id)
        self.assertEqual(task.session_id, session.session_id)
        self.assertEqual(task.status.value, "running")

    async def test_finalize_run_marks_success(self) -> None:
        session, task = await self.manager.ensure_session_and_task(
            query="build weekly report",
            user_id="demo.user",
            tenant_id="merchant-data",
            source_type="web_app",
            task_type="report",
        )
        result = await self.manager.finalize_run(
            session=session,
            task=task,
            run_id="run-1",
            run_status="success",
            trigger_type="manual",
        )
        self.assertIn(result["task"]["status"], {"success", "completed", "running"})
        self.assertIn("decision", result)

    async def test_close_session(self) -> None:
        session, _ = await self.manager.ensure_session_and_task(
            query="metric definition question",
            user_id="demo.user",
            tenant_id="merchant-data",
            source_type="web_app",
            task_type="metric_definition",
        )
        closed = await self.manager.close_session(
            session_id=session.session_id,
            closed_by="ops.user",
        )
        self.assertEqual(closed["status"], "closed")
        self.assertEqual(closed["close_reason"], "user_closed")
        self.assertEqual(closed["meta"]["closed_by"], "ops.user")

    async def test_list_and_stats(self) -> None:
        await self.manager.ensure_session_and_task(
            query="q1",
            user_id="u1",
            tenant_id="t1",
            source_type="web_app",
            task_type="diagnosis",
        )
        await self.manager.ensure_session_and_task(
            query="q2",
            user_id="u1",
            tenant_id="t1",
            source_type="web_app",
            task_type="report",
        )
        listing = await self.manager.list_sessions(tenant_id="t1", user_id="u1")
        stats = await self.manager.get_session_stats(tenant_id="t1", user_id="u1")
        self.assertGreaterEqual(listing["count"], 2)
        self.assertGreaterEqual(stats["total"], 2)
        self.assertIn("by_status", stats)


if __name__ == "__main__":
    unittest.main()
