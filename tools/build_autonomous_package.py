#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path
from string import Template
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SKELETON = ROOT / "templates" / "autonomous-package"
FULL_TICKET_ID = re.compile(r"^TKT-\d{4}-\d{2}-\d{2}-[A-Za-z0-9][A-Za-z0-9_.-]*$")
DEFAULT_FORBIDDEN = [".env", ".env.*", "**/secrets/**", "node_modules/**", "dist/**", "build/**", "coverage/**", ".git/**"]


VALIDATE_PACKAGE_SCRIPT = '''#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

FULL_TICKET_ID = re.compile(r"^TKT-\\d{4}-\\d{2}-\\d{2}-[A-Za-z0-9][A-Za-z0-9_.-]*$")


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _inside(child: Path, root: Path) -> bool:
    try:
        child.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def validate(root: Path, active_ticket_id: str | None = None, active_ticket_file: Path | None = None) -> list[str]:
    errors: list[str] = []
    if not root.is_absolute():
        return ["package root must be absolute"]
    if not root.is_dir():
        return [f"package root missing: {root}"]
    manifest_path = root / "manifest.json"
    if not manifest_path.is_file():
        return ["manifest.json missing"]
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"invalid manifest: {exc}"]

    declared_entries = manifest.get("files", [])
    declared = {entry.get("path"): entry for entry in declared_entries if isinstance(entry, dict)}
    if len(declared) != len(declared_entries):
        errors.append("duplicate or invalid file declarations")
    actual = {
        p.relative_to(root).as_posix()
        for p in root.rglob("*")
        if p.is_file() and "__pycache__" not in p.parts and not p.name.endswith(".pyc")
    }
    actual.discard("manifest.json")
    declared_paths = set(declared)
    missing = sorted(declared_paths - actual)
    extra = sorted(actual - declared_paths)
    if missing:
        errors.append(f"declared files missing: {missing}")
    if extra:
        errors.append(f"undeclared files: {extra}")
    for rel, entry in declared.items():
        path = root / rel
        expected = entry.get("sha256")
        if not isinstance(expected, str) or not expected:
            errors.append(f"missing sha256: {rel}")
            continue
        if path.is_file() and digest(path) != expected:
            errors.append(f"hash mismatch: {rel}")

    tickets = manifest.get("tickets", [])
    seen: set[str] = set()
    order_by_id: dict[str, int] = {}
    for index, ticket in enumerate(tickets):
        tid = ticket.get("id")
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
        if not isinstance(rel, str) or rel not in declared:
            errors.append(f"ticket file undeclared: {tid}")
        else:
            path = root / rel
            if not path.is_file():
                errors.append(f"ticket file missing: {tid}")
            else:
                text = path.read_text(encoding="utf-8")
                match = re.search(r'^id:\\s*"?([^"\\s]+)"?\\s*$', text, re.M)
                if not match or match.group(1) != tid:
                    errors.append(f"ticket id/path mismatch: {tid}")
        for dep in ticket.get("depends_on", []):
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
            if not _inside(active, root):
                errors.append("active ticket file is outside package root")
            by_id = {ticket.get("id"): ticket for ticket in tickets}
            item = by_id.get(active_ticket_id)
            if not item:
                errors.append(f"active ticket id not in manifest: {active_ticket_id}")
            else:
                expected = (root / item["path"]).resolve()
                if active != expected:
                    errors.append(f"active ticket path mismatch: expected {expected}, got {active}")
                file_entry = declared.get(item["path"])
                if not file_entry:
                    errors.append("active ticket manifest file entry missing")
                elif active.is_file() and file_entry.get("sha256") and digest(active) != file_entry.get("sha256"):
                    errors.append("active ticket manifest hash mismatch")
                if active.is_file():
                    text = active.read_text(encoding="utf-8")
                    match = re.search(r'^id:\\s*"?([^"\\s]+)"?\\s*$', text, re.M)
                    if not match or match.group(1) != active_ticket_id:
                        errors.append("active ticket file id mismatch")
                else:
                    errors.append(f"active ticket file missing: {active}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a source-locked autonomous ticket package.")
    parser.add_argument("package_root", type=Path, help="Absolute package root.")
    parser.add_argument("--active-ticket-id", help="Full active ticket ID.")
    parser.add_argument("--active-ticket-file", type=Path, help="Absolute active package ticket path.")
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
'''


