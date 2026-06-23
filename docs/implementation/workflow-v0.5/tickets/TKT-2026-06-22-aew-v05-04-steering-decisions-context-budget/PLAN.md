# Ticket 04 Plan

## Scope

Add conditional steering metadata, decision locks, and bounded context packs
without removing `spec_refs`, `expert_routing`, or drift fields.

## Steps

1. Copy the canonical ticket into `tickets/upgrades/v0.5/` as an exact execution record.
2. Add `templates/steering/*` guidance files with `always`, `fileMatch`,
   `manual`, and `auto`-style metadata.
3. Add `decision_locks`, `context_budget`, `required_context`, and `steering`
   fields to ticket templates.
4. Update manager, worker, final verifier, readiness, closeout, workflow docs,
   and AGENTS template so blocking decisions stop implementation and context
   handoffs stay compact.
5. Record execution, review, handoff, and Git delivery evidence.

## Proof

- Parse YAML templates.
- Validate steering fixture matrix for always/fileMatch/manual/auto modes.
- Validate unresolved blocking decisions reject implementation.
- Measure `templates/AGENTS.md.template` byte size.
- Validate context budget excludes raw transcripts, secrets, and unrelated logs.
- Run scoped `git diff --check`.

## Hard Stops

- Source-lock validation fails.
- A blocking unresolved decision can reach implementation.
- Steering conflicts are silently merged.
- AGENTS template grows beyond the instruction-size budget.
