from __future__ import annotations

import unittest

from department_agent_audit.audit import AuditLogger
from department_agent_audit.eval_worker import EvalWorker, StubLLMJudge
from department_agent_audit.session_manager import SessionManager
from department_agent_audit.storage import CollectingAuditRepository
from merchant_data_agent.app import MerchantDepartmentApp, _route_by_rule


class _FailingRemoteRegistry:
    async def invoke_with_audit(self, **kwargs):
        del kwargs
        raise TimeoutError("report child agent timed out")


class _CapturingRemoteRegistry:
    def __init__(self) -> None:
        self.calls: list[dict] = []

    async def invoke_with_audit(self, **kwargs):
        self.calls.append(kwargs)
        return {
            "route": kwargs["route"],
            "reply": "ok",
        }


class MerchantDepartmentAppTests(unittest.IsolatedAsyncioTestCase):
    def test_route_rule_supports_data_query_intents(self) -> None:
        self.assertEqual(_route_by_rule("show table schema for merchant_order"), "data_query")
        self.assertEqual(_route_by_rule("请执行sql查询近7天交易"), "data_query")

    async def test_failed_remote_call_marks_task_failed(self) -> None:
        repository = CollectingAuditRepository()
        app = MerchantDepartmentApp(
            audit_logger=AuditLogger(repository),
            agents=None,
            tools=None,
            eval_worker=EvalWorker(repository, StubLLMJudge()),
            session_manager=SessionManager(repository),
            remote_registry=_FailingRemoteRegistry(),
        )

        with self.assertRaises(TimeoutError):
            await app.handle_query(
                query="generate monthly report",
                user_id="demo.user",
                tenant_id="merchant-data",
                source_type="http_api",
                trigger_type="manual",
            )

        tasks = await repository.list_tasks(tenant_id="merchant-data", user_id="demo.user")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["status"], "failed")
        self.assertEqual(tasks[0]["meta"]["last_error_type"], "TimeoutError")

        sessions = await repository.list_sessions(tenant_id="merchant-data", user_id="demo.user")
        self.assertEqual(len(sessions), 1)
        self.assertEqual(sessions[0]["status"], "active")

    async def test_data_query_route_forwards_extra_payload(self) -> None:
        repository = CollectingAuditRepository()
        remote_registry = _CapturingRemoteRegistry()
        app = MerchantDepartmentApp(
            audit_logger=AuditLogger(repository),
            agents=None,
            tools=None,
            eval_worker=EvalWorker(repository, StubLLMJudge()),
            session_manager=SessionManager(repository),
            remote_registry=remote_registry,
        )

        result = await app.handle_query(
            query="please execute sql for merchant trades",
            user_id="demo.user",
            tenant_id="merchant-data",
            source_type="http_api",
            trigger_type="manual",
            extra_payload={
                "action": "sql_query",
                "sql": "select 1",
                "database_name": "demo_db",
                "export_excel": True,
            },
        )

        self.assertEqual(result["route"], "data_query")
        self.assertEqual(len(remote_registry.calls), 1)
        self.assertEqual(remote_registry.calls[0]["route"], "data_query")
        self.assertEqual(remote_registry.calls[0]["extra_payload"]["sql"], "select 1")


if __name__ == "__main__":
    unittest.main()
