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
7. **Technical status must be traceable.** Never mark a requirement,
   design, work item, release, or project verified/closed without linked
   authority and evidence; use `unknown` rather than inventing progress.

## Where the rules live

| You are about to… | Read first |
|---|---|
| Do anything at all (role, tone, prime directives) | [rules/shared/00-role.md](rules/shared/00-role.md) |
| Create, move, or name any file; touch an index/catalog | [rules/shared/10-structure.md](rules/shared/10-structure.md) |
| File new material or facts (inbox, chat, meetings) | [rules/shared/20-capture.md](rules/shared/20-capture.md) |
| Answer a question from the vault | [rules/shared/30-retrieval.md](rules/shared/30-retrieval.md) |
| Plan or update technical projects, systems, infrastructure, requirements, designs, UI/UX, work, risks, or releases | [rules/shared/35-technical-project-management.md](rules/shared/35-technical-project-management.md) |
| Generate a report (markdown/HTML/PDF, templates) | [rules/shared/40-reports.md](rules/shared/40-reports.md) |
| Commit completed work or handle a dirty worktree | [rules/shared/50-version-control.md](rules/shared/50-version-control.md) |
| Run a named procedure (process the inbox, file a meeting, brief me, …) | the matching skill in [skills/shared/](skills/shared/) |

Procedures are **Agent Skills**, portable across harnesses. Ask for one by
name — "use the `vault-inbox` skill" — or just describe the task and let the
agent select it. The vault's own procedures are prefixed `vault-`
(`vault-inbox`, `vault-meeting`, `vault-brief`, `vault-recall`,
`vault-remember`, `vault-decision`, `vault-prep`, `vault-one-on-one`,
`vault-project-plan`, `vault-project-update`, `vault-project-status`,
`vault-requirements`, `vault-system-map`, `vault-design`, `vault-release`,
`vault-project-close`, `vault-weekly`, `vault-checkup`, `vault-reindex`,
`vault-handoff`, `vault-cv-update`); the document-producing ones are
`report-builder`, `performance-evaluation`, `interview-debrief`, and
`claude-report-design`.

## Orientation (map, not content)

```
inbox/    → raw dumps from the principal (process OUT only)
library/  → originals, untouched, YYYY/ shards + per-year catalog.md
memory/   → everything you author: people/ meetings/ projects/ decisions/
            technical-assets/ requirements/ designs/ work-items/ raid/
            releases/ notes/ ideas/ topics/ — plus index.md and log.md
reports/  → generated reports (YYYY/), templates/, design/ kits
scripts/  → health.py + project_health.py (invariant checkers), export-pdf.sh,
            sync-agent-adapters.sh (regenerates the harness adapters)

rules/shared/   → CANONICAL agent rules (this file points at them)
skills/shared/  → CANONICAL agent skills
.agents/skills/ → GENERATED adapter (Codex, Antigravity, Cline)
.claude/skills/ → GENERATED adapter (Claude Code)
.clinerules/hooks/ → Cline-only enforcement (host-specific, not portable)
```

**Never edit `.agents/skills/` or `.claude/skills/` directly** — they are
generated copies. Edit `skills/shared/`, then run
`./scripts/sync-agent-adapters.sh` (`--check` verifies they are in sync).

Navigation is a strict two-level tree: root lists children with counts,
leaves hold entries; any leaf index over **300 lines** gets sharded one
level deeper (see [rules/shared/10-structure.md](rules/shared/10-structure.md)).

## If you get lost

- Start from `memory/index.md` (never grep blindly first).
- Unsure where a fact goes? File it in `memory/topics/`, note the
  uncertainty in the log — a misfiled note beats an unfiled one.
- Found drift (wrong counts, broken links)? Run
  `python3 scripts/health.py`; repair with the `vault-reindex` skill.
