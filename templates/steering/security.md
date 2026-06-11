---
id: security
title: Security And Privacy Steering
inclusion:
  mode: always
  fileMatch: []
  description: "Load for all tasks because security, secrets, and approval boundaries are core workflow constraints."
context_pack:
  required_when:
    - "<all tickets>"
  excluded_when: []
---

# Security And Privacy Steering

## Source Of Truth

- Secret locations: `<unknown and should not be read unless explicitly approved>`
- Sensitive data classes: `<unknown until confirmed from repository evidence or user input>`
- External services: `<unknown until confirmed from repository evidence>`

## Guidance

- Do not read, print, copy, create, or modify secret values or private
  environment files.
- Do not push, deploy, release, publish, run migrations with side effects, or
  contact external services unless the ticket and user approval allow the exact
  action.
- Keep security and privacy rules at least as strict as `AGENTS.md`; specialized
  steering may narrow behavior but must not weaken safety boundaries.
