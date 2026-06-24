# Git Delivery Policy

Git delivery is part of ticket closeout when the active ticket assigns commit
and push. The default policy is `main` tracking `origin/main`, one scoped commit
per completed ticket, push to `origin`, and proof that local `HEAD` equals the
configured upstream after push.

## Policy Recording

Repository initialization asks once for the delivery policy and records it in a
workflow policy file based on `templates/TEMPLATE.workflow-policy.yaml`. Agents
do not ask again per ticket when the recorded policy is present, consistent with
the active ticket, and safe for the current repository state.

Ask again or stop with a bounded blocker when the policy is absent,
contradictory, missing an upstream, points at the wrong branch or remote, or
would require staging, discarding, rewriting, or overwriting unrelated work.

## Baseline Cleanliness

Cleanliness is evaluated relative to the ticket baseline and explicit scope.
At ticket start, record pre-existing unrelated dirty paths once with stable
content identity, such as size and SHA-256 for files. Repeated warnings for
those paths are suppressed only when the identity is unchanged and the path does
not overlap the active ticket scope.

Active ticket records, active plan/review/handoff/delivery files, the context
ledger, and required `agent/*.md` updates are authorized workflow artifacts.
Authorized does not mean always deliverable: previous-ticket managed dirt blocks
the next ticket until delivered or explicitly resolved.

## Explicit Staging

Stage only explicit paths from the active ticket scope and required workflow
records:

```text
git add -- <path...>
```

Do not use `git add -A`, `git add .`, broad path roots, or staging commands that
can include unrelated baseline work. Verify the staged set before committing and
stop if any staged path is outside the allowed scope.

## Commit And Push

A completed ticket must update its execution record before delivery so the
scoped commit is normally non-empty. Use the ticket id as the commit message
prefix, push `HEAD` to the configured branch, then prove:

```text
git rev-parse HEAD
git rev-parse origin/main
```

The two SHAs must match, or the ticket is not delivered.

## Forbidden Operations

Delivery agents and helpers must not emit or run:

- `git add -A`
- `git add .`
- branch creation, deletion, or switching for delivery
- `git worktree`
- `git stash`
- force push
- destructive reset, especially `git reset --hard`
- checkout or restore to discard unrelated work
- staging unrelated baseline paths

Use `tools/workflow_git.py` for dependency-free preflight, scoped staging,
commit, push, and SHA equality proof.
