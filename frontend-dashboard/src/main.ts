import "./style.css";

type SessionStatsResponse = {
  total: number;
  by_status: Record<string, number>;
};

type TaskStatsResponse = {
  total: number;
  running: number;
  completed: number;
  failed: number;
  completion_rate: number;
  failure_rate: number;
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

type TaskItem = {
  task_id: string;
  session_id: string;
  title: string | null;
  task_type: string | null;
  status: string;
  waiting_state: string | null;
  assigned_agent: string | null;
  started_at: string;
  last_active_at: string;
  completed_at: string | null;
};

type TaskListResponse = {
  items: TaskItem[];
  limit: number;
  offset: number;
  count: number;
};

type SessionSnapshotResponse = {
  session: SessionItem;
  tasks: TaskItem[];
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
        <h1>Merchant Agent Operations Dashboard</h1>
        <p class="subtext">Sessions, tasks, and completion progress for main-agent and child-agent execution.</p>
      </div>
      <div class="endpoint">${auditBaseUrl}</div>
    </header>

    <section class="filters">
      <label>Tenant ID <input id="tenantId" type="text" /></label>
      <label>User ID <input id="userId" type="text" /></label>
      <label>Status
        <select id="status">
          <option value="">all</option>
          <option value="running">running</option>
          <option value="success">success</option>
          <option value="failed">failed</option>
          <option value="completed">completed</option>
          <option value="closed">closed</option>
          <option value="waiting_human">waiting_human</option>
        </select>
      </label>
      <label>Limit <input id="limit" type="number" min="1" max="200" value="50" /></label>
      <button id="refreshBtn" type="button">Refresh</button>
    </section>

    <section class="section">
      <div class="section-title-row">
        <h2>Session Overview</h2>
      </div>
      <section class="cards" id="sessionCards"></section>
      <section class="status-breakdown" id="sessionStatusBreakdown"></section>
    </section>

    <section class="section">
      <div class="section-title-row">
        <h2>Task Completion</h2>
      </div>
      <section class="cards task-cards" id="taskCards"></section>
      <section class="status-breakdown" id="taskStatusBreakdown"></section>
    </section>

    <section class="panel">
      <div class="panel-header">
        <h2>Recent Tasks</h2>
        <div id="errorText" class="error-text"></div>
      </div>
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Task</th>
              <th>Status</th>
              <th>Type</th>
              <th>Assigned Agent</th>
              <th>Session</th>
              <th>Last Active</th>
            </tr>
          </thead>
          <tbody id="tasksTableBody"></tbody>
        </table>
      </div>
    </section>

    <section class="panel">
      <div class="panel-header">
        <h2>Recent Sessions</h2>
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
      <div id="snapshotContent" class="snapshot-empty">Select a session to inspect task details.</div>
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
const sessionCards = mustGet<HTMLElement>("#sessionCards");
const taskCards = mustGet<HTMLElement>("#taskCards");
const sessionStatusBreakdown = mustGet<HTMLElement>("#sessionStatusBreakdown");
const taskStatusBreakdown = mustGet<HTMLElement>("#taskStatusBreakdown");
const tasksTableBody = mustGet<HTMLTableSectionElement>("#tasksTableBody");
const sessionsTableBody = mustGet<HTMLTableSectionElement>("#sessionsTableBody");
const snapshotContent = mustGet<HTMLElement>("#snapshotContent");
const errorText = mustGet<HTMLElement>("#errorText");

tenantInput.value = defaultTenant;
userInput.value = defaultUser;

let autoRefreshHandle: number | null = null;

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

function renderStatusPills(container: HTMLElement, stats: Record<string, number>): void {
  const entries = Object.entries(stats);
  if (entries.length === 0) {
    container.innerHTML = `<div class="status-pill">No status data</div>`;
    return;
  }
  container.innerHTML = entries
    .sort((a, b) => b[1] - a[1])
    .map(([status, count]) => `<div class="status-pill"><span>${escapeHtml(status)}</span><strong>${count}</strong></div>`)
    .join("");
}

function renderSessionCards(stats: SessionStatsResponse): void {
  sessionCards.innerHTML = `
    <article class="metric"><span>Total Sessions</span><strong>${stats.total}</strong></article>
    <article class="metric"><span>Active</span><strong>${stats.by_status.active || 0}</strong></article>
    <article class="metric"><span>Completed</span><strong>${stats.by_status.completed || 0}</strong></article>
    <article class="metric"><span>Closed</span><strong>${stats.by_status.closed || 0}</strong></article>
    <article class="metric"><span>Waiting Human</span><strong>${stats.by_status.waiting_human || 0}</strong></article>
  `;
}

function renderTaskCards(stats: TaskStatsResponse): void {
  taskCards.innerHTML = `
    <article class="metric emphasis"><span>Total Tasks</span><strong>${stats.total}</strong></article>
    <article class="metric emphasis"><span>Running Now</span><strong>${stats.running}</strong></article>
    <article class="metric emphasis"><span>Completed</span><strong>${stats.completed}</strong></article>
    <article class="metric emphasis"><span>Failed</span><strong>${stats.failed}</strong></article>
    <article class="metric emphasis"><span>Completion Rate</span><strong>${stats.completion_rate}%</strong></article>
  `;
}

function renderSessions(listing: SessionListResponse): void {
  if (listing.items.length === 0) {
    sessionsTableBody.innerHTML = `<tr><td colspan="6" class="empty-row">No sessions found.</td></tr>`;
    return;
  }
  sessionsTableBody.innerHTML = listing.items
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

function renderTasks(listing: TaskListResponse): void {
  if (listing.items.length === 0) {
    tasksTableBody.innerHTML = `<tr><td colspan="6" class="empty-row">No tasks found.</td></tr>`;
    return;
  }
  tasksTableBody.innerHTML = listing.items
    .map(
      (item) => `
        <tr>
          <td><code>${item.task_id}</code></td>
          <td><span class="status-tag">${escapeHtml(item.status)}</span></td>
          <td>${escapeHtml(item.task_type || "-")}</td>
          <td>${escapeHtml(item.assigned_agent || "-")}</td>
          <td><code>${escapeHtml(item.session_id)}</code></td>
          <td>${fmtTime(item.last_active_at)}</td>
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

function buildQuery(limit: number): URLSearchParams {
  const tenant = tenantInput.value.trim();
  const user = userInput.value.trim();
  const status = statusInput.value.trim();
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
  return query;
}

function buildStatsQuery(): URLSearchParams {
  const tenant = tenantInput.value.trim();
  const user = userInput.value.trim();
  const query = new URLSearchParams();
  if (tenant) {
    query.set("tenant_id", tenant);
  }
  if (user) {
    query.set("user_id", user);
  }
  return query;
}

async function loadDashboard(): Promise<void> {
  errorText.textContent = "";
  refreshBtn.disabled = true;
  refreshBtn.textContent = "Loading...";
  try {
    const limit = Number(limitInput.value) || 50;
    const query = buildQuery(limit);
    const statsQuery = buildStatsQuery();

    const [sessionStats, taskStats, sessions, tasks] = await Promise.all([
      apiGet<SessionStatsResponse>(`/audit/sessions/stats?${statsQuery.toString()}`),
      apiGet<TaskStatsResponse>(`/audit/tasks/stats?${statsQuery.toString()}`),
      apiGet<SessionListResponse>(`/audit/sessions?${query.toString()}`),
      apiGet<TaskListResponse>(`/audit/tasks?${query.toString()}`),
    ]);

    renderSessionCards(sessionStats);
    renderTaskCards(taskStats);
    renderStatusPills(sessionStatusBreakdown, sessionStats.by_status);
    renderStatusPills(taskStatusBreakdown, taskStats.by_status);
    renderSessions(sessions);
    renderTasks(tasks);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    errorText.textContent = message;
    sessionCards.innerHTML = "";
    taskCards.innerHTML = "";
    sessionStatusBreakdown.innerHTML = "";
    taskStatusBreakdown.innerHTML = "";
    tasksTableBody.innerHTML = `<tr><td colspan="6" class="empty-row">Failed to load tasks.</td></tr>`;
    sessionsTableBody.innerHTML = `<tr><td colspan="6" class="empty-row">Failed to load sessions.</td></tr>`;
  } finally {
    refreshBtn.disabled = false;
    refreshBtn.textContent = "Refresh";
  }
}

sessionsTableBody.addEventListener("click", async (event) => {
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

if (autoRefreshHandle !== null) {
  window.clearInterval(autoRefreshHandle);
}
autoRefreshHandle = window.setInterval(() => {
  void loadDashboard();
}, 15000);

void loadDashboard();
