# Phase 1 API Contract Snapshot

classification: PIPELINE_PHASE1_API_CONTRACT_SNAPSHOT_V0

Captures stable JSON snapshots for the local read-only Web MVP API.

Commands:
- python3 tools/api_contract_snapshot.py
- python3 tools/api_contract_replay.py

Boundary:
- local-only
- read-only
- no authority mutation
- promotion HOLD
- no external model/tool/network execution
- no production deployment
