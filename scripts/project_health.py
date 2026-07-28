#!/usr/bin/env python3
"""Validate the technical project-management source of truth.

Standard-library only. The module is importable by tests and scripts/health.py.
Templates and indexes define the model but are not treated as live records.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from dataclasses import dataclass, field
from pathlib import Path


AREAS = {
    "project": "projects",
    "technical-asset": "technical-assets",
    "requirement": "requirements",
    "design": "designs",
    "work-item": "work-items",
    "raid": "raid",
    "release": "releases",
}

ID_PATTERNS = {
    "project": re.compile(r"^PRJ-([a-z0-9][a-z0-9-]*)$"),
    "technical-asset": re.compile(r"^AST-([a-z0-9][a-z0-9-]*)$"),
    "requirement": re.compile(r"^REQ-([a-z0-9][a-z0-9-]*?)-(\d{3})$"),
    "design": re.compile(r"^DES-([a-z0-9][a-z0-9-]*?)-(\d{3})$"),
    "work-item": re.compile(r"^WORK-([a-z0-9][a-z0-9-]*?)-(\d{3})$"),
    "raid": re.compile(r"^RAID-([a-z0-9][a-z0-9-]*?)-(\d{3})$"),
    "release": re.compile(
        r"^REL-([a-z0-9][a-z0-9-]*?)-(\d{8})(?:-(\d+))?$"
    ),
}

KINDS = {
    "project": {"project", "programme", "initiative"},
    "technical-asset": {
        "domain", "system", "service", "component", "api", "data-store",
        "infrastructure", "environment", "ui-surface",
    },
    "requirement": {
        "business", "user", "functional", "non-functional", "technical",
        "security", "operational", "ui", "ux",
    },
    "design": {
        "product", "solution", "software", "api", "data", "infrastructure",
        "security", "ui", "ux",
    },
    "work-item": {"outcome", "workstream", "epic", "feature", "task"},
    "raid": {"risk", "assumption", "issue", "dependency"},
    "release": {"release", "migration", "infrastructure-change", "experiment"},
}

STATUSES = {
    "project": {"proposed", "active", "on-hold", "closing", "closed", "cancelled"},
    "technical-asset": {"planned", "active", "deprecated", "retired"},
    "requirement": {
        "draft", "proposed", "approved", "implemented", "verified", "retired",
        "rejected", "superseded",
    },
    "design": {
        "draft", "in-review", "approved", "implemented", "verified",
        "rejected", "superseded", "retired",
    },
    "work-item": {
        "backlog", "ready", "in-progress", "blocked", "done", "verified",
        "cancelled",
    },
    "raid": {"open", "monitoring", "mitigating", "resolved", "accepted", "closed"},
    "release": {
        "planned", "ready", "approved", "deploying", "deployed", "verified",
        "closed", "rolled-back", "cancelled",
    },
}

TERMINAL = {
    "project": {"closed", "cancelled"},
    "technical-asset": {"retired"},
    "requirement": {"verified", "retired", "rejected", "superseded"},
    "design": {"verified", "rejected", "superseded", "retired"},
    "work-item": {"verified", "cancelled"},
    "raid": {"resolved", "accepted", "closed"},
    "release": {"closed", "rolled-back", "cancelled"},
}

COMMON_FIELDS = {
    "type", "id", "title", "date", "updated", "status", "owner", "project",
    "authority", "authority-ref", "verified", "tags", "kind",
}

TYPE_FIELDS = {
    "project": {"review-by"},
    "technical-asset": {"review-by"},
    "requirement": {"priority", "version", "review-by"},
    "design": {"version", "review-by"},
    "work-item": {"priority", "due"},
    "raid": {"review-by", "due"},
    "release": {"window", "review-by"},
}

ID_REF_RE = re.compile(
    r"\b(?:PRJ|AST|REQ|DES|WORK|RAID|REL)-[A-Za-z0-9][A-Za-z0-9-]*"
)
PLACEHOLDER_RE = re.compile(
    r"\{\{|YYYY|stable-slug|project-NNN|unknown|unassigned|none|TBD",
    re.IGNORECASE,
)


@dataclass
class Record:
    path: Path
    meta: dict[str, str]
    text: str
    refs: set[str]

    @property
    def id(self) -> str:
        return self.meta.get("id", "")

    @property
    def type(self) -> str:
        return self.meta.get("type", "")

    @property
    def status(self) -> str:
        return self.meta.get("status", "")


@dataclass
class Result:
    records: list[Record] = field(default_factory=list)
    issues: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def parse_date(value: str) -> dt.date | None:
    try:
        return dt.date.fromisoformat(value)
    except (TypeError, ValueError):
        return None


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str, list[str]]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, text, ["missing YAML frontmatter"]
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text, ["unterminated YAML frontmatter"]
    raw = text[4:end]
    meta: dict[str, str] = {}
    for number, line in enumerate(raw.splitlines(), 2):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[:1].isspace() or ":" not in line:
            errors.append(f"unsupported frontmatter syntax on line {number}")
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key in meta:
            errors.append(f"duplicate frontmatter key: {key}")
        meta[key] = value.strip("\"'")
    return meta, text[end + 5 :], errors


def collect_records(root: Path) -> Result:
    result = Result()
    memory = root / "memory"
    for record_type, area_name in AREAS.items():
        area = memory / area_name
        if not area.exists():
            result.issues.append(f"missing technical record area: memory/{area_name}/")
            continue
        for path in sorted(area.rglob("*.md")):
            if path.name in {"index.md", "_template.md"}:
                continue
            meta, body, errors = parse_frontmatter(path)
            rel = path.relative_to(root)
            for error in errors:
                result.issues.append(f"{rel}: {error}")
            if errors:
                continue
            declared_type = meta.get("type")
            if declared_type != record_type:
                result.issues.append(
                    f"{rel}: type {declared_type or '<missing>'!r} does not "
                    f"match memory/{area_name}/ ({record_type})"
                )
                meta["_declared-type"] = declared_type or ""
                meta["type"] = record_type
            refs = set(ID_REF_RE.findall(body))
            project = meta.get("project", "")
            if ID_REF_RE.fullmatch(project):
                refs.add(project)
            result.records.append(Record(path, meta, body, refs))
    return result


def _relative(record: Record, root: Path) -> str:
    return record.path.relative_to(root).as_posix()


def _real_field(record: Record, label: str) -> bool:
    pattern = re.compile(rf"(?im)^\s*[-*]?\s*\*{{0,2}}{re.escape(label)}\*{{0,2}}\s*:\s*(.+)$")
    match = pattern.search(record.text)
    return bool(match and not PLACEHOLDER_RE.search(match.group(1)))


def _validate_path(record: Record, root: Path, issues: list[str]) -> None:
    rel = record.path.relative_to(root / "memory")
    rid = record.id.lower()
    if record.type in {"project", "technical-asset"}:
        expected = Path(AREAS[record.type]) / f"{rid}.md"
        if rel != expected:
            issues.append(f"{_relative(record, root)}: canonical path is memory/{expected}")
        return
    project = record.meta.get("project", "")
    project_slug = project.removeprefix("PRJ-").lower()
    expected_parent = Path(AREAS[record.type]) / f"prj-{project_slug}"
    if rel.parent != expected_parent:
        issues.append(
            f"{_relative(record, root)}: project-scoped record belongs under "
            f"memory/{expected_parent}/"
        )
    if not (record.path.stem == rid or record.path.stem.startswith(rid + "_")):
        issues.append(f"{_relative(record, root)}: filename must begin with {rid}")


def _validate_schema(
    record: Record, root: Path, today: dt.date, result: Result
) -> None:
    rel = _relative(record, root)
    required_fields = COMMON_FIELDS | TYPE_FIELDS.get(record.type, set())
    missing = sorted(field for field in required_fields if field not in record.meta)
    if missing:
        result.issues.append(f"{rel}: missing frontmatter fields: {', '.join(missing)}")

    pattern = ID_PATTERNS.get(record.type)
    match = pattern.fullmatch(record.id) if pattern else None
    if not match:
        result.issues.append(f"{rel}: invalid {record.type} ID {record.id!r}")
    if record.meta.get("status") not in STATUSES.get(record.type, set()):
        result.issues.append(
            f"{rel}: invalid {record.type} status {record.meta.get('status')!r}"
        )
    if record.meta.get("kind") not in KINDS.get(record.type, set()):
        result.issues.append(
            f"{rel}: invalid {record.type} kind {record.meta.get('kind')!r}"
        )
    if record.meta.get("authority") not in {"vault", "external"}:
        result.issues.append(f"{rel}: authority must be vault or external")
    if PLACEHOLDER_RE.search(record.meta.get("authority-ref", "")):
        result.issues.append(f"{rel}: authority-ref is missing or still a placeholder")

    dates: dict[str, dt.date] = {}
    for field_name in ("date", "updated", "verified"):
        value = record.meta.get(field_name, "")
        parsed = parse_date(value)
        if not parsed:
            result.issues.append(f"{rel}: {field_name} is not YYYY-MM-DD: {value!r}")
        else:
            dates[field_name] = parsed
    if dates.get("updated") and dates.get("date") and dates["updated"] < dates["date"]:
        result.issues.append(f"{rel}: updated date precedes record date")
    if dates.get("verified") and dates["verified"] > today:
        result.issues.append(f"{rel}: verified date is in the future")

    if record.type == "project":
        if record.meta.get("project") != "none":
            result.issues.append(f"{rel}: project record must use project: none")
    elif record.type == "technical-asset":
        project = record.meta.get("project", "")
        if project != "none" and not ID_PATTERNS["project"].fullmatch(project):
            result.issues.append(f"{rel}: invalid project reference {project!r}")
    else:
        project = record.meta.get("project", "")
        project_match = ID_PATTERNS["project"].fullmatch(project)
        if not project_match:
            result.issues.append(f"{rel}: project must be a valid PRJ-* ID")
        elif match and match.group(1) != project_match.group(1):
            result.issues.append(
                f"{rel}: ID project scope {match.group(1)!r} does not match {project!r}"
            )

    _validate_path(record, root, result.issues)

    owner = record.meta.get("owner", "")
    if not owner or PLACEHOLDER_RE.search(owner):
        result.warnings.append(f"{rel}: owner is unassigned")

    review_by = record.meta.get("review-by")
    if review_by:
        review_date = parse_date(review_by)
        if not review_date:
            result.issues.append(f"{rel}: review-by is not YYYY-MM-DD: {review_by!r}")
        elif review_date < today and record.status not in TERMINAL.get(record.type, set()):
            result.warnings.append(f"{rel}: review overdue since {review_by}")

    verified = dates.get("verified")
    if verified:
        max_age = 30 if record.type == "project" else 90
        if record.type in {"project", "technical-asset", "design"}:
            age = (today - verified).days
            if age > max_age and record.status not in TERMINAL.get(record.type, set()):
                result.warnings.append(
                    f"{rel}: authority verification is stale ({age} days)"
                )


def _validate_lifecycle(record: Record, root: Path, result: Result) -> None:
    rel = _relative(record, root)
    refs = record.refs
    if record.type == "requirement":
        if record.status in {"implemented", "verified"} and not any(
            ref.startswith("WORK-") for ref in refs
        ):
            result.issues.append(f"{rel}: {record.status} requirement has no WORK-* evidence")
        if record.status == "verified" and not _real_field(record, "Verification evidence"):
            result.issues.append(f"{rel}: verified requirement lacks verification evidence")
    elif record.type == "design":
        if record.status in {"approved", "implemented", "verified"}:
            if not any(ref.startswith("REQ-") for ref in refs):
                result.issues.append(f"{rel}: {record.status} design has no REQ-* trace")
            if not any(ref.startswith("AST-") for ref in refs):
                result.issues.append(f"{rel}: {record.status} design has no AST-* trace")
    elif record.type == "work-item":
        if record.status in {"ready", "in-progress", "blocked", "done", "verified"}:
            if not any(ref.startswith(("REQ-", "DES-")) for ref in refs):
                result.issues.append(f"{rel}: delivery work has no REQ-* or DES-* trace")
        if record.status in {"done", "verified"} and not _real_field(record, "Evidence"):
            result.issues.append(f"{rel}: {record.status} work item lacks completion evidence")
    elif record.type == "raid":
        if record.status not in TERMINAL["raid"]:
            for field_name in ("review-by", "due"):
                if not parse_date(record.meta.get(field_name, "")):
                    result.issues.append(f"{rel}: open RAID lacks valid {field_name}")
    elif record.type == "release":
        if record.status in {"ready", "approved", "deploying", "deployed", "verified", "closed"}:
            for prefix in ("WORK-", "AST-"):
                if not any(ref.startswith(prefix) for ref in refs):
                    result.issues.append(
                        f"{rel}: {record.status} release has no {prefix}* trace"
                    )
        if record.status in {"approved", "deploying", "deployed", "verified", "closed"}:
            if "- [ ]" in record.text:
                result.issues.append(f"{rel}: {record.status} release has unchecked readiness gates")
        if record.status in {"verified", "closed"} and not _real_field(record, "Evidence"):
            result.issues.append(f"{rel}: {record.status} release lacks outcome evidence")


def validate(root: Path, today: dt.date | None = None) -> Result:
    root = root.resolve()
    today = today or dt.date.today()
    result = collect_records(root)
    by_id: dict[str, Record] = {}

    for record in result.records:
        if record.id in by_id:
            result.issues.append(
                f"duplicate ID {record.id}: {_relative(by_id[record.id], root)} and "
                f"{_relative(record, root)}"
            )
        elif record.id:
            by_id[record.id] = record
        _validate_schema(record, root, today, result)
        _validate_lifecycle(record, root, result)

    for record in result.records:
        rel = _relative(record, root)
        for ref in sorted(record.refs - {record.id}):
            target = by_id.get(ref)
            if not target:
                result.issues.append(f"{rel}: dangling technical record reference {ref}")
            elif record.id not in target.refs:
                result.issues.append(
                    f"{rel}: {ref} does not link back to {record.id}"
                )

    projects: dict[str, list[Record]] = {}
    for record in result.records:
        project_id = record.id if record.type == "project" else record.meta.get("project", "")
        if project_id.startswith("PRJ-"):
            projects.setdefault(project_id, []).append(record)
        if record.type != "project" and record.meta.get("project", "") != "none":
            if record.meta.get("project") not in by_id:
                result.issues.append(
                    f"{_relative(record, root)}: missing project hub "
                    f"{record.meta.get('project')}"
                )

    for project_id, records in projects.items():
        project = by_id.get(project_id)
        if not project or project.status not in {"closed", "cancelled"}:
            continue
        for child in records:
            if child is project:
                continue
            if child.type == "technical-asset":
                # Long-lived assets transfer to operations and commonly remain
                # active after the changing project closes.
                continue
            if child.status not in TERMINAL.get(child.type, set()):
                result.issues.append(
                    f"{_relative(project, root)}: {project.status} project has non-terminal "
                    f"{child.id} ({child.status})"
                )
    return result


def format_result(result: Result, root: Path) -> str:
    lines = ["== Technical project truth =="]
    if not result.records and not result.issues:
        lines.append("ok: no live technical records; templates are ready")
    else:
        lines.append(f"records: {len(result.records)}")
    for issue in result.issues:
        lines.append(f"ISSUE: {issue}")
    for warning in result.warnings:
        lines.append(f"note: {warning}")
    if not result.issues:
        lines.append(
            f"Technical project health: healthy "
            f"({len(result.records)} records, {len(result.warnings)} warning(s))"
        )
    else:
        lines.append(
            f"Technical project health: {len(result.issues)} issue(s), "
            f"{len(result.warnings)} warning(s)"
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--today", type=dt.date.fromisoformat)
    parser.add_argument("--strict", action="store_true", help="exit 1 when issues exist")
    args = parser.parse_args()
    result = validate(args.root, args.today)
    print(format_result(result, args.root))
    return 1 if args.strict and result.issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
