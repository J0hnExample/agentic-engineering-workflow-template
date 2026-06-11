# Codex Workflow

This template supports Codex-first planning, execution, verification, and
memory closeout for a target repository.

## Basic Workflow

1. Plan one bounded step from current repository evidence.
2. For non-trivial work, create or update compact spec artifacts for
   requirements, design, and tasks. For significant behavior, API, data, or
   workflow changes, also create a delta spec under `specs/changes/<change-id>/`
   or record why the lifecycle does not apply. For tiny quick-flow work, record
   the exemption reason in the ticket.
3. Create a ticket from the installed target template
   `tickets/templates/TEMPLATE.ticket.yaml`, or for tiny bounded work from
   `tickets/templates/TEMPLATE.quick-ticket.yaml`.
4. Build the ticket context pack from `AGENTS.md`, selected steering files,
   linked specs, linked docs, and allowed files.
5. Identify implementation grey areas and resolve them through user input,
   specs, or locked decisions before planning implementation. If they cannot be
   resolved inside scope, create a `research_only` blocker ticket.
6. Start a fresh context for ticket execution.
7. Execute only the ticket scope.
8. Run the ticket proof gates.
9. Close out with the installed target template
   `tickets/templates/TEMPLATE.execution-result.yaml`.
10. Update `agent/*.md`, or record `agent memory checked: no update needed`.

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
- `delta-spec.md` captures durable spec changes in `ADDED`, `MODIFIED`, and
  `REMOVED` sections so implementation can be checked against the intended
  lifecycle update.

The source templates live in `templates/specs/` before installation. In a target
repository, copy them to the project-local spec location named by the ticket.
Implementation tickets link to the package with `spec_refs` and declare the
contract with `spec_contract`.

For ongoing maintenance, use this target repository layout:

- `specs/current/**` contains the durable current specs for implemented
  behavior, contracts, workflows, and important constraints.
- `specs/changes/<change-id>/proposal.md` explains the change intent and
  scope.
- `specs/changes/<change-id>/delta-spec.md` records `ADDED`, `MODIFIED`, and
  `REMOVED` updates against `specs/current/**`.
- `specs/changes/<change-id>/design.md` and `tasks.md` hold the implementation
  plan when the change is non-trivial.
- `specs/archive/<date>-<change-id>/**` stores accepted or closed delta-spec
  packages after closeout.

At closeout, significant changes must either merge the delta into
`specs/current/**` and archive the change package, or record a deferred spec
update blocker in the ticket result. Parallel tickets that touch the same
current spec path or requirement ID must stop and reconcile before either ticket
archives its delta.

See `docs/spec_lifecycle.md` for the propose/apply/archive lifecycle.

Tiny typo, formatting, narrow tests, or documentation-only changes may use
quick-flow instead of a full spec package. The quick ticket must set
`spec_contract.quick_flow_exemption.used: true` and provide a concrete reason.
It must still include discovery evidence, concrete file paths, forbidden files,
Given-When-Then acceptance, proof commands or manual proof, escalation
conditions, and a complete `execution_result`. Readiness fails when non-trivial
implementation lacks both linked specs and a justified exemption.

## Quick-Flow

Quick-flow is a ticketed path for tiny, clear, low-risk work. It exists to avoid
full requirements/design/tasks ceremony when current repository evidence already
shows the change is small and directly verifiable.

Use quick-flow only when all of these are true:

- The objective is one bounded outcome.
- Discovery can name the exact current files and patterns involved.
- The change stays within explicit `allowed_files` and avoids all
  `forbidden_files`.
- Acceptance can be written as concrete Given-When-Then cases.
- Proof is available, local, and meaningful.
- No durable spec, API, data, workflow, release, security, or architecture
  decision is required.

Quick-flow must not bypass proof gates, forbidden files, no-secrets rules,
approval boundaries, no bulk staging, conditional steering, delta lifecycle
rules, spec drift checks, expert routing, or ticket closeout. It still records
changed files, commands run, proof, skipped checks, blockers, risks, and the
agent-memory update check.

