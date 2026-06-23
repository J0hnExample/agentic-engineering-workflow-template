#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


PHASES = [
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

PHASE_INDEX = {phase: index for index, phase in enumerate(PHASES)}
REVIEW_OR_LATER = PHASE_INDEX["self_review_completed"]
DELIVERY_PROOF_PHASES = {"committed", "pushed", "head_equals_upstream_proved", "completed"}
MODES = {"full_chain", "single_ticket"}


def _load_json(path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return None, [f"invalid JSON in {path}: {exc}"]
    if not isinstance(value, dict):
        return None, [f"run state must be a JSON object: {path}"]
    return value, []


def _phase_prefix(completed_phases: Any) -> tuple[list[str], list[str]]:
    if not isinstance(completed_phases, list):
        return [], ["completed_phases must be a list"]
    phases: list[str] = []
    errors: list[str] = []
    for item in completed_phases:
        if not isinstance(item, str) or item not in PHASE_INDEX:
            errors.append(f"unknown completed phase: {item}")
        else:
            phases.append(item)
    if phases:
        expected = PHASES[: len(phases)]
        if phases != expected:
            errors.append(
                "illegal phase skip: completed_phases must be the exact legal prefix "
                f"{expected}, got {phases}"
            )
    return phases, errors


def _ticket_delivery(ticket: dict[str, Any]) -> dict[str, Any]:
    delivery = ticket.get("delivery", {})
    return delivery if isinstance(delivery, dict) else {}


def validate(state_path: Path, manifest_path: Path | None = None) -> tuple[list[str], dict[str, Any]]:
    state, errors = _load_json(state_path)
    if state is None:
        return errors, {}
    manifest: dict[str, Any] | None = None
    if manifest_path is not None:
        manifest, manifest_errors = _load_json(manifest_path)
        errors.extend(manifest_errors)

    if state.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if state.get("mode") not in MODES:
        errors.append("mode must be full_chain or single_ticket")
    if not state.get("package_id"):
        errors.append("package_id is required")

    source_lock = state.get("source_lock", {})
    if not isinstance(source_lock, dict):
        source_lock = {}
        errors.append("source_lock must be an object")
    if source_lock.get("status") == "failed" or source_lock.get("failure_marker"):
        errors.append("source-lock failure marker present")
    if state.get("active_ticket_id") and source_lock.get("active_ticket_id") != state.get("active_ticket_id"):
        errors.append("source_lock.active_ticket_id must match active_ticket_id")

    tickets = state.get("tickets")
    if not isinstance(tickets, list) or not tickets:
        errors.append("tickets must be a non-empty list")
        tickets = []
    if manifest is not None:
        if state.get("package_id") != manifest.get("package_id"):
            errors.append("manifest package_id does not match run state")
        manifest_tickets = manifest.get("tickets", [])
        manifest_ids = [item.get("id") for item in manifest_tickets if isinstance(item, dict)]
        state_ids = [item.get("id") for item in tickets if isinstance(item, dict)]
        if manifest_ids and state_ids != manifest_ids:
            errors.append("run state ticket order does not match manifest")
    if state.get("mode") == "single_ticket" and len(tickets) != 1:
        errors.append("single_ticket mode must contain exactly one ticket")

    ids: list[str] = []
    completed_prefix_open = True
    open_writers: list[str] = []
    first_incomplete: dict[str, Any] | None = None
    last_completed_id: str | None = None

    for index, raw in enumerate(tickets):
        if not isinstance(raw, dict):
            errors.append(f"ticket at index {index} must be an object")
            continue
        ticket_id = raw.get("id")
        if not isinstance(ticket_id, str) or not ticket_id:
            errors.append(f"ticket at index {index} requires id")
            ticket_id = f"<index {index}>"
        if ticket_id in ids:
            errors.append(f"duplicate ticket id: {ticket_id}")
        ids.append(ticket_id)
        if raw.get("order") != index:
            errors.append(f"ticket order mismatch for {ticket_id}: expected {index}")

        completed_phases, phase_errors = _phase_prefix(raw.get("completed_phases", []))
        errors.extend(f"{ticket_id}: {error}" for error in phase_errors)
        current_phase = raw.get("phase")
        if current_phase not in PHASE_INDEX:
            errors.append(f"{ticket_id}: invalid phase {current_phase}")
            current_phase = "pending"
        if completed_phases and PHASE_INDEX[current_phase] < PHASE_INDEX[completed_phases[-1]]:
            errors.append(f"{ticket_id}: current phase precedes recorded completed phase")
        if not completed_phases and current_phase != "pending":
            errors.append(f"{ticket_id}: phase skip before pending completion")
        if completed_phases and current_phase not in completed_phases and current_phase != next_phase_after(completed_phases[-1]):
            errors.append(f"{ticket_id}: current phase must be the last completed phase or the next legal phase")

        is_completed = "completed" in completed_phases
        if is_completed:
            if not completed_prefix_open:
                errors.append(f"completed-prefix violation: {ticket_id} completed after an incomplete ticket")
            last_completed_id = ticket_id
        else:
            completed_prefix_open = False
            if first_incomplete is None:
                first_incomplete = raw

        delivery = _ticket_delivery(raw)
        if is_completed:
            if not delivery.get("commit_sha"):
                errors.append(f"{ticket_id}: completed without commit_sha")
            if delivery.get("pushed") is not True:
                errors.append(f"{ticket_id}: completed without push proof")
            if delivery.get("head_equals_upstream_proved") is not True:
                errors.append(f"{ticket_id}: completed without upstream equality proof")
        for phase in DELIVERY_PROOF_PHASES:
            if phase in completed_phases and not delivery.get("commit_sha"):
                errors.append(f"{ticket_id}: {phase} requires recorded commit_sha")

        if any(PHASE_INDEX[p] >= REVIEW_OR_LATER for p in completed_phases) and "writer_thread_closed" not in completed_phases:
            errors.append(f"{ticket_id}: review or later phase before writer_thread_closed")

        writer_closed = "writer_thread_closed" in completed_phases
        writer_open = "implementation_writer_locked" in completed_phases and not writer_closed
        if writer_open:
            open_writers.append(ticket_id)

        resume = raw.get("resume", {})
        if not isinstance(resume, dict):
            resume = {}
        requested = resume.get("requested_phase") or resume.get("requested_action")
        if "committed" in completed_phases and requested in {"git_delivery_started", "explicit_paths_staged", "committed", "commit", "recommit"}:
            errors.append(f"{ticket_id}: post-commit resume must verify recorded SHA, not recommit")

    if state.get("last_completed_ticket_id") != last_completed_id:
        errors.append("last_completed_ticket_id must match the completed ticket prefix")

    active_ticket_id = state.get("active_ticket_id")
    if active_ticket_id is not None and active_ticket_id not in ids:
        errors.append("active_ticket_id is not in tickets")
    if first_incomplete is not None:
        first_incomplete_id = first_incomplete.get("id")
        if active_ticket_id and active_ticket_id != first_incomplete_id:
            active_index = ids.index(active_ticket_id) if active_ticket_id in ids else -1
            first_index = ids.index(first_incomplete_id) if first_incomplete_id in ids else -1
            if active_index > first_index:
                errors.append("next-ticket planning blocked until previous ticket is completed")

    if len(open_writers) > 1:
        errors.append(f"writer-lock contention: open implementation writers {open_writers}")
    writer_lock = state.get("writer_lock", {})
    if isinstance(writer_lock, dict) and writer_lock.get("held_by"):
        holder_ticket = writer_lock.get("ticket_id")
        if holder_ticket not in open_writers:
            errors.append("writer_lock holder does not match the single open implementation writer")
    elif open_writers:
        errors.append("open implementation writer exists without top-level writer_lock")

    resume = resume_target(state)
    if resume.get("ticket_id"):
        source_phase = resume.get("phase")
        active_phase = state.get("active_phase")
        if active_phase and active_phase != source_phase:
            errors.append("active_phase must match computed resume phase")

    return errors, resume


def next_phase_after(phase: str | None) -> str | None:
    if phase is None:
        return PHASES[0]
    index = PHASE_INDEX.get(phase)
    if index is None or index + 1 >= len(PHASES):
        return None
    return PHASES[index + 1]


def resume_target(state: dict[str, Any]) -> dict[str, Any]:
    tickets = state.get("tickets")
    if not isinstance(tickets, list):
        return {}
    for ticket in tickets:
        if not isinstance(ticket, dict):
            continue
        completed_phases, _ = _phase_prefix(ticket.get("completed_phases", []))
        if "completed" in completed_phases:
            continue
        last = completed_phases[-1] if completed_phases else None
        phase = next_phase_after(last)
        if "committed" in completed_phases and "pushed" not in completed_phases:
            phase = "pushed"
        return {"ticket_id": ticket.get("id"), "phase": phase}
    return {"ticket_id": None, "phase": None}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate deterministic autonomous controller run state.")
    parser.add_argument("state", type=Path, help="Path to RUN_STATE JSON.")
    parser.add_argument("--manifest", type=Path, help="Optional package manifest for ticket-order validation.")
    args = parser.parse_args()
    errors, resume = validate(args.state, args.manifest)
    if errors:
        print("RUN STATE VALIDATION FAILED")
        for error in errors:
            print("- " + error)
        return 1
    print("RUN STATE VALIDATION PASSED")
    if resume.get("ticket_id"):
        print(f"resume_ticket={resume['ticket_id']}")
        print(f"resume_phase={resume['phase']}")
    else:
        print("resume_ticket=<none>")
        print("resume_phase=<none>")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
