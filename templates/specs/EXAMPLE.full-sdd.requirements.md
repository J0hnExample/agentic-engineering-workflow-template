# Requirements

Spec ID: `REQSET-2026-06-23-example-full-sdd`
Status: `accepted`
Feature or fix: `example-full-sdd`
Owning ticket: `TKT-YYYY-MM-DD-example-full-sdd`

## Summary

Add a documented workflow feature through explicit requirements, design, tasks,
ticket scope, and proof.

## Source Of Truth

- User request: `tickets/TKT-YYYY-MM-DD-example-full-sdd.yaml`
- Product/spec source: `none`
- Related design: `templates/specs/EXAMPLE.full-sdd.design.md`
- Related tasks: `templates/specs/EXAMPLE.full-sdd.tasks.md`

## Requirements

| Requirement ID | Status | Requirement | Acceptance criteria | Proof target |
| --- | --- | --- | --- | --- |
| REQ-001 | accepted | Ticket templates can reference external SDD specs. | When a full-SDD ticket is created, it shall name requirements, design, and tasks spec paths. | YAML parse and cross-reference check. |

## Non-Goals

- No product runtime behavior.

## Ambiguity Log

| Question | Current handling | Owner | Blocks implementation |
| --- | --- | --- | --- |
| none | none | manager | no |

## Traceability

| Requirement ID | Design section | Task ID | Ticket ID | Evidence |
| --- | --- | --- | --- | --- |
| REQ-001 | Interfaces And Contracts | TASK-001 | TKT-YYYY-MM-DD-example-full-sdd | `python tools/check_sdd_references.py` or manual equivalent. |
