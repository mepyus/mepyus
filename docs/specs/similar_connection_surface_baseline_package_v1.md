# similar connection surface baseline package v1

## 1. verdict

판정:
- **lock this as current baseline**

중요:
- 이 문서는 UI 구현안이 아니다
- recommendation semantics를 여는 문서가 아니다
- 전체 공간 뷰 설계 문서도 아니다
- schema 변경안도 아니다

현재 의미는 아래까지다.
- 탐색에서 건져낸 연결 추출값을 seed로 삼아 내부 공간에서 유사한 연결 구조를 다시 찾고 보여주는 별도 면을 baseline으로 잠근다
- 이 면은 operating UI / exploration / search / memory sticker와 구분되는 독립 surface로 해석해야 한다

## 2. package structure choice

이번 패키지는 **1문서 구조**를 택했다.

이유:
- 이번 턴의 목적은 새 페이지의 구현을 설계하는 것이 아니라, 역할과 경계를 baseline으로 먼저 잠그는 데 있었다
- `page role`, `input unit`, `structure baseline`, `similarity meaning`, `memory carryover`, `naming`, `decision`은 하나의 연속된 기준 문서로 읽혀야 한다
- 보조 문서를 추가하면 exploration/search/whole-space-view와의 경계가 다시 분산될 수 있다

즉 이번 패키지는
- 페이지 정의
- 입력 단위 잠금
- 구조 baseline
- similarity 의미 제한
- 기억 규칙 carryover
- 이름 후보
- baseline 잠금
을 하나의 spec 문서로 통합한다.

## 3. page role definition

### one-line definition

이 페이지는
**기억 스티커가 붙은 연결 추출값을 seed로 삼아, 내부 공간에서 유사한 연결 구조를 다시 찾고 읽게 하는 별도 조회면**이다.

### operating UI와의 구분

- operating UI는 현재 선택된 대상과 현재 상태를 read-only로 읽게 하는 current read surface다
- 이 페이지는 현재 상태를 읽는 운용면이 아니라,
  선택된 연결 seed를 기준으로 유사 구조를 다시 조회하는 별도 면이다

### exploration과의 구분

- exploration은 step-by-step 경로를 따라가며 발견하는 과정이다
- 이 페이지는 step-by-step 탐색 과정 자체가 아니라,
  탐색에서 건져낸 연결 seed를 기준으로 유사 구조를 다시 보는 조회면이다

### search와의 구분

- search는 사용자가 필요한 것을 바로 찾는 direct access 구조다
- 이 페이지는 대상에 즉시 접근하는 search가 아니라,
  특정 seed connection을 중심으로 similarity를 읽는 구조다

### memory sticker와의 구분

- memory sticker는 selective promotion된 표찰이다
- 이 페이지는 sticker 자체가 아니라,
  sticker가 붙은 연결 추출값을 입력으로 받아 유사 구조를 조회하는 surface다

### what it does

- 의미 있는 연결 추출값을 seed로 삼는다
- 그 seed와 닿는 유사한 내부 연결 구조를 읽게 한다
- 더 깊은 읽기가 필요하면 modal/detail로 넘긴다

### what it does not do

- 정답 추천을 하지 않는다
- 전체 공간을 한 번에 지도처럼 보여주지 않는다
- exploration과 search를 대체하지 않는다
- 카드 클릭을 자동 기억화하지 않는다

## 4. input unit lock

### locked input unit

입력 단위는
**객체 자체가 아니라, 기억 스티커가 붙은 연결 추출값(해석 경로)**이다.

예:
- `장미 -> AI -> 홀로그램`

### why this is the seed

- 이 페이지가 다시 읽으려는 것은 “어떤 객체가 중요한가”가 아니라
  “어떤 연결 경로가 의미 있는 seed로 남았는가”이기 때문이다
- sticker가 붙은 연결 추출값은 이미 한번 selective promotion을 통과한 경로이므로,
  내부 유사 구조를 다시 조회할 기준점으로 충분하다
- 즉 seed는 object identity가 아니라 interpreted connection path다

## 5. page structure baseline

최소 화면 구조는 아래로 잠근다.

### left

- 연결 추출값 카드 목록

의미:
- sticker가 붙은 seed connection들을 카드 단위로 읽고 선택하는 영역이다

### main

- 선택한 카드와 유사한 내부 연결 구조

의미:
- 선택된 seed와 닿는 유사 구조를 메인에서 읽는다
- 이 메인은 similarity reading surface이지, 전체 지도면이 아니다

### deeper path

- 더 깊은 내용은 modal/detail 진입

의미:
- 메인에서 다 담지 않고, deeper reading이 필요할 때만 detail로 들어간다

### why this is better than whole-space view

- whole-space view는 한 번에 너무 많은 구조를 동시 노출해 현재 읽기의 기준점을 흐릴 수 있다
- 반면 이 구조는 seed connection을 기준으로 주변 유사 구조만 제한적으로 드러내므로,
  전체 공간 지도화로 번지지 않고 current reading focus를 유지하기 쉽다

## 6. similarity meaning lock

`유사한 연결 구조`는
**선택된 seed connection과 해석 경로 차원에서 닿는 내부 구조를 다시 읽게 하는 것**
으로 잠근다.

중요:
- 이것은 recommendation이 아니다
- “이것이 정답이다”를 말하지 않는다
- “이것을 다음에 하라”를 유도하지 않는다

### explicitly out of scope

- 정답 추천
- 순위화
- workflow 유도
- 전체 공간 지도화

정리:
- similarity는 reading aid다
- similarity는 answer ranking이 아니다
- similarity는 path resonance를 다시 읽게 하는 제한적 surface다

