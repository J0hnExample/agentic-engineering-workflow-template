# Git Delivery

Status: delivery started on `main`; explicit scoped staging planned.

Delivery can start after independent review `PASS` by subagent
`019efa34-9e02-70a1-ab23-4d0a18912745`.

When started, use explicit staging only, preserve the pre-existing untracked ZIP,
exclude generated cache artifacts such as `__pycache__`, and record commit,
push, and upstream equality proof.

Explicit paths to stage:

- `README.md`
- `agent/CHANGELOG.md`
- `agent/DECISIONS.md`
- `agent/PATHS.md`
- `docs/git_delivery.md`
- `docs/implementation/workflow-v0.5/CONTEXT_LEDGER.md`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree/EXECUTION_REPORT.md`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree/GIT_DELIVERY.md`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree/HANDOFF.md`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree/PLAN.md`
- `docs/implementation/workflow-v0.5/tickets/TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree/REVIEW.md`
- `docs/workflow.md`
- `prompts/git-delivery-agent.md`
- `prompts/initialize-repo.md`
- `templates/AGENTS.md.template`
- `templates/TEMPLATE.git-delivery-result.yaml`
- `templates/TEMPLATE.workflow-policy.yaml`
- `tests/test_workflow_git.py`
- `tickets/upgrades/v0.5/TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree.yaml`
- `tools/workflow_git.py`
