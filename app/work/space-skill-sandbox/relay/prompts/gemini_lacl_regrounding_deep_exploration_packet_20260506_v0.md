# Gemini Deep Exploration Packet - Line / Axis / Camera / Lens Re-Grounding

## Role

You are doing deep bounded exploration for VectorFL.

Your task is not to summarize the whole space.

Your task is to collect evidence and propose candidate data needed to re-ground:

```text
line / axis / camera / lens
```

so future small anchors can transmit effective position values.

## Why This Matters

The current Anchor Stack can say:

```text
Line: Plan from Space / Session Convergence Prevention
Axis: small split vs broad-but-bounded package
Camera: user relay burden
Lens: Plan Basis / Return-to-Space
```

But these can become decorative unless grounded in repeated space data.

We need to know:

- which lines are real long-flow continuities
- which axes actually change plan shape
- which cameras prevent wrong completion
- which lenses are reliable gates
- which position values should travel in small anchors

## Input Bundle A - User May Supply

If the user provides the May 6 nine documents, read them first:

- `05-06/1.md`
- `05-06/2.md`
- `05-06/3.md`
- `05-06/4.md`
- `05-06/5.md`
- `05-06/6.md`
- `05-06/7.md`
- `05-06/8.md`
- `05-06/9.md`

If they are not available, mark:

```text
SOURCE_MISSING: MAY6_NINE_DOCS
```

and continue with repo-local assets.

## Input Bundle B - Current Anchor / Position Setup

Read these:

- `docs/reports/may6_nine_doc_anchor_stack_alignment_review_v0.md`
- `docs/specs/space_anchor_stack_operating_setup_v0.md`
- `docs/specs/stable_space_operating_anchor_v0.md`
- `docs/indexes/plan_from_space_line_asset_map_v0.md`
- `docs/specs/session_space_anchor_template_v0.md`
- `docs/specs/plan_basis_template_v0.md`
- `docs/specs/anchor_position_value_layer_setup_v0.md`
- `docs/indexes/plan_from_space_position_map_seed_v0.md`
- `docs/specs/compact_position_anchor_template_v0.md`
- `docs/reports/position_value_discovery_gemini_return_packaging_v0.md`
- `docs/specs/position_value_application_trial_packet_v0.md`

## Input Bundle C - Whole-Space Orientation / Prior Deep Reread

Read these for wider structure:

- `docs/indexes/space_asset_map_v0.md`
- `app/work/space-skill-sandbox/outputs/whole_space_orientation_atlas_candidate_v0.md`
- `docs/reports/whole_space_four_maturation_axes_orientation_candidate_v0.md`
- `docs/reports/whole_space_deep_reread_pipeline_setup_v0.md`
- `docs/reports/whole_space_deep_reread_pipeline_record_v0.md`
- `docs/reports/whole_space_deep_reread_gemini_result_packaging_v0.md`

## Input Bundle D - Line / Axis / Camera / Lens Candidate Records

Read these if present. Mark missing files explicitly and continue.

- `app/work/space-skill-sandbox/outputs/line_axis_synthesis_report_candidate_v0.md`
- `app/work/space-skill-sandbox/outputs/reusable_operating_settings_catalog_v0.md`
- `app/work/space-skill-sandbox/outputs/harness_orientation_reread_to_line_axis_reference_v0.md`
- `app/work/space-skill-sandbox/outputs/affordance_program_reread_to_line_axis_reference_v0.md`
- `app/work/space-skill-sandbox/outputs/signal_memory_reread_to_line_axis_reference_v0.md`
- `app/work/space-skill-sandbox/outputs/provenance_integrity_reread_to_line_axis_reference_v0.md`
- `docs/specs/line_maturity_and_operating_anchor_direction_lock_v0.md`

## Input Bundle E - External Tool / Return / Boundary Records

Read as needed:

- `app/work/PROGRAM_FRAME_EXTERNAL_PATTERN_MAP_V0.md`
- `app/work/SESSION_43_RESULTS_V0.md`
- `app/work/SESSION_44_RESULTS_V0.md`
- `app/work/SESSION_46_RESULTS_V0.md`
- `app/work/SESSION_47_RESULTS_V0.md`
- `docs/reports/space_feedback_loop_return_to_space_record_minimum_v0.md`
- `docs/specs/manual_external_tool_relay_bridge_note_v0.md`
- `docs/reports/plan_from_space_bounded_exploration_gemini_manual_return_v0.md`

## Output Required

Return a report with these sections.

### 1. Read Trace

List:

- files read
- files missing
- files not inspected
- files only lightly inspected

Do not claim full-space coverage.

### 2. Current Line Candidates

For each candidate line, return:

```yaml
line_name:
evidence_pointers:
what_continuity_it_tracks:
what_tasks_should_use_it:
maturity_state: reading_lens | comparison_memory | operating_anchor_candidate | hold
watch:
do_not_infer:
```

Include at least:

- Plan from Space / Session Convergence Prevention
- Return-to-Space Recovery
- User Relay Burden Reduction
- External Tool Boundary / Raw Trace

Add others only if evidence supports them.

### 3. Axis Candidates

For each axis, return:

```yaml
axis_name:
evidence_pointers:
what_plan_decision_it_changes:
paired_risks:
use_when:
watch:
```

Focus on axes that change work shape, not labels.

### 4. Camera Candidates

For each camera, return:

```yaml
camera_name:
evidence_pointers:
what_wrong_completion_it_prevents:
user_or_space_value:
use_when:
watch:
```

### 5. Lens / Gate Candidates

For each lens/gate, return:

```yaml
lens_name:
evidence_pointers:
pass_condition:
hold_condition:
watch_condition:
what_return_shape_it_requires:
```

### 6. LACL -> Position Value Mapping

Map line/axis/camera/lens candidates to existing or new position IDs.

Use existing IDs where possible:

- `PV_PLAN_BASIS_GATE`
- `PV_BROAD_BOUNDED_PACKAGE`
- `PV_RAW_TRACE_BOUNDARY`
- `PV_MANUAL_RELAY_BRIDGE`
- `PV_NON_INSPECTED_DISCLOSURE`
- `PV_LINE_MATURITY_CAUTION`
- `PV_RETURN_TO_SPACE_CLOSEOUT`
- `PV_CURRENT_POSITION_ENTRY`
- `PV_BOUNDED_REREAD_UNIT`

Propose new `PV_*` only if necessary.

### 7. Best Small-Anchor Sets

Give 3 recommended compact anchor sets:

1. external tool planning
2. bounded Gemini reread
3. manual relay / worker return packaging

Each set should contain only 2-4 position IDs.

### 8. Conflict / Overlap / Missing Data

Identify:

- line overlaps
- axis overlaps
- camera/lens confusion
- missing evidence
- older records needing active/residue sampling

### 9. HOLD / Do Not Promote

State what must remain:

- not baseline
- not ontology
- not schema
- not registry
- not workflow
- not automation
- not current-position update

### 10. Return-to-Space Value

Return:

- reusable findings
- position IDs that should be updated
- new candidate position IDs if any
- next bounded read candidate
- what Codex should synthesize next

## Constraints

- You may read deeply and use substantial tokens.
- Stay evidence-backed.
- Do not invent missing files.
- Do not promote any candidate to baseline.
- Do not turn line / axis / camera / lens into ontology.
- Do not propose implementation or automation.
- Do not ask the user to relay more than the resulting report.
