import "./style.css";

type SessionStatsResponse = {
  total: number;
  by_status: Record<string, number>;
};

type SessionItem = {
  session_id: string;
  tenant_id: string | null;
  user_id: string | null;
  topic: string | null;
  status: string;
  waiting_state: string | null;
  current_task_id: string | null;
  opened_at: string;
  last_active_at: string;
  closed_at: string | null;
  close_reason: string | null;
};

type SessionListResponse = {
  items: SessionItem[];
  limit: number;
  offset: number;
  count: number;
};

type SessionTask = {
  task_id: string;
  title: string | null;
  task_type: string | null;
  status: string;
  assigned_agent: string | null;
  started_at: string;
  last_active_at: string;
  completed_at: string | null;
};

type SessionSnapshotResponse = {
  session: SessionItem;
  tasks: SessionTask[];
};

const auditBaseUrl = (import.meta.env.VITE_AUDIT_BASE_URL as string | undefined)?.trim() || "http://127.0.0.1:8081";
const auditToken = (import.meta.env.VITE_AUDIT_TOKEN as string | undefined)?.trim() || "ingest-token";
const defaultTenant = (import.meta.env.VITE_DEFAULT_TENANT_ID as string | undefined)?.trim() || "merchant-data";
const defaultUser = (import.meta.env.VITE_DEFAULT_USER_ID as string | undefined)?.trim() || "";

const app = document.querySelector<HTMLDivElement>("#app");
if (!app) {
  throw new Error("Missing #app container");
}

app.innerHTML = `
  <main class="layout">
    <header class="topbar">
      <div>
        <h1>Merchant Agent Audit Dashboard</h1>
        <p class="subtext">Session-level visibility for main-agent and child-agent calls.</p>
      </div>
      <div class="endpoint">${auditBaseUrl}</div>
    </header>

    <section class="filters">
      <label>Tenant ID <input id="tenantId" type="text" /></label>
      <label>User ID <input id="userId" type="text" /></label>
      <label>Status
        <select id="status">
          <option value="">all</option>
          <option value="active">active</option>
          <option value="completed">completed</option>
          <option value="closed">closed</option>
          <option value="waiting_human">waiting_human</option>
        </select>
      </label>
      <label>Limit <input id="limit" type="number" min="1" max="200" value="50" /></label>
      <button id="refreshBtn" type="button">Refresh</button>
    </section>

    <section class="cards" id="cards"></section>
    <section class="status-breakdown" id="statusBreakdown"></section>

    <section class="panel">
      <div class="panel-header">
        <h2>Recent Sessions</h2>
        <div id="errorText" class="error-text"></div>
      </div>
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Session</th>
              <th>Status</th>
              <th>User</th>
              <th>Topic</th>
              <th>Last Active</th>
              <th></th>
            </tr>
          </thead>
          <tbody id="sessionsTableBody"></tbody>
        </table>
      </div>
    </section>

    <section class="panel" id="snapshotPanel">
      <div class="panel-header">
        <h2>Session Snapshot</h2>
      </div>
      <div id="snapshotContent" class="snapshot-empty">Select a session to inspect its tasks.</div>
    </section>
  </main>
`;

function mustGet<T extends Element>(selector: string): T {
  const element = document.querySelector(selector);
  if (!element) {
    throw new Error(`Missing element: ${selector}`);
  }
  return element as T;
}

const tenantInput = mustGet<HTMLInputElement>("#tenantId");
const userInput = mustGet<HTMLInputElement>("#userId");
const statusInput = mustGet<HTMLSelectElement>("#status");
const limitInput = mustGet<HTMLInputElement>("#limit");
const refreshBtn = mustGet<HTMLButtonElement>("#refreshBtn");
const cardsContainer = mustGet<HTMLElement>("#cards");
const statusBreakdown = mustGet<HTMLElement>("#statusBreakdown");
const tableBody = mustGet<HTMLTableSectionElement>("#sessionsTableBody");
const snapshotContent = mustGet<HTMLElement>("#snapshotContent");
const errorText = mustGet<HTMLElement>("#errorText");

tenantInput.value = defaultTenant;
userInput.value = defaultUser;

async function apiGet<T>(path: string): Promise<T> {
  const headers: Record<string, string> = {};
  if (auditToken) {
    headers.Authorization = `Bearer ${auditToken}`;
  }
  const response = await fetch(`${auditBaseUrl}${path}`, { headers });
  if (!response.ok) {
    const detail = await response.text();
    throw new Error(`HTTP ${response.status}: ${detail}`);
  }
  return (await response.json()) as T;
}

function fmtTime(value: string | null): string {
  if (!value) {
    return "-";
  }
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) {
    return value;
  }
  return date.toLocaleString();
}

