# Workflow: cv-update (brag doc → CV)

The principal maintains their CV outside the vault (record the repo/file
location in their dossier on first use; dated PDF snapshots live in the
library). Their dossier's brag log is the feed.

Steps:

1. Read the principal's dossier in `memory/people/` and collect
   accomplishments dated **after the last CV snapshot** in `library/`
   (compare against the newest CV entry in the year catalogs; if no
   snapshot exists yet, ask for the current CV and ingest it first).
2. Draft CV-ready bullets in the CV's own voice — match its register,
   spelling convention, and formatting; quantified impact, strongest
   first.
3. Deliver in chat: the new bullets, which CV section each belongs to,
   and which existing bullets they might supersede or merge with.
4. Do NOT edit the external CV repo unless the principal grants access
   in that session; if granted, apply the changes there and remind them
   to regenerate/export, then ingest the new PDF as a fresh dated
   snapshot (new catalog entry — never overwrite the old one).
5. Log a `report` entry.

Also fires the other way: if the brag log looks thin for the period
(nothing recorded in 2+ months), say so — that's a capture failure to
raise, not a sign the principal did nothing.
