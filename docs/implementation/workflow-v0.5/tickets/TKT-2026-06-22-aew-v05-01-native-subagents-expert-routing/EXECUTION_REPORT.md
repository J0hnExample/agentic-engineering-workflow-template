# Ticket 01 Execution Report

## Changed Files

- `.codex/config.toml`
- `.codex/agents/*.toml`
- `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-01-native-subagents-expert-routing.yaml`
- `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-01-native-subagents-expert-routing/*`
- `templates/TEMPLATE.ticket.yaml`
- `templates/TEMPLATE.orchestrator-ticket.yaml`
- `prompts/manager-orchestrator.md`
- `prompts/read-only-expert.md`
- `prompts/scoped-worker.md`
- `prompts/final-verifier.md`
- `checklists/ticket-readiness.md`
- `checklists/closeout.md`
- `docs/workflow.md`
- `README.md`
- `agent/PATHS.md`
- `agent/CHANGELOG.md`

## Commands Run

| Command | Result |
| --- | --- |
| `validate_active_ticket.py --ticket-id TKT-2026-06-22-aew-v05-01-native-subagents-expert-routing ...` | `ACTIVE TICKET LOCK PASSED`. |
| Python `tomllib` parse over `.codex/**/*.toml` | `TOML CHECK PASSED: 15 agents`; `.codex/config.toml` has `max_threads = 4`, `max_depth = 1`. |
| Custom-agent uniqueness and required-key check | Passed; every custom agent has `name`, `description`, and `developer_instructions`. |
| Read-only sandbox check | Passed for global planner, ticket planner, independent reviewer, blocker resolver, release auditor, and all expert reviewers. |
| Single-writer check | Passed; `workflow-ticket-implementer` is the only implementation writer profile. |
| Model-pin search in `.codex` | No durable `model = "gpt..."`, `model = "o..."`, or `model = "codex..."` pins found. |
| YAML parse for changed templates and repository ticket copy | Passed. |
| `cmp` canonical ticket 01 vs repository copy | `cmp_exit=0`. |
| `git diff --check -- .codex prompts templates checklists docs README.md agent tickets/upgrades/v0.5` | Passed with no output. |

## Acceptance Notes

- Native project-scoped Codex profiles are added under `.codex/agents/*.toml`.
- Markdown role prompts remain the fallback path when native profiles are unavailable.
- Expert routing is risk/evidence based and explicitly avoids a second manager hierarchy.
- Ticket templates now require either selected expert profiles or an explicit not-required reason.
- No hooks, controller implementation, release/version bump, or v0.4 branch merge was performed.

## Agent Memory

- `agent/PATHS.md` records the new native Codex config/profile paths.
- `agent/CHANGELOG.md` records the ticket 01 workflow change.
