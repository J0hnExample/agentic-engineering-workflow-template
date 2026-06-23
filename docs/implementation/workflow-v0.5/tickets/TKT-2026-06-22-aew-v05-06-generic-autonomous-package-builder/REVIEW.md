# Ticket 06 Review

Status: passed after repair round 1.

Independent review round 1 failed. Do not claim PASS until a fresh reviewer
inspects the repaired diff and proof.

## Round 1 Verdict

- Verdict: FAIL
- Reviewer: fresh read-only independent reviewer subagent
  `019ef347-f274-7752-8bc5-44b715762480`
- Finding 1: validators accepted manifest file entries with missing `sha256`.
- Finding 2: validators did not compare `dependency_graph.depends_on` exactly
  against the matching ticket dependencies.

## Repair Round 1

- Updated `tools/validate_autonomous_package.py` to require a non-empty string
  `sha256` for every manifest file entry.
- Updated the embedded package validator in `tools/build_autonomous_package.py`
  with the same `sha256` requirement.
- Updated both validators to compare the entire dependency graph against the
  ordered ticket list, including exact `depends_on` lists.
- Added regression tests for missing `sha256` rejection and dependency graph
  drift rejection.
- Reran the full proof: 10 unit tests passed, single and multi package fixtures
  built and validated, and missing `sha256` was rejected by both repository and
  embedded validators.

## Re-Review Verdict

- Verdict: PASS
- Reviewer: fresh read-only independent reviewer subagent
  `019ef34a-ef13-76f3-bf34-00a38d2adc76`
- Required repairs: none after repair round 1.

## Re-Review Evidence

- Canonical ticket and repository ticket copy match byte-for-byte.
- Changed paths are within the ticket allowed scope, except the pre-existing
  untracked package ZIP.
- Builder and validator imports are standard-library only.
- Unit tests passed: `Ran 10 tests`, `OK`.
- Single and multi fixtures built and validated.
- All manifest file entries have `sha256`.
- Missing `sha256` is rejected by both repository and embedded validators.
- Dependency graph drift is rejected.
- Active ticket path substitution is rejected.
- `git diff --check` passed.

## Review Checklist

- Package templates are generic and avoid project-specific product language.
- Builder uses only the Python standard library.
- Validator uses only the Python standard library.
- Manifest file declarations reject missing and undeclared files.
- Deterministic package files are SHA-256 hashed.
- Active-ticket validation requires full ID, absolute package-local path,
  manifest path match, and hash match.
- Repository ticket substitution is rejected.
- Single-ticket and multi-ticket fixtures build and validate.
- Failure tests cover mutation, missing file, duplicate ID, out-of-order
  dependency, and active-ticket path substitution.
- Documentation avoids premature release claims.
- Pre-existing package ZIP remains unstaged.
