# Delta Spec

Delta ID: `DELTA-YYYY-MM-DD-short-name`
Status: `unknown | proposed | accepted | superseded`
Change: `<short-name>`
Owning ticket: `<ticket-id>`
Current specs affected:

- `<spec path or none>`

## ADDED

| Delta Item ID | Status | Requirement ID | New behavior, guarantee, constraint, or proof rule | Required current-spec update | Proof |
| --- | --- | --- | --- | --- | --- |
| ADD-001 | proposed | `<REQ-001>` | `<new expected behavior>` | `<spec path and section>` | `<test, command, review, or manual proof>` |

## MODIFIED

| Delta Item ID | Status | Requirement ID | Existing behavior | New behavior | Required current-spec update | Proof |
| --- | --- | --- | --- | --- | --- |
| MOD-001 | proposed | `<REQ-001>` | `<current behavior>` | `<changed behavior>` | `<spec path and section>` | `<test, command, review, or manual proof>` |

## REMOVED

| Delta Item ID | Status | Requirement ID | Removed behavior, guarantee, constraint, or proof rule | Replacement or removal reason | Required current-spec update | Proof |
| --- | --- | --- | --- | --- | --- | --- |
| REM-001 | proposed | `<REQ-001>` | `<removed expectation>` | `<replacement or none>` | `<spec path and section>` | `<test, command, review, or manual proof>` |

## Closeout

- Accepted delta items must be reflected in durable current specs before ticket
  closeout, or the ticket must record a blocking deferred-spec update with an
  owner and follow-up ticket.
- Superseded delta items must name the replacing item or decision.
- Removed behavior must be documented as intentionally removed, not silently
  omitted from current specs.
