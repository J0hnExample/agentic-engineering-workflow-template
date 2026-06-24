#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from tools.codex_hooks.common import continuation_budget, emit, is_terminal, load_active_state, next_phase, progress_token, read_stdin_json, repo_root, source_lock_valid


def main() -> int:
    read_stdin_json()
    root = repo_root(Path.cwd())
    state, _, error = load_active_state(root)
    if state is None:
        return emit({"hook": "Stop", "continue": False, "reason": error or "no_active_run"})
    if not source_lock_valid(state):
        return emit({"hook": "Stop", "continue": False, "reason": "source_lock_not_valid"})
    if is_terminal(state):
        return emit({"hook": "Stop", "continue": False, "reason": "terminal_state"})
    phase = next_phase(state)
    if not phase:
        return emit({"hook": "Stop", "continue": False, "reason": "no_next_phase"})
    total, used, remaining = continuation_budget(state)
    if remaining <= 0:
        return emit({"hook": "Stop", "continue": False, "reason": "continuation_budget_exhausted"})
    token = progress_token(state, root)
    continuation = state.get("continuation", {}) if isinstance(state.get("continuation"), dict) else {}
    if continuation.get("last_continuation_token") == token:
        return emit({"hook": "Stop", "continue": False, "reason": "no_progress", "progress_token": token})
    return emit(
        {
            "hook": "Stop",
            "continue": True,
            "reason": "active_run_has_progress_and_budget",
            "active_ticket_id": state.get("active_ticket_id"),
            "next_legal_phase": phase,
            "progress_token": token,
            "continuation_budget": {"total": total, "used": used, "remaining": remaining},
        }
    )


if __name__ == "__main__":
    raise SystemExit(main())
