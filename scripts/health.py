#!/usr/bin/env python3
"""Vault health check — mechanical invariants only; judgment calls are the
agent's job (see the vault-checkup skill).

Verifies the DOX-style navigation tree (small roots listing children with
counts; entries only in leaves) defined in rules/shared/10-structure.md.

Run from anywhere: python3 scripts/health.py
Stdlib only. Always exits 0 (it reports; it doesn't gate)."""

import datetime
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TODAY = datetime.date.today()
STALE_DAYS = 60
MAX_NAV_LINES = 300

issues = 0
DATE_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
LINK_RE = re.compile(r"\]\(([^)#]+)(?:#[^)]*)?\)")


def section(title):
    print(f"\n== {title} ==")


def flag(msg):
    global issues
    issues += 1
    print(f"ISSUE: {msg}")


def ok(msg):
    print(f"ok: {msg}")


def note(msg):
    print(f"note: {msg}")


def parse_date(s):
    try:
        return datetime.date.fromisoformat(s)
    except ValueError:
        return None


def entry_lines(text):
    """Real list entries: lines starting with '- ['. Backtick-quoted lines
    are format examples in headers and never count."""
    return [
        ln.strip() for ln in text.splitlines()
        if ln.strip().startswith("- [")
    ]


def linkable_lines(text):
    """Lines whose links should resolve — skips backticked format examples."""
    return [ln for ln in text.splitlines() if not ln.strip().startswith("`")]


def read(p):
    return p.read_text(encoding="utf-8")


# --- Inbox backlog ---------------------------------------------------------
section("Inbox backlog")
backlog = [p for p in (ROOT / "inbox").rglob("*") if p.is_file() and p.name != "README.md"]
if backlog:
    flag(f"{len(backlog)} unprocessed file(s) in inbox/ — use the vault-inbox skill")
    for p in backlog:
        print(f"  - {p.relative_to(ROOT)}")
else:
    ok("inbox is empty")

# --- Library tree: shards, leaf catalogs, root catalog ----------------------
section("Library tree")
lib = ROOT / "library"
root_cat = read(lib / "catalog.md") if (lib / "catalog.md").exists() else ""

lib_files = [p for p in lib.rglob("*") if p.is_file() and p.name != "catalog.md"]
year_counts = {}
for p in lib_files:
    rel = p.relative_to(lib)
    m = re.match(r"^(\d{4}-\d{2}-\d{2})_", p.name)
    if not m:
        flag(f"library file not date-prefixed (YYYY-MM-DD_slug.ext): {rel}")
        continue
    year = m.group(1)[:4]
    if len(rel.parts) < 2 or rel.parts[0] != year:
        flag(f"library file not in its year shard (should be library/{year}/): {rel}")
        continue
    year_counts[year] = year_counts.get(year, 0) + 1
    shard_cat = lib / year / "catalog.md"
    if not shard_cat.exists():
        flag(f"missing shard catalog: library/{year}/catalog.md")
    elif f"({p.name})" not in read(shard_cat):
        flag(f"library file not in its shard catalog: {rel}")

# leaf catalog references must exist
for shard_cat in lib.glob("*/catalog.md"):
    for line in entry_lines(read(shard_cat)):
        for ref in LINK_RE.findall(line):
            if ref.startswith(("http://", "https://")):
                continue
            if not (shard_cat.parent / ref).exists():
                flag(f"{shard_cat.relative_to(ROOT)} references missing file: {ref}")

# root catalog: one line per existing shard, with accurate count; no leaf entries
for year, count in sorted(year_counts.items()):
    m = re.search(rf"- \[{year}\]\({year}/catalog\.md\) — (\d+) file", root_cat)
    if not m:
        flag(f"root catalog missing shard line for {year} — use the vault-reindex skill")
    elif int(m.group(1)) != count:
        flag(f"root catalog count for {year} is {m.group(1)}, actual {count} — use the vault-reindex skill")
for y in re.findall(r"- \[(\d{4})\]\(\1/catalog\.md\)", root_cat):
    if y not in year_counts:
        flag(f"root catalog lists shard {y} but library/{y}/ has no files")
for line in entry_lines(root_cat):
    if not re.match(r"- \[\d{4}\]\(\d{4}/catalog\.md\)", line):
        flag(f"root library/catalog.md has a non-shard entry (belongs in a leaf catalog): {line[:60]}")
ok("library tree check done")

# --- Memory tree: area indexes (leaves), master index (root) ---------------
section("Memory tree")
mem = ROOT / "memory"
master = read(mem / "index.md")
skip = {"index.md", "log.md", "_template.md"}

