# INSTRUCTION_20260506_SMALL_ANCHOR_GENERATION_RULE_V1_SETUP

## Status

```yaml
status: instruction_candidate
date: 2026-05-06
baseline_lock: false
automation: false
schema: false
registry: false
work_id: SMALL_ANCHOR_GENERATION_RULE_V1_SETUP
```

## Purpose

Set up `small_anchor_generation_rule_v1` by incorporating the new operating principles and the broad-deep Gemini material topology survey.

The goal is not to make a final registry or ontology.

The goal is to make future small anchors more concrete by adding:

```text
route + PV + LACL + material family + signal zone + recognition marker
```

to the existing small-anchor generation logic.

## Current Position

Start here:

```text
app/work/CURRENT_POSITION_20260506_ANCHOR_STACK_AFTER_SET_A_V0.md
```

Current package marker:

```text
PKG_20260506_ANCHOR_STACK_OPERATIONAL_VALIDATION_V0
```

## PLAN_BASIS

```yaml
work_type: small_anchor_generation_rule_v1_setup
line: Plan from Space / Session Convergence Prevention
axis:
  - file-based anchor vs material-family-aware anchor
  - generic PV set vs task-specific LACL activation
  - small session split vs broad-but-bounded package
camera:
  - operator_perspective
  - space_recovery_camera
  - user_burden_camera
lens:
  - anchor_stack_maturation_lens
  - material_family_activation_lens
  - recognition_marker_lens
route:
  - ROUTE_SESSION_REENTRY
  - ROUTE_EXTERNAL_TOOL_PLANNING
  - ROUTE_BOUNDED_GEMINI_REREAD
position_ids:
  - PV_CURRENT_POSITION_ENTRY
  - PV_PLAN_BASIS_GATE
  - PV_BROAD_BOUNDED_PACKAGE
  - PV_NON_INSPECTED_DISCLOSURE
  - PV_RETURN_TO_SPACE_CLOSEOUT
  - PV_LINE_MATURITY_CAUTION
  - PV_RAW_TRACE_BOUNDARY
package_sizing_judgment: broad-but-bounded
return_shape: rule_v1_candidate + template_v1_candidate + material-family matrix + movement record update
```

## Inputs To Read

Read these first:

- `app/work/CURRENT_POSITION_20260506_ANCHOR_STACK_AFTER_SET_A_V0.md`
- `docs/specs/anchor_stack_big_frame_operating_structure_v0.md`
- `docs/indexes/anchor_stack_operating_surface_tiers_v0.md`
- `docs/specs/small_anchor_generation_rule_v0.md`
- `docs/specs/compact_position_anchor_template_v0.md`
- `docs/indexes/plan_from_space_position_map_seed_v0.md`
- `docs/indexes/anchor_map_position_route_seed_v0.md`
- `docs/specs/useful_shape_maturation_boundary_v0.md`
- `docs/specs/active_residue_marker_policy_v0.md`
- `app/work/MOVEMENT_RECORD_20260506_PLAN_FROM_SPACE_SETUP_V0.md`

Use these as worker evidence, not authority:

- Gemini broad-deep material topology survey return supplied by user
- `app/work/space-skill-sandbox/relay/prompts/gemini_broad_deep_lacl_material_topology_survey_20260506_v0.md`

Optional supporting read:

- `app/work/SPACE_MATERIAL_ACTIVATION_MAP_V0.md`
- `docs/indexes/lacl_candidate_synthesis_matrix_seed_v0.md`
- `docs/reports/anchor_stack_validation_lens_alignment_review_20260506_v0.md`
- `docs/reports/anchor_stack_session_execution_list_trial_20260506_v0.md`
- `docs/reports/anchor_stack_recognition_probe_result_20260506_v0.md`

## Required Output Files

Create candidate files only:

1. `docs/specs/small_anchor_generation_rule_v1_candidate.md`
2. `docs/specs/compact_position_anchor_template_v1_candidate.md`
3. `docs/indexes/small_anchor_material_family_matrix_v0.md`
4. `docs/reports/small_anchor_generation_rule_v1_setup_review_20260506_v0.md`

