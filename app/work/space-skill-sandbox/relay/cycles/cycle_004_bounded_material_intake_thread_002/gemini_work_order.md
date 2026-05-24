# Gemini Work Order
# cycle_004_bounded_material_intake_thread_002
# 2026-05-13 Candidate v0

cycle_id:
  cycle_004_bounded_material_intake_thread_002

status:
  READY_TO_SEND_TO_GEMINI

target:
  Gemini

role:
  execution / observation lane inside Manual Cycle Relay

authority:
  pending bounded material intake observation only

not:
  automation
  broad repo read
  baseline
  workflow
  registry
  schema
  ontology
  current-position update
  output_manifest update
  Big Frame Candidate Map rewrite

---

## 1. Material Slot

material_status:
  MATERIAL_INSERTED_READY_FOR_GEMINI

material:
  GeekNews -- Agent Skills

Source:
  GeekNews topic id 29200
  https://news.hada.io/topic?id=29200

Material summary:
  Agent Skills is a GeekNews item about Markdown-based skill scaffolding for AI coding agents.
  The article says skills are closer to workflows than reference documents because they include step order, checkpoint evidence, and exit criteria.
  It also frames the purpose as preventing AI coding agents from skipping senior engineering practices such as specification, testing, reviewable PRs, and trust-boundary review.

User Purpose:
  Use this as the first real material intake test after creating the Vessel / Contents Separation Spec.
  Determine whether Agent Skills should be read as:
    - content inside the existing vessel
    - processing mechanism
    - safety guard / guardrail
    - autonomy support
    - or a risky workflow / automation candidate

Core question:
  Is Agent Skills a new cup, or a drink / handling part inside the existing VectorFL vessel?

material_source:
  selected GeekNews external material

Important:
  bounded material has been inserted.
  Gemini may execute this bounded material intake observation only when the user manually transfers this work_order path.

first_anchor:
  app/work/space-skill-sandbox/outputs/vectorfl_vessel_contents_separation_spec_20260513_candidate_v0.md

optional_anchors_only_if_needed:
  - app/work/space-skill-sandbox/outputs/operating_term_disambiguation_table_20260513_candidate_v0.md
  - app/work/space-skill-sandbox/outputs/codex_gemini_chatgpt_lane_contract_20260513_candidate_v0.md
  - app/work/space-skill-sandbox/outputs/manual_cycle_relay_operating_contract_20260513_candidate_v0.md

---

## 2. Task When Ready

task_when_ready:
  Read one bounded user-provided material and perform material intake observation.

Gemini must answer later:

1. What is the material?
2. What is the user purpose?
3. What is the smallest sufficient context?
4. Using the Vessel / Contents Separation Spec, classify the material:
   - vessel / container
   - content
   - inlet / intake
   - processing mechanism
   - recovery outlet
   - re-entry surface
   - safety lid / guardrail
   - label / status marker
   - autonomy support
   - mixed / WATCH
5. Which Camera / Lens candidates apply?
6. What useful judgment can be recovered?
7. What should not be read?
8. What remains WATCH?
9. What remains HOLD?
10. Is Codex structure work needed?
11. What is the suggested placement?

Specific focus:

- Does Agent Skills represent a new operating structure, or can it be treated as content / guardrail / autonomy support inside the existing vessel?
- Does it risk turning VectorFL into workflow / automation / skill registry?
- What part can be reused without creating new clutter?

---

## 3. Default Read Boundary

Default read boundary:
  use only the provided material and the first anchor by default; use optional anchors only if needed.

Do not read:
  - entire repo
  - all runs
  - raw logs
  - broad Obsidian vault
  - implementation files
  - output_manifest unless explicitly necessary
  - current-position unless explicitly necessary

---

## 4. Structural Gap Rule

If Gemini finds a structure gap:
  do not solve it directly.
  Add a Codex request entry suitable for codex_request_queue.md.

---

## 5. Hard Boundaries

- no automation
- no scripts
- no baseline promotion
- no workflow / registry / schema / ontology promotion
- no Big Frame Map rewrite
- no current-position update
- no output_manifest update
- no final authority claim

---

## 6. Return Format When Ready

Verdict:
  GEMINI_MATERIAL_INTAKE_RETURNED_WITH_WATCH / STRUCTURAL_GAP_FOUND / WATCH_ONLY / HOLD

Cycle:
  cycle_004_bounded_material_intake_thread_002

Material:
  ...

Directly inspected:
  - ...

Not inspected:
  - ...

Smallest sufficient context:
  ...

Camera / Lens candidates:
  - ...

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
  - material intake != baseline
  - Gemini return != truth
  - placement != approval
  - next pull != automatic task

Next action:
  ...

Hard boundaries confirmation:
  - no automation
  - no scripts
  - no broad repo read
  - no current-position update
  - no output_manifest update
  - no baseline / workflow / registry / schema / ontology promotion
