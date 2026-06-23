# Ticket 02 Handoff

## Next Ticket

- Ticket: `TKT-2026-06-22-aew-v05-02-sdd-spec-artifacts`
- Canonical source: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-02-sdd-spec-artifacts.yaml`
- Repository execution copy target: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-02-sdd-spec-artifacts.yaml`

## Context To Carry Forward

- Repository version remains `0.3.0`; do not bump version before ticket 12.
- Ticket 01 added project-scoped native Codex profiles under `.codex/agents/*.toml` and global subagent limits under `.codex/config.toml`.
- `workflow-ticket-implementer` is the only implementation writer profile.
- Planning, review, blocker, release-audit, and expert profiles are read-only.
- Markdown prompts remain fallbacks when native profiles are unavailable.
- Ticket templates now include `expert_routing`; ticket 02 should preserve that block while adding SDD artifact references.
- The pre-existing package ZIP under `tickets/` remains unrelated and must stay unstaged.

## Ticket 02 Path Map

Allowed by the canonical ticket:

- `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-02-sdd-spec-artifacts.yaml`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-02-sdd-spec-artifacts/**`
- `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md`
- `agent/**`
- `templates/specs/**`
- `templates/TEMPLATE.ticket.yaml`
- `templates/TEMPLATE.orchestrator-ticket.yaml`
- `templates/AGENTS.md.template`
- `prompts/**`
- `checklists/**`
- `docs/workflow.md`
