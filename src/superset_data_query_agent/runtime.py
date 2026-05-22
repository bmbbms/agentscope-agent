from __future__ import annotations

import importlib.util
import json
import os
from dataclasses import dataclass
from typing import Any

from .prompts import DATA_QUERY_GUARD_PROMPT, DATA_QUERY_PLANNER_PROMPT
from .query_service import SupersetDataQueryService, SupersetQueryRequestSpec


@dataclass(slots=True)
class DataQueryWorkflowResult:
    action: str
    should_execute: bool
    planner_output: dict[str, Any]
    guard_output: dict[str, Any] | None
    service_result: dict[str, Any] | None

    def to_dict(self) -> dict[str, Any]:
        return {
            "action": self.action,
            "should_execute": self.should_execute,
            "planner_output": self.planner_output,
            "guard_output": self.guard_output,
            "service_result": self.service_result,
        }


class AgentScopeDataQueryWorkflow:
    def __init__(self, service: SupersetDataQueryService):
        self.service = service
        self._planner_agent: Any | None = None
        self._guard_agent: Any | None = None
        self._agentscope_initialized = False

    async def run(self, spec: SupersetQueryRequestSpec) -> DataQueryWorkflowResult:
        if not self.is_enabled():
            return self._run_without_runtime(spec)
        return await self._run_with_runtime(spec)

    @staticmethod
    def is_enabled() -> bool:
        return bool(os.getenv("OPENAI_API_KEY", "").strip()) and importlib.util.find_spec("agentscope") is not None

    async def _run_with_runtime(self, spec: SupersetQueryRequestSpec) -> DataQueryWorkflowResult:
        planner = self._get_planner_agent()
        guard = self._get_guard_agent()

        planner_prompt = self._build_planner_prompt(spec)
        planner_output = self._parse_json_reply(await self._invoke_agent(planner, planner_prompt))

        action = str(planner_output.get("action") or spec.action).strip().lower() or "schema_search"
        should_execute = bool(planner_output.get("should_execute", action != "schema_search"))
        planned_sql = planner_output.get("sql") or spec.sql
        database_name = planner_output.get("database_name") or spec.database_name
        schema_keyword = planner_output.get("schema_keyword") or spec.schema_keyword or spec.query

        if action != "sql_query":
            service_result = self.service.handle(
                SupersetQueryRequestSpec(
                    query=spec.query,
                    action=action,
                    sql=None,
                    database_name=database_name,
                    preview_rows=spec.preview_rows,
                    enable_mask=spec.enable_mask,
                    export_excel=False,
                    export_name=spec.export_name,
                    schema_keyword=schema_keyword,
                    search_limit=spec.search_limit,
                    output_dir=spec.output_dir,
                    timeout_seconds=spec.timeout_seconds,
                )
            )
            return DataQueryWorkflowResult(
                action=action,
                should_execute=False,
                planner_output=planner_output,
                guard_output=None,
                service_result=service_result,
            )

        guard_prompt = self._build_guard_prompt(
            spec=spec,
            planner_output=planner_output,
            sql=planned_sql,
            database_name=database_name,
        )
        guard_output = self._parse_json_reply(await self._invoke_agent(guard, guard_prompt))
        approved = bool(guard_output.get("approved", False))
        safe_sql = guard_output.get("safe_sql") or planned_sql

        if not approved or not should_execute:
            return DataQueryWorkflowResult(
                action=action,
                should_execute=False,
                planner_output=planner_output,
                guard_output=guard_output,
                service_result=None,
            )

        service_result = self.service.handle(
            SupersetQueryRequestSpec(
                query=spec.query,
                action="sql_query",
                sql=safe_sql,
                database_name=database_name,
                preview_rows=spec.preview_rows,
                enable_mask=spec.enable_mask,
                export_excel=spec.export_excel,
                export_name=spec.export_name,
                schema_keyword=schema_keyword,
                search_limit=spec.search_limit,
                output_dir=spec.output_dir,
                timeout_seconds=spec.timeout_seconds,
            )
        )
        return DataQueryWorkflowResult(
            action=action,
            should_execute=True,
            planner_output=planner_output,
            guard_output=guard_output,
            service_result=service_result,
        )

    def _run_without_runtime(self, spec: SupersetQueryRequestSpec) -> DataQueryWorkflowResult:
        planner_output = self._fallback_plan(spec)
        action = planner_output["action"]
        guard_output: dict[str, Any] | None = None
        service_result: dict[str, Any] | None = None

        if action == "sql_query":
            guard_output = self._fallback_guard(spec, planner_output)
            if guard_output["approved"]:
                effective_sql = guard_output.get("safe_sql") or spec.sql
                service_result = self.service.handle(
                    SupersetQueryRequestSpec(
                        query=spec.query,
                        action="sql_query",
                        sql=effective_sql,
                        database_name=planner_output.get("database_name") or spec.database_name,
                        preview_rows=spec.preview_rows,
                        enable_mask=spec.enable_mask,
                        export_excel=spec.export_excel,
                        export_name=spec.export_name,
                        schema_keyword=planner_output.get("schema_keyword") or spec.schema_keyword,
                        search_limit=spec.search_limit,
                        output_dir=spec.output_dir,
                        timeout_seconds=spec.timeout_seconds,
                    )
                )
            return DataQueryWorkflowResult(
                action=action,
                should_execute=guard_output["approved"],
                planner_output=planner_output,
                guard_output=guard_output,
                service_result=service_result,
            )

        service_result = self.service.handle(
            SupersetQueryRequestSpec(
                query=spec.query,
                action=action,
                sql=None,
                database_name=planner_output.get("database_name") or spec.database_name,
                preview_rows=spec.preview_rows,
                enable_mask=spec.enable_mask,
                export_excel=False,
                export_name=spec.export_name,
                schema_keyword=planner_output.get("schema_keyword") or spec.schema_keyword or spec.query,
                search_limit=spec.search_limit,
                output_dir=spec.output_dir,
                timeout_seconds=spec.timeout_seconds,
            )
        )
        return DataQueryWorkflowResult(
            action=action,
            should_execute=False,
            planner_output=planner_output,
            guard_output=guard_output,
            service_result=service_result,
        )

    def _get_planner_agent(self):
        if self._planner_agent is None:
            self._planner_agent = self._build_agent("data_query_planner_agent", DATA_QUERY_PLANNER_PROMPT)
        return self._planner_agent

    def _get_guard_agent(self):
        if self._guard_agent is None:
            self._guard_agent = self._build_agent("data_query_guard_agent", DATA_QUERY_GUARD_PROMPT)
        return self._guard_agent

    def _build_agent(self, name: str, sys_prompt: str):
        import agentscope
        from agentscope.agent import ReActAgent
        from agentscope.formatter import OpenAIChatFormatter
        from agentscope.memory import InMemoryMemory
        from agentscope.model import OpenAIChatModel
        from agentscope.tool import Toolkit

        client_kwargs = {}
        base_url = os.getenv("OPENAI_BASE_URL", "").strip()
        if base_url:
            client_kwargs["base_url"] = base_url

        if not self._agentscope_initialized:
            agentscope.init(project="superset-data-query-sub-agent")
            self._agentscope_initialized = True
        model = OpenAIChatModel(
            model_name=os.getenv("AGENTSCOPE_MODEL_NAME", "gpt-4o-mini"),
            api_key=os.getenv("OPENAI_API_KEY", "").strip(),
            client_kwargs=client_kwargs,
            stream=False,
        )
        return ReActAgent(
            name=name,
            sys_prompt=sys_prompt,
            model=model,
            formatter=OpenAIChatFormatter(),
            memory=InMemoryMemory(),
            toolkit=Toolkit(),
        )

    @staticmethod
    async def _invoke_agent(agent: Any, prompt: str) -> Any:
        from agentscope.message import Msg

        return await agent(
            Msg(
                name="data_query_user",
                role="user",
                content=prompt,
            )
        )

    @staticmethod
    def _build_planner_prompt(spec: SupersetQueryRequestSpec) -> str:
        payload = {
            "query": spec.query,
            "requested_action": spec.action,
            "sql": spec.sql,
            "database_name": spec.database_name,
            "schema_keyword": spec.schema_keyword,
            "export_excel": spec.export_excel,
            "preview_rows": spec.preview_rows,
        }
        return json.dumps(payload, ensure_ascii=False, indent=2)

    @staticmethod
    def _build_guard_prompt(
        *,
        spec: SupersetQueryRequestSpec,
        planner_output: dict[str, Any],
        sql: str | None,
        database_name: str | None,
    ) -> str:
        payload = {
            "query": spec.query,
            "database_name": database_name,
            "sql": sql,
            "planner_output": planner_output,
            "export_excel": spec.export_excel,
            "timeout_seconds": spec.timeout_seconds,
        }
        return json.dumps(payload, ensure_ascii=False, indent=2)

    @staticmethod
    def _parse_json_reply(reply: Any) -> dict[str, Any]:
        if isinstance(reply, str):
            text = reply
        else:
            text = getattr(reply, "content", str(reply))
        text = text.strip()
        if text.startswith("```"):
            text = text.strip("`")
            if text.lower().startswith("json"):
                text = text[4:].strip()
        return json.loads(text)

    @staticmethod
    def _fallback_plan(spec: SupersetQueryRequestSpec) -> dict[str, Any]:
        action = spec.action.lower()
        if action == "schema_search":
            return {
                "action": "schema_search",
                "should_execute": False,
                "database_name": spec.database_name,
                "schema_keyword": spec.schema_keyword or spec.query,
                "sql": None,
                "reason": "Fallback planner chose schema search for safer discovery.",
                "risk_flags": [],
                "candidate_tables": [],
                "assumptions": [],
            }
        if action == "list_databases":
            return {
                "action": "list_databases",
                "should_execute": False,
                "database_name": None,
                "schema_keyword": None,
                "sql": None,
                "reason": "Fallback planner chose database listing.",
                "risk_flags": [],
                "candidate_tables": [],
                "assumptions": [],
            }
        return {
            "action": "sql_query",
            "should_execute": True,
            "database_name": spec.database_name,
            "schema_keyword": spec.schema_keyword,
            "sql": spec.sql,
            "reason": "Fallback planner accepted explicit SQL request.",
            "risk_flags": [],
            "candidate_tables": [],
            "assumptions": [],
        }

    @staticmethod
    def _fallback_guard(spec: SupersetQueryRequestSpec, planner_output: dict[str, Any]) -> dict[str, Any]:
        sql = (planner_output.get("sql") or spec.sql or "").strip()
        lowered = sql.lower()
        risk_flags: list[str] = []
        required_fixes: list[str] = []

        if not sql:
            risk_flags.append("missing_sql")
            required_fixes.append("Provide explicit SQL before execution.")
        if any(token in lowered for token in ("insert ", "update ", "delete ", "drop ", "alter ", "truncate ")):
            risk_flags.append("non_readonly_sql")
            required_fixes.append("Only read-only SQL is allowed.")
        if "select *" in lowered:
            risk_flags.append("select_star")
            required_fixes.append("Select explicit fields instead of select *.")

        approved = not risk_flags
        return {
            "approved": approved,
            "reason": "Fallback guard approved explicit read-only SQL." if approved else "Fallback guard blocked SQL execution.",
            "risk_flags": risk_flags,
            "required_fixes": required_fixes,
            "safe_sql": sql if approved else None,
        }
