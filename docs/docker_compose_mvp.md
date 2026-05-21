# Docker Compose MVP

This is the fastest way to run the minimal main-child-agent chain.

## Services

- `postgres` (database)
- `audit-ingest` (central audit + session API)
- `child-agent` (remote child service)
- `main-agent` (main orchestrator API)

## Start

```bash
docker compose up --build
```

## Smoke call

```bash
curl -X POST "http://127.0.0.1:8090/main/query" \
  -H "Authorization: Bearer main-token" \
  -H "Content-Type: application/json" \
  -d '{"query":"analyze yesterday core merchant gmv drop","user_id":"demo.analyst","tenant_id":"merchant-data"}'
```

## Session query

```bash
curl -H "Authorization: Bearer ingest-token" "http://127.0.0.1:8081/audit/sessions"
```

```bash
curl -H "Authorization: Bearer ingest-token" "http://127.0.0.1:8081/audit/sessions/stats"
```

## Trace query

```bash
curl -H "Authorization: Bearer ingest-token" "http://127.0.0.1:8081/audit/traces/<trace_id>"
```

## Stop

```bash
docker compose down
```

If you also want to remove persisted database data:

```bash
docker compose down -v
```
