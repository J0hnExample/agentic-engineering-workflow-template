# Spec Lifecycle

Use this lifecycle for significant behavior, API, data, workflow, or durable
documentation changes. It keeps implemented behavior anchored to current specs
without adding a runtime dependency.

## Layout

- `templates/specs/TEMPLATE.requirements.md`: durable requirements template.
- `templates/specs/TEMPLATE.design.md`: durable design template.
- `templates/specs/TEMPLATE.tasks.md`: durable task template.
- `templates/specs/TEMPLATE.delta-spec.md`: proposed changes to current specs.
- `specs/current/**`: recommended target-repository location for accepted
  durable specs.
- `specs/changes/<change-id>/**`: recommended target-repository location for
  in-flight change packages.
- `specs/archive/<date>-<change-id>/**`: recommended target-repository location
  for accepted or superseded change packages.

## Delta Semantics

- `ADDED`: new behavior, guarantees, constraints, proof gates, or workflow rules.
- `MODIFIED`: existing behavior or contracts that intentionally change.
- `REMOVED`: behavior, guarantees, constraints, or proof rules that no longer
  apply.

Each delta item must name a status, requirement ID, current-spec update target,
and proof. Accepted deltas must update durable specs before closeout unless a
blocking deferred-spec update is recorded with owner and follow-up ticket.

## Closeout Rules

Before a significant ticket is marked done:

1. Compare implementation and proof against every `ADDED`, `MODIFIED`, and
   `REMOVED` item.
2. Update durable current specs for accepted deltas.
3. Archive or close the change package.
4. Record `execution_result.spec_alignment`.

Do not let removed behavior disappear silently. Do not let changed public
behavior ship without either an accepted delta or an explicit no-spec reason for
tiny low-risk work.
