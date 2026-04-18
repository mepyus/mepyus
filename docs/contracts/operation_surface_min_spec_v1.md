# operation_surface_min_spec_v1

## 1. 목적
이 문서는 전체 공간 뷰어 대신 먼저 필요한 read-only operation surface 의 최소 스펙을 잠근다.

## 2. surface 성격
- read-only
- latest pointer surface
- operation trace summary
- search/observe/render 의 출발점

## 3. 최소 섹션
- current question / directive
- related inputs
- execution steps
- expected scenario
- generated outputs
- failure / hold / retry status
- related reference pointers
- related observation pointers
- next candidate actions

## 4. 필수 표시 규칙
- source doc ref 를 숨기지 않는다.
- generated output path 를 직접 가리킨다.
- latest state 와 historical trace 를 혼동하지 않는다.
- overwrite surface 라면 per-run pointer 도 함께 제공한다.

## 5. 금지
- raw input 수정 기능
- interpretation overwrite 기능
- observation result 를 원본 사실처럼 고정하는 기능

## 6. 현재 구현과의 연결
- current seed surface:
  - [runtime/views/operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)
- future expansion:
  - per-run operation board
  - filtered operation view by namespace / company / scenario

## 7. 잠금 문장
operation surface 는 공간 본체가 아니라, 지금 무엇이 들어와서 어떻게 흘렀는지 잃어버리지 않게 해주는 read-only 추적면이다.
