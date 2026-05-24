# Cycle Brief
# cycle_001_big_frame_candidate_map_orientation

cycle_id:
  cycle_001_big_frame_candidate_map_orientation

status:
  CYCLE_READY_FOR_GEMINI

authority:
  manual cycle setup only

not:
  Big Frame Candidate Map
  map draft
  map creation approval
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

Test Manual Cycle Relay by asking Gemini to inspect whether Big Frame Candidate Map orientation conditions are safe, without creating the map.

large_frame_layer:
  Big Frame Candidate Map Orientation / Manual Cycle Relay Trial

## 2. This Cycle Will Do

- provide Gemini a bounded work order
- ask Gemini to inspect orientation-only map conditions
- ask Gemini to identify structural gaps if any
- ask Gemini to create Codex request entries if structure work is needed

## 3. This Cycle Will Not Do

- create Big Frame Candidate Map
- draft the map
- approve map creation
- update current-position
- update output_manifest
- create automation
- create scripts
- promote workflow / registry / baseline / schema

## 4. Lanes

Gemini lane:
  execute / observe / return one cycle-level result

Codex lane:
  only process Codex request queue later if Gemini creates requests

ChatGPT / Supervisor lane:
  review Gemini cycle return and decide placement

User gate:
  manual transfer of gemini_work_order path to Gemini
  explicit approval required before any map draft execution

## 5. Hard Stops

- no map creation
- no map draft
- no automation
- no scripts
- no current-position update
- no output_manifest update
- no baseline / workflow / registry / schema promotion
- no product architecture

## 6. Expected Cycle Return

Expected cycle return:
  Gemini cycle observation return with WATCH / HOLD and structural-gap status

Placement options:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD

