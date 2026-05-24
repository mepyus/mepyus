# User Surface Card — HOLD Review State Candidate

status: USER_SURFACE_CARD_WITH_HOLD
created_at: 2026-05-23 08:12:54 KST

## Plain Korean Summary

HOLD Review State는 후보/receipt가 승격처럼 읽히는 순간을 막는 후보 기능으로 리허설 통과했다.

즉, “증거가 있다”와 “승인됐다”를 분리하는 안전장치다.

## What Passed Locally

- candidate-only review -> CANDIDATE_MATERIAL_WITH_HOLD
- fake promotion approval -> STOP
- soft approval language -> HOLD_STOP_REVIEW

## Boundary

promotion_status: HOLD
program_alpha_status: NOT_READY
vectorfl_authority_mutation: no
model_execution: no
real_gemini_execution: no
real_codex_execution: no
approval_applied: no
live_db_mutation: no
schema_mutation: no
snapshot_mutation: no
router_runner_claim: no

