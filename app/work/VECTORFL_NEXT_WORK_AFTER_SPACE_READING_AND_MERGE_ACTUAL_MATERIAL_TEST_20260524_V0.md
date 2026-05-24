# VECTORFL_NEXT_WORK_AFTER_SPACE_READING_AND_MERGE_ACTUAL_MATERIAL_TEST_20260524_V0

NEXT_SAFE_LANE: SPACE_READING_AND_MERGE_SHAPE_EXTRACTION_FROM_ACTUAL_TEST_NO_AUTHORITY_MUTATION_V0

purpose:
Use the passing actual-material test to extract stable shape candidates for space reading and merge.

Do:
1. Extract required fields from actual_space_reading_packet_v0.json.
2. Extract required fields from actual_space_mediated_merge_packet_v0.json.
3. Preserve timing/processing-method checks as validator requirements.
4. Keep negative tests: missing current-position, insufficient refs, missing original, model-only merge, authority/promotion drift.

Do not:
- call model/Codex/Gemini
- run API/local endpoint/server
- mutate authority/registry/current-position
- promote module
