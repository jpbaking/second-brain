---
name: vault-cv-update
description: Turn the principal's own brag log in the vault into CV-ready bullets, comparing against the last CV snapshot in the library. Use when the principal asks to update their CV or résumé, wants their recent accomplishments written up for it, is preparing a promo case or self-review, or asks what they have shipped since the last CV revision.
---

# Brag doc to CV

The principal maintains their CV outside the vault. Record the repository or
file location in their dossier on first use; dated PDF snapshots live in the
library. Their dossier's brag log is the feed.

## Steps

1. Read the principal's own dossier in `memory/people/` and collect
   accomplishments dated **after the last CV snapshot** in `library/`,
   comparing against the newest CV entry in the year catalogs. If no snapshot
   exists yet, ask for the current CV and ingest it first with the
   `vault-inbox` procedure.
2. Draft CV-ready bullets in the CV's own voice — match its register,
   spelling convention, and formatting. Quantify impact, strongest first.
3. Deliver in chat: the new bullets, which CV section each belongs to, and
   which existing bullets they might supersede or merge with.
4. Do **not** edit the external CV repository unless the principal grants
   access in that session. If granted, apply the changes there, remind them
   to regenerate or export, then ingest the new PDF as a fresh dated
   snapshot — a new catalog entry, never overwriting the old one.
5. Append a `report` entry to `memory/log.md`.

This also fires the other way: if the brag log looks thin for the period —
nothing recorded in two or more months — say so. That is a capture failure to
raise, not a sign the principal did nothing.
