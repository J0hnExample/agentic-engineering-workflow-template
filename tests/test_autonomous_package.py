from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "tools" / "build_autonomous_package.py"
VALIDATE = ROOT / "tools" / "validate_autonomous_package.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


builder = load_module("build_autonomous_package", BUILD)
validator = load_module("validate_autonomous_package", VALIDATE)


def request(ticket_count: int = 1) -> dict:
    tickets = []
    for index in range(ticket_count):
        tid = f"TKT-2026-01-0{index + 1}-generic-ticket-{index + 1}"
        tickets.append(
            {
                "id": tid,
                "order": index,
                "title": f"Generic ticket {index + 1}",
                "objective": f"Implement generic scoped outcome {index + 1}.",
                "depends_on": [] if index == 0 else [tickets[index - 1]["id"]],
                "allowed_paths": ["src/**", "tests/**"],
                "forbidden_paths": [".env", ".git/**"],
                "acceptance_criteria": ["The scoped behavior is implemented."],
                "required_tests": ["Run the focused unit tests."],
                "required_evidence": ["Record changed files and test output."],
                "stop_conditions": ["Stop if scope expands."],
                "delivery": {"assigned": True, "require_push": True},
            }
        )
    return {
        "package_id": f"GENERIC-AUTONOMOUS-PACKAGE-{ticket_count}",
        "target_repository": "ExampleOrg/example-repository",
        "target_branch": "main",
        "goal": "Deliver a generic software change.",
        "context": "Current repository evidence is authoritative.",
        "constraints": "Use serial execution and preserve unrelated work.",
        "done": "All acceptance criteria and proof gates are recorded.",
        "tickets": tickets,
    }


class AutonomousPackageTests(unittest.TestCase):
    def build_fixture(self, ticket_count: int = 1):
        temp = tempfile.TemporaryDirectory()
        base = Path(temp.name)
        request_path = base / "request.json"
        package_root = base / "package"
        zip_path = base / "package.zip"
        request_path.write_text(json.dumps(request(ticket_count), indent=2), encoding="utf-8")
        root, zip_file, manifest = builder.build(request_path, package_root, zip_path)
        self.addCleanup(temp.cleanup)
        return root, zip_file, manifest

    def test_single_ticket_build_and_validate(self):
        root, zip_file, manifest = self.build_fixture(1)
        self.assertTrue(zip_file.is_file())
        self.assertEqual(1, len(manifest["tickets"]))
        by_path = {entry["path"]: entry for entry in manifest["files"]}
        self.assertIn("sha256", by_path["VALIDATION_REPORT.md"])
        self.assertEqual([], validator.validate(root))
        ticket = manifest["tickets"][0]
        self.assertEqual([], validator.validate(root, ticket["id"], (root / ticket["path"]).resolve()))

    def test_multi_ticket_build_and_validate(self):
        root, zip_file, manifest = self.build_fixture(3)
        self.assertTrue(zip_file.is_file())
        self.assertEqual(3, len(manifest["tickets"]))
        self.assertEqual(
            [[], [manifest["tickets"][0]["id"]], [manifest["tickets"][1]["id"]]],
            [ticket["depends_on"] for ticket in manifest["tickets"]],
        )
        self.assertEqual([], validator.validate(root))

    def test_mutation_failure(self):
        root, _, _ = self.build_fixture(1)
        (root / "README.md").write_text("mutated\n", encoding="utf-8")
        self.assertTrue(any("hash mismatch: README.md" in error for error in validator.validate(root)))

    def test_missing_file_failure(self):
        root, _, _ = self.build_fixture(1)
        (root / "REQUEST.md").unlink()
        self.assertTrue(any("declared files missing" in error for error in validator.validate(root)))

    def test_missing_sha_failure(self):
        root, _, manifest = self.build_fixture(1)
        manifest["files"][0].pop("sha256", None)
        (root / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
        self.assertTrue(any("missing sha256" in error for error in validator.validate(root)))

    def test_duplicate_id_failure(self):
        root, _, manifest = self.build_fixture(2)
        manifest["tickets"][1]["id"] = manifest["tickets"][0]["id"]
        (root / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
        self.assertTrue(any("duplicate ticket id" in error for error in validator.validate(root)))

    def test_out_of_order_dependency_failure(self):
        root, _, manifest = self.build_fixture(2)
        manifest["tickets"][0]["depends_on"] = [manifest["tickets"][1]["id"]]
        manifest["dependency_graph"][0]["depends_on"] = [manifest["tickets"][1]["id"]]
        (root / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
        self.assertTrue(any("depends on missing/later" in error for error in validator.validate(root)))

    def test_dependency_graph_drift_failure(self):
        root, _, manifest = self.build_fixture(2)
        manifest["dependency_graph"][1]["depends_on"] = []
        (root / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
        self.assertTrue(any("dependency graph order" in error for error in validator.validate(root)))

    def test_repository_ticket_substitution_failure(self):
        root, _, manifest = self.build_fixture(1)
        ticket = manifest["tickets"][0]
        with tempfile.TemporaryDirectory() as temp:
            repo_ticket = Path(temp) / Path(ticket["path"]).name
            shutil.copy2(root / ticket["path"], repo_ticket)
            errors = validator.validate(root, ticket["id"], repo_ticket.resolve())
        self.assertTrue(any("outside package root" in error for error in errors))

    def test_generated_fixture_has_generic_language(self):
        root, _, _ = self.build_fixture(2)
        forbidden = ["RL Trainer", "Rocket League", "J0hnExample", "aew-v05", "v0.5"]
        hits = []
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() not in {".zip"}:
                text = path.read_text(encoding="utf-8", errors="ignore")
                for word in forbidden:
                    if word in text:
                        hits.append(f"{path.relative_to(root)}:{word}")
        self.assertEqual([], hits)


if __name__ == "__main__":
    unittest.main()
