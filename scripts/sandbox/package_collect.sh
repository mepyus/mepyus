#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  bash scripts/sandbox/package_collect.sh PACKAGE_DIR

Collect central Gemini runner artifacts into a package folder and write a
Codex-readable review bundle. This script does not judge success, apply
Gemini output, modify source-space, declare promotion, or run automation.
USAGE
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ $# -ne 1 ]]; then
  usage >&2
  exit 2
fi

PACKAGE_DIR="${1%/}"
if [[ ! -d "$PACKAGE_DIR" ]]; then
  echo "Package directory not found: $PACKAGE_DIR" >&2
  exit 1
fi

PACKAGE_NAME="$(basename "$PACKAGE_DIR")"
RUN_ID="${PACKAGE_NAME}_handoff"

if [[ ! "$RUN_ID" =~ ^[A-Za-z0-9._-]+$ ]] || [[ "$RUN_ID" == *".."* ]]; then
  echo "Unsafe package-derived run id: $RUN_ID" >&2
  exit 2
fi

CENTRAL_OUTBOX="app/work/space-skill-sandbox/relay/outbox"
CENTRAL_RAW="app/work/space-skill-sandbox/outputs/gemini_raw_results"
PACKAGE_OUTBOX="$PACKAGE_DIR/outbox"
PACKAGE_RAW="$PACKAGE_DIR/raw"
REVIEW_BUNDLE="$PACKAGE_DIR/codex_review_bundle.md"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"

mkdir -p "$PACKAGE_OUTBOX" "$PACKAGE_RAW"

OUTBOX_FOUND=0
RAW_FOUND=0

for file in "$CENTRAL_OUTBOX"/"${RUN_ID}"_gemini_outbox_*.md; do
  if [[ -f "$file" ]]; then
    cp "$file" "$PACKAGE_OUTBOX/"
    OUTBOX_FOUND=$((OUTBOX_FOUND + 1))
  fi
done

for file in "$CENTRAL_RAW"/"${RUN_ID}"_gemini_raw_* "$CENTRAL_RAW"/"${RUN_ID}"_gemini_stderr_*.log; do
  if [[ -f "$file" ]]; then
    cp "$file" "$PACKAGE_RAW/"
    RAW_FOUND=$((RAW_FOUND + 1))
  fi
done

{
  echo "# Codex Review Bundle"
  echo
  echo "- package_dir: $PACKAGE_DIR"
  echo "- run_id: $RUN_ID"
  echo "- collected_at: $TIMESTAMP"
  echo "- outbox_files_collected: $OUTBOX_FOUND"
  echo "- raw_files_collected: $RAW_FOUND"
  echo
  echo "## Package Files"
  echo
  find "$PACKAGE_DIR" -maxdepth 2 -type f | sort
  echo
  echo "## Review Note"
  echo
  echo "This bundle is transport evidence only. Codex must validate content and boundaries separately."
} > "$REVIEW_BUNDLE"

echo "Package artifacts collected:"
echo "- $REVIEW_BUNDLE"
echo "- outbox_files_collected: $OUTBOX_FOUND"
echo "- raw_files_collected: $RAW_FOUND"
