# Spec Drift Verifier Prompt

Use after implementation proof is available and before final closeout for
non-trivial tickets. This verifier is read-only. It must not edit product code,
rewrite specs, update tickets, repair tests, or change documentation.

Read:

1. `AGENTS.md`
2. the active ticket and execution result
3. linked requirements, design, and tasks specs unless the ticket records a
   justified `spec_refs.mode: no_spec`
4. relevant delta specs, current specs, and archive records
5. changed files and diff
6. tests, logs, screenshots, or other proof artifacts named by the ticket
7. documentation changed by the ticket or documentation that should have changed

Compare requirements, design, tasks, delta-spec items, changed files, tests,
public docs, and execution-result claims. Look for implemented-but-unspecified
behavior, specified-but-unimplemented behavior, missing tests, stale
requirements, and undocumented public behavior.

Verdict rules:

- `pass`: no material drift found.
- `pass_with_risk`: only non-blocking drift or uncertainty remains, with owner
  and follow-up recorded.
- `fail`: material drift exists, required proof is missing, behavior changed
  without approval, or `execution_result.spec_alignment` is absent for a
  non-trivial ticket without a no-spec exemption.

Output required:

- verdict: `pass`, `pass_with_risk`, or `fail`
- checked_specs
- drift_findings with file references and blocking status
- required_followups, or `none`
- missing_proof
- residual_risks
- whether the ticket may proceed to final verification
