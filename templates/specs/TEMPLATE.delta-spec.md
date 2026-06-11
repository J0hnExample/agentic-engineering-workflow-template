# Delta Spec

Change ID: `<change-id>`

## Purpose

Describe the significant behavior, API, workflow, data, or documentation change
this delta proposes. Keep it bounded to the active ticket or ticket chain.

## Current Spec References

| Current spec | Capability or contract | Expected update |
| --- | --- | --- |
| `specs/current/<area>.md` | `<existing behavior or contract>` | `<merge, replace, remove, or none>` |

## ADDED

List new capabilities, guarantees, constraints, proof gates, or workflow rules.
Use stable requirement IDs when this delta supports implementation work.

- `REQ-001`: `<new requirement>`

## MODIFIED

List current spec statements that change. Reference the current spec path and
the intended new wording or behavior.

| Current spec | Existing statement or section | New behavior |
| --- | --- | --- |
| `specs/current/<area>.md` | `<section or requirement>` | `<replacement behavior>` |

## REMOVED

List current spec statements, capabilities, tasks, or proof rules that are being
retired. Include the compatibility or migration note when removal affects users
or dependent work.

| Current spec | Removed item | Reason and compatibility note |
| --- | --- | --- |
| `specs/current/<area>.md` | `<item>` | `<reason>` |

## Conflicts And Dependencies

- Parallel changes touching the same `specs/current/**` file or same
  requirement ID must stop and reconcile before implementation or archive.
- Depends on: `<ticket, change-id, decision, or none>`
- Blocks: `<ticket, change-id, decision, or none>`

## Proof And Archive Plan

| Proof target | Covers | Command or inspection |
| --- | --- | --- |
| `<proof>` | `<ADDED/MODIFIED/REMOVED item>` | `<command or manual check>` |

Closeout result:

- [ ] Delta was merged into `specs/current/**`.
- [ ] Delta was moved or copied to `specs/archive/<date>-<change-id>/`.
- [ ] Spec update was deferred with a blocker recorded in the ticket.
