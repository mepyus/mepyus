# VectorFL Ops Phase 1 Local Web MVP Skeleton

classification: PIPELINE_PHASE1_LOCAL_WEB_MVP_SKELETON_V0

Approved scope:
- local-only Web/API skeleton
- reads Phase 0.5 local SQLite evidence
- dashboard/API for requests, guardrails, receipts, reviews, maturation

Boundary:
- no authority mutation
- promotion HOLD
- no Program Alpha claim
- no external model/tool/network execution
- no real company data
- rollback by deleting this workdir

Run:
python3 app.py

Test:
python3 tests/test_phase1_server.py
python3 tools/smoke_check.py http://127.0.0.1:8765

Deterministic stable cycle:
python3 tools/phase1_deterministic_stable_cycle.py
