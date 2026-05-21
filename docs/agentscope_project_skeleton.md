# AgentScope Project Skeleton

This is the first production-oriented project layout for a merchant data department agent.

The recommended deployment mode is:

- main platform: routing, audit, evaluation, scheduling, dashboard
- child agents: independent services reached over HTTP or A2A

## Structure

- [src/merchant_data_agent/settings.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/src/merchant_data_agent/settings.py): environment-driven runtime settings
- [src/merchant_data_agent/prompts.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/src/merchant_data_agent/prompts.py): system prompts for router, metric, diagnosis, report, and evaluator agents
- [src/merchant_data_agent/tools.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/src/merchant_data_agent/tools.py): business tool stubs
- [src/merchant_data_agent/agents.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/src/merchant_data_agent/agents.py): AgentScope ReAct agent builders
- [src/merchant_data_agent/remote_agents.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/src/merchant_data_agent/remote_agents.py): protocol-based remote child-agent clients
- [src/merchant_data_agent/app.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/src/merchant_data_agent/app.py): department app orchestration with audit integration
- [agentscope_demo.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/agentscope_demo.py): end-to-end bootstrap demo
- [remote_agents_demo.py](/C:/Users/yangsheng/Documents/Codex/2026-05-21/agentscope-agent/remote_agents_demo.py): remote child-agent orchestration demo

## Current design choice

The app currently supports two modes:

- local mode: AgentScope agents and local tools
- remote mode: child agents exposed as HTTP or A2A services
- both modes still use the same audit/evaluation wrapper

This is intentional. It keeps routing predictable while your team validates:

- audit field completeness
- evaluation signal quality
- dashboard metric definitions
- data permission boundaries

## Recommended evolution

1. Expose each specialized child agent as a separate service.
2. Register them through `MERCHANT_REMOTE_AGENTS_JSON`.
3. Keep the main platform focused on routing, policy, audit, scheduling, and evaluation.
4. Wrap each remote call with `tool_step()` from the audit layer.
5. Add scheduled workflows for anomaly scan, report generation, and merchant watchlists.
6. Feed the audit tables into BI for team-level observability.

## Why this shape works

For department-level agents, the hard part is not the first answer. It is the operating model:

- what ran
- why it ran
- whether it succeeded
- whether it was useful
- whether scheduled jobs stayed healthy

This scaffold keeps those concerns visible from day one.
