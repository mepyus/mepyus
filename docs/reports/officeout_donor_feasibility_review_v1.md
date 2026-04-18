# officeout donor feasibility review

## 1. verdict

- 조건부 OK

## 2. why

- `Officeout.jsx`는 **header + 좌측 규칙 패널 + 중앙 카드 보드 + 우측 상세/액션 패널 + 하단 로그**로 이루어진 명확한 운용화면 셸을 이미 가지고 있다.
- 선택 상태, 검색, 필터링, 액션 버튼, 시스템 로그 같은 **운용 UI 기본 문법**은 donor로 재사용 가치가 높다.
- 하지만 파일 자체는 `jms` 서비스, `DONE -> NEXT READY 생성`, tank/job naming, protocol wording에 강하게 묶여 있어 **그대로 복제하면 WashTank 의미가 따라온다**.
- 또한 `officeout.jsx` 자체에는 상세 **모달이 없고 우측 패널형 상세**만 있다. 목표 화면의 “카드 선택 -> 상세 모달” 구조는 같은 donor군의 [TankControl.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/TankControl.jsx) 또는 [Fhandler.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Fhandler.jsx)에서 modal shell을 별도로 빌려와야 한다.
- 따라서 donor 가치는 높지만, **직접 변형보다 구조 추출 승격**이 더 안전하다.

## 3. reusable surface

- page shell
  - 상단 navbar, 좌/중/우 3영역 본문, 하단 로그 shelf 구조
- board/list structure
  - 중앙 grid 카드 목록
  - 선택된 카드 강조
  - 검색 input + refresh action
- state handling pattern
  - `list`, `selected`, `search`, `isProcessing`, `logs`
  - fetch -> select -> act -> refresh 흐름
- status expression
  - badge
  - next-step hint
  - success/error/system log tone
- side panel pattern
  - 선택 오브젝트 상세 + primary action button
- modal donor 후보
  - [TankControl.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/TankControl.jsx): overlay + modal + slot 구조
  - [Fhandler.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Fhandler.jsx): modal overlay / content / header / grid slot 시각 패턴

## 4. coupling / blockers

- hardcoded service coupling
  - [Officeout.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officeout.jsx) 는 `./services/jms`에 직접 결합되어 있다.
  - `getJobsByStatusAndTypes`, `hasActiveJob`, `createJob` 호출과 반환 shape에 의존한다.
- business-specific naming
  - `DONE`, `INBOUND`, `WASH`, `REPAIR`, `OUTBOUND`, `tank`, `job`, `READY`
  - `TRANSITION_HUB`, `NEXT_STEP_PROTOCOL`, `TRANSITION_CONTROL`
- hardcoded field shape
  - `job_type`, `tank_id`, `completed_at`, `tanks.tank_number`
  - `getTankNumber()` 자체가 tank 도메인 fallback을 내장한다.
- inline styles monolith
  - 스타일이 파일 내부 객체 하나에 전부 박혀 있다.
  - BoardShell / Card / Panel / FooterLog 같은 단위로 재사용 abstraction이 없다.
- no modal flow in target file
  - 목표 화면은 “카드 선택 -> 상세 모달”인데, `Officeout.jsx`는 “카드 선택 -> 우측 패널”이다.
- routing / container ambiguity
  - [OfficePageContainer.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/OfficePageContainer.jsx) 는 오히려 `Office.jsx`를 물고 있고, `Officeout.jsx`는 self-contained page처럼 직접 `main.jsx`에 연결된다.
  - 즉 container/view/service 분리는 donor로 보기엔 느슨하고 일관되지 않다.

## 5. promotion path

- 가장 현실적인 1차 승격 경로는 **직접 변형이 아니라 donor extraction**이다.

### recommended component promotion draft

- `BoardShell`
  - navbar + main body + footer log shell
- `BoardToolbar`
  - title / search / refresh / top badges
- `StatusLane`
  - 좌측 가이드/규칙/필터 요약 패널
- `ObjectCardGrid`
  - 중앙 카드 리스트
- `ObjectCard`
  - 선택 가능 카드 단위
- `SelectionDetailPanel`
  - 우측 상세/액션 패널
- `DetailModal`
  - `TankControl`/`Fhandler` donor를 참고한 상세 모달 shell
- `ActivityPanel`
  - footer log / activity stream
- `FeedbackComposer`
  - 목표 화면의 feedback input 영역 후보

### minimal-change promotion path

1. [Officeout.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Officeout.jsx) 에서 **레이아웃/선택/로그 구조만 donor로 읽는다.
2. 도메인 로직(`jms`, tank/job naming, next-step protocol)은 재사용하지 않는다.
3. 새 운용화면은 `BoardShell + ObjectCardGrid + SelectionDetailPanel` 구조로 먼저 만든다.
4. 상세 modal은 `Officeout`에서 억지로 만들지 말고, [TankControl.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/TankControl.jsx) / [Fhandler.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/app/main/Fhandler.jsx) donor를 참고해 별도 `DetailModal`로 붙인다.
5. 서비스는 WashTank `jms` shape를 버리고 현재 엔진의 `latest/history/diff/attention/memory` payload에 맞는 adapter를 새로 만든다.

## 6. recommended next step

- 다음 1스텝은 구현이 아니라, **`Officeout donor extraction map`** 을 한 장 더 만드는 것이다.
- 구체적으로는 아래 4개만 분리 표로 적으면 된다.
  - shell donor
  - card donor
  - right-panel donor
  - modal donor

### structural read

- `Officeout.jsx`를 운용화면 donor로 아예 못 쓰는 것은 아니다.
- 다만 “wash tank 업무 페이지를 조금 바꾸자”는 접근은 baseline에 해롭다.
- 맞는 접근은 **Officeout의 표면 구조만 donor로 삼고, 서비스/도메인 의미/상태 전이 규칙은 버린 뒤, 공용 BoardShell 계층으로 승격하는 것**이다.
