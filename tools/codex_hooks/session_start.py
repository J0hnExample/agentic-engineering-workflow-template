#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from tools.codex_hooks.common import active_ticket, continuation_budget, emit, load_active_state, next_phase, read_stdin_json, repo_root, source_lock_valid


def main() -> int:
    read_stdin_json()
    root = repo_root(Path.cwd())
    state, path, error = load_active_state(root)
    if state is None:
        return emit({"hook": "SessionStart", "active_run": False, "reason": error or "no_active_run"})
    ticket = active_ticket(state)
    total, used, remaining = continuation_budget(state)
    return emit(
        {
            "hook": "SessionStart",
            "active_run": True,
            "state_path": str(path.relative_to(root)) if path else None,
            "package_id": state.get("package_id"),
            "mode": state.get("mode"),
            "active_ticket_id": state.get("active_ticket_id"),
            "active_phase": state.get("active_phase") or ticket.get("phase"),
            "next_legal_phase": next_phase(state),
            "source_lock_valid": source_lock_valid(state),
            "writer_lock": state.get("writer_lock", {}),
            "last_completed_ticket_id": state.get("last_completed_ticket_id"),
            "repair_count": state.get("repair_count", ticket.get("repair", {})),
            "continuation_budget": {"total": total, "used": used, "remaining": remaining},
        }
    )


if __name__ == "__main__":
    raise SystemExit(main())
