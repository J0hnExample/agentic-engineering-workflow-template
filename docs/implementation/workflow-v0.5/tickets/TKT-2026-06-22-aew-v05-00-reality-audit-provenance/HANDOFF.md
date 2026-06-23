# Ticket 01 Handoff

## Next Ticket

- Ticket: `TKT-2026-06-22-aew-v05-01-native-subagents-expert-routing`
- Canonical source: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-01-native-subagents-expert-routing.yaml`
- Repository execution copy target: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-01-native-subagents-expert-routing.yaml`
- Depends on: ticket 00 completion and review.

## Required Startup Checks

Run the active-ticket source-lock validation for ticket 01 before planning or implementation. Re-check branch, HEAD/upstream, origin URL, version, status, and the pre-existing package zip path.

## Context To Carry Forward

- Repository is still version `0.3.0`; do not bump version before ticket 12.
- v0.4 `expert-routing-profiles` maps to ticket 01.
- `feature/sdd-workflow-v0.4.0` is read-only evidence at `9fbab079609f8f4ff634d9b44da0599cffcf7982`; do not merge, cherry-pick, or apply it.
- Pre-existing artifact `tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip` must remain untouched and unstaged.
- Ticket 00 created the v0.5 plan, traceability, contracts, context ledger, and ticket-local records under `docs/implementation/workflow-v0.5/`.

## Ticket 01 Path Map

Allowed by the canonical ticket:

- `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-01-native-subagents-expert-routing.yaml`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-01-native-subagents-expert-routing/**`
- `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md`
- `agent/**`
- `.codex/**`
- `prompts/**`
- `templates/**`
- `checklists/**`
- `docs/workflow.md`
- `README.md`

Ticket 01 should add native Codex custom-agent profiles with bounded concurrency and read-only planning/review/blocker/audit roles while preserving markdown prompt fallbacks.
