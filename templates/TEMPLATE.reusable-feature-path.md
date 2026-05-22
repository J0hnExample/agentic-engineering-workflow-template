# Reusable Feature Implementation Path: <Feature Family>

## Purpose

Describe when this path should be reused and what class of work it covers.

## Applies When

- The ticket changes `<area>`.
- The implementation should follow existing `<pattern>`.
- The proof can be collected through `<commands or UI route>`.

## Does Not Apply When

- The ticket requires a different owner boundary.
- The change touches unrelated subsystems.
- The user asks for diagnosis only.

## Known Entry Points

- `path/to/component`
- `path/to/service`
- `path/to/test`

## Standard Scope

Allowed by default:

- `src/<area>/**`
- `tests/<area>/**`
- `tickets/<ticket-id>.yaml`

Forbidden by default:

- `.env*`
- generated build output
- dependency folders
- unrelated shared infrastructure

## Standard Test Plan

- `npm run lint`
- `npm run typecheck`
- `npm test -- <targeted-test>`
- `npm run build`
- `npx playwright test <targeted-spec>`

Replace commands with repo-local equivalents.

## Proof Gates

- The target behavior is visible or observable.
- Targeted tests cover the changed behavior.
- Regression-sensitive flows are checked.
- Skipped checks have concrete reasons.

## Common Risks

- Scope creep into adjacent features.
- Editing shared primitives without broad tests.
- Passing unit tests while missing browser/runtime behavior.
- Leaving temporary logs, fixtures, mocks, or debug UI enabled.

## Handoff Notes

Record:

- changed files
- commands run
- proof artifacts
- skipped checks
- blockers
- risks
- exact next recommended step