VALIDATE_ACTIVE_TICKET_SCRIPT = '''#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an active package ticket source lock.")
    parser.add_argument("package_root", type=Path, help="Absolute package root.")
    parser.add_argument("--active-ticket-id", required=True, help="Full active ticket ID.")
    parser.add_argument("--active-ticket-file", required=True, type=Path, help="Absolute active package ticket path.")
    args = parser.parse_args()
    validator_path = args.package_root / "tools" / "validate_package.py"
    spec = importlib.util.spec_from_file_location("validate_package", validator_path)
    if spec is None or spec.loader is None:
        print("ACTIVE TICKET VALIDATION FAILED")
        print("- cannot load package validator")
        return 1
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    errors = module.validate(args.package_root, args.active_ticket_id, args.active_ticket_file)
    if errors:
        print("ACTIVE TICKET VALIDATION FAILED")
        for error in errors:
            print("- " + error)
        return 1
    print("ACTIVE TICKET VALIDATION PASSED: " + args.active_ticket_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
'''


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def render(text: str, values: dict[str, str]) -> str:
    return Template(text.replace("{{", "${").replace("}}", "}")).safe_substitute(values)


def yaml_scalar(value: Any) -> str:
    return json.dumps(str(value))


def yaml_list(values: Any) -> str:
    if not values:
        return "[]"
    if not isinstance(values, list):
        values = [values]
    return "[" + ", ".join(json.dumps(str(value)) for value in values) + "]"


def require_string(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"request field {key!r} must be a non-empty string")
    return value.strip()


def normalize_request(data: dict[str, Any]) -> dict[str, Any]:
    package_id = require_string(data, "package_id")
    target_repository = require_string(data, "target_repository")
    target_branch = require_string(data, "target_branch")
    goal = require_string(data, "goal")
    context = require_string(data, "context")
    constraints = require_string(data, "constraints")
    done = require_string(data, "done")
    tickets = data.get("tickets")
    if not isinstance(tickets, list) or not tickets:
        raise ValueError("request field 'tickets' must be a non-empty list")
    normalized: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, raw in enumerate(tickets):
        if not isinstance(raw, dict):
            raise ValueError(f"ticket {index} must be an object")
        tid = require_string(raw, "id")
        if not FULL_TICKET_ID.match(tid):
            raise ValueError(f"ticket id is not full: {tid}")
        if tid in seen:
            raise ValueError(f"duplicate ticket id: {tid}")
        seen.add(tid)
        order = int(raw.get("order", index))
        if order != index:
            raise ValueError(f"ticket {tid} order must be {index}")
        depends_on = raw.get("depends_on", [])
        if not isinstance(depends_on, list):
            raise ValueError(f"ticket {tid} depends_on must be a list")
        for dep in depends_on:
            if dep not in seen:
                raise ValueError(f"ticket {tid} depends on missing or later ticket {dep}")
        normalized.append(
            {
                "id": tid,
                "order": index,
                "title": require_string(raw, "title"),
                "objective": str(raw.get("objective") or raw.get("goal") or goal),
                "depends_on": depends_on,
                "allowed_paths": raw.get("allowed_paths", ["**"]),
                "forbidden_paths": raw.get("forbidden_paths", DEFAULT_FORBIDDEN),
                "acceptance_criteria": raw.get("acceptance_criteria", data.get("done", [])),
                "required_tests": raw.get("required_tests", ["Run focused tests named by the ticket."]),
                "required_evidence": raw.get("required_evidence", ["Record commands, results, changed files, and residual risks."]),
                "stop_conditions": raw.get("stop_conditions", ["Required work exceeds scope or touches forbidden paths."]),
                "delivery": raw.get("delivery", {"assigned": True, "require_push": True}),
            }
        )
    result = dict(data)
    result["tickets"] = normalized
    result["package_id"] = package_id
    result["target_repository"] = target_repository
    result["target_branch"] = target_branch
    result["goal"] = goal
    result["context"] = context
    result["constraints"] = constraints
    result["done"] = done
    return result


