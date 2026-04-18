# Integrated Engine Internal / External Test Pool Matrix v0

## Status

PASS_WITH_NOTE

This matrix defines a narrow test pool for reusable reading-frame review.
It uses only assets already surfaced in the current work.
It does not open a new probe.

## Pool Classes

1. external content-bearing
2. internal content-bearing
3. invalid / rollback-only shapes

## External Content-Bearing

| asset | asset type | why content-bearing | testable camera slots | likely useful lenses | promotion evidence? | probe-valid? |
|---|---|---|---|---|---|---|
| `inputs/external_cases/choi_ai_classroom_transformer1.txt` | lecture transcript | Has long body explaining transformer encoder, self-attention, positional encoding. | C0-C6 | scope-reading, processing-tension, preparation-structure, selection-mechanism, output-result, support-placement | yes, already used | yes |
| `inputs/external_cases/choi_ai_classroom_transformer2.txt` | lecture transcript | Has long body explaining decoder, autoregressive generation, causal mask, cross-attention, generation strategies. | C0-C6 | scope-reading, processing-tension, preparation-structure, selection-mechanism, output-result, support-placement | yes, already used | yes |

## Internal Content-Bearing

| asset | asset type | why content-bearing | testable camera slots | likely useful lenses | promotion evidence? | probe-valid? |
|---|---|---|---|---|---|---|
| `docs/reports/integrated_engine_body_camera_lens_reread_correction_v0.md` | correction report | Has verdict, corrected meaning, body/camera/lens, misread correction, projection rules, must-not, clarification. | C0-C6 | correction-reading, screen-projection, scope-reading, processing-tension, support-placement, rollback-detection | yes, already used as cross-shape evidence | yes |
| `docs/reports/integrated_engine_real_handoff_grammar_classification_v0.md` | grammar classification report | Has route, authority, hold/watch, validation, reread/support, bridge-before-flatten grammar and targeted checks. | C0-C6 likely testable | grammar-classification, rollback-detection, correction-reading, support-placement | not yet counted | yes |
| `docs/reports/gemini_mock_test_structural_analysis_v0.md` | structural analysis report | Has verdict, summary, screen/panel mapping, conflict list, salvageable/hold elements, reflection order. | C0-C5 likely, C6 via conflict/hold sections | screen-projection, correction-reading, support-placement, rollback-detection | not yet counted | yes |

## Invalid / Rollback-Only Shapes

| asset or shape | asset type | why not content-bearing for F1-C6 probe | usable role | promotion evidence? | probe-valid? |
|---|---|---|---|---|---|
| `source_assets/external_case_inputs/choi_ai_classroom_transformer1_input_v1.md` | intake note | Gives object tag, source pointer, topic hint, series position; does not provide enough content flow. | support object, scope/source pointer, topic hint | no | no |
| `source_assets/external_case_inputs/choi_ai_classroom_transformer2_input_v1.md` | intake note | Same shape: source pointer and topic summary only; F1-C6 cannot be tested without forcing. | support object, asset-specific metadata | no | no |
| metadata-only records | metadata | Object id/semantic id/link only. | source identity only | no | no |
| pointer-only manifests | pointer/reference | Route/object reference may exist, but content-level frame cannot be tested. | support/evidence pointer | no | no |
| index-only documents | index | Lists documents but does not provide processing flow. | navigation support | no | no |

## Inclusion Rule

Count a probe toward promotion evidence only if:

- it is content-bearing
- C1-C6 can be meaningfully tested, with at least four slots match/partial/missing by evidence
- C0 scope anchor split can be checked
- support placement can be checked
- mismatch can be named without frame forcing

Do not count:

- intake-note-only probes
- metadata-only probes
- pointer-only probes
- index-only probes
- support-object-only checks

## Next Valid Test Options

If review asks for one more probe, choose one:

1. `docs/reports/integrated_engine_real_handoff_grammar_classification_v0.md`
   - reason: tests grammar-classification and authority/route state.
2. `docs/reports/gemini_mock_test_structural_analysis_v0.md`
   - reason: tests screen-projection and design-analysis shape.

Do not use intake notes as full probe targets.

## Current Recommendation

Current status does not require another probe before camera-candidate review.
If confidence is needed, use one internal content-bearing report, not another intake note.

## Pointers

- Target-shape rule source: `docs/reports/integrated_engine_reusable_reading_frame_probe_result_template_v0.md`
- Camera big frame: `docs/reports/integrated_engine_provisional_camera_big_frame_v0.md`
- Lens draft: `docs/reports/integrated_engine_lens_structure_draft_v0.md`
