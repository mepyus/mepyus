# Minimum Manual Application Scenarios
# VectorFL Circulation System v0

## 1. Status

Status:
  MATERIALIZED_FROM_SOURCE_26_WITH_WATCH

Source:
  `26.md`

Purpose:
  Apply the Minimum Operating Manual to bounded scenarios that do not require user approval, external execution, or promotion.

Not:
  automation
  dispatch
  baseline
  workflow
  schema
  registry
  ontology

## 2. Six Surfaces

1. One-page Operator Surface
2. Maturation Queue Item
3. Daily Circulation Loop
4. Packet Builder
5. Return Packet
6. Re-entry Compression

## 3. Scenario A - New External Tool Candidate

input:
  A new tool candidate appears.

surface_1_operator:
  classify by actual enablement boundary and current approval scope.

likely_decision:
  REFERENCE_ONLY if documentation only
  BOUNDED_TEST_CANDIDATE if useful but execution/file/API boundary exists
  HOLD if credential/API/account/upload/automation boundary exists
  USE_NOW only if exact approved action is complete

surface_2_queue_item:
  create a queue item only if the candidate produces reusable WATCH/HOLD or decision anchor material.

surface_3_daily_loop:
  compare with existing patterns:
  small tool -> harmless assumption
  capability -> permission
  read-only claim -> side-effect proof

surface_4_packet_builder:
  only if BOUNDED_TEST_CANDIDATE and a future bounded packet is justified.

surface_5_return_packet:
  if reviewed or tested, recover decision, WATCH, HOLD, do-not-repeat.

surface_6_compression:
  compress if it becomes a reusable anchor.

hard_stop:
  no execution or credential/API/account/file/browser/memory action without exact approval.

## 4. Scenario B - Returned Codex Result

input:
  Codex returns a repo-side result or patch summary.

surface_1_operator:
  not needed unless deciding future Codex use.

surface_2_queue_item:
  split mechanical result from recovered judgment:
  files read/written, commands run, patch summary, WATCH, HOLD.

surface_3_daily_loop:
  detect:
  patch success -> approval
  run record -> baseline
  repo affordance -> task authority

surface_4_packet_builder:
  if a next Codex task is needed, create execution-capable packet with file/command/write boundaries.

surface_5_return_packet:
  required for nontrivial Codex work.

surface_6_compression:
  final reading, do-not-repeat, next smallest action.

hard_stop:
  no current-position/output_manifest/baseline promotion unless explicitly approved.

## 5. Scenario C - Gemini Synthesis Return

input:
  Gemini returns broad reading or synthesis.

surface_1_operator:
  not needed unless deciding future Gemini use.

surface_2_queue_item:
  split observations, inferences, uncertainty, reusable lens candidates, WATCH, HOLD.

surface_3_daily_loop:
  detect:
  synthesis -> truth
  recommendation -> adoption
  external terminology -> ontology
  framework -> authority

surface_4_packet_builder:
  if more reading is needed, create broad-reading packet with selected excerpts and no-adoption hard stop.

surface_5_return_packet:
  use Analysis Return Packet shape.

surface_6_compression:
  retain reusable WATCH, not adoption direction.

hard_stop:
  no framework adoption, schema/workflow creation, architecture migration, or baseline promotion.

## 6. Scenario D - User Correction

input:
  User corrects the assistant's frame or execution mode.

surface_1_operator:
  use if correction authorizes bounded workspace action.

surface_2_queue_item:
  treat as high-priority active frame correction.

surface_3_daily_loop:
  detect conflict between previous assistant action and user intention.

surface_4_packet_builder:
  usually not needed unless external tool inspection is requested.

surface_5_return_packet:
  recover what changed in the active frame.

surface_6_compression:
  preserve do-not-repeat and next action.

hard_stop:
  do not turn one correction into permanent baseline without repeated confirmation.

## 7. Next Non-user-gated Work

If continuing without a new user decision, the next safe work is:

1. Keep enriching candidate artifacts under `dry_runs/`.
2. Do not dispatch external tools.
3. Do not promote any surface.
4. Do not update current-position or output manifests.

`STATUS: MINIMUM_MANUAL_APPLICATION_SCENARIOS_MATERIALIZED_WITH_WATCH`
