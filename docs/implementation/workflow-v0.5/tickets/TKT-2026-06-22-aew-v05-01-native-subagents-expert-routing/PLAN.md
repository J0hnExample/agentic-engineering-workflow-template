# Ticket 01 Plan

## Scope

Add project-scoped native Codex custom-agent profiles and risk-based expert routing while preserving the existing markdown prompts as tool-agnostic fallbacks.

## Steps

1. Copy the canonical ticket into `tickets/upgrades/v0.5/` as an exact repository execution record.
2. Add `.codex/config.toml` with bounded subagent settings: `max_threads = 4` and `max_depth = 1`.
3. Add workflow agent profiles for global planning, ticket planning, implementation, independent review, context curation, Git delivery, blocker resolution, and release audit.
4. Add read-only expert reviewer profiles for architecture, tests, security, UX/accessibility, performance, data/migration, and release/docs.
5. Update ticket templates, prompts, checklists, workflow docs, and README to document risk-based routing, single-writer policy, read-only profile boundaries, and markdown fallback behavior.
6. Record execution, review, handoff, and Git delivery evidence under the ticket 01 implementation directory.

## Proof

- Parse every `.codex/**/*.toml` file with Python `tomllib`.
- Validate unique custom-agent names and required keys.
- Confirm read-only roles have `sandbox_mode = "read-only"`.
- Confirm the only implementation writer profile is `workflow-ticket-implementer`.
- Search durable profiles for model pins.
- Parse changed YAML templates and ticket copy.
- Run scoped `git diff --check`.

## Hard Stops

- Source-lock validation fails.
- More than one implementation writer is introduced.
- Durable profiles pin a model.
- Native profiles replace markdown prompt fallbacks.
- Scope expands into hooks, controller implementation, release/version bump, or wholesale v0.4 branch merge.
