# Run Export: Run 002 STANDARD shorts script

request_id: 2
depth: STANDARD
state: MATURED_OR_HELD
promotion_status: HOLD
authority_status: NO

## request
VectorFL을 소개하는 30초 쇼츠 대본 초안을 만들어줘.

## routing
STANDARD

## assets
synthetic/no-real-data assets only.

## decision
[('ROUTE_STANDARD', 'route before execution')]

## execution or boundary
[(2, 'STANDARD_CONTENT_DRAFT', 'COMPLETED', 'CONTENT_DRAFT_CANDIDATE_NOT_PUBLISH_READY')]

## receipt
[('synthetic local receipt; no external tool; no real company data',)]

## review
[('LOCAL_SAMPLE_PASS_WITH_HOLD', 'review sample recovery and keep promotion HOLD', 'HOLD', 'NO')]

## maturation / HOLD
[('sample recovered into local maturation record', 'routing and recovery path verified for STANDARD', 'NO')]

## guardrail results
[('G3', 'PASS', 'STANDARD output remains candidate, not approved asset'), ('G5', 'PASS', 'COMPLETED -> RECEIPT_REQUIRED'), ('G7', 'PASS', 'receipt -> REVIEW_REQUIRED'), ('G8_G9_G10_G11', 'PASS', 'review has next/HOLD, promotion HOLD, authority NO'), ('G12', 'PASS', 'no authority mutation')]

## final classification
CANDIDATE_LOCAL_PROTOTYPE_EVIDENCE_NOT_AUTHORITY
