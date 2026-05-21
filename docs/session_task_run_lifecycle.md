# Session / Task / Run Lifecycle

## Three different completion concepts

For a department-level agent system, these must stay separate:

1. `run`: one execution chain
2. `task`: one business goal
3. `session`: one ongoing collaboration context

## Definitions

### Run

A run is one concrete execution triggered by:

- one user message
- one scheduled execution
- one delegated child-agent invocation

Typical run statuses:

- `running`
- `success`
- `failed`
- `timeout`
- `cancelled`

### Task

A task is a business objective that may contain multiple runs.

Examples:

- investigate a merchant anomaly
- generate a weekly report
- create and confirm a merchant follow-up list

Typical task statuses:

- `running`
- `success`
- `failed`
- `waiting_user`
- `waiting_human`
- `scheduled_pending`
- `cancelled`

### Session

A session is a sustained collaboration window, not just one question.

Typical session statuses:

- `active`
- `idle`
- `waiting_user`
- `waiting_human`
- `completed`
- `closed`
- `archived`

## Core rule

`run success` does not mean `session closed`.

The normal progression is:

```text
run completes
-> task may or may not complete
-> session may stay open for follow-up
```

## Recommended close policy

Close a session only when one of these is true:

1. the user explicitly closes it
2. it has been idle beyond timeout
3. all task work is finished and the session can be safely closed

## Data model

The schema adds:

- `conversation_session`
- `conversation_task`
- `session_id` on `agent_invocation_log`

## Code support

See [lifecycle.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/src/department_agent_audit/lifecycle.py).

The helper `decide_lifecycle_transition()` answers:

- should the task be marked complete?
- should the session stay open?
- is the system waiting on user/human/scheduled work?
- should the session close now or later?
