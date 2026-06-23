# Review, Repair, Blocker, And Context Checklist

Use before a ticket enters delivery or is marked done.

- [ ] Independent reviewer inspected the actual diff, changed files, tests,
      evidence, ticket scope, and spec/workflow alignment.
- [ ] A `FAIL` review produced bounded reproducible findings with expected,
      actual, failed criterion, reproduction, and required repair.
- [ ] The ticket is not marked done after `FAIL` without a later independent
      reviewer `PASS`.
- [ ] Repair used a fresh writer or fresh repair task and then returned to
      independent review.
- [ ] Repair did not weaken acceptance criteria, proof gates, or tests.
- [ ] Repair attempts are capped at three materially different attempts.
- [ ] After the repair cap, a blocker capsule is created instead of silently
      completing.
- [ ] The blocker resolver received a minimal facts capsule, not raw transcript
      or full log dumps.
- [ ] The blocker decision includes classification, confidence, authorization,
      action, validation, rollback, and a user question only when required.
- [ ] Preapproved actions stay inside ticket scope and accepted plan boundaries.
- [ ] User-required actions include secrets, `.env*`, production/deploy/release,
      external side effects, destructive cleanup, force push/history rewrite,
      irreversible migration, unapproved dependency changes, and irreducible
      product or policy decisions.
- [ ] Context curation ran only after independent review `PASS`.
- [ ] Curated context contains durable ticket, handoff, decision, proof, risk,
      follow-up, and next-action facts only.
- [ ] Curated context excludes raw logs, raw transcripts, secrets, `.env*`,
      forbidden paths, unrelated local paths, speculation, and unrelated
      context.
