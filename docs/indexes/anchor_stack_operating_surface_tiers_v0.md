# Anchor Stack Operating Surface Tiers v0

## Status

```yaml
status: operating_surface_tiers_candidate
date: 2026-05-06
baseline_lock: false
automation: false
schema: false
registry: false
scope: anchor_stack_file_tiers
```

## Purpose

Reduce wobble by separating files into operating tiers.

This tier map tells future work which files to read first and which files are evidence, candidate, watch, or raw trace.

## Tier 1. Active Operating Core Pool

Use these as the active pool for normal re-entry and external planning.

This is not a read-all list. A future session should start with Current Position and Big Frame, then select only the route/PV-specific files needed for the current task.

| Surface | File |
| --- | --- |
| current position | `app/work/CURRENT_POSITION_20260506_ANCHOR_STACK_AFTER_SET_A_V0.md` |
| big frame | `docs/specs/anchor_stack_big_frame_operating_structure_v0.md` |
| stable anchor | `docs/specs/stable_space_operating_anchor_v0.md` |
| line map | `docs/indexes/plan_from_space_line_asset_map_v0.md` |
| route seed | `docs/indexes/anchor_map_position_route_seed_v0.md` |
| position map | `docs/indexes/plan_from_space_position_map_seed_v0.md` |
| gate sequence | `docs/specs/anchor_stack_plan_mode_gate_sequence_v0.md` |
| plan wrapper | `docs/specs/external_tool_plan_prompt_wrapper_v0.md` |
| review checklist | `docs/specs/anchor_stack_gate_checklist_v0.md` |
| Movement Record | `app/work/MOVEMENT_RECORD_20260506_PLAN_FROM_SPACE_SETUP_V0.md` |

Rule:

Do not bulk-read Tier 1. Treat it as the small active pool from which the current route selects 3-7 relevant surfaces.

Do not read beyond Tier 1 unless a route, gate, or validation lens asks for evidence support.

## Tier 2. Candidate Extension Surfaces

Use when the work is about maturation, residue, route overlap, or runner watch:

| Surface | File |
| --- | --- |
| useful shape maturation | `docs/specs/useful_shape_maturation_boundary_v0.md` |
| active/residue marker policy | `docs/specs/active_residue_marker_policy_v0.md` |
| runner reliability watch | `docs/specs/external_tool_runner_reliability_watch_v0.md` |
| compact position anchor template | `docs/specs/compact_position_anchor_template_v0.md` |
| external plan return review | `docs/specs/external_tool_plan_return_review_template_v0.md` |

Rule:

Candidate extension surfaces may guide bounded trials. They do not become baseline policies by being referenced.

## Tier 3. Evidence / Alignment Surfaces

Use when checking whether the setup still matches the May 6 inputs or local space records:

| Surface | File |
| --- | --- |
| nine-doc alignment | `docs/reports/may6_nine_doc_anchor_stack_alignment_review_v0.md` |
| route input evidence | `docs/indexes/anchor_route_input_evidence_matrix_v0.md` |
| current position check | `docs/reports/current_position_check_20260506_anchor_stack_after_set_a_v0.md` |
| Set A worker review | `docs/reports/gemini_external_tool_planning_trial_set_a_return_review_20260506_v0.md` |

Rule:

Evidence surfaces support judgment. They are not the active operating core unless promoted through Movement Record.

Validation rule:

When a route is used for the first time, revised, promoted, or challenged, spot-check Tier 3 evidence before accepting the structure as space-grounded.

## Tier 4. Worker Return / Raw Trace Surfaces

Use when packaging or auditing external tool outputs:

| Surface | File |
| --- | --- |
| Gemini compact crosscheck return | `docs/reports/plan_from_space_anchor_stack_gemini_compact_crosscheck_return_v0.md` |
| Gemini bounded exploration manual return | `docs/reports/plan_from_space_bounded_exploration_gemini_manual_return_v0.md` |
| Gemini LACL persisted packaging | `docs/reports/lacl_regrounding_gemini_persisted_assets_packaging_20260506_v0.md` |
| Gemini route discovery packaging | `docs/reports/gemini_anchor_map_position_discovery_return_packaging_20260506_v0.md` |
| Gemini Set A review | `docs/reports/gemini_external_tool_planning_trial_set_a_return_review_20260506_v0.md` |

Rule:

Worker returns are never final authority. They require Codex packaging and downshift checks.

## Tier 5. Manifest / Discovery Surface

Use only when you need to find files:

| Surface | File |
| --- | --- |
| manifest | `docs/indexes/anchor_stack_manifest_v0.md` |

Rule:

The manifest is an index, not a registry and not a reading order.

## Default Read Path

For a future external planning request:

```text
Current Position
-> Big Frame
-> select route/PV
-> 3-7 route-specific active surfaces
-> Movement Record
```

For a future Gemini exploration request:

```text
Current Position
-> Big Frame
-> Route Seed
-> specific evidence surface named by route
-> worker return packaging
```

For a future residue sampling request:

```text
Current Position
-> Big Frame
-> Active/Residue Marker Policy
-> 5-8 named files only
-> Movement Record
```

## Do Not

- Do not use this as a registry.
- Do not bulk-read every tier.
- Do not promote Tier 2 or Tier 3 files without Movement Record evidence.
- Do not treat raw worker returns as operating core.
