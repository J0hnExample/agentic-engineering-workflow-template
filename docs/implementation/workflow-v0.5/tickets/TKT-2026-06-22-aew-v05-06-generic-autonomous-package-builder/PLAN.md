# Ticket 06 Plan

## Source And Baseline

- Ticket: `TKT-2026-06-22-aew-v05-06-generic-autonomous-package-builder`
- Canonical source: `/tmp/aew-v0.5-package/agentic-engineering-workflow-v0.5-autonomous-upgrade/tickets/TKT-2026-06-22-aew-v05-06-generic-autonomous-package-builder.yaml`
- Repository ticket copy: `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-06-generic-autonomous-package-builder.yaml`
- Source-lock validation: passed before planning.
- Repository ticket copy proof: `cmp` passed against the canonical package ticket.
- Start branch: `main`
- Start commit: `32a305a867ace26abed0d8fe97e80f7f05f61afd`, matching `origin/main`.
- Pre-existing untracked artifact excluded from delivery: `tickets/Agentic_Engineering_Workflow_V0.5_Autonomous_Multiagent_Upgrade.zip`

## Accepted Plan

Add a generic, dependency-free autonomous ticket-package builder and validator so the source-locked package pattern can be reused for arbitrary software requests. The generated package must be generic, hash-validated, source-locked, serial, and capable of representing either one ticket or a multi-ticket chain.

## Implementation Scope

Allowed implementation paths are limited to the canonical ticket scope:

- `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-06-generic-autonomous-package-builder.yaml`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-06-generic-autonomous-package-builder/**`
- `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md`
- `agent/**`
- `prompts/create-autonomous-ticket-package.md`
- `prompts/generic-autonomous-software-request.md`
- `templates/autonomous-package/**`
- `tools/build_autonomous_package.py`
- `tools/validate_autonomous_package.py`
- `tests/**`
- `docs/autonomous_ticket_packages.md`
- `README.md`

Forbidden paths remain `.env`, `.env.*`, `**/secrets/**`, `node_modules/**`, `dist/**`, `build/**`, `coverage/**`, and `.git/**`.

## Planned Design

### Generic Package Skeleton

Create `templates/autonomous-package/` with generic template files for:

- package entry point and request record,
- manifest template,
- orchestration contract,
- agent roles for orchestrator, global planner, ticket planner, one implementer, independent reviewer, context curator, Git delivery, and blocker resolver,
- source-lock, serial execution, Git delivery, test/evidence, and context/handoff policies,
- runtime run-state and logs,
- ticket template,
- plan, execution report, review, handoff, and Git delivery report templates,
- package-local validator templates.

Do not copy project-specific or RL-specific language into generic fixtures or templates.

### Builder

Add `tools/build_autonomous_package.py` using only the Python standard library.

Expected CLI:

```text
python tools/build_autonomous_package.py --request <request.json> --output-dir <directory>
python tools/build_autonomous_package.py --request <request.json> --zip <zip-path>
```

The builder should:

- read a request containing `package_id`, `target_repository`, `target_branch`, `goal`, `context`, `constraints`, `done`, and one or more tickets,
- emit exactly one package directory and one ZIP,
- render generic skeleton files plus ticket YAML files,
- build `manifest.json` with ordered `tickets`, `read_order`, `files`, `dependency_graph`, and SHA-256 hashes for package files,
- write a validation report that includes manifest hash and file/dependency summary,
- support both single-ticket and multi-ticket requests.

### Validator

Add `tools/validate_autonomous_package.py` using only the Python standard library.

Expected CLI:

```text
python tools/validate_autonomous_package.py <absolute-package-root>
python tools/validate_autonomous_package.py <absolute-package-root> --active-ticket-id <full-id> --active-ticket-file <absolute-package-ticket>
```

The validator must reject:

- missing declared files,
- mutation of hashed files,
- undeclared package files,
- duplicate ticket IDs,
- short/non-full active ticket IDs,
- missing dependencies,
- out-of-order dependencies,
- active ticket paths outside the package root,
- repository-local ticket substitution, even when basename or ID matches.

### Tests

Add stdlib `unittest` coverage under `tests/**`:

- build and validate a single-ticket fixture,
- build and validate a multi-ticket fixture,
- mutate a hashed file and assert failure,
- remove a declared file and assert failure,
- duplicate a ticket ID and assert failure,
- create an out-of-order dependency and assert failure,
- pass a repository ticket path with matching basename/ID and assert source-substitution failure,
- assert generated fixture text has no known project-specific language.

## Planned Artifact Records

Create:

- `EXECUTION_REPORT.md`
- `REVIEW.md`
- `HANDOFF.md`
- `GIT_DELIVERY.md`

Update:

- `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md`
- `agent/CHANGELOG.md`
- `agent/PATHS.md`
- `README.md`
- `docs/autonomous_ticket_packages.md`

## Required Proof

- Active ticket source-lock validation.
- `cmp` between canonical package ticket and repository ticket copy.
- `python -m unittest discover -s tests -p 'test*.py'`.
- Builder and validator `--help` commands.
- Build/validate single-ticket fixture.
- Build/validate multi-ticket fixture.
- Mutation, missing file, duplicate ID, out-of-order dependency, and ticket-path substitution failures covered by tests.
- Generated fixture ZIP path and manifest/hash report recorded.
- `git diff --check` on scoped paths.
- Independent reviewer PASS before delivery.
- Delivery proof after commit and push: `HEAD == origin/main`.

## Review Focus

The independent reviewer must verify the package is generic, the builder has no third-party dependencies, manifests are deterministic and hash all package files, the dependency graph is ordered, active-ticket validation uses full ID plus absolute package path plus hash, repository ticket substitution is rejected, single and multi-ticket fixtures both work, docs avoid premature v0.5 release claims, and the pre-existing ZIP remains unstaged.
