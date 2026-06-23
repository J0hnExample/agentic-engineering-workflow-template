# PATHS

Important repo paths, commands, routes, artifact locations, and generated output
locations. Prefer repo-relative paths and named external locations. Avoid
private absolute paths unless the user explicitly approves a narrow local-only
note.

## Source Areas

- `<area>`: `<path>`
- Native Codex profile config: `.codex/config.toml`
- Project-scoped Codex custom agents: `.codex/agents/*.toml`
- Workflow v0.5 implementation records: `docs/implementation/workflow-v0.5/`
- SDD spec templates and examples: `templates/specs/`
- Spec lifecycle docs: `docs/spec_lifecycle.md`
- Spec drift verifier prompt/checklist: `prompts/spec-drift-verifier.md`, `checklists/spec-drift.md`
- Steering templates: `templates/steering/`
- Quick-flow prompt and template: `prompts/quick-dev.md`, `templates/TEMPLATE.quick-ticket.yaml`
- Single-ticket autonomous runner prompt: `prompts/run-single-ticket-autonomously.md`
- Autonomous package prompts: `prompts/create-autonomous-ticket-package.md`, `prompts/generic-autonomous-software-request.md`
- Autonomous package skeleton: `templates/autonomous-package/`
- Autonomous package tools: `tools/build_autonomous_package.py`, `tools/validate_autonomous_package.py`
- Autonomous package docs: `docs/autonomous_ticket_packages.md`
- Autonomous execution controller docs: `docs/autonomous_execution.md`
- Autonomous orchestrator prompt: `prompts/autonomous-orchestrator.md`
- Autonomous run-state validator: `tools/validate_run_state.py`
- Autonomous runtime schema and example: `templates/runtime/RUN_STATE.schema.json`, `templates/runtime/RUN_STATE.example.json`
- Autonomous run templates: `templates/TEMPLATE.autonomous-run.yaml`, `templates/TEMPLATE.ticket-plan.md`, `templates/TEMPLATE.ticket-handoff.md`, `templates/TEMPLATE.next-agent-capsule.md`
- Review/repair prompts: `prompts/independent-reviewer.md`,
  `prompts/blocker-resolver.md`, `prompts/context-curator.md`
- Review/repair templates: `templates/TEMPLATE.ticket-review.md`,
  `templates/TEMPLATE.blocker-capsule.md`,
  `templates/TEMPLATE.blocker-decision.md`,
  `templates/TEMPLATE.context-ledger.md`
- Review/repair checklist: `checklists/review-repair-context.md`

## Tests And Proof

- Lint: `<command>`
- Typecheck: `<command>`
- Unit tests: `<command>`
- Build: `<command>`
- Quick-flow fixture proof: in-memory Python assertion recorded by the active
  ticket.
- Single-ticket state proof: in-memory Python assertion recorded by the active
  ticket.
- Autonomous package proof: `python -m unittest discover -s tests -p 'test*.py'`
  plus explicit build/validate fixtures in `/tmp`.
- Autonomous run-state proof: `python -m unittest tests.test_run_state`
  and direct `python tools/validate_run_state.py tests/fixtures/run_state/<fixture>/RUN_STATE.json`
- Review/repair/context proof: `python -m unittest tests.test_review_repair_context`
- E2E/browser: `<command>`

## Artifacts

- Screenshots: `<path>`
- Test output: `<path>`
- Logs: `<path>`
