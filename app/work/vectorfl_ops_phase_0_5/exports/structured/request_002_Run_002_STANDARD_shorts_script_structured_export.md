# Structured Run Export: Run 002 STANDARD shorts script

classification: STRUCTURED_LOCAL_RUN_EXPORT
request_id: 2
exported_at: 2026-05-20T10:31:50Z
external_execution: NO
real_company_data: NO
authority_mutation: NO
promotion: HOLD
program_alpha_evidence: NO

## request
| id | title | body | depth | state | source_known | audience_known | sensitivity_known | approval_marker | scope_marker | promotion_status | authority_status | created_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | Run 002 STANDARD shorts script | VectorFL을 소개하는 30초 쇼츠 대본 초안을 만들어줘. | STANDARD | MATURED_OR_HELD | 0 | 0 | 0 |  |  | HOLD | NO | 2026-05-20 09:57:38 |

## assets
_none_

## decisions
| id | decision | reason | created_at |
| --- | --- | --- | --- |
| 2 | ROUTE_STANDARD | route before execution | 2026-05-20 09:57:38 |

## executions
| id | execution_type | status | output_classification | created_at | updated_at |
| --- | --- | --- | --- | --- | --- |
| 2 | STANDARD_CONTENT_DRAFT | COMPLETED | CONTENT_DRAFT_CANDIDATE_NOT_PUBLISH_READY | 2026-05-20 09:57:38 | 2026-05-20 09:57:38 |

## receipts
| id | execution_id | content | created_at |
| --- | --- | --- | --- |
| 2 | 2 | synthetic local receipt; no external tool; no real company data | 2026-05-20 09:57:38 |

## reviews
| id | verdict | next_smallest_action | promotion_status | authority_status | created_at |
| --- | --- | --- | --- | --- | --- |
| 2 | LOCAL_SAMPLE_PASS_WITH_HOLD | review sample recovery and keep promotion HOLD | HOLD | NO | 2026-05-20 09:57:38 |

## maturation
| id | summary | next_work_easier_value | authority_mutation | created_at |
| --- | --- | --- | --- | --- |
| 2 | sample recovered into local maturation record | routing and recovery path verified for STANDARD | NO | 2026-05-20 09:57:38 |

## next_actions
_none_

## guardrail_events
| id | guardrail | result | detail | created_at |
| --- | --- | --- | --- | --- |
| 6 | G3 | PASS | STANDARD output remains candidate, not approved asset | 2026-05-20 09:57:38 |
| 7 | G5 | PASS | COMPLETED -> RECEIPT_REQUIRED | 2026-05-20 09:57:38 |
| 8 | G7 | PASS | receipt -> REVIEW_REQUIRED | 2026-05-20 09:57:38 |
| 9 | G8_G9_G10_G11 | PASS | review has next/HOLD, promotion HOLD, authority NO | 2026-05-20 09:57:38 |
| 10 | G12 | PASS | no authority mutation | 2026-05-20 09:57:38 |

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
