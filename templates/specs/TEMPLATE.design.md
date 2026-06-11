# Design

Feature or fix: `<short-name>`

## Overview

Describe the chosen approach and why it satisfies the requirements without
widening the ticket scope.

## Architecture

- Entry points: `<files, commands, routes, or workflows>`
- Components changed: `<modules or docs>`
- Components reused: `<existing helpers, services, or patterns>`
- Components intentionally untouched: `<boundaries>`

## Impacted Files

| Path | Change | Requirement IDs |
| --- | --- | --- |
| `<path>` | `<create, edit, remove, or verify>` | `<REQ-001>` |

## Interfaces

- Inputs: `<API, CLI, UI, config, event, file, or none>`
- Outputs: `<response, state, artifact, log, or none>`
- Contracts: `<schema, type, protocol, markdown/YAML contract, or none>`

## Data Flow

```text
<source> -> <processing step> -> <observable output>
```

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

## Rollout And Compatibility

- Compatibility: `<existing behavior preserved or intentional change>`
- Rollback: `<revert path, feature flag, or not applicable>`
- Documentation: `<docs or agent memory updates needed>`
