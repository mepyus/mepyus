[[A]] [[OBJ:engine_operating_surface_component_spec_v1]] [[SEM:component_spec_for_process_console_operating_surface]]

# engine_operating_surface_component_spec_v1

## 1. screen purpose

- 이 화면의 목적은 아래 3개다.
  - 자산 하나가 **어떻게 읽혔는지**를 추적한다
  - 자산 하나가 **어디서 조기 고정되거나 막혔는지**를 드러낸다
  - 그 상태를 실패가 아니라 **비교 기억 / 상태 기억**으로 다시 붙잡는다

- 즉 이 화면은
  - 분석 결과 화면이 아니고
  - 최종 의미 지도 화면도 아니고
  - 운영자가 원문과 해석 흔적을 왕복하면서 재독해하는 **운용 콘솔**이다.

## 2. top-level layout

화면은 5영역으로 나눈다.

### A. top control bar

- 역할:
  - 현재 자산명
  - 현재 packet texture
  - 현재 maturation 상태
  - 비교모드 on/off
  - 필터와 정렬
  - traceability 상태 표시

- 표시 항목:
  - asset title
  - asset type
  - last processed run
  - packet texture badge
  - grounding badge
  - emergence badge
  - scaffold carryover risk badge
  - traceability status

- 해석:
  - 이 상단은 “무엇을 보고 있는지”보다
    **“지금 어떤 생육 상태의 자산을 보고 있는지”**를 먼저 보여줘야 한다.

### B. left asset rail

- 역할:
  - 자산 목록
  - 자산별 상태 요약
  - 클릭 시 중앙 process trace 전환

- 카드 최소 정보:
  - asset name
  - source type
  - packet texture
  - blocker count
  - traceability confirmed 여부
  - last notable state
  - question-inducing candidate 존재 여부
  - comparison memory reason
    - 예: `same compressed family`
    - 예: `same fallback dominance`
    - 예: `breathing contrast`

- 해석:
  - 이 영역은 단순 파일 탐색기가 아니다.
  - 운영자가 “무슨 파일을 열까”가 아니라
    **“어떤 질감과 어떤 막힘을 가진 자산을 들어갈까”**를 결정하는 진입면이다.

### C. center process trace body

- 역할:
  - 이 화면의 핵심
  - 원문에서 상태 기억까지의 흐름을 단계형으로 노출

- 권장 흐름:
  1. Source
  2. First-pass trace
  3. One-point-five packet
  4. Second-order rereading
  5. Maturation state

- 해석:
  - 그래프뷰가 아니라 **과정 추적면**이어야 한다.

### D. right state/interpretation panel

- 역할:
  - 현재 선택된 단계의 상세 메타데이터와 판독 이유 표시
  - weak/fallback/hold/residue를 설명 가능한 상태 언어로 제공

- 표시 항목:
  - current selected node type
  - summary
  - why this state
  - blockers
  - carryover signs
  - grounding notes
  - operator memo slot

- 해석:
  - 이 영역은 “모델 판단 설명”이 아니라
    **현재 상태를 운영 언어로 다시 붙잡는 면**이다.

### E. bottom comparative memory strip

- 역할:
  - 현재 자산과 유사한 packet texture / blocker 패턴 자산 비교
  - recent second-order 자산을 실패물이 아니라 comparative memory로 연결

- 예:
  - `knowledge_editing_youtube`
  - `gary_tan_brain`
  - `youtube_03_22`
  - `openai_02_11`

- 해석:
  - 이 영역이 있어야 최근 자산들이 “개별 실패 사례”가 아니라
    **비교 기억 자산 묶음**으로 작동한다.

## 3. core component definitions

## 3-1. `AssetRail`

### 목적

- 운영자가 자산을 고르는 진입 컴포넌트

### 입력

- asset_id
- asset_name
- source_type
- packet_texture
- blocker_summary
- traceability_confirmed
- emergence_state
- carryover_risk
- comparison_memory_reason

### 출력/행동

- asset select
- filter by texture
- filter by blocker
- sort by recent / unstable / compressed / breathing

### 표시 규칙

- 카드 첫 줄은 asset name
- 둘째 줄은 texture + emergence
- 셋째 줄은 blocker/traceability 요약
- 넷째 줄은 comparison memory reason

### 해석

- 파일 목록이 아니라
  **생육 상태를 읽고 자산에 들어가는 게이트**다.

