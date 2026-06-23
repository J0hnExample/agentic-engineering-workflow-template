# Generic Autonomous Software Request

Use this as the user-facing request shape for any software repository.

Goal:
<what should be true when the work is done>

Context:
<repository path or name, current behavior, relevant docs or tickets, examples,
logs, screenshots, external package paths, and known risks>

Constraints:
<allowed files, forbidden files, dependency policy, branch policy, install
policy, testing limits, delivery limits, security/privacy constraints, and
actions requiring approval>

Done:
<acceptance criteria, required tests, proof artifacts, review state, handoff
state, and delivery state>

Autonomous defaults:

- Start by auditing repository evidence and effective local instructions.
- Build or verify a source-locked ticket package before implementation.
- Plan freshly from current files; do not rely on stale chat context.
- Execute tickets strictly serially.
- Use exactly one implementation writer for the active ticket.
- Use independent read-only review before delivery.
- Repair only inside a bounded loop and do not weaken acceptance criteria.
- Curate context into compact handoff records after every ticket.
- Stage, commit, and push only explicitly scoped paths when delivery is assigned.
- Deliver each ticket completely before starting the next ticket.
- Preserve unrelated dirty work and stop before forbidden files, secrets,
  destructive commands, deployments, releases, force pushes, or hidden scope
  expansion.

Expected first response:

- verified repository and Git baseline
- package or ticket source-lock status
- gaps or blockers
- proposed serial ticket order
- proof gates for each ticket
- implementation start only after the package or active ticket validates
