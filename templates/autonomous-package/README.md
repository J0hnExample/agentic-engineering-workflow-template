# {{PACKAGE_ID}}

This package contains source-locked instructions and tickets for autonomous
software work in `{{TARGET_REPOSITORY}}`.

It is generic by design. Repository-specific product details belong in the
request record and ticket files, not in the orchestration policy.

## Required Flow

1. Validate this package and its hashes.
2. Read files in manifest `read_order`.
3. Execute tickets in manifest order.
4. Validate the active ticket with full ID and package-local absolute path.
5. Use exactly one implementation writer for each ticket.
6. Run focused proof.
7. Perform independent read-only review.
8. Repair within the configured maximum rounds.
9. Curate handoff context.
10. Commit and push only scoped paths when delivery is assigned.
