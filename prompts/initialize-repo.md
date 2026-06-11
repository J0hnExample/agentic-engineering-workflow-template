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

Rules:

- Inspect repository evidence before writing `AGENTS.md`, `agent/*.md`,
  tickets, docs, or prompts.
- Use manifests, lockfiles, framework config, test config, build config, CI
  files, Docker files, environment examples, scripts, and existing docs.
- Do not invent unknown values. Mark unknowns explicitly.
- Generate starter `steering/*.md` files only from repository evidence and
  template-neutral placeholders. Do not use product-specific fake values,
  private paths, secret names with values, or machine-local notes.
- Do not install dependencies automatically. Propose the commands first, explain
  why they are needed, and ask for approval.
- Use Codex-only planning, execution, review, verification, and closeout.
- Any Codex subagent inherits `AGENTS.md`, the active ticket scope, approval
  boundaries, forbidden actions, and verification requirements.
- Do not push, deploy, release, publish, edit secrets, or widen scope unless the
  user explicitly approves the exact action.
- Propose external tools, network-dependent setup commands, and dependency
  operations before running them.

Initialization work:

1. Confirm which directory is the workflow package source and which directory is
   the target repository.
2. Confirm the target layout:
   - `AGENTS.md`
   - `agent/*.md`
   - `tickets/templates/*`
   - `docs/reusable_feature_implementation_paths.md`
3. Check whether the package files are already installed in the target
   repository before proposing writes.
4. Check whether `templates/AGENTS.md.template` has been installed as
   `AGENTS.md`.
5. Check whether starter steering templates are installed under `steering/` and
   whether their YAML front matter uses only supported inclusion modes:
   `always`, `fileMatch`, `manual`, and `auto`.
6. Check whether `agent/*.md` exists and contains repo-specific evidence rather
   than placeholders.
7. Check whether ticket templates are available under `tickets/templates/*`.
8. Check whether reusable workflow docs exist under `docs/`.
9. If files are missing, propose the minimal package-to-target copy plan before
   writing anything.
10. Propose the minimal files to create or update.
11. Propose dependency, lint, test, build, and dev-server commands from repo
   evidence.
12. Ask for approval before writing files or running dependency installation.

Closeout:

- Summarize files created or updated.
- List commands run and proof collected.
- Record skipped checks with reasons.
- State whether Codex subagents are enabled for bounded tasks.
- Record updated `agent/*.md` files, or write:

```text
agent memory checked: no update needed
```
