# User guide

Second Brain works best when you treat the agent as an executive secretary:
give it raw context, ask for an outcome, and let the vault procedures handle
filing, retrieval, and follow-through.

The vault is not tied to one AI harness. Use plain-language requests with any
supported agent; naming a skill explicitly is useful when you want a precise
procedure.

## The everyday loop

Most work follows four movements:

1. **Capture** source material or something said in conversation.
2. **Organise** it into dated, indexed memory without altering the evidence.
3. **Retrieve** relevant context with citations when it becomes useful.
4. **Act** through a brief, meeting pack, decision record, status view, or
   report.

You do not need to decide where every item belongs. If the right destination
is unclear, the agent files it in `memory/topics/`, records the uncertainty,
and asks afterwards.

## Capture

### Process files

Drop raw material into `inbox/` and ask:

> Process everything in my inbox.

Use `vault-inbox` for notes, transcripts, PDFs, screenshots, exports, and
other source files. Originals move into the year-sharded `library/`; all
summaries and extracted facts go into `memory/`.

Never manually use `inbox/` as a long-term folder. It is a queue to process
out of, not a filing destination.

### Remember chat context

Use `vault-remember` for facts shared directly with the agent:

> Remember that Priya completed the security review on 24 July 2026.

> Note that I owe Finance a revised forecast by 31 July 2026.

The agent dates and files the fact, updates the relevant dossier, project, or
commitment page, and logs the change.

### File a meeting

Give `vault-meeting` raw minutes or a verbal recap. It produces a meeting
record and fans out the consequences:

- decisions to the decision index;
- actions to reminders or commitments;
- project changes to project pages;
- relevant facts to people dossiers.

This prevents useful details from being trapped in a chronological meeting
note.

## Recall and preparation

### Ask the vault

Use `vault-recall` for questions about people, projects, meetings, decisions,
and past work:

> What did we agree about the authentication migration?

> What evidence do we have for the current delivery risk?

> When did the client first raise the data-residency concern?

Answers cite the relevant vault paths and line ranges. Recorded fact and agent
inference are labelled separately.

### Prepare for a meeting

Use `vault-prep` for a meeting pack containing:

- short attendee context;
- open threads in both directions;
- current project state;
- likely risks or landmines;
- suggested talking points.

Use `vault-one-on-one` for a 1:1. It adds recognition, carry-over from the last
conversation, follow-ups in both directions, goal pulse, and useful probes.
The same skill files the notes afterwards.

## Decisions, projects, and people

### Record a decision

Use `vault-decision` to create an ADR-style record with the context, chosen
option, rejected alternatives, reasons, consequences, and revisit trigger.

> Record the decision to keep the identity service in-house, including the
> managed-service option we rejected.

### Review project status

Use `vault-project-status` for one project or the whole portfolio. Status is
derived from dated evidence, with movement, risks, dependencies, and asks.
Stale information is reported as stale or unknown rather than carried forward
as current green status.

### Run full technical project management

The vault can act as the control plane for product, systems, infrastructure,
data, security, and UI/UX delivery. Stable project, asset, requirement,
design, work, RAID, and release records connect approved intent to evidence.

Use:

- `vault-project-plan` to charter, plan, baseline, or rebaseline;
- `vault-project-update` to reconcile progress and changes across registers;
- `vault-requirements` for acceptance, non-functional requirements, coverage,
  and change control;
- `vault-system-map` for systems, services, APIs, data, infrastructure,
  environments, ownership, interfaces, and UI surfaces;
- `vault-design` for technical, infrastructure, security, UI, and UX design;
- `vault-release` for readiness, go/no-go, rollout, rollback, and verification;
- `vault-project-close` for outcomes, operational handover, residual
  obligations, lessons, and closure.

See the [technical project-management guide](technical-project-management.md)
for the complete lifecycle and prompt examples.

### Work with people evidence

People dossiers collect dated goals, accomplishments, feedback, follow-ups,
and relevant meeting context.

- `performance-evaluation` drafts an evidence-based review and identifies
  missing support.
- `interview-debrief` structures candidate feedback against the recorded
  rubric and keeps sensitive material appropriately scoped.
- `vault-cv-update` turns your own accomplishment log into CV-ready bullets
  and compares them with the last saved CV snapshot.

The agent asks before creating a document that asserts a judgement about a
person.

## Briefs, reviews, and handoffs

Use recurring procedures to keep the vault active:

