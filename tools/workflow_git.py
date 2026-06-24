from __future__ import annotations

import argparse
import dataclasses
import fnmatch
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Iterable, Sequence


class GitDeliveryError(RuntimeError):
    def __init__(self, code: str, facts: Sequence[str]):
        self.code = code
        self.facts = list(facts)
        super().__init__(f"{code}: {'; '.join(self.facts)}")


@dataclasses.dataclass(frozen=True)
class PathIdentity:
    state: str
    size: int | None = None
    sha256: str | None = None


@dataclasses.dataclass(frozen=True)
class GitPolicy:
    branch: str = "main"
    remote: str = "origin"
    upstream: str = "origin/main"
    auto_commit: bool = True
    auto_push: bool = True
    explicit_staging_only: bool = True


@dataclasses.dataclass(frozen=True)
class PreflightResult:
    branch: str
    head: str
    upstream_ref: str
    upstream_sha: str
    dirty_paths: tuple[str, ...]
    suppressed_paths: tuple[str, ...]
    scoped_dirty_paths: tuple[str, ...]


@dataclasses.dataclass(frozen=True)
class DeliveryResult:
    ticket_id: str
    branch: str
    baseline_head: str
    upstream_ref: str
    staged_paths: tuple[str, ...]
    commit_sha: str | None
    push_remote: str | None
    push_branch: str | None
    upstream_sha: str
    head_equals_upstream: bool


PROHIBITED_COMMAND_MARKERS = (
    ("add", "-A"),
    ("add", "."),
    ("reset", "--hard"),
    ("checkout",),
    ("restore",),
    ("stash",),
    ("worktree",),
    ("switch",),
    ("branch",),
    ("push", "--force"),
    ("push", "-f"),
)


AUTHORIZED_WORKFLOW_PATTERNS = (
    "tickets/upgrades/*/TKT-*.yaml",
    "tickets/templates/*",
    "docs/implementation/workflow-*/CONTEXT_LEDGER.md",
    "docs/implementation/workflow-*/tickets/TKT-*/*",
    "agent/*.md",
)


