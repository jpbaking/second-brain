# Workflow: process the inbox

Process every file currently in `inbox/` per the capture rules
(`.clinerules/20-capture.md`).

Steps:

1. List `inbox/` (ignore `README.md`). If empty, say so and stop.
2. For each item, oldest first:
   a. Read/inspect it enough to know what it is and roughly when it's from.
   b. Move it to `library/YYYY/YYYY-MM-DD_slug.ext` (year shard = filename
      year; create the shard + its `catalog.md` if new) — content untouched.
   c. Add its line to `library/YYYY/catalog.md`; update that year's count
      in the root `library/catalog.md`.
   d. Extract meaning into `memory/` — update existing pages (check the
      area indexes via the root `memory/index.md` first) or create new
      ones from the area's `_template.md`. Date every fact; link the
      memory page back to the library original.
   e. Update the touched area `index.md` files and the counts in the root
      `memory/index.md`.
   f. Append an `ingest` entry to `memory/log.md`.
3. Finish with a filing summary: one line per item — original name →
   library name → memory pages touched — plus any flags (contradictions,
   ambiguities, follow-up questions). Ask the questions; don't guess.
