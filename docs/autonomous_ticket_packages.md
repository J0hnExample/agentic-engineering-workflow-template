# Autonomous Ticket Packages

Autonomous ticket packages are source-locked bundles for serial Codex execution
in a target software repository. They turn a goal, context, constraints, done
definition, and ticket list into a package directory plus ZIP with manifests,
hashes, policies, role instructions, ticket files, reports, runtime state, and
validators.

The package directory is the source of truth for packaged ticket files. The
software repository being changed is the target repository. Copying a ticket
into the target can create a local execution record, but active-ticket source
lock validation must still compare against the package-local canonical ticket
and reject repository-local substitution.

## Build A Package

Create a JSON request with:

- `package_id`
- `target_repository`
- `target_branch`
- `goal`
- `context`
- `constraints`
- `done`
- `tickets`

Each ticket needs a full ID such as `TKT-2026-01-01-example`, a zero-based
`order`, title, objective, dependency list, scoped paths, proof gates, and
delivery policy.

Run:

```text
python tools/build_autonomous_package.py --request request.json --output-dir /tmp/example-package
```

The builder creates `/tmp/example-package` and `/tmp/example-package.zip` unless
`--zip` supplies a different ZIP path. It uses only the Python standard library.
Generated ZIPs and package output are build artifacts. Do not stage them by
default unless the active delivery policy explicitly includes them.

## Validate A Package

Run:

```text
python tools/validate_autonomous_package.py /absolute/package/root
```

For an active ticket, validate the full ticket ID and absolute package-local
ticket file:

```text
python tools/validate_autonomous_package.py /absolute/package/root \
  --active-ticket-id TKT-2026-01-01-example \
  --active-ticket-file /absolute/package/root/tickets/TKT-2026-01-01-example.yaml
```

The validator rejects relative package roots, missing manifests, missing
declared files, undeclared files, hash mismatches, duplicate ticket IDs, short
ticket IDs, missing or later dependencies, dependency graph order drift, active
ticket paths outside the package root, and repository-local ticket substitution.

Run active-ticket validation before every planner, writer, reviewer, repair,
context curator, blocker resolver, and delivery role. A mismatch is a hard stop,
not a warning to repair by editing the repository copy.

## Generic Execution Defaults

Generated packages default to:

- strict serial ticket execution
- repository evidence over chat memory
- fresh global planning and fresh ticket planning
- exactly one implementation writer per ticket
- independent read-only review of the actual diff
- bounded repair without acceptance weakening
- context curation after every ticket
- scoped commit and push only when assigned
- per-ticket delivery before the next ticket starts

Use `prompts/create-autonomous-ticket-package.md` to create a package request and
`prompts/generic-autonomous-software-request.md` as the reusable software request
shape.