Update only if the setup succeeds:

- `docs/indexes/anchor_stack_manifest_v0.md`
- `app/work/MOVEMENT_RECORD_20260506_PLAN_FROM_SPACE_SETUP_V0.md`
- `app/work/CURRENT_POSITION_20260506_ANCHOR_STACK_AFTER_SET_A_V0.md`

## Rule v1 Must Add

Add these fields to small-anchor generation:

```yaml
material_family:
signal_zone:
recognition_markers:
read_depth_default:
when_to_deepen:
when_to_stop:
return_to_space_shape:
```

Keep the existing v0 fields:

```yaml
current_purpose:
position_ids:
position_meaning_now:
required_gate:
watch_signals:
do_not_infer:
return_shape:
```

## Material Families To Treat As Candidate

Use these as candidate families, not taxonomy:

```text
core_operating_anchors
space_navigation_maps
task_mode_gate_specs
sandbox_run_records
bounded_work_package_folders
worker_return_packaging_records
maturation_residue_policy
current_position_reentry_notes
external_material_intake_records
integrated_engine_operating_surface_records
```

For each family in the matrix, define:

```yaml
material_family:
default_route:
alternate_routes:
default_position_ids:
default_lacl:
read_depth_default: shallow | medium | deep
when_to_deepen:
when_to_stop:
return_to_space_shape:
recognition_markers:
watch:
do_not_infer:
```

## Small Anchor Use Cases To Include

At minimum include examples for:

1. external tool planning
2. Gemini broad/deep exploration
3. manual worker return packaging
4. current-position recovery
5. residue / active marker sampling
6. package closeout review
7. external material intake
8. integrated engine / operating surface work

Each example must include:

```yaml
anchor_use_case:
material_family:
signal_zone:
line:
axis:
camera:
lens:
route:
position_ids:
recognition_markers:
read_depth_default:
when_to_deepen:
when_to_stop:
return_to_space_shape:
watch:
do_not_infer:
```

## Acceptance Checks

Pass only if:

- v1 changes anchor behavior beyond v0
- each use case selects material families before file lists
- every example includes canonical PV IDs
- every example includes recognition markers
- every example includes stop/deepen rules
- no new PV is introduced unless necessary
- no candidate family is called taxonomy, ontology, registry, or baseline
- Movement Record receives reusable judgment

Hold if:

- Gemini survey is copied as authority
- material families become a global taxonomy
- v1 grows into a heavy manual that small anchors will not use
- anchor examples include more than 4 PVs without a blocking reason
- read depth defaults encourage broad scan

## Do Not

- Do not edit `small_anchor_generation_rule_v0.md`; create v1 candidate separately.
- Do not promote v1 to baseline.
- Do not create automation, writer, runner, schema, registry, or controller.
- Do not treat Gemini's broad-deep survey as full-space coverage.
- Do not add `PV_AUTHORITY_DOWNSHIFT` as canonical unless it already exists in `plan_from_space_position_map_seed_v0.md`.
- Do not bulk-label the repo.
- Do not make material family a final ontology.

## Return-to-Space Requirement

Closeout must include:

```yaml
recoverable_material:
  - v1 rule candidate
  - v1 template candidate
  - material family matrix candidate
reusable_judgment:
  - how v1 changes small anchor setup
issue_watch:
  - what remains candidate / hold
future_reuse_note:
  - which small anchor should be trialed next
recognition_markers:
  - SMALL_ANCHOR_GENERATION_RULE_V1_SETUP
  - small_anchor_material_family_matrix
  - material_family_aware_anchor
  - PKG_20260506_ANCHOR_STACK_OPERATIONAL_VALIDATION_V0
recommended_review_label:
  - PASS_AS_MATERIAL_FAMILY_AWARE_SMALL_ANCHOR_SETUP
  - PASS_WITH_WATCH
  - HOLD_FOR_OVERPROMOTION_RISK
```

