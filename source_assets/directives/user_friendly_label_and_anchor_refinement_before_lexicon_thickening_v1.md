[[A]] [[OBJ:codex_directive_user_friendly_label_and_anchor_refinement_before_lexicon_thickening_v1]] [[SEM:bounded_internal_refinement_user_friendly_labels_anchors_before_dictionary_memory_thickening]]

# CODEx 지시서 — 사용자 친화적 라벨/앵커 미세수정 선행, 축값 고정, 사전류 투입은 후행

## 0. 목적

이번 턴의 목적은 엔진 전체 구조를 다시 짜는 것이 아니다.

또한 이번 턴의 목적은
- 축값 체계를 새로 정의하는 것
- scene/flow/role 축을 크게 뜯는 것
- core engine을 수정하는 것
- 미래/연결/온톨로지 같은 특정 사례를 일반 법칙으로 승격하는 것
도 아니다.

이번 턴의 목적은 오직 하나다.

> **이미 잠근 `connection_meaning_and_user_layer_translation_baseline_v1`를 기준으로,
> 엔진 내부 출력이 사용자 질문의 의미 층위를 더 잘 열 수 있도록
> 축값은 건드리지 않고, 라벨과 앵커를 사용자 친화적인 방향으로 bounded하게 미세조정하는 것**

즉 이번 작업은
“엔진의 내부 언어를 더 예쁘게 만들기”
가 아니라,

**사용자가 실제로 탐색하는 의미 층위와 더 가까운 표면으로
라벨/앵커 출력면을 조율하는 초기 세팅**
이다.

---

## 1. 최상위 전제

이미 잠근 기준선은 아래다.

- `source_assets/baselines/connection_meaning_and_user_layer_translation_baseline_v1.md`

앞으로 모든 refinement는 먼저 이 baseline을 통과해야 한다.

즉 이번 수정도 아래 원칙을 따른다.

- 연결은 공출현이 아니라 **의미 운동**으로 읽는다
- 층위는 engine label 이름이 아니라 **사용자 질문의 펼쳐짐**으로 읽는다
- refinement는 출력 품질 문제만이 아니라 **사용자 층위 번역 문제**로 본다
- 내부 수정은 “이번 결과 패치”가 아니라 **멀리 가기 위한 준비**여야 한다

---

## 2. 이번 턴의 해석

현재까지 확인한 것은 아래다.

- 분절은 된다
- 응결핵도 어느 정도 보인다
- 특정 상위 개념 축에서 다층 분포가 반복적으로 보인다
- 하지만 출력 표면은 아직 엔진 내부 언어가 강하다
- 사용자가 바로 이해하는 층위 언어와는 간극이 남아 있다

이 간극을 당장 축값 변경으로 해결하려 하면 안 된다.

왜냐하면 지금은 아직
- 일반화 잠금 전
- 반복 체득 단계
- 사용자 친화 표면 조율 단계
이기 때문이다.

따라서 이번 턴은
**축값 고정 상태에서 라벨/앵커 표면만 사용자 친화적으로 다듬는 초기 정렬 작업**
으로 제한한다.

---

## 3. 이번 턴에서 수정하는 것

## 3-1. 수정 대상
이번 턴에서 수정 가능한 범위는 아래다.

- 라벨 표면 표현
- 앵커 표면 표현
- 앵커 분류 기준 일부
- residue 분리 기준 일부
- 출력 packet/report에서의 사용자 친화적 요약층

## 3-2. 수정 불가 대상
다음은 이번 턴에서 건드리지 않는다.

- 축값 정의 자체
- scene/flow 본체 체계
- core engine
- baseline
- current shared reality
- promotion logic
- generalized ontology화
- 대규모 구조 재설계
- 사용자 질문 의미층 전체 taxonomy 확정

즉:
**이번 턴은 label/anchor surface refinement이지, axis refactor가 아니다.**

---

## 4. 이번 턴의 핵심 방향

이번 수정은 아래 방향으로만 진행한다.

### 방향 A — engine label을 사용자 해석 보조 라벨로 번역
예:
- `review` -> 설명/해석 층
- `impl` -> 구현/실행 층
- `evidence` -> 근거/검증 층
- `spec` -> 규칙/형식/명세 힌트 층
- `compare` -> 비교/해석 흐름
- `run` -> 작동/실행 흐름

중요:
기존 axis value는 바꾸지 않는다.
다만 **사용자에게 보여주는 해석 표면을 더 친화적으로 조정**한다.

### 방향 B — topic-bearing anchor를 더 위로, discourse/speaker residue는 더 아래로
앞으로는 최소 아래처럼 더 분리해서 다룬다.

- topic-bearing anchor
- user-layer hint anchor
- discourse residue
- speaker/source residue

즉
`AGI`, `자동화`, `온톨로지`, `그래프`, `안보`, `검증`
같은 것은 위로 올리고,

`그래서`, `우리가`, 화자 이름, 발화 습관성 연결어`
같은 것은 중심 경쟁에서 약화시킨다.

### 방향 C — 출력을 “엔진 분류 결과”가 아니라 “사용자 질문을 여는 실마리”로 보이게 한다
수치 보고 이전에 **의미 층위 열림**이 먼저 보이게 한다.

---

## 5. 운영 잠금

- 이번 턴의 포인트는 axis 수정이 아니다
- 라벨/앵커를 사용자 친화적으로 조율하는 초기 세팅이다
- refinement는 baseline을 먼저 통과해야 한다
- 결과는 “내부 언어 정리”보다 “사용자 층위 열림”으로 평가한다
- 사전류 강화는 후행이다

---

## 6. 한 줄 최종 잠금

> **이번 수정은 axis refactor가 아니라, connection meaning / user-layer translation baseline을 기준으로 label과 anchor를 사용자 친화적인 표면으로 bounded하게 미세조정하는 초기 세팅이며, 사전류를 통한 기억 두께 강화는 공간 형성 이후의 후행 단계로 둔다.**
