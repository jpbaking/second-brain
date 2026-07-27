---
name: vault-inbox
description: Process every file sitting in the vault's inbox/ into library/ originals plus memory/ synthesis, then index and log it. Use when the principal says to process, clear, or file the inbox, asks what is waiting to be processed, or has just dropped notes, transcripts, screenshots, or exports into inbox/ and wants them catalogued.
---

# Process the inbox

Process every file currently in `inbox/` per the capture rules in
`rules/shared/20-capture.md`.

## Steps

1. List `inbox/`, ignoring `README.md`. If it is empty, say so and stop.
2. For each item, oldest first:
   a. Read or inspect it enough to know what it is and roughly when it is
      from.
   b. Move it to `library/YYYY/YYYY-MM-DD_slug.ext` — the year shard equals
      the filename year; create the shard and its `catalog.md` if new. Move,
      never copy, and never alter the content.
   c. Add its line to `library/YYYY/catalog.md`, then update that year's
      count in the root `library/catalog.md`.
   d. Extract meaning into `memory/`. Check the area indexes via the root
      `memory/index.md` first and update existing pages; create new ones
      from the area's `_template.md` only when no home exists. Date every
      fact and link the memory page back to the library original.
   e. Update the touched area `index.md` files and the counts in the root
      `memory/index.md`.
   f. Append an `ingest` entry to `memory/log.md`.
3. Finish with a filing summary: one line per item — original name → library
   name → memory pages touched — plus any flags (contradictions,
   ambiguities, follow-up questions). Ask the questions; do not guess.

If a file is unintelligible (corrupt or unknown format), move it to its year
shard anyway using the received date, catalog it as
`unprocessed — needs principal input`, and ask.
