# Ticket 04 Handoff

## Next Ticket

- Ticket: `TKT-2026-06-22-aew-v05-04-steering-decisions-context-budget`
- Canonical source: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-04-steering-decisions-context-budget.yaml`
- Repository execution copy target: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-04-steering-decisions-context-budget.yaml`

## Context To Carry Forward

- Repository version remains `0.3.0`; do not bump version before ticket 12.
- Ticket 03 added `templates/specs/TEMPLATE.delta-spec.md` and drift verifier guidance.
- Non-trivial tickets should record `execution_result.spec_alignment`.
- Accepted delta specs must update durable specs or record owner/follow-up.
- Ticket 04 should extend ticket templates with decision locks and context budgets without removing `spec_refs`, `expert_routing`, or drift fields.
- The pre-existing package ZIP under `tickets/` remains unrelated and must stay unstaged.

## Ticket 04 Path Map

Allowed by the canonical ticket:

- `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-04-steering-decisions-context-budget.yaml`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-04-steering-decisions-context-budget/**`
- `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md`
- `agent/**`
- `templates/steering/**`
- `templates/AGENTS.md.template`
- `templates/TEMPLATE.ticket.yaml`
- `templates/TEMPLATE.orchestrator-ticket.yaml`
- `prompts/**`
- `checklists/**`
- `docs/workflow.md`
