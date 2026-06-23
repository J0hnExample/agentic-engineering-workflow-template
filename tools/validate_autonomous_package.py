#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


FULL_TICKET_ID = re.compile(r"^TKT-\d{4}-\d{2}-\d{2}-[A-Za-z0-9][A-Za-z0-9_.-]*$")


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def inside(child: Path, root: Path) -> bool:
    try:
        child.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def validate(package_root: Path, active_ticket_id: str | None = None, active_ticket_file: Path | None = None) -> list[str]:
    errors: list[str] = []
    if not package_root.is_absolute():
        return ["package root must be absolute"]
    if not package_root.is_dir():
        return [f"package root missing: {package_root}"]

    manifest_path = package_root / "manifest.json"
    if not manifest_path.is_file():
        return ["manifest.json missing"]
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"invalid manifest: {exc}"]

    declared_entries = manifest.get("files", [])
    if not isinstance(declared_entries, list):
        errors.append("manifest files must be a list")
        declared_entries = []
    declared: dict[str, dict[str, object]] = {}
    for entry in declared_entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), str):
            errors.append("invalid file declaration")
            continue
        rel = entry["path"]
        if rel in declared:
            errors.append(f"duplicate file declaration: {rel}")
        declared[rel] = entry

    actual = {
        path.relative_to(package_root).as_posix()
        for path in package_root.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts and not path.name.endswith(".pyc")
    }
    actual.discard("manifest.json")
    missing = sorted(set(declared) - actual)
    extra = sorted(actual - set(declared))
    if missing:
        errors.append(f"declared files missing: {missing}")
    if extra:
        errors.append(f"undeclared files: {extra}")

    for rel, entry in declared.items():
        expected = entry.get("sha256")
        if not isinstance(expected, str) or not expected:
            errors.append(f"missing sha256: {rel}")
            continue
        path = package_root / rel
        if path.is_file() and digest(path) != expected:
            errors.append(f"hash mismatch: {rel}")

    tickets = manifest.get("tickets", [])
    if not isinstance(tickets, list) or not tickets:
        errors.append("manifest tickets must be a non-empty list")
        tickets = []
    seen: set[str] = set()
    order_by_id: dict[str, int] = {}
    ticket_ids: list[str] = []
    for index, ticket in enumerate(tickets):
        if not isinstance(ticket, dict):
            errors.append(f"invalid ticket declaration at {index}")
            continue
        tid = ticket.get("id")
        ticket_ids.append(str(tid))
        if ticket.get("order") != index:
            errors.append(f"ticket order mismatch at {index}")
        if not isinstance(tid, str) or not FULL_TICKET_ID.match(tid):
            errors.append(f"ticket id is not full: {tid}")
        elif tid in seen:
            errors.append(f"duplicate ticket id: {tid}")
        else:
            seen.add(tid)
            order_by_id[tid] = index
        rel = ticket.get("path")
        if not isinstance(rel, str):
            errors.append(f"ticket path missing: {tid}")
        elif rel not in declared:
            errors.append(f"ticket file undeclared: {tid}")
        else:
            path = package_root / rel
            if not path.is_file():
                errors.append(f"ticket file missing: {tid}")
            else:
                match = re.search(r'^id:\s*"?([^"\s]+)"?\s*$', path.read_text(encoding="utf-8"), re.M)
                if not match or match.group(1) != tid:
                    errors.append(f"ticket id/path mismatch: {tid}")
        depends_on = ticket.get("depends_on", [])
        if not isinstance(depends_on, list):
            errors.append(f"ticket depends_on must be a list: {tid}")
            depends_on = []
        for dep in depends_on:
            if dep not in order_by_id:
                errors.append(f"{tid} depends on missing/later {dep}")
            elif order_by_id[dep] >= index:
                errors.append(f"{tid} depends on later {dep}")

    graph = manifest.get("dependency_graph", [])
    expected_graph = [
        {"id": ticket.get("id"), "depends_on": ticket.get("depends_on", [])}
        for ticket in tickets
        if isinstance(ticket, dict)
    ]
    if graph != expected_graph:
        errors.append("dependency graph order does not match ticket order")
    for rel in manifest.get("read_order", []):
        if rel != "manifest.json" and rel not in declared:
            errors.append(f"read_order undeclared: {rel}")

    if active_ticket_id or active_ticket_file:
        if not active_ticket_id or not active_ticket_file:
            errors.append("active ticket requires both id and file")
        elif not FULL_TICKET_ID.match(active_ticket_id):
            errors.append("active ticket id must be full")
        elif not active_ticket_file.is_absolute():
            errors.append("active ticket file must be absolute")
        else:
            active = active_ticket_file.resolve()
            if not inside(active, package_root):
                errors.append("active ticket file is outside package root")
            by_id = {ticket.get("id"): ticket for ticket in tickets if isinstance(ticket, dict)}
            item = by_id.get(active_ticket_id)
            if not item:
                errors.append(f"active ticket id not in manifest: {active_ticket_id}")
            else:
                expected_path = (package_root / item["path"]).resolve()
                if active != expected_path:
                    errors.append(f"active ticket path mismatch: expected {expected_path}, got {active}")
                entry = declared.get(item["path"])
                if not entry:
                    errors.append("active ticket manifest file entry missing")
                elif active.is_file() and entry.get("sha256") and digest(active) != entry.get("sha256"):
                    errors.append("active ticket manifest hash mismatch")
                if active.is_file():
                    match = re.search(r'^id:\s*"?([^"\s]+)"?\s*$', active.read_text(encoding="utf-8"), re.M)
                    if not match or match.group(1) != active_ticket_id:
                        errors.append("active ticket file id mismatch")
                else:
                    errors.append(f"active ticket file missing: {active}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a generic source-locked autonomous ticket package.")
    parser.add_argument("package_root", type=Path, help="Absolute package root.")
    parser.add_argument("--active-ticket-id", help="Full active ticket ID.")
    parser.add_argument("--active-ticket-file", type=Path, help="Absolute package-local active ticket file.")
    args = parser.parse_args()
    errors = validate(args.package_root, args.active_ticket_id, args.active_ticket_file)
    if errors:
        print("AUTONOMOUS PACKAGE VALIDATION FAILED")
        for error in errors:
            print("- " + error)
        return 1
    print("AUTONOMOUS PACKAGE VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
