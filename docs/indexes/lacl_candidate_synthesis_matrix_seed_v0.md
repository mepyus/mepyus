# LACL Candidate Synthesis Matrix Seed v0

## Status

```yaml
status: synthesis_matrix_seed_candidate
date: 2026-05-06
baseline_lock: false
automation: false
scope: lacl_regrounding
```

## Purpose

Prepare the matrix that will receive Gemini's LACL re-grounding result.

This is intentionally empty-ish until Gemini returns evidence.

## Matrix Fields

```text
item_type:
name:
evidence_pointers:
decision_effect:
maturity_state:
position_value_link:
watch:
do_not_infer:
codex_action:
```

## Item Types

- line
- axis
- camera
- lens_gate
- position_value
- conflict_overlap
- missing_data

## Current Seed Entries

| item_type | name | evidence_pointers | decision_effect | maturity_state | position_value_link | watch | do_not_infer | codex_action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| line | Plan from Space / Session Convergence Prevention | `docs/indexes/plan_from_space_line_asset_map_v0.md` | plan must start with space basis | operating_anchor_candidate | `PV_PLAN_BASIS_GATE` | global baseline drift | no line registry baseline | keep_existing |
| axis | small split vs broad-but-bounded package | `docs/indexes/plan_from_space_position_map_seed_v0.md` | changes package sizing | reusable_setting_candidate | `PV_BROAD_BOUNDED_PACKAGE` | session convergence | no scope expansion | keep_existing |
| camera | user relay burden | `docs/specs/manual_external_tool_relay_bridge_note_v0.md` | prevents user-as-dispatcher completion | watch_only | `PV_MANUAL_RELAY_BRIDGE` | normalized relay | no permanent relay workflow | keep_existing |
| lens_gate | non-inspected evidence disclosure | `docs/reports/position_value_discovery_gemini_return_packaging_v0.md` | blocks overclaim from bounded reads | process_asset_candidate | `PV_NON_INSPECTED_DISCLOSURE` | evidence overclaim | no full-space read claim | keep_existing |
| lens_gate | Return-to-Space Value present | `app/work/SESSION_47_RESULTS_V0.md` | prevents output-only closeout | process_asset_candidate | `PV_RETURN_TO_SPACE_CLOSEOUT` | done without memory | no automatic memory promotion | keep_existing |
| line | Return-to-Space Recovery | `docs/reports/lacl_regrounding_deep_exploration_result_20260506_v0.md` | forces reusable closeout value | candidate_input | `PV_RETURN_TO_SPACE_CLOSEOUT` | dead-end closeout | no automatic memory promotion | add_candidate |
| axis | external runtime trace vs VectorFL space memory | `docs/reports/lacl_regrounding_gemini_persisted_assets_packaging_20260506_v0.md` | decides raw trace vs interpreted memory | reusable_setting_candidate | `PV_RAW_TRACE_BOUNDARY` | worker authority drift | no tool output as final memory | add_candidate |
| camera | space recovery camera | `docs/reports/lacl_regrounding_deep_exploration_result_20260506_v0.md` | detects output-only completion | candidate_input | `PV_RETURN_TO_SPACE_CLOSEOUT` | missing movement record | no done-without-return | add_candidate |
| lens_gate | Plan Basis Gate | `docs/reports/lacl_regrounding_deep_exploration_result_20260506_v0.md` | blocks model-default planning | operating_anchor_candidate | `PV_PLAN_BASIS_GATE` | decorative LACL | no plan without evidence pointers | merge_overlap |
| conflict_overlap | Gemini PV aliases vs canonical PV IDs | `docs/specs/anchor_position_value_layer_setup_v0.md` | normalizes handoff position values | correction_record | `PV_LINE_MATURITY_CAUTION` | alias drift | no duplicate PV family | revise_candidate |

## Codex Actions

Use these after Gemini returns:

- `keep_existing`
- `revise_candidate`
- `add_candidate`
- `merge_overlap`
- `hold_for_evidence`
- `reject_overreach`

## Do Not

- Do not fill this matrix with unsupported terms.
- Do not infer maturity from repeated wording alone.
- Do not merge camera and lens just because they share words.
- Do not promote line/axis/camera/lens into ontology.
