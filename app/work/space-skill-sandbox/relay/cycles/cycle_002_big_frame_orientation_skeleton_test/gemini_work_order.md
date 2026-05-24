# Gemini Work Order
# cycle_002_big_frame_orientation_skeleton_test

cycle_id:
  cycle_002_big_frame_orientation_skeleton_test

status:
  READY_TO_SEND_TO_GEMINI

target:
  Gemini

role:
  execution / observation lane inside Manual Cycle Relay

authority:
  cycle work order only

not:
  final Big Frame Candidate Map
  workflow
  registry
  schema
  baseline
  product architecture
  dashboard
  routing authority
  current-position update
  output_manifest update
  automation
  final authority

## 1. Task

Read the Big Frame Candidate Map Orientation Skeleton and inspect whether it is sufficient as an orientation-only heatmap skeleton.

This cycle does not create the final map.
This cycle does not draft the final map.
This cycle does not approve map creation.

## 2. Questions To Answer

Gemini must answer:

1. Is the skeleton sufficient for orientation-only map drafting later?
2. Does it avoid becoming workflow / registry / current-position / routing authority?
3. What minimal parts are usable?
4. What remains WATCH?
5. What remains HOLD?
6. Is a limited dry-fill useful or should it remain empty?
7. Does any structural gap require Codex?
8. Should next owner be ChatGPT, Codex, User, or HOLD?

## 3. Read Scope

Required:

- app/work/space-skill-sandbox/outputs/big_frame_candidate_map_orientation_skeleton_20260513_candidate_v0.md
- app/work/space-skill-sandbox/outputs/big_frame_candidate_map_preparation_recovery_20260512_candidate_v0.md
- app/work/space-skill-sandbox/outputs/big_frame_consolidation_readiness_recovery_20260512_candidate_v0.md

Optional if needed:

- app/work/space-skill-sandbox/outputs/active_reentry_surface_genealogy_recovery_20260512_candidate_v0.md
- app/work/space-skill-sandbox/outputs/return_to_space_recovery_genealogy_recovery_20260512_candidate_v0.md
- app/work/space-skill-sandbox/outputs/promotion_caution_genealogy_recovery_20260512_candidate_v0.md

## 4. Do Not Read

- entire repo
- all runs
- raw logs
- broad Obsidian vault
- implementation files
- output_manifest unless explicitly necessary
- current-position unless explicitly necessary
- credential / token material

## 5. Structural Gap Rule

If Gemini finds a structure gap:

Do not solve it directly.

Add a Codex request entry suitable for:

app/work/space-skill-sandbox/relay/cycles/cycle_002_big_frame_orientation_skeleton_test/codex_request_queue.md

Each request should include:

- request_id
- structural_gap
- requested_codex_work
- expected_output
- priority
- forbidden_actions

Codex should not act until user transfers this queue or ChatGPT / Supervisor approves.

## 6. Return Format

Verdict:
  GEMINI_CYCLE_002_OBSERVATION_RETURNED_WITH_WATCH / STRUCTURAL_GAP_FOUND / WATCH_ONLY / HOLD

Cycle:
  cycle_002_big_frame_orientation_skeleton_test

Directly inspected:
  - ...

Not inspected:
  - ...

Skeleton usability:
  ...

Limited dry-fill:
  useful / not needed / unsafe

Main finding:
  ...

Recovered judgment candidates:
  - ...

What is usable:
  - ...

What remains WATCH:
  - ...

What remains HOLD:
  - ...

Structural gaps found:
  none / list

Codex requests needed:
  none / list

If Codex request needed:
  request_id:
  structural_gap:
  requested_codex_work:
  expected_output:
  priority:
  forbidden_actions:

Suggested next owner:
  ChatGPT / Codex / User / HOLD

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD

Do Not Promote:
  - ...

Next action:
  ...

## 7. Hard Boundaries

- no final Big Frame Candidate Map creation
- no workflow
- no registry
- no schema
- no baseline
- no product architecture
- no current-position update
- no output_manifest update
- no automation
- no final authority claim
- no repo modification