def write_text(path: Path, text: str, executable: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    if executable:
        path.chmod(0o755)


def render_skeleton(package_root: Path, request: dict[str, Any]) -> None:
    values = {
        "PACKAGE_ID": request["package_id"],
        "TARGET_REPOSITORY": request["target_repository"],
        "TARGET_BRANCH": request["target_branch"],
        "GOAL": request["goal"],
        "CONTEXT": request["context"],
        "CONSTRAINTS": request["constraints"],
        "DONE": request["done"],
    }
    for source in sorted(SKELETON.rglob("*")):
        if not source.is_file():
            continue
        rel = source.relative_to(SKELETON)
        if rel.as_posix() in {
            "manifest.template.json",
            "tickets/TICKET.template.yaml",
            "runtime/RUN_STATE.template.json",
            "tools/validate_package.py.template",
            "tools/validate_active_ticket.py.template",
        }:
            continue
        target = package_root / rel
        write_text(target, render(source.read_text(encoding="utf-8"), values))
    write_text(package_root / "PACKAGE_ID.txt", request["package_id"] + "\n")
    write_text(package_root / "tools" / "validate_package.py", VALIDATE_PACKAGE_SCRIPT, executable=True)
    write_text(package_root / "tools" / "validate_active_ticket.py", VALIDATE_ACTIVE_TICKET_SCRIPT, executable=True)


def ticket_yaml(request: dict[str, Any], ticket: dict[str, Any]) -> str:
    delivery = ticket.get("delivery") if isinstance(ticket.get("delivery"), dict) else {}
    values = {
        "TICKET_ID": ticket["id"],
        "TICKET_ORDER": str(ticket["order"]),
        "TICKET_TITLE": ticket["title"],
        "TARGET_REPOSITORY": request["target_repository"],
        "TARGET_BRANCH": request["target_branch"],
        "TICKET_DEPENDS_ON": yaml_list(ticket["depends_on"]),
        "TICKET_OBJECTIVE": ticket["objective"],
        "TICKET_ALLOWED_PATHS": yaml_list(ticket["allowed_paths"]),
        "TICKET_FORBIDDEN_PATHS": yaml_list(ticket["forbidden_paths"]),
        "TICKET_ACCEPTANCE_CRITERIA": yaml_list(ticket["acceptance_criteria"]),
        "TICKET_REQUIRED_TESTS": yaml_list(ticket["required_tests"]),
        "TICKET_REQUIRED_EVIDENCE": yaml_list(ticket["required_evidence"]),
        "TICKET_DELIVERY_ASSIGNED": "true" if delivery.get("assigned", True) else "false",
        "TICKET_REQUIRE_PUSH": "true" if delivery.get("require_push", True) else "false",
        "TICKET_STOP_CONDITIONS": yaml_list(ticket["stop_conditions"]),
    }
    template = (SKELETON / "tickets" / "TICKET.template.yaml").read_text(encoding="utf-8")
    return render(template, values)


def render_tickets(package_root: Path, request: dict[str, Any]) -> None:
    for ticket in request["tickets"]:
        write_text(package_root / "tickets" / f"{ticket['id']}.yaml", ticket_yaml(request, ticket))
        for name in ["TICKET_PLAN", "TICKET_EXECUTION_REPORT", "TICKET_REVIEW", "TICKET_HANDOFF", "GIT_DELIVERY_REPORT"]:
            source = SKELETON / "reports" / f"{name}.template.md"
            rel_name = {
                "TICKET_PLAN": "PLAN.md",
                "TICKET_EXECUTION_REPORT": "EXECUTION_REPORT.md",
                "TICKET_REVIEW": "REVIEW.md",
                "TICKET_HANDOFF": "HANDOFF.md",
                "GIT_DELIVERY_REPORT": "GIT_DELIVERY.md",
            }[name]
            write_text(
                package_root / "reports" / ticket["id"] / rel_name,
                render(source.read_text(encoding="utf-8"), {"PACKAGE_ID": request["package_id"], "TICKET_ID": ticket["id"]}),
            )


def write_run_state(package_root: Path, request: dict[str, Any]) -> None:
    state = {
        "schema_version": 1,
        "package_id": request["package_id"],
        "current_ticket_id": None,
        "last_completed_ticket_id": None,
        "tickets": [
            {"id": ticket["id"], "order": ticket["order"], "status": "pending"}
            for ticket in request["tickets"]
        ],
    }
    write_text(package_root / "runtime" / "RUN_STATE.json", json.dumps(state, indent=2, sort_keys=True) + "\n")


def classify_role(rel: str) -> str:
    if rel.startswith("tickets/"):
        return "ticket"
    if rel.startswith("agents/"):
        return "agent_role"
    if rel.startswith("policies/"):
        return "policy"
    if rel.startswith("tools/"):
        return "validator"
    if rel.startswith("reports/"):
        return "report"
    if rel.startswith("runtime/"):
        return "runtime"
    return "documentation"


def build_manifest(package_root: Path, request: dict[str, Any]) -> dict[str, Any]:
    ticket_paths = [f"tickets/{ticket['id']}.yaml" for ticket in request["tickets"]]
    read_order = [
        "00_START_HERE.md",
        "PACKAGE_ID.txt",
        "README.md",
        "REQUEST.md",
        "ORCHESTRATION_CONTRACT.md",
        "policies/SOURCE_LOCK_POLICY.md",
        "policies/SERIAL_EXECUTION_POLICY.md",
        "policies/REVIEW_REPAIR_POLICY.md",
        "policies/CONTEXT_HANDOFF_POLICY.md",
        "policies/GIT_DELIVERY_POLICY.md",
        "policies/TEST_EVIDENCE_POLICY.md",
        "agents/00_ORCHESTRATOR_AGENT.md",
        "agents/01_GLOBAL_PLANNER_AGENT.md",
        "agents/02_TICKET_PLANNER_AGENT.md",
        "agents/03_TICKET_IMPLEMENTER_AGENT.md",
        "agents/04_INDEPENDENT_REVIEWER_AGENT.md",
        "agents/05_CONTEXT_CURATOR_AGENT.md",
        "agents/06_GIT_DELIVERY_AGENT.md",
        "agents/07_BLOCKER_RESOLVER_AGENT.md",
        *ticket_paths,
        "runtime/RUN_STATE.json",
        "runtime/LOG.template.md",
        "tools/validate_package.py",
        "tools/validate_active_ticket.py",
    ]
    files: list[dict[str, Any]] = []
    for path in sorted(p for p in package_root.rglob("*") if p.is_file()):
        rel = path.relative_to(package_root).as_posix()
        if rel == "manifest.json":
            continue
        entry: dict[str, Any] = {"path": rel, "role": classify_role(rel)}
        entry["sha256"] = digest(path)
        files.append(entry)
    tickets = [
        {
            "order": ticket["order"],
            "id": ticket["id"],
            "title": ticket["title"],
            "path": f"tickets/{ticket['id']}.yaml",
            "depends_on": ticket["depends_on"],
        }
        for ticket in request["tickets"]
    ]
    return {
        "schema_version": 1,
        "package_id": request["package_id"],
        "package_version": "1.0.0",
        "target_repository": request["target_repository"],
        "target_branch": request["target_branch"],
        "execution_mode": "strict_serial_autonomous",
        "read_order": read_order,
        "tickets": tickets,
        "dependency_graph": [{"id": ticket["id"], "depends_on": ticket["depends_on"]} for ticket in request["tickets"]],
        "files": files,
    }


def write_manifest_and_report(package_root: Path, request: dict[str, Any]) -> dict[str, Any]:
    report = [
        "# Validation And Hash Report",
        "",
        f"Package: `{request['package_id']}`",
        f"Tickets: {len(request['tickets'])}",
        "",
        "## Dependency Graph",
        "",
    ]
    for ticket in request["tickets"]:
        deps = ", ".join(ticket["depends_on"]) if ticket["depends_on"] else "none"
        report.append(f"- `{ticket['id']}` depends on: {deps}")
    report.extend([
        "",
        "## Hash Note",
        "",
        "All non-manifest package files are declared with SHA-256 in `manifest.json`.",
        "The builder prints the final manifest SHA-256 after writing `manifest.json`.",
    ])
    write_text(package_root / "VALIDATION_REPORT.md", "\n".join(report) + "\n")
    manifest = build_manifest(package_root, request)
    write_text(package_root / "manifest.json", json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    return manifest


def create_zip(package_root: Path, zip_path: Path) -> None:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(p for p in package_root.rglob("*") if p.is_file()):
            zf.write(path, path.relative_to(package_root.parent).as_posix())


def build(request_path: Path, output_dir: Path | None, zip_path: Path | None, force: bool = False) -> tuple[Path, Path, dict[str, Any]]:
    request = normalize_request(json.loads(request_path.read_text(encoding="utf-8")))
    package_root = output_dir if output_dir is not None else (zip_path.parent / zip_path.stem if zip_path else Path.cwd() / request["package_id"])
    package_root = package_root.resolve()
    if package_root.exists():
        if not force:
            raise FileExistsError(f"output package directory already exists: {package_root}")
        shutil.rmtree(package_root)
    package_root.mkdir(parents=True)
    render_skeleton(package_root, request)
    render_tickets(package_root, request)
    write_run_state(package_root, request)
    manifest = write_manifest_and_report(package_root, request)
    final_zip = zip_path.resolve() if zip_path else package_root.with_suffix(".zip")
    if final_zip.exists():
        if not force:
            raise FileExistsError(f"zip already exists: {final_zip}")
        final_zip.unlink()
    create_zip(package_root, final_zip)
    return package_root, final_zip, manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a generic source-locked autonomous ticket package.")
    parser.add_argument("--request", required=True, type=Path, help="JSON request file.")
    parser.add_argument("--output-dir", type=Path, help="Package directory to create.")
    parser.add_argument("--zip", dest="zip_path", type=Path, help="ZIP path to create. Defaults to <output-dir>.zip.")
    parser.add_argument("--force", action="store_true", help="Replace the output directory or ZIP if they already exist.")
    args = parser.parse_args()
    try:
        package_root, zip_path, manifest = build(args.request, args.output_dir, args.zip_path, args.force)
    except Exception as exc:
        print(f"BUILD FAILED: {exc}", file=sys.stderr)
        return 1
    print("AUTONOMOUS PACKAGE BUILT")
    print(f"package_root={package_root}")
    print(f"zip_path={zip_path}")
    print(f"ticket_count={len(manifest['tickets'])}")
    print(f"declared_files={len(manifest['files'])}")
    print(f"manifest_sha256={digest(package_root / 'manifest.json')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
