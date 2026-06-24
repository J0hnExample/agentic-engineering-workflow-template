# Handoff

Ticket: `TKT-2026-06-22-aew-v05-10-hooks-validators-selftests`

## Current State

- Implementation completed inside Ticket 10 scope.
- Independent review passed by subagent
  `019efa44-64a6-7273-b92e-20f8eeeb6d6b`.
- Manager self-review repaired `.codex/hooks.json` to require the official
  top-level `hooks` object before independent review.
- Git delivery is not started.
- The pre-existing untracked ZIP remains outside implementation scope.

## Durable Facts

- Hook config lives at `.codex/hooks.json`.
- Hook helpers live under `tools/codex_hooks/`.
- Aggregate validation command is
  `PYTHONDONTWRITEBYTECODE=1 python tools/validate_workflow.py`.
- Focused hook/validator test command is
  `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_codex_hooks tests.test_validate_workflow`.
- Full test discovery passed with 51 tests.
- Hook changes require normal Codex project trust review. Do not recommend
  bypassing hook trust for normal workflow operation.
- Stop continuation requires valid source lock, nonterminal state, an incomplete
  next phase, remaining continuation budget, and a progress token that differs
  from the last continuation token.

## Next Agent

Run scoped Git delivery on `main`, excluding the pre-existing ZIP.
