---
id: tech
title: Technical Steering
inclusion:
  mode: fileMatch
  fileMatch:
    - "src/**"
    - "app/**"
    - "packages/**"
    - "lib/**"
    - "server/**"
    - "tests/**"
    - "package.json"
    - "pyproject.toml"
    - "Cargo.toml"
    - "go.mod"
    - "Makefile"
    - ".github/**"
  description: "Load when allowed files touch implementation, build, dependency, runtime, or test tooling."
context_pack:
  required_when:
    - "ticket changes architecture, dependencies, runtime code, or tooling"
  excluded_when:
    - "ticket only edits product copy or non-technical notes"
---

# Technical Steering

## Guidance

- Prefer existing repository patterns, scripts, and local helper APIs.
- Do not install, upgrade, or remove dependencies without explicit approval.
- Keep technical changes within `allowed_files`; stop if required work belongs
  in a different package or scope.
