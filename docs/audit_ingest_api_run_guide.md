# Audit Ingest API Run Guide

## Purpose

This service is the central receiver for child-agent audit events.

## Environment

PowerShell:

```powershell
$env:AGENT_AUDIT_PG_DSN="postgresql://user:password@localhost:5432/agent_audit"
$env:AUDIT_INGEST_TOKEN="replace-me"
$env:PYTHONPATH="$PWD\\src"
```

## Start the API

```powershell
uvicorn audit_ingest_api:app --host 0.0.0.0 --port 8081
```

## Child-agent request path

The main platform should pass:

```json
{
  "query": "帮我分析昨天核心商户GMV异常下滑原因",
  "audit_context": {
    "trace_id": "...",
    "task_id": "...",
    "request_id": "...",
    "parent_run_id": "...",
    "user_id": "demo.analyst"
  },
  "audit_sink": {
    "url": "http://main-platform.internal:8081/audit/events",
    "auth_token": "replace-me",
    "timeout_seconds": 10
  }
}
```

## Event types

- `invocation.start`
- `invocation.finish`
- `invocation.upsert`
- `step.upsert`
- `eval.enqueue`
- `eval.result`

## Event envelope

Each event sent to `/audit/events` now includes:

- `event_id`
- `event_type`
- `trace_id`
- `run_id`
- `producer_service`
- `occurred_at`
- `payload`

This lets the ingest API deduplicate retried events by `event_id`.

## Trace query

To fetch the full central view for one trace:

```powershell
curl -H "Authorization: Bearer $env:AUDIT_INGEST_TOKEN" http://localhost:8081/audit/traces/<trace_id>
```

## Dead letters

List open dead-letter events:

```powershell
curl -H "Authorization: Bearer $env:AUDIT_INGEST_TOKEN" "http://localhost:8081/audit/events/dead-letters?status=open&limit=100"
```

Replay one failed event:

```powershell
curl -X POST -H "Authorization: Bearer $env:AUDIT_INGEST_TOKEN" http://localhost:8081/audit/events/replay/<event_id>
```
