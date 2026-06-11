# Tasks

Feature or fix: `<short-name>`

## Task List

Order tasks by dependency. Keep each task small enough for one scoped worker.

| Task ID | Depends on | Owner role | Allowed files | Requirement IDs | Proof |
| --- | --- | --- | --- | --- | --- |
| TASK-001 | none | `<manager, scoped_worker, reviewer, verifier>` | `<paths>` | `<REQ-001>` | `<command or review>` |

## Implementation Notes

- `<existing pattern to follow>`
- `<boundary or stop condition>`

## Proof Map

| Proof item | Covers | Command or inspection |
| --- | --- | --- |
| `<proof>` | `<REQ-001, TASK-001>` | `<exact command or manual step>` |

## Handoff Notes

- Changed files must remain within task `allowed_files`.
- Record skipped checks with reasons.
- Record agent memory update check before closing the ticket.
