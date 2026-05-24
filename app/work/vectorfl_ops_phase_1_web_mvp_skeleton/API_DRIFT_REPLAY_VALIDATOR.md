# Phase 1 API Drift Replay Validator

classification: PIPELINE_PHASE1_API_DRIFT_REPLAY_VALIDATOR_V0

Formal gate that compares live local API behavior against the captured Phase 1 API contract snapshot.

Command:
python3 tools/api_drift_replay_gate.py

Default checks:
- endpoint status/content type
- JSON schema shape
- selected stable counts
- boundary tokens
- request id set

Hash behavior:
- response hash changes are WATCH by default
- set VECTORFL_PHASE1_STRICT_HASH=1 to make response hash changes FAIL

Boundary:
- local-only
- read-only
- no authority mutation
- promotion HOLD
- no external model/tool/network execution
- no production deployment
