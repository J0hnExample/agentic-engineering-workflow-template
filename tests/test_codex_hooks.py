from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_hook(script: str, cwd: Path) -> dict:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONPATH"] = str(ROOT)
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "codex_hooks" / script)],
        cwd=cwd,
        input="{}",
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(result.stdout + result.stderr)
    return json.loads(result.stdout)


class CodexHookTests(unittest.TestCase):
    def make_repo(self, state: dict | None = None) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / ".git").mkdir()
        if state is not None:
            state_dir = root / ".git" / "agentic-workflow-controller"
            state_dir.mkdir(parents=True)
            (state_dir / "RUN_STATE.json").write_text(json.dumps(state), encoding="utf-8")
        return root

    def active_state(self) -> dict:
        return {
            "schema_version": 1,
            "status": "active",
            "package_id": "pkg-v05",
            "mode": "full_chain",
            "active_ticket_id": "TKT-10",
            "active_phase": "focused_tests_passed",
            "last_completed_ticket_id": "TKT-09",
            "source_lock": {"status": "valid", "active_ticket_id": "TKT-10"},
            "writer_lock": {},
            "continuation": {"budget_total": 3, "budget_used": 1, "last_continuation_token": "old"},
            "tickets": [
                {
                    "id": "TKT-10",
                    "phase": "focused_tests_passed",
                    "objective": "Validate hooks without leaking token_value",
                    "completed_phases": ["pending", "source_lock_validated"],
                    "scope": {"allowed_paths": ["tools/**"], "forbidden_paths": [".env", "secrets/**"]},
                    "acceptance_criteria": ["no bypass"],
                    "hard_stop_conditions": ["source lock failure"],
                    "delivery": {"pushed": False, "head_equals_upstream_proved": False},
                    "repair": {"rounds_used": 0},
                }
            ],
            "api_token": "secret-token-value",
        }

    def test_no_active_run_hooks_are_noops(self):
        root = self.make_repo()
        self.assertEqual(False, run_hook("session_start.py", root)["active_run"])
        self.assertEqual(False, run_hook("subagent_start.py", root)["active_run"])
        stop = run_hook("stop.py", root)
        self.assertFalse(stop["continue"])
        self.assertEqual("no_active_run", stop["reason"])

    def test_session_and_subagent_redact_secret_values(self):
        root = self.make_repo(self.active_state())
        session = run_hook("session_start.py", root)
        subagent = run_hook("subagent_start.py", root)
        combined = json.dumps([session, subagent])
        self.assertIn("[REDACTED]", combined)
        self.assertNotIn("secret-token-value", combined)
        self.assertNotIn(".env", combined)
        self.assertEqual("TKT-10", session["active_ticket_id"])
        self.assertEqual(["tools/**"], subagent["allowed_paths"])

    def test_stop_continues_with_progress_and_budget(self):
        root = self.make_repo(self.active_state())
        stop = run_hook("stop.py", root)
        self.assertTrue(stop["continue"])
        self.assertEqual("active_run_has_progress_and_budget", stop["reason"])
        self.assertIn("progress_token", stop)

    def test_stop_denies_no_budget(self):
        state = self.active_state()
        state["continuation"]["budget_used"] = 3
        root = self.make_repo(state)
        stop = run_hook("stop.py", root)
        self.assertFalse(stop["continue"])
        self.assertEqual("continuation_budget_exhausted", stop["reason"])

    def test_stop_denies_no_progress_token(self):
        state = self.active_state()
        root = self.make_repo(state)
        first = run_hook("stop.py", root)
        state["continuation"]["last_continuation_token"] = first["progress_token"]
        (root / ".git" / "agentic-workflow-controller" / "RUN_STATE.json").write_text(
            json.dumps(state), encoding="utf-8"
        )
        second = run_hook("stop.py", root)
        self.assertFalse(second["continue"])
        self.assertEqual("no_progress", second["reason"])

    def test_stop_denies_blocked_and_source_lock_failure(self):
        state = self.active_state()
        state["status"] = "blocked"
        self.assertEqual("terminal_state", run_hook("stop.py", self.make_repo(state))["reason"])
        state = self.active_state()
        state["source_lock"] = {"status": "failed", "active_ticket_id": "TKT-10"}
        self.assertEqual("source_lock_not_valid", run_hook("stop.py", self.make_repo(state))["reason"])


if __name__ == "__main__":
    unittest.main()
