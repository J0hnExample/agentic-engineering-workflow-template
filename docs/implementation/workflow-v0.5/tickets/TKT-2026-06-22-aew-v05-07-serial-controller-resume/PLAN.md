# Ticket 07 Plan

## Source And Baseline

- Ticket: `TKT-2026-06-22-aew-v05-07-serial-controller-resume`
- Canonical source: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-07-serial-controller-resume.yaml`
- Repository ticket copy: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-07-serial-controller-resume.yaml`
- Source-lock validation: passed before planning.
- Repository ticket copy proof: `cmp` passed against the canonical package ticket.
- Start branch: `main`
- Start commit: `53f85a098db98c8d5c8b2429305136d1e88348b3`, matching `origin/main`.
- Pre-existing untracked artifact excluded from delivery: `tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip`

## Accepted Plan

Implement a deterministic serial controller state model for full-chain and single-ticket execution. The state machine must reject skipped phases, out-of-order completion, duplicate implementation writers, next-ticket planning before upstream equality, and resume paths that trust ticket names instead of delivery proof.

## Implementation Scope

Allowed implementation paths are limited to the canonical ticket scope:

- `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-07-serial-controller-resume.yaml`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-07-serial-controller-resume/**`
- `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md`
- `agent/**`
- `prompts/autonomous-orchestrator.md`
- `docs/autonomous_execution.md`
- `templates/TEMPLATE.autonomous-run.yaml`
- `templates/TEMPLATE.ticket-plan.md`
- `templates/TEMPLATE.ticket-handoff.md`
- `templates/TEMPLATE.next-agent-capsule.md`
- `templates/runtime/**`
- `tools/validate_run_state.py`
- `tests/**`
- `templates/AGENTS.md.template`

Forbidden paths remain `.env`, `.env.*`, `**/secrets/**`, `node_modules/**`, `dist/**`, `build/**`, `coverage/**`, and `.git/**`.

## State Model

Use one engine for `full_chain` and `single_ticket` modes.

Legal per-ticket phases:

```text
pending
-> source_lock_validated
-> repository_validated
-> plan_recorded
-> repository_ticket_recorded
-> implementation_writer_locked
-> implementation_spawned
-> implementation_completed
-> writer_thread_closed
-> focused_tests_passed
-> self_review_completed
-> independent_review_spawned
-> independent_review_completed
-> repair_completed_or_not_needed
-> context_curated
-> git_delivery_started
-> explicit_paths_staged
-> committed
-> pushed
-> head_equals_upstream_proved
-> completed
```

The validator must reject:

- skipped phases,
- completed phases after missing predecessors,
- completed tickets outside the completed-prefix invariant,
- active next tickets before the previous ticket records commit, push, and upstream equality proof,
- completed tickets without commit SHA and upstream equality proof,
- writer-lock contention,
- independent review or later phases before `writer_thread_closed`,
- resume states that would redo a completed commit instead of verifying the recorded delivery SHA.

## Gating Rules

Before every role spawn, the controller requires package validation and active-ticket source-lock proof. Implementation spawn additionally requires the writer lock. Only one implementation writer may hold the lock. Completed implementation threads must be closed before review and before any later writer.

Live controller state belongs outside the worktree, for example under `.git/agentic-workflow-v05-controller/`. Repository files store templates, validators, compact handoffs, and durable records only.

## Resume Algorithm

On resume:

1. Validate package and active-ticket source lock.
2. Validate branch and upstream configuration.
3. Validate completed-ticket prefix.
4. For the last completed ticket, verify recorded delivery SHA, pushed status, and `HEAD == origin/main` before planning the next ticket.
5. Select the first incomplete ticket and the first missing legal phase.
6. If interrupted at review, resume review or repair decision, not implementation.
7. If interrupted after commit, verify recorded commit and upstream equality instead of recommitting.
8. Stop with a blocker when repository evidence conflicts with state.

## Planned Files

- `tools/validate_run_state.py`: deterministic validator and resume helper CLI.
- `tests/test_run_state.py` and `tests/fixtures/run_state/**`: transition, lock, resume, and source-lock tests.
- `templates/runtime/RUN_STATE.schema.json` and `RUN_STATE.example.json`.
- `templates/TEMPLATE.autonomous-run.yaml`.
- `templates/TEMPLATE.ticket-plan.md`.
- `templates/TEMPLATE.ticket-handoff.md`.
- `templates/TEMPLATE.next-agent-capsule.md`.
- `docs/autonomous_execution.md`.
- `prompts/autonomous-orchestrator.md`.
- `templates/AGENTS.md.template` updates for stricter controller rules.
- Ticket records: `EXECUTION_REPORT.md`, `REVIEW.md`, `HANDOFF.md`, `GIT_DELIVERY.md`.
- Durable memory updates: `agent/PATHS.md`, `agent/CHANGELOG.md`, and context ledger.

## Required Proof

- Active ticket source-lock validation.
- `cmp` between canonical package ticket and repository ticket copy.
- `python -m unittest tests.test_run_state`.
- `python -m unittest discover -s tests -p 'test*.py'`.
- Direct validator commands for valid and invalid run-state fixtures.
- `git diff --check` on scoped paths.
- Independent reviewer PASS before delivery.
- Delivery proof after commit and push: `HEAD == origin/main`.

## Review Focus

The independent reviewer must verify phase skips and out-of-order completion fail, completed-prefix is enforced, source-lock gating is represented before role spawn, writer-lock contention fails, review cannot start before writer thread closure, next-ticket planning is blocked until previous upstream equality proof, post-commit resume verifies delivery SHA instead of recommitting, full-chain and single-ticket modes share the same engine, live state is documented outside the worktree, and the pre-existing ZIP remains unstaged.
