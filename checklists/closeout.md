# Closeout Checklist

Use before marking a ticket `done`.

- [ ] All changed files are inside allowed scope.
- [ ] No forbidden files changed.
- [ ] No unrelated user changes were reverted.
- [ ] Full-SDD spec traceability was updated, or the ticket records why no spec
  update was required.
- [ ] Requirement -> design -> task -> ticket -> proof links are present when
  full SDD mode is used.
- [ ] No secrets, credentials, `.env*`, or private local paths were changed.
- [ ] No dependencies were installed, upgraded, or removed without explicit approval.
- [ ] No destructive cleanup, reset, migration with side effects, or persistent external-service action ran without explicit approval.
- [ ] No push, force-push, release, deploy, publish, or remote modification was performed without explicit approval.
- [ ] Formatter/lint check passed or skip reason is recorded.
- [ ] Typecheck passed or skip reason is recorded.
- [ ] Targeted tests passed or skip reason is recorded.
- [ ] Changed `.codex/**/*.toml` files parse and custom-agent names are unique.
- [ ] Read-only native profiles are configured with `sandbox_mode = "read-only"`.
- [ ] Exactly one implementation-writer profile exists when native profiles are
  changed.
- [ ] Durable native profiles do not pin current model names.
- [ ] Build passed when relevant or skip reason is recorded.
- [ ] Browser/UI proof was collected when user-facing UI changed.
- [ ] Screenshots/recordings were captured when visual gate required them.
- [ ] Temporary logs, debug UI, fixtures, and probes were removed or gated.
- [ ] `agent/STATE.md` was checked and updated if current state changed.
- [ ] `agent/DECISIONS.md` was checked and updated if a durable decision was made.
- [ ] `agent/KNOWN_ISSUES.md` was checked and updated if a repeatable hazard remains.
- [ ] `agent/TODO.md` was checked and updated if follow-up work remains.
- [ ] `agent/PATHS.md` was checked and updated if important paths, commands, routes, or artifacts changed.
- [ ] `agent/SERVICES.md` was checked and updated if external service or environment assumptions changed.
- [ ] `agent/CHANGELOG.md` was checked and updated if the project keeps local changelog notes.
- [ ] Ticket result records updated `agent` files or `agent memory checked: no update needed`.
- [ ] Ticket contains changed files.
- [ ] Ticket contains commands run.
- [ ] Ticket contains proof.
- [ ] Ticket contains skipped checks.
- [ ] Ticket contains blockers and risks.
- [ ] Ticket states whether a human smoke test is useful.
- [ ] Ticket states the exact next recommended step.
- [ ] Commit, if any, stages only scoped paths.
