#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from tools.codex_hooks.common import active_ticket, emit, load_active_state, read_stdin_json, repo_root, source_lock_valid


def main() -> int:
    read_stdin_json()
    root = repo_root(Path.cwd())
    state, _, error = load_active_state(root)
    if state is None:
        return emit({"hook": "SubagentStart", "active_run": False, "reason": error or "no_active_run"})
    if not source_lock_valid(state):
        return emit(
            {
                "hook": "SubagentStart",
                "active_run": True,
                "source_lock_valid": False,
                "hard_stop": "source lock is not valid; do not inject scope or continue ticket work",
            }
        )
    ticket = active_ticket(state)
    scope = ticket.get("scope", {}) if isinstance(ticket.get("scope"), dict) else {}
    return emit(
        {
            "hook": "SubagentStart",
            "active_run": True,
            "active_ticket_id": state.get("active_ticket_id"),
            "objective": ticket.get("objective"),
            "current_phase": state.get("active_phase") or ticket.get("phase"),
            "allowed_paths": scope.get("allowed_paths", ticket.get("allowed_paths", [])),
            "forbidden_paths": scope.get("forbidden_paths", ticket.get("forbidden_paths", [])),
            "acceptance_gates": ticket.get("acceptance_criteria", ticket.get("acceptance_gates", [])),
            "hard_stop_reminders": ticket.get("hard_stop_conditions", []),
        }
    )


if __name__ == "__main__":
    raise SystemExit(main())
