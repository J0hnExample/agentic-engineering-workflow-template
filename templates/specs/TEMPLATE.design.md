# Design

Design ID: `DES-YYYY-MM-DD-short-name`
Status: `unknown | proposed | accepted | superseded`
Feature or fix: `<short-name>`
Requirements: `<requirements spec path>`
Owning ticket: `<ticket-id>`

## Overview

Describe the chosen approach and why it satisfies accepted requirements without
widening ticket scope.

## Decisions

| Decision ID | Status | Decision | Rationale | Requirement IDs |
| --- | --- | --- | --- | --- |
| DEC-001 | unknown | `<decision>` | `<why>` | `<REQ-001>` |

Allowed statuses: `unknown`, `proposed`, `accepted`, `superseded`.
Unknown blocking decisions must be resolved before implementation starts.

## Impacted Files

| Path | Change | Requirement IDs | Task IDs |
| --- | --- | --- | --- |
| `<path>` | `<create, edit, remove, verify>` | `<REQ-001>` | `<TASK-001>` |

## Interfaces And Contracts

- Inputs: `<API, CLI, UI, config, event, file, or none>`
- Outputs: `<response, state, artifact, log, or none>`
- Contracts: `<schema, type, protocol, markdown/YAML contract, or none>`

## Failure Modes

| Failure | Expected handling | Proof |
| --- | --- | --- |
| `<failure>` | `<fallback, validation, error, or stop condition>` | `<test or check>` |

## Security And Privacy

- Secrets: `<not affected, or handling requirement>`
- Permissions: `<not affected, or boundary>`
- User data: `<not affected, or protection requirement>`
- Local/private paths: `<must not be introduced unless the target repo requires them>`

## Test Strategy

| Requirement ID | Test or proof | Notes |
| --- | --- | --- |
| REQ-001 | `<command, test file, inspection, or manual proof>` | `<notes>` |
