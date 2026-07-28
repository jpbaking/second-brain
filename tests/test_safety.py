import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load(ROOT / "scripts" / "validate_commit.py", "validator")


class HookTests(unittest.TestCase):
    def invoke(self, payload):
        proc = subprocess.run(
            [sys.executable, str(ROOT / ".clinerules/hooks/PreToolUse")],
            input=json.dumps(payload), text=True, capture_output=True, check=True,
        )
        return json.loads(proc.stdout)

    def test_blocks_direct_library_edit(self):
        out = self.invoke({"toolName": "edit_file", "parameters": {"path": "library/2026/a.pdf"}})
        self.assertTrue(out["cancel"])

    def test_blocks_obvious_shell_deletion(self):
        out = self.invoke({"toolName": "execute_command", "parameters": {"command": "rm library/2026/a.pdf"}})
        self.assertTrue(out["cancel"])

    def test_allows_library_move(self):
        out = self.invoke({"toolName": "execute_command", "parameters": {"command": "mv inbox/a.pdf library/2026/a.pdf"}})
        self.assertFalse(out["cancel"])

    def test_allows_catalog_edit(self):
        out = self.invoke({"toolName": "edit_file", "parameters": {"path": "library/2026/catalog.md"}})
        self.assertFalse(out["cancel"])


class ValidatorTests(unittest.TestCase):
    def test_rejects_modified_original(self):
        self.assertIn(
            "tracked library original modified: library/2026/a.pdf",
            validator.validate_history([("M", "library/2026/a.pdf", None)]),
        )

    def test_allows_new_original(self):
        self.assertEqual([], validator.validate_history([("A", "library/2026/a.pdf", None)]))

    def test_health_validation_uses_staged_snapshot(self):
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp) / "repo"
            shutil.copytree(
                ROOT,
                repo,
                ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
            )
            fixture_paths = [
                str(path.relative_to(repo))
                for path in repo.rglob("*")
                if path.is_file() or path.is_symlink()
            ]

            def run(*args, check=True):
                return subprocess.run(
                    args, cwd=repo, text=True, capture_output=True, check=check,
                )

            run("git", "init", "-q")
            run("git", "add", "--", *fixture_paths)
            run(
                "git", "-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                "commit", "-qm", "fixture",
            )

            project_health = repo / "scripts" / "project_health.py"
            valid_content = project_health.read_text()
            project_health.write_text("this is invalid Python\n" + valid_content)
            run("git", "add", "scripts/project_health.py")
            run("git", "restore", "--source=HEAD", "--worktree", "scripts/project_health.py")

            result = run(
                sys.executable, "scripts/validate_commit.py", check=False,
            )
            self.assertNotEqual(0, result.returncode)
            self.assertIn(
                "staged vault health check reported mechanical issues",
                result.stdout,
            )


if __name__ == "__main__":
    unittest.main()
