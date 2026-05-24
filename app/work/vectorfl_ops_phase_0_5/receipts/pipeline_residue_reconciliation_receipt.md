# Pipeline Residue Reconciliation Receipt

classification: PIPELINE_RESIDUE_RECONCILIATION_V0
verdict: PASS_INTENTIONAL_RESIDUE_CLASSIFIED
external_execution: NO
real_company_data: NO
authority_mutation: NO
promotion: HOLD
program_alpha_evidence: NO

## Purpose
Classify the residue left by G1/G6/G8 negative probes so dashboard readers do not mistake intentional blocked states for broken production states.

## Residue records
```json
[
  {
    "request_id": 5,
    "title": "Probe G1 direct transition",
    "depth": "STANDARD",
    "state": "RECEIVED",
    "guardrail": "G1",
    "result": "PASS_BLOCKED",
    "detail": "probe: RECEIVED -> IN_EXECUTION direct transition blocked",
    "residue_class": "INTENTIONAL_NEGATIVE_PROBE_RESIDUE"
  },
  {
    "request_id": 6,
    "title": "Probe G6 close without receipt",
    "depth": "STANDARD",
    "state": "RECEIPT_REQUIRED",
    "guardrail": "G6",
    "result": "PASS_BLOCKED",
    "detail": "probe: RECEIPT_REQUIRED cannot close without receipt",
    "residue_class": "INTENTIONAL_NEGATIVE_PROBE_RESIDUE"
  },
  {
    "request_id": 7,
    "title": "Probe G8 close without review",
    "depth": "STANDARD",
    "state": "REVIEW_REQUIRED",
    "guardrail": "G8",
    "result": "PASS_BLOCKED",
    "detail": "probe: REVIEW_REQUIRED cannot close without review",
    "residue_class": "INTENTIONAL_NEGATIVE_PROBE_RESIDUE"
  }
]
```

## Counts
```json
{
  "probe_requests": 3,
  "probe_guardrail_events": 3,
  "fail_events": 0,
  "receipts_without_reviews": 1,
  "authority_mutations": 0,
  "non_hold_reviews": 0
}
```

## Interpretation
- Probe RECEIVED state is intentional G1 residue.
- Probe RECEIPT_REQUIRED state is intentional G6 residue.
- Probe REVIEW_REQUIRED plus receipts_without_reviews=1 is intentional G8 residue.
- These residues remain visible because guardrail tests should leave recoverable evidence, not erase the pressure they revealed.

## Boundary
This is local evidence reconciliation only. It is not Phase 1 readiness, not authority, not promotion, and not Program Alpha evidence.
