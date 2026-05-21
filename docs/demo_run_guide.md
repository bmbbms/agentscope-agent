# Demo Run Guide

This guide wires the current scaffold into a single runnable path.

## 1. Prerequisites

- PostgreSQL 15+
- Python 3.11+
- `asyncpg` installed

## 2. Apply schema

Run:

```sql
\i sql/audit_schema.sql
```

## 3. Set environment variable

PowerShell:

```powershell
$env:AGENT_AUDIT_PG_DSN="postgresql://user:password@localhost:5432/agent_audit"
```

## 4. Install local package path

From the workspace root:

```powershell
$env:PYTHONPATH="$PWD\\src"
```

## 5. Run the demo

```powershell
python demo_app.py
```

The demo does three things:

1. executes one merchant diagnosis run
2. writes invocation data into `agent_invocation_log`
3. consumes one queued evaluation and writes `agent_eval_result`

## 6. Replace demo components

- `DemoMerchantAgent`: replace with your real AgentScope business workflow
- `DemoEvaluatorAgent`: replace with your real AgentScope evaluator agent
- `PostgresAuditRepository`: keep as the production repository layer
