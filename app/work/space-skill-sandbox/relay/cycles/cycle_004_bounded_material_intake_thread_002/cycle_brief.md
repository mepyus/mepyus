# Cycle Brief
# cycle_004_bounded_material_intake_thread_002
# 2026-05-13 Candidate v0

cycle_id:
  cycle_004_bounded_material_intake_thread_002

status:
  CYCLE_READY_FOR_GEMINI

authority:
  bounded material intake setup only

not:
  material processing
  Gemini execution
  automation
  workflow
  registry
  schema
  ontology
  baseline
  current-position
  output_manifest
  Big Frame Candidate Map rewrite

---

## 1. Purpose

Prepare a bounded operating thread for one actual material input.

large_frame_layer:
  Material Intake / Camera-Lens Reading / Return-to-Space Recovery

---

## 2. Approval Scope

user_instruction_raw:
  긱뉴스를 검색해서 넣을 재료를 찾아서 넣어보자

interpreted_approval_scope:
  insert the selected GeekNews Agent Skills material into Operating Thread 002 and prepare Gemini work_order only

not_approved_items:
  - Gemini execution by Codex
  - material analysis by Codex
  - automation
  - baseline promotion
  - workflow / registry / schema / ontology promotion
  - broad repo read
  - Big Frame rewrite
  - current-position update
  - output_manifest update
  - new vessel-level structure creation

stop_condition:
  stop after preparing cycle_004 for Gemini and return the work_order path

approval_recorded_by:
  ChatGPT / Supervisor

approval_scope_watch:
  external material intake must not become automation approval or workflow promotion

---

## 3. This Cycle Will Do

- wait for one user-provided material
- prepare Gemini to perform bounded intake observation later
- preserve Camera / Lens distinction
- detect structural gaps if any
- support return-to-space recovery after Gemini return

---

## 4. This Cycle Will Not Do

- process material before user provides it
- run Gemini
- create automation
- promote anything to baseline
- update current-position
- update output_manifest
- rewrite Big Frame Candidate Map
- perform broad repo read

---

## 5. Material Slot

material_status:
  MATERIAL_INSERTED_READY_FOR_GEMINI

material:
  GeekNews -- Agent Skills

Source:
  GeekNews topic id 29200
  https://news.hada.io/topic?id=29200

Context:
  Operating Thread 002 had been created as a material intake slot.
  The previous "next" material is retained only as an approval-scope test candidate.
  It is not treated as the first real material intake.
  This is the first real external material selected for Operating Thread 002.

Material summary:
  Agent Skills is a GeekNews item about Markdown-based skill scaffolding for AI coding agents.
  The article says skills are closer to workflows than reference documents because they include step order, checkpoint evidence, and exit criteria.
  It also frames the purpose as preventing AI coding agents from skipping senior engineering practices such as specification, testing, reviewable PRs, and trust-boundary review.

User Purpose:
  Use this as the first real material intake test after creating the Vessel / Contents Separation Spec.
  Determine whether Agent Skills should be read as content inside the existing vessel, processing mechanism, safety guard / guardrail, autonomy support, or risky workflow / automation candidate.

Core question:
  Is Agent Skills a new cup, or a drink / handling part inside the existing VectorFL vessel?

first_anchor:
  app/work/space-skill-sandbox/outputs/vectorfl_vessel_contents_separation_spec_20260513_candidate_v0.md

optional_anchors_only_if_needed:
  - app/work/space-skill-sandbox/outputs/operating_term_disambiguation_table_20260513_candidate_v0.md
  - app/work/space-skill-sandbox/outputs/codex_gemini_chatgpt_lane_contract_20260513_candidate_v0.md
  - app/work/space-skill-sandbox/outputs/manual_cycle_relay_operating_contract_20260513_candidate_v0.md

material_boundary:
  use only the provided material and the first anchor by default; use optional anchors only if needed

---

## 6. Lanes

Gemini lane:
  ready for manual Gemini transfer

Codex lane:
  setup cycle files only

ChatGPT / Supervisor lane:
  select/approve material and later review Gemini return

User gate:
  user must manually transfer gemini_work_order.md to Gemini

---

## 7. Hard Stops

- no material processing yet
- no Gemini execution yet
- no automation
- no scripts
- no current-position update
- no output_manifest update
- no baseline / workflow / registry / schema / ontology promotion
- no Big Frame Candidate Map rewrite
- no broad repo read

---

## 8. Expected Cycle Return

expected cycle return:
  after Gemini later runs, one cycle-level observation with recovered judgment, WATCH/HOLD, and Codex request status

Placement options:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD
