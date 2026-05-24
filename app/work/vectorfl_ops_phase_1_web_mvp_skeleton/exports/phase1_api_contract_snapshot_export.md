# Phase 1 API Contract Snapshot Export

classification: PIPELINE_PHASE1_API_CONTRACT_SNAPSHOT_V0
verdict: PASS_API_CONTRACT_SNAPSHOT_CAPTURED
created_at: 2026-05-20T11:23:32Z

## Captured
base_url: http://127.0.0.1:8878
endpoints: 13

## Endpoint list
- /health
- /api/summary
- /api/requests
- /api/guardrails
- /api/ui-surface
- /
- /api/request/1
- /api/request/2
- /api/request/3
- /api/request/4
- /api/request/5
- /api/request/6
- /api/request/7

## Counts
```json
{
  "requests": 7,
  "executions": 3,
  "receipts": 4,
  "reviews": 4,
  "maturation_entries": 4,
  "guardrail_events": 22,
  "fail_events": 0,
  "authority_mutations": 0,
  "non_hold_reviews": 0,
  "probe_requests": 3,
  "receipts_without_reviews": 1
}
```

## Boundary
promotion: HOLD
authority mutation: NO
Program Alpha evidence: NO
external model/tool/network execution: NO
real company data: NO
production deployment: NO

## Problems
[]

## Next lane
PIPELINE_PHASE1_API_DRIFT_REPLAY_VALIDATOR_V0
