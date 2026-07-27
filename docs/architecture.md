# Architecture

Second Brain is a portable Markdown vault operated by an AI agent. Its design
keeps source evidence immutable, synthesis inspectable, navigation bounded,
and agent integration replaceable.

The product is not coupled to Cline or any other single harness. Harness
adapters are delivery mechanisms for one canonical set of rules and skills.

## Storage layers

```text
inbox/    →    library/               →    memory/
queue          evidentiary record          agent-maintained synthesis
```

### `inbox/`

The user-controlled drop zone for raw material. Files are processed out of
the inbox; nothing is filed into it.

### `library/`

The immutable evidence layer. Originals are moved and renamed into
`library/YYYY/`, but their bytes are never edited, reformatted, converted, or
deleted. Each year has a catalogue that links the source to related synthesis.

### `memory/`

The agent-authored working-memory layer:

- `people/` for dossiers;
- `meetings/` for dated minutes;
- `projects/` for initiatives and status;
- `decisions/` for ADR-style records;
- `notes/` for reminders and commitments;
- `ideas/` and `topics/` for other synthesis.

Every factual entry is dated. Derived notes identify their source, and answers
distinguish recorded evidence from inference.

## Navigation

The vault uses a bounded two-level navigation tree.

- Root navigation files list child areas and counts.
- Leaf indexes and catalogues list the actual pages or originals.
- A leaf over 300 lines is sharded one level deeper.

This keeps the map reliable for agents with different context windows and
reasoning capabilities. `scripts/health.py` checks counts, links, placement,
and size limits.

`memory/log.md` is the append-only operational history. Every ingest, filing,
update, reindex, check-up, or report adds an entry; prior entries are never
rewritten.

## Portable agent layer

Canonical agent material lives outside harness auto-discovery paths:

```text
AGENTS.md               compact root map and hard invariants
rules/shared/           canonical operating rules
skills/shared/          canonical Agent Skills
```

Generated or thin adapters expose that material to supported agents:

```text
.agents/skills/         Codex, Antigravity, Cline, and compatible agents
.claude/skills/         Claude Code
.agents/rules/          additional rule pointer where required
CLAUDE.md               bridge into AGENTS.md
.clinerules/hooks/      optional host-specific enforcement
```

The adapters do not define product behaviour. They point to or mirror the
canonical material, so changing agents does not change the vault's operating
model.

Host-specific hooks provide defence in depth where an agent supports them.
The portable rules, validation script, and version-control workflow remain
the source of truth, so correctness does not depend on hooks from one harness.

## Synchronising skills

Edit only the canonical source under `skills/shared/`, then regenerate the
adapters:

```bash
./scripts/sync-agent-adapters.sh
```

Verify that generated copies have not drifted:

```bash
./scripts/sync-agent-adapters.sh --check
```

Do not edit `.agents/skills/` or `.claude/skills/` directly.

## Repository layout

| Path | Responsibility |
|---|---|
| `inbox/` | Raw material waiting to be processed |
| `library/YYYY/` | Preserved originals and per-year catalogues |
| `memory/` | Dated synthesis, indexes, reminders, commitments, and log |
| `reports/YYYY/` | Generated reports |
| `reports/templates/` | Reusable report shapes and evolved templates |
| `reports/design/` | Offline HTML design kits and assets |
| `rules/shared/` | Canonical agent rules |
| `skills/shared/` | Canonical task procedures |
| `scripts/` | Health, validation, adapter synchronisation, and PDF export |
| `tests/` | Safety and integrity tests |

## Hard invariants

The root `AGENTS.md` carries the rules that every supported agent must see:

1. Never alter an original under `library/`.
2. Never rewrite the history in `memory/log.md`.
3. Index and log every filing.
4. Date every fact and cite sources in answers.
5. Process out of `inbox/`; never file into it.
6. Run the vault health check after touching library, memory, or navigation.

These invariants matter more than any individual workflow or agent
integration.

## Validation

The project uses local, standard-library checks:

```bash
python3 scripts/health.py
python3 scripts/validate_commit.py
python3 -m unittest discover -s tests
./scripts/sync-agent-adapters.sh --check
```

`validate_commit.py` inspects staged changes and invokes the vault health check
when applicable. It prevents a commit from silently changing protected
history or originals.
