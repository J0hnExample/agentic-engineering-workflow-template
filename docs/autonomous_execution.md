# Autonomous Execution Controller

The autonomous controller is a deterministic state machine for serial ticket
chains and single-ticket runs. It does not infer completion from ticket names,
chat history, or file presence. It advances only when the required evidence for
the next legal phase is recorded in live run state and compact repository
records.

## Run State

Live controller state belongs outside the worktree, for example:

```text
.git/agentic-workflow-controller/RUN_STATE.json
```

Repository files store templates, validators, ticket plans, execution reports,
handoffs, review notes, and delivery records. They are durable records, not the
live lock file.

The canonical run-state schema and example live in:

- `templates/runtime/RUN_STATE.schema.json`
- `templates/runtime/RUN_STATE.example.json`

Validate live state with:

```bash
python tools/validate_run_state.py .git/agentic-workflow-controller/RUN_STATE.json
```

## Legal Phases

Every ticket uses the same ordered phase list in `full_chain` and
`single_ticket` mode:

```text
pending
-> source_lock_validated
-> repository_validated
-> plan_recorded
-> repository_ticket_recorded
-> implementation_writer_locked
-> implementation_spawned
-> implementation_completed
-> writer_thread_closed
-> focused_tests_passed
-> self_review_completed
-> independent_review_spawned
-> independent_review_completed
-> repair_completed_or_not_needed
-> context_curated
-> git_delivery_started
-> explicit_paths_staged
-> committed
-> pushed
-> head_equals_upstream_proved
-> completed
```

The validator rejects skipped phases, a current phase that precedes recorded
evidence, and a completed phase list that is not the exact legal prefix.

## Source Lock Before Spawn

Before every planner, writer, reviewer, repair, curator, or delivery role is
spawned, validate the package and active ticket source lock. A failed source
lock is a hard stop. For package-backed tickets, the active ticket must be the
package-local canonical ticket file, and the repository copy must remain a
byte-for-byte copy unless the ticket explicitly authorizes otherwise.

## Writer Lock

Only one implementation writer may be open. The writer lock is acquired at
`implementation_writer_locked` and is released only after the implementation
thread is closed at `writer_thread_closed`.

Review, repair, context curation, and delivery phases are blocked until the
writer thread is closed. A later ticket cannot acquire a writer lock while an
earlier writer is still open.

## Completed Prefix

In `full_chain` mode, completed tickets must form a prefix of the ticket list.
The next ticket cannot begin planning until every previous ticket has:

- recorded commit SHA
- push proof
- `HEAD == upstream` proof
- `completed` phase

This prevents next-ticket planning from starting after a local commit or push
when upstream equality has not been proven.

## Resume Algorithm

On resume:

1. Validate the package and active-ticket source lock.
2. Validate branch, upstream configuration, and live run state.
3. Verify the completed-ticket prefix.
4. For the last completed ticket, verify recorded delivery SHA, push proof, and
   upstream equality before planning the next ticket.
5. Select the first incomplete ticket.
6. Select the first missing legal phase for that ticket.
7. If interrupted at review, resume review or repair, not implementation.
8. If interrupted after `committed`, verify the recorded SHA and continue to
   push/upstream proof instead of recommitting.
9. Stop with a blocker when repository evidence conflicts with run state.

## Repository Records

Each ticket should keep compact records:

- `PLAN.md`
- `EXECUTION_REPORT.md`
- `REVIEW.md`
- `HANDOFF.md`
- `GIT_DELIVERY.md` when delivery is assigned

These files should record commands, proof, skipped checks, risks, blockers,
repair rounds, changed files, and the exact resume state. They should not be
treated as lock files.
