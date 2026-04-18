# Integrated Engine Verification Pool Refinement v0

## Status

PASS_WITH_NOTE

This document refines the review-stage verification pool.
It does not open a new probe.

## External Content-Bearing

| asset | asset shape | content-bearing? | testable slots | useful lenses | support placement testability | promotion evidence eligibility | recommended use |
|---|---|---|---|---|---|---|---|
| `inputs/external_cases/choi_ai_classroom_transformer1.txt` | lecture transcript | yes | C0-C6 | scope-reading, processing-tension, preparation-structure, selection-mechanism, output-result, support-placement | yes | counted | full probe already used |
| `inputs/external_cases/choi_ai_classroom_transformer2.txt` | lecture transcript | yes | C0-C6 | scope-reading, processing-tension, preparation-structure, selection-mechanism, output-result, support-placement | yes | counted | full probe already used |

## Internal Content-Bearing

| asset | asset shape | content-bearing? | testable slots | useful lenses | support placement testability | promotion evidence eligibility | recommended use |
|---|---|---|---|---|---|---|---|
| `docs/reports/integrated_engine_body_camera_lens_reread_correction_v0.md` | correction report | yes | C0-C6 | correction-reading, screen-projection, scope-reading, processing-tension, support-placement, rollback-detection | yes | counted | full cross-shape probe already used |
| `docs/reports/integrated_engine_real_handoff_grammar_classification_v0.md` | grammar classification report | yes | C0-C6 likely | grammar-classification, rollback-detection, correction-reading, support-placement | yes | eligible if probed | next stress-test candidate |
| `docs/reports/gemini_mock_test_structural_analysis_v0.md` | structural analysis report | yes | C0-C5 likely; C6 via conflicts/hold | screen-projection, correction-reading, support-placement, rollback-detection | yes | eligible if probed | next stress-test candidate |

## Rollback-Only Shapes

| asset/shape | asset shape | content-bearing? | testable slots | useful lenses | support placement testability | promotion evidence eligibility | recommended use |
|---|---|---|---|---|---|---|---|
| `source_assets/external_case_inputs/choi_ai_classroom_transformer2_input_v1.md` | intake note | no for C1-C6 | C0 only, C4 topic hint partial | scope-reading only | no | excluded | rollback-only / support object |
| intake-note-only | source pointer / topic hint | no | C0 only | scope-reading | no | excluded | support object only |
| metadata-only | id/tag/path | no | C0 metadata only | scope-reading limited | no | excluded | asset-specific metadata |
| pointer-only | link/reference | no | none without linked target | scope-reading limited | no | excluded | evidence pointer |
| index-only | list/navigation | no | none for camera probe | scope-reading limited | no | excluded | navigation support |

## Stress-Test Shortlist

1. `docs/reports/integrated_engine_real_handoff_grammar_classification_v0.md`
   - useful because it tests route/authority/state/boundary grammar instead of transformer or screen correction content.
   - risk it may reveal: `grammar-classification` may overtake C0-C6 or drift toward glossary.

2. `docs/reports/gemini_mock_test_structural_analysis_v0.md`
   - useful because it tests design-analysis and screen-projection shape.
   - risk it may reveal: support/conflict/salvage material may inflate and become the center.

## Required Verification

- rollback-only asset accidentally probe-valid? no
- internal assets classified by body, not title only? yes
- promotion evidence eligibility aligned with target-shape gate? yes

## Pointers

- Usage boundary: `docs/reports/integrated_engine_provisional_camera_candidate_usage_boundary_v0.md`
- Lens-slot matrix: `docs/reports/integrated_engine_lens_slot_compatibility_matrix_v0.md`
