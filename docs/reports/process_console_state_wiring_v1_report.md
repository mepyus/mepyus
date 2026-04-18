[[A]] [[OBJ:process_console_state_wiring_v1_report]] [[SEM:report_for_process_console_canonical_state_wiring]]

# process_console_state_wiring_v1_report

## 1. purpose

- 이번 report의 목적은 canonical operating state layer를 process console read path에 연결한 범위와 한계를 기록하는 것이다.

## 2. connected components

- header badge:
  - latest state 6 badges 연결 완료
- asset rail:
  - latest index 기반 state-aware rail 연결 완료
- state panel:
  - canonical 8필드 중심 상세 연결 완료
- compare entry:
  - state overlap heuristic 기반 compare candidate 연결 완료
- latest state preview:
  - selected asset preview 연결 완료

## 3. filter / sort basis

- filter:
  - `packet_texture`
  - `grounding_status`
  - `emergence_status`
  - `carryover_risk`
  - `maturation_state`
  - `traceable_only`

- sort:
  - `updated_at`
  - `packet_texture`
  - `maturation_state`
  - `carryover_risk`
  - `emergence_status`

## 4. experimental guard

- `experimental_namespace`는 기본 화면에서 숨김 처리된다.
- top-level canonical section에는 naming-heavy field를 렌더하지 않는다.
- debug query가 없으면 experimental payload는 surface에 드러나지 않는다.

## 5. fallback behavior

- latest state가 없으면:
  - `state_unavailable`
  - `no_canonical_state_yet`
  - neutral empty panel

- malformed state는 current build에서 strict parser까지는 아니고 graceful absence 처리 중심이다.

## 6. compare heuristic

- 같은 `packet_texture`
- 같은 `carryover_risk`
- 겹치는 `comparison_memory_reason`
- 겹치는 `gate_blocker_summary`
- `same_compressed_family`
- `breathing_contrast`

## 7. representative check

- representative 4개 자산에서 확인된 것:
  - asset click -> latest load
  - header badge 6개 노출
  - asset rail 4개 자산 state-aware listing
  - state panel loaded
  - compare entry candidates 3개 이상 생성
  - experimental hidden by default

## 8. remaining limits

- 아직 source/first-pass/one-point-five/second-order trace body 전체를 canonical state와 하나의 interactive card flow로 묶진 않았다.
- current process console은 state-first read path가 먼저 연결된 상태다.
- history drill-down, malformed enum sanitization detail, debug inspection surface는 후속 보강 여지가 남아 있다.

## 9. one-line verdict

> 이번 wiring으로 process console은 이제 결과맵보다 먼저 canonical operating state를 읽는 표면이 되었고, representative asset 기준으로 header / rail / state panel / compare entry가 latest surface 위에서 실제로 동작한다.
