# Phase 1 Read-only Contract

classification: PIPELINE_PHASE1_READONLY_CONTRACT_HARDENING_V0

The Phase 1 local Web MVP skeleton is a read-only evidence viewer.

Allowed:
- GET /health
- GET /api/summary
- GET /api/requests
- GET /api/guardrails
- GET /api/request/<id>
- GET /
- GET /request/<id>

Expected blocked/unsupported:
- POST
- PUT
- PATCH
- DELETE

Boundary:
- no write UI
- no Phase 0.5 DB mutation
- no authority mutation
- promotion HOLD
- no Program Alpha claim
- no production deployment
