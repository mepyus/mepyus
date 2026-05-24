# Run Export: Run 001 LIGHT meeting summary

request_id: 1
depth: LIGHT
state: MATURED_OR_HELD
promotion_status: HOLD
authority_status: NO

## request
이번 주 회의록을 내부 팀 공유용으로 요약해줘.

## routing
LIGHT

## assets
synthetic/no-real-data assets only.

## decision
[('ROUTE_LIGHT', 'route before execution')]

## execution or boundary
[(1, 'LIGHT_LOCAL_DRAFT', 'COMPLETED', 'INTERNAL_SUMMARY_DRAFT_NOT_OFFICIAL_RECORD')]

## receipt
[('synthetic local receipt; no external tool; no real company data',)]

## review
[('LOCAL_SAMPLE_PASS_WITH_HOLD', 'review sample recovery and keep promotion HOLD', 'HOLD', 'NO')]

## maturation / HOLD
[('sample recovered into local maturation record', 'routing and recovery path verified for LIGHT', 'NO')]

## guardrail results
[('G2', 'PASS_BLOCKED', 'LIGHT missing source/audience/sensitivity'), ('G5', 'PASS', 'COMPLETED -> RECEIPT_REQUIRED'), ('G7', 'PASS', 'receipt -> REVIEW_REQUIRED'), ('G8_G9_G10_G11', 'PASS', 'review has next/HOLD, promotion HOLD, authority NO'), ('G12', 'PASS', 'no authority mutation')]

## final classification
CANDIDATE_LOCAL_PROTOTYPE_EVIDENCE_NOT_AUTHORITY
