# Gemini Work Order
# cycle_007_big_frame_gemini_execution_batch
# 2026-05-13 Candidate v0

## 1. Status

cycle_id:
  cycle_007_big_frame_gemini_execution_batch

status:
  READY_TO_SEND_TO_GEMINI

target:
  Gemini

role:
  execution / observation / verification lane inside Manual Cycle Relay

authority:
  observation return only

not:
  map creation
  release approval
  final authority
  workflow
  registry
  baseline
  current-position update
  automation

---

## 2. Task

Read the specified files and perform one bundled execution / observation check based on the current large-frame operating principle:

ChatGPT / User:
  large-frame design and judgment

Codex:
  structure implementation

Gemini:
  execution / observation / verification / structural gap detection

User:
  final approval and manual gate

Your job is to classify and evaluate the next Gemini-suitable work, not to design the large frame and not to create the map.

---

## 3. Required Read Scope

Read:

- app/work/space-skill-sandbox/outputs/gemini_execution_task_classification_20260513_candidate_v0.md
- app/work/space-skill-sandbox/outputs/manual_cycle_relay_progress_ledger_20260513_candidate_v0.md
- app/work/space-skill-sandbox/outputs/genealogy_reservoir_index_candidate_v0.md
- app/work/space-skill-sandbox/outputs/big_frame_candidate_map_release_decision_packet_20260513_candidate_v0.md
- app/work/space-skill-sandbox/outputs/big_frame_candidate_map_orientation_skeleton_20260513_candidate_v0.md
- app/work/space-skill-sandbox/relay/packets/to_codex/big_frame_candidate_map_draft_packet_20260513_v0.md
- app/work/space-skill-sandbox/outputs/codex_gemini_chatgpt_lane_contract_20260513_candidate_v0.md

Optional only if needed:

- app/work/space-skill-sandbox/outputs/big_frame_candidate_map_preparation_recovery_20260512_candidate_v0.md
- app/work/space-skill-sandbox/outputs/big_frame_consolidation_readiness_recovery_20260512_candidate_v0.md
- app/work/space-skill-sandbox/outputs/manual_cycle_relay_operating_contract_20260513_candidate_v0.md

---

## 4. Do Not Read

Do not read:

- entire repo
- all runs
- raw logs
- broad Obsidian vault
- implementation files
- current-position files unless explicitly necessary
- output_manifest unless explicitly necessary

---

## 5. Questions To Answer

Answer as Gemini execution / observation lane:

1. Is the next Gemini-facing work correctly classified?
2. Is the Genealogy Reservoir Index sufficient as the preferred compressed source for a later map draft, or would it force too much rereading?
3. Should the existing Big Frame Candidate Map draft packet be revised before any execution?
4. Does the release decision surface clearly separate release readiness from release approval?
5. Does the current setup preserve the thin-surface principle?
6. Which parts are safe for Gemini to execute / observe next?
7. Which parts should Codex implement next?
8. Which parts require ChatGPT / User judgment?
9. What remains WATCH?
10. What remains HOLD?
11. Is there any structural gap requiring Codex?
12. Should the next owner be Codex, ChatGPT / User, Gemini, or HOLD?

---

## 6. Structural Gap Rule

If you find a structural gap:

Do not solve it directly.

Return a Codex request entry with:

- request_id
- structural_gap
- requested_codex_work
- expected_output
- priority
- forbidden_actions

Codex should not act until the user or ChatGPT / Supervisor accepts the request.

---

## 7. Hard Boundaries

Do not:

- create the Big Frame Candidate Map
- draft the map
- approve release
- revise the Codex packet yourself
- create workflow
- create registry
- create schema
- create baseline
- create product architecture
- update current-position
- update output_manifest
- create automation
- treat Gemini output as final authority
- turn next pull into automatic task

---

## 8. Return Format

Return exactly:

Verdict:
  GEMINI_CYCLE_007_EXECUTION_BATCH_RETURNED_WITH_WATCH / STRUCTURAL_GAP_FOUND / WATCH_ONLY / HOLD

Cycle:
  cycle_007_big_frame_gemini_execution_batch

Directly inspected:
  - ...

Not inspected:
  - ...

Task classification check:
  ...

Index sufficiency:
  ...

Draft packet revision need:
  not needed / recommended / required before release / HOLD

Release decision clarity:
  ...

Thin-surface fitness:
  ...

Safe for Gemini next:
  - ...

Codex implementation candidates:
  - ...

Requires ChatGPT / User judgment:
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
  Codex / ChatGPT + User / Gemini / HOLD

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD

Do Not Promote:
  - ...

Next action:
  ...

Hard boundaries confirmation:
  - no Big Frame Candidate Map creation
  - no map draft
  - no release approval
  - no workflow / registry / schema / baseline promotion
  - no current-position update
  - no output_manifest update
  - no automation
