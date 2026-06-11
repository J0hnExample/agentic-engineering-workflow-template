# Agentic Engineering Workflow Template

Current version: 0.4.0

> **Codex 5.5-led setup:** do not install this workflow by hand first.
> Use Codex 5.5 as the setup and orchestration agent, let it inspect the target
> repository, and let it implement the workflow layer with a scoped setup plan.

`Agentic Engineering Workflow Template` turns an existing or new repository into
a governed SDD/context-engineering workspace for Codex 5.5. It gives Codex an
automatic spec, ticket, documentation, proof, and memory workflow so agent work
stays scoped, traceable, and reviewable.

The template is designed to reduce drift and hallucinations by forcing clear
ownership, explicit handoffs, bounded context packs, proof gates, spec drift
checks, and documentation checkpoints between every meaningful step. Specs,
tickets, notes, and agent memory files act as the working memory for the agent
system, so humans can focus on engineering decisions instead of manually
tracking what each agent did, why it did it, and what must happen next.

It is not an app, framework, service, or runtime. Use it when work needs more
structure than one chat prompt: multi-step delivery, risky refactors, UI changes
that need proof, migrations, diagnosis tasks, or handoffs between planning,
implementation, review, and final verification.

| Signal | Meaning |
| --- | --- |
| Codex 5.5 first | Use Codex 5.5 to understand, initialize, calibrate, and orchestrate the workflow. |
| SDD mode | Use specs, tickets, context packs, and proof gates to keep agent work anchored to explicit intent. |
| Ticket-driven memory | Tickets, closeouts, and `agent/*.md` files preserve context between agent steps. |
| Drift control | Scope, proof gates, role boundaries, and documentation checkpoints keep work reviewable. |
| Target-repo installed | This template stays the source; the workflow files are installed into another repo. |
| No runtime dependency | It does not add an app runtime, framework, service, or product code. |
| No project security rules | Security constraints must be added after target-context review. |

## Start Here

Choose the path that matches your repository, then ask Codex 5.5 to take over
the setup.

| If you are starting... | Do this |
| --- | --- |
| A new repository | Use this repository as a template, open the new repository in Codex 5.5, and ask Codex how the workflow works before changing product code. |
| An existing repository | Download this repository as a zip or keep it as a local package folder, place it near the target repository, open Codex 5.5 in the target repository, and give Codex both paths. |

> **Run calibration loops first:** before using this on important work, run 1-2
> small test tickets. Let Codex 5.5 help tune ticket size, allowed files, proof
> gates, stop conditions, review style, and memory closeout rules to match how
> you want agents to operate. As a best practice, remind Codex to document
> decisions, ticket handoffs, extensions, skipped checks, and memory updates
> between tickets until the workflow reliably does that in the form you expect.
>
> **Security note:** this template does not include project-specific security
> rules. It includes workflow guardrails, but security constraints for secrets,
> data handling, auth, deployment, compliance, or threat models must be added
> only after Codex has reviewed the target project's context, stack, data flows,
> deployment model, and risk profile.

## Public Release Status

Version 0.4.0 is the first SDD/context-engineering upgrade for Codex-managed
repository workflows. It is meant to be copied, reviewed, and adapted inside a
target repository before relying on it for day-to-day work.

Maturity: early practical template / pre-1.0.

The template is mature enough to describe repeatable Codex roles, scoped
tickets, spec artifacts, context packs, proof expectations, and closeout records.
It is not a guarantee that a target repository is ready to ship, and it does not
claim Spec-as-Source maturity.

## SDD Mode

SDD mode means Codex works from explicit intent before implementation. For
non-trivial changes, the manager should establish requirements, design, tasks,
and, when durable behavior changes, a delta spec before assigning scoped work.
The worker then implements against the ticket, linked specs, selected steering,
locked decisions, and bounded context pack instead of improvising from a single
chat prompt.

This template supports two levels of SDD practice:

| Mode | Use when | Required anchor |
| --- | --- | --- |
| Spec-first | New behavior, API, data, workflow, UI, security, migration, or architecture work needs explicit agreement before implementation. | Requirements, design, tasks, ticket scope, and delta spec when durable specs must change. |
| Spec-anchored | A smaller change can start from an existing ticket or current spec, but implementation still has to stay aligned with the recorded contract. | Existing current specs, ticket acceptance, context pack, locked decisions, and proof gates. |

