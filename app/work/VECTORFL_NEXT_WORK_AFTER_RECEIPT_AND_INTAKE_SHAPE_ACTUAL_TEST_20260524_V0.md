# VECTORFL_NEXT_WORK_AFTER_RECEIPT_AND_INTAKE_SHAPE_ACTUAL_TEST_20260524_V0

NEXT_SAFE_LANE: SCENARIO_1_SPACE_READING_AND_MERGE_FUNCTION_SHAPE_EXTRACTION_NO_AUTHORITY_MUTATION_V0

purpose:
Now actual-test the next middle shapes: space reading packet shape and space-mediated merge packet shape.

Do:
1. Extract shapes from scenario_1_space_reading_packet_v0.json and scenario_1_space_mediated_merge_packet_v0.json.
2. Create positive/negative fixtures.
3. Test missing space refs, model-only merge, omitted original ref, authority/promotion drift.
4. Keep no-call/HOLD.

Do not:
- call model/Codex/Gemini
- run API/local endpoint/server
- mutate authority/registry/current-position
