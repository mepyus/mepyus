# Gemini Work Order
# cycle_003_bounded_input_intake_thread_001
# 2026-05-13 Candidate v0

## 1. Status

cycle_id:
  cycle_003_bounded_input_intake_thread_001

status:
  READY_TO_SEND_TO_GEMINI

target:
  Gemini

role:
  execution / observation lane for one bounded input intake thread

authority:
  pending observation packet only

not:
  automation
  broad repo read
  baseline
  workflow
  registry
  current-position update
  output_manifest update
  Big Frame Candidate Map rewrite

---

## 2. Input Slot

input_status:
  INPUT_INSERTED_READY_FOR_GEMINI

input_material:
  같은 pipeline 구조라도,
  사고 흐름 / Codex-Gemini 전달 / 기존 공간의 처리 파이프라인은
  구조적으로는 비슷하지만 의미 해석이 다르다.

  그래서 Camera / Lens가 필요하다.
  같은 구조를 어떤 관점으로 읽느냐에 따라
  그것은 사고의 흐름이 되기도 하고,
  실행 전달 구조가 되기도 하고,
  회수 구조가 되기도 한다.

input_source:
  user-provided short internal memo

Important:
  user-provided input has been inserted.
  Gemini may execute this bounded intake observation when the user manually transfers this work_order path.

---

## 3. Task When Input Is Ready

When the user provides one short input material, observe it through the current VectorFL operating frame.

Answer:

1. What is the input?
2. What is the smallest sufficient context?
3. Which Camera / Lens candidates apply?
4. What useful judgment can be recovered?
5. What remains WATCH?
6. What remains HOLD?
7. Is Codex structure work needed?
8. What is the suggested placement?

---

## 4. Read Scope

Required:
  - the user-provided input material
  - this work_order

Optional only if needed:
  - app/work/space-skill-sandbox/outputs/big_frame_candidate_map_20260513_candidate_v0.md
  - app/work/space-skill-sandbox/outputs/manual_cycle_relay_operating_contract_20260513_candidate_v0.md
  - app/work/space-skill-sandbox/outputs/manual_cycle_relay_fast_path_contract_20260513_candidate_v0.md
  - app/work/space-skill-sandbox/outputs/operating_term_disambiguation_table_20260513_candidate_v0.md

Do not read by default:
  - entire repo
  - all runs
  - raw logs
  - broad Obsidian vault
  - linked notes
  - current-position files
  - output_manifest
  - implementation files

---

## 5. Structural Gap Rule

If Gemini finds a structure gap:

Do not solve it directly.

Return a Codex request entry with:

- request_id
- structural_gap
- requested_codex_work
- expected_output
- priority
- forbidden_actions

---

## 6. Hard Boundaries

Do not:

- process anything before input is provided
- read broad repo context
- create automation
- create scripts
- update current-position
- update output_manifest
- promote baseline / workflow / registry / schema
- rewrite the Big Frame Candidate Map
- treat Gemini observation as approval

---

## 7. Return Format When Executed Later

Return exactly:

Verdict:
  GEMINI_BOUNDED_INPUT_INTAKE_RETURNED_WITH_WATCH / STRUCTURAL_GAP_FOUND / WATCH_ONLY / HOLD

Cycle:
  cycle_003_bounded_input_intake_thread_001

Input:
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

Suggested placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD

Suggested next owner:
  Codex / ChatGPT + User / Gemini / HOLD

Do Not Promote:
  - input observation != truth
  - Gemini return != approval
  - placement != baseline
  - next pull != automatic next task

Hard boundaries confirmation:
  - no automation
  - no scripts
  - no broad repo read
  - no current-position update
  - no output_manifest update
  - no baseline / workflow / registry / schema promotion
