#!/usr/bin/env python3
"""Validate staged vault changes. Standard-library Python plus Git only."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def git(*args, check=True):
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=check, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, text=False,
    )


def staged_paths():
    raw = git("diff", "--cached", "--name-status", "-z", "--find-renames").stdout
    fields = raw.split(b"\0")
    result = []
    i = 0
    while i < len(fields) and fields[i]:
        status = fields[i].decode("ascii", "replace")
        i += 1
        old = fields[i].decode("utf-8", "surrogateescape")
        i += 1
        new = None
        if status[0] in "RC":
            new = fields[i].decode("utf-8", "surrogateescape")
            i += 1
        result.append((status, old, new))
    return result


def blob(spec):
    proc = git("show", spec, check=False)
    return proc.stdout if proc.returncode == 0 else None


def validate_history(changes):
    errors = []
    for status, old, new in changes:
        code = status[0]
        if old.startswith("library/") and not old.endswith("catalog.md"):
            if code == "D":
                errors.append(f"tracked library original deleted: {old}")
            elif code == "M":
                errors.append(f"tracked library original modified: {old}")
            elif code in "RC":
                destination = new or ""
                if not destination.startswith("library/") or destination.endswith("catalog.md"):
                    errors.append(f"library original moved outside its protected area: {old} -> {destination}")
                elif blob(f"HEAD:{old}") != blob(f":{destination}"):
                    errors.append(f"library rename changed file content: {old} -> {destination}")

    if any((new or old) == "memory/log.md" for _, old, new in changes):
        previous = blob("HEAD:memory/log.md") or b""
        staged = blob(":memory/log.md")
        if staged is None or not staged.startswith(previous):
            errors.append("memory/log.md is append-only; staged content changed existing history")
    return errors


def main():
    try:
        changes = staged_paths()
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"VALIDATION FAILED: cannot inspect staged changes: {exc}", file=sys.stderr)
        return 2
    if not changes:
        print("VALIDATION FAILED: no staged changes")
        return 1

    errors = validate_history(changes)
    touched_vault = any(
        (new or old).startswith(("library/", "memory/"))
        or (new or old) in {"library/catalog.md", "memory/index.md"}
        for _, old, new in changes
    )
    touched_project_model = any(
        (new or old).startswith(
            (
                "rules/shared/",
                "skills/shared/",
                ".agents/skills/",
                ".claude/skills/",
                "scripts/project_health.py",
                "tests/test_project_health.py",
            )
        )
        for _, old, new in changes
    )
    if touched_vault or touched_project_model:
        health = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "health.py")], cwd=ROOT,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
        )
        print(health.stdout, end="")
        if "Vault healthy: no mechanical issues found." not in health.stdout:
            errors.append("vault health check reported mechanical issues")

    if errors:
        print("\nVALIDATION FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Staged changes valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
