#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  bash scripts/sandbox/run_gemini_packet.sh --preflight
  bash scripts/sandbox/run_gemini_packet.sh [--dry-run] [--smoke-text] [--output-format json|text] [--timeout-seconds N] [PACKET_PATH] RUN_ID

Examples:
  bash scripts/sandbox/run_gemini_packet.sh --preflight
  bash scripts/sandbox/run_gemini_packet.sh --smoke-text --timeout-seconds 60 smoke_text
  bash scripts/sandbox/run_gemini_packet.sh --dry-run app/work/space-skill-sandbox/outputs/next_gemini_task_packet_run_032_tool_affordance_v0.md run_032
  bash scripts/sandbox/run_gemini_packet.sh app/work/space-skill-sandbox/outputs/next_gemini_task_packet_run_032_tool_affordance_v0.md run_032

This script is manually triggered. It does not watch files, install tools,
apply Gemini output, modify source-space, or declare promotion.
USAGE
}

DRY_RUN=0
PREFLIGHT=0
SMOKE_TEXT=0
OUTPUT_FORMAT="json"
TIMEOUT_SECONDS=120
OUT_DIR="app/work/space-skill-sandbox/relay/outbox"
RAW_DIR="app/work/space-skill-sandbox/outputs/gemini_raw_results"
SMOKE_PROMPT='Reply with exactly: GEMINI_SMOKE_OK'

env_present() {
  local name="$1"
  if [[ -n "${!name:-}" ]]; then
    echo "present"
  else
    echo "absent"
  fi
}

gemini_path() {
  command -v gemini 2>/dev/null || true
}

gemini_version() {
  if command -v gemini >/dev/null 2>&1; then
    gemini --version 2>/dev/null || echo "version_unavailable"
  else
    echo "missing"
  fi
}

write_preflight() {
  mkdir -p "$OUT_DIR" "$RAW_DIR"
  local gemini_bin
  gemini_bin="$(gemini_path)"
  echo "# Gemini Runner Preflight"
  echo
  echo "- gemini_binary_exists: $([[ -n "$gemini_bin" ]] && echo true || echo false)"
  echo "- gemini_path: ${gemini_bin:-missing}"
  echo "- gemini_version: $(gemini_version)"
  echo "- timeout_command_exists: $([[ -x /usr/bin/timeout || -x /opt/homebrew/bin/timeout || -x /usr/local/bin/timeout ]] && echo true || echo false)"
  echo "- jq_exists: $(command -v jq >/dev/null 2>&1 && echo true || echo false)"
  echo "- current_working_directory: $(pwd)"
  echo "- outbox_directory_writable: $([[ -w "$OUT_DIR" ]] && echo true || echo false)"
  echo "- raw_results_directory_writable: $([[ -w "$RAW_DIR" ]] && echo true || echo false)"
  echo "- GEMINI_API_KEY: $(env_present GEMINI_API_KEY)"
  echo "- GOOGLE_APPLICATION_CREDENTIALS: $(env_present GOOGLE_APPLICATION_CREDENTIALS)"
  echo "- GOOGLE_CLOUD_PROJECT: $(env_present GOOGLE_CLOUD_PROJECT)"
  echo "- GOOGLE_CLOUD_LOCATION: $(env_present GOOGLE_CLOUD_LOCATION)"
  echo "- GOOGLE_GENAI_USE_VERTEXAI: $(env_present GOOGLE_GENAI_USE_VERTEXAI)"
  echo "- CI: $(env_present CI)"
  echo "- GITHUB_ACTIONS: $(env_present GITHUB_ACTIONS)"
  echo
  echo "Credential values are intentionally not printed."
}

extract_json_response() {
  local raw_file="$1"
  if command -v jq >/dev/null 2>&1; then
    # Try multiple common response paths, fallback to whole JSON if none match
    local extracted
    extracted=$(jq -r '.response // .text // .candidates[0].content.parts[0].text // .content // empty' "$raw_file" 2>/dev/null || echo "")
    if [[ -n "$extracted" ]]; then
      echo "$extracted"
    else
      cat "$raw_file"
    fi
  else
    cat "$raw_file"
  fi
}

