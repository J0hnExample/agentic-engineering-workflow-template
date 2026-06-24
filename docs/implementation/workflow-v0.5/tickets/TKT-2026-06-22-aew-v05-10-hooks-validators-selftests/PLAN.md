# Ticket 10 Plan

## Source And Baseline

- Ticket: `TKT-2026-06-22-aew-v05-10-hooks-validators-selftests`
- Canonical source: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-10-hooks-validators-selftests.yaml`
- Repository ticket copy: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-10-hooks-validators-selftests.yaml`
- Source-lock validation: `ACTIVE TICKET LOCK PASSED`.
- Repository ticket copy proof: `cmp` passed against the canonical package ticket.
- Start branch: `main`
- Start commit: `da88539c8757e71bfe6a004dce3f67ff998ee2f2`, matching `origin/main`.
- Pre-existing untracked artifact excluded from delivery: `tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip`

## Accepted Plan

Add trusted Codex lifecycle hooks, deterministic hook helper scripts, broader
workflow validation, and adversarial self-tests without bypassing hook trust,
weakening source-lock controls, or touching the pre-existing untracked ZIP.

## Planned Files

Create:

- `.codex/hooks.json`
- `tools/codex_hooks/__init__.py`
- `tools/codex_hooks/common.py`
- `tools/codex_hooks/session_start.py`
- `tools/codex_hooks/subagent_start.py`
- `tools/codex_hooks/stop.py`
- `tools/validate_workflow.py`
- `tests/test_codex_hooks.py`
- `tests/test_validate_workflow.py`
- focused fixtures under `tests/fixtures/workflow_validator/` and
  `tests/fixtures/codex_hooks/`
- ticket records under `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-10-hooks-validators-selftests/`

Update:

- `docs/autonomous_execution.md`
- `README.md`
- `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md`
- `agent/DECISIONS.md`
- `agent/PATHS.md`
- `agent/CHANGELOG.md`
- `agent/STATE.md` only if needed for durable current workflow status

## Hook Configuration

Add `.codex/hooks.json` using the official lifecycle hook shape:

- event level, such as `SessionStart`, `SubagentStart`, and `Stop`;
- matcher group;
- one or more command handlers.

Handlers must be dependency-free Python commands:

- `python tools/codex_hooks/session_start.py`
- `python tools/codex_hooks/subagent_start.py`
- `python tools/codex_hooks/stop.py`

Documentation must state that hook changes require normal one-time Codex project
trust review. This workflow must not use or recommend hook-trust bypass for
normal operation. Hooks do not override ticket scope, review, approvals, or
source-lock policy.

## Hook Script Design

Shared `tools/codex_hooks/common.py` will:

- read hook stdin JSON when present and tolerate empty stdin;
- locate the repository root from the working directory;
- find controller state under `.git/agentic-workflow-controller/RUN_STATE.json`
  and, for this v0.5 run, tolerate `.git/agentic-workflow-v05-controller/RUN_STATE.json`
  in tests;
- no-op when no active state exists, state is invalid, complete, blocked, or
  source-lock failed;
- redact secret-looking values and paths matching `secret`, `token`,
  `password`, `credential`, `.env`, or `secrets`;
- emit compact JSON/text bounded by size limits;
- use only the Python standard library.

`session_start.py` emits a compact active-run summary when safe:
package id, mode, active ticket id, active phase, next legal phase,
source-lock status, writer-lock status, last completed ticket, repair count, and
remaining continuation budget.

`subagent_start.py` emits active ticket identity and scope summary for
subagents: ticket id, objective, allowed paths, forbidden paths, current phase,
acceptance gates, and hard-stop reminders. If source lock is not valid, it emits
that fact instead of injecting scope.

`stop.py` allows stop when the run is complete, blocked, waiting on a user
decision, source-lock failed, no budget remains, or no progress was made. It may
continue only when an active nonblocked run has an incomplete next legal phase,
a changed progress token, and remaining continuation budget.

## Circuit Breaker

Use deterministic continuation fields in live controller state or in hook output
fixtures:

- budget total and used count;
- last progress token;
- last continuation token;
- last reason.

The progress token must come from stable nonsecret fields: active ticket id,
active phase, completed phase count or digest, repair round count, writer lock
holder, recorded commit SHA, HEAD SHA when safe, and pushed/upstream proof
booleans. Stop continuation is denied when the token equals the last
continuation token.

## Workflow Validator

Implement `tools/validate_workflow.py` as a stdlib-only aggregate validator with
clear nonzero failures. It should validate:

- JSON files including `.codex/hooks.json`, runtime schema/example JSON, and
  package/template JSON;
- TOML files including `.codex/config.toml` and `.codex/agents/*.toml`;
- known workflow YAML structures with line-oriented checks where no YAML parser
  is available;
- deterministic references from docs, prompts, templates, and tickets;
- AGENTS template size against a conservative context budget;
- v0.5 ticket required fields;
- source hashes for package manifests and active ticket hashes when package
  root arguments are provided;
- run-state transitions by reusing `tools/validate_run_state.py`;
- version consistency for `VERSION`, README current version, and changelog when
  they claim public version values.

## Adversarial Fixtures

Add focused fixtures for:

- wrong ticket id/source-lock mismatch;
- stale state and impossible resume;
- dirty leakage including the preserved ZIP;
- repair-loop bypass beyond `max_repair_rounds`;
- premature stop and no-progress/no-budget/blocked stop behavior;
- hook no-active-run behavior;
- secret redaction of `.env`, token/password/secret-looking fields.

## Required Proof

- `cmp /tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-10-hooks-validators-selftests.yaml tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-10-hooks-validators-selftests.yaml`
- `python -m json.tool .codex/hooks.json`
- `PYTHONDONTWRITEBYTECODE=1 python tools/validate_workflow.py`
- `PYTHONDONTWRITEBYTECODE=1 python tools/validate_run_state.py tests/fixtures/run_state/valid_full_chain/RUN_STATE.json --manifest tests/fixtures/run_state/manifest.json`
- `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_codex_hooks tests.test_validate_workflow`
- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -p 'test*.py'`
- `git diff --check -- . ':!tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip'`
- `find . -type d -name __pycache__ -print`

## Review Focus

The independent reviewer must inspect actual `.codex/hooks.json` shape against
official lifecycle docs, no-op and redaction behavior, Stop continuation circuit
breaker, validator dependency boundaries, adversarial fixture failures,
canonical ticket copy proof, unchanged trust requirements, and preserved ZIP
exclusion.

## Context Curation

After review `PASS`, curate only durable facts: hook locations, validator
command, trust-review requirement, continuation rule, proof results, repair
rounds, residual risks, and next Ticket 11 starting context.

## Delivery

Delivery uses explicit staging only on `main`, excludes the pre-existing ZIP,
commits with prefix `TKT-2026-06-22-aew-v05-10-hooks-validators-selftests`,
pushes to `origin/main`, and proves local `HEAD == origin/main`.
