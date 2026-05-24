#!/usr/bin/env bash
set -euo pipefail
BASE='/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/candidate_to_component_review_packet_v0'
OUT="$BASE/outputs"
PACKET="$BASE/CANDIDATE_TO_COMPONENT_REVIEW_PACKET_V0.md"
PROMPT="$BASE/GEMINI_C2C_REVIEW_PROMPT_V0.md"
RAW="$OUT/gemini_c2c_raw_output.txt"
LITE="$OUT/gemini_c2c_lite_output.json"
CODEX_RETURN="$OUT/codex_c2c_recovery_return.md"
stop() { echo "STOP: $*" >&2; exit 2; }
require_approval() {
  grep -q 'EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes' "$PACKET" || stop 'C2C packet does not grant execution approval: yes'
  grep -q 'APPROVED_PROMOTION: no' "$PACKET" || stop 'promotion boundary missing or not no'
  grep -q 'APPROVED_VECTORFL_AUTHORITY_MUTATION: no' "$PACKET" || stop 'authority boundary missing or not no'
  test "${I_UNDERSTAND_THIS_RUNS_C2C_GEMINI_CODEX:-}" = 'yes' || stop 'missing env I_UNDERSTAND_THIS_RUNS_C2C_GEMINI_CODEX=yes'
}
case "${1:-}" in
  validate-static)
    python3 "$BASE/scripts/validate_c2c_contract_v0.py" ;;
  guard-stop-probe)
    require_approval ;;
  run-gemini-after-approval)
    require_approval
    mkdir -p "$OUT"
    gemini --approval-mode yolo --sandbox --output-format text -p "$(cat "$PROMPT")" > "$RAW" ;;
  materialize-lite)
    python3 "$BASE/scripts/materialize_c2c_lite_v0.py" ;;
  run-codex-after-approval)
    require_approval
    test -s "$RAW" || stop 'missing C2C Gemini raw output'
    test -s "$LITE" || stop 'missing C2C Gemini lite JSON'
    codex exec "$(cat "$BASE/CODEX_C2C_RECOVERY_PROMPT_V0.md")"
    test -s "$CODEX_RETURN" || stop 'C2C Codex recovery return was not written' ;;
  *) echo 'Usage: validate-static | guard-stop-probe | run-gemini-after-approval | materialize-lite | run-codex-after-approval' ;;
esac
