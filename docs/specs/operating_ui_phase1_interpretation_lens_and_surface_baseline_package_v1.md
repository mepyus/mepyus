# operating ui phase1 interpretation lens and surface baseline package v1

## 1. verdict

판정:
- **lock as phase1 baseline**

중요:
- 이 문서는 UI 구현안이 아니다
- schema 변경안도 아니다
- recommendation/workflow semantics를 여는 문서도 아니다
- parked compare track을 재개하는 문서도 아니다

현재 의미는 아래까지다.
- operating UI / exploration / search / memory sticker / similar connection surface / interpretation lens 구조를 phase1의 상위 baseline으로 잠근다
- 이후 UI / engine / script 논의가 와도, 이 문서를 해석 기준의 상위 축으로 재사용해야 한다

## 2. package structure choice

이번 패키지는 **1문서 구조**를 택했다.

이유:
- 이번 턴의 목적은 지금까지 나뉘어 잠긴 면들을 하나의 phase1 해석축으로 통합하는 데 있었다
- `phase1 structure`, `lens lock`, `richness rule`, `surface distinctions`, `memory baseline`, `non-goals`, `decision`은 하나의 연속된 baseline 문서로 읽혀야 한다
- 2문서로 나누면 면 역할과 해석 렌즈 규칙이 다시 분리되어 상위 기준선 효과가 약해질 수 있다

즉 이번 패키지는
- phase1 구조 요약
- interpretation lens 잠금
- richness 발현 규칙
- surface 역할 분리
- memory baseline
- non-goals
- phase1 잠금
을 하나의 spec 문서로 통합한다.

## 3. phase1 structure summary

### operating UI

- operating UI는 **관측면**이다
- 현재 선택된 대상과 현재 상태를 read-only로 읽게 하는 current read surface이며, 지금 무엇을 보고 있는지와 어디서 더 들어갈지를 보여준다

### exploration

- exploration은 **step-by-step 해석 진입면**이다
- 객체에서 출발해 카메라, 위치값, 연결/값을 따라가며 의미 있는 경로를 발견하는 과정이고, 얇은 탐색 흔적을 남기며 deeper reading으로 이어진다

### search

- search는 **direct access 면**이다
- 사용자가 지금 필요한 것을 바로 찾는 구조이며, step-by-step 경로를 대체하지 않고 필요한 entry를 짧게 여는 역할이다

### memory sticker

- memory sticker는 **선택적 승격 장치**다
- 탐색 과정에서 나온 것 중 다시 볼 가치가 있는 일부만 sparse하게 붙잡아 재접속 가능성을 남긴다

### similar connection surface

- similar connection surface는 **스티커 기반 유사 구조 재조회면**이다
- 기억 스티커가 붙은 연결 추출값을 seed로 삼아, 내부 공간에서 유사한 연결 구조를 국소적으로 다시 읽게 한다

## 4. interpretation lens lock

컬럼값 / 층위값은
**data field가 아니라 interpretation lens**
로 정의한다.

의미:
- 렌즈는 같은 재료를 다시 읽게 만드는 해석면이다
- 렌즈는 고정 데이터 컬럼처럼 “항상 전량 표시되는 필드 집합”이 아니다
- 렌즈는 선택된 재료와 읽기 목적에 따라 제한적으로 켜지는 interpretation path다

중요:
- 모든 렌즈를 전량 활성화하지 않는다
- 렌즈는 선택적이고 희소하게 작동해야 한다
- 렌즈 자체를 데이터 표처럼 과밀화하면 phase1의 읽기 구조가 무너진다

정리:
- column은 field table이 아니다
- column/층위는 같은 재료를 다르게 드러내는 interpretation lens다

## 5. richness emergence rule

공간이 풍부해지는 것은
렌즈 자체 때문이 아니라,
**스티커 / 기억 / 선택된 구조를 통해 발현**
된다는 점을 phase1 기준으로 잠근다.

### lens = 가능성 층

- lens는 무엇을 어떤 각도에서 읽을 수 있는지의 가능성을 연다
- lens 자체는 richness를 전량 보유하거나 보장하지 않는다

