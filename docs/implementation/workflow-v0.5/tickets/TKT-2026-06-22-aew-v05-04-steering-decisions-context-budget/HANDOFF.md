# Ticket 05 Handoff

## Next Ticket

- Ticket: `TKT-2026-06-22-aew-v05-05-quick-flow-single-ticket`
- Canonical source: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-05-quick-flow-single-ticket.yaml`
- Repository execution copy target: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-05-quick-flow-single-ticket.yaml`

## Context To Carry Forward

- Repository version remains `0.3.0`; do not bump version before ticket 12.
- Ticket 04 added steering templates plus `decision_locks`, `context_budget`, and `steering` fields.
- Ticket 05 should preserve `spec_refs`, `expert_routing`, drift fields, decision locks, and context budgets while defining quick-flow and autonomous single-ticket behavior.
- Quick no-spec remains allowed only for tiny low-risk work with a concrete reason.
- The pre-existing package ZIP under `tickets/` remains unrelated and must stay unstaged.

## Ticket 05 Path Map

Allowed by the canonical ticket:

- `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-05-quick-flow-single-ticket.yaml`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-05-quick-flow-single-ticket/**`
- `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md`
- `agent/**`
- `prompts/quick-dev.md`
- `prompts/run-single-ticket-autonomously.md`
- `templates/TEMPLATE.quick-ticket.yaml`
- `templates/TEMPLATE.ticket.yaml`
- `templates/TEMPLATE.execution-result.yaml`
- `checklists/**`
- `docs/workflow.md`
- `templates/AGENTS.md.template`
- `README.md`
