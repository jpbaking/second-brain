# Second Brain — an AI executive secretary vault

A file-based knowledge vault operated by an AI agent
([Cline](https://cline.bot)) acting as your executive secretary. You dump
raw material and talk; the agent files, indexes, and cross-references
everything; you ask questions and get cited answers; you request reports
and get polished, offline-ready HTML/PDF documents whose formatting
improves with your feedback.

Built for a senior engineer / architect / group lead: team dossiers and
performance evaluations, meeting minutes and prep packs, decision records,
project RAG rollups, commitments tracking, interview debriefs, and a brag
log that turns into CV bullets.

Inspired by [Karpathy's LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
(agent-maintained markdown + indexes) and [DOX](https://github.com/jpbaking/dox)
(small root docs, detail in leaves — so navigation files never outgrow a
weaker model's reliability).

## Quick start

1. **Get a private copy.** This repo is a data-free template. Create your
   private instance from it (GitHub: *Use this template*), keep it
   private — it will hold sensitive people data. Optionally add the
   template as an `upstream` remote to pull future improvements.
2. **Requirements:** [Cline](https://cline.bot) (VS Code extension);
   `python3` (stdlib only, for the health check and hooks);
   Chrome/Chromium (optional, for agent-side PDF export).
3. **Open the folder in Cline.** Rules in `.clinerules/` load
   automatically; hooks and skills are picked up from `.clinerules/hooks/`
   and `.cline/skills/`.
4. **Start using it:** drop files into `inbox/` and say `/inbox.md` — or
   just tell the agent about your team, meetings, and projects. Ask it
   anything later.

## How it works

Three layers, strictly separated:

```
inbox/    →   library/               →   memory/
your dumps    originals, untouched,      the agent's synthesis:
              renamed + catalogued       dossiers, minutes, projects,
              by year                    decisions, notes — indexed + logged
```

- **Originals are sacred.** Files are moved (never edited) into
  `library/YYYY/` with date-prefixed names. A `PreToolUse` hook hard-blocks
  agent edits to them.
- **Everything is indexed.** Navigation is a two-level tree: root files
  (`memory/index.md`, `library/catalog.md`) list only children with
  counts; entries live in leaf indexes/catalogs. A mechanical 300-line
  rule triggers deeper sharding, so no navigation file ever grows past
  what a small model handles reliably.
- **Everything is logged.** `memory/log.md` is an append-only journal of
  every ingest, filing, and report.
- **Every fact is dated**, answers cite their source pages, and recorded
  fact is kept separate from inference.

## Daily use

| You say | The secretary does |
|---|---|
| *"Sam shipped the migration two weeks early"* | Files it (dated) into Sam's dossier's accomplishments log |
| *"/prep.md — steering meeting with KDDI folks tomorrow"* | Prep pack: attendee one-liners, open threads, landmines, talking points |
| *"/one-on-one.md Sam"* | 1:1 arc: recognise / follow up / probe / goal pulse / carry-over |
| *"Draft Sam's performance eval"* | Evidence-based draft from goals + dated entries; flags gaps loudly |
| *"/project-status.md"* | Portfolio RAG rollup; stale statuses report as "unknown", not old green |
| *"/brief.md"* | Overdue reminders/commitments, upcoming dates, loose ends |
| *"Make that report a deck instead"* + feedback | Report re-done; your formatting persisted as a template for next time |

## Workflows (type `/` in Cline)

| Command | Does |
|---|---|
| `/inbox.md` | Process everything in `inbox/` into `library/` + `memory/` |
| `/remember.md` | File facts you just said in chat |
| `/recall.md` | Answer a question with sources cited |
| `/meeting.md` | File meeting minutes; fan out decisions/actions/people facts |
| `/prep.md` | Meeting prep pack |
| `/one-on-one.md` | 1:1 prep and post-1:1 capture |
| `/decision.md` | Record a decision (ADR-style: options, rejections, revisit date) |
| `/project-status.md` | Single-project deep dive or portfolio RAG rollup |
| `/cv-update.md` | Turn the principal's brag log into CV-ready bullets |
| `/brief.md` | Daily brief |
| `/weekly.md` | Weekly review: sweep, nudge list, people pulse, look ahead |
| `/handoff.md` | Out-of-office handoff and re-entry brief |
| `/report.md` | Generate a report (markdown or HTML), template-aware |
| `/reindex.md` | Rebuild the navigation tree from disk |
| `/checkup.md` | Health check + judgment-level hygiene |

## Skills (auto-trigger or type `/name`)

| Skill | Does |
|---|---|
| `performance-evaluation` | Evidence-based eval drafts from dossier + goals + meetings |
| `interview-debrief` | Structured candidate feedback vs your rubric; HR-sensitive handling |
| `report-builder` | The template-evolution loop for recurring reports |
| `lazyway-io-design` | Rules for `lazyway.*` HTML reports (kit's own skill) |
| `claude-report-design` | Rules for `claude.*` HTML reports (light/dark kit) |

## Hooks (`.clinerules/hooks/`, Python, fail-open)

- **TaskStart** — injects a briefing into every session: inbox backlog,
  overdue reminders/commitments, unresolved ⚠ markers.
- **PreToolUse** — blocks any file-edit tool targeting `library/`
  originals (catalogs excepted). Moving/renaming via shell stays allowed.

## Reports, design kits, PDF

HTML reports are **fully offline** — kits are vendored under
`reports/design/<kit>/` with self-hosted fonts; no CDN, no CORS/referrer
issues opening from disk. Kits: **lazyway** (IBM Plex, brand blue, one
amber accent) and **claude** (warm ivory/charcoal light+dark, terracotta,
persisted theme toggle, print always light). Index and add-a-kit recipe:
[reports/design/README.md](reports/design/README.md).

Three template shapes per kit in `reports/templates/` —
`document` (Word-style A4), `deck` (PowerPoint-style 16:9 slides),
`interactive` (responsive one-pager). Export to PDF via the browser's
Print → Save as PDF, or `scripts/export-pdf.sh <report.html>` (headless
Chrome). Formatting feedback is persisted to `reports/templates/` so it's
never given twice.

## Maintenance

- `python3 scripts/health.py` — mechanical invariants: inbox backlog,
  shard placement, catalog/index tree consistency and counts, broken
  links, navigation size rule, overdue items, stale dossiers. Run by
  `/checkup.md` and `/weekly.md`.
- `/reindex.md` — rebuilds the tree when drift is found.

## Repo layout

| Path | What | Written by |
|---|---|---|
| `inbox/` | Raw dumps, unprocessed | You |
| `library/YYYY/` | Originals, byte-for-byte untouched, per-year catalogs | Agent (move/rename only) |
| `memory/` | People, meetings, projects, decisions, notes, ideas, topics + root index + append-only log | Agent |
| `reports/` | Generated reports (`YYYY/`), templates, design kits | Agent |
| `scripts/` | `health.py`, `export-pdf.sh` | — |
| `.clinerules/` | Always-on rules, `workflows/`, `hooks/` | You + agent |
| `.cline/skills/` | On-demand skills | You + agent |

## For AI agents (non-Cline)

If you are an agent other than Cline working in this repo: read
`.clinerules/00-role.md` and `.clinerules/10-structure.md` before
changing anything. The invariants bind you too — never modify files under
`library/` (except catalogs), never rewrite `memory/log.md` history,
update indexes + log with every filing, and run
`python3 scripts/health.py` before finishing.

## Privacy

The private instance will hold performance evaluations, attrition risks,
and interview feedback. Keep it private; don't sync it anywhere you
wouldn't email it. Initialise git only after confirming no personal data
is present (this template ships clean).

## License

Template: [0BSD](LICENSE) — use it for anything, no attribution needed.
Vendored material (IBM Plex fonts under SIL OFL 1.1; the lazyway design
kit): see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