### sticker / memory / selected structure = 발현 층

- 실제 richness는 선택적으로 붙잡힌 memory sticker,
  다시 볼 수 있게 남은 memory,
  현재 선택된 구조에서 발현된다
- 즉 richness는 “렌즈를 많이 켠다”가 아니라
  “어떤 구조를 선택하고 무엇을 기억으로 붙잡았는가”에서 나온다

정리:
- lens는 opening layer다
- sticker/memory/selected structure는 emergence layer다

## 6. exploration vs search vs similar-connection

### exploration

- **객체에서 출발하는 step-by-step**
- 경로를 따라가며 의미 있는 연결과 위치를 발견하는 과정이다

### search

- **필요한 것을 바로 찾는 direct access**
- 객체, 카메라, 위치값, 연결, 기억 중 무엇이든 상황에 맞게 바로 접속시키는 entry 구조다

### similar connection surface

- **기억 스티커가 붙은 연결 추출값을 씨앗으로 유사 구조를 국소적으로 훑는 면**
- exploration처럼 경로를 처음부터 밟는 것도 아니고, search처럼 즉시 원하는 대상만 찾는 것도 아니다

### anti-confusion note

- exploration은 discovery path다
- search는 direct entry다
- similar connection surface는 seeded local similarity reading이다

이 셋이 다시 섞이기 시작하면 phase1 baseline 위반으로 본다.

## 7. memory sticker baseline

기억 스티커는
**자동 전량 저장이 아니라 선택적 승격**
으로 잠근다.

### distinction

- 탐색 흔적:
  step-by-step 탐색 중 스쳐 지나간 얇은 흔적
- 기억 스티커:
  다시 볼 가치가 있어 selective promotion된 표찰
- 유사 연결 조회 결과:
  stickered connection seed를 기준으로 다시 드러난 유사 구조

이 셋은 같은 것이 아니다.

### memory sticker minimum conditions

아래 조건 중 의미 있게 충족되는 경우에만 기억 스티커를 붙인다.

1. 다시 볼 가치가 있다
2. 후속 해석 가능성이 남아 있다
3. 응결핵이 될 가능성이 있다
4. 의미 있는 연결 경로를 남긴다

보정 원칙:
- 너무 느슨해서 모든 흔적이 sticker가 되게 해서는 안 된다
- 너무 빡빡해서 중요한 중간 표찰이 사라지게 해서도 안 된다
- sticker는 sparse하지만 재접속 가치가 분명해야 한다

## 8. phase1 non-goals

아래는 명시적으로 phase1 baseline 밖에 둔다.

- 전체 공간 한 번에 보기
- recommendation/workflow 면으로 확장
- 모든 클릭 자동 기억화
- 컬럼값을 고정된 데이터 필드처럼 이해하는 것
- parked compare track을 자동 재개하는 것
- 새 candidate track을 섣불리 승격하는 것

추가 원칙:
- phase1은 whole-space view가 아니다
- phase1은 recommendation layer가 아니다
- phase1은 memory hoarding layer가 아니다
- phase1은 lens table이 아니다

## 9. future direction note

장기적으로는 아래 가능성이 열려 있을 수 있다.

- 더 넓은 공간
- 더 풍부한 렌즈
- 더 가벼운 기억 표현
  예: 벡터화된 관계 흔적 같은 더 압축된 기억 표현

중요:
- 이것은 지금 당장 구현안을 뜻하지 않는다
- phase1은 그 장기 확장의 기반만 잠그는 단계다
- 현재는 역할 분리, lens 해석, selective memory, local similarity reading의 baseline만 유지한다

## 10. lock / clarification decision

판정:
- **lock as phase1 baseline**

이유:
- 지금까지의 논의는 이미 phase1 구조를 거의 맞춘 상태이고, 현재는 이를 상위 해석축으로 고정하는 편이 더 중요하다
- operating UI / exploration / search / memory sticker / similar connection surface / interpretation lens의 경계가 지금 충분히 명확하다
- 이 시점에서 잠그지 않으면 이후 구현/스크립트 논의에서 다시 역할이 섞일 가능성이 크다

