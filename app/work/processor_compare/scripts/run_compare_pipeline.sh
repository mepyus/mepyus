#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPTS_DIR="$ROOT_DIR/scripts"
RAW_DIR="$ROOT_DIR/processor_outputs/raw"
NORMALIZED_DIR="$ROOT_DIR/processor_outputs/normalized"
REPORTS_DIR="$ROOT_DIR/reports"

step() {
  echo ""
  echo "[STEP] $1"
}

fail() {
  echo "[FAIL] $1" >&2
  exit 1
}

step "validate raw/codex"
python3 "$SCRIPTS_DIR/validate_processor_output.py" "$RAW_DIR/codex" --processor codex || fail "validate raw/codex"

step "validate raw/chatgpt"
python3 "$SCRIPTS_DIR/validate_processor_output.py" "$RAW_DIR/chatgpt" --processor chatgpt || fail "validate raw/chatgpt"

step "validate raw/gemini"
python3 "$SCRIPTS_DIR/validate_processor_output.py" "$RAW_DIR/gemini" --processor gemini || fail "validate raw/gemini"

step "normalize codex"
python3 "$SCRIPTS_DIR/normalize_processor_output.py" \
  "$RAW_DIR/codex" \
  "$NORMALIZED_DIR/codex/normalized.jsonl" \
  --processor codex || fail "normalize codex"

step "normalize chatgpt"
python3 "$SCRIPTS_DIR/normalize_processor_output.py" \
  "$RAW_DIR/chatgpt" \
  "$NORMALIZED_DIR/chatgpt/normalized.jsonl" \
  --processor chatgpt || fail "normalize chatgpt"

step "normalize gemini"
python3 "$SCRIPTS_DIR/normalize_processor_output.py" \
  "$RAW_DIR/gemini" \
  "$NORMALIZED_DIR/gemini/normalized.jsonl" \
  --processor gemini || fail "normalize gemini"

step "compare normalized outputs"
python3 "$SCRIPTS_DIR/compare_processor_outputs.py" \
  --codex "$NORMALIZED_DIR/codex/normalized.jsonl" \
  --chatgpt "$NORMALIZED_DIR/chatgpt/normalized.jsonl" \
  --gemini "$NORMALIZED_DIR/gemini/normalized.jsonl" \
  --reports-dir "$REPORTS_DIR" || fail "compare normalized outputs"

echo ""
echo "[DONE] reports generated in $REPORTS_DIR"
