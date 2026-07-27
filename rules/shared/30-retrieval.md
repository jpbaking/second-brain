# Retrieval: how to answer questions from the vault

When the principal asks about their world (people, meetings, projects,
decisions, notes), the vault is the source of truth — not your general
knowledge and not your guesses.

## Search order

1. Traverse the index tree root→leaf: `memory/index.md` (areas) → the
   relevant `memory/<area>/index.md` (pages). Read only the indexes you
   need — that's what keeps them small enough to be reliable.
2. Read the candidate pages fully; follow their wiki-links one hop.
3. If the indexes don't surface anything, grep/search across `memory/`
   for names and keywords, then traverse `library/catalog.md` → the
   relevant `library/YYYY/catalog.md` for originals that were catalogued
   but thinly extracted.
4. Only if the vault has nothing: say so explicitly, then (and only then)
   offer general knowledge, clearly labeled as such.

## Answer format

- Lead with the answer.
- Cite the memory pages used: `(source: people/sam-reyes.md)`.
- Separate **recorded fact** from **inference**: "Recorded: X, Y.
  My read: Z." Never present inference as record.
- Include the date of the underlying facts when the answer is
  time-sensitive; flag staleness ("last entry on this is from March —
  may be out of date").
- If the vault contains conflicting entries, surface both with dates
  rather than picking one silently.

## Filing the byproduct

If answering required nontrivial synthesis (comparing people, summarizing a
project across many meetings), consider saving that synthesis as a new
memory page or report so it's cheap next time. Mention it if you do.
