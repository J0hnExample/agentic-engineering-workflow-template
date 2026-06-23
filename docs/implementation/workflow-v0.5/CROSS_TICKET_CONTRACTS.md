# Workflow v0.5 Cross-Ticket Contracts

## Source Authority

- The package ticket under `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/` is canonical for each ticket.
- Repository copies under `tickets/upgrades/v0.5/` are execution records only.
- Every ticket must validate the active ticket against `.git/agentic-workflow-v05-controller/PACKAGE_SOURCE_LOCK.json` before planning, implementation, review, curation, or delivery.

## Serial Execution

- Execute tickets strictly in order `00` through `12`.
- Exactly one implementation writer may edit files for an active ticket.
- Planning, review, blocker resolution, audit, and curation roles may be read-only unless the active ticket explicitly allows writes.
- Do not start the next ticket until the current ticket has a review record, execution report, handoff, and delivery proof or an explicit blocker.

## Worktree And Scope

- Preserve unrelated user or generated work byte-for-byte.
- Do not stage or modify `tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip`.
- Do not stage, commit, push, switch branches, create stashes, create worktrees, or edit `.git` unless acting as an authorized delivery/controller role under the active ticket policy.
- Use explicit path staging only during delivery. Bulk staging is forbidden.

## Evidence Standards

- Command-backed facts must name the command and result in the ticket execution report.
- Package-observed facts must be labeled as package baseline or approved-plan baseline when not independently re-verified.
- Placeholder reviews must say pending independent review and must not claim `PASS`.
- `git diff --check` must be run on scoped paths before ticket closeout when files were changed.

## Versioning

- Do not bump `VERSION`, README version text, changelog release headings, or public release state before ticket 12.
- Docs before ticket 12 may describe the planned v0.5 workflow but must not claim the repository has shipped v0.5.0.

## Handoff

- Each ticket handoff must include the next canonical ticket path, package root, repository root, managed paths, required source-lock command, and any unresolved risks.
- Context should be compact enough for the next ticket planner to read before implementation.
