---
name: vault-project-status
description: Report project status from the vault — a deep dive on one project (RAG, movement, risks, dependencies, asks) or a portfolio rollup across all active projects. Use when the principal asks where a project stands, for a status update, portfolio view, or programme review, what is at risk or blocked, what changed on a project, or asks to prepare for a steering meeting.
---

# Project status

The principal runs multiple concurrent programmes with commercial operator
deployments. This produces the status view: one project deep, or the
portfolio wide. Use the single-project path when a project is named, and the
portfolio path when none is, or when asked for "all projects".

## Single project

1. Read the project page fully, then pull related entries from meetings,
   decisions, and commitments since the last status entry.
2. Deliver: RAG and why; movement since the last status (milestones hit or
   slipped, new risks, closed issues); the top three risks with owners;
   dependencies that are blocking or ageing; and the asks — what the
   principal must decide, escalate, or nudge.
3. Append the essence of the rollup as a dated status-log entry on the
   project page. That is how the next rollup knows "since when".

## Portfolio

4. One row per project from `memory/projects/`: RAG, phase, next milestone
   and date, top risk, and ask. Order red, then amber, then green.
5. Flag projects whose status log is stale — no entry in 30 or more days — as
   "status unknown — RAG unreliable" rather than repeating the old colour.

## Output

6. Chat by default. As a document, the report rules in
   `rules/shared/40-reports.md` apply: the deck shape suits exec readouts and
   the document shape suits written programme reviews. Evolve a
   `project-status` template in `reports/templates/` on first feedback, and
   log it.
