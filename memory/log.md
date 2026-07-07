# Log

Append-only journal of every vault operation, newest last. Never edit or
delete past entries. Entry format (see `.clinerules/10-structure.md`):

```
## [YYYY-MM-DD] operation | subject
One or two lines: what came in, where it was filed, what was updated.
```

Operations: `ingest`, `chat-capture`, `meeting`, `report`, `update`,
`reindex`, `checkup`.

---

(no entries yet — the first filing writes the first entry)
