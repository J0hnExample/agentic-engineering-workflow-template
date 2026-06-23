# Review And Repair Fixture

## PASS Fixture

- Ticket scope: `prompts/**`, `templates/**`, `checklists/**`, `docs/**`,
  `agent/**`, and `tests/**` as allowed by the active ticket.
- Diff inspected: actual changed files and tests.
- Evidence inspected: focused unit test, full unittest discovery, source-lock
  comparison, and diff whitespace check.
- Verdict: `PASS` is allowed only when scope, acceptance criteria, tests, and
  evidence align.

## FAIL Fixture

Finding:

- Finding id: `RR-001`
- Severity: blocking
- File or path: `templates/TEMPLATE.ticket-review.md`
- Expected: `FAIL` review blocks done until a later repaired-diff `PASS`.
- Actual: review record allows done after `FAIL`.
- Failed criterion: reviewer failure cannot be marked done without later PASS.
- Reproduction or evidence: inspect the review template closeout gate.
- Required repair: add the later-PASS gate and rerun independent review.

## Repair Cap Fixture

- Maximum attempts: `3`
- Attempts must be materially different and must not weaken acceptance criteria,
  proof gates, or tests.
- Attempts 1-3 may return to independent review.
- Attempt 4 is not allowed as silent repair; create
  `TEMPLATE.blocker-capsule.md` content and request blocker resolution.
