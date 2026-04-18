# exploration search memory sticker baseline package v1

## 1. verdict

판정:
- **lock this as current baseline**

중요:
- 이 문서는 UI 구현안이 아니다
- schema 변경안도 아니다
- recommendation/workflow semantics를 여는 문서도 아니다

현재 의미는 아래까지다.
- operating UI / exploration / search / memory sticker의 역할 분리를 현재 baseline으로 잠근다
- 이후 탐색/검색/운용 화면이 확장되더라도, 이 문서의 역할 경계가 상위 해석축으로 재사용되어야 한다

## 2. package structure choice

이번 패키지는 **1문서 구조**를 택했다.

이유:
- 이번 턴의 목적은 기능 제안이 아니라 역할 기준을 baseline으로 잠그는 데 있었다
- `baseline definition`, `exploration minimal loop`, `search definition`, `memory sticker rule`, `anti-confusion`, `lock decision`은 하나의 연속된 기준 문서로 읽혀야 한다
- 보조 문서를 추가하면 탐색/검색/기억 스티커 기준이 다시 분산될 수 있다

즉 이번 패키지는
- 역할 정의
- 최소 탐색 루프
- 검색 정의
- 기억 스티커 기준
- 혼동 방지
- baseline 잠금
을 하나의 spec 문서로 통합한다.

## 3. baseline definition

### operating UI

무엇을 하는가:
- 현재 선택된 대상과 현재 상태를 read-only로 읽게 하는 운용 화면이다
- 지금 무엇을 보고 있는지, 현재 선택의 상태가 어떠한지, 어디서 더 들어갈지의 진입 기준을 제공한다

무엇을 하지 않는가:
- 전체 공간을 한 번에 다 보여주려 하지 않는다
- 탐색 그 자체를 모두 대신하지 않는다
- 검색 엔진이나 recommendation 면 역할을 하지 않는다

### exploration

무엇을 하는가:
- 사용자가 step-by-step으로 객체, 카메라, 위치값, 연결을 따라가며 의미 있는 경로를 발견하는 과정이다
- 아직 확정되지 않은 경로를 얇은 흔적으로 남기며, 필요하면 더 깊은 상세로 들어간다

무엇을 하지 않는가:
- 바로 필요한 것을 즉시 찾는 direct access를 기본으로 하지 않는다
- 모든 탐색 흔적을 기억으로 승격하지 않는다
- 전체 공간을 한눈에 정리하는 역할을 하지 않는다

### search

무엇을 하는가:
- 사용자가 지금 필요한 것을 바로 찾는 direct access 구조다
- entry point를 줄여 원하는 대상에 빠르게 접속하게 한다

무엇을 하지 않는가:
- step-by-step 탐색을 대체하지 않는다
- 탐색 경로 자체를 풍부하게 보존하는 장치가 아니다
- 검색 결과를 자동으로 기억 스티커로 승격하지 않는다

### memory sticker

무엇을 하는가:
- 탐색 과정에서 나온 것 중 다시 볼 가치가 있는 일부를 선택적으로 승격해 붙잡는 기억 표찰이다
- 얇은 탐색 흔적을 모두 저장하는 것이 아니라, 재접속 가치가 있는 지점을 selective promotion으로 남긴다

무엇을 하지 않는가:
- 전체 탐색 로그 저장소가 아니다
- 모든 클릭/이동/미리보기를 자동 수집하지 않는다
- 작은 recommendation 카드나 workflow 지시문 역할을 하지 않는다

## 4. exploration minimal loop

탐색의 최소 루프는 아래로 잠근다.

1. 객체 선택
2. 카메라 선택
3. 위치값 선택
4. 연결/값 미리보기
5. 의미 있으면 기억 스티커
6. 더 깊으면 모달/상세 진입

### 얇은 탐색 흔적

- 객체를 보고 지나간 흔적
- 카메라를 바꿔 본 흔적
- 위치값을 잠깐 확인한 흔적
- 연결/값을 미리보기만 한 흔적

