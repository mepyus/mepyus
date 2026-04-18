# operating ui resource utilization review

## 1. verdict

- hybrid OK

## 2. target reading

- 우리가 만들려는 화면은 단순 업무 페이지가 아니라, `latest / diff / attention / memory` 같은 운용 상태를 **카드/패널/모달 단위로 읽고 다음 행동을 취하는 보드형 operating surface**다.
- 따라서 핵심 요구는 예쁜 보드가 아니라, 아래 5가지를 한 표면에 안정적으로 담는 것이다.
  - board or card-oriented main selection surface
  - selected object detail
  - activity log
  - feedback input and action buttons
  - derived operating state display
- 이 목표는 현재 엔진의 [engine_operating_surface_component_spec_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/engine_operating_surface_component_spec_v1.md), [process_console_state_wiring_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/process_console_state_wiring_v1.md), [process_console_history_drilldown_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/process_console_history_drilldown_v1.md), [state_change_diff_surface_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/state_change_diff_surface_v1.md)와 직접 맞물린다.

## 3. usable resources

### strongest donors

- [Officeout.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officeout.jsx)
  - 활용 수준: 의미를 바꿔 재사용 가능
  - 이유: header, sidebar, central card grid, right detail panel, footer log의 운용면 뼈대가 이미 있다.

- [TankControl.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/TankControl.jsx)
  - 활용 수준: 구조만 참고 가능
  - 이유: overlay + modal + action slot 구조는 좋지만 파일 자체 완성도와 독립성이 낮다.

- [Fhandler.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Fhandler.jsx)
  - 활용 수준: 의미를 바꿔 재사용 가능
  - 이유: bright board layout, left task rail, right spatial panel, modal overlay 패턴이 강하다.

### secondary donors

- [Officein.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officein.jsx)
  - 활용 수준: 구조만 참고 가능
  - 이유: 상세 폼, 기록 허브, feedback-like 입력 패턴은 참고할 수 있지만 board shell donor로는 약하다.

- [OfficePageContainer.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/OfficePageContainer.jsx)
  - 활용 수준: donor 가치 낮음
  - 이유: container/service 분리 감각은 보여주지만 실제로는 `Office.jsx`에 묶여 있고 generic adapter로 보기 어렵다.

### current engine assets to keep

- [builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/builder.py)
  - 활용 수준: 그대로 재사용 가능
  - 이유: latest/history/diff/attention/memory를 하나의 selected asset payload로 합치는 container 역할이 이미 있다.

- [render.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/render.py)
  - 활용 수준: 구조만 참고 가능
  - 이유: 현재는 plain HTML 렌더지만 section arrangement, payload reading, safe fallback은 유지 가치가 있다.

- [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)
  - 활용 수준: 그대로 재사용 가능
  - 이유: process console API/read path를 이미 제공한다.

## 4. donor candidates

### board shell donor

- [Officeout.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officeout.jsx)
  - donor 이유:
    - top navigation + search + refresh
    - left protocol/info lane
    - center card/list workspace
    - right selected detail/action lane
    - bottom/recent log surface
  - donor 한계:
    - modal 없음
    - wash-tank job transition semantics 강함

### modal and action-flow donor

- [TankControl.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/TankControl.jsx)
  - donor 이유:
    - common search + popup slot 패턴
  - donor 한계:
    - 코드가 얇고 style context가 외부 전제에 의존

- [Fhandler.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Fhandler.jsx)
  - donor 이유:
    - modal overlay / header / content / close action
    - left rail + right board 조합
  - donor 한계:
    - site/tank/block meaning이 강함

### feedback/detail form donor

- [Officein.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officein.jsx)
  - donor 이유:
    - selected object editing form
    - record save / feedback note / log message pattern
  - donor 한계:
    - board shell이 아니라 archive-record hub에 가깝다

### data/container donor

- [builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/builder.py)
  - donor 이유:
    - current engine payload를 한 번에 읽어오는 canonical container
  - donor 한계:
    - UI component abstraction이 아니라 Python payload aggregator다

