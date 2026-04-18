# VectorFL Inputs Intake Adapter Contract v0

이 문서는 `qmd-ref intake layer`와 `VectorFL core` 사이의 입력 결과를  
`paperclip-ref host shell`에서 읽게 하는 최소 adapter 계약을 잠근다.  
입력기 전체 구현이나 full intake UI를 고정하는 문서가 아니라,  
operator가 source / context / block / status를 읽을 수 있게 하는 최소 view model만 잠근다.

## 1. 목적

현재 단계에서 Inputs / Intake adapter가 해야 할 일은 아래다.

- 어떤 입력이 들어왔는지 보여준다
- source와 context를 보이게 한다
- 어떻게 split/block이 형성됐는지 보이게 한다
- weak/fallback/status를 숨기지 않는다
- core와 linked case가 있으면 연결만 보여준다

즉 intake 결과를 readable하게 만들되,
lane progression이나 governance canonical decision을 대신하지 않는다.

## 2. Adapter Position

`qmd-ref intake layer`
-> `Source Registry Entry / Intake Block / Intake Packet / Intake Status Record`
-> `Inputs Intake Adapter`
-> `Input Detail View Model`
-> `paperclip-ref host shell`

필요하면 linked case를 위해 아래 core object를 약하게 참조할 수 있다.

- `Case Record`
- `Lane State Record`

## 3. Source Objects

adapter가 읽는 최소 source object는 아래다.

- `Source Registry Entry`
- `Intake Packet`
- `Intake Status Record`
- `Intake Block`
- optional linked `Case Record`

## 4. Input Detail View Model Minimum Sections

### 4-1. Source Header

- 목적: 지금 보고 있는 입력 원천이 무엇인지 보여준다
- minimum fields:
  - `source_id`
  - `source_kind`
  - `source_locator`
  - `source_family`
  - `source_subgroup`
  - `registry_status`

### 4-2. Context Layer Summary

- 목적: 어떤 문맥이 붙었는지 보여준다
- minimum fields:
  - `matched_context_layers`
  - `default_context_ref`
  - `intake_classification`
  - `next_lane_hint`

### 4-3. Intake Block Summary

- 목적: 입력이 어떤 block들로 준비되었는지 보여준다
- minimum fields:
  - `intake_block_refs`
  - `block_kind`
  - `split_reason`
  - `protected_region_flag`
  - `overlap_group_ref`

### 4-4. Weakness / Fallback Card

- 목적: intake의 약함을 숨기지 않고 보여준다
- minimum fields:
  - `weakness_note`
  - `fallback_used`
  - `weak_intake`
  - `re_read_needed`
  - `status_level`

### 4-5. Intake Status Summary

- 목적: intake 진행 상태와 readiness를 보여준다
- minimum fields:
  - `source_registered`
  - `context_attached`
  - `classification_done`
  - `split_generated`
  - `downstream_ready`
  - `readiness_level`
  - `updated_at`

### 4-6. Linked Case Preview

- 목적: 이 intake가 이미 case와 연결되어 있다면 그 연결만 보여준다
- minimum fields:
  - `linked_case_ref`
  - `case_status`
  - `current_lane_ref`

## 5. Display-Only Rules

Inputs / Intake adapter와 shell은 아래를 할 수 있다.

- source와 context를 readable summary로 보여준다
- split block을 browseable summary로 보여준다
- weakness/fallback를 caution card나 status note로 보여준다
- linked case와 current lane을 preview로 보여준다

하지만 아래는 하지 않는다.

- source classification rewrite
- next lane canonical 확정
- governance release 판단
- intake weakness 은폐

즉 Inputs / Intake adapter는 `intake visibility adapter`이지
`core routing authority`가 아니다.

## 6. Weakness Visibility Rules

Inputs / Intake 화면은 아래를 반드시 visible하게 유지한다.

- `weakness_note`
- `fallback_used`
- `weak_intake`
- `re_read_needed`
- `downstream_ready`

이 정보는 숨기면 안 되며,
current-reading으로 넘어가기 전단에서 operator가 가장 먼저 확인할 수 있어야 한다.

## 7. Linked Case Boundary Rules

linked case 정보는 보여줄 수 있지만,
입력 화면이 case를 canonical하게 소유하지는 않는다.

즉:

- intake 화면은 `linked_case_ref`를 보여줄 수 있다
- case의 canonical status와 lane meaning은 core 소유다
- intake 화면은 linked case를 진입점처럼 다룰 수는 있어도, case object를 대체하지 않는다

## 8. Adapter Output Minimum Shape

Inputs / Intake adapter가 shell에 넘기는 최소 output shape는 아래처럼 읽는다.

- `source_header`
- `context_layer_summary`
- `intake_block_summary`
- `weakness_fallback_card`
- `intake_status_summary`
- `linked_case_preview`

이 output은 canonical object가 아니라 `Input Detail View Model`이다.

## 9. What Is Not Locked Yet

현재 문서에서 아직 잠그지 않는 것은 아래다.

- full input browser layout
- block drill-down interaction
- block-to-case linking workflow
- source registration editing flow
- search/filter UX
- multi-source compare UX

즉 지금은 `입력 결과를 readable하게 보여주는 최소 adapter 계약`만 잠근다.

## 10. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`Inputs / Intake adapter는 Source/Context/Block/Status를 operator-facing detail view model로 적응시키되, weak/fallback와 linked-case 관계를 숨기지 않고 next-lane과 case 의미의 canonical 판정권은 core에 남긴다.`
