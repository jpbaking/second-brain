import datetime as dt
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location(
    "project_health", ROOT / "scripts" / "project_health.py"
)
project_health = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = project_health
spec.loader.exec_module(project_health)


class ProjectHealthTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for area in project_health.AREAS.values():
            (self.root / "memory" / area).mkdir(parents=True)
        self.today = dt.date(2026, 7, 28)

    def tearDown(self):
        self.temp.cleanup()

    def write(self, record_type, rid, status, body="", **overrides):
        area = project_health.AREAS[record_type]
        project = overrides.pop(
            "project", "none" if record_type in {"project", "technical-asset"} else "PRJ-alpha"
        )
        kind = overrides.pop(
            "kind",
            {
                "project": "project",
                "technical-asset": "system",
                "requirement": "functional",
                "design": "solution",
                "work-item": "epic",
                "raid": "risk",
                "release": "release",
            }[record_type],
        )
        meta = {
            "type": record_type,
            "id": rid,
            "title": rid,
            "date": "2026-07-01",
            "updated": "2026-07-28",
            "status": status,
            "owner": "Platform team",
            "project": project,
            "authority": "vault",
            "authority-ref": "memory/decisions/2026-07-01_alpha.md",
            "verified": "2026-07-28",
            "tags": "[]",
            "kind": kind,
        }
        meta.update({key.replace("_", "-"): value for key, value in overrides.items()})
        if record_type in {"project", "technical-asset"}:
            path = self.root / "memory" / area / f"{rid.lower()}.md"
        else:
            path = (
                self.root / "memory" / area / "prj-alpha" /
                f"{rid.lower()}_record.md"
            )
        path.parent.mkdir(parents=True, exist_ok=True)
        frontmatter = "\n".join(f"{key}: {value}" for key, value in meta.items())
        path.write_text(f"---\n{frontmatter}\n---\n\n# {rid}\n\n{body}\n")
        return path

    def valid_graph(self):
        ids = [
            "PRJ-alpha", "AST-core", "REQ-alpha-001", "DES-alpha-001",
            "WORK-alpha-001", "RAID-alpha-001", "REL-alpha-20260728",
        ]
        all_refs = " ".join(ids)
        self.write("project", ids[0], "active", all_refs, review_by="2026-08-01")
        self.write(
            "technical-asset", ids[1], "active", all_refs,
            project="PRJ-alpha", review_by="2026-10-01",
        )
        self.write(
            "requirement", ids[2], "draft", all_refs,
            priority="must", version="1", review_by="2026-08-01",
        )
        self.write(
            "design", ids[3], "draft", all_refs,
            version="1", review_by="2026-08-01",
        )
        self.write(
            "work-item", ids[4], "backlog", all_refs,
            priority="must", due="2026-08-15",
        )
        self.write(
            "raid", ids[5], "resolved", all_refs,
            review_by="2026-07-20", due="2026-07-20",
        )
        self.write(
            "release", ids[6], "planned", all_refs,
            window="2026-08-20T02:00Z", review_by="2026-08-10",
        )

    def test_valid_full_graph(self):
        self.valid_graph()
        result = project_health.validate(self.root, self.today)
        self.assertEqual([], result.issues)
        self.assertEqual(7, len(result.records))

    def test_closed_project_with_verified_delivery_graph(self):
        ids = [
            "PRJ-alpha", "AST-core", "REQ-alpha-001", "DES-alpha-001",
            "WORK-alpha-001", "RAID-alpha-001", "REL-alpha-20260728",
        ]
        refs = " ".join(ids)
        self.write(
            "project", ids[0], "closed", refs, review_by="2026-07-28"
        )
        self.write(
            "technical-asset", ids[1], "active", refs,
            project="PRJ-alpha", review_by="2026-10-01",
        )
        self.write(
            "requirement", ids[2], "verified",
            refs + "\n- **Verification evidence:** accepted test report",
            priority="must", version="2", review_by="2026-07-28",
        )
        self.write(
            "design", ids[3], "verified", refs,
            version="3", review_by="2026-10-01",
        )
        self.write(
            "work-item", ids[4], "verified",
            refs + "\n- **Evidence:** merged change and accepted demonstration",
            priority="must", due="2026-07-20",
        )
        self.write(
            "raid", ids[5], "resolved", refs,
            review_by="2026-07-20", due="2026-07-20",
        )
        self.write(
            "release", ids[6], "closed",
            refs + "\n- [x] all readiness gates\n- **Evidence:** observation window passed",
            window="2026-07-20T02:00Z", review_by="2026-07-28",
        )
        result = project_health.validate(self.root, self.today)
        self.assertEqual([], result.issues)
        graph = {record.id: record.refs - {record.id} for record in result.records}
        for source, targets in graph.items():
            for target in targets:
                self.assertIn(source, graph[target])

    def test_reports_missing_frontmatter(self):
        path = self.root / "memory" / "projects" / "prj-alpha.md"
        path.write_text("# no metadata\n")
        result = project_health.validate(self.root, self.today)
        self.assertTrue(any("missing YAML frontmatter" in issue for issue in result.issues))

    def test_type_mismatch_is_reported_without_crashing(self):
        path = self.write(
            "project", "PRJ-alpha", "active", "", review_by="2026-08-01"
        )
        path.write_text(path.read_text().replace("type: project", "type: unexpected"))
        result = project_health.validate(self.root, self.today)
        self.assertTrue(any("does not match memory/projects/" in x for x in result.issues))

    def test_rejects_duplicate_id(self):
        self.write("project", "PRJ-alpha", "active", review_by="2026-08-01")
        duplicate = self.root / "memory" / "projects" / "prj-other.md"
        duplicate.write_text(
            (self.root / "memory" / "projects" / "prj-alpha.md").read_text()
        )
        result = project_health.validate(self.root, self.today)
        self.assertTrue(any("duplicate ID PRJ-alpha" in issue for issue in result.issues))

    def test_rejects_invalid_state_and_path(self):
        path = self.write("requirement", "REQ-alpha-001", "finished")
        path.rename(path.with_name("wrong.md"))
        result = project_health.validate(self.root, self.today)
        self.assertTrue(any("invalid requirement status" in issue for issue in result.issues))
        self.assertTrue(any("filename must begin" in issue for issue in result.issues))

    def test_reports_dangling_and_missing_backlink(self):
        self.write(
            "project", "PRJ-alpha", "active",
            "REQ-alpha-001 REQ-alpha-999", review_by="2026-08-01",
        )
        self.write(
            "requirement", "REQ-alpha-001", "draft", "PRJ-alpha",
            priority="must", version="1", review_by="2026-08-01",
        )
        result = project_health.validate(self.root, self.today)
        self.assertTrue(any("dangling technical record reference REQ-alpha-999" in x for x in result.issues))
        self.assertFalse(any("does not link back" in x for x in result.issues))

    def test_reports_missing_reciprocal_link(self):
        self.write(
            "project", "PRJ-alpha", "active", "REQ-alpha-001 AST-core",
            review_by="2026-08-01",
        )
        self.write(
            "requirement", "REQ-alpha-001", "draft", "PRJ-alpha",
            project="PRJ-alpha", priority="must", version="1",
            review_by="2026-08-01",
        )
        self.write(
            "technical-asset", "AST-core", "active",
            "PRJ-alpha REQ-alpha-001", project="PRJ-alpha",
            review_by="2026-10-01",
        )
        result = project_health.validate(self.root, self.today)
        self.assertTrue(any("does not link back" in x for x in result.issues))

    def test_verified_requirement_requires_work_and_evidence(self):
        self.write(
            "project", "PRJ-alpha", "active", "REQ-alpha-001",
            review_by="2026-08-01",
        )
        self.write(
            "requirement", "REQ-alpha-001", "verified", "PRJ-alpha",
            priority="must", version="1", review_by="2026-08-01",
        )
        result = project_health.validate(self.root, self.today)
        self.assertTrue(any("has no WORK-* evidence" in x for x in result.issues))
        self.assertTrue(any("lacks verification evidence" in x for x in result.issues))

    def test_closed_project_rejects_open_child(self):
        self.write(
            "project", "PRJ-alpha", "closed", "WORK-alpha-001",
            review_by="2026-07-28",
        )
        self.write(
            "work-item", "WORK-alpha-001", "backlog", "PRJ-alpha",
            priority="must", due="2026-08-01",
        )
        result = project_health.validate(self.root, self.today)
        self.assertTrue(any("closed project has non-terminal" in x for x in result.issues))

    def test_stale_verification_and_overdue_review_are_warnings(self):
        self.write(
            "project", "PRJ-alpha", "active", "",
            verified="2026-05-01", review_by="2026-07-01",
        )
        result = project_health.validate(self.root, self.today)
        self.assertTrue(any("verification is stale" in x for x in result.warnings))
        self.assertTrue(any("review overdue" in x for x in result.warnings))

    def test_unassigned_owner_is_warning(self):
        self.write(
            "project", "PRJ-alpha", "active", "", owner="unassigned",
            review_by="2026-08-01",
        )
        result = project_health.validate(self.root, self.today)
        self.assertTrue(any("owner is unassigned" in x for x in result.warnings))

    def test_release_gates_are_enforced(self):
        self.write(
            "project", "PRJ-alpha", "active", "REL-alpha-20260728",
            review_by="2026-08-01",
        )
        self.write(
            "release", "REL-alpha-20260728", "approved",
            "PRJ-alpha\n- [ ] readiness is incomplete",
            window="2026-08-01T02:00Z", review_by="2026-08-01",
        )
        result = project_health.validate(self.root, self.today)
        self.assertTrue(any("has no WORK-* trace" in x for x in result.issues))
        self.assertTrue(any("has no AST-* trace" in x for x in result.issues))
        self.assertTrue(any("unchecked readiness gates" in x for x in result.issues))

    def test_project_scoped_id_must_match_project(self):
        path = self.write(
            "requirement", "REQ-beta-001", "draft", "PRJ-alpha",
            priority="must", version="1", review_by="2026-08-01",
        )
        result = project_health.validate(self.root, self.today)
        self.assertTrue(any("ID project scope" in x for x in result.issues))
        self.assertIn("prj-alpha", path.as_posix())


if __name__ == "__main__":
    unittest.main()
