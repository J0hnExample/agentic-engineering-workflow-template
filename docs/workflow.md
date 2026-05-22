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
