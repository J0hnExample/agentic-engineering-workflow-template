#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
import tomllib
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
HOOK_EVENTS = {"SessionStart", "SubagentStart", "Stop"}
TICKET_REQUIRED = {
    "schema_version",
    "id",
    "order",
    "title",
    "target_repository",
    "target_branch",
    "objective",
    "scope",
    "implementation_requirements",
    "acceptance_criteria",
    "required_tests",
    "review",
    "delivery",
    "hard_stop_conditions",
}
KNOWN_TICKET_FIELDS = TICKET_REQUIRED | {
    "depends_on",
    "mandatory_plan",
    "source_requirements",
    "required_evidence",
    "context_handoff",
}
PUBLIC_VERSION_RE = re.compile(r"(?:Current version:|Version)\\s+([0-9]+\\.[0-9]+\\.[0-9]+)")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def simple_yaml_top_keys(path: Path) -> list[str]:
    keys: list[str] = []
    for line in read(path).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[:1].isspace() or ":" not in line:
            continue
        keys.append(line.split(":", 1)[0].strip())
    return keys


def simple_yaml_value(path: Path, key: str) -> str | None:
    prefix = key + ":"
    for line in read(path).splitlines():
        if line.startswith(prefix):
            return line.split(":", 1)[1].strip().strip("'\"")
    return None


def validate_json(errors: list[str]) -> None:
    for path in ROOT.rglob("*.json"):
        if any(part in {"node_modules", "dist", "build", "coverage", ".git"} for part in path.parts):
            continue
        try:
            json.loads(read(path))
        except Exception as exc:
            errors.append(f"{rel(path)}: invalid JSON: {exc}")


def validate_hooks(errors: list[str]) -> None:
    path = ROOT / ".codex" / "hooks.json"
    if not path.exists():
        errors.append(".codex/hooks.json: missing")
        return
    try:
        hooks = json.loads(read(path))
    except Exception as exc:
        errors.append(f".codex/hooks.json: invalid JSON: {exc}")
        return
    if not isinstance(hooks, dict):
        errors.append(".codex/hooks.json: top-level value must be an object")
        return
    if set(hooks) != {"hooks"} or not isinstance(hooks.get("hooks"), dict):
        errors.append(".codex/hooks.json: top-level object must contain only a hooks object")
        return
    event_hooks = hooks["hooks"]
    if set(event_hooks) != HOOK_EVENTS:
        errors.append(f".codex/hooks.json: events must be exactly {sorted(HOOK_EVENTS)}")
    for event in HOOK_EVENTS:
        groups = event_hooks.get(event)
        if not isinstance(groups, list) or not groups:
            errors.append(f".codex/hooks.json: {event} must contain matcher groups")
            continue
        for group in groups:
            if not isinstance(group, dict) or "matcher" not in group or not isinstance(group.get("hooks"), list):
                errors.append(f".codex/hooks.json: {event} matcher group must contain matcher and hooks")
                continue
            for hook in group["hooks"]:
                if not isinstance(hook, dict):
                    errors.append(f".codex/hooks.json: {event} hook must be object")
                    continue
                if hook.get("type") != "command":
                    errors.append(f".codex/hooks.json: {event} hook type must be command")
                command = hook.get("command")
                expected = f"python tools/codex_hooks/{event.lower()}.py"
                if event == "SessionStart":
                    expected = "python tools/codex_hooks/session_start.py"
                if event == "SubagentStart":
                    expected = "python tools/codex_hooks/subagent_start.py"
                if command != expected:
                    errors.append(f".codex/hooks.json: {event} command must be {expected}")


def validate_toml(errors: list[str]) -> None:
    for path in [ROOT / ".codex" / "config.toml", *sorted((ROOT / ".codex" / "agents").glob("*.toml"))]:
        if not path.exists():
            continue
        try:
            tomllib.loads(read(path))
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"{rel(path)}: invalid TOML: {exc}")


def validate_tickets(errors: list[str]) -> None:
    for path in sorted((ROOT / "tickets").rglob("*.yaml")):
        if any(part in {"node_modules", "dist", "build", "coverage"} for part in path.parts):
            continue
        keys = simple_yaml_top_keys(path)
        if not keys:
            errors.append(f"{rel(path)}: no YAML top-level keys found")
            continue
        if path.name.startswith("TKT-"):
            missing = sorted(TICKET_REQUIRED - set(keys))
            if missing:
                errors.append(f"{rel(path)}: missing ticket fields {missing}")
            unknown = sorted(set(keys) - KNOWN_TICKET_FIELDS)
            if unknown:
                errors.append(f"{rel(path)}: unknown ticket fields {unknown}")
            ticket_id = simple_yaml_value(path, "id")
            if ticket_id and ticket_id not in path.name:
                errors.append(f"{rel(path)}: id does not match filename")


def validate_references(errors: list[str]) -> None:
    pattern = re.compile(r"`([^`]+\\.(?:md|py|json|yaml|toml))`")
    for path in list((ROOT / "docs").rglob("*.md")) + list((ROOT / "agent").rglob("*.md")) + [ROOT / "README.md"]:
        if not path.exists():
            continue
        for match in pattern.finditer(read(path)):
            target = match.group(1)
            if "://" in target or target.startswith("/"):
                continue
            candidate = (path.parent / target).resolve()
            root_candidate = (ROOT / target).resolve()
            if not candidate.exists() and not root_candidate.exists():
                errors.append(f"{rel(path)}: referenced path not found: {target}")


