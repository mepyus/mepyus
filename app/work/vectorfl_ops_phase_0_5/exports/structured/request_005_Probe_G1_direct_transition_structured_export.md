# Structured Run Export: Probe G1 direct transition

classification: STRUCTURED_LOCAL_RUN_EXPORT
request_id: 5
exported_at: 2026-05-20T10:31:50Z
external_execution: NO
real_company_data: NO
authority_mutation: NO
promotion: HOLD
program_alpha_evidence: NO

## request
| id | title | body | depth | state | source_known | audience_known | sensitivity_known | approval_marker | scope_marker | promotion_status | authority_status | created_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | Probe G1 direct transition | Try to execute before routing | STANDARD | RECEIVED | 0 | 0 | 0 |  |  | HOLD | NO | 2026-05-20 10:10:18 |

## assets
_none_

## decisions
_none_

## executions
_none_

## receipts
_none_

## reviews
_none_

## maturation
_none_

## next_actions
_none_

## guardrail_events
| id | guardrail | result | detail | created_at |
| --- | --- | --- | --- | --- |
| 20 | G1 | PASS_BLOCKED | probe: RECEIVED -> IN_EXECUTION direct transition blocked | 2026-05-20 10:10:18 |

## completeness checklist
- request: PASS count=1
- assets: PASS_EMPTY_OK count=0
- decisions: WATCH_EMPTY count=0
- executions: WATCH_EMPTY count=0
- receipts: WATCH_EMPTY count=0
- reviews: WATCH_EMPTY count=0
- maturation: WATCH_EMPTY count=0
- next_actions: PASS_EMPTY_OK count=0
- guardrail_events: PASS count=1
- boundary_hold_no: PASS

## final classification
LOCAL_STRUCTURED_EXPORT_EVIDENCE_NOT_AUTHORITY
