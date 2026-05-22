# Ticket Readiness Checklist

Use before product-code work starts.

- [ ] Ticket has `schema_version`.
- [ ] Ticket has `ticket.id`, `title`, `repo`, `branch`, `status`, and
  `owner_agent`.
- [ ] Ticket has a single concrete `scope.goal`.
- [ ] `allowed_files` and `forbidden_files` are explicit.
- [ ] `in_scope` and `out_of_scope` are explicit.
- [ ] `execution_intensity` is one of `standard_worker`, `expert_supported`,
  `bounded_expert_rounds`, or `research_only`.
- [ ] `manager_role` is explicit.
- [ ] `worker_sequence` is ordered and each worker has a bounded task.
- [ ] `expert_plan` says whether expert review is required.
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
