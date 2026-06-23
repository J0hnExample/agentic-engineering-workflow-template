# Ticket Readiness Checklist

Use before product-code work starts.

- [ ] Ticket has `schema_version`.
- [ ] Ticket has `ticket.id`, `title`, `repo`, `branch`, `status`, and
  `owner_agent`.
- [ ] Ticket has a single concrete `scope.goal`.
- [ ] Ticket has `quick_classification` with `quick`, `standard`, or
  `escalate` result.
- [ ] Quick-flow is allowed only when one bounded objective, exact files,
  maximum three non-ticket files, maximum one module/service, and local proof are
  all true.
- [ ] Quick-flow escalates on security/auth/privacy, schema/data, dependencies,
  multiple services/modules, public API/shared contract, visual ambiguity,
  unclear requirements, forbidden paths, or broad file scope.
- [ ] `allowed_files` and `forbidden_files` are explicit.
- [ ] `spec_refs` either names requirements/design/tasks specs or gives a
  concrete no-spec reason for tiny low-risk work.
- [ ] Full-SDD spec references resolve and use stable IDs.
- [ ] Blocking unknown/proposed requirements or design decisions are resolved
  before a worker starts.
- [ ] `locked_decisions` and `unresolved_decisions` are explicit.
- [ ] No `unresolved_decisions` item blocks implementation.
- [ ] `context_budget.required_context` is compact and excludes raw transcripts,
  secrets, and unrelated logs.
- [ ] Required steering docs are named, and any steering conflict is recorded as
  a blocker or resolved decision.
- [ ] `in_scope` and `out_of_scope` are explicit.
- [ ] `execution_intensity` is one of `quick_flow`, `standard_worker`,
  `expert_supported`, `bounded_expert_rounds`, or `research_only`.
- [ ] Single-ticket autonomous runs record the full state machine and block
  `done` until `head_equals_origin_main_proved`.
- [ ] `manager_role` is explicit.
- [ ] `worker_sequence` is ordered and each worker has a bounded task.
- [ ] `expert_plan` says whether read-only Codex reviewer input is required.
- [ ] `expert_routing` names required native expert profiles or records an
  explicit not-required reason.
- [ ] Expert routing is based on concrete risk/evidence needs, not ceremony.
- [ ] Any Codex subagent role inherits `AGENTS.md`, ticket scope, approval
  boundaries, forbidden actions, and verification requirements.
- [ ] `debug_logging_plan` names an owner and surfaces.
- [ ] `test_plan` lists concrete commands or manual proof steps.
- [ ] `proof_gates` define what must pass before done.
- [ ] Proof gates require repository discovery, focused tests, self-review,
  independent review when required, execution result, context curation, and
  delivery proof when assigned.
- [ ] `regression_gates` define what must not break.
- [ ] `visual_gate` is explicit when UI changes.
- [ ] `checkpoint_policy` is explicit.
- [ ] `rollback_or_accept_policy` is explicit.
- [ ] `stop_conditions` are explicit.
- [ ] `handoff_requirements` are explicit.
- [ ] `done_definition` is concrete.
- [ ] Ticket allows `agent/**` updates or explicitly explains where durable
  state/decision/issue/todo updates will be recorded.
