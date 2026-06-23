# Workflow v0.5 Global Plan

## Baseline

- Repository: `J0hnExample/agentic-engineering-workflow-template`
- Local root: `/home/sascha/workspace/agentic-engineering-workflow-template`
- Package root: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade`
- Branch at ticket 00 start: `main`
- HEAD/upstream at ticket 00 start: `612d8a3f165eb3c3a127fe7478f405d2ad415802`
- Upstream: `origin/main`
- Origin URL: `git@github.com:J0hnExample/agentic-engineering-workflow-template.git`
- Current repository version: `0.3.0` in `VERSION` and `README.md`
- Pre-existing unrelated/generated artifact: `tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip`
- Canonical package validation: passed.
- Active ticket source lock: passed for `TKT-2026-06-22-aew-v05-00-reality-audit-provenance`.
- Package bootstrap/controller state: already present and source-lock readable at implementation start; no `.git` writes were performed by this ticket writer.
- Ticket source collisions: none observed in repository-local ticket paths.
- v0.4 read-only evidence branch: `feature/sdd-workflow-v0.4.0` at `9fbab079609f8f4ff634d9b44da0599cffcf7982`; treat as evidence only. The approved baseline records whitespace issues in that evidence and it must not be merged, cherry-picked, or applied.

## Strict Ticket Order

| Order | Ticket | Delivery focus |
| --- | --- | --- |
| 00 | `reality-audit-provenance` | Current-state baseline, v0.4 provenance, global plan, traceability, handoff. |
| 01 | `native-subagents-expert-routing` | Codex custom-agent profiles and expert routing with markdown fallbacks. |
| 02 | `sdd-spec-artifacts` | Machine-readable SDD requirements, design, and task artifacts. |
| 03 | `delta-spec-drift-verification` | Delta-spec lifecycle plus cross-artifact drift verification. |
| 04 | `steering-decisions-context-budget` | Conditional steering, decision locks, and bounded context packs. |
| 05 | `quick-flow-single-ticket` | Quick flow plus autonomous execution for one ticket. |
| 06 | `generic-autonomous-package-builder` | Source-locked generic autonomous package builder. |
| 07 | `serial-controller-resume` | Serial multi-agent controller, run state, and safe resume. |
| 08 | `review-repair-blocker-context` | Independent review, repair loop, blocker resolver, and context curator. |
| 09 | `git-delivery-clean-worktree` | Deterministic clean-worktree handling and automatic per-ticket delivery. |
| 10 | `hooks-validators-selftests` | Trusted hooks, validators, and adversarial self-tests. |
| 11 | `docs-installation-modernization` | Installation, AGENTS guidance, and public docs modernization. |
| 12 | `release-0-5-0` | Final 0.5.0 release proof and version bump. |

Ticket order is serial. Each ticket starts from the package canonical ticket, validates the active source lock, creates or updates its repository execution records, receives independent review, then hands off compact context to the next ticket.

## Tests And Evidence Strategy

- Before each ticket: validate package integrity and active-ticket source lock.
- For documentation and YAML records: parse all package tickets, parse imported v0.4 ticket-pack YAMLs, and run `git diff --check` on scoped paths.
- For implementation tickets: run the ticket's required tests first, then the narrowest repository regression checks that cover touched behavior.
- Evidence records must separate command-backed facts from package/user baseline facts. Placeholder review records must not claim `PASS` before independent review.
- Do not treat generated package files, mocks, or documentation claims as runtime proof.

## Git Delivery Strategy

- Work on `main` only.
- Preserve unrelated changes and generated artifacts; do not stage or modify `tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip`.
- Use explicit path staging only during delivery. This implementation writer did not stage, commit, push, switch branches, create stashes, create worktrees, or edit `.git`.
- Later delivery agents must prove local `HEAD` equals `origin/main` after each pushed ticket commit.

## Risks

- The repository is version `0.3.0`; no premature version bump is allowed before ticket 12.
- v0.4 evidence is provenance, not an already-applied implementation.
- The workflow introduces autonomous execution and per-ticket delivery, so source-lock validation and explicit staging must remain hard gates.
- Local package/controller state is outside normal tracked files; ticket records must preserve enough command evidence for reviewers without treating repository copies as canonical tickets.
