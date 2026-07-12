# AGENTS.md — read this first

This vault is operated by an AI executive secretary. This file is the root
map: it tells you what must never break and where the detailed instructions
live. **Do not act from this file alone — follow the links for the task at
hand.** Like the vault's own indexes (DOX-style), this root stays small;
detail lives in the leaves.

## Hard invariants (never break, no exceptions)

1. **Never edit, reformat, convert, or delete anything under `library/`**
   (catalogs `catalog.md` excepted). Originals are byte-for-byte sacred;
   you may only move/rename inbox files into `library/YYYY/`.
2. **Never rewrite history in `memory/log.md`** — append-only, one line per
   ingest/filing/report.
3. **Every filing updates its leaf index and the log.** An unindexed page
   is a lost page. Root navigation files (`memory/index.md`,
   `library/catalog.md`) list children + counts only — never leaf entries.
4. **Every fact is dated** (`- YYYY-MM-DD: …`, absolute dates only) and
   answers cite their source files.
5. **Never file into `inbox/`** — only process out of it.
6. **Run `python3 scripts/health.py` before finishing** any task that
   touched `library/`, `memory/`, or indexes. Fix what it reports.

## Where the rules live

| You are about to… | Read first |
|---|---|
| Do anything at all (role, tone, prime directives) | [.clinerules/00-role.md](.clinerules/00-role.md) |
| Create, move, or name any file; touch an index/catalog | [.clinerules/10-structure.md](.clinerules/10-structure.md) |
| File new material or facts (inbox, chat, meetings) | [.clinerules/20-capture.md](.clinerules/20-capture.md) |
| Answer a question from the vault | [.clinerules/30-retrieval.md](.clinerules/30-retrieval.md) |
| Generate a report (markdown/HTML/PDF, templates) | [.clinerules/40-reports.md](.clinerules/40-reports.md) |
| Commit completed work or handle a dirty worktree | [.clinerules/50-version-control.md](.clinerules/50-version-control.md) |
| Run a named workflow (`/inbox`, `/meeting`, `/brief`, …) | the matching file in [.clinerules/workflows/](.clinerules/workflows/) |
| Draft an eval, interview debrief, or styled HTML report | the matching skill in [.cline/skills/](.cline/skills/) |

## Orientation (map, not content)

```
inbox/    → raw dumps from the principal (process OUT only)
library/  → originals, untouched, YYYY/ shards + per-year catalog.md
memory/   → everything you author: people/ meetings/ projects/ decisions/
            notes/ ideas/ topics/ — plus index.md (root nav) and log.md
reports/  → generated reports (YYYY/), templates/, design/ kits
scripts/  → health.py (invariant checker), export-pdf.sh
```

Navigation is a strict two-level tree: root lists children with counts,
leaves hold entries; any leaf index over **300 lines** gets sharded one
level deeper (see [.clinerules/10-structure.md](.clinerules/10-structure.md)).

## If you get lost

- Start from `memory/index.md` (never grep blindly first).
- Unsure where a fact goes? File it in `memory/topics/`, note the
  uncertainty in the log — a misfiled note beats an unfiled one.
- Found drift (wrong counts, broken links)? Run
  `python3 scripts/health.py`; repair via the
  [/reindex workflow](.clinerules/workflows/reindex.md).
