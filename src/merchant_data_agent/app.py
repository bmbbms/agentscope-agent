from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from department_agent_audit.audit import AuditContext, AuditLogger
from department_agent_audit.eval_agent import AgentScopeLLMJudge
from department_agent_audit.eval_worker import EvalWorker
from department_agent_audit.session_manager import SessionManager

from .agents import MerchantAgents
from .remote_agents import RemoteAgentRegistry
from .tools import MerchantDataTools


def _route_by_rule(query: str) -> str:
    lowered = query.lower()
    metric_markers = ["metric", "definition", "formula", "dimension", "calculation"]
    data_query_markers = [
        "sql",
        "select ",
        " from ",
        "database",
        "schema",
        "table",
        "column",
        "field",
        "export excel",
        "superset",
        "data query",
        "\u6570\u636e\u67e5\u8be2",
        "\u67e5\u8be2",
        "\u67e5\u6570",
        "\u67e5\u5e93",
        "\u67e5\u8868",
        "\u5b57\u6bb5",
        "\u8868\u7ed3\u6784",
        "\u6570\u636e\u5e93",
        "\u6267\u884csql",
        "\u5bfc\u51faexcel",
        "\u7edf\u8ba1",
        "\u603b\u8ba1",
        "\u603b\u548c",
        "\u6d41\u6c34",
        "\u4ea4\u6613",
        "\u89c4\u6a21",
        "\u591a\u5c11",
    ]
    report_markers = [
        "report",
        "summary",
        "weekly",
        "daily",
        "review",
        "dashboard",
        "month",
        "monthly",
        "reporting",
        "\u62a5\u544a",
        "\u6708\u62a5",
        "\u770b\u677f",
        "\u62a5\u8868",
        "\u751f\u6210\u62a5\u544a",
    ]
    if any(marker in lowered for marker in metric_markers):
        return "metric_definition"
    if any(marker in lowered for marker in data_query_markers):
        return "data_query"
    if any(marker in lowered for marker in report_markers):
        return "report"
    return "diagnosis"


@dataclass(slots=True)
class MerchantDepartmentApp:
    audit_logger: AuditLogger
    agents: MerchantAgents | None
    tools: MerchantDataTools | None
    eval_worker: EvalWorker
    session_manager: SessionManager | None = None
    remote_registry: RemoteAgentRegistry | None = None

    async def handle_query(
        self,
        *,
        query: str,
        user_id: str,
        tenant_id: str = "merchant-data",
        source_type: str = "web_app",
        trigger_type: str = "manual",
        session_id: str | None = None,
        task_id: str | None = None,
        topic: str | None = None,
        user_explicitly_closed: bool = False,
        extra_payload: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        route = _route_by_rule(query)
        agent_name = self._agent_name_for_route(route)

        session = None
        task = None
        if self.session_manager is not None:
            session, task = await self.session_manager.ensure_session_and_task(
                query=query,
                user_id=user_id,
                tenant_id=tenant_id,
                source_type=source_type,
                session_id=session_id,
                task_id=task_id,
                topic=topic,
                task_type=route,
                assigned_agent=agent_name,
            )

        context, agent_name = AuditContext.new(
            session_id=session.session_id if session else session_id,
            source_type=source_type,
            trigger_type=trigger_type,
            agent_name=agent_name,
            workflow_name="merchant_department_workflow",
            scenario_name=route,
            user_id=user_id,
            tenant_id=tenant_id,
            tags=[route],
        )
        if task is not None:
            context.task_id = task.task_id

        try:
            if self.remote_registry is not None:
                result = await self.remote_registry.invoke_with_audit(
                    route=route,
                    query=query,
                    context=context,
                    audit_logger=self.audit_logger,
                    extra_payload=extra_payload if route == "data_query" else None,
                )
                return await self._finalize_response(
                    result=result,
                    session=session,
                    task=task,
                    context=context,
                    trigger_type=trigger_type,
                    user_explicitly_closed=user_explicitly_closed,
                )

            async def _call() -> dict[str, Any]:
                if self.tools is None:
                    raise RuntimeError("Local tool mode is disabled and no remote registry is configured.")
                if route == "metric_definition":
                    tool_result = await self.tools.explain_metric_definition(query)
                    return {
                        "route": route,
                        "reply": tool_result["definition"],
                        "tool_result": tool_result,
                    }
                if route == "report":
                    facts = [{"source": "placeholder", "detail": "Replace with real analysis output"}]
                    tool_result = await self.tools.build_report(query, facts)
                    return {
                        "route": route,
                        "reply": tool_result["report"],
                        "tool_result": tool_result,
                    }
                if route == "data_query":
                    return {
                        "route": route,
                        "reply": "Local data_query mode is not implemented. Configure the remote data_query child agent.",
                        "tool_result": {"query": query, "route": route},
                    }
                tool_result = await self.tools.diagnose_metric_drop(query)
                return {
                    "route": route,
                    "reply": tool_result["summary"],
                    "tool_result": tool_result,
                }

            result = await self.audit_logger.invoke_with_audit(
                context,
                agent_name=agent_name,
                input_payload={"query": query, "route": route},
                agent_call=_call,
            )
            return await self._finalize_response(
                result=result,
                session=session,
                task=task,
                context=context,
                trigger_type=trigger_type,
                user_explicitly_closed=user_explicitly_closed,
            )
        except Exception as exc:
            await self._finalize_failure(
                session=session,
                task=task,
                context=context,
                trigger_type=trigger_type,
                error=exc,
            )
            raise

    async def run_eval_once(self, worker_id: str = "merchant-eval-worker-1") -> Any:
        return await self.eval_worker.run_once(worker_id=worker_id)

    @staticmethod
    def _agent_name_for_route(route: str) -> str:
        mapping = {
            "metric_definition": "metric_definition_agent",
            "diagnosis": "merchant_diagnosis_agent",
            "report": "report_agent",
            "data_query": "superset_data_query_agent",
        }
        return mapping[route]

    async def _finalize_response(
        self,
        *,
        result: dict[str, Any],
        session: Any,
        task: Any,
        context: AuditContext,
        trigger_type: str,
        user_explicitly_closed: bool,
    ) -> dict[str, Any]:
        if self.session_manager is None or session is None or task is None:
            return result
        lifecycle = await self.session_manager.finalize_run(
            session=session,
            task=task,
            run_id=context.run_id,
            run_status="success",
            trigger_type=trigger_type,
            user_explicitly_closed=user_explicitly_closed,
        )
        result["session"] = lifecycle["session"]
        result["task"] = lifecycle["task"]
        result["lifecycle_decision"] = lifecycle["decision"]
        return result

    async def _finalize_failure(
        self,
        *,
        session: Any,
        task: Any,
        context: AuditContext,
        trigger_type: str,
        error: Exception,
    ) -> None:
        if self.session_manager is None or session is None or task is None:
            return
        task.meta = {
            **dict(task.meta),
            "last_error_type": type(error).__name__,
            "last_error_message": str(error),
        }
        await self.session_manager.finalize_run(
            session=session,
            task=task,
            run_id=context.run_id,
            run_status="failed",
            trigger_type=trigger_type,
            user_explicitly_closed=False,
        )


def build_eval_worker(repository: Any, agents: MerchantAgents) -> EvalWorker:
    judge = AgentScopeLLMJudge(agents.evaluator)
    return EvalWorker(repository, judge)
