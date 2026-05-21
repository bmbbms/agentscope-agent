from __future__ import annotations

import unittest

from department_agent_audit.distributed import ChildAgentAuditRunner
from department_agent_audit.event_ingest import AuditIngestService, build_audit_event
from department_agent_audit.storage import CollectingAuditRepository


class DistributedAndIngestTests(unittest.IsolatedAsyncioTestCase):
    async def test_ingest_normalizes_datetime_strings(self) -> None:
        repository = CollectingAuditRepository()
        service = AuditIngestService(repository)
        event = build_audit_event(
            event_type="step.upsert",
            payload={
                "trace_id": "trace-1",
                "run_id": "run-1",
                "step_id": "step-1",
                "parent_step_id": None,
                "step_type": "tool_call",
                "step_name": "manual_test",
                "sequence_no": 1,
                "target_name": "manual",
                "input_summary": "i",
                "output_summary": "o",
                "input_payload": {},
                "output_payload": {},
                "status": "success",
                "success": True,
                "error_code": None,
                "error_message": None,
                "started_at": "2026-05-21T08:47:54.270479+00:00",
                "finished_at": "2026-05-21T08:47:55.270479+00:00",
                "latency_ms": 1000,
                "token_usage": {},
                "meta": {},
            },
            producer_service="test-service",
            event_id="evt-1",
            occurred_at="2026-05-21T08:47:54.270479+00:00",
        )

        await service.ingest_event(event)

        self.assertEqual(len(repository.steps), 1)
        self.assertEqual(repository.steps[0]["step_id"], "step-1")

    async def test_child_runner_returns_non_recursive_bundle(self) -> None:
        runner = ChildAgentAuditRunner()
        payload = {
            "query": "ping",
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
                "scenario_name": "diagnosis",
                "user_id": "demo.user",
                "tenant_id": "merchant-data",
                "tags": [],
                "meta": {},
            },
        }

        async def handler(context, audit_logger, request_payload):
            del context, audit_logger
            return {
                "reply": "ok",
                "evidence": [{"query": request_payload["query"]}],
            }

        result = await runner.run(
            request_payload=payload,
            agent_name="child-agent",
            handler=handler,
            source_name="child-service",
            workflow_name="wf",
            scenario_name="diagnosis",
        )

        self.assertEqual(result["reply"], "ok")
        self.assertIn("audit_bundle", result)
        self.assertEqual(result["audit_bundle"]["invocations"][0]["output_payload"]["reply"], "ok")


if __name__ == "__main__":
    unittest.main()
