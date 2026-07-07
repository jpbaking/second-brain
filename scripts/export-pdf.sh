#!/usr/bin/env bash
# Export an HTML report to PDF with headless Chrome/Chromium.
# Usage: scripts/export-pdf.sh <report.html> [output.pdf]
# Page size/orientation come from the report's own @page CSS
# (document.html → A4 portrait, deck.html → 16:9 slides).
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "usage: $0 <report.html> [output.pdf]" >&2
  exit 2
fi

if [ ! -f "$1" ]; then
  echo "error: no such file: $1" >&2
  exit 2
fi
in=$(realpath "$1")
out=${2:-"${in%.html}.pdf"}

chrome=""
for c in google-chrome google-chrome-stable chromium chromium-browser; do
  if command -v "$c" >/dev/null 2>&1; then chrome=$c; break; fi
done
if [ -z "$chrome" ]; then
  echo "No Chrome/Chromium found — open the report in a browser and use Print → Save as PDF instead." >&2
  exit 1
fi

"$chrome" --headless --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf="$out" \
  --virtual-time-budget=4000 \
  "file://$in" 2>/dev/null

echo "PDF written: $out"
