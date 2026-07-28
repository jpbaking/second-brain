# Second Brain

## Your work has context. Give it memory.

Second Brain is a private, file-based AI executive secretary. Give it notes,
documents, meeting transcripts, decisions, and the facts you would otherwise
forget. Your AI agent organises them into durable working memory, then uses
that memory to brief you, answer questions with citations, prepare meetings,
track commitments, and produce polished reports.

For technical delivery, it can also become the control plane connecting
project scope, requirements, systems and infrastructure, technical and UI/UX
design, work, RAID, decisions, releases, and verification evidence.

It is built for people whose work depends on context: engineering leaders,
architects, managers, consultants, founders, and anyone juggling projects,
people, decisions, and follow-ups.

[Get started](docs/getting-started.md) ·
[Read the user guide](docs/user-guide.md) ·
[See how it works](docs/architecture.md)

## Not another notes app

Most notes systems wait for you to maintain them. Second Brain gives that job
to the agent already helping you work.

| You bring | Second Brain returns |
|---|---|
| Loose notes and source documents | An organised, indexed knowledge base |
| Meetings and conversations | Minutes, decisions, actions, and follow-ups |
| Questions about past work | Answers linked to the recorded evidence |
| Projects and people context | Briefings, status views, and preparation packs |
| Fragmented technical delivery artefacts | One traceable project, system, requirement, design, risk, and release graph |
| Repeated report requests | Reusable reports that retain your formatting feedback |

The result is plain Markdown, HTML, and original files on disk. There is no
proprietary database and no hosted service holding your professional memory.

## Use the AI agent you already use

Second Brain v2 is agent-agnostic. It is not a Cline-only extension and its
knowledge is not tied to any one model or coding-agent harness.

The same canonical rules and skills work across Cline, Claude Code, OpenAI
Codex, Google Antigravity, and Cursor. Thin adapters expose those shared
instructions in the format each agent understands, while your vault remains
portable and readable by people.

Ask in plain language:

> Process my inbox and file everything.

> Prep me for tomorrow's steering meeting.

> What did we decide about the migration, and why?

> Turn the latest project updates into an executive status report.

The agent selects the appropriate vault skill and follows the same safeguards
regardless of the harness.

## Memory you can trust

Second Brain separates evidence from interpretation:

```text
inbox/    →    library/               →    memory/
raw input      untouched originals         dated, cited synthesis
```

- **Originals stay original.** Source files are preserved byte-for-byte.
- **Answers show their work.** Recorded facts carry dates and source links.
- **Nothing gets lost in a folder.** Every filing is indexed and logged.
- **Old green does not masquerade as current truth.** Stale and missing
  information is surfaced instead of guessed.
- **Sensitive context stays under your control.** The vault is designed to be
  kept in a private repository or on local storage.

## Built for real working rhythms

- Start the day with overdue follow-ups, commitments, and what changed.
- Walk into meetings with attendee context, open threads, risks, and talking
  points.
- Capture minutes once and fan out the consequences to project pages, people
  dossiers, decisions, and reminders.
- Review a project or a whole portfolio with evidence-backed status and risks.
- Plan and govern technical projects from charter through requirements,
  system/infra and UI/UX design, release, operational handover, and closure.
- Draft performance evaluations and interview debriefs from recorded evidence,
  with gaps called out rather than papered over.
- Turn a brag log into CV-ready achievements.
- Generate offline HTML reports, documents, and decks, then retain design
  feedback for the next report.

## Start in five minutes

1. Create a private copy of this template.
2. Open the folder with a supported AI coding agent.
3. Drop material into `inbox/`, or simply tell the agent something worth
   remembering.
4. Ask the agent to process the inbox, prepare a brief, recall a decision, or
   create a report.

Python 3 is used for local integrity checks. Chrome or Chromium is optional
for automated PDF export.

Follow the [getting-started guide](docs/getting-started.md) for the complete
setup and first-vault walkthrough.

## Documentation

- [Getting started](docs/getting-started.md) — create a private vault and run
  the first capture, recall, and health check.
- [User guide](docs/user-guide.md) — daily workflows, available skills,
  reports, maintenance, and good prompts.
- [Technical project management](docs/technical-project-management.md) —
  project lifecycle, system/infra and UI/UX source of truth, traceability, and
  release governance.
- [Architecture](docs/architecture.md) — storage layers, safety invariants,
  repository layout, and agent portability.
- [Report design kits](reports/design/README.md) — offline HTML themes and
  customisation.

Agents working inside the repository should begin with
[AGENTS.md](AGENTS.md), the compact root map for the vault's operating rules.

## Privacy

A working vault may contain performance discussions, interview feedback,
commercial context, and personal circumstances. Keep your instance private
and do not sync it anywhere you would not send the same material directly.
This template contains no personal data.

## Licence

The template is released under [0BSD](LICENSE). Vendored fonts and design
assets retain their original terms; see
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
