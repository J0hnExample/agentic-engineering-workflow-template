# Tasks

Task Set ID: `TASKSET-YYYY-MM-DD-short-name`
Status: `unknown | proposed | accepted | superseded`
Feature or fix: `<short-name>`
Requirements: `<requirements spec path>`
Design: `<design spec path>`
Owning ticket: `<ticket-id>`

## Task List

Order tasks by dependency. Keep each task small enough for one scoped worker.

| Task ID | Status | Depends on | Owner role | Allowed files | Requirement IDs | Proof |
| --- | --- | --- | --- | --- | --- | --- |
| TASK-001 | proposed | none | `<manager, scoped_worker, reviewer, verifier>` | `<paths>` | `<REQ-001>` | `<command or review>` |

Allowed statuses: `unknown`, `proposed`, `accepted`, `superseded`.

## Proof Map

| Proof item | Covers | Command or inspection |
| --- | --- | --- |
| `<proof>` | `<REQ-001, TASK-001>` | `<exact command or manual step>` |

## Handoff Notes

- Changed files must remain within task `allowed_files`.
- Record skipped checks with reasons.
- Record agent memory update check before closing the ticket.