의미:
- 이들은 exploration의 얇은 진행 흔적이다
- 기본적으로는 탐색 진행을 돕는 transient trace에 가깝고, 곧바로 기억 승격 대상이 아니다

### 기억 스티커와의 분리

- 기억 스티커는 위 루프 중 일부 지점을 선택적으로 승격한 것이다
- 즉 모든 탐색 흔적이 sticker가 되는 것이 아니라,
  탐색 흔적 중 다시 붙잡을 가치가 확인된 일부만 sticker가 된다

### 더 깊은 진입과의 분리

- 모달/상세 진입은 더 깊은 읽기를 위한 다음 단계다
- 이것도 기억 스티커와 동일하지 않다
- sticker는 “다시 볼 가치가 있는 표찰”이고,
  modal/detail은 “지금 더 깊게 읽는 진입면”이다

## 5. search definition

검색은
**사용자가 지금 필요한 것을 바로 찾는 구조**
로 정의한다.

중요:
- 검색 대상이 미리 하나로 고정되는 것은 아니다
- 대상은 상황에 따라
  - 객체
  - 카메라
  - 위치값
  - 연결
  - 기억
  가 될 수 있다

즉 search는
대상을 미리 좁히는 구조라기보다,
필요한 entry를 direct access로 여는 구조다.

### exploration과의 차이

- `exploration = step-by-step`
- `search = direct access`

정리:
- exploration은 경로를 따라가며 발견하는 구조다
- search는 필요한 지점으로 바로 접근하는 구조다
- 둘은 연결될 수는 있어도 동일한 역할로 섞이면 안 된다

## 6. memory sticker rule

기억 스티커는
**자동 전량 저장이 아니라 선택적 승격**
으로 잠근다.

### 구분

- 얇은 탐색 흔적:
  step-by-step 탐색 중 스쳐 지나가는 흔적
- 기억 스티커:
  다시 보거나 다시 연결할 가치가 있어 선택적으로 붙잡은 표찰

### 기억 스티커 최소 조건

아래 조건 중 의미 있게 충족되는 경우에만 기억 스티커를 붙인다.

1. 다시 볼 가치가 있다
2. 후속 해석 가능성이 남아 있다
3. 응결핵이 될 가능성이 있다
4. 의미 있는 연결 경로를 남긴다

보정 원칙:
- 위 조건은 너무 느슨해서 아무 흔적이나 sticker가 되게 해서는 안 된다
- 동시에 너무 빡빡해서 중요한 중간 표찰이 사라지게 해서도 안 된다
- 즉 sticker는 sparse하지만 실질적인 재접속 표찰이어야 한다

## 7. non-goals / anti-confusion

아래는 명시적으로 이 baseline 밖에 둔다.

- 모든 탐색 클릭 자동 기억화
- 탐색과 검색의 혼용
- 운용화면에서 전체 공간 뷰 시도
- 탐색면을 recommendation 면처럼 만드는 것
- 모달을 작은 전체 우주처럼 비대화하는 것

추가 원칙:
- operating UI는 current read surface다
- exploration은 경로형 접근이다
- search는 direct access다
- memory sticker는 selective promotion이다

이 네 역할이 다시 섞이기 시작하면 baseline 위반으로 본다.

## 8. future scalability note

나중에 공간이 더 커지면,
지금의 명시적 연결 기억은
더 가벼운 표현으로 옮겨갈 가능성이 있다.

예를 들면:
- 더 압축된 관계 흔적
- 더 가벼운 연결 표찰

중요:
- 이것은 지금 당장 구현안을 뜻하지 않는다
- 현재 baseline은 여전히 `명시적 연결 기억 + selective promotion` 기준 위에서 해석한다
- 이 note는 오직 방향성 메모 수준으로만 남긴다

## 9. lock / clarification decision

판정:
- **lock this as current baseline**

