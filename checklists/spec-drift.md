# Spec Drift Checklist

Use before final verification for non-trivial tickets unless
`spec_contract.quick_flow_exemption.used: true` is justified in the ticket.

- [ ] The verifier stayed read-only and did not repair code, rewrite specs,
      update docs, or change ticket fields.
- [ ] Requirements acceptance criteria were compared with the implemented diff
      and proof.
- [ ] Design constraints were compared with changed files, interfaces, data
      flow, failure modes, and security/privacy notes.
- [ ] Tasks were compared with completed work, skipped work, and
      `execution_result`.
- [ ] Delta-spec `ADDED`, `MODIFIED`, and `REMOVED` items were checked when a
      delta spec was in scope.
- [ ] Current spec updates, archives, or explicit deferrals were checked when
      durable behavior changed.
- [ ] Implemented-but-unspecified behavior was checked.
- [ ] Specified-but-unimplemented behavior was checked.
- [ ] Tests-missing-for-acceptance criteria were checked.
- [ ] Docs-outdated risk was checked.
- [ ] Changed behavior not approved by ticket/specs/decisions was checked.
- [ ] Drift findings list concrete file references and mark blocking versus
      non-blocking impact.
- [ ] Required follow-ups are separate scoped repair/spec/test/doc tickets, not
      auto-repairs by the verifier.
- [ ] `execution_result.spec_alignment.verdict` is `pass`, `pass_with_risk`,
      or `fail`.
- [ ] `execution_result.spec_alignment.checked_specs`,
      `drift_findings`, and `required_followups` are complete.
