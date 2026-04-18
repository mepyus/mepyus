# VectorFL Current Reading Mock Fixture Contract v0

이 문서는 `VectorFL Paper`의 첫 shell 프로토타입을  
`Current Reading` 중심 mock/view-model 방식으로 시작할 때 필요한 최소 fixture 계약을 잠근다.  
실제 구현 파일을 만드는 문서가 아니라, 첫 mock shell이 어떤 입력 묶음을 받아야 하는지 고정하는 문서다.

## 1. 목적

현재 단계에서 첫 구현은 live integration보다
`core-fed mock/view-model shell`로 시작하는 것이 맞다.

따라서 먼저 필요한 것은 아래다.

- 어떤 canonical object를 fixture로 준비할 것인가
- 어떤 수준까지 mock이면 충분한가
- 무엇은 첫 mock에 넣고 무엇은 뒤로 미룰 것인가

## 2. First Mock Goal

첫 Current Reading mock shell의 목표는 아래로 잠근다.

- `case 하나`를 중심으로 읽을 수 있다
- `current reading body`가 보인다
- `lane 상태`가 보인다
- `governance 상태`가 보인다
- `trace/residue preview`가 보인다
- weakness/fallback 또는 caution이 있으면 숨기지 않는다

즉 첫 mock은 예쁜 UI보다
`current-reading contract가 실제로 읽히는가`를 확인하는 용도다.

## 3. Fixture Input Set

첫 mock shell은 아래 fixture 묶음을 최소 입력으로 받는다.

### 3-1. Case Fixture

- source object:
  - `Case Record`
- minimum fields:
  - `case_id`
  - `case_kind`
  - `case_status`
  - `linked_program_refs`
  - `current_lane_ref`
  - `current_surface_ref`
  - `governance_state_ref`
  - `trace_refs`
  - `updated_at`

### 3-2. Lane Fixture

- source object:
  - `Lane State Record`
- minimum fields:
  - `lane_state_id`
  - `lane_kind`
  - `lane_status`
  - `current_output_refs`
  - `next_hop_candidates`
  - `hold_flags`

### 3-3. Governance Fixture

- source object:
  - `Governance Record`
- minimum fields:
  - `governance_id`
  - `restriction_flags`
  - `hold_state`
  - `reason_summary`
  - `release_condition`
  - `next_check_trigger`

### 3-4. Surface Fixture

- source object:
  - `Surface Packet`
- minimum fields:
  - `surface_id`
  - `surface_kind`
  - `headline`
  - `summary_body_ref`
  - `supporting_unit_refs`
  - `governance_refs`
  - `trace_preview_refs`

### 3-5. Trace Preview Fixture

- source object:
  - `Trace / Memory Record`
- minimum fields:
  - `trace_id`
  - `trace_kind`
  - `summary`
  - `residue_note`
  - `reentry_hint`
  - `created_at`

### 3-6. Optional Intake Caution Fixture

- source object:
  - `Intake Packet` or `Intake Status Record`
- minimum fields:
  - `weakness_note`
  - `fallback_used`
  - `readiness_level`
  - `re_read_needed`

### note

이 마지막 fixture는 현재-reading이 intake weakness를 어느 정도까지 다시 보여줘야 하는지 확인하기 위한 선택 입력이다.

## 4. Adapter Output Expectation

mock shell은 fixture를 받아 아래 view-model shape로 적응되면 충분하다.

- `case_header`
- `current_reading_body`
- `lane_strip`
- `governance_card`
- `trace_strip`
- optional `caution_note`

즉 첫 mock은 이미 잠근
[vectorfl_current_reading_adapter_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/vectorfl_current_reading_adapter_contract_v0.md)
의 output shape를 실제 fixture로 시험하는 단계다.

## 5. Must-Be-Visible In Mock

첫 mock에서 반드시 숨기지 말아야 하는 것은 아래다.

- `hold_state`
- `restriction_flags`
- `release_condition`
- `latest_residue_note`
- `latest_reentry_hint`
- optional `weakness_note`
- optional `fallback_used`

즉 첫 mock은 긍정 요약 화면이 아니라,
`현재 읽기 + governance + caution`이 같이 보이는 화면이어야 한다.

## 6. What Can Be Mocked Freely

현재 단계에서 아래는 자유 mock으로 둬도 된다.

- exact body text
- supporting unit content detail
- linked program label text
- trace list length
- visual styling tokens
- iconography / color system

즉 semantic slot만 유지되면 된다.

## 7. What Not To Add Yet

첫 mock에는 아래를 넣지 않는다.

- editable controls
- action execution buttons
- full program connection control
- assignment / team management UI
- live refresh logic
- multi-case compare

즉 first mock은 shell capability 확인용이지 full product demo가 아니다.

## 8. Recommended First Fixture Scenario

첫 fixture는 아래 성격이 가장 적절하다.

- case 하나
- lane 하나
- mixed 또는 observer-only 성격의 governance 하나
- readable surface 하나
- residue/reentry가 보이는 trace 1~2개

즉 “문제가 없는 happy path”보다
VectorFL다운 governance/caution이 보이는 사례가 first mock에 더 적합하다.

## 9. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`Current Reading first mock은 Case/Lane/Governance/Surface/Trace fixture 한 묶음을 받아 current-reading body, lane strip, governance card, trace strip을 보여주고, hold·restriction·residue·reentry·weakness를 숨기지 않는 shell capability 확인용 mock으로 시작한다.`
