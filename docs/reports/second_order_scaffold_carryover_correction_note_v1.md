[[A]] [[OBJ:second_order_scaffold_carryover_correction_note_v1]] [[SEM:note_on_scaffold_carryover_as_premature_closure_points_in_second_order_rereading]]

# second_order_scaffold_carryover_correction_note_v1

## 1. purpose

- 이번 문서의 목적은 2차 일부 코드에 남아 있는 scaffold carryover를 “틀림”으로 적는 것이 아니라, 열린 재독해를 조기 고정시키는 지점으로 분리 기록하는 것이다.

## 2. observed premature-closure points

### A. `run_multi_pass_interpretation_training.py`
- hardcoded context unit:
  - `agent_interface_transition_unit`
  - `future_of_work_supervisor_unit`
  - `model_eval_shift_unit`
- 의미:
  - 재독해 태도 자체는 살아 있다.
  - 하지만 context unit 발생이 새 재료에서 생기기보다 기존 scaffold 이름을 따라가게 될 위험이 있다.

### B. `run_paragraph_role_interpretation_training.py`
- fixed targets:
  - `Bundle-Unbundle 프레임워크`
  - `GTC 키노트와 ‘일의 미래’`
  - `RLVR과 CUA`
- 의미:
  - role-like reading 가능성은 probe 한다.
  - 그러나 paragraph role이 새 자산에서 발견되기보다 기존 target을 재투사하는 경향을 만든다.

### C. `run_dialogue_asset_purpose_synthesis.py`
- asset wording 고정
- `input_asset_type = "high_density_dialogue"` 고정
- youtube-style phrasing carryover
- 의미:
  - purpose synthesis가 새 층위를 여는 것보다, 이미 익숙한 dialogue interpretation wording으로 수렴할 위험이 있다.

## 3. correct reading of these traces

- 이것들은 기관 승격 실패의 증거가 아니다.
- 이것들은 현재 2차가 어디서 새 층위를 발견하기보다 기존 틀로 재기술하려는지 보여 주는 조기 고정점이다.
- 따라서 교정의 핵심은 더 많은 naming이나 더 강한 heuristic가 아니라, prepared scaffold를 줄여 열린 재독해 여지를 회복하는 데 있다.

## 4. why this matters

- 사용자가 원하는 것은 층위를 미리 정해 놓는 것이 아니라, 자료 안에서 새로운 해석 층위가 열리는 것이다.
- scaffold carryover는 바로 그 열림을 가장 먼저 질식시키는 부분이다.

## 5. one-line summary

> 현재 2차 일부 코드에 남아 있는 AI dialogue scaffold carryover는 단순 구현 실수가 아니라, 열린 재독해를 기존 unit/role/wording으로 조기 고정시키는 지점으로 읽어야 한다.
