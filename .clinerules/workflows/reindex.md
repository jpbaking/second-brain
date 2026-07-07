# Workflow: reindex

Rebuild the navigation tree (indexes + catalogs) from what's actually on
disk. Use after manual edits, suspected drift, wrong counts, or when
`/checkup.md` reports orphans. The tree shape is defined in
`.clinerules/10-structure.md` — small roots, entries only in leaves.

Steps:

1. **Area indexes (leaves).** Walk each `memory/<area>/` (skip `index.md`
   and `_template.md`). For each page, derive its one-line summary (from
   its content; freshest dated entry = the "updated" date). Rewrite the
   area's `index.md` in the standard entry format, preserving existing
   grouping/ordering conventions.
2. **Master index (root).** Rewrite `memory/index.md` with one line per
   area and the recounted page totals. No per-page lines at root.
3. **Year catalogs (leaves).** For each `library/YYYY/`, reconcile its
   `catalog.md`: add missing entries (marked `⚠ recovered — details
   unknown` if you can't infer), flag entries whose file no longer exists
   (mark `⚠ missing`, don't delete the line). A file whose year prefix
   doesn't match its shard folder gets moved to the right shard (this is
   a rename, which is allowed — content stays untouched) with both
   catalogs and any memory links updated.
4. **Root catalog.** Rewrite `library/catalog.md`: one line per existing
   year shard with the recounted file totals.
5. **Size rule.** Any leaf index/catalog over 300 lines → shard it one
   level deeper per the procedure in `.clinerules/10-structure.md`.
6. Append a `reindex` entry to `memory/log.md`; run
   `python3 scripts/health.py` to confirm the tree is consistent.
7. Report: pages/files indexed, counts fixed, orphans adopted,
   discrepancies flagged.
