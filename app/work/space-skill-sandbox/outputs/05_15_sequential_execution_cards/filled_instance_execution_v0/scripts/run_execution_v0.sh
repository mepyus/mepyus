#!/usr/bin/env bash
set -euo pipefail

BASE='/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0'
OUT="$BASE/outputs"
PACKET="$BASE/FILLED_BOUNDED_COMBINED_BRIDGE_PACKET_EXECUTION_V0.md"
GEMINI_PROMPT="$BASE/GEMINI_PROMPT_EXECUTION_V0.md"
CODEX_PROMPT="$BASE/CODEX_RECOVERY_PROMPT_EXECUTION_V0.md"
RAW="$OUT/gemini_raw_output.txt"
LITE="$OUT/gemini_lite_output.json"
CODEX_RETURN="$OUT/codex_combined_bridge_recovery_return.md"

stop() {
  echo "STOP: $*" >&2
  exit 2
}

require_explicit_approval() {
  grep -q 'EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes' "$PACKET" || stop 'packet does not grant execution approval: yes'
  grep -q 'APPROVED_PROMOTION: no' "$PACKET" || stop 'promotion boundary missing or not no'
  test "${I_UNDERSTAND_THIS_RUNS_GEMINI_AND_CODEX:-}" = 'yes' || stop 'missing env I_UNDERSTAND_THIS_RUNS_GEMINI_AND_CODEX=yes'
}

case "${1:-}" in
  validate-static)
    python3 "$BASE/scripts/validate_execution_contract_v0.py"
    ;;
  materialize-lite)
    python3 "$BASE/scripts/materialize_gemini_lite_v0.py"
    ;;
  run-gemini-after-approval)
    require_explicit_approval
    mkdir -p "$OUT"
    gemini --approval-mode plan --sandbox --output-format text -p "$(cat "$GEMINI_PROMPT")" > "$RAW"
    python3 "$BASE/scripts/materialize_gemini_lite_v0.py"
    ;;
  run-codex-after-approval)
    require_explicit_approval
    test -s "$RAW" || stop 'missing Gemini raw output'
    test -s "$LITE" || stop 'missing Gemini lite JSON'
    codex exec "$(cat "$CODEX_PROMPT")"
    test -s "$CODEX_RETURN" || stop 'Codex recovery return was not written'
    python3 "$BASE/scripts/validate_codex_recovery_return_v0.py"
    ;;
  validate-codex-return)
    python3 "$BASE/scripts/validate_codex_recovery_return_v0.py"
    ;;
  write-closeout-after-approval)
    require_explicit_approval
    python3 "$BASE/scripts/validate_codex_recovery_return_v0.py"
    python3 "$BASE/scripts/write_hermes_execution_closeout_v0.py"
    ;;
  *)
    cat <<'USAGE'
Usage:
  ./scripts/run_execution_v0.sh validate-static
  ./scripts/run_execution_v0.sh materialize-lite
  ./scripts/run_execution_v0.sh validate-codex-return
  I_UNDERSTAND_THIS_RUNS_GEMINI_AND_CODEX=yes ./scripts/run_execution_v0.sh run-gemini-after-approval
  I_UNDERSTAND_THIS_RUNS_GEMINI_AND_CODEX=yes ./scripts/run_execution_v0.sh run-codex-after-approval
  I_UNDERSTAND_THIS_RUNS_GEMINI_AND_CODEX=yes ./scripts/run_execution_v0.sh write-closeout-after-approval

All real execution subcommands also require the packet to contain:
  EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes

Current prep packet is expected to say no, so real execution must STOP until explicit approval.
USAGE
    ;;
esac
