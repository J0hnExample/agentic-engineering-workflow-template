# Agentic Engineering Workflow Template

Current version: 0.3.0

`Agentic Engineering Workflow Template` is a workflow package for Codex-first
software engineering. It is not an app, framework, service, or runtime. It gives
an existing or new target repository a durable way to plan work, write scoped
tickets, run scoped Codex work, verify results, and close out project memory.
Think of it as a Codex starter for repository workflow, not product code.

Use this package when the work needs more structure than a single chat prompt:
multi-step delivery, risky refactors, UI changes that need proof, migrations,
diagnosis tasks, or handoffs between planning, implementation, review, and final
verification.

## Public Release Status

Version 0.3.0 is an early public template release for Codex-managed repository
workflows. It is meant to be copied, reviewed, and adapted inside a target
repository before relying on it for day-to-day work.

Maturity: early practical template / pre-1.0.

The template is mature enough to describe repeatable Codex roles, scoped tickets,
proof expectations, and closeout records. It is not a guarantee that a target
repository is ready to ship.

## Calibration Loop

Before serious use, run one or two small calibration loops in a non-critical
target repository. A useful pair is one documentation-only ticket and one small
code-change ticket with tests, each run from planning through final verification.
Compare the ticket scope, proof, closeout, and memory updates against the target
repository's actual work style. Tighten the copied prompts, ticket templates, and
closeout wording until Codex consistently asks before expanding scope and records
proof in the form the project owner can review.

Rules and approval boundaries are context-dependent. Adapt them for each target
repository's risk level, ownership model, release process, and review habits.

## Who It Is For

- Developers using Codex to execute changes in a real repository.
- Project owners who want repeatable tickets, proof gates, and handoff records.
- Teams that want one Codex manager/orchestrator to keep context while scoped
  Codex workers edit only assigned files.
- Review-heavy workflows where read-only Codex reviewers can inspect plans or
  results before another bounded implementation step.

This package works by copying templates and prompts into a target repository. It
does not promise automation, pipeline setup, dependency installation, issue
tracker integration, or production readiness by itself.

## What This Template Is Not

- It is not an application runtime, service, library, or framework.
- It is not a replacement for project ownership, code review, or release
  decisions.
- It is not a guarantee that Codex output is correct without repository-specific
  proof and final verification.
- It does not provide secret handling, deployment, publishing, or remote
  management.

## 5-Minute Quickstart

1. Put this workflow package next to the repository you want to initialize.
2. Open Codex in the target repository, not inside this package directory.
3. Paste the initialization prompt below and fill in the two paths.
4. Let Codex inspect the target repository before it proposes any file writes.
5. Approve the minimal copy/update plan only after Codex shows which files will
   be installed.
6. Start the first ticket from `tickets/templates/TEMPLATE.ticket.yaml`.

Codex should ask before writing files or installing dependencies. The package's
own initialization prompt also requires Codex to distinguish the package source
from the target repository before copying anything.

## Copy-Paste Codex Initialization Prompt

```text
You are Codex initializing this repository for Codex-managed software work.

Workflow package source:
<path-to-workflow-package>

Target repository:
<path-to-target-repository>

Use the package prompt at:
<workflow-package-source>/prompts/initialize-repo.md

First confirm which directory is the workflow package and which directory is the
target repository. Then inspect the target repository evidence before writing
anything. Identify manifests, lockfiles, framework config, test config, build
config, pipeline files, Docker files, environment examples, scripts, and existing
docs.

Propose the minimal package-to-target copy plan for AGENTS.md, agent/*.md,
tickets/templates/*, and docs/reusable_feature_implementation_paths.md. Ask for
approval before writing files or running dependency installation. Do not invent
unknown values; mark unknowns explicitly.
```

For the full version, use [`prompts/initialize-repo.md`](prompts/initialize-repo.md).

## Package vs Target Paths

This repository is the package source. The repository being initialized is the
target. Source files in this package install into different paths in the target:

| Package source | Target repository path |
| --- | --- |
| [`templates/AGENTS.md.template`](templates/AGENTS.md.template) | `AGENTS.md` |
| [`agent/*.md`](agent/) | `agent/*.md` |
| [`templates/TEMPLATE.ticket.yaml`](templates/TEMPLATE.ticket.yaml) | `tickets/templates/TEMPLATE.ticket.yaml` |
| [`templates/TEMPLATE.orchestrator-ticket.yaml`](templates/TEMPLATE.orchestrator-ticket.yaml) | `tickets/templates/TEMPLATE.orchestrator-ticket.yaml` |
| [`templates/TEMPLATE.execution-result.yaml`](templates/TEMPLATE.execution-result.yaml) | `tickets/templates/TEMPLATE.execution-result.yaml` |
| [`templates/TEMPLATE.reusable-feature-path.md`](templates/TEMPLATE.reusable-feature-path.md) | `docs/reusable_feature_implementation_paths.md` |

