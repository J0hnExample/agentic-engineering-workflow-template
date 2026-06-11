# SDD Upgrade Ticket Index

Created: 2026-06-09  
Target version: 0.4.0

These tickets turn the existing Codex-first workflow template into a Spec-driven Development capable workflow while preserving the current safety model.

## Tickets

1. `TKT-2026-06-09-sdd-upgrade-orchestrator.yaml` — parent ticket for the whole SDD upgrade.
2. `TKT-2026-06-09-expert-routing-profiles.yaml` — specialize the existing read-only expert-team workflow with routing profiles.
3. `TKT-2026-06-09-spec-artifact-package.yaml` — add requirements/design/tasks spec artifacts.
4. `TKT-2026-06-09-delta-spec-lifecycle.yaml` — add Spec-anchored delta-spec lifecycle.
5. `TKT-2026-06-09-spec-drift-verifier.yaml` — add cross-artifact spec drift verification.
6. `TKT-2026-06-09-conditional-steering.yaml` — add conditional context/steering files.
7. `TKT-2026-06-09-quick-flow-escalation.yaml` — add small-task quick-flow with escalation rules.
8. `TKT-2026-06-09-decision-lock-context-budget.yaml` — add grey-area decision locks and context-budget controls.
9. `TKT-2026-06-09-readme-terminology-version-0-4-0.yaml` — update README, VERSION, and changelog to 0.4.0 after the SDD changes land.

## Manager note

Run the README/version ticket last. Until the implementation tickets are complete, `VERSION` should remain `0.3.0` in the source tree; the ticket defines the intended bump to `0.4.0`.
