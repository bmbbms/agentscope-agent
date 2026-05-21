# Department Agent Audit Architecture

This scaffold treats audit and evaluation as first-class workflow stages around AgentScope agents.

## 1. Core idea

Every invocation becomes a measurable run with:

- `trace_id`: full request chain
- `task_id`: business task
- `request_id`: entry request
- `run_id`: concrete agent execution
- `schedule_id`: scheduled job identity when applicable

## 2. Required data products

The schema in [audit_schema.sql](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/sql/audit_schema.sql) creates:

- `agent_invocation_log`: one row per run
- `agent_step_log`: one row per internal step or tool call
- `schedule_run_log`: one row per scheduled execution
- `agent_eval_result`: one row per evaluation
- `agent_eval_queue`: async evaluation queue

The two views provide a useful first dashboard layer:

- `v_agent_daily_overview`
- `v_schedule_daily_overview`

## 3. Runtime flow

```text
request/schedule trigger
-> invoke_with_audit()
-> agent/tool execution
-> invocation log finish
-> enqueue evaluation
-> async eval worker
-> evaluation result table
-> BI dashboard / alerts
```

## 4. Python modules

- [audit.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/src/department_agent_audit/audit.py): audit context, invocation wrapper, step logging
- [eval_worker.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/src/department_agent_audit/eval_worker.py): rules + LLM evaluation worker
- [storage.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/src/department_agent_audit/storage.py): repository abstraction
- [agentscope_adapter.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/src/department_agent_audit/agentscope_adapter.py): thin integration example

## 5. Production integration notes

1. Replace `AuditRepository` stubs with your real storage layer.
2. Replace `StubLLMJudge` with an AgentScope evaluator agent.
3. Wrap every SQL/API/tool call with `tool_step()` so failures are visible in the audit trail.
4. Feed `agent_invocation_log`, `schedule_run_log`, and `agent_eval_result` into BI.
5. Add alerts for:
   - schedule missed runs
   - schedule SLA breaches
   - agent failure rate spikes
   - evaluation pass-rate drops

## 6. Recommended dashboard metrics

- total calls
- system success rate
- execution success rate
- business success rate
- average latency
- P95 latency
- total tokens
- total cost
- eval pass rate
- low-score runs
- schedule on-time rate
- schedule missed-run count

## 7. Suggested next step

After this scaffold, the best next implementation slice is:

1. bind the repository to PostgreSQL
2. wrap one real AgentScope workflow with `invoke_with_audit()`
3. run one async evaluator worker
4. build one dashboard page over the two daily views
