# Version-control safety

Treat each completed vault task as one reversible transaction. Commits are
task checkpoints, not a substitute for validation or the vault's append-only
history.

## Before changing files

1. Run `git status --short` and note which paths are already modified or
   untracked.
2. Never alter, discard, stage, or commit pre-existing changes unless the
   principal explicitly includes them in the task.
3. If the current task overlaps pre-existing changes and cannot be isolated
   safely, leave the result uncommitted and explain why.

## After completing a task

1. Run every applicable validation step, including `python3 scripts/health.py`
   when `library/`, `memory/`, an index, or a catalog was touched.
2. Review `git diff` and run `git diff --check`.
3. Stage only the current task's files, using explicit paths. Never use
   `git add .` or `git add -A`.
4. Create one atomic commit when validation passes, the task is complete, no
   unrelated changes are staged, and the diff contains no secrets or
   temporary artefacts.
5. Use a concise message in the form `<operation>: <subject>`, such as
   `ingest: file July planning notes` or
   `report: add weekly programme status`.
6. Report the resulting commit hash to the principal.

## Never do automatically

- Never push unless the principal explicitly asks in the current task.
- Never amend, rebase, squash, reset, clean, or force-update history.
- Never commit unresolved conflicts or failing validation.
- Never commit pre-existing user changes.
- Never claim that a commit was created without verifying it.

To undo a committed task, prefer `git revert <commit>`. Do not rewrite shared
history.
