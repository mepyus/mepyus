# Pipeline Baseline Replay Validator Export

classification: PIPELINE_BASELINE_REPLAY_VALIDATOR_V0
verdict: FAIL_REPLAY_MISMATCH
validated_at: 2026-05-22T21:45:06Z
external_execution: NO
real_company_data: NO
authority_mutation: NO
promotion: HOLD
program_alpha_evidence: NO
phase1_implementation: NO

## Replay counts
- checked_files: 45
- matched_files: 39
- problem_count: 6
- watch_count: 1

## Result
```json
{
  "classification": "PIPELINE_BASELINE_REPLAY_VALIDATOR_V0",
  "verdict": "FAIL_REPLAY_MISMATCH",
  "validated_at": "2026-05-22T21:45:06Z",
  "mode": "frozen",
  "checked_files": 45,
  "matched_files": 39,
  "problem_count": 6,
  "watch_count": 1,
  "problems": [
    {
      "code": "CHECKSUM_MISMATCH",
      "relative_path": "data/vectorfl_ops_phase_0_5.sqlite",
      "expected": "5515df980a5eb1cf6234f89f17d9f687d0ef4e1f1dbfa798b9e47499dcd2e0c3",
      "actual": "2d658aeb52384b9b87a608e226187bf30fb1fee0ab17f8420caa91525f531063"
    },
    {
      "code": "CHECKSUM_MISMATCH",
      "relative_path": "exports/guardrail_probe_negative_results.md",
      "expected": "5b72504f92d477711c92c03d310cdf29b4b5459417a93d141c46b12f2ff0b08b",
      "actual": "e67250b3fb62b4f16af8cea26af34581e688c7bdc28120780b5aaff776543c4e"
    },
    {
      "code": "CHECKSUM_MISMATCH",
      "relative_path": "exports/pipeline_transition_table_hardening_export.md",
      "expected": "f8de949da07edaa5da52446742148e05f709cdadb1cf7e1255e72e849f17199d",
      "actual": "8be8bbc171b721dba283585fe5151ed4de68de5d72f95fb88eff0791770e01c3"
    },
    {
      "code": "CHECKSUM_MISMATCH",
      "relative_path": "probes/guardrail_probe_runner.py",
      "expected": "657cd5be0526a255a2f12fe6ce4b0ce494adca801b049617d018d6f9ba4eca6b",
      "actual": "f9446713a40e224f7ac819fb98e6d26ed5801daa41e386cd48687ee7f15e74e8"
    },
    {
      "code": "CHECKSUM_MISMATCH",
      "relative_path": "receipts/guardrail_probe_receipt.md",
      "expected": "ef60fe34a205bd75624fd490d219a200652812d253c1d798bbaa4daed742316a",
      "actual": "02ac97e7e1964c239188a42ad2b18ba3f07be34be9d6acb95a7b9ccf00b1748d"
    },
    {
      "code": "CHECKSUM_MISMATCH",
      "relative_path": "receipts/pipeline_transition_table_hardening_receipt.md",
      "expected": "8d40517092ec13aaad57e8ff2c71587c9c2346d8ebc4d422f3be7cc555a309dd",
      "actual": "0c363c5a8bc18c8151ab0ae5abfbf0024043ef644f3c107e297562cb968da40a"
    }
  ],
  "watches": [
    {
      "code": "DB_FACT_DRIFT_AFTER_SNAPSHOT",
      "detail": {
        "guardrail_events": {
          "baseline": 22,
          "current": 25
        },
        "probe_requests": {
          "baseline": 3,
          "current": 6
        },
        "receipts": {
          "baseline": 4,
          "current": 5
        },
        "requests": {
          "baseline": 7,
          "current": 10
        }
      }
    }
  ],
  "current_db_facts": {
    "requests": 10,
    "executions": 3,
    "receipts": 5,
    "reviews": 4,
    "maturation_entries": 4,
    "guardrail_events": 25,
    "fail_events": 0,
    "authority_mutations": 0,
    "non_hold_reviews": 0,
    "probe_requests": 6
  },
  "baseline_db_facts": {
    "requests": 7,
    "executions": 3,
    "receipts": 4,
    "reviews": 4,
    "maturation_entries": 4,
    "guardrail_events": 22,
    "fail_events": 0,
    "authority_mutations": 0,
    "non_hold_reviews": 0,
    "probe_requests": 3
  },
  "manifest": "/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_ops_phase_0_5/snapshots/phase0_5_candidate_baseline_v0/baseline_manifest.json",
  "checksums": "/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_ops_phase_0_5/snapshots/phase0_5_candidate_baseline_v0/baseline_checksums.tsv",
  "hold": {
    "promotion": "HOLD",
    "authority_mutation": "NO",
    "phase1_implementation": "NO",
    "external_execution": "NO"
  }
}
```

## Interpretation
Frozen replay checks exact snapshot byte identity. File checksum mismatches are FAIL. DB count drift after snapshot is WATCH unless safety invariants fail. Promotion remains HOLD and authority remains NO.

## Boundary
This frozen replay validator confirms candidate baseline snapshot integrity only. It is not live-safety PASS, not authority, not promotion, not Program Alpha evidence, and not Phase 1 implementation.