areas = sorted(d for d in mem.iterdir() if d.is_dir())
for area in areas:
    area_index_path = area / "index.md"
    if not area_index_path.exists():
        flag(f"area missing its index: memory/{area.name}/index.md")
        continue
    area_index = read(area_index_path)
    pages = [
        p for p in area.rglob("*.md")
        if p.name not in skip
    ]
    for p in pages:
        rel = p.relative_to(area).as_posix()
        if f"({rel})" not in area_index:
            flag(f"page not in its area index: memory/{area.name}/{rel} — use the vault-reindex skill")
    # root line: link + accurate count
    m = re.search(rf"- \[[^\]]+\]\({area.name}/index\.md\) — (\d+) page", master)
    if not m:
        flag(f"master index missing area line for memory/{area.name}/ — use the vault-reindex skill")
    elif int(m.group(1)) != len(pages):
        flag(f"master index count for {area.name} is {m.group(1)}, actual {len(pages)} — use the vault-reindex skill")
for line in entry_lines(master.split("## Areas")[-1]):
    if not re.match(r"- \[[^\]]+\]\([a-z-]+/index\.md\)", line):
        flag(f"root memory/index.md has a non-area entry (belongs in an area index): {line[:60]}")

# link integrity across all memory pages and indexes
for p in mem.rglob("*.md"):
    if p.name == "log.md":
        continue
    for line in linkable_lines(read(p)):
        for ref in LINK_RE.findall(line):
            if ref.startswith(("http://", "https://", "mailto:")):
                continue
            if not (p.parent / ref).exists():
                flag(f"broken link in {p.relative_to(ROOT)}: ({ref})")

# staleness (people/projects only)
stale = []
for area_name in ("people", "projects"):
    for p in (mem / area_name).rglob("*.md"):
        if p.name in skip:
            continue
        dates = [d for d in (parse_date(m) for m in DATE_RE.findall(read(p))) if d]
        if dates and (TODAY - max(dates)).days > STALE_DAYS:
            stale.append((p.relative_to(ROOT), max(dates)))
if stale:
    note(f"{len(stale)} people/project page(s) with no entry in {STALE_DAYS}+ days:")
    for rel, last in stale:
        print(f"  - {rel} (last dated entry {last})")
ok("memory tree check done")

# --- Navigation file size rule ----------------------------------------------
section("Navigation size rule")
nav_files = [mem / "index.md", lib / "catalog.md"]
nav_files += [a / "index.md" for a in areas if (a / "index.md").exists()]
nav_files += list(lib.glob("*/catalog.md"))
oversized = [(p, n) for p in nav_files if (n := len(read(p).splitlines())) > MAX_NAV_LINES]
if oversized:
    for p, n in oversized:
        flag(f"navigation file over {MAX_NAV_LINES} lines ({n}): {p.relative_to(ROOT)} — shard it per 10-structure.md")
else:
    ok(f"all navigation files under {MAX_NAV_LINES} lines")

# --- Reminders & commitments -------------------------------------------------
section("Reminders & commitments")
overdue = []
for fname in ("reminders.md", "commitments.md"):
    path = mem / "notes" / fname
    if not path.exists():
        continue
    for line in read(path).splitlines():
        m = re.match(r"\s*- \[ \] (\d{4}-\d{2}-\d{2}) due:(.*)", line)
        if m and (d := parse_date(m.group(1))) and d < TODAY:
            overdue.append(f"{fname[:-3]}: {m.group(1)}:{m.group(2).rstrip()}")
if overdue:
    note(f"{len(overdue)} overdue reminder(s)/commitment(s):")
    for r in overdue:
        print(f"  - {r}")
else:
    ok("no overdue reminders or commitments")

# --- Pending markers ---------------------------------------------------------
section("Unconfirmed / superseded markers")
marked = [
    p.relative_to(ROOT)
    for p in mem.rglob("*.md")
    if p.name not in ("log.md", "_template.md") and "⚠" in read(p)
]
if marked:
    note(f"{len(marked)} page(s) carry ⚠ markers needing eventual resolution:")
    for rel in marked:
        print(f"  - {rel}")
else:
    ok("no pending ⚠ markers")

# --- Technical project truth -------------------------------------------------
project_health = subprocess.run(
    [
        sys.executable,
        str(ROOT / "scripts" / "project_health.py"),
        "--root",
        str(ROOT),
        "--strict",
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
)
print()
print(project_health.stdout.rstrip())
if project_health.returncode:
    flag("technical project source-of-truth validation failed")

# --- Summary -----------------------------------------------------------------
section("Summary")
if issues == 0:
    print("Vault healthy: no mechanical issues found.")
else:
    print(f"{issues} issue(s) found — see above.")
