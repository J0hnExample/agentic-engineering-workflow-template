from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "validate_workflow.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_workflow", VALIDATOR)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


validator = load_validator()


class WorkflowValidatorTests(unittest.TestCase):
    def test_cli_passes_repository(self):
        result = subprocess.run(
            [sys.executable, str(VALIDATOR)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("WORKFLOW VALIDATION PASSED", result.stdout)
        self.assertIn("hooks", result.stdout)

    def test_hooks_validator_rejects_wrong_event_shape(self):
        errors: list[str] = []
        path = ROOT / "tests" / "fixtures" / "workflow_validator" / "bad_hooks" / "hooks.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertNotIn("hooks", data)
        original = validator.read
        try:
            validator.read = lambda requested: path.read_text(encoding="utf-8") if requested.name == "hooks.json" else original(requested)
            validator.validate_hooks(errors)
        finally:
            validator.read = original
        self.assertTrue(any("top-level object must contain only a hooks object" in error for error in errors), errors)

    def test_hooks_validator_accepts_official_hooks_wrapper(self):
        errors: list[str] = []
        validator.validate_hooks(errors)
        self.assertFalse(any(".codex/hooks.json" in error for error in errors), errors)

    def test_ticket_validator_rejects_wrong_ticket_id(self):
        errors: list[str] = []
        path = ROOT / "tests" / "fixtures" / "workflow_validator" / "bad_ticket" / "wrong_ticket.yaml"
        keys = validator.simple_yaml_top_keys(path)
        self.assertIn("id", keys)
        self.assertNotIn("TKT-actual", path.name)

    def test_source_hash_validator_detects_mismatch(self):
        with tempfile.TemporaryDirectory() as temp:
            package = Path(temp)
            (package / "tickets").mkdir()
            ticket = package / "tickets" / "TKT.yaml"
            ticket.write_text("id: TKT\n", encoding="utf-8")
            (package / "manifest.json").write_text(
                json.dumps({"tickets": [{"path": "tickets/TKT.yaml", "sha256": "bad"}]}),
                encoding="utf-8",
            )
            errors: list[str] = []
            validator.validate_source_hashes(errors, package)
            self.assertTrue(any("source hash mismatch" in error for error in errors), errors)

    def test_adversarial_fixture_inventory(self):
        errors: list[str] = []
        validator.validate_adversarial_fixtures(errors)
        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
