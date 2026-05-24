# VECTORFL_NEXT_WORK_AFTER_PHASE2_PACKET_SHAPE_ACTUAL_TEST_20260524_V0

NEXT_SAFE_LANE: PHASE2_PACKET_SHAPE_REAL_USE_ON_SMALL_SPACE_AFFECTING_TASK_WITH_BUDGET_GATE_V0

purpose:
Use the Phase2 packet shape on one real small space-affecting task.

Required:
- choose one small internal detail target
- read actual space refs
- write space_reference_delta
- decide fast/heavy by budget gate
- if heavy trigger appears, run Codex/Gemini once each
- validate negative cases remain blocked

Do not:
- mutate authority/current-position/registry
- treat HOLD packet as schema
- cite space decoratively
