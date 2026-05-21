# Frontend Dashboard

Independent npm project for audit/session visualization.

## Quick Start

```bash
cd frontend-dashboard
npm install
cp .env.example .env
npm run dev
```

Default local URL:

- `http://127.0.0.1:5173`

## Environment Variables

- `VITE_AUDIT_BASE_URL`: audit ingest API base URL.
- `VITE_AUDIT_TOKEN`: bearer token for audit API.
- `VITE_DEFAULT_TENANT_ID`: default tenant filter.
- `VITE_DEFAULT_USER_ID`: default user filter.

## Current Views

- Session total and status cards
- Status distribution pills
- Recent sessions table
- Session snapshot with task list
