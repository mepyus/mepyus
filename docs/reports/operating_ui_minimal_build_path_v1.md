# operating ui minimal build path v1

## 목표

- 현재 repo를 크게 흔들지 않으면서, `엔진 운용화면/보드형 운영 UI`의 1차 베이스를 만들 수 있는 최소 경로를 정한다.

## 1차 범위 제한

- 이번 1차 베이스는 아래까지만 포함한다.
  - asset board main screen
  - selected asset detail modal
  - activity log section
  - feedback input shell
  - latest / diff / attention / memory read badges

- 이번 1차에서 제외한다.
  - graph/terrain integration
  - canonical write actions
  - real feedback persistence
  - complex editing workflow
  - donor 리팩터링

## 가장 현실적인 경로

### step 1. current process console payload 유지

- data source는 그대로 유지한다.
  - [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/viewer_server.py)
  - [builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/process_console_view/builder.py)

- 이유:
  - 이미 `latest / history / diff / attention / memory`가 한 payload로 묶여 있다.
  - UI donor 검토와 별개로 data contract는 충분히 안정적이다.

### step 2. UI adapter만 얇게 추가

- 새로 필요한 것은 service replacement가 아니라 **UI adapter**다.

### recommended adapter

- `OperatingUiPayloadAdapter`
  - selected asset payload -> board card view model
  - selected asset payload -> detail modal view model
  - history summary -> activity section view model

- 이유:
  - donor UI는 현재 payload를 그대로 못 읽는다.
  - adapter 하나를 두면 UI와 runtime payload를 느슨하게 묶을 수 있다.

### step 3. component start order

1. `OperatingBoardShell`
2. `AssetStateBoard`
3. `AssetStateCard`
4. `SelectionSummaryPanel`
5. `DetailModal`
6. `ActivityPanel`
7. `FeedbackComposer`
8. `DerivedStateStrip`

## donor 연결 방식

### shell donor

- [Officeout.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officeout.jsx)
  - left/center/right composition
  - toolbar rhythm
  - footer log positioning

### modal donor

- [Fhandler.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Fhandler.jsx)
- [TankControl.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/TankControl.jsx)
  - overlay + modal skeleton

### feedback donor

- [Officein.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officein.jsx)
  - feedback / note / action grouping

## 1차 위험 최소화 기준

- donor 파일은 직접 수정하지 않는다.
- WashTank service/data shape는 끌어오지 않는다.
- current engine payload를 건드리지 않는다.
- detail modal은 read-first로 시작한다.
- feedback input은 1차에선 local shell 또는 no-op action으로 제한한다.

## 왜 이 경로가 덜 해로운가

- core와 derived layer를 건드리지 않는다.
- surface layer만 확장한다.
- donor를 억지 재사용하지 않고, 필요한 interaction grammar만 취한다.
- current process console을 대체하지 않고, 같은 데이터를 더 운영 친화적인 표면으로 재배열하는 수준에서 출발할 수 있다.

## 바로 다음 1스텝

- 다음 턴에서 해야 할 가장 현실적인 작업은 **React component tree + props spec** 문서를 만드는 것이다.

### minimum spec target

- `OperatingBoardShell`
- `AssetStateBoard`
- `AssetStateCard`
- `DetailModal`
- `ActivityPanel`
- `FeedbackComposer`
- `OperatingUiPayloadAdapter`

- 이 단계까지 잠기면, donor reference를 어떻게 사용할지와 fresh-build 경계가 구현 전에 이미 안정된다.
