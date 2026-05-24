# Structured Run Export: Run 001 LIGHT meeting summary

classification: STRUCTURED_LOCAL_RUN_EXPORT
request_id: 1
exported_at: 2026-05-20T10:31:50Z
external_execution: NO
real_company_data: NO
authority_mutation: NO
promotion: HOLD
program_alpha_evidence: NO

## request
| id | title | body | depth | state | source_known | audience_known | sensitivity_known | approval_marker | scope_marker | promotion_status | authority_status | created_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Run 001 LIGHT meeting summary | 이번 주 회의록을 내부 팀 공유용으로 요약해줘. | LIGHT | MATURED_OR_HELD | 1 | 1 | 1 |  |  | HOLD | NO | 2026-05-20 09:57:38 |

## assets
_none_

## decisions
| id | decision | reason | created_at |
| --- | --- | --- | --- |
| 1 | ROUTE_LIGHT | route before execution | 2026-05-20 09:57:38 |

## executions
| id | execution_type | status | output_classification | created_at | updated_at |
| --- | --- | --- | --- | --- | --- |
| 1 | LIGHT_LOCAL_DRAFT | COMPLETED | INTERNAL_SUMMARY_DRAFT_NOT_OFFICIAL_RECORD | 2026-05-20 09:57:38 | 2026-05-20 09:57:38 |

## receipts
| id | execution_id | content | created_at |
| --- | --- | --- | --- |
| 1 | 1 | synthetic local receipt; no external tool; no real company data | 2026-05-20 09:57:38 |

## reviews
| id | verdict | next_smallest_action | promotion_status | authority_status | created_at |
| --- | --- | --- | --- | --- | --- |
| 1 | LOCAL_SAMPLE_PASS_WITH_HOLD | review sample recovery and keep promotion HOLD | HOLD | NO | 2026-05-20 09:57:38 |

## maturation
| id | summary | next_work_easier_value | authority_mutation | created_at |
| --- | --- | --- | --- | --- |
| 1 | sample recovered into local maturation record | routing and recovery path verified for LIGHT | NO | 2026-05-20 09:57:38 |

## next_actions
_none_

## guardrail_events
| id | guardrail | result | detail | created_at |
| --- | --- | --- | --- | --- |
| 1 | G2 | PASS_BLOCKED | LIGHT missing source/audience/sensitivity | 2026-05-20 09:57:38 |
| 2 | G5 | PASS | COMPLETED -> RECEIPT_REQUIRED | 2026-05-20 09:57:38 |
| 3 | G7 | PASS | receipt -> REVIEW_REQUIRED | 2026-05-20 09:57:38 |
| 4 | G8_G9_G10_G11 | PASS | review has next/HOLD, promotion HOLD, authority NO | 2026-05-20 09:57:38 |
| 5 | G12 | PASS | no authority mutation | 2026-05-20 09:57:38 |

## completeness checklist
- request: PASS count=1
- assets: PASS_EMPTY_OK count=0
- decisions: PASS count=1
- executions: PASS count=1
- receipts: PASS count=1
- reviews: PASS count=1
- maturation: PASS count=1
- next_actions: PASS_EMPTY_OK count=0
- guardrail_events: PASS count=5
- boundary_hold_no: PASS

## final classification
LOCAL_STRUCTURED_EXPORT_EVIDENCE_NOT_AUTHORITY
