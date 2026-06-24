# Workflow v0.5 Requirement Traceability

Release: `0.5.0` on 2026-06-24.

This matrix preserves the supplied v0.4 release intent as upgraded into the v0.5.0 release. It does not claim that `0.4.0` shipped from `main`.

## v0.4 Requirement Map

| Source requirement | Release destination | Implemented files | Tests and proof | Review / delivery | Status |
| --- | --- | --- | --- | --- | --- |
| Expert routing profiles | Ticket 01 `native-subagents-expert-routing` | `.codex/config.toml`, `.codex/agents/*.toml`, role prompts, README/workflow docs | TOML parsing, routing/read-only checks, workflow validator coverage | Review PASS; delivered in `a62d29c02f703fd8ce36c34d97ff74c17c508e1a` | Released in 0.5.0 |
| SDD artifact package | Ticket 02 `sdd-spec-artifacts` | `templates/specs/**`, spec-aware ticket templates, workflow docs, checklists | YAML/template parse, required spec identifiers, rendered example package | Review PASS after repair; delivered in `1662fc1705e4f5026bb45ceffa87368e6c16d12d` | Released in 0.5.0 |
| Delta spec lifecycle | Ticket 03 `delta-spec-drift-verification` | `templates/specs/**`, `docs/spec_lifecycle.md`, verifier prompts/checklists | Lifecycle examples and drift fixtures | Review PASS; delivered in `40bd1d5ddadbfef973553fa03faa1e3662a4833d` | Released in 0.5.0 |
| Spec drift verifier | Ticket 03 `delta-spec-drift-verification` | `prompts/spec-drift-verifier.md`, `checklists/spec-drift.md`, `prompts/final-verifier.md`, execution-result template | Positive/negative drift fixtures and final-verifier consumption | Review PASS; delivered in `40bd1d5ddadbfef973553fa03faa1e3662a4833d` | Released in 0.5.0 |
| Conditional steering | Ticket 04 `steering-decisions-context-budget` | `templates/steering/**`, `templates/AGENTS.md.template`, prompts, checklists, docs | Steering match/no-match/conflict fixtures and context-pack checks | Review PASS after repair; delivered in `c462e7e8fc501d7bf421524b4f28809efcedfd51` | Released in 0.5.0 |
| Decision lock and context budget | Ticket 04 `steering-decisions-context-budget` | Ticket/orchestrator templates, `agent/DECISIONS.md`, prompts, context docs | Decision-lock transition and unresolved-decision rejection fixtures | Review PASS after repair; delivered in `c462e7e8fc501d7bf421524b4f28809efcedfd51` | Released in 0.5.0 |
| Quick-flow escalation | Ticket 05 `quick-flow-single-ticket` | `prompts/quick-dev.md`, `prompts/run-single-ticket-autonomously.md`, quick-ticket and execution templates, docs | Quick/escalate classification and single-ticket state-machine checks | Review PASS; delivered in `32a305a867ace26abed0d8fe97e80f7f05f61afd` | Released in 0.5.0 |
| README terminology and release metadata | Tickets 11 and 12 | `README.md`, `docs/**`, prompts/templates, `VERSION`, `CHANGELOG.md`, `agent/CHANGELOG.md` | Stale-version search, workflow validator docs checks, release consistency proof | Ticket 11 review PASS delivered in `b494fa4d5f148cf59fa37a0684593770cbddfa0c`; Ticket 12 release audit recorded in its review | Released in 0.5.0 |
| v0.4 SDD orchestrator parent | Ticket 00 provenance only | `GLOBAL_PLAN.md`, `CONTEXT_LEDGER.md`, this traceability file, package provenance records | Package/source-lock baseline evidence and child-row coverage | Review PASS after repair; delivered in `802f1cad291ab2e1fe8e92f1322d53a3fe7b56a2` | Provenance preserved; not an executable v0.5 controller |

## v0.5 Autonomy And Git Requirements