## 11. if lock: rationale

### why lock now

- phase1은 지금 수준에서 이미 충분한 구조적 일관성을 갖췄다
- 특히 `operating UI = 관측면`, `exploration = step-by-step`, `search = direct access`, `memory sticker = selective promotion`, `similar connection surface = sticker-based local rereading`, `columns = interpretation lens` 구도는 더 미루면 다시 흐려질 가능성이 높다
- 지금 잠그면 이후 구현/스크립트/UI 확장 논의가 먼저 상위 기준을 통과해야 하므로 구조 혼용을 줄일 수 있다

### upper interpretation rule

- 이후 구현/스크립트/UI 확장 논의는 모두 이 문서를 상위 해석 기준으로 봐야 한다
- 즉 후속 논의는 먼저 아래 질문을 통과해야 한다
  - 이것은 어떤 surface 역할인가
  - 이것은 lens인가 field인가
  - richness가 lens 자체에서 나오나, selected structure에서 발현되나
  - memory는 selective promotion을 지키는가
  - recommendation / whole-space / promotion obsession으로 새지 않는가

## 12. if needs clarification: rationale

현재 판정은 lock이므로 아래는 적용하지 않는다.

### rationale

- not applicable

## 13. risk and correction record

### 이번 패키지에서 본 리스크

1. exploration/search confusion
- exploration, search, similar connection surface가 다시 entry 구조로 한데 섞일 위험이 있었다

2. memory overuse risk
- 탐색 흔적과 유사 연결 조회 결과까지 모두 sticker/memory로 과승격될 위험이 있었다

3. recommendation drift
- similar connection이나 richer reading을 recommendation/workflow semantics로 오해할 위험이 있었다

4. column-as-data-field misunderstanding
- 컬럼값/층위값을 interpretation lens가 아니라 고정 필드 테이블처럼 읽을 위험이 있었다

5. premature promotion obsession
- watchpoint나 compare parked track을 다시 열거나, 새 candidate track으로 바로 이어가려는 조급함이 스며들 위험이 있었다

### 어떻게 통제했는가

- phase1 surface들을 역할별로 다시 분리해 적었다
- memory sticker baseline에서 탐색 흔적 / sticker / 조회 결과를 구분했다
- recommendation/workflow, whole-space view, automatic memory를 non-goal로 바깥에 뒀다
- interpretation lens를 field가 아니라 선택적 해석 렌즈로 못박았다
- parked compare 재개와 premature candidate promotion을 명시적으로 금지했다

### working memory / log record

- broad package 수행 기준에서
  - operating UI = observation surface
  - exploration = step-by-step interpretation entry
  - search = direct access surface
  - memory sticker = selective promotion device
  - similar connection surface = sticker-seeded local similarity rereading
  - columns = interpretation lenses
  - richness = emerges through sticker/memory/selected structure
  로 기록한다

## 14. alignment / memory record

- supervisor starting judgment:
  1차 페이즈 구조는 거의 맞춰졌고, 지금은 이를 상위 기준선으로 잠가야 한다고 봤다
- codex own judgment:
  이 판단에 동의한다. 가장 흔들리기 쉬운 경계는 `exploration / search / similar connection surface`의 역할 혼용과, `columns`를 해석 렌즈가 아니라 고정 데이터 필드처럼 읽는 지점이라고 봤다
- disagreement or risk:
  richness를 lens 자체의 속성처럼 읽거나, similar connection을 exploration/search와 혼용하면 phase1 구조가 다시 흐려질 위험이 있었다
- resolution:
  surface 역할을 다시 분리하고, `lens = 가능성 층`, `sticker/memory/selected structure = 발현 층`으로 phase1 baseline을 고정했다

## 15. recommendation

- 추천:
  **lock as phase1 baseline**

짧은 이유:
- 지금 phase1 구조는 상위 기준선으로 잠글 만큼 충분히 정리되어 있다
- 이후 확장 논의가 오더라도 먼저 이 문서를 통과하게 해야 역할 혼용과 과잉 확장을 막을 수 있다
