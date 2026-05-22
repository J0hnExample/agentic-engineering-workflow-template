# Initialize Repository Prompt

Use this prompt immediately after cloning the workflow package or installing it
into a target repository. If this prompt is being used from a package directory
next to a target repository, first distinguish the package source from the
target repository that will receive the installed files.

You are Codex initializing this repository for agentic software work.

Start by asking the user for:

- the project goal
- the intended product type
- preferred stack, frameworks, language, package manager, and test tools
- whether dependencies should only be proposed or may be installed after
  approval
- whether Claude CLI should be included in expert rounds

Rules:

- Inspect repository evidence before writing `AGENTS.md`, `agent/*.md`,
  tickets, docs, or prompts.
- Use manifests, lockfiles, framework config, test config, build config, CI
  files, Docker files, environment examples, scripts, and existing docs.
- Do not invent unknown values. Mark unknowns explicitly.
- Do not install dependencies automatically. Propose the commands first, explain
  why they are needed, and ask for approval.
- If Claude CLI expert rounds are enabled by the user, Codex CLI may invoke
  Claude CLI for planning or review expert passes. Codex remains responsible for
  execution, verification, and ticket closeout.
- If Claude CLI expert rounds are not enabled, use Codex-only planning,
  execution, verification, and closeout.

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
5. Check whether `agent/*.md` exists and contains repo-specific evidence rather
   than placeholders.
6. Check whether ticket templates are available under `tickets/templates/*`.
7. Check whether reusable workflow docs exist under `docs/`.
8. If files are missing, propose the minimal package-to-target copy plan before
   writing anything.
9. Propose the minimal files to create or update.
10. Propose dependency, lint, test, build, and dev-server commands from repo
   evidence.
11. Ask for approval before writing files or running dependency installation.

Closeout:

- Summarize files created or updated.
- List commands run and proof collected.
- Record skipped checks with reasons.
- State whether Claude CLI expert rounds are enabled.
- Record updated `agent/*.md` files, or write:

```text
agent memory checked: no update needed
```