이유:
- operating UI / exploration / search / memory sticker의 역할 구분은 지금 잠가 두는 편이 후속 확장에서 훨씬 안전하다
- 특히 `exploration = step-by-step`, `search = direct access`, `memory sticker = selective promotion` 구도는 더 미루면 다시 섞일 가능성이 크다
- 현재 수준에서는 기준선 잠금에 필요한 최소 명확성이 충분하다

## 10. if lock: rationale

### why lock now

- 지금 기준을 잠그면 이후 탐색면, 검색면, 운용화면, 기억 표찰이 서로의 역할을 침범하는 것을 미리 막을 수 있다
- operating UI 확장이나 engine-side 확장이 오더라도, 먼저 이 역할 분리 기준에 맞는지 확인하는 상위 해석축이 생긴다
- 특히 전체 공간 뷰 욕구, recommendation화, 자동 기억화 같은 과성장을 baseline 단계에서 차단할 수 있다

### upper interpretation rule

- 이후 어떤 종류의 페이지나 기능이 와도
  이 문서의 기준을 상위 해석축으로 삼아야 한다
- 즉 새 기능은 먼저 아래 질문을 통과해야 한다
  - 이것은 operating UI인가
  - exploration인가
  - search인가
  - memory sticker인가
  - 아니면 여러 역할을 혼합해 baseline을 흐리는가

## 11. if needs clarification: rationale

현재 판정은 lock이므로 아래는 적용하지 않는다.

### rationale

- not applicable

## 12. risk and correction record

### 이번 패키지에서 본 리스크

1. exploration/search confusion
- step-by-step 탐색과 direct access 검색이 다시 같은 것으로 읽힐 위험이 있었다

2. sticker overuse risk
- 탐색 흔적 대부분이 기억 스티커로 과승격될 위험이 있었다

3. UI overgrowth risk
- operating UI가 전체 공간 뷰나 과대 모달로 자라날 위험이 있었다

4. promotion obsession risk
- 탐색 중 나온 모든 의미 있는 순간을 sticker로 올리고 싶어지는 승격 집착이 생길 위험이 있었다

### 어떻게 통제했는가

- exploration과 search를 각각 `step-by-step`과 `direct access`로 명시 고정했다
- 얇은 탐색 흔적과 기억 스티커를 분리하고, sticker를 selective promotion으로 못박았다
- operating UI는 current read surface이지 전체 공간 뷰가 아니라고 다시 적었다
- non-goals에 자동 기억화, recommendation화, modal 비대화를 명시적으로 바깥에 뒀다

### working memory / log record

- broad package 수행 기준에서
  - operating UI = current read surface
  - exploration = step-by-step path
  - search = direct access
  - memory sticker = selective promotion
  으로 기록한다
- 이후 관련 문서는 먼저 이 baseline과 충돌하는지부터 확인해야 한다

## 13. alignment / memory record

- supervisor starting judgment:
  지금은 operating UI / exploration / search / memory sticker의 기준을 먼저 잠가야 하며, 그렇지 않으면 나중에 탐색/검색/운용화면 역할이 다시 섞인다고 봤다
- codex own judgment:
  이 판단에 동의한다. 지금 가장 흔들리기 쉬운 경계는 `탐색 흔적 vs 기억 스티커`, 그리고 `exploration vs search`라고 봤다
- disagreement or risk:
  memory sticker를 너무 넓게 잡으면 탐색 기록 전체가 기억화되고, search를 넓게 잡으면 exploration과 역할이 다시 섞일 위험이 있었다
- resolution:
  `exploration = step-by-step`, `search = direct access`, `memory sticker = selective promotion`, `operating UI = current read surface`로 역할을 명시 고정했다

## 14. recommendation

- 추천:
  **lock this as current baseline**

짧은 이유:
- 지금 이 기준을 먼저 잠가야 이후 확장에서도 역할 혼용을 막을 수 있다
- 특히 탐색/검색/기억 스티커의 분리를 baseline으로 고정해 두는 것이 later-stage 확장보다 먼저다
