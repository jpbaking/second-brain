---
name: vault-recall
description: Answer a question about the principal's world — people, meetings, projects, requirements, systems, infrastructure, designs, UI/UX, work, RAID, releases, decisions, and notes — strictly from the vault, with cited sources and recorded fact separated from inference. Use when the principal asks what the vault knows, what was required, designed, built, released, said or agreed, why a choice was made, when something happened, or any question whose answer should come from their own records.
---

# Answer from the vault

Answer the principal's question strictly per the retrieval rules in
`rules/shared/30-retrieval.md`. The vault is the source of truth — not your
general knowledge and not your guesses.

## Steps

1. Parse the question and list people, stable record IDs, projects, assets,
   topics, status terms, and time ranges. Load
   `rules/shared/35-technical-project-management.md` for technical questions.
2. Search the vault index service first, using exact/text mode for IDs, names,
   acronyms, repositories, interfaces, and release codes, then expand only
   promising sections. If unavailable, traverse `memory/index.md` → relevant
   area index → candidate pages. Follow traceability links to authority and
   evidence, then inspect library catalogs for originals that were thinly
   extracted.
3. Answer: lead with the answer, cite the source pages
   (`(source: people/sam-reyes.md)`), separate recorded fact from inference
   ("Recorded: X, Y. My read: Z."), date time-sensitive facts, and flag
   staleness and conflicts. Where entries conflict, surface both with dates
   rather than silently picking one.
   For technical state, name the authoritative system, last verification,
   baseline or lifecycle state, supporting record IDs, and missing gates.
4. If the vault cannot answer, say exactly what is missing and where you
   looked — then offer clearly-labelled general knowledge if it would help.
5. If the synthesis was substantial, offer to save it as a memory page or a
   report so it is cheap next time.
