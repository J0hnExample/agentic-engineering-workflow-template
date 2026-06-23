# Ticket 03 Handoff

## Next Ticket

- Ticket: `TKT-2026-06-22-aew-v05-03-delta-spec-drift-verification`
- Canonical source: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-03-delta-spec-drift-verification.yaml`
- Repository execution copy target: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-03-delta-spec-drift-verification.yaml`

## Context To Carry Forward

- Repository version remains `0.3.0`; do not bump version before ticket 12.
- Ticket 02 added SDD requirements, design, and tasks templates with stable IDs and explicit statuses.
- `templates/TEMPLATE.ticket.yaml` and `templates/TEMPLATE.orchestrator-ticket.yaml` now include `spec_refs`.
- Quick low-risk tickets may use `mode: no_spec` only with a concrete not-required reason.
- Ticket 03 should extend the new spec artifacts with delta lifecycle and drift verification, not replace them.
- The pre-existing package ZIP under `tickets/` remains unrelated and must stay unstaged.

## Ticket 03 Path Map

Allowed by the canonical ticket:

- `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-03-delta-spec-drift-verification.yaml`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-03-delta-spec-drift-verification/**`
- `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md`
- `agent/**`
- `templates/specs/**`
- `docs/spec_lifecycle.md`
- `docs/workflow.md`
- `prompts/spec-drift-verifier.md`
- `prompts/final-verifier.md`
- `checklists/spec-drift.md`
- `checklists/closeout.md`
- `templates/TEMPLATE.execution-result.yaml`
- `templates/TEMPLATE.ticket.yaml`
- `templates/AGENTS.md.template`
