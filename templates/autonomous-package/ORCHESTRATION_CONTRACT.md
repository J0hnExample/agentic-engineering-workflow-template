# Orchestration Contract

- Repository evidence is authoritative.
- Package manifests and hashes are source locks.
- Tickets run in dependency order.
- Exactly one writer may implement the active ticket.
- Review is independent and read-only.
- Repair is bounded by the ticket and package policy.
- Context handoff records must be compact and evidence based.
- Delivery uses explicit scoped staging only when assigned.
- Unrelated work is preserved and never reverted or staged.
