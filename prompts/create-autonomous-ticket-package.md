# Create Autonomous Ticket Package Prompt

Use this prompt to ask Codex to turn a software request into a source-locked
autonomous ticket package before implementation starts.

## Request

Goal:
<the desired software outcome>

Context:
<repository path, relevant docs, constraints, incidents, examples, or prior work>

Constraints:
<allowed paths, forbidden paths, commands, dependency policy, delivery policy,
security limits, and anything that must not change>

Done:
<observable acceptance criteria, proof commands, reports, and delivery state>

## Defaults

Unless the request overrides them explicitly, build a package that requires:

- strict serial autonomous execution
- repository evidence over chat memory
- a source lock for every package file and active ticket
- fresh global planning before tickets are written
- fresh ticket planning before each implementation
- exactly one implementation writer per ticket
- independent read-only review of the actual diff
- a bounded review-repair-validate loop with at most three repair rounds
- context curation into compact handoff records after every ticket
- explicit scoped staging, commit, and push only when delivery is assigned
- one ticket delivered before the next ticket starts
- no stashes, worktrees, feature branches, bulk staging, force pushes, destructive
  resets, secret access, deployments, or release actions unless the user grants
  exact approval

## Package Requirements

Create a request JSON for `tools/build_autonomous_package.py` with these fields:

- `package_id`
- `target_repository`
- `target_branch`
- `goal`
- `context`
- `constraints`
- `done`
- `tickets`

Each ticket must have a full unique ID, order, title, objective, dependencies,
allowed paths, forbidden paths, acceptance criteria, tests, evidence, stop
conditions, and delivery policy.

After building the package, run the package validator, record the package ZIP
path, manifest hash report, dependency order, and any unresolved risks. Do not
start implementation until the package validates.
