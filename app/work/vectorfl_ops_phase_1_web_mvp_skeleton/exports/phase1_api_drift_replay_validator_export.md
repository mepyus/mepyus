# Phase 1 API Drift Replay Validator Export

classification: PIPELINE_PHASE1_API_DRIFT_REPLAY_VALIDATOR_V0
verdict: PASS_API_DRIFT_REPLAY_MATCH
created_at: 2026-05-22T22:29:28Z

## Snapshot manifest
/Users/sungsookim/universe/vectorfl_replica/app/work/vectorfl_ops_phase_1_web_mvp_skeleton/snapshots/phase1_api_contract_snapshot_v0/manifest.json

## Replay mode
strict_hash: False

## Checked
endpoints: 13

## Problems
```json
[]
```

## Watches
```json
[
  "/health response hash changed or runtime ordering differs",
  "/api/summary response hash changed or runtime ordering differs",
  "/api/requests response hash changed or runtime ordering differs",
  "/api/guardrails response hash changed or runtime ordering differs",
  "/ response hash changed or runtime ordering differs",
  "/api/request/1 response hash changed or runtime ordering differs",
  "/api/request/2 response hash changed or runtime ordering differs",
  "/api/request/3 response hash changed or runtime ordering differs",
  "/api/request/4 response hash changed or runtime ordering differs",
  "/api/request/5 response hash changed or runtime ordering differs",
  "/api/request/6 response hash changed or runtime ordering differs",
  "/api/request/7 response hash changed or runtime ordering differs"
]
```

## Boundary
promotion: HOLD
authority mutation: NO
Program Alpha evidence: NO
external model/tool/network execution: NO
real company data: NO
production deployment: NO
write UI: NO

## Next lane
PIPELINE_PHASE1_UI_SURFACE_COMPLETENESS_V0