This is different from Vibe Coding. Codex can still move quickly, but the work
is not accepted because it "looks right" in a chat. The workflow asks Codex to
name the relevant files and specs, lock grey-area decisions, state what context
is intentionally excluded, prove the result, and record whether any spec drift
or follow-up remains.

SDD artifacts in this template include:

- `specs/current/**` for durable current behavior, contracts, workflows, and
  important constraints after installation in a target repository.
- `specs/changes/<change-id>/proposal.md`, `delta-spec.md`, `design.md`, and
  `tasks.md` for proposed changes.
- `templates/specs/TEMPLATE.*.md` for requirements, design, tasks, and delta
  spec structure.
- `context_pack.required_files`, `context_pack.required_specs`,
  `context_pack.required_steering_files`, `context_pack.excluded_context`, and
  `context_pack.budget_notes` in ticket templates.
- `locked_decisions` for pre-implementation decisions that resolve grey areas.
- `templates/steering/*.md` for conditional steering that loads specialized
  guidance only when file patterns, task types, or manual selection require it.
- `expert_routing` profiles for targeted read-only review by lens, such as
  requirements, architecture, test, security/privacy, UX/visual,
  performance/reliability, data migration, or docs/release.
- `prompts/spec-drift-verifier.md` for read-only comparison of specs, tickets,
  implementation, tests, docs, and closeout.

## Quick-Flow vs Full Orchestrator

Use quick-flow only for tiny, clear, low-risk work that already has repository
discovery evidence, exact `allowed_files`, exact `forbidden_files`, concrete
Given-When-Then acceptance, proof, closeout, no-secrets handling, approval
boundaries, and a justified `spec_contract.quick_flow_exemption`.

Use a full ticket or orchestrator when the change needs more than 3 non-ticket
files, more than 1 behavior module, requirements/design/tasks specs, a delta
spec lifecycle, conditional steering conflict resolution, expert routing,
architecture decisions, dependency changes, data migration, auth, security,
privacy, unclear acceptance, unavailable proof, visual/product ambiguity, files
outside scope, or spec drift repair. For larger delivery, the orchestrator owns
the context budget, creates child tickets, routes the minimum useful read-only
experts, and keeps specs, tickets, implementation, and proof aligned.

## Upgrade Notes For Existing Targets

Existing repositories initialized from 0.3.0 should update the workflow files
intentionally instead of blindly overwriting local rules. Ask Codex to compare
the target `AGENTS.md`, `agent/*.md`, ticket templates, prompts, checklists,
steering files, and specs against this template, preserve project-specific
rules, and add the 0.4.0 concepts only where they fit the target repository.
After updating, run one small calibration ticket and one quick-flow candidate to
confirm context packs, quick-flow escalation, spec drift verification, and
closeout records are working as expected.

## Codex Quickstart

1. Put this workflow template where Codex 5.5 can read it.
2. Open Codex 5.5 in the target repository, not inside this template directory.
3. Ask Codex to explain the workflow and initialize the target repository from
   this template.
4. Give Codex the workflow template path and the target repository path.
5. Let Codex inspect the target repository before it proposes any file writes.
6. Let Codex propose the minimal setup plan, including exactly which workflow
   files it will install or update.
7. After the setup plan is clear, let Codex implement it and run the first small
   calibration ticket from `tickets/templates/TEMPLATE.ticket.yaml`.

Codex should distinguish the template source from the target repository before
copying anything. It should mark unknown values as unknown instead of inventing
them, and it should propose dependency installation before running it.

## Copy-Paste Codex Initialization Prompt

```text
You are Codex 5.5 initializing this repository for Codex-managed software work.

Workflow template source:
<path-to-workflow-template>

Target repository:
<path-to-target-repository>

Use the template prompt at:
<workflow-template-source>/prompts/initialize-repo.md

First confirm which directory is the workflow template and which directory is the
target repository. Then inspect the target repository evidence before writing
anything. Identify manifests, lockfiles, framework config, test config, build
config, pipeline files, Docker files, environment examples, scripts, and existing
docs.

Propose the minimal template-to-target copy plan for AGENTS.md, agent/*.md,
tickets/templates/*, and docs/reusable_feature_implementation_paths.md. Ask for
approval before writing files or running dependency installation. Do not invent
unknown values; mark unknowns explicitly.

Before serious work starts, recommend 1-2 small calibration loops so the user can
tune ticket size, scope rules, proof gates, stop conditions, review style, and
memory behavior. Also identify that this template does not include
project-specific security rules; propose security constraints only after
reviewing the target repository context.
```