def validate_agents_size(errors: list[str]) -> None:
    candidates = [ROOT / "AGENTS.md", ROOT / "templates" / "AGENTS.md.template"]
    for path in candidates:
        if path.exists():
            size = len(read(path).split())
            if size > 12000:
                errors.append(f"{rel(path)}: AGENTS content too large ({size} words)")


def validate_source_hashes(errors: list[str], package_root: Path | None) -> None:
    if package_root is None:
        return
    manifest = package_root / "manifest.json"
    if not manifest.exists():
        errors.append(f"{manifest}: package manifest missing")
        return
    try:
        data = json.loads(read(manifest))
    except Exception as exc:
        errors.append(f"{manifest}: invalid package manifest JSON: {exc}")
        return
    tickets = data.get("tickets", [])
    if not isinstance(tickets, list):
        errors.append(f"{manifest}: tickets must be list")
        return
    for item in tickets:
        if not isinstance(item, dict) or not item.get("path") or not item.get("sha256"):
            continue
        source = package_root / str(item["path"])
        if not source.exists():
            errors.append(f"{manifest}: ticket source missing {item['path']}")
            continue
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        if digest != item["sha256"]:
            errors.append(f"{manifest}: source hash mismatch for {item['path']}")


def validate_run_states(errors: list[str]) -> None:
    validator_path = ROOT / "tools" / "validate_run_state.py"
    namespace: dict[str, Any] = {}
    exec(compile(read(validator_path), str(validator_path), "exec"), namespace)
    validate = namespace["validate"]
    manifest = ROOT / "tests" / "fixtures" / "run_state" / "manifest.json"
    for state in sorted((ROOT / "tests" / "fixtures" / "run_state").glob("*/RUN_STATE.json")):
        state_errors, _ = validate(state, manifest if state.parent.name == "valid_full_chain" else None)
        should_be_valid = state.parent.name in {
            "valid_full_chain",
            "single_ticket_mode",
            "interrupted_post_commit_resume",
            "interrupted_review_resume",
        }
        if should_be_valid and state_errors:
            errors.append(f"{rel(state)}: expected valid run state, got {state_errors}")
        if not should_be_valid and not state_errors:
            errors.append(f"{rel(state)}: adversarial run state unexpectedly valid")


def validate_version(errors: list[str]) -> None:
    version_path = ROOT / "VERSION"
    if not version_path.exists():
        return
    version = read(version_path).strip()
    for path in [ROOT / "README.md", ROOT / "CHANGELOG.md"]:
        if not path.exists():
            continue
        matches = PUBLIC_VERSION_RE.findall(read(path))
        if matches and version not in matches:
            errors.append(f"{rel(path)}: public version claims {matches}, VERSION is {version}")


def validate_stdlib_only(errors: list[str]) -> None:
    for path in [ROOT / "tools" / "validate_workflow.py", *sorted((ROOT / "tools" / "codex_hooks").glob("*.py"))]:
        tree = ast.parse(read(path), filename=str(path))
        for node in ast.walk(tree):
            module = None
            if isinstance(node, ast.Import):
                for alias in node.names:
                    module = alias.name.split(".", 1)[0]
                    if module not in sys.stdlib_module_names and module not in {"tools"}:
                        errors.append(f"{rel(path)}: non-stdlib import {alias.name}")
            elif isinstance(node, ast.ImportFrom) and node.module:
                module = node.module.split(".", 1)[0]
                if module not in sys.stdlib_module_names and module not in {"tools", "__future__"}:
                    errors.append(f"{rel(path)}: non-stdlib import {node.module}")


def validate_adversarial_fixtures(errors: list[str]) -> None:
    required = [
        "wrong_ticket.yaml",
        "stale_state.json",
        "dirty_leakage.txt",
        "repair_loop.json",
        "premature_stop.json",
        "secret_state.json",
    ]
    base = ROOT / "tests" / "fixtures" / "workflow_validator"
    found = {path.name for path in base.rglob("*") if path.is_file()}
    for name in required:
        if name not in found:
            errors.append(f"tests/fixtures/workflow_validator: missing adversarial fixture {name}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate workflow hooks, config, tickets, state and docs.")
    parser.add_argument("--package-root", type=Path, help="Optional package root for source hash checks.")
    args = parser.parse_args()
    errors: list[str] = []
    validate_json(errors)
    validate_hooks(errors)
    validate_toml(errors)
    validate_tickets(errors)
    validate_references(errors)
    validate_agents_size(errors)
    validate_source_hashes(errors, args.package_root)
    validate_run_states(errors)
    validate_version(errors)
    validate_stdlib_only(errors)
    validate_adversarial_fixtures(errors)
    if errors:
        print("WORKFLOW VALIDATION FAILED")
        for error in errors:
            print("- " + error)
        return 1
    print("WORKFLOW VALIDATION PASSED")
    print("checks=json,hooks,toml,yaml,references,agents,tickets,source_hashes,state_transitions,version,stdlib,adversarial_fixtures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
