# Ticket 02 Plan

## Scope

Add reusable SDD requirements, design, and tasks artifacts with stable IDs and ticket cross-references while preserving quick no-spec tickets for tiny low-risk work.

## Steps

1. Copy the canonical ticket into `tickets/upgrades/v0.5/` as an exact execution record.
2. Add `templates/specs/TEMPLATE.requirements.md`, `TEMPLATE.design.md`, and `TEMPLATE.tasks.md`.
3. Add example full-SDD and quick no-spec fixtures.
4. Add `spec_refs` to ticket and orchestrator templates without removing existing safety fields or ticket scope controls.
5. Update initialization, manager, worker, readiness, closeout, AGENTS template, and workflow docs to describe minimal SDD package creation and no-spec escalation rules.
6. Record execution, review, handoff, and Git delivery evidence.

## Proof

- Parse changed YAML templates and fixture ticket.
- Validate stable IDs and cross-references in full-SDD examples.
- Validate quick no-spec fixture has a concrete `not_required_reason`.
- Check no existing safety fields were removed from ticket templates.
- Run scoped `git diff --check`.

## Hard Stops

- Source-lock validation fails.
- Existing ticket safety fields are removed.
- Quick/no-spec mode can bypass risk gates.
- Blocking unknown requirements or design decisions are allowed to reach implementation.
