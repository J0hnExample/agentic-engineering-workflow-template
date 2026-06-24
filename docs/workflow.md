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
8. When delivery is assigned, run scoped Git delivery from the recorded policy
   and prove local `HEAD` equals the configured upstream.

Fresh-context execution is intentional. The ticket must carry enough context,
scope, proof requirements, and stop conditions for a new Codex session to do the
work without relying on unstated chat history.

## Quick Flow

Quick-flow is for genuinely small work, not for skipping the workflow. Create
quick tickets from `templates/TEMPLATE.quick-ticket.yaml` before installation or
`tickets/templates/TEMPLATE.quick-ticket.yaml` after installation.

A task is quick only when all quick conditions are true:

- one bounded objective
- exact affected files are known before editing
- no more than three non-ticket files need edits
- at most one bounded module, service, package, or documentation area changes
- local meaningful proof exists
- no full SDD, expert review, public contract, migration, dependency,
  security/auth/privacy, ambiguous visual flow, unclear requirement, forbidden
  path, or broad file-scope trigger applies

Escalate to a full ticket or parent orchestrator flow when any threshold is
triggered:

| Threshold | Escalate when |
| --- | --- |
| Security/auth/privacy | Auth, permissions, secrets, privacy, payments, deployment, release, remotes, or external-service behavior may change. |
| Schema/data | Schema, storage, migration, backfill, persistence compatibility, or destructive cleanup is required. |
| Dependencies | Dependencies must be added, removed, upgraded, reconfigured, or installed. |
| Multiple services/modules | More than one package, service, app, bounded module, or ownership area changes behavior. |
| Public API/shared contract | Public APIs, exported types, CLI behavior, config contracts, shared contracts, or integration boundaries change. |
| Visual flow ambiguity | UI, product copy, layout, accessibility, or visual flow is ambiguous or needs unspecified visual proof. |
| Unclear requirements | Requirements are unclear, contradictory, missing observable outcomes, or contain unresolved decisions. |
| Broad file scope | More than three non-ticket files need edits, affected files are unknown, or needed files are outside allowed scope. |

Quick-flow still requires repository discovery, focused proof, self-review,
independent review of the actual diff, execution result, context curation, Git
delivery when assigned, push when assigned, and proof that `HEAD == origin/main`
or the configured upstream before `done`.

Use `prompts/quick-dev.md` as the scoped worker prompt for a quick ticket.

## Single-Ticket Autonomous Run

Use `prompts/run-single-ticket-autonomously.md` when the user assigns one ticket
for complete autonomous execution. The runner uses the same planner -> writer ->
reviewer -> repair -> curator -> delivery shape as a package chain, with one
implementation writer.

The required state machine is:

```text
source_lock_validated
-> repository_discovered
-> plan_recorded
-> repository_ticket_recorded
-> writer_assigned
-> implementation_complete
-> focused_tests_passed
-> self_review_complete
-> independent_review_complete
-> repair_loop_complete_or_not_needed
-> context_curated
-> git_delivery_started
-> explicit_paths_staged
-> committed
-> pushed
-> head_equals_origin_main_proved
-> done
```

The runner may advance one state only when that state's evidence is recorded.
Do not assign a writer before the plan exists and the repository ticket record
is in place. Independent review must inspect the actual diff. The repair loop is
capped at three rounds. Git delivery uses explicit path staging only. `done` is
blocked until commit, push, and upstream equality proof are recorded when
delivery is assigned.

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

## Steering And Context Budgets

Steering files under `templates/steering/` are focused guidance packs. Load them
deterministically:

1. `always` steering, such as security boundaries.
2. `fileMatch` steering for the paths in scope.
3. `auto` steering discovered from repository structure or ownership signals.
4. `manual` steering named by the ticket or manager.

Conflicting steering must be reported as a decision or blocker. Do not silently
merge incompatible guidance. Tickets should also carry `locked_decisions`,
`unresolved_decisions`, `context_budget`, and `required_context` fields so
planners resolve grey areas before a writer starts and workers receive compact
verified context instead of raw transcripts.

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

`git delivery agent` stages only explicit ticket paths and required workflow
records, commits the completed ticket, pushes to the recorded branch/remote, and
records SHA equality proof. It does not edit product behavior.

All Codex roles, including subagents, inherit the installed `AGENTS.md`, active
ticket scope, approval boundaries, forbidden actions, and verification
requirements. A subagent may not push, deploy, release, publish, edit secrets,
install dependencies, widen scope, or write out-of-scope reports unless the
active ticket and user approval allow the exact action.

## Execution Modes

`quick_flow` means one tiny, low-risk, ticketed change that passes the
deterministic quick classification and still completes discovery, proof, review,
context curation, and delivery gates.

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

## Git Delivery

Repository initialization records the delivery policy once from
`templates/TEMPLATE.workflow-policy.yaml`: branch, remote/upstream,
commit-and-push-per-ticket, explicit staging, authorized workflow artifacts,
baseline dirty-path handling, and prohibited operations. Agents do not ask again
per ticket unless the policy is absent, contradictory, or unsafe.

Use `docs/git_delivery.md`, `prompts/git-delivery-agent.md`, and
`tools/workflow_git.py` for delivery. The helper is dependency-free and provides
preflight, scoped staging verification, commit, push, and upstream equality
proof.

Expected active ticket artifacts do not block delivery. Unrelated pre-existing
dirty paths are recorded once and preserved byte-for-byte; repeated warnings are
suppressed only when those paths are unchanged and non-overlapping. Previous
ticket managed dirt blocks the next ticket.

Forbidden delivery operations include bulk staging, branch switching or
creation, worktrees, stashes, force push, destructive reset, and checkout or
restore used to discard unrelated work.
