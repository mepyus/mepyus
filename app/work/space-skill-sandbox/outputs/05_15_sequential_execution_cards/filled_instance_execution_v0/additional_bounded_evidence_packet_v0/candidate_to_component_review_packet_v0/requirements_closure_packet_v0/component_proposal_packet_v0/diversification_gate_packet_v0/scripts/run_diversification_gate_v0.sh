#!/usr/bin/env bash
set -euo pipefail
BASE='/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/filled_instance_execution_v0/additional_bounded_evidence_packet_v0/candidate_to_component_review_packet_v0/requirements_closure_packet_v0/component_proposal_packet_v0/diversification_gate_packet_v0'
OUT="$BASE/outputs"
PACKET="$BASE/DIVERSIFICATION_GATE_PACKET_V0.md"
PROMPT="$BASE/GEMINI_DIVERSIFICATION_PROMPT_V0.md"
RAW="$OUT/gemini_diversification_raw_output.txt"
LITE="$OUT/gemini_diversification_lite_output.json"
CODEX_RETURN="$OUT/codex_diversification_recovery_return.md"
stop() { echo "STOP: $*" >&2; exit 2; }
require_approval() {
 grep -q 'EXECUTION_APPROVAL_GRANTED_FOR_THIS_PACKET: yes' "$PACKET" || stop 'execution approval missing'
 grep -q 'APPROVED_DIVERSIFICATION_REVIEW: yes' "$PACKET" || stop 'diversification review approval missing'
 grep -q 'APPROVED_PROMOTION: no' "$PACKET" || stop 'promotion boundary missing'
 grep -q 'APPROVED_VECTORFL_AUTHORITY_MUTATION: no' "$PACKET" || stop 'authority boundary missing'
 grep -q 'APPROVED_REGISTRY_SCHEMA_WORKFLOW_INTEGRATION: no' "$PACKET" || stop 'registry/schema/workflow boundary missing'
 test "${I_UNDERSTAND_THIS_RUNS_DIVERSIFICATION_GEMINI_CODEX:-}" = 'yes' || stop 'missing env I_UNDERSTAND_THIS_RUNS_DIVERSIFICATION_GEMINI_CODEX=yes'
}
case "${1:-}" in
 validate-static) python3 "$BASE/scripts/validate_diversification_contract_v0.py" ;;
 guard-stop-probe) require_approval ;;
 run-gemini-after-approval) require_approval; mkdir -p "$OUT"; gemini --approval-mode yolo --sandbox --output-format text -p "$(cat "$PROMPT")" > "$RAW" ;;
 materialize-lite) python3 "$BASE/scripts/materialize_diversification_lite_v0.py" ;;
 run-codex-after-approval) require_approval; test -s "$RAW" || stop 'missing Gemini raw'; test -s "$LITE" || stop 'missing Gemini lite'; codex exec "$(cat "$BASE/CODEX_DIVERSIFICATION_RECOVERY_PROMPT_V0.md")"; test -s "$CODEX_RETURN" || stop 'Codex return missing' ;;
 *) echo 'Usage: validate-static | guard-stop-probe | run-gemini-after-approval | materialize-lite | run-codex-after-approval' ;;
esac
