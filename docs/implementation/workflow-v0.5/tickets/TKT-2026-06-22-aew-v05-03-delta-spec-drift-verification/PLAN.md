# Ticket 03 Plan

## Scope

Add delta-spec lifecycle and read-only spec drift verification that extends the
ticket 02 SDD artifact package.

## Steps

1. Copy the canonical ticket into `tickets/upgrades/v0.5/` as an exact execution record.
2. Add `TEMPLATE.delta-spec.md` and example delta/drift fixtures.
3. Add `docs/spec_lifecycle.md`, `prompts/spec-drift-verifier.md`, and `checklists/spec-drift.md`.
4. Add `execution_result.spec_alignment` fields.
5. Update ticket, AGENTS, workflow, closeout, and final verifier guidance so accepted deltas update durable specs and blocking drift fails closeout.
6. Record execution, review, handoff, and Git delivery evidence.

## Proof

- Parse changed YAML templates and canonical ticket copy.
- Validate delta template/example includes `ADDED`, `MODIFIED`, and `REMOVED`.
- Validate drift fixtures cover missing test, stale requirement, and undocumented public behavior.
- Validate `execution_result.spec_alignment` fields.
- Run scoped `git diff --check`.

## Hard Stops

- Source-lock validation fails.
- The verifier is allowed to edit files.
- Blocking drift can be silently ignored by final verification.
- Accepted deltas can close without current-spec updates or owner/follow-up.
