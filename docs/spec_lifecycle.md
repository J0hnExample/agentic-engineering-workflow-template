# Spec Lifecycle

Use this lifecycle for significant behavior, API, data, workflow, or durable
documentation changes. It keeps implemented behavior anchored to current specs
without adding a CLI or external tool dependency.

## Repository Layout

Target repositories should use this local layout:

- `specs/current/**` contains the durable current specs for implemented
  behavior, contracts, workflows, and important constraints.
- `specs/changes/<change-id>/proposal.md` explains why the change exists, the
  intended user or maintainer outcome, and the boundaries.
- `specs/changes/<change-id>/delta-spec.md` records spec changes in `ADDED`,
  `MODIFIED`, and `REMOVED` sections.
- `specs/changes/<change-id>/design.md` records the chosen implementation
  approach when the change is non-trivial.
- `specs/changes/<change-id>/tasks.md` records dependency-ordered scoped work
  and proof.
- `specs/archive/<date>-<change-id>/**` stores accepted, superseded, or closed
  change packages.

## Propose

Create `specs/changes/<change-id>/` before implementation for significant
changes. Copy `templates/specs/TEMPLATE.delta-spec.md` to
`specs/changes/<change-id>/delta-spec.md` and fill:

- `ADDED` for new capabilities, guarantees, constraints, proof gates, or
  workflow rules.
- `MODIFIED` for existing current-spec behavior or contracts that will change.
- `REMOVED` for capabilities, requirements, constraints, or proof rules that
  will no longer apply.

The ticket should link the delta spec through `spec_refs`, keep
`spec_contract` aligned with the requirements/design/tasks package, and name the
`specs/current/**` files expected to change. Tiny quick-flow work may skip this
only when the ticket records a concrete exemption.

## Apply

During implementation, treat the delta spec as the intended contract for the
change. Keep edits inside the ticket `allowed_files`. If the implementation
needs to change a current spec or delta package outside scope, stop and revise
the ticket or create a follow-up ticket.

Parallel work must stop for reconciliation when two active tickets touch the
same `specs/current/**` file or the same requirement ID. Reconcile by merging
the intended current-spec wording, splitting ownership, or recording a blocker.

## Archive

Before a significant ticket is marked done:

1. Check implementation against each `ADDED`, `MODIFIED`, and `REMOVED` item.
2. Merge accepted changes into `specs/current/**`.
3. Move or copy the closed change package to
   `specs/archive/<date>-<change-id>/**`.
4. Record proof, changed files, skipped checks, blockers, and risks in the
   ticket `execution_result`.

If the current-spec update or archive step cannot be completed inside scope,
leave the ticket non-done or record a concrete deferred spec update blocker,
depending on the ticket stop conditions and manager decision.
