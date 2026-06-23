# Autonomous Ticket Package

Package: {{PACKAGE_ID}}

Target repository: {{TARGET_REPOSITORY}}

Target branch: {{TARGET_BRANCH}}

Goal:
{{GOAL}}

Read `manifest.json` first, then follow `read_order` exactly. Validate the
package before planning or implementing:

```text
python tools/validate_package.py <absolute-package-root>
```

For an active ticket, validate the full ticket ID and absolute package-local
ticket path before starting work:

```text
python tools/validate_active_ticket.py <absolute-package-root> --active-ticket-id <full-ticket-id> --active-ticket-file <absolute-package-ticket>
```

Execution is strict serial: plan, implement with exactly one writer, review,
repair within the bounded loop, curate context, and deliver one ticket before
starting the next.
