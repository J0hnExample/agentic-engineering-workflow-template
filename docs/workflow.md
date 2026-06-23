# Codex Workflow

This template supports Codex-first planning, execution, verification, and
memory closeout for a target repository.

## Basic Workflow

1. Plan one bounded step from current repository evidence.
2. Create a ticket from the installed target template
   `tickets/templates/TEMPLATE.ticket.yaml`.
3. Start a fresh context for ticket execution.
4. Execute only the ticket scope.
5. Run the ticket proof gates.
6. Close out with the installed target template
   `tickets/templates/TEMPLATE.execution-result.yaml`.
7. Update `agent/*.md`, or record `agent memory checked: no update needed`.

Fresh-context execution is intentional. The ticket must carry enough context,
scope, proof requirements, and stop conditions for a new Codex session to do the
work without relying on unstated chat history.

## Ticket Chains

Use a ticket chain for complex work, risky changes, visual work, migrations, or
multi-stage delivery.

- A parent orchestrator ticket owns the whole outcome.
- Create the parent from the installed target template
  `tickets/templates/TEMPLATE.orchestrator-ticket.yaml`.
- Child tickets own narrow implementation or verification slices.
- Create child tickets from the installed target template
  `tickets/templates/TEMPLATE.ticket.yaml`.
- Ticket comments and execution results pass context into the next child ticket.
- Record worker closeout with the installed target template
  `tickets/templates/TEMPLATE.execution-result.yaml`.
- The manager looks back at recent child ticket results before planning the next
  step.
- Failed approaches, blockers, skipped checks, and accepted proof should be
  carried forward explicitly.
- A final verifier checks the completed chain before the parent ticket closes.

Before installation, the workflow package stores these source files under
`templates/`. After installation, use the target repository paths under
`tickets/templates/`.

## Native Codex Profiles

Projects can provide optional native Codex profiles under `.codex/agents/*.toml`
with shared subagent limits in `.codex/config.toml`. Native profiles are the
preferred path when Codex loads project configuration; the markdown prompts in
`prompts/` remain the fallback for tools or environments that do not load those
profiles.

The workflow keeps one implementation writer active for a ticket:
`workflow-ticket-implementer`. Planning, review, blocker resolution, release
audit, and expert-review profiles are read-only. Context curation and Git
delivery have narrow write responsibilities and should not edit product
behavior.

Expert reviewers are selected by risk and evidence needs:

| Risk area | Native profile |
| --- | --- |
| Architecture, contracts, public API shape | `expert-architecture-reviewer` |
| Tests, fixtures, proof quality | `expert-test-reviewer` |
| Secrets, auth, permissions, dependency risk | `expert-security-reviewer` |
| UI, accessibility, keyboard or visual regressions | `expert-ux-accessibility-reviewer` |
| Latency, memory, scaling, expensive work | `expert-performance-reviewer` |
| Schema, persistence, migrations, backfills | `expert-data-migration-reviewer` |
| Release notes, version claims, install docs | `expert-release-docs-reviewer` |

Do not ask every expert by default. Each expert response should record
`profile_used`, the trigger, findings, required proof, and a bounded next
action.

## SDD Spec Artifacts

For non-trivial work, keep durable requirements, design decisions, and task
decomposition in linked spec files instead of overloading the ticket. The ticket
still owns execution scope, proof, and closeout.

Use:

- `templates/specs/TEMPLATE.requirements.md` for stable requirement IDs,
  acceptance criteria, ambiguity logs, and proof targets.
- `templates/specs/TEMPLATE.design.md` for accepted design decisions, impacted
  files, interfaces, failure modes, and test strategy.
- `templates/specs/TEMPLATE.tasks.md` for dependency-ordered scoped tasks and
  proof mapping.

Ticket `spec_refs` must either point to requirements, design, and tasks specs or
record a concrete `no_spec` reason. Tiny low-risk documentation or mechanical
changes can skip full specs when there is no behavior, API, data, dependency,
security, or UI contract change. Workers must stop when a blocking requirement
or design decision remains `unknown` or `proposed`.

Delta specs describe changes to durable specs:

- `ADDED` for new behavior or proof rules.
- `MODIFIED` for intentional changes to existing contracts.
- `REMOVED` for behavior or constraints that no longer apply.

Before closeout, non-trivial tickets should run a read-only spec drift check and
record `execution_result.spec_alignment`. Final verification must treat a
blocking drift verdict as a ticket failure.

## Roles

`manager-orchestrator` keeps the whole chain in view, creates child tickets,
chooses the next bounded action, reviews worker output, and decides whether to
advance, retry, checkpoint, or stop.

`scoped worker` executes one ticket inside its allowed files. It reports changed
files, commands, proof, skipped checks, blockers, risks, and memory updates.

`read-only reviewer` is a Codex subagent or role prompt that analyzes planning,
risk, architecture, tests, or review questions without editing files. Reviewer
output should become ticket context for the next worker.

`final verifier` checks the result against scope, proof gates, regression gates,
skipped checks, and memory closeout. It does not repair issues unless the
manager creates or assigns a repair ticket.

All Codex roles, including subagents, inherit the installed `AGENTS.md`, active
ticket scope, approval boundaries, forbidden actions, and verification
requirements. A subagent may not push, deploy, release, publish, edit secrets,
install dependencies, widen scope, or write out-of-scope reports unless the
active ticket and user approval allow the exact action.

## Execution Modes

`standard_worker` means one scoped worker completes one bounded ticket with
direct proof.

`expert_supported` means a read-only Codex planning or review subagent runs
before or after one scoped worker.

`bounded_expert_rounds` means the manager runs a capped loop: collect proof,
ask a read-only Codex reviewer, assign one bounded worker task, run proof, then
checkpoint or record a blocker.

`research_only` means read-only Codex reviewers analyze and recommend. Product
files do not change.

## Agent Memory

Update `agent/*.md` only when a ticket changes durable project knowledge:
current state, decisions, known issues, follow-up tasks, important paths,
service assumptions, or changelog notes.

If no update is needed, record this exact phrase in the ticket result:

```text
agent memory checked: no update needed
```

Do not invent unknowns. Use repository evidence, explicit user input, verified
commands, or ticket results.
