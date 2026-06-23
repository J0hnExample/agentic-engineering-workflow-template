# Next Agent Capsule

## Assignment

- Ticket:
- Role:
- Allowed write paths:
- Forbidden paths:

## Must Read First

- `AGENTS.md`
- active ticket
- current `RUN_STATE.json`
- latest ticket `HANDOFF.md`
- files in scope

## Controller Gates

- Validate source lock before role spawn.
- Validate `RUN_STATE.json` before writing.
- Respect the writer lock.
- Resume at the recorded first incomplete phase.
- After a recorded commit, verify the SHA and upstream proof instead of committing again.

## Evidence To Return

- changed files
- commands and results
- proof summary
- skipped checks
- blockers and risks
