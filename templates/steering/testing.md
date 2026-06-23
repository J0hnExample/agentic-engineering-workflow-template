---
id: testing
title: Testing Steering
inclusion:
  mode: fileMatch
  fileMatch:
    - "tests/**"
    - "test/**"
    - "**/*.test.*"
    - "**/*.spec.*"
    - "vitest.config.*"
    - "jest.config.*"
    - "playwright.config.*"
    - "pytest.ini"
    - "tox.ini"
    - "src/**"
    - "app/**"
    - "packages/**"
  description: "Load when changes require automated tests, manual proof, coverage decisions, or verification strategy."
context_pack:
  required_when:
    - "ticket changes behavior, test files, test config, or proof gates"
  excluded_when:
    - "ticket is documentation-only and proof is limited to inspection"
---

# Testing Steering

## Guidance

- Let proof scale with risk and blast radius.
- Record skipped checks with a concrete reason.
- If the test surface is missing or ambiguous, use the smallest reliable proof
  available and record residual risk.
