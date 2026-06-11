---
id: tech
title: Technical Steering
inclusion:
  mode: fileMatch
  fileMatch:
    - "<source-or-config-glob>"
    - "<test-or-build-glob>"
  description: "Load when allowed files touch implementation, build, dependency, runtime, or test tooling."
context_pack:
  required_when:
    - "<ticket changes technical architecture, dependencies, runtime code, or tooling>"
  excluded_when:
    - "<ticket only edits product copy or non-technical notes>"
---

# Technical Steering

## Source Of Truth

- Language and runtime: `<unknown until confirmed from repository evidence>`
- Package manager: `<unknown until confirmed from repository evidence>`
- Frameworks and services: `<unknown until confirmed from repository evidence>`
- Test commands: `<unknown until confirmed from repository evidence>`

## Guidance

- Prefer existing repository patterns, scripts, and local helper APIs.
- Do not install, upgrade, or remove dependencies without explicit approval.
- Keep technical changes within the ticket's `allowed_files`; stop if required
  work belongs in a different package or scope.
