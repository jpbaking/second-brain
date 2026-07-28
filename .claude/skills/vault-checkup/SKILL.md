---
name: vault-checkup
description: Run the vault's integrity and hygiene check — the health script plus the judgment calls a script cannot make, such as contradictions, staleness, thin extractions, and missing links. Use when the principal asks for a vault health check, checkup, integrity check, or asks whether the vault is consistent, drifting, or out of date.
---

# Vault health checkup

Run the vault's integrity and hygiene check.

## Steps

1. Run `python3 scripts/health.py` and read its output: inbox backlog,
   orphaned or unindexed files, catalog mismatches, broken links, overdue
   reminders, stale people/projects, and technical project-health failures
   covering record identity, lifecycle, reciprocal traceability, authority,
   evidence, release gates, and closure.
2. Review `memory/` for the things a script cannot judge:
   - **Contradictions** — dated entries on the same page, or across pages,
     that conflict without a `⚠ superseded` marker.
   - **Staleness** — dossiers and projects with no entries in 60 or more days
     that read as if current; reminders long overdue.
   - **Thin extractions** — catalog entries whose memory notes are a bare
     stub relative to the richness of the original.
   - **Missing links** — pages that mention people or projects that have
     pages of their own but are not linked to them.
   - **Project truth** — optimistic RAG unsupported by evidence; baselines
     changed without decisions; approved requirements without designs/work/
     verification; system/infra/UI/UX records inconsistent with their named
     authorities; unowned RAID; releases with paper-only gates; and closed
     projects with residual obligations.
3. Fix the mechanical issues — indexes, links, markers — directly, using the
   `vault-reindex` skill where a full rebuild is warranted. List
   judgment-call issues for the principal instead of deciding them yourself
   (for example: "these two entries about Sam's transfer conflict — which is
   current?").
4. Append a `checkup` entry to `memory/log.md`.
5. Report what was checked, what was fixed, and what needs the principal.
   Separate mechanical failures from judgement calls and list affected stable
   IDs.
