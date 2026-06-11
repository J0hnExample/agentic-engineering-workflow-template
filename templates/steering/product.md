---
id: product
title: Product Steering
inclusion:
  mode: manual
  fileMatch: []
  description: "Load when product goals, user outcomes, or domain behavior are explicitly in scope."
context_pack:
  required_when:
    - "<ticket names product behavior, user outcomes, or domain terminology>"
  excluded_when:
    - "<task is purely mechanical and product behavior is not in scope>"
---

# Product Steering

## Source Of Truth

- Product goal: `<unknown until confirmed from repository evidence or user input>`
- Primary users: `<unknown until confirmed from repository evidence or user input>`
- Non-goals: `<unknown until confirmed from repository evidence or user input>`

## Guidance

- Use repository evidence and ticket specs before making product assumptions.
- Mark unknown product facts as unknown instead of inventing placeholder values.
- If implementation would change user-visible behavior not covered by the
  ticket, stop and request a scope update or follow-up ticket.
