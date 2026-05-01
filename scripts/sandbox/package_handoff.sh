#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  bash scripts/sandbox/package_handoff.sh [--dry-run] [--timeout-seconds N] PACKAGE_DIR

Manual-triggered package handoff.

Expected package files:
  package_brief.md
  gemini_packet.md

This script records transport state and calls run_gemini_packet.sh.
It does not validate Gemini output, apply results, modify source-space,
declare promotion, or run in the background.
USAGE
}

DRY_RUN=0
TIMEOUT_SECONDS=180

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    --timeout-seconds)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for --timeout-seconds" >&2
        exit 2
      fi
      TIMEOUT_SECONDS="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    -*)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
    *)
      break
      ;;
  esac
done

if [[ $# -ne 1 ]]; then
  usage >&2
  exit 2
fi

PACKAGE_DIR="${1%/}"
PACKET_PATH="$PACKAGE_DIR/gemini_packet.md"
BRIEF_PATH="$PACKAGE_DIR/package_brief.md"
LOG_PATH="$PACKAGE_DIR/handoff_log.md"

if [[ ! -d "$PACKAGE_DIR" ]]; then
  echo "Package directory not found: $PACKAGE_DIR" >&2
  exit 1
fi

if [[ ! -f "$BRIEF_PATH" ]]; then
  echo "Missing package_brief.md: $BRIEF_PATH" >&2
  exit 1
fi

if [[ ! -f "$PACKET_PATH" ]]; then
  echo "Missing gemini_packet.md: $PACKET_PATH" >&2
  exit 1
fi

PACKAGE_NAME="$(basename "$PACKAGE_DIR")"
RUN_ID="${PACKAGE_NAME}_handoff"

if [[ ! "$RUN_ID" =~ ^[A-Za-z0-9._-]+$ ]] || [[ "$RUN_ID" == *".."* ]]; then
  echo "Unsafe package-derived run id: $RUN_ID" >&2
  exit 2
fi

mkdir -p "$PACKAGE_DIR/raw" "$PACKAGE_DIR/outbox"

TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
{
  echo "## Handoff $TIMESTAMP"
  echo
  echo "- package_dir: $PACKAGE_DIR"
  echo "- packet: $PACKET_PATH"
  echo "- run_id: $RUN_ID"
  echo "- dry_run: $([[ "$DRY_RUN" -eq 1 ]] && echo true || echo false)"
  echo "- timeout_seconds: $TIMEOUT_SECONDS"
  echo "- state_recorded: sent_to_gemini"
  echo
} >> "$LOG_PATH"

set +e
if [[ "$DRY_RUN" -eq 1 ]]; then
  bash scripts/sandbox/run_gemini_packet.sh --dry-run --timeout-seconds "$TIMEOUT_SECONDS" "$PACKET_PATH" "$RUN_ID"
else
  bash scripts/sandbox/run_gemini_packet.sh --timeout-seconds "$TIMEOUT_SECONDS" "$PACKET_PATH" "$RUN_ID"
fi
RUNNER_EXIT=$?
set -e

{
  echo "## Return $TIMESTAMP"
  echo
  echo "- state_recorded: gemini_runner_returned"
  echo "- runner_exit_code: $RUNNER_EXIT"
  echo "- note: package_collect.sh should gather raw/outbox artifacts for Codex review."
  echo
} >> "$LOG_PATH"

exit "$RUNNER_EXIT"