Escalate from quick-flow to a full ticket or parent orchestrator flow before
implementation continues when any threshold is met:

- More than 3 non-ticket files need edits.
- More than 1 package, service, app, or bounded module needs behavior changes.
- The change requires an architecture decision or alters a shared contract.
- Dependencies must be added, removed, upgraded, or reconfigured.
- Schema, storage, data migration, backfill, or destructive cleanup is needed.
- Auth, security, permissions, secrets, privacy, payments, deployment, release,
  remotes, or external-service behavior may change.
- Acceptance is unclear, contradictory, or lacks observable outcomes.
- Proof is unavailable, flaky, network-dependent without approval, or fails for
  unclear reasons.
- User-facing UI, product copy, layout, accessibility, or visual behavior is
  ambiguous or needs visual proof that is not already specified.
- Required files are outside `allowed_files` or match `forbidden_files`.
- Spec drift, conditional steering conflicts, delta lifecycle work, or expert
  routing is discovered.

When escalation triggers, stop implementation, record the trigger in
`execution_result.blockers`, and convert to the full SDD ticket or orchestrator
flow. The discovery evidence collected by quick-flow should become context for
the new ticket.

## Conditional Steering

Steering files are optional Markdown files with YAML front matter under
`steering/` in an installed target repository. The workflow package provides
starter templates under `templates/steering/`. Steering keeps specialized rules
available without loading every domain note into every worker context.

Supported inclusion modes are:

- `always`: load for every ticket. Use this sparingly for core safety,
  security, privacy, or repository-wide rules.
- `fileMatch`: load when the ticket's `allowed_files` match the steering
  `inclusion.fileMatch` patterns.
- `manual`: load only when the user, manager, ticket, spec, or prompt names the
  steering file.
- `auto`: load when the steering `inclusion.description` clearly matches the
  requested task, changed-file domain, or proof risk.

Tickets can make selection explicit with:

- `context_pack.required_files`: exact repository files the worker must read.
- `context_pack.required_specs`: specs the worker must read, or an explicitly
  empty list for a justified quick-flow exemption.
- `context_pack.required_steering_files`: steering files that must be read for
  the ticket.
- `context_pack.excluded_context`: relevant-looking context intentionally left
  out because it is noisy, stale, unsafe, or outside scope.
- `context_pack.budget_notes`: the context budget and stop rule for loading
  more context.

Always-loaded steering is read before specialized steering. `fileMatch` steering
is selected from the ticket's `allowed_files`. `manual` and `auto` steering must
stay bounded to explicit references or clear task-description matches. Do not
put secrets, private local paths, machine-specific notes, or invented product
facts into steering files. Unknowns should remain marked as unknown until
confirmed by repository evidence or user input.

## Grey Areas And Decision Locks

Before implementation planning, the manager records `context.grey_areas.status`
as `none`, `resolved`, or `blocked`. Grey areas are decisions that would make a
worker guess about behavior, scope, ownership, safety boundaries, proof, or
which context is authoritative.

Resolved grey areas are captured in ticket-local `locked_decisions` entries.
Each entry includes `decision`, `rationale`, `owner`, `source`, and
`expiry/change rule`. Use `agent/DECISIONS.md` only for durable decisions that
future tickets must inherit; do not use it for one-off closeout notes.

If a grey area cannot be resolved from current repository evidence, specs,
existing durable decisions, or user input, stop and create or update a
`research_only` blocker ticket. Implementation workers stop when a required
decision or context-pack item is missing, when `context.grey_areas.status` is
`blocked`, or when the requested context exceeds `context_pack.budget_notes`.

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
- Child tickets that materially change durable behavior should link to the
  relevant `specs/changes/<change-id>/delta-spec.md` and identify any
  `specs/current/**` files they intend to update.
- Child quick-flow tickets may use
  `tickets/templates/TEMPLATE.quick-ticket.yaml` only when they satisfy the
  quick-flow rules and escalation thresholds above.
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
