# Getting started

This guide takes a new Second Brain from an empty template to its first
captured material, cited answer, and health check.

Second Brain is agent-agnostic. The steps are the same whether you use Cline,
Claude Code, OpenAI Codex, Google Antigravity, Cursor, or another agent that
can follow repository instructions and Agent Skills.

## What you need

- A supported AI coding agent with access to the vault folder.
- Python 3 for the integrity and commit-safety checks. The scripts use only
  the standard library.
- Chrome or Chromium only if you want automated PDF export from HTML reports.
- A private place to store the vault. A private Git repository is useful for
  history and recovery, but is not required.

## 1. Create a private vault

Use GitHub's **Use this template** action to create a new private repository,
then clone that private copy:

```bash
git clone git@github.com:YOUR_ACCOUNT/YOUR_PRIVATE_VAULT.git my-second-brain
cd my-second-brain
```

Confirm the destination is private before adding any real work or people
data. You can keep the public template as an `upstream` remote if you want to
bring future improvements into your private vault deliberately.

The template begins with an empty `inbox/`, an empty `library/`, and the
indexes and templates needed to grow the `memory/` layer safely.

## 2. Open the folder with your agent

Open the repository root, not an individual subfolder. The agent discovers
the root guidance in `AGENTS.md` through the adapter supported by its harness.
That file routes it to the canonical rules in `rules/shared/` and the
task-specific skills in `skills/shared/`.

You should not need a harness-specific command. Describe the outcome in plain
language, or explicitly name a skill:

> Give me a daily brief from this vault.

> Use the `vault-inbox` skill to process everything waiting in the inbox.

## 3. Capture the first material

Put a note, document, transcript, screenshot, or export into `inbox/`. Then
ask:

> Process my inbox.

The agent will:

1. Preserve the original under `library/YYYY/` with a dated filename.
2. Create dated synthesis under the relevant area of `memory/`.
3. Update the appropriate leaf indexes and library catalogue.
4. Append the operation to `memory/log.md`.
5. Reindex the vault search service and run the health check.

The original is evidentiary material. The agent may move and rename it during
filing, but must never edit, reformat, convert, or delete it.

## 4. Capture something from conversation

You do not need a source file for every useful fact. Tell the agent:

> Remember that the platform migration decision is due on 15 August 2026.

The `vault-remember` procedure files the dated fact in `memory/`, updates
navigation, and records the capture in the log. Relative dates such as
"tomorrow" are converted to absolute dates when filed.

## 5. Ask a question

Try a question that the captured material can answer:

> What do we know about the platform migration? Cite the source.

The agent searches the vault index before opening files, cites the relevant
line ranges, and separates recorded evidence from its own inference. If the
vault does not contain the answer, it should say so rather than filling the
gap.

## 6. Check the vault

Run the local health check:

```bash
python3 scripts/health.py
```

It checks navigation counts and links, filing placement, inbox backlog,
oversized indexes, overdue commitments, stale dossiers, and unresolved
markers.

You can also ask:

> Run a vault check-up and fix any documentation drift you find.

The agent will use the `vault-checkup` procedure for the mechanical checks and
the judgement calls a script cannot make.

## Next steps

- Read the [user guide](user-guide.md) for common workflows and prompts.
- Read [architecture](architecture.md) to understand the storage model and
  portable agent adapters.
- Review the [report design kits](../reports/design/README.md) before building
  recurring documents or decks.
