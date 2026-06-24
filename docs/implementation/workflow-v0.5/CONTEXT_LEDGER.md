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

## Ticket 03 Context

- Active ticket: `TKT-2026-06-22-aew-v05-03-delta-spec-drift-verification`.
- Canonical ticket file: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-03-delta-spec-drift-verification.yaml`.
- Delivery starts from `main` at `1662fc1705e4f5026bb45ceffa87368e6c16d12d`, matching `origin/main`.
- v0.4 `delta-spec-lifecycle` and `spec-drift-verifier` map to this ticket. The feature branch docs were used only as read-only evidence and adapted to v0.5 SDD artifacts.

## Ticket 04 Context

- Active ticket: `TKT-2026-06-22-aew-v05-04-steering-decisions-context-budget`.
- Canonical ticket file: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-04-steering-decisions-context-budget.yaml`.
- Delivery starts from `main` at `40bd1d5ddadbfef973553fa03faa1e3662a4833d`, matching `origin/main`.
- v0.4 `conditional-steering` and `decision-lock-context-budget` map to this ticket. Feature branch steering docs were used only as read-only evidence.

## Ticket 05 Context

- Active ticket: `TKT-2026-06-22-aew-v05-05-quick-flow-single-ticket`.
- Canonical ticket file: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-05-quick-flow-single-ticket.yaml`.
- Repository ticket copy: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-05-quick-flow-single-ticket.yaml`.
- Delivery starts from `main` at `c462e7e8fc501d7bf421524b4f28809efcedfd51`.
- v0.4 `quick-dev.md` and `TEMPLATE.quick-ticket.yaml` were used only as read-only evidence and adapted to v0.5 source-lock, review, context curation, and delivery-proof requirements.
- Quick-flow must remain ticketed work and escalates on security/auth/privacy, schema/data, dependencies, multiple modules/services, public contracts, visual ambiguity, unclear requirements, forbidden paths, or broad file scope.
- Single-ticket autonomous execution uses the planner -> writer -> reviewer -> repair -> curator -> delivery state machine and blocks `done` until `head_equals_origin_main_proved`.

## Ticket 06 Context

- Active ticket: `TKT-2026-06-22-aew-v05-06-generic-autonomous-package-builder`.
- Canonical ticket file: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-06-generic-autonomous-package-builder.yaml`.
- Repository ticket copy: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-06-generic-autonomous-package-builder.yaml`.
- Delivery starts from `main` at `32a305a867ace26abed0d8fe97e80f7f05f61afd`, matching `origin/main`.
- Generic autonomous package generation lives in `tools/build_autonomous_package.py`, `tools/validate_autonomous_package.py`, `templates/autonomous-package/`, and `docs/autonomous_ticket_packages.md`.
- Generated package fixtures must remain generic and avoid project-specific product language from this upgrade package.

## Ticket 07 Context

- Active ticket: `TKT-2026-06-22-aew-v05-07-serial-controller-resume`.
- Canonical ticket file: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-07-serial-controller-resume.yaml`.
- Repository ticket copy: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-07-serial-controller-resume.yaml`.
- Delivery starts from `main` at `53f85a098db98c8d5c8b2429305136d1e88348b3`, matching `origin/main`.
- Deterministic autonomous run-state validation lives in `tools/validate_run_state.py` with fixtures under `tests/fixtures/run_state/`.
- The canonical controller phase list is documented in `docs/autonomous_execution.md`, `prompts/autonomous-orchestrator.md`, and `templates/runtime/RUN_STATE.schema.json`.
- Live controller state belongs outside the worktree, for example `.git/agentic-workflow-controller/RUN_STATE.json`; repository records remain compact ticket plans, reports, reviews, handoffs, and delivery proof.

## Ticket 08 Context