| Source requirement | Release destination | Implemented files | Tests and proof | Review / delivery | Status |
| --- | --- | --- | --- | --- | --- |
| Generic autonomous package builder | Ticket 06 | `prompts/create-autonomous-ticket-package.md`, `prompts/generic-autonomous-software-request.md`, `templates/autonomous-package/**`, `tools/build_autonomous_package.py`, `tools/validate_autonomous_package.py`, tests, docs | Builder/validator unit tests, mutation and substituted-path failures, generated fixture packages | Review PASS after repair; delivered in `53f85a098db98c8d5c8b2429305136d1e88348b3` | Released in 0.5.0 |
| Serial controller and safe resume | Ticket 07 | `prompts/autonomous-orchestrator.md`, `docs/autonomous_execution.md`, runtime templates, `tools/validate_run_state.py`, tests | Full-chain/single-ticket state fixtures, writer lock, interrupted resume, source-lock failure markers | Review PASS after bounded repairs; delivered in `6e407947ea92c001debc439a18aaab9859a8e9aa` | Released in 0.5.0 |
| Review, repair, blocker handling, context curation | Ticket 08 | `prompts/independent-reviewer.md`, blocker/context prompts, templates, checklists, docs, fixtures | PASS/FAIL/repair-cap tests, blocker decision matrix, context capsule checks | Review PASS; delivered in `248b2a2376dfc07ac90fdddf5f6f32d2932e8f7c` | Released in 0.5.0 |
| Git delivery clean worktree | Ticket 09 | `docs/git_delivery.md`, `prompts/git-delivery-agent.md`, `templates/TEMPLATE.workflow-policy.yaml`, `templates/TEMPLATE.git-delivery-result.yaml`, `tools/workflow_git.py`, tests | Temp Git/bare-origin fixtures, explicit staging, dirty baseline, divergence and upstream equality tests | Review PASS after repair; delivered in `da88539c8757e71bfe6a004dce3f67ff998ee2f2` | Released in 0.5.0 |
| Trusted hooks, validators, self-tests | Ticket 10 | `.codex/hooks.json`, `tools/codex_hooks/**`, `tools/validate_workflow.py`, tests, docs | Hook contract tests, continuation circuit breaker tests, aggregate validator, adversarial fixtures | Review PASS; delivered in `151c6eaac952a9e36348c4e55c06ab68205fb658` | Released in 0.5.0 |
| Documentation and installation modernization | Ticket 11 | `README.md`, `docs/workflow.md`, install/package docs, prompts/templates, validator docs checks | Workflow validator, focused validator tests, stale public language checks | Review PASS; delivered in `b494fa4d5f148cf59fa37a0684593770cbddfa0c` | Released in 0.5.0 |
| Release metadata and final proof | Ticket 12 | `VERSION`, `README.md`, `CHANGELOG.md`, release records, traceability, agent ledger | Workflow validators, active source lock evidence, run-state fixture validator, full unittest discovery, parse checks, version search, diff check, no-cache check | PASS | Delivered in release commit `f42f359212b4ba3a364c684fddab019cfcf7cd85` with final proof follow-up commits |

## Canonical Ticket Release Table

| Order | Ticket | Title | Review | Delivery SHA / exception |
| --- | --- | --- | --- | --- |
| 00 | `TKT-2026-06-22-aew-v05-00-reality-audit-provenance` | Reality audit and provenance | PASS after repair | `802f1cad291ab2e1fe8e92f1322d53a3fe7b56a2` |
| 01 | `TKT-2026-06-22-aew-v05-01-native-subagents-expert-routing` | Native subagents and expert routing | PASS | `a62d29c02f703fd8ce36c34d97ff74c17c508e1a` |
| 02 | `TKT-2026-06-22-aew-v05-02-sdd-spec-artifacts` | SDD spec artifacts | PASS after repair | `1662fc1705e4f5026bb45ceffa87368e6c16d12d` |
| 03 | `TKT-2026-06-22-aew-v05-03-delta-spec-drift-verification` | Delta spec lifecycle and drift verification | PASS | `40bd1d5ddadbfef973553fa03faa1e3662a4833d` |
| 04 | `TKT-2026-06-22-aew-v05-04-steering-decisions-context-budget` | Steering, decisions, context budget | PASS after repair | `c462e7e8fc501d7bf421524b4f28809efcedfd51` |
| 05 | `TKT-2026-06-22-aew-v05-05-quick-flow-single-ticket` | Quick flow and single-ticket runner | PASS | `32a305a867ace26abed0d8fe97e80f7f05f61afd` |
| 06 | `TKT-2026-06-22-aew-v05-06-generic-autonomous-package-builder` | Generic autonomous package builder | PASS after repair | `53f85a098db98c8d5c8b2429305136d1e88348b3` |
| 07 | `TKT-2026-06-22-aew-v05-07-serial-controller-resume` | Serial controller and resume | PASS after bounded repairs | `6e407947ea92c001debc439a18aaab9859a8e9aa` |
| 08 | `TKT-2026-06-22-aew-v05-08-review-repair-blocker-context` | Review, repair, blocker, context | PASS | `248b2a2376dfc07ac90fdddf5f6f32d2932e8f7c` |
| 09 | `TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree` | Git delivery clean worktree | PASS after repair | `da88539c8757e71bfe6a004dce3f67ff998ee2f2` |
| 10 | `TKT-2026-06-22-aew-v05-10-hooks-validators-selftests` | Hooks, validators, self-tests | PASS | `151c6eaac952a9e36348c4e55c06ab68205fb658` |
| 11 | `TKT-2026-06-22-aew-v05-11-docs-installation-modernization` | Docs and installation modernization | PASS | `b494fa4d5f148cf59fa37a0684593770cbddfa0c` |
| 12 | `TKT-2026-06-22-aew-v05-12-release-0-5-0` | Release 0.5.0 | PASS | Release commit `f42f359212b4ba3a364c684fddab019cfcf7cd85`; final proof follow-up commits pushed to `origin/main` |

## Release Boundary

`VERSION`, README release status, and the root changelog now agree on `0.5.0`. The canonical package root remains immutable; its strict validator currently rejects the original package with `dependency graph order does not match ticket order`, which is recorded as a validator/package-shape limitation rather than repaired in package contents.
