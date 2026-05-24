# Closed-loop Stress Test
# Codex Case

## 1. Status

Status:
  MATERIALIZED_FROM_SOURCE_22_WITH_WATCH

Source:
  `22.md`

Purpose:
  Verify that an execution-capable external tool can receive a bounded packet, return through Return Packet, and re-enter Maturation Queue without becoming authority.

Not:
  real Codex execution
  file read
  file write
  command execution
  baseline promotion

## 2. Initial Input

User intent:
  Codex에게 특정 repo-side 작업을 맡기고 싶다.

Example task:
  Inspect whether the One-page Operator Surface is sufficient for first-pass external tool candidate classification.

Current approval:
  chat-only simulation only

## 3. One-page Operator Surface

Candidate:
  Codex as execution-capable external tool

Actual boundary:
  repo inspection, file read, possible file modification, command execution possibility, patch proposal/application, run record generation

Decision:
  BOUNDED_TEST_CANDIDATE_WITH_WATCH

Allowed now:
  build Codex packet draft

HOLD:
  Codex execution
  repo read
  file modification
  command execution
  AGENTS.md / SKILL.md / eval creation
  baseline promotion

WATCH:
  Codex capability -> permission
  repo affordance -> task authority
  patch success -> direction approval
  file change -> structural promotion
  run record -> baseline

## 4. Packet Builder Output

target_tool:
  Codex

tool_mode:
  execution-capable

risk_focus:
  file / command / patch / repo-affordance drift

task:
  Inspect whether the One-page Operator Surface is sufficient for first-pass external tool candidate classification.

smallest_anchor:
  One-page Operator Surface
  Small Tool Boundary Drift Pattern summary
  three decision anchors

allowed:
  read provided anchors only
  identify missing fields or ambiguity
  return usability judgment
  suggest minimal wording improvements in chat only

forbidden:
  file creation
  file modification
  command execution
  broad repo search
  eval creation
  AGENTS.md / SKILL.md update
  baseline promotion
  current-position update
  output_manifest update

return_format:
  Return Packet v0

hard_stop:
  stop before reading outside anchors, editing files, repo-wide restructuring, or promotion

post_return_route:
  Return Packet -> Maturation Queue Item -> Daily Circulation Loop

## 5. Simulated Return Packet

verdict:
  CODEX_PACKET_REVIEW_RETURNED_WITH_WATCH

direct_answer:
  One-page Operator Surface is usable for first-pass classification.

recovered_judgment:
  The one-page surface is sufficient as an operator-facing entry point, but examples must remain anchors, not fixed ontology.

usable:
  Preserve the reminder: "Examples guide classification but do not determine it."

WATCH:
  examples becoming fixed ontology
  BOUNDED_TEST_CANDIDATE becoming execution approval
  one-page becoming policy
  missing-field pressure expanding the packet again

HOLD:
  file modification
  schema expansion
  eval creation
  AGENTS.md / SKILL.md update
  baseline promotion

do_not_repeat:
  Do not expand the one-page surface every time a new ambiguity appears.

placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH

next:
  keep one-page unchanged; if ambiguity repeats, create WATCH note before editing surface

## 6. Maturation Queue Item

source_type:
  Codex Return Packet

origin_lane:
  Codex

recovered_judgment_candidate:
  One-page Operator Surface is usable, but examples must remain anchors, not ontology.

WATCH:
  examples -> fixed ontology
  one-page -> policy
  Codex review -> authority

HOLD:
  immediate surface modification
  schema/eval/baseline promotion

repeat_signal:
  medium

promotion_risk:
  medium

placement_candidate:
  WATCH_PATTERN_CANDIDATE and COMPRESS_ONLY

## 7. Daily Loop Output

repeated:
  Example-as-Ontology Drift

conflict:
  none strong

packet_next:
  future tool candidate classification packet

compression:
  One-page surface remains usable; examples guide but do not determine placement.

hard_stop:
  no file modification
  no surface update
  no baseline promotion

## 8. Re-entry Compression

Final reading:
  Codex case proves the closed loop can handle execution-capable tools without giving whole-space access or treating Codex return as authority.

Do not repeat:
  Do not give Codex whole-space access.
  Do not treat Codex review as approval.
  Do not treat examples as ontology.

Next:
  compare with Gemini broad-reading case.

`STATUS: CLOSED_LOOP_CODEX_STRESS_TEST_MATERIALIZED_WITH_WATCH`