- Active ticket: `TKT-2026-06-22-aew-v05-08-review-repair-blocker-context`.
- Canonical ticket file: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-08-review-repair-blocker-context.yaml`.
- Repository ticket copy: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-08-review-repair-blocker-context.yaml`.
- Implementation starts from `main` at `6e407947ea92c001debc439a18aaab9859a8e9aa`.
- Review/repair contracts live in `prompts/independent-reviewer.md`,
  `templates/TEMPLATE.ticket-review.md`, and
  `checklists/review-repair-context.md`.
- Blocker-resolution contracts live in `prompts/blocker-resolver.md`,
  `templates/TEMPLATE.blocker-capsule.md`, and
  `templates/TEMPLATE.blocker-decision.md`.
- Context-curation contracts live in `prompts/context-curator.md` and
  `templates/TEMPLATE.context-ledger.md`.
- Independent review returned `PASS` by subagent
  `019ef371-c355-71e3-81e2-5a61c08adc92`; repair rounds used: `0`.
- Proof rerun by the reviewer passed: canonical/repository ticket `cmp`,
  focused `tests.test_review_repair_context` with 8 tests, full unittest
  discovery with 31 tests, scoped `git diff --check`, and no `__pycache__`
  output.
- Context was curated after PASS. Next legal phase is
  `git_delivery_started`; Git delivery remains not started until the delivery
  agent runs.
- Residual non-blocking risk: the pre-existing untracked ZIP remains excluded
  from delivery unless separately approved.

## Ticket 09 Context

- Active ticket: `TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree`.
- Canonical ticket file: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree.yaml`.
- Repository ticket copy: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree.yaml`.
- Implementation starts from `main` at `248b2a2376dfc07ac90fdddf5f6f32d2932e8f7c`, matching `origin/main`.
- Git delivery policy lives in `docs/git_delivery.md`,
  `templates/TEMPLATE.workflow-policy.yaml`,
  `templates/TEMPLATE.git-delivery-result.yaml`, and
  `prompts/git-delivery-agent.md`.
- Dependency-free Git delivery helper lives in `tools/workflow_git.py` with
  focused tests in `tests/test_workflow_git.py`.
- Independent review passed after one bounded repair round that removed only a
  generated `tools/__pycache__` artifact; proof was rerun with
  `PYTHONDONTWRITEBYTECODE=1`.
- README feature review confirmed no additional README edit was needed because
  deterministic Git delivery, recorded policy, helper, explicit staging,
  commit/push/upstream proof, and baseline-relative dirty handling are already
  named.
- The pre-existing untracked ZIP
  `tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip`
  remains excluded from Ticket 09 delivery.

## Ticket 10 Context

- Active ticket: `TKT-2026-06-22-aew-v05-10-hooks-validators-selftests`.
- Canonical ticket file: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-10-hooks-validators-selftests.yaml`.
- Repository ticket copy: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-10-hooks-validators-selftests.yaml`.
- Implementation starts from `main` at `da88539c8757e71bfe6a004dce3f67ff998ee2f2`, matching `origin/main`.
- Hook configuration lives in `.codex/hooks.json` using the official top-level
  `hooks` object with `SessionStart`, `SubagentStart`, and `Stop` command hooks.
- Hook helpers live in `tools/codex_hooks/`; aggregate validation lives in
  `tools/validate_workflow.py`.
- Hook changes require normal Codex trust review. The workflow does not
  recommend bypassing hook trust for normal operation.
- Stop continuation requires valid source lock, nonterminal state, an incomplete
  next phase, remaining continuation budget, and a changed progress token.
- Independent review passed by subagent
  `019efa44-64a6-7273-b92e-20f8eeeb6d6b`; repair rounds after review: `0`.
- Proof passed: workflow validator, package-root source hash validation,
  focused hook/validator tests with 12 tests, full discovery with 51 tests,
  scoped diff check, and no `__pycache__` output.
- The pre-existing untracked ZIP remains excluded from Ticket 10 delivery.

## Ticket 10 Context

