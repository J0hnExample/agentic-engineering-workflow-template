# Delta Spec

Delta ID: `DELTA-2026-06-23-example`
Status: `accepted`
Change: `example-drift-fixture`
Owning ticket: `TKT-YYYY-MM-DD-example-delta`
Current specs affected:

- `templates/specs/EXAMPLE.full-sdd.requirements.md`

## ADDED

| Delta Item ID | Status | Requirement ID | New behavior, guarantee, constraint, or proof rule | Required current-spec update | Proof |
| --- | --- | --- | --- | --- | --- |
| ADD-001 | accepted | REQ-001 | Tickets record `spec_refs` for full SDD work. | Add traceability row to current requirements. | YAML and cross-reference check. |

## MODIFIED

| Delta Item ID | Status | Requirement ID | Existing behavior | New behavior | Required current-spec update | Proof |
| --- | --- | --- | --- | --- | --- |
| MOD-001 | accepted | REQ-001 | Ticket carried all requirements directly. | Ticket links durable spec files and owns execution scope. | Template inspection. |

## REMOVED

| Delta Item ID | Status | Requirement ID | Removed behavior, guarantee, constraint, or proof rule | Replacement or removal reason | Required current-spec update | Proof |
| --- | --- | --- | --- | --- | --- | --- |
| REM-001 | accepted | REQ-001 | Silent omission of removed behavior from specs. | Removed behavior must be listed in delta specs. | Checklist inspection. |

## Closeout

- All accepted items have current-spec update targets.
- No deferred drift remains.
