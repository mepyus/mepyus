# Guardrail Probe Receipt

classification: LOCAL_NEGATIVE_GUARDRAIL_PROBE_RECEIPT
probe_time: 2026-05-22T21:20:45Z
external_execution: NO
real_company_data: NO
authority_mutation: NO
promotion: HOLD
program_alpha_evidence: NO

## Probe results
```json
[
  {
    "guardrail": "G1",
    "request_id": 8,
    "result": "PASS_BLOCKED",
    "state_after": "RECEIVED"
  },
  {
    "guardrail": "G6",
    "request_id": 9,
    "result": "PASS_BLOCKED",
    "state_after": "RECEIPT_REQUIRED"
  },
  {
    "guardrail": "G8",
    "request_id": 10,
    "result": "PASS_BLOCKED",
    "state_after": "REVIEW_REQUIRED"
  }
]
```

## Summary
- G1 direct RECEIVED -> IN_EXECUTION attempt: PASS_BLOCKED
- G6 close from RECEIPT_REQUIRED without receipt: PASS_BLOCKED
- G8 close from REVIEW_REQUIRED without review: PASS_BLOCKED
- fail_count: 0
- guardrail_events_total_after_probe: 25
- authority_mutations: 0
- non_hold_reviews: 0

## Boundary
This strengthens Phase 0.5 local prototype evidence only. It is not Phase 1 readiness, not authority, not promotion, and not Program Alpha evidence.
