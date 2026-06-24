# Initialize Repository Prompt

Use this prompt immediately after cloning the workflow package or installing it
into a target repository. If this prompt is being used from a package directory
next to a target repository, first distinguish the package source from the
target repository that will receive the installed files.

You are Codex initializing this repository for Codex-managed software work.

Start by asking the user for:

- the project goal
- the intended product type
- preferred stack, frameworks, language, package manager, and test tools
- whether dependencies should only be proposed or may be installed after
  approval
- whether Codex subagents may be used for bounded read-only review or scoped
  implementation tasks
- whether larger features should use full SDD specs, quick tickets without
  specs, or a mixed policy based on risk
- the Git delivery policy: target branch, remote/upstream, whether completed
  tickets should be committed and pushed automatically, and whether scoped
  explicit staging is required

Ask once for delivery and side-effect policy, then record it from
`templates/TEMPLATE.workflow-policy.yaml`. Include dependency installation,
external-service commands, commit/push behavior, explicit staging, generated
artifact handling, and baseline dirty-path handling. Future ticket agents should
reuse the recorded policy unless it is absent, contradictory, or unsafe.

Rules:

- Inspect repository evidence before writing `AGENTS.md`, `agent/*.md`,
  tickets, docs, or prompts.
- Use manifests, lockfiles, framework config, test config, build config, CI
  files, Docker files, environment examples, scripts, and existing docs.
- Do not invent unknown values. Mark unknowns explicitly.
- Do not install dependencies automatically. Propose the commands first, explain
  why they are needed, and ask for approval.
- Use Codex-only planning, execution, review, verification, and closeout.
- Any Codex subagent inherits `AGENTS.md`, the active ticket scope, approval
  boundaries, forbidden actions, and verification requirements.
- Do not push, deploy, release, publish, edit secrets, or widen scope unless the
  user explicitly approves the exact action.
- Record the approved Git delivery policy once from
  `templates/TEMPLATE.workflow-policy.yaml`. Future agents should not ask again
  per ticket unless the policy is absent, contradictory, or unsafe for the
  current repository state.
- Propose external tools, network-dependent setup commands, and dependency
  operations before running them.
- Keep the workflow template source and target repository distinct. Never treat
  a package source path as the target path for product changes.

Initialization work:

1. Confirm which directory is the workflow package source and which directory is
   the target repository.
2. Produce a source-to-target install map:
   - `templates/AGENTS.md.template` -> `AGENTS.md`
   - `agent/*.md` -> `agent/*.md`
   - `templates/TEMPLATE.*.yaml` -> `tickets/templates/TEMPLATE.*.yaml`
   - `templates/TEMPLATE.workflow-policy.yaml` -> the selected workflow policy
     record path
   - `docs/reusable_feature_implementation_paths.md` -> `docs/reusable_feature_implementation_paths.md`
   - optional prompts/checklists/docs -> target paths only if they will be used
3. Confirm the target layout:
   - `AGENTS.md`
   - `agent/*.md`
   - `tickets/templates/*`
   - `docs/reusable_feature_implementation_paths.md`
4. Check whether the package files are already installed in the target
   repository before proposing writes.
5. Check whether `templates/AGENTS.md.template` has been installed as
   `AGENTS.md`.
6. Check whether `agent/*.md` exists and contains repo-specific evidence rather
   than placeholders.
7. Check whether ticket templates are available under `tickets/templates/*`.
8. Check whether reusable workflow docs exist under `docs/`.
9. Check whether a Git delivery policy exists and whether it names the target
   branch, remote/upstream, commit/push behavior, explicit staging, baseline
   dirty-path handling, and prohibited operations.
10. If files are missing, propose the minimal package-to-target copy plan before
   writing anything.
11. Propose the minimal files to create or update.
12. For non-trivial features, propose the minimal useful SDD package:
    requirements, design, and tasks specs. For tiny low-risk work, record why
    no full spec is needed.
13. Propose dependency, lint, test, build, and dev-server commands from repo
   evidence.
14. Ask for approval before writing files or running dependency installation.

Closeout:

- Summarize files created or updated.
- List commands run and proof collected.
- Record skipped checks with reasons.
- State whether Codex subagents are enabled for bounded tasks.
- State the recorded Git delivery policy path, branch, remote/upstream, and
  whether commit-and-push-per-ticket is enabled.
- Record updated `agent/*.md` files, or write:

```text
agent memory checked: no update needed
```
