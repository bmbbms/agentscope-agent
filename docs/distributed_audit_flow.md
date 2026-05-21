# Distributed Audit Flow For Remote Child Agents

## Goal

The main platform should see both:

- the remote child-agent call itself
- the child agent's internal invocation and step chain

## How it works

1. The main platform creates the root `AuditContext`.
2. It calls a child agent and passes:
   - `query`
   - `audit_context`
3. The child agent creates a new local `run_id` but keeps:
   - the same `trace_id`
   - the same `task_id`
   - the same `request_id`
   - `parent_run_id = main_platform_run_id`
4. The child agent logs its own invocation and steps and immediately pushes audit events to the central ingest API.
5. The child agent returns only the business response.
6. The central ingest API writes those events into the shared audit tables.

## Resulting chain

```text
main platform invocation
-> remote_agent_call step
-> child agent invocation.start event
-> child tool step 1 event
-> child tool step 2 event
-> child agent invocation.finish event
-> ...
```

All records share the same `trace_id`, and the child invocation points back to the parent through `parent_run_id`.

## Key files

- [remote_agents.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/src/merchant_data_agent/remote_agents.py)
- [distributed.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/src/department_agent_audit/distributed.py)
- [event_ingest.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/src/department_agent_audit/event_ingest.py)
- [audit_ingest_api.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/audit_ingest_api.py)
- [child_agent_http_example.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/child_agent_http_example.py)

## Deployment choices

This scaffold now prefers active audit event ingestion:

1. The main platform includes `audit_sink` in each child-agent request.
2. The child agent uses `HttpAuditIngestRepository`.
3. Every invocation and step is POSTed to `/audit/events`.
4. The central ingest API persists those events immediately.

The old `audit_bundle` path remains only as a fallback when no `audit_sink` is configured.