## 5. blockers

- domain naming 결합
  - `tank`, `job`, `DONE`, `OUTBOUND`, `WASH`, `BLOCK`, `OFFICE_REQUESTS` 같은 의미가 donor 전반에 강하게 박혀 있다.

- hardcoded field shape
  - `job_type`, `tank_id`, `completed_at`, `results`, `tanks.tank_number` 전제가 많다.

- service coupling
  - [jms.js](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/services/jms.js) 는 supabase + tank_jobs schema에 강하게 묶여 있어 현재 엔진 payload에는 직접 연결 불가다.

- inline style monolith
  - donor UI 대부분이 파일 내부 `styles` 객체 또는 inline style 중심이다.
  - View / Styles 분리 원칙으로 보면 공용 승격 전에 추출 비용이 든다.

- routing and page identity coupling
  - donor 파일들이 `onBack`, 특정 route, 특정 작업 큐 identity를 전제로 한다.

- modal/data abstraction 부족
  - 목표 화면의 핵심은 “선택 카드 -> 상세 모달 -> feedback / actions / activity”인데, donor는 각각 일부만 가지고 있다.
  - 한 파일이 완성 donor가 아니라 donor 조합이 필요하다.

## 6. fresh-build justification

- 새로 만드는 편이 나은 이유는, 현재 엔진 운용화면이 이미 [builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/builder.py) 기준의 `selected asset payload` 구조를 갖고 있기 때문이다.
- donor를 억지로 살리면 WashTank 데이터 shape와 naming을 계속 벗겨내야 하고, 그 과정에서 baseline을 오염시킬 가능성이 있다.
- 특히 canonical latest/history/diff/attention/memory를 카드/모달/feedback 구조로 배열하는 목표는 WashTank 도메인 로직보다 **엔진 payload에 맞는 UI composition**이 더 중요하다.

### 그래도 반드시 가져가야 할 것

- [Officeout.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officeout.jsx) 에서:
  - board shell 감각
  - left/center/right panel composition
  - card selection and action rhythm
  - footer activity tone

- [Fhandler.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Fhandler.jsx) 에서:
  - modal overlay 존재감
  - 작업 대상 선택 후 상세 행동으로 진입하는 흐름

- [Officein.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officein.jsx) 에서:
  - feedback/input section composition
  - selection-driven form binding 감각

- [render.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/render.py) 에서:
  - current process console section ordering
  - latest + history + diff + attention + memory 배치 논리

## 7. minimal path

- 가장 현실적인 1차 경로는 **donor 일부 + 신규 작성**이다.

### recommended baseline

1. current engine data path는 유지
   - [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)
   - [builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/builder.py)

2. 새 UI는 fresh-build
   - 이유: current payload에 맞는 `BoardShell`, `AssetBoard`, `DetailModal`, `ActivityPanel`, `FeedbackComposer`를 새로 짜는 쪽이 더 안전하다.

3. donor는 structure reference로만 사용
   - board shell: [Officeout.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officeout.jsx)
   - modal shell: [Fhandler.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Fhandler.jsx), [TankControl.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/TankControl.jsx)
   - feedback section: [Officein.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officein.jsx)

4. 1차 범위는 여기까지 제한
   - board main surface
   - selected detail modal
   - activity log read
   - feedback input shell
   - latest/diff/attention/memory read badges
   - 쓰기 동작은 mock or no-op 수준으로 제한

## 8. recommended next step

- 다음 1스텝은 구현이 아니라 **운용화면 component decomposition draft**를 잠그는 것이다.
- 즉 아래 컴포넌트 트리만 먼저 문서로 고정하면 된다.
  - `OperatingBoardShell`
  - `AssetStateBoard`
  - `AssetStateCard`
  - `SelectionSummaryPanel`
  - `DetailModal`
  - `ActivityPanel`
  - `FeedbackComposer`
  - `DerivedStateStrip`
- 그 다음에야 donor reference를 보면서 실제 1차 UI build 범위를 안전하게 잘라낼 수 있다.
