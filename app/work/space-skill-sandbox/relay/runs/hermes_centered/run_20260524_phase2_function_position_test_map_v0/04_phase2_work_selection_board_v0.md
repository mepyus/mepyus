# PHASE2_WORK_SELECTION_BOARD_V0

classification: PHASE2_WORK_SELECTION_BOARD_HOLD

## 1. Test S1 intake/original preservation on a small real instruction
- phase: Phase2 now
- attached: S1_INTAKE
- why_now: Every later function depends on correct original preservation and task classification.
- expected_delta: Distinguish light tasks vs space-affecting tasks before merge.
- codex/gemini: FAST unless classification ambiguous
- operator_load: LOW

## 2. Test S2 source-selection on one real non-validator target
- phase: Phase2 now
- attached: S2_SPACE_SELECTION
- why_now: Space reference is core; must avoid model-only and avoid archaeology.
- expected_delta: Show which refs changed judgment and which refs were rejected.
- codex/gemini: FAST, HEAVY if refs conflict
- operator_load: MEDIUM

## 3. Test S3 Hermes merge trace on a small real output
- phase: Phase2 now
- attached: S3_HERMES_MERGE_EXECUTION
- why_now: Phase2 must verify function placement in actual Hermes execution, not only validators.
- expected_delta: Prove space refs altered merge/execution result.
- codex/gemini: HEAVY if merge interpretation is layered or contested
- operator_load: MEDIUM

## 4. Test S4/S5 Codex-Gemini role handoff on one bounded result
- phase: Phase2 now after S1-S3 small tests
- attached: S4_CODEX_EVALUATION / S5_GEMINI_LAYER_JUDGMENT
- why_now: User specifically wants Codex evaluating Hermes result and Gemini evaluating structure/layers.
- expected_delta: Identify where Codex/Gemini add non-duplicate value.
- codex/gemini: HEAVY_BUDGETED
- operator_load: HIGH

## 5. Checklist/validator negative hardening
- phase: Phase3 backlog
- attached: S6_OPERATOR_RECEIPT_REENTRY
- why_now: Useful but too inward now.
- expected_delta: N/A until enough Phase2 observations accumulate.
- codex/gemini: FAST later
- operator_load: MEDIUM

NEXT_RECOMMENDED: S1_INTAKE_ORIGINAL_PRESERVATION_FUNCTION_TEST_SPACE_REFERENCED_NO_AUTHORITY_MUTATION_V0

HOLD only.