| Skill | Best used for |
|---|---|
| `vault-brief` | What needs attention now, overdue follow-ups, and recent change |
| `vault-weekly` | A weekly sweep of commitments, people, projects, decisions, and the week ahead |
| `vault-handoff` | An out-of-office delegation pack and a re-entry brief |
| `vault-checkup` | Mechanical health plus contradictions, staleness, and thin synthesis |
| `vault-reindex` | Rebuilding navigation and counts from what is actually on disk |

A useful rhythm is a short brief each morning and a weekly review before
planning the next week.

## Reports

Use `report-builder` for status reports, pre-reads, one-pagers, summaries,
documents, decks, and interactive HTML pages. It searches the vault for
evidence, reports data gaps, and reuses any formatting feedback you have
already given.

The bundled HTML reports are fully offline. Two design kits live under
`reports/design/`, and three reusable shapes live under
`reports/templates/`:

- `document` for A4-style reading and printing;
- `deck` for 16:9 slides;
- `interactive` for a responsive one-page experience.

Export HTML to PDF through the browser print dialog or:

```bash
scripts/export-pdf.sh reports/YYYY/example-report.html
```

See the [design-kit guide](../reports/design/README.md) for customisation.

## Skill reference

You may describe the task naturally or say "use the `<skill-name>` skill".

| Skill | Purpose |
|---|---|
| `vault-inbox` | Process raw files into preserved originals and indexed memory |
| `vault-remember` | Capture a fact, reminder, commitment, or update from chat |
| `vault-recall` | Answer from the vault with citations |
| `vault-meeting` | File minutes and distribute their consequences |
| `vault-prep` | Prepare for a meeting |
| `vault-one-on-one` | Prepare for or capture a 1:1 |
| `vault-decision` | Record or retrieve an ADR-style decision |
| `vault-project-status` | Report one-project or portfolio status |
| `vault-project-plan` | Charter, plan, baseline, or rebaseline technical delivery |
| `vault-project-update` | Reconcile delivery evidence across all technical registers |
| `vault-requirements` | Capture, approve, change, trace, and verify requirements |
| `vault-system-map` | Map systems, infrastructure, interfaces, environments, and UI surfaces |
| `vault-design` | Create or review technical, infrastructure, security, UI, or UX design |
| `vault-release` | Govern readiness, rollout, rollback, and post-release evidence |
| `vault-project-close` | Audit outcomes, handover, residual obligations, and closure |
| `vault-brief` | Produce a concise attention brief |
| `vault-weekly` | Run the weekly review and sweep |
| `vault-handoff` | Prepare absence and return handoffs |
| `vault-cv-update` | Convert your accomplishment log into CV material |
| `vault-checkup` | Audit mechanical and judgement-level vault health |
| `vault-reindex` | Rebuild navigation from disk |
| `performance-evaluation` | Draft an evidence-based performance evaluation |
| `interview-debrief` | Capture structured interview feedback |
| `report-builder` | Build reusable Markdown or HTML reports |
| `claude-report-design` | Apply the warm ivory and terracotta report design kit |

The lazyway report kit uses the separately maintained
[`lazyway-io-design`](https://github.com/jpbaking/lazyway-io-design) skill.

## Maintenance

Run these from the repository root:

```bash
python3 scripts/health.py
python3 scripts/project_health.py --strict
./scripts/sync-agent-adapters.sh --check
python3 -m unittest discover -s tests
```

- `health.py` verifies vault structure and flags time-sensitive items.
- `project_health.py` validates technical record identity, lifecycle,
  traceability, authority freshness, evidence, release, and closure gates.
- `sync-agent-adapters.sh --check` confirms all agent adapters match the
  canonical skills.
- The unit tests exercise the safeguards around original files and append-only
  history.

When editing a canonical skill, change `skills/shared/` and then run
`./scripts/sync-agent-adapters.sh`. Never edit `.agents/skills/` or
`.claude/skills/` directly.

## Privacy and sharing

Assume vault content is confidential. Keep the repository private and review
generated reports before sharing them.

When requesting a shareable report, name the audience. The agent should scope
the material accordingly and say what sensitive or irrelevant context it
excluded.

Do not place credentials, API keys, or secrets in the vault. Use the secret
management mechanism appropriate to the system that needs them.

## Prompt patterns

Strong requests state the outcome and useful scope:

> Prep me for the programme review on 3 August 2026. Focus on delivery risk,
> open decisions, and what I need from Finance.

> Produce a one-page project status for the leadership team. Exclude people
> performance details and flag anything older than 30 days.

> Capture these meeting notes, then tell me which actions have no owner or due
> date.

> Compare the decision record with what the last two meeting notes say. Label
> contradictions and inference.

The procedures provide the filing mechanics. Your prompt should supply the
decision, audience, or emphasis that only you can choose.