For the full initialization prompt, use
[`prompts/initialize-repo.md`](prompts/initialize-repo.md).

## What This Template Is Not

- It is not an application runtime, service, library, or framework.
- It is not a replacement for project ownership, code review, or release
  decisions.
- It is not a guarantee that Codex output is correct without repository-specific
  proof and final verification.
- It does not provide project-specific security rules, secret handling,
  deployment, publishing, or remote management.

## What Gets Installed

This repository is the template source. The repository being initialized is the
target. Source files in this template install into different paths in the target:

| Template source | Target repository path |
| --- | --- |
| [`templates/AGENTS.md.template`](templates/AGENTS.md.template) | `AGENTS.md` |
| [`agent/*.md`](agent/) | `agent/*.md` |
| [`templates/TEMPLATE.ticket.yaml`](templates/TEMPLATE.ticket.yaml) | `tickets/templates/TEMPLATE.ticket.yaml` |
| [`templates/TEMPLATE.quick-ticket.yaml`](templates/TEMPLATE.quick-ticket.yaml) | `tickets/templates/TEMPLATE.quick-ticket.yaml` |
| [`templates/TEMPLATE.orchestrator-ticket.yaml`](templates/TEMPLATE.orchestrator-ticket.yaml) | `tickets/templates/TEMPLATE.orchestrator-ticket.yaml` |
| [`templates/TEMPLATE.execution-result.yaml`](templates/TEMPLATE.execution-result.yaml) | `tickets/templates/TEMPLATE.execution-result.yaml` |
| [`templates/TEMPLATE.reusable-feature-path.md`](templates/TEMPLATE.reusable-feature-path.md) | `docs/reusable_feature_implementation_paths.md` |

Prompts and checklists can remain in the template or be copied into the target if
that makes the repository easier to operate.

## Target Layout

After Codex installs the workflow layer, a target repository should have this
shape around its normal product code, tests, package files, docs, and scripts:

```text
.
├── AGENTS.md
├── agent/
│   ├── STATE.md
│   ├── DECISIONS.md
│   ├── KNOWN_ISSUES.md
│   ├── TODO.md
│   ├── PATHS.md
│   ├── SERVICES.md
│   └── CHANGELOG.md
├── tickets/
│   ├── templates/
│   │   ├── TEMPLATE.ticket.yaml
│   │   ├── TEMPLATE.quick-ticket.yaml
│   │   ├── TEMPLATE.orchestrator-ticket.yaml
│   │   └── TEMPLATE.execution-result.yaml
│   └── TKT-YYYY-MM-DD-example.yaml
└── docs/
    └── reusable_feature_implementation_paths.md
```

## How The Workflow Runs

- `manager-orchestrator`: a Codex 5.5 session that keeps the ticket chain in
  view, creates child tickets, assigns scoped work, reviews proof, and decides
  whether to advance, retry, checkpoint, or stop.
- `scoped worker`: a Codex worker that implements one bounded ticket inside
  explicit `allowed_files`, reports changed files and proof, and stops if scope
  needs to expand.
- `read-only reviewer`: a Codex subagent or role prompt that reviews plans,
  risks, code, tests, or architecture without editing files. Reviewer routes can
  use the `requirements`, `architecture`, `test`, `security_privacy`,
  `ux_visual`, `performance_reliability`, `data_migration`, or `docs_release`
  profile as a narrow review lens.
- `final verifier`: a Codex reviewer that checks scope, proof gates, regression
  gates, skipped checks, and agent-memory closeout before a ticket or chain is
  marked done.

All roles are Codex roles. Codex subagents inherit the installed `AGENTS.md`, the
active ticket scope, approval boundaries, forbidden actions, and verification
requirements of the main Codex session.

The execution modes are defined in the templates and docs:
`standard_worker`, `expert_supported`, `bounded_expert_rounds`, and
`research_only`.

Tickets can add `expert_routing` to declare required profiles, optional
profiles, trigger conditions, `max_rounds`, escalation behavior, and where
reviewer output is recorded. The manager chooses the minimum useful read-only
route from ticket risk and repository evidence; simple tickets can explicitly
set no required profiles and `max_rounds: 0`.

