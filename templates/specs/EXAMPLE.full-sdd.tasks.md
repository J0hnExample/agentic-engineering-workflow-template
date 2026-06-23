# Tasks

Task Set ID: `TASKSET-2026-06-23-example-full-sdd`
Status: `accepted`
Feature or fix: `example-full-sdd`
Requirements: `templates/specs/EXAMPLE.full-sdd.requirements.md`
Design: `templates/specs/EXAMPLE.full-sdd.design.md`
Owning ticket: `TKT-YYYY-MM-DD-example-full-sdd`

## Task List

| Task ID | Status | Depends on | Owner role | Allowed files | Requirement IDs | Proof |
| --- | --- | --- | --- | --- | --- | --- |
| TASK-001 | accepted | none | scoped_worker | `templates/TEMPLATE.ticket.yaml` | REQ-001 | YAML parse and cross-reference check. |

## Proof Map

| Proof item | Covers | Command or inspection |
| --- | --- | --- |
| Cross-reference check | REQ-001, TASK-001 | `python tools/check_sdd_references.py` or manual equivalent. |

## Handoff Notes

- Keep ticket execution results separate from durable spec files.
- Record skipped checks with reasons.
- Record agent memory update check before closing the ticket.
