# Frontend Dashboard Run Guide

This project now includes an independent npm frontend:

- Path: `frontend-dashboard`
- Local URL: `http://127.0.0.1:5173`

## 1) Start backend APIs

At minimum, start `audit_ingest_api.py` with valid DB connection and token:

```powershell
$env:PYTHONPATH="$PWD\src"
$env:AGENT_AUDIT_PG_DSN="postgresql://user:password@127.0.0.1:5432/agent_audit"
$env:AUDIT_INGEST_TOKEN="ingest-token"
uvicorn audit_ingest_api:app --host 127.0.0.1 --port 8081
```

## 2) Configure frontend env

```powershell
cd frontend-dashboard
copy .env.example .env
```

Optional: edit `.env`:

- `VITE_AUDIT_BASE_URL`
- `VITE_AUDIT_TOKEN`
- `VITE_DEFAULT_TENANT_ID`
- `VITE_DEFAULT_USER_ID`

## 3) Start frontend

```powershell
cd frontend-dashboard
npm install
npm run dev -- --host 127.0.0.1 --port 5173
```

## 4) What the page shows

- Session totals and status cards
- Status distribution
- Session table with filters
- Session snapshot and task list
