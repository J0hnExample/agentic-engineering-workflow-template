# PATHS

Important repo paths, commands, routes, artifact locations, and generated output
locations. Prefer repo-relative paths and named external locations. Avoid
private absolute paths unless the user explicitly approves a narrow local-only
note.

## Source Areas

- `<area>`: `<path>`
- Native Codex profile config: `.codex/config.toml`
- Project-scoped Codex custom agents: `.codex/agents/*.toml`
- Workflow v0.5 implementation records: `docs/implementation/workflow-v0.5/`
- SDD spec templates and examples: `templates/specs/`

## Tests And Proof

- Lint: `<command>`
- Typecheck: `<command>`
- Unit tests: `<command>`
- Build: `<command>`
- E2E/browser: `<command>`

## Artifacts

- Screenshots: `<path>`
- Test output: `<path>`
- Logs: `<path>`
