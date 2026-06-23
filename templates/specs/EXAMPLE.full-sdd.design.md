# Design

Design ID: `DES-2026-06-23-example-full-sdd`
Status: `accepted`
Feature or fix: `example-full-sdd`
Requirements: `templates/specs/EXAMPLE.full-sdd.requirements.md`
Owning ticket: `TKT-YYYY-MM-DD-example-full-sdd`

## Overview

The ticket carries execution scope while spec files carry durable requirements,
design decisions, and task decomposition.

## Decisions

| Decision ID | Status | Decision | Rationale | Requirement IDs |
| --- | --- | --- | --- | --- |
| DEC-001 | accepted | Keep SDD specs separate from ticket execution records. | Tickets stay bounded and specs remain reusable. | REQ-001 |

## Impacted Files

| Path | Change | Requirement IDs | Task IDs |
| --- | --- | --- | --- |
| `templates/TEMPLATE.ticket.yaml` | Add spec references | REQ-001 | TASK-001 |

## Interfaces And Contracts

- Inputs: ticket `spec_refs`
- Outputs: traceable requirement/design/task links
- Contracts: markdown spec IDs and ticket YAML references

## Failure Modes

| Failure | Expected handling | Proof |
| --- | --- | --- |
| Missing spec path | Ticket readiness blocks implementation. | Cross-reference check. |

## Security And Privacy

- Secrets: not affected.
- Permissions: not affected.
- User data: not affected.
- Local/private paths: not introduced.

## Test Strategy

| Requirement ID | Test or proof | Notes |
| --- | --- | --- |
| REQ-001 | Parse ticket YAML and inspect referenced paths. | Low-risk documentation/template proof. |
