# Gemini Position Value Discovery Packet - Plan from Space

## Role

You are doing bounded space exploration for position values.

Do not summarize the whole space. Do not build ontology. Do not propose automation.

Your job is to find locations in the existing VectorFL space that can become compact position values for future small Session Space Anchors.

## Core Question

When a future anchor is small, what position values should it carry so the worker knows where it is in the space?

We need candidates like:

```yaml
position_id:
asset_family:
authority_state:
maturity_state:
active_line:
axis_tension:
camera_position:
lens_gate:
worker_boundary:
return_shape:
watch_signal:
reentry_trigger:
do_not_infer:
evidence_pointer:
```

## Read Scope

Use bounded representative reading. If a file is missing, mark `SOURCE_MISSING`.

Primary files:

- `docs/specs/anchor_position_value_layer_setup_v0.md`
- `docs/indexes/plan_from_space_position_map_seed_v0.md`
- `docs/indexes/space_asset_map_v0.md`
- `app/work/space-skill-sandbox/outputs/whole_space_orientation_atlas_candidate_v0.md`
- `docs/reports/whole_space_four_maturation_axes_orientation_candidate_v0.md`
- `docs/reports/whole_space_deep_reread_pipeline_setup_v0.md`
- `docs/reports/whole_space_deep_reread_pipeline_record_v0.md`
- `docs/reports/whole_space_deep_reread_gemini_result_packaging_v0.md`
- `docs/indexes/plan_from_space_line_asset_map_v0.md`
- `docs/reports/plan_from_space_bounded_exploration_gemini_manual_return_v0.md`
- `docs/specs/manual_external_tool_relay_bridge_note_v0.md`

Secondary only if needed:

- `app/work/space-skill-sandbox/outputs/line_axis_synthesis_report_candidate_v0.md`
- `app/work/space-skill-sandbox/outputs/reusable_operating_settings_catalog_v0.md`
- four line-axis reference notes if present:
  - `app/work/space-skill-sandbox/outputs/harness_orientation_reread_to_line_axis_reference_v0.md`
  - `app/work/space-skill-sandbox/outputs/affordance_program_reread_to_line_axis_reference_v0.md`
  - `app/work/space-skill-sandbox/outputs/signal_memory_reread_to_line_axis_reference_v0.md`
  - `app/work/space-skill-sandbox/outputs/provenance_integrity_reread_to_line_axis_reference_v0.md`

## Output Required

Return:

1. `Position Candidates`
   - 6 to 12 candidates.
   - Use the YAML-like field set above.
   - Include evidence pointer for each candidate.

2. `Map Position Families`
   - group candidates by asset family and authority/maturity state.

3. `Best Positions For Small Anchors`
   - choose 3 to 5 that should travel in the next Session Space Anchor.

4. `Missing / Unclear Map Areas`
   - bounded future reads only.

5. `HOLD / Do Not Promote`
   - what must not become baseline, workflow, registry, schema, automation, or ontology.

6. `Return-to-Space Value`
   - reusable findings for Codex to synthesize into the position map.

## Constraints

- Do not say ready or baseline.
- Do not propose implementation.
- Do not create a universal taxonomy.
- Do not treat line/axis/camera/lens as law.
- Do not treat Gemini output as verified truth.
- Keep it compact.