## 7. memory rule carryover

### no automatic memory on click

- 카드 클릭 자체는 자동 기억이 아니다
- 조회 결과를 봤다는 사실만으로 sticker가 붙어선 안 된다

### selective sticker only

- 다시 의미 있다고 판단한 결과만 선택적으로 sticker 부착 가능하다
- 즉 조회 결과 중에서도 selective promotion을 다시 통과한 일부만 memory sticker가 될 수 있다

### distinction

- 탐색 흔적:
  step-by-step exploration 중 스쳐 지나간 경로
- 기억 스티커:
  다시 볼 가치가 있어 승격된 연결 표찰
- 유사 연결 조회 결과:
  특정 sticker seed를 기준으로 다시 드러난 유사 구조

이 셋은 같은 것이 아니다.

## 8. non-goals / anti-confusion

아래는 명시적으로 이 baseline 밖에 둔다.

- 전체 공간 한 번에 보기
- recommendation 면처럼 보이기
- 카드 클릭 자동 기억화
- 유사 연결을 곧바로 candidate/proposal로 승격
- 구현/스크립트 상세 설계를 baseline에 포함하기

추가 원칙:
- similar connection surface는 seed-based similarity reading 면이다
- search가 아니다
- graph view가 아니다
- recommendation 면이 아니다

## 9. naming candidates

이 페이지의 이름 후보는 아래 3개 이하로 남긴다.

1. `similar connection surface`
2. `connection resonance surface`
3. `seeded connection reading surface`

### final recommended name

- **`similar connection surface`**

이유:
- recommendation, search, graph view처럼 오해될 가능성이 가장 낮다
- 입력이 connection seed라는 점과, 페이지가 similarity reading 면이라는 점을 가장 직접적으로 드러낸다

## 10. lock / clarification decision

판정:
- **lock this as current baseline**

이유:
- 현재 필요한 것은 구현 세부가 아니라 페이지 역할과 비범위를 먼저 잠그는 일이다
- seed input, limited layout, similarity meaning, memory carryover를 지금 선명하게 고정해 두면 이후 whole-space-view drift와 recommendation-like misread를 막기 쉽다
- 현재 수준에서는 baseline 정의에 필요한 최소 명확성이 충분하다

## 11. if lock: rationale

### why lock now

- 지금 이 구조를 잠가야 이후 실제 구현이나 스크립트 논의가 와도 역할 혼용을 막을 수 있다
- 특히 “similarity reading surface”라는 정체성을 먼저 고정해야 exploration/search/recommendation/whole-space-view 쪽으로 새지 않는다
- seed가 object가 아니라 stickered connection path라는 점을 먼저 잠그는 것이 핵심이다

### upper interpretation rule

- 이후 실제 구현/스크립트 논의가 와도 이 문서의 정의를 상위 기준으로 써야 한다
- 즉 후속 논의는 먼저 아래 질문을 통과해야 한다
  - 이것이 seed-based similarity reading을 유지하는가
  - recommendation처럼 읽히지 않는가
  - whole-space-view로 커지지 않는가
  - automatic-memory drift를 만들지 않는가

## 12. if needs clarification: rationale

현재 판정은 lock이므로 아래는 적용하지 않는다.

### rationale

- not applicable

## 13. risk and correction record

### 이번 패키지에서 본 리스크

1. exploration/search confusion
- 이 페이지가 step-by-step exploration의 연장인지, direct access search인지 다시 섞여 읽힐 위험이 있었다

2. recommendation-like misread
- similarity 결과가 곧 추천이나 정답 제시처럼 보일 위험이 있었다

3. whole-space-view drift
- 내부 유사 연결 조회가 전체 공간 지도면으로 비대화될 위험이 있었다

4. automatic-memory drift
- 카드 클릭이나 조회 결과가 자동으로 기억화될 위험이 있었다

### 어떻게 통제했는가

- operating UI / exploration / search / memory sticker와의 구분을 각각 명시했다
- similarity를 recommendation이 아니라 reading aid로 고정하고, 순위화/정답추천/workflow를 바깥에 뒀다
- 최소 구조를 `left cards -> main similar structures -> deeper modal/detail`로 제한해 whole-space drift를 막았다
- memory rule carryover에서 click != memory, result != sticker를 분리해 automatic-memory drift를 차단했다

### working memory / log record

- broad package 수행 기준에서
  - similar connection surface = seed-based similarity reading surface
  - seed = stickered connection extraction path
  - click != memory
  - similarity != recommendation
  - main != whole-space view
  로 기록한다

## 14. alignment / memory record

- supervisor starting judgment:
  새 페이지는 유효하며, 탐색/검색/전체 공간 뷰와 구분되는 별도 면으로 먼저 잠가야 한다고 봤다
- codex own judgment:
  이 판단에 동의한다. 가장 흔들리기 쉬운 지점은 `similarity reading`이 recommendation이나 whole-space-view로 오해되는 경계라고 봤다
- disagreement or risk:
  seed를 object처럼 읽거나, similar structure를 graph-like total view처럼 읽으면 baseline이 바로 흐려질 위험이 있었다
- resolution:
  입력 단위를 stickered connection path로 잠그고, 이 페이지를 recommendation/search/whole-space-view와 분리된 seed-based similarity reading surface로 고정했다

## 15. recommendation

- 추천:
  **lock this as current baseline**

짧은 이유:
- 지금 이 페이지의 역할과 비범위를 먼저 잠가야 후속 구현 논의가 안전해진다
- 특히 seed input, similarity meaning, memory carryover, whole-space/recommendation 비범위를 baseline으로 먼저 고정하는 것이 우선이다