- Active ticket: `TKT-2026-06-22-aew-v05-10-hooks-validators-selftests`.
- Canonical ticket file: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-10-hooks-validators-selftests.yaml`.
- Repository ticket copy: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-10-hooks-validators-selftests.yaml`.
- Implementation starts from `main` at `da88539c8757e71bfe6a004dce3f67ff998ee2f2`, matching `origin/main`.
- Trusted hook configuration lives in `.codex/hooks.json` and uses `SessionStart`, `SubagentStart`, and `Stop` command hooks backed by `tools/codex_hooks/`.
- Hook changes require the normal Codex project trust review. The workflow must not recommend hook-trust bypass for normal operation.
- `tools/validate_workflow.py` is a dependency-free aggregate validator for hook JSON, TOML, known YAML fields, references, AGENTS size, ticket fields, optional source hashes, run-state transitions, version consistency, stdlib imports, and adversarial fixture inventory.
- Stop continuation is allowed only with valid source lock, nonterminal state, an incomplete next phase, changed progress token, and remaining continuation budget.
- The pre-existing untracked ZIP remains excluded from Ticket 10 implementation and delivery.

## Ticket 11 Context

- Active ticket: `TKT-2026-06-22-aew-v05-11-docs-installation-modernization`.
- Canonical ticket file: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-11-docs-installation-modernization.yaml`.
- Repository ticket copy: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-11-docs-installation-modernization.yaml`.
- Public docs now use model-neutral Codex wording and avoid stale current-version claims for `0.3.0` or `0.4.0`.
- README and `docs/workflow.md` document full SDD, quick flow, single-ticket autonomous, and source-locked package autonomous modes.
- `prompts/initialize-repo.md` requires target-repository evidence first, source-to-target install mapping, and one recorded delivery/side-effect policy from `templates/TEMPLATE.workflow-policy.yaml`.
- `docs/autonomous_ticket_packages.md` clarifies package-local source of truth, repository-ticket substitution rejection, active-ticket validation before role spawns, and generated package/ZIP output not staged by default.
- `tools/validate_workflow.py` now checks stale public language, public references, install mapping, documentation consistency, and a 2500-word `templates/AGENTS.md.template` ceiling. Its pass output includes documentation consistency and fixture install dry-run summaries.
- Independent review passed by reviewer
  `019efa53-3dbc-7963-8d07-19323217a370`; the only follow-up was a hygiene
  repair changing `REVIEW.md` from `pass_with_risk` to `PASS` after the review
  had already confirmed no blocking residual risk.
- Proof passed after the hygiene repair: `PYTHONDONTWRITEBYTECODE=1 python tools/validate_workflow.py`, focused validator tests with 9 tests, full unittest discovery with 54 tests, and no `__pycache__` output.
- Ticket 12 still owns `VERSION`, release changelog headings, and any `0.5.0` current-release claim.
- Git delivery was intentionally not run for Ticket 11 in this implementation turn because the user prohibited staging, committing, pushing, branches, stashes, and worktrees.

## Ticket 12 Context

- Active ticket: `TKT-2026-06-22-aew-v05-12-release-0-5-0`.
- Canonical ticket file: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-12-release-0-5-0.yaml`.
- Repository ticket copy: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-12-release-0-5-0.yaml`.
- Implementation starts from `main` at `b494fa4d5f148cf59fa37a0684593770cbddfa0c`, matching `origin/main`.
- Release metadata now targets `0.5.0` in `VERSION`, README public release status, and root `CHANGELOG.md`.
- `docs/implementation/workflow-v0.5/REQUIREMENT_TRACEABILITY.md` is the release matrix for imported v0.4 requirements, v0.5 autonomy/Git requirements, and canonical tickets 00-12.
- The package root remained immutable. Package validation with the package-local active ticket file currently fails with `dependency graph order does not match ticket order`; this is recorded as a package/validator-shape limitation, not repaired by mutating package contents.
- Ticket 12 delivery commit is `f42f359212b4ba3a364c684fddab019cfcf7cd85` on `main`.
- After fetch, local `HEAD` matched `origin/main` at `f42f359212b4ba3a364c684fddab019cfcf7cd85`.
- The pre-existing untracked ZIP `tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip` remains untouched and excluded.