Quick-flow is available for tiny, clear, low-risk work through
[`templates/TEMPLATE.quick-ticket.yaml`](templates/TEMPLATE.quick-ticket.yaml)
and [`prompts/quick-dev.md`](prompts/quick-dev.md). It still requires repository
discovery evidence, exact `allowed_files`, `forbidden_files`, Given-When-Then
acceptance, proof, closeout, no-secrets handling, approval boundaries, and no
bulk staging. It must escalate to the full ticket or orchestrator flow if the
change needs more than 3 non-ticket files, more than 1 behavior module, an
architecture decision, dependency changes, data migration, auth/security/privacy
work, unclear acceptance, failing or unavailable proof, ambiguous visual/product
behavior, files outside scope, spec drift, delta lifecycle work, or expert
routing.

## Safety Model

The template is built around narrow scope and explicit proof:

- Codex inspects repository evidence before writing initialization files.
- Unknown values are marked as unknown instead of invented.
- Dependencies are proposed before installation and require approval.
- Tickets declare `allowed_files`, `forbidden_files`, in-scope work,
  out-of-scope work, proof gates, regression gates, stop conditions, and done
  definitions.
- Quick-flow tickets are allowed only for tiny bounded work and must escalate
  when scope or risk grows; they cannot bypass proof gates, forbidden files,
  no-secrets rules, approval boundaries, closeout, or no bulk staging.
- Implementation workers edit only assigned scope and do not use bulk staging.
- Read-only Codex reviewers may analyze but do not edit files, run migrations,
  install dependencies, deploy, release, use secrets, push, perform remote
  operations, or widen scope.
- Closeout records changed files, commands run, proof, skipped checks, blockers,
  risks, and whether `agent/*.md` needed updates.
- If no durable agent-memory update is needed, closeout records:

```text
agent memory checked: no update needed
```

These are workflow guardrails, not a complete security policy. Add security
rules only after reviewing the target repository's real context.

## Example Flow

1. Codex 5.5 initializes the target repository from this template.
2. The manager creates a small calibration ticket from
   [`templates/TEMPLATE.ticket.yaml`](templates/TEMPLATE.ticket.yaml).
3. The ticket names the goal, allowed files, forbidden files, proof gates, and
   done definition.
4. A scoped worker runs with
   [`prompts/scoped-worker.md`](prompts/scoped-worker.md), edits only the ticket
   scope, and records proof.
5. If the work is risky or blocked, the manager asks a read-only Codex reviewer
   using [`prompts/read-only-expert.md`](prompts/read-only-expert.md) and the
   smallest useful `expert_routing` profile.
6. The worker or manager records closeout using
   [`templates/TEMPLATE.execution-result.yaml`](templates/TEMPLATE.execution-result.yaml).
7. A final verifier uses
   [`prompts/final-verifier.md`](prompts/final-verifier.md) before the ticket is
   marked done.
8. Durable state, decisions, known issues, follow-up work, paths, services, or
   changelog notes are updated under `agent/`, or the no-update phrase is
   recorded.

For larger delivery, start from
[`templates/TEMPLATE.orchestrator-ticket.yaml`](templates/TEMPLATE.orchestrator-ticket.yaml)
and let the manager split the outcome into child tickets.

For tiny bounded work, start from
[`templates/TEMPLATE.quick-ticket.yaml`](templates/TEMPLATE.quick-ticket.yaml)
and use [`prompts/quick-dev.md`](prompts/quick-dev.md). Convert to a full ticket
as soon as any escalation condition is true.

## Reference

- [`docs/workflow.md`](docs/workflow.md) explains the workflow, roles, execution
  modes, ticket chains, and memory closeout.
- [`docs/reusable_feature_implementation_paths.md`](docs/reusable_feature_implementation_paths.md)
  is the template's reusable feature-path document.
- [`prompts/initialize-repo.md`](prompts/initialize-repo.md) initializes a target
  repository from this template.
- [`prompts/manager-orchestrator.md`](prompts/manager-orchestrator.md) runs a
  parent ticket chain.
- [`prompts/scoped-worker.md`](prompts/scoped-worker.md) runs one bounded
  implementation ticket.
- [`prompts/read-only-expert.md`](prompts/read-only-expert.md) supports Codex
  planning or review without file edits.
- [`prompts/final-verifier.md`](prompts/final-verifier.md) checks completion
  before done.
- [`checklists/ticket-readiness.md`](checklists/ticket-readiness.md) checks a
  ticket before product-code work starts.
- [`checklists/closeout.md`](checklists/closeout.md) checks a ticket before it is
  marked done.
- [`templates/`](templates/) contains the installable agent rules and ticket
  templates.
- [`agent/`](agent/) contains starter project-memory files for the target
  repository.
