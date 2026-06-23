from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "tools" / "validate_run_state.py"
FIXTURES = ROOT / "tests" / "fixtures" / "run_state"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_run_state", VALIDATOR)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


validator = load_validator()


class RunStateValidatorTests(unittest.TestCase):
    def validate_fixture(self, name: str):
        return validator.validate(FIXTURES / name / "RUN_STATE.json")

    def assert_valid(self, name: str, resume_phase: str | None = None):
        errors, resume = self.validate_fixture(name)
        self.assertEqual([], errors)
        if resume_phase is not None:
            self.assertEqual(resume_phase, resume.get("phase"))

    def assert_invalid(self, name: str, expected: str):
        errors, _ = self.validate_fixture(name)
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_valid_full_chain(self):
        self.assert_valid("valid_full_chain", "source_lock_validated")

    def test_single_ticket_mode(self):
        self.assert_valid("single_ticket_mode", "focused_tests_passed")

    def test_illegal_phase_skip(self):
        self.assert_invalid("illegal_phase_skip", "illegal phase skip")

    def test_out_of_order_completion(self):
        self.assert_invalid("out_of_order_completion", "completed-prefix violation")

    def test_writer_lock_contention(self):
        self.assert_invalid("writer_lock_contention", "writer-lock contention")

    def test_interrupted_review_resume(self):
        self.assert_valid("interrupted_review_resume", "self_review_completed")

    def test_interrupted_post_commit_resume(self):
        self.assert_valid("interrupted_post_commit_resume", "pushed")

    def test_post_commit_recommit_request_fails(self):
        self.assert_invalid("post_commit_recommit_request", "not recommit")

    def test_source_lock_failure(self):
        self.assert_invalid("source_lock_failure", "source-lock failure marker")

    def test_next_ticket_planning_blocked_until_previous_upstream(self):
        self.assert_invalid("next_ticket_planning_blocked", "next-ticket planning blocked")

    def test_cli_positive(self):
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), str(FIXTURES / "valid_full_chain" / "RUN_STATE.json")],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("RUN STATE VALIDATION PASSED", result.stdout)

    def test_cli_positive_with_manifest(self):
        result = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                str(FIXTURES / "valid_full_chain" / "RUN_STATE.json"),
                "--manifest",
                str(FIXTURES / "manifest.json"),
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("RUN STATE VALIDATION PASSED", result.stdout)

    def test_cli_negative(self):
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), str(FIXTURES / "writer_lock_contention" / "RUN_STATE.json")],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertNotEqual(0, result.returncode)
        self.assertIn("writer-lock contention", result.stdout)


if __name__ == "__main__":
    unittest.main()
