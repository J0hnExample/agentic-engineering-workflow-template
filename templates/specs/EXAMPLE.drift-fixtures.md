# Spec Drift Fixtures

These fixtures document expected verifier outcomes without requiring a project
runtime.

## Positive Fixture

- Requirement: `REQ-001` is accepted.
- Design: `DEC-001` is accepted.
- Task: `TASK-001` is accepted.
- Ticket proof: YAML parse and cross-reference checks passed.
- Expected verifier verdict: `pass`.

## Missing Test Fixture

- Requirement: `REQ-MISSING-TEST` has acceptance criteria.
- Execution result claims implementation is done.
- Proof list lacks a command, test, review, or manual inspection for the
  acceptance criteria.
- Expected verifier verdict: `fail`.
- Blocking finding: missing proof for accepted requirement.

## Stale Requirement Fixture

- Delta `MOD-STALE-REQ` changes behavior.
- Durable requirements still describe the old behavior.
- Expected verifier verdict: `fail`.
- Blocking finding: accepted delta not reflected in durable current specs.

## Undocumented Public Behavior Fixture

- Diff changes README-visible or workflow-visible behavior.
- No requirement, design decision, delta spec, public doc update, or explicit
  no-spec reason covers the behavior.
- Expected verifier verdict: `fail`.
- Blocking finding: implemented but unspecified public behavior.
