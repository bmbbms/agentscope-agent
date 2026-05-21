# Session Manager Integration

This integration makes `session`, `task`, and `run` part of the actual request flow.

## What now happens on each request

1. `MerchantDepartmentApp.handle_query()` receives optional:
   - `session_id`
   - `task_id`
   - `topic`
   - `user_explicitly_closed`
2. `SessionManager.ensure_session_and_task()`:
   - creates or refreshes a session
   - creates or refreshes a task
3. `AuditContext` is created with `session_id`
4. the business run executes
5. `SessionManager.finalize_run()` updates:
   - task status
   - session status
   - close decision

## Current scope

This is the minimal useful lifecycle integration:

- sessions are persisted
- tasks are persisted
- invocations are linked to `session_id`
- lifecycle decisions are returned in the business response

## What is still intentionally simple

- no separate session API yet
- no branching task tree management yet
- no schedule-to-session linkage yet
- no UI layer yet

## Current API endpoints

The central service now provides:

- `GET /audit/sessions?status=active&tenant_id=...&user_id=...&limit=100&offset=0`: list sessions with filters
- `GET /audit/sessions/stats?tenant_id=...&user_id=...`: status aggregation stats
- `GET /audit/sessions/{session_id}?task_limit=200`: returns session + task snapshot
- `POST /audit/sessions/{session_id}/close`: closes one session

Close request body (optional):

```json
{
  "closed_by": "operator.name"
}
```
