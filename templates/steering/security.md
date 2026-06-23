---
id: security
title: Security And Privacy Steering
inclusion:
  mode: always
  fileMatch: []
  description: "Load for all tasks because secrets and approval boundaries are core workflow constraints."
context_pack:
  required_when:
    - "<all tickets>"
  excluded_when: []
---

# Security And Privacy Steering

## Guidance

- Do not read, print, copy, create, or modify secret values or private
  environment files.
- Do not push, deploy, release, publish, run migrations with side effects, or
  contact external services unless the ticket and user approval allow the exact
  action.
- Specialized steering may narrow behavior but must not weaken safety
  boundaries.
