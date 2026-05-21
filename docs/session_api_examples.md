# Session API Examples

This document provides practical request/response examples for session operations.

## Base assumptions

- Service URL: `http://localhost:8081`
- Token env: `AUDIT_INGEST_TOKEN`
- Header: `Authorization: Bearer <token>`

## 1) List sessions

Request:

```bash
curl -H "Authorization: Bearer $AUDIT_INGEST_TOKEN" \
  "http://localhost:8081/audit/sessions?status=active&tenant_id=merchant-data&limit=20&offset=0"
```

Response example:

```json
{
  "items": [
    {
      "session_id": "a8f3c8b0e6f14687b8d7ecf5e4297f19",
      "tenant_id": "merchant-data",
      "user_id": "demo.analyst",
      "topic": "gmv anomaly review",
      "status": "active",
      "waiting_state": null,
      "current_task_id": "f214f0fef0434ec1b495556f7d5c95eb",
      "opened_at": "2026-05-21T10:00:00+00:00",
      "last_active_at": "2026-05-21T10:04:17+00:00",
      "closed_at": null,
      "close_reason": null,
      "source_type": "web_app",
      "source_name": null,
      "meta": {
        "source_type": "web_app"
      }
    }
  ],
  "limit": 20,
  "offset": 0,
  "count": 1
}
```

## 2) Session status stats

Request:

```bash
curl -H "Authorization: Bearer $AUDIT_INGEST_TOKEN" \
  "http://localhost:8081/audit/sessions/stats?tenant_id=merchant-data"
```

Response example:

```json
{
  "total": 27,
  "by_status": {
    "active": 8,
    "completed": 11,
    "closed": 7,
    "waiting_human": 1
  }
}
```

## 3) Session snapshot

Request:

```bash
curl -H "Authorization: Bearer $AUDIT_INGEST_TOKEN" \
  "http://localhost:8081/audit/sessions/a8f3c8b0e6f14687b8d7ecf5e4297f19?task_limit=50"
```

Response example:

```json
{
  "session": {
    "session_id": "a8f3c8b0e6f14687b8d7ecf5e4297f19",
    "tenant_id": "merchant-data",
    "user_id": "demo.analyst",
    "topic": "gmv anomaly review",
    "status": "completed",
    "waiting_state": null,
    "current_task_id": "f214f0fef0434ec1b495556f7d5c95eb",
    "opened_at": "2026-05-21T10:00:00+00:00",
    "last_active_at": "2026-05-21T10:05:01+00:00",
    "closed_at": null,
    "close_reason": null,
    "source_type": "web_app",
    "source_name": null,
    "meta": {
      "source_type": "web_app"
    }
  },
  "tasks": [
    {
      "task_id": "f214f0fef0434ec1b495556f7d5c95eb",
      "session_id": "a8f3c8b0e6f14687b8d7ecf5e4297f19",
      "tenant_id": "merchant-data",
      "user_id": "demo.analyst",
      "title": "analyze yesterday gmv drop",
      "task_type": "diagnosis",
      "status": "success",
      "waiting_state": null,
      "priority": 100,
      "assigned_agent": "merchant_diagnosis_agent",
      "started_at": "2026-05-21T10:00:01+00:00",
      "last_active_at": "2026-05-21T10:05:01+00:00",
      "completed_at": "2026-05-21T10:05:01+00:00",
      "closed_reason": null,
      "meta": {
        "assigned_agent": "merchant_diagnosis_agent"
      }
    }
  ]
}
```

## 4) Close a session

Request:

```bash
curl -X POST -H "Authorization: Bearer $AUDIT_INGEST_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"closed_by":"ops.user"}' \
  "http://localhost:8081/audit/sessions/a8f3c8b0e6f14687b8d7ecf5e4297f19/close"
```

Response example:

```json
{
  "session": {
    "session_id": "a8f3c8b0e6f14687b8d7ecf5e4297f19",
    "tenant_id": "merchant-data",
    "user_id": "demo.analyst",
    "topic": "gmv anomaly review",
    "status": "closed",
    "waiting_state": null,
    "current_task_id": "f214f0fef0434ec1b495556f7d5c95eb",
    "opened_at": "2026-05-21T10:00:00+00:00",
    "last_active_at": "2026-05-21T10:06:43+00:00",
    "closed_at": "2026-05-21T10:06:43+00:00",
    "close_reason": "user_closed",
    "meta": {
      "source_type": "web_app",
      "closed_by": "ops.user"
    }
  }
}
```
