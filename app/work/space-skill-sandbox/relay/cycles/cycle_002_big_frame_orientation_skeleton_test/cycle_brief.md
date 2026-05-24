# Cycle Brief
# cycle_002_big_frame_orientation_skeleton_test

cycle_id:
  cycle_002_big_frame_orientation_skeleton_test

status:
  CYCLE_READY_FOR_GEMINI

authority:
  manual cycle setup only

not:
  final Big Frame Candidate Map
  map draft approval
  final framework
  workflow
  registry
  schema
  baseline
  product architecture
  dashboard
  routing authority
  automation
  current-position update
  output_manifest update

## 1. Purpose

Test whether Codex-created Big Frame orientation skeleton can support Gemini execution without long prompt relay.

large_frame_layer:
  Big Frame Candidate Map / Orientation Skeleton / Manual Cycle Relay Trial

## 2. This Cycle Will Do

- provide Gemini a bounded work order
- provide Gemini a skeleton to inspect
- test whether Gemini can execute from cycle files
- identify structural gaps if any

## 3. This Cycle Will Not Do

- create final Big Frame Candidate Map
- approve map creation
- update current-position
- update output_manifest
- create automation
- create scripts
- promote workflow / registry / baseline / schema

## 4. Lanes

Gemini lane:
  inspect skeleton / perform limited dry-fill if useful / return one cycle-level result

Codex lane:
  structure implementation only; process Codex request queue later only if Gemini creates requests

ChatGPT / Supervisor lane:
  review Gemini cycle return and decide placement

User gate:
  manual transfer of gemini_work_order path to Gemini
  explicit approval required before final map draft

## 5. Hard Stops

- no final map
- no map draft approval
- no automation
- no scripts
- no current-position update
- no output_manifest update
- no baseline / workflow / registry / schema promotion
- no product architecture

## 6. Expected Cycle Return

Expected cycle return:
  Gemini cycle observation return with skeleton usability, WATCH / HOLD, and structural-gap status

Placement options:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD

