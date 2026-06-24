from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "tools" / "workflow_git.py"


def load_helper():
    spec = importlib.util.spec_from_file_location("workflow_git", HELPER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


workflow_git = load_helper()


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(f"git {' '.join(args)} failed\n{result.stdout}{result.stderr}")
    return result.stdout.strip()


class GitFixture:
    def __init__(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.origin = self.root / "origin.git"
        self.repo = self.root / "work"
        subprocess.run(["git", "init", "--bare", str(self.origin)], check=True, stdout=subprocess.PIPE)
        subprocess.run(["git", "clone", str(self.origin), str(self.repo)], check=True, stdout=subprocess.PIPE)
        git(self.repo, "config", "user.name", "Workflow Test")
        git(self.repo, "config", "user.email", "workflow-test@example.invalid")
        git(self.repo, "checkout", "-b", "main")
        self.write("README.md", "initial\n")
        git(self.repo, "add", "README.md")
        git(self.repo, "commit", "-m", "initial")
        git(self.repo, "push", "-u", "origin", "main")

    def cleanup(self):
        self.tmp.cleanup()

    def write(self, relative: str, content: str):
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


class WorkflowGitTests(unittest.TestCase):
    def setUp(self):
        self.fixture = GitFixture()
        self.repo = self.fixture.repo

    def tearDown(self):
        self.fixture.cleanup()

    def test_expected_dirty_suppression(self):
        self.fixture.write("notes/local.txt", "local\n")
        baseline = workflow_git.record_baseline(self.repo)
        ticket_id = "TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree"
        self.fixture.write(
            f"docs/implementation/workflow-v0.5/tickets/{ticket_id}/EXECUTION_REPORT.md",
            "report\n",
        )
        result = workflow_git.preflight(
            self.repo,
            ticket_id=ticket_id,
            allowed_paths=["src/change.txt"],
            baseline_dirty=baseline,
        )
        self.assertIn("notes/local.txt", result.suppressed_paths)
        self.assertIn(
            f"docs/implementation/workflow-v0.5/tickets/{ticket_id}/EXECUTION_REPORT.md",
            result.suppressed_paths,
        )

    def test_explicit_path_staging_excludes_unrelated_changes(self):
        self.fixture.write("src/change.txt", "change\n")
        self.fixture.write("unrelated.txt", "do not stage\n")
        ticket_id = "TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree"
        baseline = workflow_git.record_baseline(self.repo, ["unrelated.txt"])
        commands: list[list[str]] = []
        result = workflow_git.finalize_delivery(
            self.repo,
            ticket_id=ticket_id,
            allowed_paths=["src/change.txt"],
            commit_message=f"{ticket_id}: test delivery",
            baseline_dirty=baseline,
            command_log=commands,
        )
        self.assertEqual(("src/change.txt",), result.staged_paths)
        self.assertEqual("?? unrelated.txt", git(self.repo, "status", "--short", "--", "unrelated.txt"))
        self.assertIn(["git", "add", "--", "src/change.txt"], commands)
        self.assertNotIn(["git", "add", "-A"], commands)
        self.assertNotIn(["git", "add", "."], commands)

    def test_commit_push_and_upstream_equality(self):
        self.fixture.write("src/feature.txt", "feature\n")
        ticket_id = "TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree"
        result = workflow_git.finalize_delivery(
            self.repo,
            ticket_id=ticket_id,
            allowed_paths=["src/feature.txt"],
            commit_message=f"{ticket_id}: add feature",
        )
        self.assertIsNotNone(result.commit_sha)
        self.assertTrue(result.head_equals_upstream)
        self.assertEqual(git(self.repo, "rev-parse", "HEAD"), git(self.repo, "rev-parse", "origin/main"))

    def test_divergence_rejection(self):
        other = self.fixture.root / "other"
        subprocess.run(["git", "clone", str(self.fixture.origin), str(other)], check=True, stdout=subprocess.PIPE)
        git(other, "config", "user.name", "Workflow Test")
        git(other, "config", "user.email", "workflow-test@example.invalid")
        git(other, "checkout", "main")
        (other / "remote.txt").write_text("remote\n", encoding="utf-8")
        git(other, "add", "remote.txt")
        git(other, "commit", "-m", "remote change")
        git(other, "push", "origin", "main")
        git(self.repo, "fetch", "origin", "main")
        self.fixture.write("src/change.txt", "local\n")
        with self.assertRaisesRegex(workflow_git.GitDeliveryError, "upstream-diverged"):
            workflow_git.finalize_delivery(
                self.repo,
                ticket_id="TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree",
                allowed_paths=["src/change.txt"],
                commit_message="TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree: local",
            )

    def test_missing_upstream_rejection(self):
        git(self.repo, "branch", "--unset-upstream")
        with self.assertRaisesRegex(workflow_git.GitDeliveryError, "missing-upstream"):
            workflow_git.preflight(
                self.repo,
                ticket_id="TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree",
                allowed_paths=[],
            )

    def test_changed_baseline_blocker(self):
        self.fixture.write("local.txt", "first\n")
        baseline = workflow_git.record_baseline(self.repo, ["local.txt"])
        self.fixture.write("local.txt", "second\n")
        with self.assertRaisesRegex(workflow_git.GitDeliveryError, "changed baseline path"):
            workflow_git.preflight(
                self.repo,
                ticket_id="TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree",
                allowed_paths=["src/change.txt"],
                baseline_dirty=baseline,
            )

    def test_no_prohibited_git_commands_are_emitted(self):
        self.fixture.write("src/change.txt", "change\n")
        commands: list[list[str]] = []
        workflow_git.finalize_delivery(
            self.repo,
            ticket_id="TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree",
            allowed_paths=["src/change.txt"],
            commit_message="TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree: safe commands",
            command_log=commands,
        )
        rendered = [" ".join(command) for command in commands]
        prohibited = [
            "git add -A",
            "git add .",
            "git reset --hard",
            "git checkout",
            "git restore",
            "git stash",
            "git worktree",
            "git switch",
            "git push --force",
            "git push -f",
        ]
        for command in rendered:
            for bad in prohibited:
                self.assertNotIn(bad, command)

    def test_previous_ticket_managed_dirt_blocks_next_ticket(self):
        previous = "TKT-2026-06-22-aew-v05-08-review-repair-blocker-context"
        current = "TKT-2026-06-22-aew-v05-09-git-delivery-clean-worktree"
        self.fixture.write(
            f"docs/implementation/workflow-v0.5/tickets/{previous}/EXECUTION_REPORT.md",
            "previous leftover\n",
        )
        with self.assertRaisesRegex(workflow_git.GitDeliveryError, "previous-ticket managed dirt"):
            workflow_git.preflight(self.repo, ticket_id=current, allowed_paths=[])


if __name__ == "__main__":
    unittest.main()
