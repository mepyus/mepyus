# VectorFL Receipt Writer Shape Candidate V0

status: FUNCTION_SHAPE_CANDIDATE_WITH_HOLD

Purpose: write evidence receipts without authority/promotion.

Required fields:
- receipt_id: stable id for receipt artifact
- classification: receipt_<domain>_with_hold
- source_layer: layer that produced the receipt, usually tool_reentry_layer/evidence_layer
- status: PASS|FAIL|WATCH|STOP
- validators_run: list of validator command refs, rc, stdout/stderr, seconds; may be empty only for non-execution receipts
- forbidden_scan: active-call/forbidden-boundary scan result when applicable
- seconds: elapsed local execution time if executed
- guard_status: PASS_WITH_HOLD|WATCH|HOLD_STOP_REVIEW|STOP|HOLD_UNTIL_APPROVED_MODEL_OUTPUT
- authority_effect: NO_AUTHORITY_MUTATION
- promotion_status: HOLD

Boundary fields:
- api_call
- api_direct
- local_http_endpoint_replay
- local_server_start
- model_execution
- codex_cli_execution
- gemini_cli_execution
- registry_mutation
- current_position_apply

Forbidden:
- receipt is authority
- receipt means promotion
- omit boundary fields for execution receipt
- hide validator failure
- treat model fixture as real model execution
