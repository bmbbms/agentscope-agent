# Minimal Main-Child Agent MVP

This guide runs one complete call chain:

`client -> main agent -> child agent -> audit ingest`

## 1) Prepare environment

PowerShell:

```powershell
$env:PYTHONPATH="$PWD\src"
$env:AGENT_AUDIT_PG_DSN="postgresql://user:password@localhost:5432/agent_audit"
$env:AUDIT_INGEST_TOKEN="ingest-token"
$env:MAIN_AGENT_API_TOKEN="main-token"
```

Apply schema once:

```powershell
psql -d agent_audit -f sql/audit_schema.sql
```

## 2) Configure remote child agents for main service

PowerShell example:

```powershell
$env:MERCHANT_REMOTE_AGENTS_JSON='[
  {"name":"diagnosis","protocol":"http","url":"http://127.0.0.1:8091/invoke"},
  {"name":"metric_definition","protocol":"http","url":"http://127.0.0.1:8091/invoke"},
  {"name":"report","protocol":"http","url":"http://127.0.0.1:8091/invoke"}
]'
$env:AUDIT_INGEST_URL="http://127.0.0.1:8081/audit/events"
```

## 3) Start three services

Terminal A:

```powershell
uvicorn audit_ingest_api:app --host 127.0.0.1 --port 8081
```

Terminal B:

```powershell
uvicorn child_agent_http_example:app --host 127.0.0.1 --port 8091
```

Terminal C:

```powershell
uvicorn main_agent_http_api:app --host 127.0.0.1 --port 8090
```

## 4) Send one main-agent request

```powershell
curl -X POST "http://127.0.0.1:8090/main/query" `
  -H "Authorization: Bearer $env:MAIN_AGENT_API_TOKEN" `
  -H "Content-Type: application/json" `
  -d '{"query":"analyze yesterday core merchant gmv drop","user_id":"demo.analyst","tenant_id":"merchant-data"}'
```

Expected response includes:

- `reply` from child-agent execution
- `session` and `task` state
- `lifecycle_decision`

## 5) Inspect trace and session

Use ingest API:

```powershell
curl -H "Authorization: Bearer $env:AUDIT_INGEST_TOKEN" "http://127.0.0.1:8081/audit/sessions?tenant_id=merchant-data"
```

```powershell
curl -H "Authorization: Bearer $env:AUDIT_INGEST_TOKEN" "http://127.0.0.1:8081/audit/sessions/stats?tenant_id=merchant-data"
```

```powershell
curl -H "Authorization: Bearer $env:AUDIT_INGEST_TOKEN" "http://127.0.0.1:8081/audit/traces/<trace_id>"
```
