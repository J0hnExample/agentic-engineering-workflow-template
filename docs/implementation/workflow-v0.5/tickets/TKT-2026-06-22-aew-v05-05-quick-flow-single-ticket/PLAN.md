# Ticket 05 Plan

## Source And Baseline

- Ticket: `TKT-2026-06-22-aew-v05-05-quick-flow-single-ticket`
- Canonical source: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-05-quick-flow-single-ticket.yaml`
- Repository ticket copy: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-05-quick-flow-single-ticket.yaml`
- Source-lock validation: passed before planning.
- Repository ticket copy proof: `cmp` passed against the canonical package ticket.
- Start branch: `main`
- Start commit: `c462e7e8fc501d7bf421524b4f28809efcedfd51`, matching `origin/main`.
- Pre-existing untracked artifact excluded from delivery: `tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip`

## Accepted Plan

Implement a lightweight quick-flow path and a one-ticket autonomous runner without weakening the serial v0.5 workflow. Quick-flow remains ticketed work: it must perform repository discovery, classify risk, keep a repository ticket record, produce an execution result, run focused proof, self-review, independent review, context curation, explicit Git delivery, push, and prove `HEAD == origin/main`.

## Implementation Scope

Allowed implementation paths are limited to the canonical ticket scope:

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

Forbidden paths remain `.env`, `.env.*`, `**/secrets/**`, `node_modules/**`, `dist/**`, `build/**`, `coverage/**`, and `.git/**`.

## Required Design

Quick-flow classification must be deterministic and conservative:

- Quick only when there is one bounded objective, exact affected files are known, no more than three non-ticket files need edits, at most one bounded module/service/package changes, local meaningful proof exists, and no full SDD, expert review, public contract, migration, dependency, security/auth/privacy, ambiguous UI, or broad-scope trigger applies.
- Escalate on any security/auth/privacy, schema/data, dependency, multi-service/module, public API/shared-contract, visual-flow ambiguity, unclear-requirement, forbidden-path, or broad-file-scope trigger.
- Fixture evidence must include a tiny low-risk case that remains quick and risky cases that escalate deterministically.

The single-ticket runner must use the same state machine as the package chain:

`source_lock_validated -> repository_discovered -> plan_recorded -> repository_ticket_recorded -> writer_assigned -> implementation_complete -> focused_tests_passed -> self_review_complete -> independent_review_complete -> repair_loop_complete_or_not_needed -> context_curated -> git_delivery_started -> explicit_paths_staged -> committed -> pushed -> head_equals_origin_main_proved -> done`

Hard gates:

- Do not assign a writer before the plan exists and the repository ticket copy matches the package ticket.
- Use exactly one implementation writer.
- Independent review must inspect the actual diff.
- Repair loop cap is three rounds.
- Context curator writes compact handoff facts.
- Git delivery uses explicit path staging only.
- Done is impossible before commit/push equality proof.
- Successful delivery leaves no prior-ticket workflow artifacts dirty; the package ZIP remains unstaged.

## Planned Edits

- Add `prompts/quick-dev.md`.
- Add `prompts/run-single-ticket-autonomously.md`.
- Add `templates/TEMPLATE.quick-ticket.yaml`.
- Update `templates/TEMPLATE.ticket.yaml` and `templates/TEMPLATE.execution-result.yaml` so quick-flow and single-ticket closeout can record classification, run state, delivery proof, and agent-memory checks. Also remove the duplicated `execution_result` mapping currently present in `TEMPLATE.execution-result.yaml`.
- Update `docs/workflow.md`, `templates/AGENTS.md.template`, `checklists/ticket-readiness.md`, `checklists/closeout.md`, and `README.md` with quick-flow and single-ticket rules.
- Update `agent/PATHS.md` and `agent/CHANGELOG.md` for durable workflow additions.
- Update `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md` with ticket 05 context.
- Create `EXECUTION_REPORT.md`, `REVIEW.md`, `HANDOFF.md`, and `GIT_DELIVERY.md` in the ticket record directory.

## Required Proof

- Active ticket source-lock validation.
- `cmp` between canonical package ticket and repository ticket copy.
- YAML parse for changed YAML templates and ticket copy.
- Quick/escalate fixture script covering low-risk, security/auth, schema/data, dependency, multi-module, public-contract, visual, unclear, and broad-scope cases.
- Single-ticket state transition script proving `done` is blocked until `head_equals_origin_main_proved`.
- Scope and whitespace proof with `git diff --check`.
- Independent reviewer verdict recorded in `REVIEW.md`.
- Delivery proof after commit and push: `HEAD == origin/main`.

## Review Focus

The independent reviewer must verify that quick-flow is not a bypass, classification thresholds are objective, risky fixtures escalate, the one-ticket runner uses the same workflow state machine, explicit staging excludes unrelated files and the package ZIP, and no version bump or release claim is introduced before ticket 12.
