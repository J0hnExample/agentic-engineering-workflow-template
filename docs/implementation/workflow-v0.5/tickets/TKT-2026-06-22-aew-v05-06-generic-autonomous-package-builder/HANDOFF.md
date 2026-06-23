# Ticket 06 Handoff

## Current State

- Generic autonomous package prompts, skeleton templates, builder, validator,
  tests, and docs have been implemented in the allowed paths.
- Required proof commands passed.
- Independent review failed once, repair round 1 fixed validator strictness,
  and re-review passed.
- Fixture ZIPs were generated at:
  - `/tmp/aew-autonomous-fixture.zip`
  - `/tmp/aew-autonomous-fixture-multi.zip`
- Repository ticket copy still matches the canonical package ticket by `cmp`.
- No Git staging, commit, push, branch switch, stash, worktree, dependency
  install, or destructive repository operation was performed.

## Important Paths

- Builder: `tools/build_autonomous_package.py`
- Validator: `tools/validate_autonomous_package.py`
- Tests: `tests/test_autonomous_package.py`
- Skeleton: `templates/autonomous-package/`
- Docs: `docs/autonomous_ticket_packages.md`
- Prompts: `prompts/create-autonomous-ticket-package.md`,
  `prompts/generic-autonomous-software-request.md`

## Follow-Up

- Stage only the explicit scoped paths, keep the pre-existing untracked package
  ZIP out of staging, commit, push, and prove `HEAD == origin/main`.

## Review Result

- Review round 1: FAIL.
- Repair rounds used: 1.
- Re-review: PASS.
- Passing reviewer subagent: `019ef34a-ef13-76f3-bf34-00a38d2adc76`.
