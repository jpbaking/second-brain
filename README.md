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
2. **Requirements:** any supported coding agent — [Cline](https://cline.bot),
   Claude Code, OpenAI Codex, Google Antigravity, or Cursor; `python3`
   (stdlib only, for the health check and hooks); Chrome/Chromium
   (optional, for agent-side PDF export).
3. **Open the folder in your agent.** It reads `AGENTS.md` (Claude Code
   reads `CLAUDE.md`, which imports it), which routes to the rules in
   `rules/shared/`. Skills are discovered from `.agents/skills/` (Codex,
   Antigravity, Cline) or `.claude/skills/` (Claude Code). Cline
   additionally runs the hooks in `.clinerules/hooks/`.
4. **Start using it:** drop files into `inbox/` and ask the agent to use
   the `vault-inbox` skill — or just tell it about your team, meetings,
   and projects. Ask it anything later.

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
| *"Steering meeting with KDDI folks tomorrow — prep me"* | Prep pack: attendee one-liners, open threads, landmines, talking points |
| *"I've got a 1:1 with Sam"* | 1:1 arc: recognise / follow up / probe / goal pulse / carry-over |
| *"Draft Sam's performance eval"* | Evidence-based draft from goals + dated entries; flags gaps loudly |
| *"Where do the projects stand?"* | Portfolio RAG rollup; stale statuses report as "unknown", not old green |
| *"What's on today?"* | Overdue reminders/commitments, upcoming dates, loose ends |
| *"Make that report a deck instead"* + feedback | Report re-done; your formatting persisted as a template for next time |

## Vault skills

Describe the task and the agent picks the skill, or name it explicitly —
"use the `vault-inbox` skill". Most harnesses also accept `/vault-inbox`;
Codex uses `$` then the skill name.

| Skill | Does |
|---|---|
| `vault-inbox` | Process everything in `inbox/` into `library/` + `memory/` |
| `vault-remember` | File facts you just said in chat |
| `vault-recall` | Answer a question with sources cited |
| `vault-meeting` | File meeting minutes; fan out decisions/actions/people facts |
| `vault-prep` | Meeting prep pack |
| `vault-one-on-one` | 1:1 prep and post-1:1 capture |
| `vault-decision` | Record a decision (ADR-style: options, rejections, revisit date) |
| `vault-project-status` | Single-project deep dive or portfolio RAG rollup |
| `vault-cv-update` | Turn the principal's brag log into CV-ready bullets |
| `vault-brief` | Daily brief |
| `vault-weekly` | Weekly review: sweep, nudge list, people pulse, look ahead |
| `vault-handoff` | Out-of-office handoff and re-entry brief |
| `vault-reindex` | Rebuild the navigation tree from disk |
| `vault-checkup` | Health check + judgment-level hygiene |

## Document skills

| Skill | Does |
|---|---|
| `performance-evaluation` | Evidence-based eval drafts from dossier + goals + meetings |
| `interview-debrief` | Structured candidate feedback vs your rubric; HR-sensitive handling |
| `report-builder` | The template-evolution loop for recurring reports |
| `claude-report-design` | Rules for `claude.*` HTML reports (light/dark kit) |

`lazyway.*` HTML reports use the `lazyway-io-design` skill, which is
installed user-global from
[its own repo](https://github.com/jpbaking/lazyway-io-design) rather than
vendored here — a project copy would be shadowed by the global one.

## Hooks (`.clinerules/hooks/`, Cline-only, Python, fail-open)

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
  links, navigation size rule, overdue items, stale dossiers. Run by the
  `vault-checkup` and `vault-weekly` skills.
- `vault-reindex` skill — rebuilds the tree when drift is found.
- `./scripts/sync-agent-adapters.sh` — regenerates `.agents/skills/` and
  `.claude/skills/` from `skills/shared/`; `--check` fails on drift.

## Repo layout

| Path | What | Written by |
|---|---|---|
| `inbox/` | Raw dumps, unprocessed | You |
| `library/YYYY/` | Originals, byte-for-byte untouched, per-year catalogs | Agent (move/rename only) |
| `memory/` | People, meetings, projects, decisions, notes, ideas, topics + root index + append-only log | Agent |
| `reports/` | Generated reports (`YYYY/`), templates, design kits | Agent |
| `scripts/` | `health.py`, `export-pdf.sh`, `sync-agent-adapters.sh` | — |
| `AGENTS.md` | Root map — hard invariants + routing (all agents but Claude Code) | You + agent |
| `CLAUDE.md` | One-line `@AGENTS.md` bridge for Claude Code | You + agent |
| `rules/shared/` | **Canonical** always-on rules | You + agent |
| `skills/shared/` | **Canonical** on-demand skills | You + agent |
| `.agents/skills/`, `.claude/skills/` | Generated skill adapters — never edit | `sync-agent-adapters.sh` |
| `.agents/rules/` | Pointer rule for Antigravity | You + agent |
| `.clinerules/hooks/` | Cline-only enforcement hooks | You + agent |

## Multi-harness support

The vault follows the [Universal Agent Support
Playbook](https://github.com/jpbaking/agent-commons/blob/main/MULTI-HARNESS-SUPPORT.md):
one canonical source, thin per-harness adapters.

| Harness | Reaches the rules via | Finds skills in |
|---|---|---|
| Cline | `AGENTS.md` | `.agents/skills/` |
| OpenAI Codex | `AGENTS.md` | `.agents/skills/` |
| Google Antigravity | `AGENTS.md` + `.agents/rules/` | `.agents/skills/` |
| Cursor | `AGENTS.md` | `.agents/skills/` |
| Claude Code | `CLAUDE.md` → `@AGENTS.md` | `.claude/skills/` |

Whatever the harness, the portable instruction is the same: **"use the
`vault-inbox` skill"**. Explicit invocation differs — `/vault-inbox` in
Claude Code, Antigravity, and Cline; `$` then the skill name in Codex — but
plain-language mention works everywhere.

If you are an agent working in this repo: start at [AGENTS.md](AGENTS.md).
It lists the hard invariants and routes you to the detailed rules in
`rules/shared/` per task — the same small-root, detail-in-leaves shape as
the vault's own indexes.

## Privacy

The private instance will hold performance evaluations, attrition risks,
and interview feedback. Keep it private; don't sync it anywhere you
wouldn't email it. Initialise git only after confirming no personal data
is present (this template ships clean).

## License

Template: [0BSD](LICENSE) — use it for anything, no attribution needed.
Vendored material (IBM Plex fonts under SIL OFL 1.1; the lazyway design
kit): see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
