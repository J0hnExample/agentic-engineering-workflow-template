# SDD Article Integration Evaluation

Date: 2026-06-09  
Current template version inspected: 0.3.0  
Proposed target version for the SDD upgrade: 0.4.0

## Verdict

The existing workflow is already a strong guarded agentic-engineering baseline: it has role separation, scoped tickets, fresh worker contexts, explicit proof gates, no-bulk-staging, stop conditions, and closeout memory. The most useful additions from the article are not another large agent framework, but a thin SDD layer that turns ticket context into explicit, traceable specs.

## Already covered well

- Existing expert-team pattern: `manager-orchestrator`, `scoped worker`, `read-only reviewer`, and `final verifier`, plus `expert_supported` and `bounded_expert_rounds` execution modes.
- Fresh-context execution for bounded tickets.
- Explicit allowed_files / forbidden_files.
- Proof gates, regression gates, visual gate, and closeout.
- Agent memory under `agent/*.md`.
- Approval boundaries for dependencies, secrets, destructive commands, remotes, releases, and deployments.

## High-value additions to automate

1. **Expert routing profiles**: keep the existing expert-team model, but let the manager select specific read-only reviewer profiles by ticket type, file patterns, risk, and proof needs.
2. **Spec artifact package**: add requirements/design/tasks templates so tickets do not carry all requirements alone.
3. **Delta-spec lifecycle**: keep durable specs current through ADDED/MODIFIED/REMOVED changes and archive/merge closeout.
4. **Spec drift verifier**: make final verification compare spec, code, tests, docs, and ticket result.
5. **Conditional steering**: load specialized guidance only when matching files/tasks require it, while keeping core safety rules always loaded.
6. **Quick-flow with escalation**: support tiny safe tasks without turning them into vibe coding.
7. **Decision locks + context budgets**: resolve grey areas before implementation and keep worker context small and intentional.
8. **README/version terminology update**: align public docs and VERSION with the SDD release line.

## Deliberately not recommended as default

- A second full BMAD-style simulated agile team with many personas: the workflow already has an expert-team pattern. The useful improvement is routing/specialization of the existing read-only experts, not duplicating them with ceremony.
- Proprietary IDE dependency: Kiro concepts are useful, but this template should stay portable.
- Spec-as-Source as the default maturity level: too strong for a pre-1.0 workflow; Spec-first plus Spec-anchored is the safer next step.
- Unbounded parallel implementation agents: keep the existing serial scoped-worker default unless write scopes are provably disjoint.

## Ticket set created

- `tickets/sdd-upgrade/TKT-2026-06-09-sdd-upgrade-orchestrator.yaml`
- `tickets/sdd-upgrade/TKT-2026-06-09-expert-routing-profiles.yaml`
- `tickets/sdd-upgrade/TKT-2026-06-09-spec-artifact-package.yaml`
- `tickets/sdd-upgrade/TKT-2026-06-09-delta-spec-lifecycle.yaml`
- `tickets/sdd-upgrade/TKT-2026-06-09-spec-drift-verifier.yaml`
- `tickets/sdd-upgrade/TKT-2026-06-09-conditional-steering.yaml`
- `tickets/sdd-upgrade/TKT-2026-06-09-quick-flow-escalation.yaml`
- `tickets/sdd-upgrade/TKT-2026-06-09-decision-lock-context-budget.yaml`
- `tickets/sdd-upgrade/TKT-2026-06-09-readme-terminology-version-0-4-0.yaml`

## Recommended implementation order

1. Expert routing profiles for the existing expert-team pattern.
2. Spec artifact package.
3. Delta-spec lifecycle.
4. Spec drift verifier.
5. Conditional steering.
6. Quick-flow escalation.
7. Decision locks and context budget.
8. README/version/changelog update to 0.4.0.
9. Final verification through the orchestrator ticket.
