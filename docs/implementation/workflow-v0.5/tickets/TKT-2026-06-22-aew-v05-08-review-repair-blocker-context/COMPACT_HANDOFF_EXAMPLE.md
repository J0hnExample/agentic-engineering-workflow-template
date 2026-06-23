# Compact Handoff Example

Ticket: `TKT-2026-06-22-aew-v05-08-review-repair-blocker-context`

## Durable Facts

- Independent review checks actual diff, tests, evidence, ticket scope, and
  spec/workflow alignment.
- A `FAIL` review blocks done until a later repaired-diff `PASS`.
- Repair is capped at three materially different attempts and cannot weaken
  acceptance criteria or tests.
- Blocker resolution uses a minimal facts capsule with authorization,
  validation, rollback, and user-question policy.
- Context curation runs only after review `PASS` and excludes raw transcripts,
  raw logs, secrets, `.env*`, forbidden paths, and unrelated context.

## Proof Summary

- Source-lock comparison: passed.
- Focused unit test: `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_review_repair_context` passed, 8 tests.
- Full unittest discovery: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -p 'test*.py'` passed, 31 tests.
- Scoped `git diff --check`: passed.
- `find . -type d -name __pycache__ -print`: no output.
- Independent review: `PASS`.
- Repair rounds used: `0`.

## Excluded Context

Raw logs, chat transcripts, secret values, `.env*`, `.git/**`,
`node_modules/**`, `dist/**`, `build/**`, `coverage/**`, unrelated local paths,
and unrelated ticket detail are intentionally excluded.