Prompts and checklists can remain in the package or be copied into the target if
that makes the repository easier to operate.

## Target Layout

After installation, a target repository should have this workflow layer:

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
│   │   ├── TEMPLATE.orchestrator-ticket.yaml
│   │   └── TEMPLATE.execution-result.yaml
│   └── TKT-YYYY-MM-DD-example.yaml
└── docs/
    └── reusable_feature_implementation_paths.md
```

The target repository still owns its normal product code, tests, package files,
docs, and scripts. This package adds the agent workflow layer around that work.

## Workflow Roles

- `manager-orchestrator`: keeps the ticket chain in view, creates child
  tickets, assigns scoped work, reviews proof, and decides whether to advance,
  retry, checkpoint, or stop.
- `scoped worker`: a Codex worker that implements one bounded ticket inside explicit
  `allowed_files`, reports changed files and proof, and stops if scope needs to
  expand.
- `read-only reviewer`: a Codex subagent or role prompt that reviews plans,
  risks, code, tests, or architecture without editing files.
- `final verifier`: a Codex reviewer that checks scope, proof gates, regression
  gates, skipped checks, and agent-memory closeout before a ticket or chain is
  marked done.

All roles are Codex roles. Codex subagents inherit the installed `AGENTS.md`, the
active ticket scope, approval boundaries, forbidden actions, and verification
requirements of the main Codex session.

The execution modes are defined in the templates and docs:
`standard_worker`, `expert_supported`, `bounded_expert_rounds`, and
`research_only`.

## Safety Model

The package is built around narrow scope and explicit proof:

- Codex inspects repository evidence before writing initialization files.
- Unknown values are marked as unknown instead of invented.
- Dependencies are proposed before installation and require approval.
- Secrets, credentials, local secret files, destructive commands, scope expansion,
  pushes, releases, deployments, publishing, and remote modifications require
  explicit approval for the exact action.
- Tickets declare `allowed_files`, `forbidden_files`, in-scope work,
  out-of-scope work, proof gates, regression gates, stop conditions, and done
  definitions.
- Implementation workers edit only assigned scope and do not use bulk staging.
- Read-only Codex reviewers may analyze but do not edit files.
- Closeout records changed files, commands run, proof, skipped checks, blockers,
  risks, and whether `agent/*.md` needed updates.
- If no durable agent-memory update is needed, closeout records:

```text
agent memory checked: no update needed
```

## Example Flow

1. The manager creates a ticket from
   [`templates/TEMPLATE.ticket.yaml`](templates/TEMPLATE.ticket.yaml).
2. The ticket names the goal, allowed files, forbidden files, proof gates, and
   done definition.
3. A scoped worker runs with
   [`prompts/scoped-worker.md`](prompts/scoped-worker.md), edits only the ticket
   scope, and records proof.
4. If the work is risky or blocked, the manager asks a read-only Codex reviewer using
   [`prompts/read-only-expert.md`](prompts/read-only-expert.md).
5. The worker or manager records closeout using
   [`templates/TEMPLATE.execution-result.yaml`](templates/TEMPLATE.execution-result.yaml).
6. A final verifier uses
   [`prompts/final-verifier.md`](prompts/final-verifier.md) before the ticket is
   marked done.
7. Durable state, decisions, known issues, follow-up work, paths, services, or
   changelog notes are updated under `agent/`, or the no-update phrase is
   recorded.

For larger delivery, start from
[`templates/TEMPLATE.orchestrator-ticket.yaml`](templates/TEMPLATE.orchestrator-ticket.yaml)
and let the manager split the outcome into child tickets.

## Docs, Prompts, Templates, And Checklists

- [`docs/workflow.md`](docs/workflow.md) explains the workflow, roles, execution
  modes, ticket chains, and memory closeout.
- [`docs/reusable_feature_implementation_paths.md`](docs/reusable_feature_implementation_paths.md)
  is the package's reusable feature-path document.
- [`prompts/initialize-repo.md`](prompts/initialize-repo.md) initializes a target
  repository from this package.
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
