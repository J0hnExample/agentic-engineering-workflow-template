# Ticket Readiness Checklist

Use before product-code work starts.

- [ ] Ticket has `schema_version`.
- [ ] Ticket has `ticket.id`, `title`, `repo`, `branch`, `status`, and
  `owner_agent`.
- [ ] Ticket has a single concrete `scope.goal`.
- [ ] `allowed_files` and `forbidden_files` are explicit.
- [ ] `in_scope` and `out_of_scope` are explicit.
- [ ] `context_pack.required_steering_files` lists every specialized steering
  file required for the ticket, or is explicitly empty.
- [ ] `context_pack.excluded_context` records noisy, stale, unsafe, or
  out-of-scope context that looked relevant but should not be loaded, or is
  explicitly empty.
- [ ] Required steering files use supported inclusion modes: `always`,
  `fileMatch`, `manual`, or `auto`.
- [ ] Non-trivial implementation work has `spec_refs` for requirements, design,
  and tasks, or `spec_contract.quick_flow_exemption.used: true` with a concrete
  reason.
- [ ] Linked spec artifacts include acceptance criteria, design boundaries,
  task/proof traceability, and unresolved ambiguity handling.
- [ ] `execution_intensity` is one of `standard_worker`, `expert_supported`,
  `bounded_expert_rounds`, or `research_only`.
- [ ] `manager_role` is explicit.
- [ ] `worker_sequence` is ordered and each worker has a bounded task.
- [ ] `expert_plan` says whether read-only Codex reviewer input is required.
- [ ] `expert_routing` lists required profiles, optional profiles, triggers,
  `max_rounds`, escalation rule, and record location, or explicitly sets no
  required profiles and `max_rounds: 0`.
- [ ] Expert routing uses the minimum useful read-only profile route and does
  not require every profile by default.
- [ ] Any Codex subagent role inherits `AGENTS.md`, ticket scope, approval
  boundaries, forbidden actions, and verification requirements.
- [ ] `debug_logging_plan` names an owner and surfaces.
- [ ] `test_plan` lists concrete commands or manual proof steps.
- [ ] `proof_gates` define what must pass before done.
- [ ] `regression_gates` define what must not break.
- [ ] `visual_gate` is explicit when UI changes.
- [ ] `checkpoint_policy` is explicit.
- [ ] `rollback_or_accept_policy` is explicit.
- [ ] `stop_conditions` are explicit.
- [ ] `handoff_requirements` are explicit.
- [ ] `done_definition` is concrete.
- [ ] Ticket allows `agent/**` updates or explicitly explains where durable
  state/decision/issue/todo updates will be recorded.
