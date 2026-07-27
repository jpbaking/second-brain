# Vault structure

```
inbox/        ← principal's dump zone. Never file INTO it; only process OUT of it.
library/      ← originals, moved from inbox, renamed, byte-for-byte untouched.
  catalog.md  ← ROOT catalog: navigation only — one line per year shard.
  YYYY/       ← year shard (by the file's date prefix).
    catalog.md← per-file entries for that year.
memory/       ← everything you author. The actual brain.
  index.md    ← ROOT index: navigation only — one line per area, with counts.
  log.md      ← append-only journal of every operation.
  people/     ← one dossier per person (team members, stakeholders). _template.md defines the shape.
  meetings/   ← minutes, one file per meeting, in YYYY/ subfolders.
  projects/   ← one page per ongoing project/initiative.
  decisions/  ← one page per significant decision (ADR-style), YYYY-MM-DD_slug.md.
  notes/      ← mental notes; reminders.md (self tasks) + commitments.md
                (promises between people: I-owe / waiting-on).
  ideas/      ← brainstorms and half-formed thinking.
  topics/     ← anything that fits nowhere else (concepts, orgs, policies).
reports/
  templates/  ← reusable report templates (markdown or HTML).
  YYYY/       ← generated reports, dated.
scripts/      ← health.py integrity check, validate_commit.py, export-pdf.sh.
```

## Naming conventions

- **Library originals:** `library/YYYY/YYYY-MM-DD_short-kebab-slug.ext` —
  date is when the material was created/received (best known), the `YYYY/`
  shard folder MUST equal the filename's year, slug describes content. Keep
  the original extension. Collisions: append `-2`, `-3`.
- **Memory pages:** `kebab-slug.md`. People: `firstname-lastname.md`.
  Meetings: `YYYY/YYYY-MM-DD_topic-slug.md`.
- **Reports:** `reports/YYYY/YYYY-MM-DD_report-slug.md` (or `.html`).
- **Wiki links:** cross-reference memory pages with relative markdown links,
  e.g. `[Sam Reyes](../people/sam-reyes.md)`. Link liberally — links are how
  retrieval works.

## Index & catalog tree (DOX-inspired: small root, detail in leaves)

Navigation files are a two-level tree so no single file grows unbounded —
**root files list children only, never leaf entries**:

- `memory/index.md` (root) — one line per area:
  `- [Area](area/index.md) — N page(s): what lives there`
- `memory/<area>/index.md` (leaf) — one line per page:
  `- [Page title](path.md) — one-line summary (updated YYYY-MM-DD)`
  (meetings pages keep their `YYYY/` prefix in the path)
- `library/catalog.md` (root) — one line per year shard:
  `- [YYYY](YYYY/catalog.md) — N file(s)`
- `library/YYYY/catalog.md` (leaf) — one line per original:
  `- [file](file) — what it is, received YYYY-MM-DD → notes: [page](../../memory/…)`

Counts in root files are recomputed on every filing (`health.py` verifies
them — a wrong count means a missed index update).

**Size rule (mechanical):** when any leaf index/catalog exceeds **300
lines**, shard it one level deeper (e.g. `meetings/index.md` → per-year
`meetings/YYYY/index.md`; `library/2031/catalog.md` → per-month
`2031/MM/`), move the entries (and for catalogs, the files) accordingly,
convert the old leaf into a root that lists the new children, fix inbound
links, and log a `reindex` entry. Never let a navigation file pass 300
lines.

## Log format (`memory/log.md`, append-only, newest last)

```
## [YYYY-MM-DD] operation | subject
One or two lines: what came in, where it was filed, what was updated.
```

Operations: `ingest`, `chat-capture`, `meeting`, `report`, `update`,
`reindex`, `checkup`.
