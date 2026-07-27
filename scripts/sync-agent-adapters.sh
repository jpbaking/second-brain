#!/usr/bin/env bash
# Regenerate the harness skill adapters from the canonical source tree.
#
#   skills/shared/<name>/  ->  .agents/skills/<name>/   (Codex, Antigravity, Cline)
#                          ->  .claude/skills/<name>/   (Claude Code)
#
# The adapters are GENERATED. Never edit them directly — edit skills/shared/
# and re-run this script. Run with --check to verify they are in sync without
# writing anything (exit 1 on drift).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/skills/shared"
TARGETS=(".agents/skills" ".claude/skills")

[ -d "$SRC" ] || { echo "missing canonical source: $SRC" >&2; exit 1; }

if [ "${1:-}" = "--check" ]; then
    status=0
    for target in "${TARGETS[@]}"; do
        if ! diff -r "$SRC" "$ROOT/$target" >/dev/null 2>&1; then
            echo "DRIFT: $target differs from skills/shared/" >&2
            diff -rq "$SRC" "$ROOT/$target" >&2 || true
            status=1
        fi
    done
    [ $status -eq 0 ] && echo "adapters in sync with skills/shared/"
    exit $status
fi

for target in "${TARGETS[@]}"; do
    rm -rf "${ROOT:?}/$target"
    mkdir -p "$ROOT/$target"
    cp -R "$SRC/." "$ROOT/$target/"
    echo "synced $target ($(find "$ROOT/$target" -name SKILL.md | wc -l) skills)"
done
