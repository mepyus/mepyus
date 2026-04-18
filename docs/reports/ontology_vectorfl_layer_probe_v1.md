# ontology_vectorfl_layer_probe_v1.md

## 1. probe condition

- method: engine-internal segment probe only
- interpretation rule: manual frame fixing 없음
- target phrase family:
  - 객체
  - 연결
  - 온톨로지
  - 벡터플
  - vectorfl
  - ontology
  - 그래프
  - 노드
  - 엣지
  - 메타온톨로지
- source scope: `inputs/external_cases/*`
- generated probe:
  - `app/work/archive_review/probe_support/concept_segment_probe/generated/ontology_vectorfl_layer_probe_v1_20260327T234948Z.json`

---

## 2. top-level result

- matched source count: 24
- overall scene counts:
  - review: 387
  - impl: 33
  - evidence: 13
  - spec: 10
- overall flow counts:
  - compare: 360
  - run: 76
  - break: 5
  - fix: 2

즉 이 축은 한 층으로만 읽히지 않는다.

기본적으로는 `review / compare` 비중이 가장 크지만,
이미 그 위에
- `impl / run`
- `evidence / run`
- `spec`

층이 얇게 겹쳐 있다.

---

## 3. source concentration

상위 source는 아래에 집중된다.

### source A
- path: `inputs/external_cases/saltlux.txt`
- matched segments: 119
- scene mix:
  - review 109
  - spec 5
  - impl 5
- flow mix:
  - compare 103
  - run 14
- reading:
  - 온톨로지 자체를 설명하고 결합/변환/표현 체계를 말하는 review 중심 층이 가장 두껍다

### source B
- path: `inputs/external_cases/ontology_youtube.txt`
- matched segments: 116
- scene mix:
  - review 110
  - evidence 5
  - impl 1
- flow mix:
  - compare 107
  - run 8
  - fix 1
- reading:
  - 온톨로지와 연결을 가장 직접적으로 말하지만, 엔진 내부 분절 기준으로는 여전히 review/explanatory 층이 압도적이다

### source C
- path: `inputs/external_cases/graphrag_neosh.txt`
- matched segments: 79
- scene mix:
  - review 53
  - impl 21
  - evidence 3
  - spec 2
- flow mix:
  - compare 45
  - run 34
- reading:
  - ontology 어휘는 약하지만 graph / retrieval / implementation 층을 통해 `연결 구조` 쪽 실행면을 가장 강하게 끌어올린다

### source D
- path: `inputs/external_cases/saltlux_ai.txt`
- matched segments: 49
- scene mix:
  - review 47
  - impl 2
- flow mix:
  - compare 40
  - run 7

### source E
- path: `inputs/external_cases/saltlux_ai_summary.txt`
- matched segments: 6
- scene mix:
  - review 5
  - impl 1
- flow mix:
  - compare 4
  - run 1

---

## 4. layer reading

이번 probe에서 `"객체의 연결을 온톨로지스럽지 않고 벡터플 스럽게"` 와 닿는 층위는 아래처럼 읽힌다.

### layer 1. explanatory review layer
- 가장 두껍다
- `온톨로지`, `그래프`, `연결이`, `데이터`, `온톨로지를` 같은 anchor가 이 층을 만든다
- 의미:
  - 객체 연결을 개념/설명/해석 차원에서 다루는 층

### layer 2. implementation / run layer
- 얇지만 분명히 있다
- 특히 `graphrag_neosh.txt` 쪽이 강하다
- 의미:
  - 연결을 실제 검색/리트리버/구현 흐름으로 옮기는 층

### layer 3. evidence layer
- 두껍지는 않지만 존재한다
- `ontology_youtube.txt`, `graphrag_neosh.txt`, 일부 다른 문서에서 나온다
- 의미:
  - 연결 구조를 주장만이 아니라 검증/사례/근거 쪽으로 붙이는 층

### layer 4. spec hint layer
- 매우 얇다
- `saltlux.txt`, `graphrag_neosh.txt`, 일부 md에서만 보인다
- 의미:
  - 연결 구조를 규칙/체계/표현 형식 쪽으로 밀어 넣는 층

---

## 5. what this means

이번 probe는 연결의 단단함을 본 것이 아니다.

대신 아래를 확인했다.

- 이 문장 계열은 엔진 내부에서 단순 철학 문장 한 덩어리로만 읽히지 않는다
- `온톨로지/그래프/연결` 관련 분절값은 이미
  - 설명층
  - 구현층
  - 근거층
  - 얇은 명세층
  으로 분포한다
- 다만 중심은 아직 명확히 `review / compare` 쪽이다
- 따라서 지금 상태를
  - 단단한 구조 연결
  로 읽기보다는
  - 다층 분포가 이미 생겨 있으나 실행/명세 쪽은 아직 얇다
  로 읽는 편이 맞다

---

## 6. caution

- 이번 결과는 engine-internal segment probe 결과다
- 내가 먼저 frame을 고정한 결과가 아니다
- `벡터플` 자체 어휘는 external cases 안에서는 강하지 않고,
  실제 분포는 `온톨로지 / 그래프 / 연결 / 구현` 쪽 source가 대리 구성한다
- 따라서 지금 단계에서 “벡터플 방식의 연결 구조가 이미 확정됐다”라고 읽으면 과하다

---

## 7. one-line lock

- `"객체의 연결을 온톨로지스럽지 않고 벡터플 스럽게"` 와 닿는 엔진 내부 층위는 이미 다층 분포를 보이지만, 현재 중심은 여전히 explanatory review layer이고 implementation/spec layer는 얇게 보조하는 상태다.
