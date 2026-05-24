#!/usr/bin/env bash
set -euo pipefail
BASE='/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0'
OUT="$BASE/outputs"
PACKET="$BASE/GEMINI_SCOPE_GAP_BOUNDED_EVIDENCE_PACKET_V0.md"
PROMPT="$BASE/GEMINI_SCOPE_GAP_REVIEW_PROMPT_V0.md"
RAW="$OUT/gemini_scope_gap_raw_output.txt"
LITE="$OUT/gemini_scope_gap_lite_output.json"
CODEX_RETURN="$OUT/codex_scope_gap_recovery_return.md"
stop() { echo "STOP: $*" >&2; exit 2; }
require_approval() {
  grep -q 'EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes' "$PACKET" || stop 'scope-gap packet does not grant execution approval: yes'
  grep -q 'APPROVED_PROMOTION: no' "$PACKET" || stop 'promotion boundary missing or not no'
  grep -q 'APPROVED_VECTORFL_AUTHORITY_MUTATION: no' "$PACKET" || stop 'authority boundary missing or not no'
  test "${I_UNDERSTAND_THIS_RUNS_SCOPE_GAP_GEMINI_CODEX:-}" = 'yes' || stop 'missing env I_UNDERSTAND_THIS_RUNS_SCOPE_GAP_GEMINI_CODEX=yes'
}
case "${1:-}" in
  validate-static)
    python3 "$BASE/scripts/validate_scope_gap_execution_contract_v0.py" ;;
  guard-stop-probe)
    require_approval ;;
  run-gemini-after-approval)
    require_approval
    mkdir -p "$OUT"
    gemini --approval-mode plan --sandbox --output-format text -p "$(cat "$PROMPT")" > "$RAW" ;;
  materialize-lite)
    python3 "$BASE/scripts/materialize_scope_gap_lite_v0.py" ;;
  run-codex-after-approval)
    require_approval
    test -s "$RAW" || stop 'missing scope-gap Gemini raw output'
    test -s "$LITE" || stop 'missing scope-gap Gemini lite JSON'
    codex exec "$(cat "$BASE/CODEX_SCOPE_GAP_RECOVERY_PROMPT_V0.md")"
    test -s "$CODEX_RETURN" || stop 'scope-gap Codex recovery return was not written' ;;
  write-closeout-after-approval)
    require_approval
    test -s "$CODEX_RETURN" || stop 'missing scope-gap Codex return'
    python3 "$BASE/scripts/write_scope_gap_closeout_v0.py" ;;
  *)
    echo 'Usage: validate-static | guard-stop-probe | run-gemini-after-approval | materialize-lite | run-codex-after-approval | write-closeout-after-approval' ;;
esac
