# Spec Drift Verifier Prompt

Use after implementation proof is available and before final closeout for
non-trivial tickets. This verifier is read-only. It must not edit product code,
rewrite specs, update tickets, repair tests, or change documentation. Material
findings require a separate scoped repair ticket with its own allowed files and
approval boundaries.

You inherit `AGENTS.md`, the active ticket scope, approval boundaries,
forbidden actions, `spec_refs`, `spec_contract`, delta-spec lifecycle rules, and
expert routing constraints.

Read:

1. `AGENTS.md`
2. active ticket and `execution_result`
3. linked requirements, design, and tasks specs unless the ticket records a
   justified `spec_contract.quick_flow_exemption`
4. relevant `specs/changes/**/delta-spec.md`, `specs/current/**`, and
   `specs/archive/**` artifacts when the ticket changes durable behavior,
   contracts, workflows, data, APIs, or documentation
5. changed files and diff
6. tests, logs, screenshots, or other proof artifacts named by the ticket
7. documentation changed by the ticket or documentation that should have changed

Compare:

- requirements acceptance criteria against implemented behavior and proof
- design constraints against changed files, interfaces, data flow, and failure
  handling
- tasks against completed work and skipped work
- delta-spec `ADDED`, `MODIFIED`, and `REMOVED` items against implementation,
  current-spec updates, archives, and recorded deferrals
- changed code and tests against approved scope
- changed or affected docs against changed behavior
- `execution_result` claims against the actual diff and proof

Required questions:

- Was anything implemented that is not specified or approved by the ticket,
  linked specs, delta spec, or recorded decision?
- Was anything specified but not implemented, tested, documented, or explicitly
  deferred?
- Are tests or proof missing for any acceptance criteria, changed behavior,
  failure mode, or regression gate?
- Are docs, templates, prompts, checklists, or agent memory now outdated because
  behavior changed?
- Did changed behavior lack approval through ticket scope, `spec_refs`,
  `spec_contract`, delta lifecycle, or expert routing?

Verdict rules:

- `pass`: no material drift found, and all relevant specs, implementation,
  tests, docs, and `execution_result` are aligned.
- `pass_with_risk`: only non-blocking drift or uncertainty remains, with clear
  risk notes and required follow-up recorded.
- `fail`: material drift exists, required proof is missing, behavior changed
  without approval, or `execution_result.spec_alignment` is absent for a
  non-trivial ticket without a documented quick-flow exemption.

Output required:

- verdict: `pass`, `pass_with_risk`, or `fail`
- checked_specs: list of requirements, design, tasks, delta specs, current
  specs, docs, and ticket/result artifacts checked, or the exemption reason
- drift_findings: list of concrete findings with file references and whether
  each is blocking
- required_followups: list of separate repair/spec/test/doc tickets required,
  or `none`
- missing proof
- residual risks
- whether the ticket may proceed to final verification
