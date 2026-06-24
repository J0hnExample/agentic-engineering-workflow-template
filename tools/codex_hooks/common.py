from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


MAX_OUTPUT_CHARS = 3500
SECRET_RE = re.compile(r"(secret|token|password|credential|api[_-]?key|\.env|secrets)", re.IGNORECASE)
SAFE_TOKEN_KEYS = {"progress_token", "last_progress_token", "last_continuation_token"}
STATE_RELATIVE_PATHS = (
    ".git/agentic-workflow-controller/RUN_STATE.json",
    ".git/agentic-workflow-v05-controller/RUN_STATE.json",
)
TERMINAL_STATUSES = {"complete", "completed", "blocked", "user_decision", "user-decision", "waiting_on_user"}


def read_stdin_json() -> dict[str, Any]:
    raw = sys.stdin.read()
    if not raw.strip():
        return {}
    try:
        value = json.loads(raw)
    except json.JSONDecodeError:
        return {"_stdin_error": "invalid_json"}
    return value if isinstance(value, dict) else {"_stdin_error": "non_object"}


def repo_root(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists():
            return candidate
    return current


def load_active_state(root: Path | None = None) -> tuple[dict[str, Any] | None, Path | None, str | None]:
    base = root or repo_root()
    for rel in STATE_RELATIVE_PATHS:
        path = base / rel
        if not path.exists():
            continue
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            return None, path, f"invalid state JSON: {exc}"
        if not isinstance(value, dict):
            return None, path, "state JSON is not an object"
        return value, path, None
    return None, None, None


def redact(value: Any) -> Any:
    if isinstance(value, dict):
        redacted: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            redacted[key_text] = item if key_text in SAFE_TOKEN_KEYS else "[REDACTED]" if SECRET_RE.search(key_text) else redact(item)
        return redacted
    if isinstance(value, list):
        return [redact(item) for item in value[:30]]
    if isinstance(value, str):
        return "[REDACTED]" if SECRET_RE.search(value) else value
    return value


def compact_json(value: dict[str, Any]) -> str:
    text = json.dumps(redact(value), sort_keys=True, separators=(",", ":"))
    if len(text) > MAX_OUTPUT_CHARS:
        text = text[: MAX_OUTPUT_CHARS - 30] + "...[truncated]"
    return text


def emit(value: dict[str, Any]) -> int:
    print(compact_json(value))
    return 0


def source_lock_valid(state: dict[str, Any]) -> bool:
    lock = state.get("source_lock")
    if not isinstance(lock, dict):
        return False
    if lock.get("status") in {"failed", "invalid"} or lock.get("failure_marker"):
        return False
    if lock.get("status") not in {"valid", "passed", "ok"}:
        return False
    active = state.get("active_ticket_id")
    return not active or lock.get("active_ticket_id") in {None, active}


def active_ticket(state: dict[str, Any]) -> dict[str, Any]:
    active_id = state.get("active_ticket_id")
    tickets = state.get("tickets")
    if isinstance(tickets, list):
        for ticket in tickets:
            if isinstance(ticket, dict) and ticket.get("id") == active_id:
                return ticket
    return {}


def is_terminal(state: dict[str, Any]) -> bool:
    status = str(state.get("status", "")).lower()
    if status in TERMINAL_STATUSES:
        return True
    ticket = active_ticket(state)
    completed = ticket.get("completed_phases", [])
    return isinstance(completed, list) and "completed" in completed


def continuation_budget(state: dict[str, Any]) -> tuple[int, int, int]:
    cont = state.get("continuation")
    if not isinstance(cont, dict):
        cont = {}
    total = int(cont.get("budget_total", state.get("continuation_budget_total", 0)) or 0)
    used = int(cont.get("budget_used", state.get("continuation_budget_used", 0)) or 0)
    return total, used, max(total - used, 0)


def completed_digest(ticket: dict[str, Any]) -> str:
    phases = ticket.get("completed_phases", [])
    if not isinstance(phases, list):
        phases = []
    return hashlib.sha256("|".join(str(item) for item in phases).encode("utf-8")).hexdigest()[:12]


def git_head(root: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            check=False,
        )
    except OSError:
        return None
    if result.returncode != 0:
        return None
    return result.stdout.strip() or None


def progress_token(state: dict[str, Any], root: Path | None = None) -> str:
    ticket = active_ticket(state)
    writer = state.get("writer_lock") if isinstance(state.get("writer_lock"), dict) else {}
    delivery = ticket.get("delivery") if isinstance(ticket.get("delivery"), dict) else {}
    repair = ticket.get("repair") if isinstance(ticket.get("repair"), dict) else {}
    parts = [
        str(state.get("active_ticket_id")),
        str(state.get("active_phase")),
        completed_digest(ticket),
        str(repair.get("round", repair.get("rounds_used", state.get("repair_count", 0)))),
        str(writer.get("held_by")),
        str(delivery.get("commit_sha")),
        str(delivery.get("pushed")),
        str(delivery.get("head_equals_upstream_proved")),
    ]
    head = git_head(root) if root is not None else None
    if head:
        parts.append(head)
    return hashlib.sha256("\n".join(parts).encode("utf-8")).hexdigest()[:16]


def next_phase(state: dict[str, Any]) -> str | None:
    active = state.get("active_phase")
    if active:
        return str(active)
    ticket = active_ticket(state)
    completed = ticket.get("completed_phases", [])
    phases = [
        "pending",
        "source_lock_validated",
        "repository_validated",
        "plan_recorded",
        "repository_ticket_recorded",
        "implementation_writer_locked",
        "implementation_spawned",
        "implementation_completed",
        "writer_thread_closed",
        "focused_tests_passed",
        "self_review_completed",
        "independent_review_spawned",
        "independent_review_completed",
        "repair_completed_or_not_needed",
        "context_curated",
        "git_delivery_started",
        "explicit_paths_staged",
        "committed",
        "pushed",
        "head_equals_upstream_proved",
        "completed",
    ]
    if not isinstance(completed, list):
        return None
    if not completed:
        return phases[0]
    try:
        index = phases.index(str(completed[-1]))
    except ValueError:
        return None
    return phases[index + 1] if index + 1 < len(phases) else None
