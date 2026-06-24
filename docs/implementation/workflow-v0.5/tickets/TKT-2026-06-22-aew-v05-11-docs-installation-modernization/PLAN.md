# Ticket 11 Plan

## Source And Baseline

- Ticket: `TKT-2026-06-22-aew-v05-11-docs-installation-modernization`
- Canonical source: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-11-docs-installation-modernization.yaml`
- Repository ticket copy: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-11-docs-installation-modernization.yaml`
- Source-lock validation: `ACTIVE TICKET LOCK PASSED`.
- Repository ticket copy proof: `cmp` passed against the canonical package ticket.
- Start branch: `main`
- Start commit: `151c6eaac952a9e36348c4e55c06ab68205fb658`, matching `origin/main`.
- Pre-existing untracked artifact excluded from delivery: `tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip`

## Accepted Plan

Modernize public installation and workflow documentation so new users can choose
and run full SDD, quick-flow, single-ticket autonomous, or source-locked package
autonomous modes with model-neutral Codex wording and concise always-on
`AGENTS.md` guidance.

## Planned Files

Core files:

- `README.md`
- `docs/workflow.md`
- `docs/autonomous_execution.md`
- `docs/git_delivery.md`
- `docs/autonomous_ticket_packages.md`
- `prompts/initialize-repo.md`
- `prompts/manager-orchestrator.md`
- `prompts/scoped-worker.md`
- `prompts/final-verifier.md`
- `templates/AGENTS.md.template`
- `tools/validate_workflow.py`
- `tests/test_validate_workflow.py`
- `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md`
- `agent/DECISIONS.md`
- `agent/PATHS.md`
- `agent/CHANGELOG.md`

Optional consistency-only files inside ticket scope may be updated when needed:
`prompts/run-single-ticket-autonomously.md`,
`prompts/create-autonomous-ticket-package.md`,
`prompts/generic-autonomous-software-request.md`, package templates, runtime
templates, spec templates, and checklists.

Ticket records will be created under
`docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-11-docs-installation-modernization/`.

## Documentation Changes

README:

- replace hardcoded `Codex 5.5` claims with model-neutral `Codex`;
- remove public current-release prose that claims `0.3.0` or `0.4.0` as current;
- do not claim `0.5.0` current before Ticket 12;
- keep historical version mentions only in historical changelog or
  implementation records;
- add a mode decision table covering full SDD, quick-flow, single-ticket
  autonomous run, and source-locked package autonomous run;
- add a generic copy-paste initialization prompt;
- add one-line package build/validate invocation;
- make source repository vs target repository mapping explicit.

Workflow docs:

- make `docs/workflow.md` the canonical workflow-mode reference;
- document expected artifacts: tickets, plans, execution reports, reviews,
  handoffs, context ledger, Git delivery records, and agent memory updates;
- define full SDD vs quick/no-spec conditions;
- keep role naming model-neutral.

Autonomous/Git/package docs:

- clarify source lock, hook trust, writer lock, resume behavior, blocker
  resolver limits, completed-prefix semantics, and clean-relative-to-baseline
  delivery behavior;
- keep blocker resolver read-only unless it authorizes a smallest safe action
  for another role;
- document package source vs target repository installation, active-ticket
  source-lock validation, and repository-ticket substitution rejection.

Installation prompts/templates:

- inspect target repo evidence first;
- produce source-to-target copy plans;
- include native profile/template installation mapping;
- ask once for delivery/side-effect policy and record it from
  `templates/TEMPLATE.workflow-policy.yaml`;
- keep dependency installs and external side effects approval-gated.

`templates/AGENTS.md.template`:

- keep durable safety, read order, ticket scope, approval boundaries, proof, and
  delivery rules;
- link to focused docs instead of embedding long mode/state-machine prose;
- preserve the rule that the file is active only after being installed as
  `AGENTS.md`.

## Validator And Tests

Extend `tools/validate_workflow.py` and `tests/test_validate_workflow.py` to
cover:

- link/path checks over README, docs, prompts, templates, checklists, and agent
  references;
- stale language search for `Codex 5.5` and public current-version claims of
  `0.3.0` or `0.4.0`;
- historical allowlist for changelog and implementation/history records;
- stricter AGENTS template size ceiling;
- fixture repository install dry-run:
  - `templates/AGENTS.md.template` maps to target `AGENTS.md`;
  - `agent/*.md` maps to target `agent/*.md`;
  - ticket templates map to `tickets/templates/*`;
  - docs map to target docs paths;
  - workflow policy target is selected or recorded;
  - generated ZIP/package output is not staged by default;
- documentation consistency report: mode names, source/target terminology,
  package source-lock docs, delivery policy docs, and clean-relative-to-baseline
  docs.

## Required Proof

- canonical ticket `cmp`;
- `PYTHONDONTWRITEBYTECODE=1 python tools/validate_workflow.py`;
- `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_validate_workflow`;
- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -p 'test*.py'`;
- stale-language search summary;
- AGENTS word/byte measurement;
- link/path checker output;
- fixture install dry-run evidence;
- `git diff --check` on ticket scope;
- no generated `__pycache__` output.

## Review Focus

The independent reviewer must verify that README mode selection is usable
without ticket internals, wording is model-neutral, public current docs do not
claim `0.3.0` or `0.4.0` as current, source/target mapping and links resolve,
delivery/side-effect policy is recorded once, `AGENTS.md.template` remains
concise, blocker resolver limits/hook trust/source lock/resume behavior remain
strict, and the pre-existing ZIP remains excluded from Git delivery.

## Context Curation And Delivery

After review `PASS`, curate compact Ticket 11 facts into the ticket records,
context ledger, and agent notes. Handoff to Ticket 12 must remind that release
metadata and the `0.5.0` version bump are still owned by Ticket 12.

Delivery must use explicit staging only on `main`, exclude the pre-existing ZIP,
commit with prefix `TKT-2026-06-22-aew-v05-11-docs-installation-modernization`,
push to `origin/main`, and prove local `HEAD == origin/main`.
