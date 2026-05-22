# TODO

Follow-up work that remains after completed tickets.

- [ ] `<actionable follow-up>` - source: `<ticket path>`

## First-Read Bootstrap Rule

When an agent reads this file for the first time in a new or newly bootstrapped
project, it should inspect the repository stack and propose initial `agent`
entries before implementation starts.

Use repo evidence only:

- package manifests and lockfiles
- framework config
- test config
- build config
- CI workflow files
- Docker or compose files
- environment examples
- existing docs and scripts

Propose updates for:

- `agent/STATE.md` - project purpose, stack, current milestone, and proof
  baseline
- `agent/PATHS.md` - important source paths, commands, routes, and artifact
  locations
- `agent/SERVICES.md` - external services, environment variables by name,
  local mocks, jobs, queues, databases, and credential policy
- `agent/KNOWN_ISSUES.md` - hazards discovered during setup or repo inspection
- `agent/TODO.md` - concrete follow-up tasks that are already visible

Rules:

- Do not invent values.
- Mark unknowns explicitly.
- Prefer concrete repo-local commands over generic examples.
- Do not store secrets.
- Do not write updates unless they are inside the active ticket scope or the
  user approves the bootstrap update.

## Closeout Rule

Every ticket must check whether this file needs updates before closing. If no
follow-up remains, the ticket result should record:

```text
agent memory checked: no update needed
```