def run_git(
    repo: Path | str,
    args: Sequence[str],
    *,
    check: bool = True,
    command_log: list[list[str]] | None = None,
) -> subprocess.CompletedProcess[str]:
    command = ["git", *args]
    _reject_prohibited_command(command)
    if command_log is not None:
        command_log.append(command)
    result = subprocess.run(
        command,
        cwd=Path(repo),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode != 0:
        raise GitDeliveryError(
            "git-command-failed",
            [f"command={' '.join(command)}", f"stderr={result.stderr.strip()}"],
        )
    return result


def _reject_prohibited_command(command: Sequence[str]) -> None:
    args = tuple(command[1:] if command and command[0] == "git" else command)
    for marker in PROHIBITED_COMMAND_MARKERS:
        if _contains_marker(args, marker):
            raise GitDeliveryError("prohibited-git-command", [f"command={' '.join(command)}"])


def _contains_marker(args: Sequence[str], marker: Sequence[str]) -> bool:
    if not marker:
        return False
    if len(marker) == 1:
        return marker[0] in args
    return any(tuple(args[index : index + len(marker)]) == tuple(marker) for index in range(len(args)))


def current_branch(repo: Path | str, command_log: list[list[str]] | None = None) -> str:
    return run_git(repo, ["rev-parse", "--abbrev-ref", "HEAD"], command_log=command_log).stdout.strip()


def rev_parse(repo: Path | str, rev: str, command_log: list[list[str]] | None = None) -> str:
    return run_git(repo, ["rev-parse", rev], command_log=command_log).stdout.strip()


def upstream_ref(repo: Path | str, command_log: list[list[str]] | None = None) -> str:
    result = run_git(
        repo,
        ["rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"],
        check=False,
        command_log=command_log,
    )
    if result.returncode != 0:
        raise GitDeliveryError("missing-upstream", ["current branch has no upstream"])
    return result.stdout.strip()


def status_paths(repo: Path | str, command_log: list[list[str]] | None = None) -> tuple[str, ...]:
    output = run_git(repo, ["status", "--porcelain=v1", "--untracked-files=all"], command_log=command_log).stdout
    paths: list[str] = []
    for line in output.splitlines():
        if not line:
            continue
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        paths.append(path.strip('"'))
    return tuple(sorted(set(paths)))


def staged_paths(repo: Path | str, command_log: list[list[str]] | None = None) -> tuple[str, ...]:
    output = run_git(repo, ["diff", "--cached", "--name-only"], command_log=command_log).stdout
    return tuple(sorted(path for path in output.splitlines() if path))


def content_identity(repo: Path | str, path: str) -> PathIdentity:
    full_path = Path(repo) / path
    if not full_path.exists():
        return PathIdentity("missing")
    if full_path.is_dir():
        return PathIdentity("directory")
    data = full_path.read_bytes()
    return PathIdentity("file", len(data), hashlib.sha256(data).hexdigest())


def record_baseline(repo: Path | str, paths: Iterable[str] | None = None) -> dict[str, PathIdentity]:
    selected = tuple(paths) if paths is not None else status_paths(repo)
    return {path: content_identity(repo, path) for path in selected}


def _match_any(path: str, patterns: Iterable[str]) -> bool:
    return any(fnmatch.fnmatch(path, pattern) for pattern in patterns)


def is_authorized_workflow_artifact(path: str, ticket_id: str) -> bool:
    if not _match_any(path, AUTHORIZED_WORKFLOW_PATTERNS):
        return False
    if path.startswith("docs/implementation/") and "/tickets/TKT-" in path:
        return f"/tickets/{ticket_id}/" in path
    if path.startswith("tickets/upgrades/") and path.endswith(".yaml"):
        return path.endswith(f"{ticket_id}.yaml")
    return True


def is_scoped(path: str, allowed_paths: Iterable[str]) -> bool:
    for allowed in allowed_paths:
        allowed = allowed.rstrip("/")
        if allowed.endswith("/**"):
            prefix = allowed[:-3].rstrip("/") + "/"
            if path.startswith(prefix):
                return True
        elif path == allowed or path.startswith(allowed + "/"):
            return True
    return False


def preflight(
    repo: Path | str,
    *,
    ticket_id: str,
    allowed_paths: Sequence[str],
    baseline_dirty: dict[str, PathIdentity] | None = None,
    policy: GitPolicy = GitPolicy(),
    command_log: list[list[str]] | None = None,
) -> PreflightResult:
    branch = current_branch(repo, command_log)
    if branch != policy.branch:
        raise GitDeliveryError("wrong-branch", [f"expected={policy.branch}", f"actual={branch}"])

    head = rev_parse(repo, "HEAD", command_log)
    upstream = upstream_ref(repo, command_log)
    if upstream != policy.upstream:
        raise GitDeliveryError("wrong-upstream", [f"expected={policy.upstream}", f"actual={upstream}"])
    upstream_sha = rev_parse(repo, upstream, command_log)
    if head != upstream_sha:
        raise GitDeliveryError("upstream-diverged", [f"HEAD={head}", f"{upstream}={upstream_sha}"])

    baseline_dirty = baseline_dirty or {}
    dirty = status_paths(repo, command_log)
    blockers: list[str] = []
    suppressed: list[str] = []
    scoped: list[str] = []
    for path in dirty:
        in_scope = is_scoped(path, allowed_paths)
        if path in baseline_dirty:
            if content_identity(repo, path) != baseline_dirty[path]:
                blockers.append(f"changed baseline path: {path}")
            elif in_scope:
                blockers.append(f"baseline path overlaps active scope: {path}")
            else:
                suppressed.append(path)
            continue
        if in_scope:
            scoped.append(path)
            continue
        if is_authorized_workflow_artifact(path, ticket_id):
            suppressed.append(path)
            continue
        if _match_any(path, AUTHORIZED_WORKFLOW_PATTERNS):
            blockers.append(f"previous-ticket managed dirt: {path}")
        else:
            blockers.append(f"unrelated dirty path: {path}")
    if blockers:
        raise GitDeliveryError("dirty-worktree-blocker", blockers)
    return PreflightResult(branch, head, upstream, upstream_sha, dirty, tuple(suppressed), tuple(scoped))


def finalize_delivery(
    repo: Path | str,
    *,
    ticket_id: str,
    allowed_paths: Sequence[str],
    commit_message: str,
    baseline_dirty: dict[str, PathIdentity] | None = None,
    policy: GitPolicy = GitPolicy(),
    command_log: list[list[str]] | None = None,
) -> DeliveryResult:
    before = preflight(
        repo,
        ticket_id=ticket_id,
        allowed_paths=allowed_paths,
        baseline_dirty=baseline_dirty,
        policy=policy,
        command_log=command_log,
    )
    preexisting_staged = staged_paths(repo, command_log)
    unrelated_staged = [path for path in preexisting_staged if not is_scoped(path, allowed_paths)]
    if unrelated_staged:
        raise GitDeliveryError("staged-unrelated-paths", unrelated_staged)

    run_git(repo, ["add", "--", *allowed_paths], command_log=command_log)
    staged = staged_paths(repo, command_log)
    out_of_scope = [path for path in staged if not is_scoped(path, allowed_paths)]
    if out_of_scope:
        raise GitDeliveryError("staged-unrelated-paths", out_of_scope)
    if not staged:
        return DeliveryResult(
            ticket_id=ticket_id,
            branch=before.branch,
            baseline_head=before.head,
            upstream_ref=before.upstream_ref,
            staged_paths=(),
            commit_sha=None,
            push_remote=None,
            push_branch=None,
            upstream_sha=before.upstream_sha,
            head_equals_upstream=True,
        )

    run_git(repo, ["commit", "-m", commit_message], command_log=command_log)
    commit_sha = rev_parse(repo, "HEAD", command_log)
    run_git(repo, ["push", policy.remote, f"HEAD:{policy.branch}"], command_log=command_log)
    upstream_sha = rev_parse(repo, policy.upstream, command_log)
    head_sha = rev_parse(repo, "HEAD", command_log)
    equal = head_sha == upstream_sha
    if not equal:
        raise GitDeliveryError("post-push-sha-mismatch", [f"HEAD={head_sha}", f"{policy.upstream}={upstream_sha}"])
    return DeliveryResult(
        ticket_id=ticket_id,
        branch=before.branch,
        baseline_head=before.head,
        upstream_ref=before.upstream_ref,
        staged_paths=staged,
        commit_sha=commit_sha,
        push_remote=policy.remote,
        push_branch=policy.branch,
        upstream_sha=upstream_sha,
        head_equals_upstream=equal,
    )


def _identity_to_json(identity: PathIdentity) -> dict[str, object]:
    return dataclasses.asdict(identity)


def _identity_from_json(data: dict[str, object]) -> PathIdentity:
    return PathIdentity(
        state=str(data["state"]),
        size=data.get("size") if data.get("size") is None else int(data["size"]),
        sha256=data.get("sha256") if data.get("sha256") is None else str(data["sha256"]),
    )


def _load_baseline(path: str | None) -> dict[str, PathIdentity]:
    if not path:
        return {}
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return {item_path: _identity_from_json(value) for item_path, value in data.items()}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Workflow Git delivery helper")
    subparsers = parser.add_subparsers(dest="command", required=True)

    baseline_parser = subparsers.add_parser("baseline")
    baseline_parser.add_argument("--repo", default=".")

    preflight_parser = subparsers.add_parser("preflight")
    preflight_parser.add_argument("--repo", default=".")
    preflight_parser.add_argument("--ticket-id", required=True)
    preflight_parser.add_argument("--allowed-path", action="append", required=True)
    preflight_parser.add_argument("--baseline-json")

    finalize_parser = subparsers.add_parser("finalize")
    finalize_parser.add_argument("--repo", default=".")
    finalize_parser.add_argument("--ticket-id", required=True)
    finalize_parser.add_argument("--allowed-path", action="append", required=True)
    finalize_parser.add_argument("--message", required=True)
    finalize_parser.add_argument("--baseline-json")

    args = parser.parse_args(argv)
    try:
        if args.command == "baseline":
            baseline = record_baseline(args.repo)
            print(json.dumps({path: _identity_to_json(value) for path, value in baseline.items()}, indent=2, sort_keys=True))
        elif args.command == "preflight":
            result = preflight(
                args.repo,
                ticket_id=args.ticket_id,
                allowed_paths=args.allowed_path,
                baseline_dirty=_load_baseline(args.baseline_json),
            )
            print(json.dumps(dataclasses.asdict(result), indent=2, sort_keys=True))
        elif args.command == "finalize":
            result = finalize_delivery(
                args.repo,
                ticket_id=args.ticket_id,
                allowed_paths=args.allowed_path,
                commit_message=args.message,
                baseline_dirty=_load_baseline(args.baseline_json),
            )
            print(json.dumps(dataclasses.asdict(result), indent=2, sort_keys=True))
        return 0
    except GitDeliveryError as error:
        print(json.dumps({"blocker": error.code, "facts": error.facts}, indent=2, sort_keys=True))
        return 2


if __name__ == "__main__":
    sys.exit(main())
