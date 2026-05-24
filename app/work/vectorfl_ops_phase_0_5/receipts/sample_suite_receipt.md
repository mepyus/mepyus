# Sample Suite Receipt

classification: LOCAL_PROTOTYPE_SAMPLE_SUITE_RECEIPT
real_external_execution: NO
real_company_data: NO
authority_mutation: NO
promotion: HOLD

## Run results
- request_id=1 depth=LIGHT state=MATURED_OR_HELD title=Run 001 LIGHT meeting summary
- request_id=2 depth=STANDARD state=MATURED_OR_HELD title=Run 002 STANDARD shorts script
- request_id=3 depth=DEEP state=MATURED_OR_HELD title=Run 003 DEEP repo feature
- request_id=4 depth=BLOCKED_SPECIAL state=MATURED_OR_HELD title=Run 004 BLOCKED authority request

## guardrail pass/fail table
- pass_or_block_pass_events: 19
- fail_events: 0


## verification result
VALIDATION_PASS
- required files missing: []
- python py_compile: PASS
- requests: 4
- executions: 3
- receipts: 3
- reviews: 4
- maturation_entries: 4
- guardrail_events: 19
- fail_events: 0
- authority_mutations: 0
- non_hold_reviews: 0

## dashboard output
```
DASHBOARD
requests_by_depth={"BLOCKED_SPECIAL": 1, "DEEP": 1, "LIGHT": 1, "STANDARD": 1}
requests_by_state={"MATURED_OR_HELD": 4}
executions_without_receipts=0
receipts_without_reviews=0
reviews_without_maturation=0
blocked_authority_requests=1
promotion_pressure_detected=4
guardrail_events_count=19
```

## HOLD confirmations
- promotion: HOLD
- authority mutation: NO
- Phase 1 Web MVP readiness: NO
- Program Alpha evidence: NO
- external Codex/Gemini/browser/network execution: NO
- real company data: NO