## 3-2. `SourceViewer`

### 목적

- 원문과 다시 접속하는 면

### 입력

- source text
- source segment boundaries
- source metadata
- linked first-pass fragments

### 출력/행동

- 원문 스크롤
- 특정 1차 trace와 하이라이트 연동
- 특정 packet과 source ref 연동

### 표시 규칙

- 원문은 항상 접속 가능해야 함
- 어떤 판독도 여기로 돌아올 수 있어야 함
- source-ref 없는 해석은 명확히 약표기

### 해석

- reference panel이 아니라
  ontology truth로 굳는 걸 막는 **현실 접점**이다.

## 3-3. `FirstPassTracePanel`

### 목적

- 1차 흔적 표시

### 입력

- scene
- flow
- anchor
- label
- residue draft
- segmentation result
- trace notes

### 출력/행동

- trace node 클릭
- source highlight 동기화
- packet formation candidate 연결

### 표시 규칙

- “판정”이 아니라 “초기 흔적” 톤으로 노출
- 확정값처럼 보이는 UI 금지
- `sensor trace` / `seed trace` 라벨 사용 권장

### 해석

- 1차는 truth layer가 아니라
  **씨앗 흔적 보존층**이다.

## 3-4. `MemoryPacketBridgePanel`

### 목적

- 1.5차 memory packet 표시

### 입력

- packet_id
- packet windows
- packet grouping logic
- packet texture
- packet compression notes
- bridge confidence
- linked second-order consumers
- packet_formation_why
- packet_comparison_reason

### 출력/행동

- packet expand/collapse
- packet-to-source jump
- packet-to-second-order jump
- packet texture compare

### 표시 규칙

- 단순 generated sidecar처럼 보이면 안 됨
- `bridge` 정체성이 드러나야 함
- packet texture는 상단 고정 표기
- `why this packet formed` 줄이 반드시 있어야 함
  - 예: `single-window compressed packet`
  - 예: `moderately open multi-window packet`
  - 예: `dense but closure-heavy packet`

### 해석

- 이 패널은 현재 엔진의 중심 장기다.
- 1차 흔적을 바로 삼켜지지 않게 중간에서 묶는 **memory packet bridge**를 표면화한다.

## 3-5. `SecondOrderRereadingPanel`

### 목적

- 2차 재독해 결과와 조기 고정 양상 표시

### 입력

- rereading summary
- question opening signs
- relation movement signs
- residue priority signs
- role probe
- carryover evidence
- grounding notes
- blocker mapping
- new_opening_signs
- carryover_signs

### 출력/행동

- second-order step review
- blocker reveal
- compare with packet texture
- operator note attach

### 표시 규칙

- 승격 심사표처럼 보이면 안 됨
- pass/fail 큰 배지 금지
- 대신 `open / partial / weak / fallback / blocked` 같은 상태어 사용
- `new opening vs carryover`를 분리해 보여줘야 함

### 해석

- 2차는 상위 판정기가 아니다.
- 현재는 **열림/조기 고정을 드러내는 재독해층**으로 봐야 한다.

## 3-6. `MaturationStatePanel`

### 목적

- hold/residue/weak/fallback/blocker 상태를 기억 자산으로 표면화

### 입력

- hold state
- residue state
- weak markers
- fallback markers
- blocker set
- state history
- time axis

### 출력/행동

- state history view
- blocker-to-evidence jump
- operator memo
- future revisit mark

### 표시 규칙

- red error 중심 UI 금지
- weak/fallback을 폐기물처럼 보이지 않게 설계
- 상태 기억이라는 의미가 드러나야 함
- 시간축이 있어야 함
  - 이전보다 더 열렸는지
  - 그대로인지
  - 더 조기 고정됐는지

### 해석

- 이 패널은 “실패 경고판”이 아니라
  **상태 기억 저장면**이다.

## 3-7. `ComparativeMemoryStrip`

### 목적

- 유사 texture / 유사 blocker / 유사 carryover 자산 빠른 비교

### 입력

- related asset ids
- similarity reason
- packet texture similarity
- blocker overlap
- emergence contrast

### 출력/행동

- compare open
- side-by-side mode
- jump to similar failure surface
- jump to breathing variant

### 표시 규칙