detect_likely_state() {
  local raw_file="$1"
  local err_file="$2"
  local fallback="${3:-no_known_issue}"
  if grep -qi "Opening authentication page" "$raw_file" "$err_file" 2>/dev/null; then
    echo "auth_interactive_wait"
  elif grep -qi "No capacity available\\|RESOURCE_EXHAUSTED\\|MODEL_CAPACITY_EXHAUSTED" "$raw_file" "$err_file" 2>/dev/null; then
    echo "model_capacity_or_quota"
  elif grep -qi "Error executing tool\\|Tool .* not found" "$raw_file" "$err_file" 2>/dev/null; then
    echo "tool_configuration_error"
  else
    echo "$fallback"
  fi
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    --preflight)
      PREFLIGHT=1
      shift
      ;;
    --smoke-text)
      SMOKE_TEXT=1
      shift
      ;;
    --output-format)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for --output-format" >&2
        usage >&2
        exit 2
      fi
      OUTPUT_FORMAT="$2"
      shift 2
      ;;
    --timeout-seconds)
      if [[ $# -lt 2 ]]; then
        echo "Missing value for --timeout-seconds" >&2
        usage >&2
        exit 2
      fi
      TIMEOUT_SECONDS="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    --)
      shift
      break
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

if [[ "$PREFLIGHT" -eq 1 ]]; then
  if [[ $# -ne 0 ]]; then
    echo "--preflight does not take packet or run id arguments." >&2
    usage >&2
    exit 2
  fi
  write_preflight
  exit 0
fi

if [[ "$SMOKE_TEXT" -eq 1 ]]; then
  if [[ $# -gt 1 ]]; then
    usage >&2
    exit 2
  fi
  PACKET_PATH=""
  RUN_ID="${1:-smoke_text}"
elif [[ $# -ne 2 ]]; then
  usage >&2
  exit 2
else
  PACKET_PATH="$1"
  RUN_ID="$2"
fi

case "$OUTPUT_FORMAT" in
  json|text) ;;
  *)
    echo "Unsupported --output-format: $OUTPUT_FORMAT" >&2
    echo "Use json or text." >&2
    exit 2
    ;;
esac

if [[ "$SMOKE_TEXT" -ne 1 && ! -f "$PACKET_PATH" ]]; then
  echo "Packet not found: $PACKET_PATH" >&2
  exit 1
fi

if [[ ! "$RUN_ID" =~ ^[A-Za-z0-9._-]+$ ]] || [[ "$RUN_ID" == *".."* ]]; then
  echo "RUN_ID must match [A-Za-z0-9._-]+ and must not contain ..." >&2
  exit 2
fi

if ! [[ "$TIMEOUT_SECONDS" =~ ^[0-9]+$ ]] || [[ "$TIMEOUT_SECONDS" -lt 1 ]]; then
  echo "--timeout-seconds must be a positive integer." >&2
  exit 2
fi

mkdir -p "$OUT_DIR" "$RAW_DIR"

TIMESTAMP="$(date +%Y%m%d_%H%M%S)"
OUT_FILE="$OUT_DIR/${RUN_ID}_gemini_outbox_${TIMESTAMP}.md"
ERR_FILE="$RAW_DIR/${RUN_ID}_gemini_stderr_${TIMESTAMP}.log"

if [[ "$OUTPUT_FORMAT" == "json" ]]; then
  RAW_FILE="$RAW_DIR/${RUN_ID}_gemini_raw_${TIMESTAMP}.json"
else
  RAW_FILE="$RAW_DIR/${RUN_ID}_gemini_raw_${TIMESTAMP}.txt"
fi

{
  echo "# Gemini Run Result"
  echo
  echo "- packet: ${PACKET_PATH:-smoke-text}"
  echo "- run_id: $RUN_ID"
  echo "- timestamp: $TIMESTAMP"
  echo "- dry_run: $([[ "$DRY_RUN" -eq 1 ]] && echo true || echo false)"
  echo "- smoke_text: $([[ "$SMOKE_TEXT" -eq 1 ]] && echo true || echo false)"
  echo "- output_format: $OUTPUT_FORMAT"
  echo "- timeout_seconds: $TIMEOUT_SECONDS"
  echo "- raw_result: $RAW_FILE"
  echo "- stderr_result: $ERR_FILE"
  echo
  echo "## Result"
  echo
} > "$OUT_FILE"

if [[ "$DRY_RUN" -eq 1 ]]; then
  {
    echo "{"
    echo "  \"dry_run\": true,"
    echo "  \"packet\": \"${PACKET_PATH:-smoke-text}\","
    echo "  \"run_id\": \"${RUN_ID}\","
    echo "  \"timestamp\": \"${TIMESTAMP}\","
    echo "  \"note\": \"Gemini CLI was not invoked.\""
    echo "}"
  } > "$RAW_FILE"
  {
    echo "Dry run completed. Gemini CLI was not invoked."
    echo
    echo "Packet preview:"
    echo
    if [[ "$SMOKE_TEXT" -eq 1 ]]; then
      echo "$SMOKE_PROMPT"
    else
      sed -n '1,80p' "$PACKET_PATH"
    fi
  } >> "$OUT_FILE"
else
  if ! command -v gemini >/dev/null 2>&1; then
    echo "gemini command not found. Install/authenticate Gemini CLI before running without --dry-run." >&2
    exit 127
  fi

  GEMINI_BIN="$(gemini_path)"
  GEMINI_VERSION="$(gemini_version)"
  if [[ "$SMOKE_TEXT" -eq 1 ]]; then
    PROMPT="$SMOKE_PROMPT"
  else
    PROMPT="$(cat "$PACKET_PATH")"
  fi

  if [[ "$OUTPUT_FORMAT" == "json" ]]; then
    gemini -p "$PROMPT" --output-format json > "$RAW_FILE" 2> "$ERR_FILE" &
  else
    gemini -p "$PROMPT" > "$RAW_FILE" 2> "$ERR_FILE" &
  fi

  GEMINI_PID=$!
  START_SECONDS="$(date +%s)"
  while kill -0 "$GEMINI_PID" >/dev/null 2>&1; do
    NOW_SECONDS="$(date +%s)"
    if [[ $((NOW_SECONDS - START_SECONDS)) -ge "$TIMEOUT_SECONDS" ]]; then
      LIKELY_STATE="$(detect_likely_state "$RAW_FILE" "$ERR_FILE" "auth_or_network_or_interactive_wait")"
      kill "$GEMINI_PID" >/dev/null 2>&1 || true
      sleep 1
      kill -9 "$GEMINI_PID" >/dev/null 2>&1 || true
      {
        echo "Gemini CLI timed out after ${TIMEOUT_SECONDS} seconds."
        echo
        echo "- timeout_seconds: ${TIMEOUT_SECONDS}"
        echo "- command_attempted: gemini -p \"<prompt redacted>\"$([[ "$OUTPUT_FORMAT" == "json" ]] && echo " --output-format json")"
        echo "- gemini_path: ${GEMINI_BIN:-missing}"
        echo "- gemini_version: ${GEMINI_VERSION}"
        echo "- stderr_result: $ERR_FILE"
        echo "- likely_state: $LIKELY_STATE"
        echo "- next_manual_check: gemini -p \"Reply with exactly: GEMINI_SMOKE_OK\" --output-format json"
        echo
        if [[ -s "$RAW_FILE" ]]; then
          echo "## Raw Tail"
          echo
          tail -40 "$RAW_FILE"
          echo
        fi
        if [[ -s "$ERR_FILE" ]]; then
          echo "## Stderr Tail"
          echo
          tail -40 "$ERR_FILE"
          echo
        fi
        echo "No repository files were modified by this runner."
      } >> "$OUT_FILE"
      echo "Gemini CLI timed out after ${TIMEOUT_SECONDS} seconds." >&2
      echo "Partial result saved:"
      echo "- $OUT_FILE"
      echo "- $RAW_FILE"
      echo "- $ERR_FILE"
      exit 124
    fi
    sleep 1
  done

  set +e
  wait "$GEMINI_PID"
  GEMINI_EXIT=$?
  set -e

  {
    echo
    echo "## Invocation Status"
    echo
    echo "- gemini_exit_code: $GEMINI_EXIT"
    echo "- likely_state: $(detect_likely_state "$RAW_FILE" "$ERR_FILE")"
    if [[ -s "$ERR_FILE" ]]; then
      echo "- stderr_nonempty: true"
    else
      echo "- stderr_nonempty: false"
    fi
    echo
  } >> "$OUT_FILE"

  if [[ "$OUTPUT_FORMAT" == "json" ]]; then
    extract_json_response "$RAW_FILE" >> "$OUT_FILE"
  else
    cat "$RAW_FILE" >> "$OUT_FILE"
  fi

  if [[ "$GEMINI_EXIT" -ne 0 ]]; then
    {
      echo
      echo "## Stderr Tail"
      echo
      if [[ -s "$ERR_FILE" ]]; then
        tail -80 "$ERR_FILE"
      else
        echo "No stderr was captured."
      fi
    } >> "$OUT_FILE"
    echo "Gemini CLI exited with code $GEMINI_EXIT." >&2
    echo "Result saved:"
    echo "- $OUT_FILE"
    echo "- $RAW_FILE"
    echo "- $ERR_FILE"
    exit "$GEMINI_EXIT"
  fi
fi

echo "Gemini result saved:"
echo "- $OUT_FILE"
echo "- $RAW_FILE"
echo "- $ERR_FILE"