function escapeHtml(value: string): string {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function renderCards(stats: SessionStatsResponse): void {
  const active = stats.by_status.active || 0;
  const completed = stats.by_status.completed || 0;
  const closed = stats.by_status.closed || 0;
  const waitingHuman = stats.by_status.waiting_human || 0;
  cardsContainer.innerHTML = `
    <article class="metric"><span>Total Sessions</span><strong>${stats.total}</strong></article>
    <article class="metric"><span>Active</span><strong>${active}</strong></article>
    <article class="metric"><span>Completed</span><strong>${completed}</strong></article>
    <article class="metric"><span>Closed</span><strong>${closed}</strong></article>
    <article class="metric"><span>Waiting Human</span><strong>${waitingHuman}</strong></article>
  `;
}

function renderStatusBreakdown(stats: SessionStatsResponse): void {
  const entries = Object.entries(stats.by_status);
  if (entries.length === 0) {
    statusBreakdown.innerHTML = `<div class="status-pill">No status data</div>`;
    return;
  }
  statusBreakdown.innerHTML = entries
    .sort((a, b) => b[1] - a[1])
    .map(([status, count]) => `<div class="status-pill"><span>${escapeHtml(status)}</span><strong>${count}</strong></div>`)
    .join("");
}

function renderSessions(listing: SessionListResponse): void {
  if (listing.items.length === 0) {
    tableBody.innerHTML = `<tr><td colspan="6" class="empty-row">No sessions found.</td></tr>`;
    return;
  }
  tableBody.innerHTML = listing.items
    .map(
      (item) => `
        <tr>
          <td><code>${item.session_id}</code></td>
          <td><span class="status-tag">${escapeHtml(item.status)}</span></td>
          <td>${escapeHtml(item.user_id || "-")}</td>
          <td title="${escapeHtml(item.topic || "-")}">${escapeHtml(item.topic || "-")}</td>
          <td>${fmtTime(item.last_active_at)}</td>
          <td><button class="ghost" data-session-id="${item.session_id}" type="button">View</button></td>
        </tr>
      `,
    )
    .join("");
}

function renderSnapshot(snapshot: SessionSnapshotResponse): void {
  const taskRows = snapshot.tasks.length
    ? snapshot.tasks
        .map(
          (task) => `
            <tr>
              <td><code>${task.task_id}</code></td>
              <td>${escapeHtml(task.task_type || "-")}</td>
              <td>${escapeHtml(task.status)}</td>
              <td>${escapeHtml(task.assigned_agent || "-")}</td>
              <td>${fmtTime(task.last_active_at)}</td>
            </tr>
          `,
        )
        .join("")
    : `<tr><td colspan="5" class="empty-row">No task data.</td></tr>`;

  snapshotContent.innerHTML = `
    <div class="snapshot-grid">
      <div><span>Session</span><code>${snapshot.session.session_id}</code></div>
      <div><span>Status</span><strong>${escapeHtml(snapshot.session.status)}</strong></div>
      <div><span>User</span><strong>${escapeHtml(snapshot.session.user_id || "-")}</strong></div>
      <div><span>Current Task</span><code>${escapeHtml(snapshot.session.current_task_id || "-")}</code></div>
      <div><span>Opened At</span><strong>${fmtTime(snapshot.session.opened_at)}</strong></div>
      <div><span>Last Active</span><strong>${fmtTime(snapshot.session.last_active_at)}</strong></div>
    </div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Task ID</th>
            <th>Type</th>
            <th>Status</th>
            <th>Assigned Agent</th>
            <th>Last Active</th>
          </tr>
        </thead>
        <tbody>${taskRows}</tbody>
      </table>
    </div>
  `;
}

async function loadDashboard(): Promise<void> {
  errorText.textContent = "";
  refreshBtn.disabled = true;
  refreshBtn.textContent = "Loading...";
  try {
    const tenant = tenantInput.value.trim();
    const user = userInput.value.trim();
    const status = statusInput.value.trim();
    const limit = Number(limitInput.value) || 50;
    const query = new URLSearchParams();
    query.set("limit", String(limit));
    query.set("offset", "0");
    if (tenant) {
      query.set("tenant_id", tenant);
    }
    if (user) {
      query.set("user_id", user);
    }
    if (status) {
      query.set("status", status);
    }
    const statsQuery = new URLSearchParams();
    if (tenant) {
      statsQuery.set("tenant_id", tenant);
    }
    if (user) {
      statsQuery.set("user_id", user);
    }

    const [stats, sessions] = await Promise.all([
      apiGet<SessionStatsResponse>(`/audit/sessions/stats?${statsQuery.toString()}`),
      apiGet<SessionListResponse>(`/audit/sessions?${query.toString()}`),
    ]);
    renderCards(stats);
    renderStatusBreakdown(stats);
    renderSessions(sessions);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    errorText.textContent = message;
    cardsContainer.innerHTML = "";
    statusBreakdown.innerHTML = "";
    tableBody.innerHTML = `<tr><td colspan="6" class="empty-row">Failed to load data.</td></tr>`;
  } finally {
    refreshBtn.disabled = false;
    refreshBtn.textContent = "Refresh";
  }
}

tableBody.addEventListener("click", async (event) => {
  const target = event.target;
  if (!(target instanceof HTMLElement)) {
    return;
  }
  if (target.tagName !== "BUTTON") {
    return;
  }
  const sessionId = target.getAttribute("data-session-id");
  if (!sessionId) {
    return;
  }
  target.setAttribute("disabled", "true");
  target.textContent = "Loading...";
  try {
    const snapshot = await apiGet<SessionSnapshotResponse>(
      `/audit/sessions/${encodeURIComponent(sessionId)}?task_limit=200`,
    );
    renderSnapshot(snapshot);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    snapshotContent.textContent = `Failed to load snapshot: ${message}`;
  } finally {
    target.removeAttribute("disabled");
    target.textContent = "View";
  }
});

refreshBtn.addEventListener("click", () => {
  void loadDashboard();
});

void loadDashboard();
