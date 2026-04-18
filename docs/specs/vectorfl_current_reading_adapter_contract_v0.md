# VectorFL Current Reading Adapter Contract v0

이 문서는 `VectorFL core canonical object`를  
`paperclip-ref host shell`의 current-reading console로 올릴 때 필요한 최소 adapter 계약을 잠근다.  
화면 설계 전체를 고정하는 문서가 아니라, core -> shell handoff에서 current-reading에 필요한 최소 view model만 고정한다.

## 1. 목적

현재 단계에서 먼저 필요한 것은

- current-reading surface를 shell에서 어떻게 읽을지
- 어떤 core object를 묶어 current-reading console에 올릴지
- 무엇은 shell이 표시만 하고 무엇은 core 판단으로 남겨둘지

를 최소 계약으로 잠그는 것이다.

## 2. Adapter Position

current-reading adapter는 아래 위치에 있다.

`VectorFL core`
-> `Surface Packet / Case Record / Lane State Record / Governance Record / Trace Preview`
-> `Current Reading Adapter`
-> `Current Reading View Model`
-> `paperclip-ref host shell console`

즉 adapter는 core canonical object를 지우거나 재판정하지 않고,
operator-facing current-reading surface로 적응시키는 층이다.

## 3. Source Objects

adapter가 읽는 최소 source object는 아래다.

- `Case Record`
- `Lane State Record`
- `Governance Record`
- `Surface Packet`
- `Trace / Memory Record` 일부 preview

## 4. Current Reading View Model Minimum Sections

현재 단계에서 current-reading console은 아래 section만 최소로 가진다.

### 4-1. Case Header

- 목적: 지금 어떤 case를 보고 있는지 보여준다
- minimum fields:
  - `case_id`
  - `case_kind`
  - `case_status`
  - `linked_program_refs`
  - `updated_at`

### 4-2. Current Reading Body

- 목적: core가 만든 현재 읽기 내용을 operator가 바로 읽을 수 있게 한다
- minimum fields:
  - `surface_id`
  - `surface_kind`
  - `headline`
  - `summary_body_ref`
  - `supporting_unit_refs`

### 4-3. Lane Strip

- 목적: 현재 lane과 다음 이동 후보를 보여준다
- minimum fields:
  - `current_lane_ref`
  - `lane_kind`
  - `lane_status`
  - `current_output_refs`
  - `next_hop_candidates`

### 4-4. Governance Card

- 목적: 지금 무엇이 멈춰 있고, 왜 멈췄는지, 무엇이 release 조건인지 보여준다
- minimum fields:
  - `restriction_flags`
  - `hold_state`
  - `reason_summary`
  - `release_condition`
  - `next_check_trigger`

### 4-5. Trace Strip

- 목적: 최근 trace와 residue/reentry 단서를 preview로 보여준다
- minimum fields:
  - `trace_preview_refs`
  - `latest_trace_kind`
  - `latest_residue_note`
  - `latest_reentry_hint`

## 5. Display-Only Rules

current-reading adapter와 shell은 아래를 할 수 있다.

- headline과 body를 읽기 좋게 배치
- governance를 badge/card 형태로 표시
- lane progression을 strip으로 표시
- trace/history preview를 묶어 표시

하지만 아래는 하지 않는다.

- line/state canonical rewrite
- governance release 결정
- next-hop canonical 확정
- trace summary의 사실 재서술

즉 current-reading adapter는 `display adaptation`이지 `interpretation replacement`가 아니다.

## 6. Governance Visibility Rules

current-reading console은 governance를 숨기지 않는다.

특히 아래는 visible해야 한다.

- `mixed hold`
- `observer-only`
- `promotion 금지`
- `release pending`
- `next check trigger`

이 정보는 current-reading의 부속이 아니라,
현재 읽기면과 같이 보여야 하는 보호 정보다.

## 7. Weakness / Fallback Visibility Rules

intake나 core 단계에서 올라온 약함은 current-reading에서도 완전히 사라지면 안 된다.

최소 visible 대상:

- `weakness note`
- `fallback used`
- `re-read needed`
- `residue-only` or equivalent readiness caution

표시 방식은 badge, note, caution strip 중 무엇이든 될 수 있으나,
adapter가 그 상태를 없애거나 침묵시키면 안 된다.

## 8. Adapter Output Minimum Shape

current-reading adapter가 shell에 넘기는 최소 output shape는 아래처럼 읽는다.

- `case_header`
- `current_reading_body`
- `lane_strip`
- `governance_card`
- `trace_strip`

이 output은 canonical object가 아니라 `Current Reading View Model`이다.

## 9. What Is Not Locked Yet

현재 문서에서 아직 잠그지 않는 것은 아래다.

- detailed page layout
- exact widget composition
- color / visual system
- multi-pane interaction rules
- edit / action workflow
- queue와의 동기화 UX 세부

즉 지금은 current-reading을 보여주기 위한 최소 adapter 계약만 잠근다.

## 10. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`Current Reading adapter는 Case/Lane/Governance/Surface/Trace의 core canonical object를 operator-facing console용 view model로 적응시키되, governance와 weakness를 숨기지 않고 canonical 판정권은 core에 남긴다.`
