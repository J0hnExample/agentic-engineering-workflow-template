# DECISIONS

Durable project, architecture, product, and workflow decisions.
Newest entries go at the bottom.

## YYYY-MM-DD - <Decision Title>

- Context: `<why the decision was needed>`
- Decision: `<what was decided>`
- Consequence: `<what future Codex sessions must do because of it>`
- Source: `<ticket or doc path>`

## 2026-06-23 - Deterministic Git Delivery Policy

- Context: `TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree` requires commit-and-push-per-ticket without repeatedly blocking on expected workflow artifacts.
- Decision: The workflow records branch/remote delivery policy once, uses explicit path staging only, preserves unchanged non-overlapping baseline dirt, and proves local `HEAD` equals the configured upstream after push.
- Consequence: Future ticket delivery must use the recorded policy and should stop on missing upstream, divergence, changed baseline dirt, previous-ticket managed dirt, or out-of-scope staged paths.
- Source: `docs/git_delivery.md`

## 2026-06-24 - Trusted Codex Hooks

- Context: `TKT-2026-06-22-aew-v05-10-hooks-validators-selftests` adds lifecycle hooks for active-run context and bounded continuation.
- Decision: Hook configuration uses `.codex/hooks.json` with the official top-level `hooks` object. Hook changes require normal Codex project trust review; this workflow does not recommend bypassing hook trust for normal operation.
- Consequence: Future hook changes must preserve no-op behavior without active state, secret redaction, source-lock gates, and the Stop continuation circuit breaker.
- Source: `docs/autonomous_execution.md`

## 2026-06-24 - Trusted Hook Review Remains Required

- Context: `TKT-2026-06-22-aew-v05-10-hooks-validators-selftests` adds project lifecycle hooks for active-run context and bounded continuation.
- Decision: Hook configuration lives in `.codex/hooks.json` and must rely on normal Codex project trust review; bypassing hook trust is not part of normal workflow operation.
- Consequence: Future changes to hook behavior must document trust-review impact and must not weaken source-lock, scope, review, approval, or delivery gates.
- Source: `docs/autonomous_execution.md`
