# VECTORFL_SPACE_READING_AND_MERGE_ACTUAL_MATERIAL_TEST_20260524_V0

verdict: PASS_SPACE_READING_AND_MERGE_ACTUAL_MATERIAL_TEST_WITH_HOLD

## What this tested

실제 공간 재료를 찾아와서 space reading + space-mediated merge 처리 방식을 실제 로컬 no-call 테스트했다.

실제 재료:
- current-position entry
- guard matrix
- Gemini space-wide reread packet
- customer response merge doc
- Scenario 1 space reading packet
- Scenario 1 merge packet
- receipt/intake actual test report

## Runner

```text
PASS_SPACE_READING_AND_MERGE_ACTUAL_MATERIAL_TEST_WITH_HOLD
parts=5 total_measured_seconds=0.004230 negative_cases=5 active_call_hits=0
P1_material_discovery seconds=0.000011 method=file material index verification by sha256/path existence, no broad mutation
P2_space_reading_actual_materials seconds=0.001506 method=read actual local files -> extract current/safe/guard/lens/boundary facts -> write packet
P3_space_mediated_merge_actual_materials seconds=0.000973 method=merge actual original material + actual space reading packet + local model fixture into directive
P4_negative_processing_checks seconds=0.000331 method=programmatic negative validation of required anchors and merge inputs
P5_forbidden_active_call_scan seconds=0.001409 method=scan generated artifacts for active network/local endpoint primitives
```

## Part timings

- P1_material_discovery: 1.1e-05s
  method: file material index verification by sha256/path existence, no broad mutation
- P2_space_reading_actual_materials: 0.001506s
  method: read actual local files -> extract current/safe/guard/lens/boundary facts -> write packet
- P3_space_mediated_merge_actual_materials: 0.000973s
  method: merge actual original material + actual space reading packet + local model fixture into directive
- P4_negative_processing_checks: 0.000331s
  method: programmatic negative validation of required anchors and merge inputs
- P5_forbidden_active_call_scan: 0.001409s
  method: scan generated artifacts for active network/local endpoint primitives


total_measured_seconds: 0.00423

## Processing method review

space_reading_method:
actual file refs -> extract anchors/lens/guard/boundary -> packet

merge_method:
original material + space reading + model fixture -> merged directive

validation_method:
positive structural checks + negative required-anchor/merge-input checks + forbidden primitive scan

## Negative checks

negative_cases: 5
negative_passed_cases: 5
active_call_hits: 0

Covered failures:
- missing current-position
- insufficient space refs
- missing original ref
- model-only merge
- authority/promotion drift
- active network/local endpoint primitive scan

## Repair note

First run exposed two validator-order issues and a self-scan issue: SPACE-NEG-002 was classified as missing current-position because empty dict was treated as absent; MERGE-NEG-002 was classified as missing original before model-only; scan included runner script literals. Patched validator ordering/presence semantics and scanned generated data artifacts excluding control script. Re-run PASS.

## HOLD

api_call: NO
local_http_endpoint_replay: NO
local_server_start: NO
model_execution: NO_FIXTURE_ONLY
authority_mutation: NO
registry_mutation: NO
promotion: HOLD

## Next Safe Lane

SPACE_READING_AND_MERGE_SHAPE_EXTRACTION_FROM_ACTUAL_TEST_NO_AUTHORITY_MUTATION_V0
