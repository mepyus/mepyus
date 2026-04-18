# reference sheet / officeout v1

## 1. reference identity
- source file: [officeout.jsx](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/src/officeout.jsx)
- source family: `WashTank`
- page role: `OfficeOutV5`
- raw size: `1654 lines`

## 2. one-line reading
- 이 파일은 단순 출고 페이지가 아니라, `DONE 상태의 작업을 다음 공정 또는 출고로 넘기기 위한 말단 운영 허브` 패턴을 담은 레퍼런스다.

## 3. core structural reading
이 파일의 중심 구조는 아래다.

1. 완료된 작업 집합을 불러온다
2. 각 항목의 다음 선택 가능 상태를 계산한다
3. 활성 상태와 예외 상태를 판독한다
4. 목록에서 후보를 좁힌다
5. 상세 패널에서 다음 액션을 확정한다
6. 일반 전이와 특수 전이 `OUTBOUND` 를 분리한다
7. 특수 전이는 `REQUESTED -> SCHEDULED -> READY` 다단계 흐름으로 처리한다
8. 모든 처리는 로그와 재동기화로 닫는다

## 4. cut units
이 파일을 전처리할 때의 1차 절단 단위는 아래가 적합하다.

### A. constants / protocol
- `UI_CONFIG`
- `PROCESS_TABS`
- `ACTOR`

### B. source-state layer
- `useState` 묶음
- selection / search / processing / outbound form / logs 상태

### C. interpretation layer
- `getTankNumber`
- `getNextJobOptions`
- `getOutboundRequestState`
- `getHandoffState`
- `getStateLabel`
- `getCardVisual`
- `matchesTab`
- `getTabCount`

### D. synchronization layer
- `loadActiveOutboundRequests`
- `fetchDoneJobs`
- `useEffect` 초기 로드 / 선택 상태 동기화 / form hydration

### E. transition action layer
- `ensureOutboundReadyJob`
- `handleNormalTransition`
- `handleCreateOutboundRequested`
- `handleScheduleOutbound`
- `handleCancelOutbound`

### F. outbound subflow layer
- `renderOutboundPanel`

### G. view composition layer
- navbar
- sidebar protocol card
- workspace list/grid
- batch panel
- footer log shelf

### H. style layer
- `const styles = { ... }`

## 5. layer tags
이 레퍼런스에 붙일 1차 층위 태그는 아래가 적합하다.

- `structure_layer`
  - 좌/중/우 패널 구조
  - 목록 + 상세 + 운영 로그

- `process_layer`
  - `DONE -> NEXT READY`
  - `OUTBOUND REQUESTED -> SCHEDULED -> READY`

- `judgment_layer`
  - 상태 판독
  - 다음 공정 허용/차단
  - 탭 매칭

- `exception_layer`
  - 이미 active job 존재
  - JMS 함수 미존재
  - 필수 입력 누락

- `domain_layer`
  - `INBOUND / WASH / INSPECT / REPAIR / STORAGE / OUTBOUND`

- `reuse_layer`
  - 후보 좁히기
  - 상세 확인 후 최종 액션
  - 일반 플로우와 특수 서브플로우 분리

- `operator_trace_layer`
  - `logs`
  - `addLog`
  - 상태 변화 메시지

## 6. reusable patterns
도메인을 제거하고 남는 재사용 패턴은 아래다.

### pattern 1. candidate narrowing
- 목록 전체를 가져온 뒤
- 탭 / 검색 / 상태 판독으로 후보를 좁힌다

### pattern 2. computed handoff state
- 원시 상태를 그대로 쓰지 않고
- `handoff state` 를 계산해서 읽는다

### pattern 3. detail-confirm split
- 목록에서 선택
- 오른쪽 상세 패널에서 최종 확인
- 액션은 상세 패널에서만 수행

### pattern 4. normal flow + special subflow
- 일반 전이는 바로 next READY 생성
- 특수 전이는 요청/확정/취소의 별도 서브플로우를 탄다

### pattern 5. action gating
- 허용되지 않은 전이 차단
- 이미 존재하는 active next 차단
- 필수값 누락 차단

### pattern 6. resync after action
- 액션 이후 반드시 재조회
- 선택 상태도 다시 동기화

### pattern 7. operator-visible trace
- 시스템이 무슨 전이를 했는지
- 로그로 바로 보이게 남긴다

## 7. why this matters
이 레퍼런스가 중요한 이유는 `OfficeOut` 라는 이름 때문이 아니다.
이 안에 이미 아래 구조가 있기 때문이다.

- 선별
- 상태 판단
- 후보 좁히기
- 상세 확인
- 최종 확정
- 일반 흐름 / 특수 흐름 분리
- 운영 로그와 재동기화

즉 이 파일은 과거 코드가 아니라,
`말단 운영 허브 패턴` 의 응축본으로 보는 게 맞다.

## 8. observer reading
현재 observer layer에서 이 파일을 읽는 방식은 아래가 적합하다.

- `reference_as_material`
  - 다음 프로그램 설계에 재사용할 구조 재료

- `reference_as_calibration`
  - 입력기를 어떤 절단 단위와 층위로 설계할지 교정하는 자산

## 9. keep / avoid
### keep
- 상태 판독 함수를 별도 절단 단위로 본다
- `OUTBOUND` 서브플로우를 독립 서브패턴으로 본다
- UI와 판단 로직이 섞여 있어도 구조를 추출해 남긴다

### avoid
- 이 파일을 단순 JSX 한 덩어리로 보는 것
- `출고 페이지` 라는 도메인 이름만 보고 패턴을 놓치는 것
- 스타일 객체 때문에 전체 가독성을 포기하는 것

## 10. current judgment
- 첫 기준 레퍼런스로 적합: `YES`
- 코어 truth로 바로 올릴 대상: `NO`
- observer preprocessor 기준 샘플로 쓰기 적합: `YES`

## 11. next natural step
- 이 파일 하나를 대상으로 `절단 단위 + 층위 태그 + 재사용 패턴` 을 JSON/MD로 동시에 뽑는 `reference preprocessor draft` 를 만드는 것이 가장 자연스럽다.
