-- Department-level agent audit schema
-- Target dialect: PostgreSQL 15+

create table if not exists agent_invocation_log (
    id bigserial primary key,
    session_id varchar(64),
    trace_id varchar(64) not null,
    task_id varchar(64) not null,
    request_id varchar(64) not null,
    run_id varchar(64) not null unique,
    schedule_id varchar(64),
    parent_run_id varchar(64),
    source_type varchar(32) not null,
    source_name varchar(128),
    trigger_type varchar(32) not null,
    agent_name varchar(128) not null,
    workflow_name varchar(128),
    scenario_name varchar(128),
    user_id varchar(128),
    tenant_id varchar(128),
    input_summary text,
    output_summary text,
    input_payload jsonb,
    output_payload jsonb,
    status varchar(32) not null,
    system_success boolean not null default false,
    execution_success boolean not null default false,
    business_success boolean,
    error_code varchar(64),
    error_message text,
    started_at timestamptz not null,
    finished_at timestamptz,
    latency_ms integer,
    prompt_tokens integer,
    completion_tokens integer,
    total_tokens integer,
    estimated_cost numeric(18, 6),
    tags jsonb not null default '[]'::jsonb,
    meta jsonb not null default '{}'::jsonb,
    created_at timestamptz not null default now()
);

create index if not exists idx_agent_invocation_trace_id
    on agent_invocation_log (trace_id);

create index if not exists idx_agent_invocation_session_id
    on agent_invocation_log (session_id, started_at desc);

create index if not exists idx_agent_invocation_started_at
    on agent_invocation_log (started_at desc);

create index if not exists idx_agent_invocation_agent_status
    on agent_invocation_log (agent_name, status, started_at desc);

create index if not exists idx_agent_invocation_schedule_id
    on agent_invocation_log (schedule_id, started_at desc);


create table if not exists agent_step_log (
    id bigserial primary key,
    trace_id varchar(64) not null,
    run_id varchar(64) not null,
    step_id varchar(64) not null unique,
    parent_step_id varchar(64),
    step_type varchar(32) not null,
    step_name varchar(128) not null,
    sequence_no integer not null,
    target_name varchar(128),
    input_summary text,
    output_summary text,
    input_payload jsonb,
    output_payload jsonb,
    status varchar(32) not null,
    success boolean not null default false,
    error_code varchar(64),
    error_message text,
    started_at timestamptz not null,
    finished_at timestamptz,
    latency_ms integer,
    token_usage jsonb,
    meta jsonb not null default '{}'::jsonb,
    created_at timestamptz not null default now()
);

create index if not exists idx_agent_step_trace_run
    on agent_step_log (trace_id, run_id, sequence_no);

create index if not exists idx_agent_step_type_status
    on agent_step_log (step_type, status, started_at desc);


create table if not exists schedule_run_log (
    id bigserial primary key,
    schedule_id varchar(64) not null,
    schedule_name varchar(128) not null,
    cron_expr varchar(64) not null,
    owner_team varchar(128),
    trace_id varchar(64),
    request_id varchar(64),
    planned_at timestamptz not null,
    triggered_at timestamptz not null,
    started_at timestamptz,
    finished_at timestamptz,
    status varchar(32) not null,
    success boolean not null default false,
    retry_count integer not null default 0,
    delay_seconds integer,
    timeout_seconds integer,
    sla_breached boolean not null default false,
    missed_run boolean not null default false,
    output_summary text,
    error_code varchar(64),
    error_message text,
    meta jsonb not null default '{}'::jsonb,
    created_at timestamptz not null default now()
);

create index if not exists idx_schedule_run_schedule_time
    on schedule_run_log (schedule_id, planned_at desc);

create index if not exists idx_schedule_run_status
    on schedule_run_log (status, triggered_at desc);


create table if not exists agent_eval_result (
    id bigserial primary key,
    trace_id varchar(64) not null,
    run_id varchar(64) not null,
    eval_id varchar(64) not null unique,
    evaluator_name varchar(128) not null,
    evaluator_version varchar(64),
    eval_mode varchar(32) not null,
    rule_passed boolean,
    llm_passed boolean,
    overall_passed boolean not null default false,
    score_total numeric(5, 2),
    score_task_completion numeric(5, 2),
    score_factual_grounding numeric(5, 2),
    score_metric_consistency numeric(5, 2),
    score_actionability numeric(5, 2),
    score_safety_compliance numeric(5, 2),
    issue_tags jsonb not null default '[]'::jsonb,
    findings jsonb not null default '[]'::jsonb,
    suggestions jsonb not null default '[]'::jsonb,
    evidence jsonb not null default '[]'::jsonb,
    raw_judge jsonb,
    evaluated_at timestamptz not null,
    latency_ms integer,
    created_at timestamptz not null default now()
);

