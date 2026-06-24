# Ticket 12 Plan: Release 0.5.0

Active ticket: `TKT-2026-06-22-aew-v05-12-release-0-5-0`

Canonical ticket:
`/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-12-release-0-5-0.yaml`

Repository ticket copy:
`tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-12-release-0-5-0.yaml`

Start state verified during planning:

- Branch: `main`
- `HEAD`: `b494fa4d5f148cf59fa37a0684593770cbddfa0c`
- `origin/main`: `b494fa4d5f148cf59fa37a0684593770cbddfa0c`
- Current public version before implementation: `VERSION` contains `0.3.0`.
- Pre-existing untracked path to preserve:
  `tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip`
- Ticket 11 handoff says Ticket 12 owns `VERSION`, root changelog release
  heading, and any `0.5.0` current-release claim.

## Scope Lock

Exactly one active ticket is allowed: Ticket 12. Do not start, repair, or
reinterpret any earlier ticket unless Ticket 12 proof discovers a release
blocker and the bounded blocker path below is followed.

Allowed implementation files for Ticket 12:

- `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-12-release-0-5-0.yaml`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-12-release-0-5-0/**`
- `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md`
- `docs/implementation/workflow-v0.5/REQUIREMENT_TRACEABILITY.md`
- `agent/**`
- `VERSION`
- `CHANGELOG.md`
- `agent/CHANGELOG.md`
- `README.md`
- `docs/**`
- `tickets/upgrades/v0.5/**`

Forbidden files and paths:

- `.env`
- `.env.*`
- `**/secrets/**`
- `node_modules/**`
- `dist/**`
- `build/**`
- `coverage/**`
- `.git/**`
- `tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip`
  unless the user explicitly widens release delivery scope, which this plan
  does not require.

Forbidden actions:

- No branch creation.
- No stash.
- No worktree creation.
- No destructive reset or checkout.
- No bulk staging such as `git add .`.
- No release metadata edits before source lock, dependency completion, and
  traceability preflight pass.
- No acceptance weakening to make the release auditor pass.

## Execution Steps

1. Source-lock and dependency preflight

   - Re-run the active source lock using the package-local canonical ticket:
     `python tools/validate_autonomous_package.py /tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade --active-ticket-id TKT-2026-06-22-aew-v05-12-release-0-5-0 --active-ticket-file /tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-12-release-0-5-0.yaml`
   - Verify the repository ticket copy is byte-for-byte canonical:
     `cmp /tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-12-release-0-5-0.yaml tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-12-release-0-5-0.yaml`
   - Verify `git branch --show-current`, `git rev-parse HEAD`, and
     `git rev-parse origin/main` still match the expected `main` baseline.
   - Verify `git status --short --branch --untracked-files=all` shows only
     expected Ticket 12 changes plus the preserved untracked ZIP.

2. Canonical ticket completion audit

   - Build a ticket table for orders 00 through 12 from the canonical package,
     repository ticket copies, `EXECUTION_REPORT.md`, `REVIEW.md`,
     `GIT_DELIVERY.md` where present, `HANDOFF.md`, and current Git history.
   - For tickets 00 through 11, record title, canonical ID, repository ticket
     copy path, review verdict, delivery SHA if available or explicit delivery
     exception, proof commands, and residual risks.
   - Confirm Ticket 11 completed at
     `b494fa4d5f148cf59fa37a0684593770cbddfa0c` and that no earlier ticket
     left a managed artifact dirty.
   - Treat implementation records as evidence, not authority, when they differ
     from canonical tickets.

3. Requirement traceability completion

   - Update `docs/implementation/workflow-v0.5/REQUIREMENT_TRACEABILITY.md`
     so every imported v0.4 child requirement and every v0.5 autonomy/Git
     requirement maps to:
     implementation files, tests, ticket review PASS, delivery commit or
     delivery exception, and release proof.
   - Include all canonical tickets 00 through 12 in the release matrix.
   - Explicitly preserve the v0.4 release intent as upgraded to `0.5.0`, not
     as a claim that `0.4.0` shipped.

4. Release metadata edits

   - Set `VERSION` to exactly `0.5.0`.
   - Update README release-status wording so the current checkout can honestly
     claim release `0.5.0` only after the release proof has passed.
   - Add a root `CHANGELOG.md` entry for `0.5.0 - 2026-06-24` covering:
     SDD artifacts, native Codex subagents, source-locked autonomous packages,
     single-ticket mode, blocker handling, trusted hooks, validators, and Git
     delivery.
   - Update `agent/CHANGELOG.md` with the Ticket 12 release closeout.
   - Do not create tags or GitHub releases unless a later explicit delivery
     instruction adds that scope.

5. Release evidence records

   Create Ticket 12 records under:
   `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-12-release-0-5-0/`

   Required records:

   - `PLAN.md` already accepted before implementation.
   - `EXECUTION_REPORT.md` with final release report, changed files, tests,
     skipped checks, residual risks, and release metadata proof.
   - `REVIEW.md` with independent release-auditor verdict.
   - `HANDOFF.md` with compact durable context.
   - `GIT_DELIVERY.md` with explicit staging list, commit SHA, push result, and
     final local/upstream equality proof.
   - A requirement traceability matrix may live inside `EXECUTION_REPORT.md` or
     as a clearly linked file in the Ticket 12 directory.
   - A complete commit table may live inside `EXECUTION_REPORT.md` or as a
     clearly linked file in the Ticket 12 directory.

6. Validators and tests

   Run every practical check from the repository and package:

   - `PYTHONDONTWRITEBYTECODE=1 python tools/validate_workflow.py`
   - `PYTHONDONTWRITEBYTECODE=1 python tools/validate_workflow.py --package-root /tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade`
   - `PYTHONDONTWRITEBYTECODE=1 python tools/validate_autonomous_package.py /tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade --active-ticket-id TKT-2026-06-22-aew-v05-12-release-0-5-0 --active-ticket-file /tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-12-release-0-5-0.yaml`
   - `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -p 'test*.py'`
   - `python -m json.tool .codex/hooks.json`
   - `python -m json.tool templates/runtime/RUN_STATE.schema.json`
   - `PYTHONDONTWRITEBYTECODE=1 python - <<'PY'` to parse all repository JSON,
     TOML via `tomllib`, and known YAML templates with the repo's simple ticket
     validation conventions.
   - `PYTHONDONTWRITEBYTECODE=1 python tools/validate_run_state.py tests/fixtures/run_state/valid_full_chain/RUN_STATE.json --manifest tests/fixtures/run_state/manifest.json`
   - `rg -n "Codex 5\\.5|Current version:\\s*(0\\.3\\.0|0\\.4\\.0)|(?:0\\.3\\.0|0\\.4\\.0)\\s+is\\s+(?:the\\s+)?(?:current|latest|released)" README.md docs prompts templates checklists agent tickets/upgrades/v0.5`
   - `rg -n "0\\.5\\.0|0\\.4\\.0|0\\.3\\.0" VERSION README.md CHANGELOG.md docs prompts templates checklists agent tickets/upgrades/v0.5`
   - `git diff --check -- README.md CHANGELOG.md VERSION docs prompts templates checklists agent tools tests tickets/upgrades/v0.5 .codex`
   - `find . -type d -name __pycache__ -print`
   - If build/lint/type commands are later discovered in manifests, run them;
     currently no `package.json`, `pyproject.toml`, `tox.ini`, `pytest.ini`,
     `Makefile`, or requirements file exists at repository depth checked during
     planning.

7. Strict package validator handling

   `tools/validate_autonomous_package.py` is intentionally strict: every
   package file must match `manifest.json`, no undeclared file may exist, hashes
   must match, ticket order must be exact, dependency graph order must match,
   and active-ticket validation requires the absolute package-local ticket file.

   Therefore:

   - Run package validation against the immutable package root, not against the
     repository ticket copy.
   - Pass both `--active-ticket-id` and the package-local
     `--active-ticket-file`.
   - Do not mutate package files to make validation pass.
   - If validation fails because the package root has acquired generated files,
     stop and classify whether those files are outside Ticket 12 scope. Do not
     delete or repair package contents without explicit user approval.
   - A failure caused by using the repository ticket copy as the active file is
     operator error, not a release blocker; rerun with the package-local ticket.

8. Independent release audit

   Spawn a fresh independent release auditor after implementation proof passes.
   The auditor must inspect actual diff, release metadata, traceability,
   canonical ticket completion evidence, test output, release records, and Git
   status. The auditor must return exactly `PASS` or `FAIL`.

   Audit criteria:

   - Every canonical ticket 00 through 12 is accounted for.
   - Every supplied v0.4 child requirement maps to implementation, tests, and
     proof.
   - `VERSION`, README release status, and `CHANGELOG.md` agree on `0.5.0`.
   - No stale public current-version claim remains.
   - No unresolved release blocker remains.
   - No managed artifact is dirty except the still-uncommitted Ticket 12 work
     before delivery.
   - The pre-existing untracked ZIP is untouched and excluded.
   - No forbidden file or action was used.

   If the auditor fails:

   - Create a bounded repair list in `REVIEW.md`.
   - Use at most 3 repair rounds.
   - Re-run relevant proof after each repair.
   - Do not weaken acceptance criteria or tests.
   - If a failure requires material scope expansion, stop and invoke blocker
     resolution before implementation continues.

9. Context curation

   After release-auditor `PASS`, update only durable context:

   - `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md`
   - `agent/STATE.md`
   - `agent/DECISIONS.md` if a durable release decision was made
   - `agent/PATHS.md` if new durable release paths matter
   - `agent/CHANGELOG.md`
   - Ticket 12 `HANDOFF.md`

   Exclude raw logs, unrelated environment details, and package internals not
   needed for future work.

10. Git delivery

   Use explicit staging only. Stage only Ticket 12 approved files, excluding
   the pre-existing untracked ZIP.

   Required Git delivery commands:

   - `git status --short --branch --untracked-files=all`
   - `git diff --name-only`
   - `git add -- <explicit Ticket 12 path list>`
   - `git diff --cached --name-only`
   - `git diff --cached --check`
   - `git commit -m "TKT-2026-06-22-aew-v05-12-release-0-5-0: release 0.5.0"`
   - `git push origin main`
   - `git rev-parse HEAD`
   - `git rev-parse origin/main`
   - `test "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)"`
   - `git status --short --branch --untracked-files=all`

   Final status may still show only the preserved untracked ZIP. Any other
   uncommitted managed artifact blocks release closeout.

## Proof Gates

Ticket 12 cannot close unless all gates pass:

- Source-lock gate: package validator active-ticket check and repository
  `cmp` pass.
- Dependency gate: tickets 00 through 11 have recorded completion evidence,
  review PASS, and delivery SHA or explicit accepted delivery exception.
- Traceability gate: every imported v0.4 child requirement and new v0.5
  autonomy/Git requirement has implementation, tests, evidence, and release
  status.
- Version gate: `VERSION`, README release status, and `CHANGELOG.md` agree on
  `0.5.0`.
- Validator gate: workflow validator, package validator, run-state validator,
  JSON/TOML/YAML parsing, stale-language search, link/reference/version checks,
  unittest discovery, and diff checks pass.
- Cleanliness gate: no `__pycache__`, no generated cache artifacts, and no
  dirty managed artifacts remain after delivery.
- Audit gate: independent release auditor returns `PASS`.
- Delivery gate: final `HEAD == origin/main` proof passes on `main`.

## Stop Conditions

Stop immediately if any of these occur:

- Canonical Ticket 12 source-lock validation fails for a reason that is not an
  operator path error.
- Required work needs forbidden secret access or irreversible external side
  effects without policy authorization.
- The release would discard, stage, rewrite, move, or delete unrelated
  pre-existing user work, including the untracked ZIP.
- Package validation requires mutating `/tmp/aew-v0.5-package/...`.
- A validator/auditor failure requires material scope expansion and blocker
  resolution cannot prove it necessary and safe.
- More than 3 repair rounds are needed.
- Final `HEAD` does not equal `origin/main` after delivery.

## Acceptance Summary

This plan releases `0.5.0` only after the implemented workflow is traceable,
validated, independently audited, committed, pushed, and proven equal to
`origin/main`. It deliberately preserves
`tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip`
as unrelated pre-existing untracked work.
