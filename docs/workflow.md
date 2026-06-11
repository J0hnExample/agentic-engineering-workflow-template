# Codex Workflow

This template supports Codex-first planning, execution, verification, and
memory closeout for a target repository.

## Basic Workflow

1. Plan one bounded step from current repository evidence.
2. For non-trivial work, create or update compact spec artifacts for
   requirements, design, and tasks. For tiny quick-flow work, record the
   exemption reason in the ticket.
3. Create a ticket from the installed target template
   `tickets/templates/TEMPLATE.ticket.yaml`.
4. Start a fresh context for ticket execution.
5. Execute only the ticket scope.
6. Run the ticket proof gates.
7. Close out with the installed target template
   `tickets/templates/TEMPLATE.execution-result.yaml`.
8. Update `agent/*.md`, or record `agent memory checked: no update needed`.

Fresh-context execution is intentional. The ticket must carry enough context,
scope, proof requirements, and stop conditions for a new Codex session to do the
work without relying on unstated chat history.

## Spec Artifacts

Non-trivial implementation work starts from a compact spec package:

- `requirements.md` captures user stories, EARS-style acceptance criteria,
  Given-When-Then cases, constraints, preconditions, postconditions,
  invariants, non-goals, ambiguity handling, and proof targets.
- `design.md` captures the chosen approach, impacted files, interfaces, data
  flow, failure modes, security/privacy notes, test strategy, and compatibility
  concerns.
- `tasks.md` captures dependency-ordered tasks with owner role, allowed files,
  proof, and traceability to requirements.

The source templates live in `templates/specs/` before installation. In a target
repository, copy them to the project-local spec location named by the ticket.
Implementation tickets link to the package with `spec_refs` and declare the
contract with `spec_contract`.

Tiny typo, formatting, or documentation-only changes may use quick flow instead
of a full spec package. The ticket must set
`spec_contract.quick_flow_exemption.used: true` and provide a concrete reason.
Readiness fails when non-trivial implementation lacks both linked specs and a
justified exemption.

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
- Child implementation tickets link to the parent spec package, a narrowed child
  spec, or an explicit quick-flow exemption.
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

Read-only reviewers can be routed through small reusable expert profiles:
`requirements`, `architecture`, `test`, `security_privacy`, `ux_visual`,
`performance_reliability`, `data_migration`, and `docs_release`. These profiles
are review lenses for the existing workflow, not a separate team model. The
manager chooses the minimum useful route from ticket risk, changed files,
unknowns, and proof gaps. Simple tickets can set no required profiles and
`max_rounds: 0`.

Every profile remains read-only. Expert reviewers may inspect files and report
bounded findings, proof requirements, and the next worker task. They may not edit
files, run migrations, install dependencies, deploy, release, use secrets, push,
perform remote operations, or widen scope. If a finding requires broader files or
unapproved actions, the manager stops, revises the ticket, or creates a new
scoped ticket instead of letting the reviewer act.

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
before or after one scoped worker. Use `expert_routing` to declare required and
optional review profiles, triggers, max rounds, escalation behavior, and where
findings are recorded.

`bounded_expert_rounds` means the manager runs a capped loop: collect proof,
ask a read-only Codex reviewer, assign one bounded worker task, run proof, then
checkpoint or record a blocker. The cap comes from `expert_routing.max_rounds`
and should be the smallest number that matches the ticket risk.

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
