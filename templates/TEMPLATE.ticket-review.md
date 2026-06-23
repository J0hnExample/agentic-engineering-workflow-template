# Ticket Review

Ticket: `<ticket id>`
Reviewer: `<independent reviewer id>`
Status: `pending`

## Inputs Inspected

- Active ticket:
- Accepted plan:
- Actual diff:
- Changed files:
- Tests and evidence:
- Specs or workflow docs:

## Verdict

`PENDING | PASS | FAIL`

Do not mark the ticket done after `FAIL`. A later independent review of the
repaired diff must return `PASS` before closeout.

## Findings

Use this structure for every `FAIL` finding:

- Finding id:
- Severity:
- File or path:
- Expected:
- Actual:
- Failed criterion:
- Reproduction or evidence:
- Required repair:

## Repair Gate

- Repair attempts used:
- Maximum repair attempts: `3`
- Materially different attempts:
- Acceptance criteria unchanged: `yes | no`
- Tests weakened: `yes | no`
- Latest review after repair: `pending | PASS | FAIL`

## PASS Summary

- Scope alignment:
- Test/evidence alignment:
- Spec/workflow alignment:
- Residual risks:
