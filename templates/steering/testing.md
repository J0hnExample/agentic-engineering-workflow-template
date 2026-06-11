---
id: testing
title: Testing Steering
inclusion:
  mode: fileMatch
  fileMatch:
    - "<test-glob>"
    - "<test-config-glob>"
    - "<implementation-glob>"
  description: "Load when changes require automated tests, manual proof, coverage decisions, or verification strategy."
context_pack:
  required_when:
    - "<ticket changes behavior, test files, test config, or proof gates>"
  excluded_when:
    - "<ticket is documentation-only and proof is limited to inspection>"
---

# Testing Steering

## Source Of Truth

- Unit test command: `<unknown until confirmed from repository evidence>`
- Integration test command: `<unknown until confirmed from repository evidence>`
- Build or typecheck command: `<unknown until confirmed from repository evidence>`

## Guidance

- Let proof scale with risk and blast radius.
- Record skipped checks with a concrete reason.
- If the test surface is missing or ambiguous, use the smallest reliable proof
  available and record the residual risk.
