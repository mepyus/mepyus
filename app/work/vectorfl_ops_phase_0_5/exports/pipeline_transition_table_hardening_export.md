# Pipeline Transition Table Hardening Export

classification: PIPELINE_TRANSITION_TABLE_HARDENING_V0
verdict: PASS_WITH_INTENTIONAL_RESIDUE
validated_at: 2026-05-22T21:20:20Z
external_execution: NO
real_company_data: NO
authority_mutation: NO
promotion: HOLD
program_alpha_evidence: NO

## Allowed vocabularies
- request_states: HOLD, IN_EXECUTION, MATURATION_READY, MATURED_OR_HELD, RECEIPT_REQUIRED, RECEIVED, REVIEW_REQUIRED, ROUTED, STOPPED
- depths: BLOCKED_SPECIAL, DEEP, LIGHT, STANDARD, UNROUTED
- execution_statuses: CANCELLED, COMPLETED, CREATED, FAILED
- guardrail_results: FAIL, PASS, PASS_BLOCKED, WATCH_INTENTIONAL

## Validation issues
```json
[
  {
    "level": "WATCH_INTENTIONAL",
    "code": "INTENTIONAL_PROBE_RESIDUE",
    "request_id": 5,
    "detail": "RECEIVED explained by G1"
  },
  {
    "level": "WATCH_INTENTIONAL",
    "code": "INTENTIONAL_PROBE_RESIDUE",
    "request_id": 6,
    "detail": "RECEIPT_REQUIRED explained by G6"
  },
  {
    "level": "WATCH_INTENTIONAL",
    "code": "INTENTIONAL_PROBE_RESIDUE",
    "request_id": 7,
    "detail": "REVIEW_REQUIRED explained by G8"
  },
  {
    "level": "WATCH_INTENTIONAL",
    "code": "RECEIPT_WITHOUT_REVIEW_G8_RESIDUE",
    "request_id": 7,
    "detail": "receipts=1"
  },
  {
    "level": "SUMMARY",
    "code": "TRANSITION_TABLE_SUMMARY",
    "detail": {
      "fail_count": 0,
      "watch_intentional_count": 4
    }
  }
]
```

## Interpretation
Open RECEIVED / RECEIPT_REQUIRED / REVIEW_REQUIRED states are acceptable only when explained as G1/G6/G8 intentional probe residues. All promotion and authority fields must remain HOLD/NO.

## Boundary
This is local state-transition hardening evidence only; not authority, not promotion, not Phase 1 implementation.
