# Workflow: project-status (single project or portfolio rollup)

The principal runs multiple concurrent programmes with commercial
operator deployments — this produces the status view: one project deep,
or the portfolio wide.

## Single project (input: project name)

1. Read the project page fully; pull related entries from meetings,
   decisions, and commitments since the last status entry.
2. Deliver: RAG + why, movement since last status (milestones hit/
   slipped, new risks, closed issues), top 3 risks with owners,
   dependencies blocking or at-age, and the asks (what the principal
   must decide/escalate/nudge).
3. Append the rollup's essence as a dated status-log entry on the
   project page (that's how the next rollup knows "since when").

## Portfolio (no input, or "all projects")

4. One row per project from `memory/projects/`: RAG, phase, next
   milestone + date, top risk, ask. Order: red, amber, green.
5. Flag projects whose status-log is stale (no entry in 30+ days) as
   "status unknown — RAG unreliable" rather than repeating the old
   colour.

## Output

6. Chat by default. As a document: the report rules apply — the deck
   shape (`<kit>.deck.html`) suits exec readouts, the document shape
   suits written programme reviews; evolve a `project-status` template
   in `reports/templates/` on first feedback. Log it.
