# Ticket 09 Plan

## Source And Baseline

- Ticket: `TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree`
- Canonical source: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree.yaml`
- Repository ticket copy: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree.yaml`
- Source-lock validation: `ACTIVE TICKET LOCK PASSED`.
- Repository ticket copy proof: `cmp` passed against the canonical package ticket.
- Start branch: `main`
- Start commit: `248b2a2376dfc07ac90fdddf5f6f32d2932e8f7c`, matching `origin/main`.
- Pre-existing untracked artifact excluded from delivery: `tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip`

## Accepted Plan

Add deterministic Git delivery policy and tooling so expected workflow artifacts
do not create repeated dirty-worktree blockers, while unrelated pre-existing
work stays preserved and unstaged. Delivery must use explicit paths, commit and
push each assigned ticket on `main`, and prove `HEAD == origin/main`.

## Planned Files

Create:

- `templates/TEMPLATE.workflow-policy.yaml`
- `templates/TEMPLATE.git-delivery-result.yaml`
- `docs/git_delivery.md`
- `prompts/git-delivery-agent.md`
- `tools/workflow_git.py`
- `tests/test_workflow_git.py`
- ticket records under `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree/`

Update:

- `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md`
- `templates/AGENTS.md.template`
- `prompts/initialize-repo.md`
- `docs/workflow.md`
- `README.md`
- `agent/DECISIONS.md`
- `agent/PATHS.md`
- `agent/CHANGELOG.md`

Do not update `.codex/**` or `docs/autonomous_execution.md`; they are outside
Ticket 09 scope.

## Git Helper Design

`tools/workflow_git.py` will be dependency-free Python using
`subprocess.run([...])`, never shell command strings. It will provide importable
functions plus a small CLI for preflight and finalize workflows.

Required behavior:

- discover branch, `HEAD`, upstream ref/SHA, and porcelain status;
- record baseline dirty paths with stable content identity where safe;
- classify authorized workflow artifacts such as ticket copies, plans,
  execution reports, reviews, handoffs, delivery records, context ledger, and
  required `agent/*.md`;
- suppress expected dirty warnings only when paths match authorized workflow
  artifacts or unchanged baseline dirty paths;
- reject changed baseline paths, unmanaged scope overlap, missing upstream,
  wrong branch, divergence, staged unrelated paths, and post-push SHA mismatch;
- verify managed changes stay inside explicit allowed paths;
- stage only with `git add -- <path...>`;
- commit with the active ticket message prefix;
- push to the configured branch and prove local `HEAD` equals upstream.

## Forbidden Operations

Docs, prompts, templates, helper construction, and tests must forbid:

- `git add -A`
- `git add .`
- branch creation or switching for delivery
- worktrees
- stashes
- force push
- destructive reset, especially `git reset --hard`
- checkout or restore used to discard unrelated work
- staging unrelated baseline paths

The helper centralizes Git command construction so tests can assert prohibited
commands are not emitted.

## Policy Artifacts

`docs/git_delivery.md` will define default `main` and `origin/main` delivery,
commit-and-push-per-ticket, explicit staging only, baseline-relative cleanliness,
authorized workflow artifacts, expected-dirty suppression, previous-ticket leak
prevention, and post-delivery proof fields.

`templates/TEMPLATE.workflow-policy.yaml` will capture branch, remote, upstream,
auto-commit/push, explicit staging, authorized artifact patterns, baseline dirty
paths, and prohibited Git operations.

`templates/TEMPLATE.git-delivery-result.yaml` will capture ticket id,
baseline branch/head/upstream, explicit staged paths, excluded pre-existing
paths, commit SHA/message, push result, local/upstream SHA equality, and
post-delivery managed state.

`prompts/git-delivery-agent.md` will instruct delivery agents to preserve
unrelated changes, stage only explicit paths, produce bounded blockers, and avoid
product edits.

Initialization and workflow docs will record the delivery policy once so agents
do not ask again per ticket unless the policy is absent, contradictory, or
unsafe.

## Tests

Create `tests/test_workflow_git.py` using `unittest`, temporary Git repositories,
and local bare remotes only.

Required scenarios:

- expected-dirty suppression for unchanged baseline dirt plus authorized
  workflow artifacts;
- explicit staging excludes unrelated changes;
- commit, push, and upstream equality proof in a local bare-origin fixture;
- divergence rejection before staging/commit;
- missing upstream rejection;
- changed baseline dirty path rejection;
- prohibited Git commands are never emitted by helper paths;
- previous-ticket managed dirt blocks the next ticket.

## Required Proof

- `cmp /tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree.yaml tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree.yaml`
- `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_workflow_git`
- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -p 'test*.py'`
- `git diff --check -- docs/implementation/workflow-v0.5 tickets/upgrades/v0.5 templates docs prompts tools tests agent README.md`
- `git status --short --untracked-files=all`
- no generated `__pycache__` directories after tests

## Review Focus

The independent reviewer must inspect the actual diff, canonical ticket copy
proof, helper command construction, temporary Git fixtures, dirty-path
preservation, staged path verification, divergence and missing-upstream
blockers, documentation wording around baseline-relative cleanliness, and that
the pre-existing ZIP remains excluded from staging.

## Context Curation

After review `PASS`, curate durable context only: policy files added, helper and
test entry points, proof commands/results, accepted delivery behavior, residual
risks, and the next-ticket expectation that no prior managed dirt remains after
delivery and `HEAD == origin/main`.
