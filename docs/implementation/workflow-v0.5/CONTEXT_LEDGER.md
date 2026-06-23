# Workflow v0.5 Context Ledger

## Ticket 00 Context

- Active ticket: `TKT-2026-06-22-aew-v05-00-reality-audit-provenance`.
- Canonical ticket file: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-00-reality-audit-provenance.yaml`.
- Repository execution copy: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-00-reality-audit-provenance.yaml`.
- Package root: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade`.
- Repository root: `/home/sascha/workspace/agentic-engineering-workflow-template`.
- Start branch and HEAD: `main` at `612d8a3f165eb3c3a127fe7478f405d2ad415802`, tracking `origin/main`.
- Current public version: `0.3.0`.
- Pre-existing unrelated/generated path: `tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip`.
- No repository-local ticket source collisions were found before ticket 00 records were created.

## Evidence Sources

- `00_START_HERE.md`: canonical package entry point, source-lock policy, per-ticket sequence, and autonomous delivery policy.
- `CURRENT_REPOSITORY_BASELINE.md`: package-observed public `0.3.0` baseline, subject to runtime verification.
- `reference/V0_4_REQUIREMENT_MAP.md`: imported v0.4-to-v0.5 mapping.
- `reference/v0.4-ticketpack-source/tickets/sdd-upgrade/*.yaml`: imported v0.4 ticket provenance.
- `manifest.json` and `runtime/RUN_STATE.json`: package ticket order and controller state.
- `feature/sdd-workflow-v0.4.0` at `9fbab079609f8f4ff634d9b44da0599cffcf7982`: read-only evidence only.

## Managed Paths For Ticket 00

- `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-00-reality-audit-provenance.yaml`
- `docs/implementation/workflow-v0.5/GLOBAL_PLAN.md`
- `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md`
- `docs/implementation/workflow-v0.5/REQUIREMENT_TRACEABILITY.md`
- `docs/implementation/workflow-v0.5/CROSS_TICKET_CONTRACTS.md`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-00-reality-audit-provenance/PLAN.md`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-00-reality-audit-provenance/BASELINE.md`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-00-reality-audit-provenance/EXECUTION_REPORT.md`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-00-reality-audit-provenance/REVIEW.md`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-00-reality-audit-provenance/HANDOFF.md`

## Next Context

Ticket 01 should start from the canonical package ticket, validate the source lock, and use the ticket 00 traceability and contracts as planning inputs. Do not rely on the repository ticket copy as the source of authority.

## Ticket 00 Review And Repair

- First independent review: FAIL. Findings were non-exact repository ticket copy and insufficient traceability fields.
- Repair round 1: restored the repository ticket copy to byte-for-byte canonical content and expanded requirement traceability.
- Second independent review: PASS. No remaining fail findings.

## Ticket 01 Context

- Active ticket: `TKT-2026-06-22-aew-v05-01-native-subagents-expert-routing`.
- Canonical ticket file: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-01-native-subagents-expert-routing.yaml`.
- Delivery starts from `main` at `802f1cad291ab2e1fe8e92f1322d53a3fe7b56a2`, matching `origin/main`.
- Official Codex documentation confirms project-scoped custom agents under `.codex/agents/*.toml`, required fields `name`, `description`, `developer_instructions`, and `[agents] max_depth = 1` as the safe default.

## Ticket 02 Context

- Active ticket: `TKT-2026-06-22-aew-v05-02-sdd-spec-artifacts`.
- Canonical ticket file: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-02-sdd-spec-artifacts.yaml`.
- Delivery starts from `main` at `a62d29c02f703fd8ce36c34d97ff74c17c508e1a`, matching `origin/main`.
- v0.4 `spec-artifact-package` maps to this ticket. The feature branch templates were used only as read-only evidence and adapted to v0.5 ticket/source-lock rules.