- “추천 자산”이 아니라 “비교 이유”를 먼저 보여야 함
- 예:
  - `same carryover risk`
  - `same fallback dominance`
  - `same compressed family`
  - `breathing contrast`

### 해석

- 이 컴포넌트가 있어야 엔진은 개별 결과판이 아니라
  **비교 기억 기반 숙성 공간**이 된다.

## 4. badge system

- badge / filter / sort / compare entry의 canonical source field는
  [engine_state_schema_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/engine_state_schema_v1.md)
  와
  [engine_state_schema_v1.json](/Users/sungsookim/universe/vectorfl_replica/app/core/schemas/engine_state_schema_v1.json)
  을 따른다.

### A. Packet Texture Badge

- 값 예시:
  - `moderately_open`
  - `structured_open_low_emergence`
  - `overcompressed_closure_heavy`
  - `overcompressed_breathing`

- 역할:
  - 1.5차 packet 질감 표시
  - 2차 문제를 2차만의 문제로 오해하지 않게 함

### B. Grounding Badge

- 값 예시:
  - `direct_grounded`
  - `partially_grounded`
  - `fallback_grounded`
  - `empty_ref_risk`

### C. Emergence Badge

- 값 예시:
  - `question_opening_present`
  - `minimal_emergence`
  - `low_emergence`
  - `no_emergence`

### D. Carryover Risk Badge

- 값 예시:
  - `low`
  - `medium`
  - `high`
  - `prepared_scaffold_carryover`

### E. Maturation State Badge

- 값 예시:
  - `hold`
  - `residue`
  - `weak`
  - `fallback`
  - `blocked`
  - `breathing`

## 5. interaction rules

### rule 1

- 모든 2차 판독은 원문으로 되돌아갈 수 있어야 한다.

### rule 2

- 모든 weak/fallback은 근거 링크를 가져야 한다.

### rule 3

- packet texture는 숨기면 안 된다.

### rule 4

- 비교모드는 자산 전체보다 “유사 양상” 중심으로 여는 게 맞다.

### rule 5

- 그래프뷰는 기본 landing이 아니라 secondary action이어야 한다.

## 6. operator flow

1. 좌측 자산 레일에서 자산 선택
2. 상단에서 packet texture / emergence / blocker 상태 먼저 확인
3. 중앙 process trace에서 1차 -> 1.5차 -> 2차 흐름 확인
4. 우측 패널에서 weak/fallback/blocker 이유 확인
5. 필요 시 원문으로 되돌아가 source 근거 확인
6. 하단 비교 기억 스트립으로 유사 자산과 비교
7. operator memo 또는 revisit mark 남김

## 7. MVP priority

### 1순위

- `AssetRail`
- `SourceViewer`
- `FirstPassTracePanel`
- `MemoryPacketBridgePanel`
- `SecondOrderRereadingPanel`
- `MaturationStatePanel`

### 2순위

- `ComparativeMemoryStrip`

### 3순위

- 그래프뷰 / 지형뷰 / 분포 시각화

## 8. key prohibitions

- 1차는 정답 판정기로 읽히면 안 된다
- 1.5차는 sidecar로 읽히면 안 된다
- 2차는 승격 심사표로 읽히면 안 된다
- weak/fallback은 실패 폐기물로 읽히면 안 된다
- 그래프뷰는 본체로 읽히면 안 된다

## 9. one-line lock

> 운용화면은 자산의 결과를 보여주는 화면이 아니라, 자산이 어떤 packet 질감으로 묶였고 어떤 재독해를 거쳐 어디서 열리거나 조기 고정되었는지를 운영자가 추적하고 비교 기억으로 다시 붙잡는 process console이어야 한다.

## 10. reinforcement points

- 이번 스펙에서 추가로 명시적으로 강화된 포인트는 아래 4개다.
  - `AssetRail`은 `comparison memory reason`을 카드에 직접 드러내야 한다.
  - `MemoryPacketBridgePanel`은 `packet formation why`를 반드시 보여줘야 한다.
  - `SecondOrderRereadingPanel`은 `new opening`과 `carryover`를 분리해 보여줘야 한다.
  - `MaturationStatePanel`은 `state history / time axis`를 통해 상태 변화 추이를 보여줘야 한다.

- 이 4개는 단순 UI 편의가 아니라,
  현재 엔진이 결과 전시판으로 미끄러지지 않고 process console로 읽히게 만드는 최소 보강점이다.
