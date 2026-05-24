# VECTORFL_NEXT_WORK_AFTER_FOUR_SHAPE_MINIMAL_LOOP_REHEARSAL_20260524_V0

NEXT_SAFE_LANE: FOUR_SHAPE_LOOP_REPEATABILITY_AND_DRIFT_TEST_NO_AUTHORITY_MUTATION_V0

purpose:
Run the four-shape loop repeatedly with varied inputs and intentional drift cases to confirm stability.

Do:
1. Run at least 3 positive loop inputs.
2. Run negative drift cases: raw mutation, missing current-position, model-only merge, hidden receipt failure, active-call literal in generated data.
3. Compare part timings and output field stability.
4. Keep no-call/HOLD.

Do not:
- call model/Codex/Gemini
- run API/local endpoint/server
- mutate authority/registry/current-position
- promote module
