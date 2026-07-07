# Workflow: checkup (vault health)

Run the vault's integrity and hygiene check.

Steps:

1. Run `python3 scripts/health.py` and read its output (inbox backlog,
   orphaned/unindexed files, catalog mismatches, broken links, overdue
   reminders, stale people/project pages).
2. Review `memory/` for the things a script can't judge:
   - **Contradictions** — dated entries on the same page (or across pages)
     that conflict without a `⚠ superseded` marker.
   - **Staleness** — dossiers/projects with no entries in 60+ days that
     read as if current; reminders long overdue.
   - **Thin extractions** — catalog entries whose memory notes are a bare
     stub relative to the original's richness.
   - **Missing links** — pages that mention people/projects that have
     pages but aren't linked.
3. Fix the mechanical issues (indexes, links, markers) directly; run
   `/reindex.md` steps where needed. List judgment-call issues for the
   principal instead of deciding (e.g. "these two entries about Sam's
   transfer conflict — which is current?").
4. Append a `checkup` entry to `memory/log.md`.
5. Report: what was checked, what was fixed, what needs the principal.
