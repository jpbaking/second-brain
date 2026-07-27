---
name: vault-recall
description: Answer a question about the principal's world — people, meetings, projects, decisions, notes — strictly from the vault, with cited sources and recorded fact separated from inference. Use when the principal asks what the vault knows about someone or something, what was said or agreed, when something happened, or any question whose answer should come from their own records rather than general knowledge.
---

# Answer from the vault

Answer the principal's question strictly per the retrieval rules in
`rules/shared/30-retrieval.md`. The vault is the source of truth — not your
general knowledge and not your guesses.

## Steps

1. Parse the question and list the entities involved: people, projects,
   topics, time ranges.
2. Search in this order: `memory/index.md` → the relevant area
   `memory/<area>/index.md` → read the candidate pages fully → follow their
   wiki-links one hop → grep across `memory/` if the indexes come up thin →
   traverse `library/catalog.md` → `library/YYYY/catalog.md` for originals
   that were catalogued but thinly extracted.
3. Answer: lead with the answer, cite the source pages
   (`(source: people/sam-reyes.md)`), separate recorded fact from inference
   ("Recorded: X, Y. My read: Z."), date time-sensitive facts, and flag
   staleness and conflicts. Where entries conflict, surface both with dates
   rather than silently picking one.
4. If the vault cannot answer, say exactly what is missing and where you
   looked — then offer clearly-labelled general knowledge if it would help.
5. If the synthesis was substantial, offer to save it as a memory page or a
   report so it is cheap next time.
