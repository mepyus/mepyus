# operating ui donor and fresh build map v1

## donor 활용

### board shell donor

- source: [Officeout.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officeout.jsx)
- 활용 대상:
  - top toolbar composition
  - left helper lane
  - center card board
  - right selected detail lane
  - bottom log strip
- 활용 방식:
  - 구조 donor
  - 의미와 데이터 shape는 재사용하지 않음

### modal donor

- source: [Fhandler.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Fhandler.jsx)
- source: [TankControl.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/TankControl.jsx)
- 활용 대상:
  - overlay
  - modal header / body / close
  - selected item focus transition
- 활용 방식:
  - interaction and modal shell donor
  - tank/block/search semantics는 버림

### feedback/input donor

- source: [Officein.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officein.jsx)
- 활용 대상:
  - selected record driven form
  - feedback and note area
  - action button grouping
- 활용 방식:
  - section donor
  - field schema는 새로 정의

## 신규 작성

### 반드시 새로 짜는 부분

- `OperatingBoardShell`
  - 이유: current engine payload와 WashTank page identity가 다름

- `AssetStateBoard`
  - 이유: card semantics가 `tank/job`가 아니라 `asset/latest/diff/attention/memory`여야 함

- `AssetStateCard`
  - 이유: canonical badge 중심으로 새로 설계해야 함

- `DetailModal`
  - 이유: 목표 모달은 `created / updated / scope / dependencies / activity log / feedback / action button`을 담아야 하고 donor에 동일 shape가 없음

- `DerivedStateStrip`
  - 이유: current engine만의 latest/diff/attention/memory 표시가 필요

- `ProcessConsoleDataAdapter`
  - 이유: donor 서비스가 아니라 [builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/builder.py) payload를 UI-friendly shape로 바꿔야 함

## 단순 참고

- [index.css](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/index.css)
  - 참고 포인트:
    - high contrast panel separation
    - mono/technical tone
  - 참고 수준:
    - style language only

- [render.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/render.py)
  - 참고 포인트:
    - section ordering
    - fallback handling
  - 참고 수준:
    - information architecture only

## 버려야 할 부분

- `jms` 직접 호출
  - 이유: current engine core와 무관

- tank/job specific fallback helpers
  - 이유: generic asset UI에 오염 유발

- task queue naming and logistics semantics
  - 이유: wash tank 도메인 의미를 그대로 끌고 옴

- donor 내부 inline style monolith
  - 이유: baseline의 `Container / View / Styles / Service` 분리 원칙과 충돌

## 요약 판정

- donor 활용 범위:
  - layout rhythm
  - card/list interaction
  - modal shell
  - activity/feedback section arrangement

- fresh-build 범위:
  - current engine data adapter
  - canonical state card semantics
  - detail modal schema
  - process-console specific derived state surface

- 최종 방향:
  - **hybrid OK**
  - donor를 설계 reference로 쓰고, 핵심 구조는 current engine payload에 맞춰 새로 짜는 것이 가장 안전하다.
