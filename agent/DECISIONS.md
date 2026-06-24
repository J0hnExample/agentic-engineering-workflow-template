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
