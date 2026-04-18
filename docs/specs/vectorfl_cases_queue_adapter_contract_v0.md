# VectorFL Cases Queue Adapter Contract v0

이 문서는 `VectorFL core case/lane/governance/surface`를  
`paperclip-ref host shell`의 case queue로 올릴 때 필요한 최소 adapter 계약을 잠근다.  
queue 화면 전체를 설계하는 문서가 아니라, operator가 여러 case를 비교하고 진입할 수 있게 하는 최소 row/view model만 고정한다.

## 1. 목적

현재 단계에서 Cases / Queue adapter가 해야 할 일은 아래다.

- 여러 case를 queue 형태로 보여준다
- 각 case의 현재 lane과 hold 상태를 빠르게 읽게 한다
- current-reading 진입 전 최소 preview를 준다
- linked program과 최근 갱신 흔적을 보여준다

즉 case queue는 current-reading의 축약 진입면이지,
case 의미체계의 canonical source가 아니다.

## 2. Adapter Position

`VectorFL core`
-> `Case Record / Lane State Record / Governance Record / Surface Packet / Trace Preview`
-> `Cases Queue Adapter`
-> `Case Queue Item View Model`
-> `paperclip-ref host shell`

## 3. Source Objects

adapter가 읽는 최소 source object는 아래다.

- `Case Record`
- `Lane State Record`
- `Governance Record`
- `Surface Packet`
- `Trace / Memory Record` 일부 preview

## 4. Case Queue Item Minimum Fields

### 4-1. Identity

- 목적: queue에서 어떤 case인지 식별
- minimum fields:
  - `case_id`
  - `case_kind`
  - `case_status`

### 4-2. Lane Snapshot

- 목적: 지금 어느 lane에 있는지 빠르게 보여준다
- minimum fields:
  - `current_lane_ref`
  - `lane_kind`
  - `lane_status`

### 4-3. Governance Snapshot

- 목적: hold나 금지 상태를 queue 수준에서 바로 보이게 한다
- minimum fields:
  - `hold_state`
  - `restriction_flags`
  - `release_condition`

### 4-4. Current Surface Preview

- 목적: current-reading으로 들어가기 전 headline 수준 preview를 준다
- minimum fields:
  - `current_surface_ref`
  - `surface_kind`
  - `headline`

### 4-5. Linked Program Snapshot

- 목적: 외부 프로그램과 연결 상태를 queue에서 본다
- minimum fields:
  - `linked_program_refs`

### 4-6. Trace Freshness

- 목적: 최근 갱신과 trace 존재를 빠르게 보여준다
- minimum fields:
  - `trace_refs`
  - `updated_at`

## 5. Queue Display Rules

Cases / Queue adapter와 shell은 아래를 할 수 있다.

- current lane과 hold 상태를 badge/strip으로 표시
- headline 기반 preview를 row나 card에 실어 표시
- linked program 존재 여부를 표시
- recent update/freshness를 표시

하지만 아래는 하지 않는다.

- case 의미 재서술
- governance release 결정
- lane canonical rewrite
- trace 사실 재구성

즉 queue는 `entry surface`이지 `interpretation engine`이 아니다.

## 6. Governance Visibility Rules

queue는 governance를 얕게라도 숨기면 안 된다.

최소 visible 대상:

- `hold_state`
- `restriction_flags`
- `release_condition`

특히 아래는 queue 수준에서 바로 보이는 편이 맞다.

- `observer-only`
- `promotion 금지`
- `mixed hold`
- `release pending`

## 7. Current-Reading Link Rules

queue item은 current-reading으로 들어가는 진입점이지만,
current-reading body를 대체하지는 않는다.

즉:

- queue item은 `headline`과 최소 lane/governance snapshot만 보여준다
- 자세한 reading body와 supporting units는 current-reading adapter가 담당한다

## 8. Adapter Output Minimum Shape

Cases / Queue adapter가 shell에 넘기는 최소 output shape는 아래처럼 읽는다.

- `case_identity`
- `lane_snapshot`
- `governance_snapshot`
- `current_surface_preview`
- `linked_program_snapshot`
- `trace_freshness`

이 output은 canonical object가 아니라 `Case Queue Item View Model`이다.

## 9. What Is Not Locked Yet

현재 문서에서 아직 잠그지 않는 것은 아래다.

- sorting / grouping rules
- queue filters
- drag / assignment interactions
- multi-case compare UX
- lane board layout
- history expansion behavior

즉 지금은 `case를 읽고 current-reading으로 진입하는 최소 queue adapter 계약`만 잠근다.

## 10. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`Cases / Queue adapter는 Case/Lane/Governance/Surface의 core object를 operator-facing queue item으로 적응시키되, hold와 restriction을 숨기지 않고 case 의미와 governance 판정의 canonical source는 계속 core에 남긴다.`
