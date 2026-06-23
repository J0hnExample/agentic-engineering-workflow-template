---
id: structure
title: Repository Structure Steering
inclusion:
  mode: auto
  fileMatch:
    - "AGENTS.md"
    - "agent/**"
    - "docs/**"
    - "tickets/**"
    - "templates/**"
    - ".codex/**"
  description: "Load when the task creates, moves, renames, or reorganizes files or directories."
context_pack:
  required_when:
    - "ticket changes repository layout or file ownership"
  excluded_when:
    - "ticket only edits files in established locations"
---

# Repository Structure Steering

## Guidance

- Preserve existing layout and naming unless the ticket explicitly changes it.
- Avoid moving files as unrelated cleanup.
- If a new directory is required, document why it belongs in the selected
  location and how future agents should discover it.
