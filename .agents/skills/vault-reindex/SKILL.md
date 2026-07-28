---
name: vault-reindex
description: Rebuild the vault's navigation tree — memory area indexes, the root index, library year catalogs, and the root catalog — from what is actually on disk, fixing counts, adopting orphans, and sharding oversized files. Use after manual edits, suspected drift, wrong counts, broken navigation, or when a health check reports orphans or mismatches.
---

# Rebuild the navigation tree

Rebuild the indexes and catalogs from what is actually on disk. Use this
after manual edits, suspected drift, wrong counts, or when the
`vault-checkup` skill reports orphans. The tree shape is defined in
`rules/shared/10-structure.md` — small roots, entries only in leaves.

## Steps

1. **Area indexes (leaves).** Walk each `memory/<area>/`, skipping `index.md`
   and `_template.md`. Include pages nested under project-scoped directories
   such as `requirements/prj-<slug>/`; keep their relative paths in the area
   index. For each page, derive its ID, title, kind, status, owner, project,
   `updated`, and `verified` from frontmatter where present, falling back to
   the freshest dated entry for legacy pages. Rewrite the area's `index.md`
   in the standard entry format, preserving the existing grouping and
   ordering conventions.
2. **Master index (root).** Rewrite `memory/index.md` with one line per area
   and the recounted page totals. No per-page lines at root.
3. **Year catalogs (leaves).** For each `library/YYYY/`, reconcile its
   `catalog.md`: add missing entries, marked `⚠ recovered — details unknown`
   where you cannot infer them, and flag entries whose file no longer exists
   with `⚠ missing` rather than deleting the line. A file whose year prefix
   does not match its shard folder gets moved to the correct shard — this is
   a rename, which is allowed, and the content stays untouched — with both
   catalogs and any memory links updated.
4. **Root catalog.** Rewrite `library/catalog.md` with one line per existing
   year shard and the recounted file totals.
5. **Size rule.** Any leaf index or catalog over 300 lines gets sharded one
   level deeper, per the procedure in `rules/shared/10-structure.md`.
6. **Technical records.** Preserve stable IDs and project-scoped paths from
   `rules/shared/35-technical-project-management.md`. Flag duplicate IDs,
   missing project hubs, or records whose project/traceability links cannot
   be resolved; never renumber them during a reindex.
7. Append a `reindex` entry to `memory/log.md`, then run
   `python3 scripts/health.py` to confirm the tree is consistent.
8. Report pages and files indexed, counts fixed, orphans adopted, and
   discrepancies flagged.