create index if not exists idx_agent_eval_run_id
    on agent_eval_result (run_id, evaluated_at desc);

create index if not exists idx_agent_eval_trace_id
    on agent_eval_result (trace_id, evaluated_at desc);


create table if not exists agent_eval_queue (
    id bigserial primary key,
    queue_item_id varchar(64) not null unique,
    trace_id varchar(64) not null,
    run_id varchar(64) not null,
    priority integer not null default 100,
    status varchar(32) not null,
    attempts integer not null default 0,
    available_at timestamptz not null,
    locked_at timestamptz,
    locked_by varchar(128),
    payload jsonb not null,
    error_message text,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create index if not exists idx_agent_eval_queue_status_available
    on agent_eval_queue (status, available_at asc, priority asc);


create table if not exists conversation_session (
    id bigserial primary key,
    session_id varchar(64) not null unique,
    tenant_id varchar(128),
    user_id varchar(128),
    topic varchar(256),
    status varchar(32) not null,
    waiting_state varchar(32),
    current_task_id varchar(64),
    opened_at timestamptz not null,
    last_active_at timestamptz not null,
    closed_at timestamptz,
    close_reason varchar(64),
    source_type varchar(32),
    source_name varchar(128),
    meta jsonb not null default '{}'::jsonb,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create index if not exists idx_conversation_session_status
    on conversation_session (status, last_active_at desc);

create index if not exists idx_conversation_session_user
    on conversation_session (tenant_id, user_id, last_active_at desc);


create table if not exists conversation_task (
    id bigserial primary key,
    task_id varchar(64) not null unique,
    session_id varchar(64) not null,
    parent_task_id varchar(64),
    tenant_id varchar(128),
    user_id varchar(128),
    title varchar(256),
    task_type varchar(64),
    status varchar(32) not null,
    waiting_state varchar(32),
    priority integer not null default 100,
    requested_by varchar(128),
    assigned_agent varchar(128),
    started_at timestamptz not null,
    last_active_at timestamptz not null,
    completed_at timestamptz,
    closed_reason varchar(64),
    meta jsonb not null default '{}'::jsonb,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create index if not exists idx_conversation_task_session
    on conversation_task (session_id, last_active_at desc);

create index if not exists idx_conversation_task_status
    on conversation_task (status, last_active_at desc);


create table if not exists audit_ingest_event (
    id bigserial primary key,
    event_id varchar(64) not null unique,
    trace_id varchar(64),
    run_id varchar(64),
    event_type varchar(64) not null,
    producer_service varchar(128),
    occurred_at timestamptz not null,
    received_at timestamptz not null default now(),
    status varchar(32) not null,
    payload jsonb not null,
    error_message text
);

create index if not exists idx_audit_ingest_trace_id
    on audit_ingest_event (trace_id, occurred_at desc);

create index if not exists idx_audit_ingest_run_id
    on audit_ingest_event (run_id, occurred_at desc);


create table if not exists audit_ingest_dead_letter (
    id bigserial primary key,
    event_id varchar(64) not null unique,
    trace_id varchar(64),
    run_id varchar(64),
    event_type varchar(64) not null,
    producer_service varchar(128),
    occurred_at timestamptz not null,
    failed_at timestamptz not null default now(),
    status varchar(32) not null,
    replay_count integer not null default 0,
    last_replayed_at timestamptz,
    resolved_at timestamptz,
    payload jsonb not null,
    error_message text
);

create index if not exists idx_audit_dead_letter_status
    on audit_ingest_dead_letter (status, failed_at desc);

create index if not exists idx_audit_dead_letter_trace_id
    on audit_ingest_dead_letter (trace_id, failed_at desc);


create or replace view v_agent_daily_overview as
select
    date_trunc('day', started_at) as stat_day,
    agent_name,
    count(*) as total_calls,
    count(*) filter (where system_success) as system_success_calls,
    count(*) filter (where execution_success) as execution_success_calls,
    count(*) filter (where business_success is true) as business_success_calls,
    round(avg(latency_ms)::numeric, 2) as avg_latency_ms,
    percentile_cont(0.95) within group (order by latency_ms) as p95_latency_ms,
    sum(total_tokens) as total_tokens,
    sum(estimated_cost) as total_cost
from agent_invocation_log
group by 1, 2;


create or replace view v_schedule_daily_overview as
select
    date_trunc('day', triggered_at) as stat_day,
    schedule_name,
    count(*) as total_runs,
    count(*) filter (where success) as success_runs,
    count(*) filter (where missed_run) as missed_runs,
    count(*) filter (where sla_breached) as sla_breached_runs,
    round(avg(delay_seconds)::numeric, 2) as avg_delay_seconds
from schedule_run_log
group by 1, 2;
