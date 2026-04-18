# label_family_separation_contract_v1

## 1. Purpose
이 문서는 `vectorfl_replica` 전반에 이미 분산되어 존재하는 labeling 을
family 단위로 다시 구획하고,
`core input-layer labeler` 가 어디까지를 맡는지 잠그기 위한 최소 계약 문서다.

핵심 목적:
- labeling 이 이미 존재한다는 사실을 부정하지 않는다.
- 서로 다른 label family 를 섞어 읽지 않게 한다.
- `app/input_layer/labeler` 를 만능 label 계층이 아니라
  입력 정규화 중심 코어 슬롯으로 정의한다.

---

## 2. Top Declaration
- `vectorfl_replica` 에는 labeling 이 이미 존재한다.
- 다만 labeling 은 서로 다른 층에 분산되어 있다.
- `core input-layer labeler` 는 이 전체를 다 먹는 만능 계층이 아니다.
- 따라서 먼저 `label family separation contract` 로 경계를 잠그는 것이 맞다.

즉 현재 상태는 아래처럼 읽는다.
- `labeling exists`
- `core labeler is not yet consolidated`

---

## 3. Minimum Label Families

### FAMILY A — external routing labels
대표 예:
- `docrole`
- `runmode`
- `priority`

붙는 위치:
- structured doc 입력 진입부
- 문서 헤더
- routing parser 인접층

역할:
- 입력 의도 표현
- 문서 처리 방향 힌트 제공
- 라우팅 초기 조건 제공

중요:
- author-facing / domain-facing 표식층이다
- core input-layer labeler 의 전부가 아니다
- operation label 과 혼동하지 않는다

---

### FAMILY B — intake/core labels
대표 예:
- `input_class`
- `processing_profile`
- `material_grade`
- `role`
- `execution_linkable`

붙는 위치:
- intake
- registry
- internal normalization 층

역할:
- 엔진이 이 입력을 어떤 재료로 볼지 정한다
- 어떤 profile 로 처리할지 정한다
- 저장/처리/정규화의 내부 판독 축을 제공한다

중요:
- 이 family 가 `core input-layer labeler` 의 현재 중심 범위다
- external routing label 을 받아 내부 기준으로 정규화하는 축이다
- operation/event classification 과 분리한다

---

### FAMILY C — operation labels
대표 예:
- `ticket_class`
- `event_type`
- status operation 관련 분류값

붙는 위치:
- ticket registry
- event schema
- operation append / execution tracking 층

역할:
- 어떤 작업이 생성/추적되는지 나타낸다
- 실제 어떤 사건이 발생했는지 기록한다

중요:
- labeling 생태계에는 속하지만 core input-layer labeler 의 직접 범위는 아니다
- input label 과 operation label 을 혼동하지 않는다

---

### FAMILY D — meaning-side handles
대표 예:
- object anchors
- semantic rules
- structural rules

붙는 위치:
- anchorizer
- meaning handle 부착층

역할:
- fragment/input 에 의미 손잡이 부여
- object / semantic / structural 고정점 제공

중요:
- 순수 label 이라기보다 handle/anchor 성격이 강하다
- label family 와 인접하지만 별도 권위를 가진다
- core input-layer labeler 가 anchorizer 전체를 흡수한다고 쓰지 않는다

---

### FAMILY E — fragment / retrieval / grouping labels
현재 상태:
- 약하거나 미잠금
- future minimal slot

대표 예시:
- `fragment_group_label`
- `retrieval_label`
- `observer_group_label`
- `result_group_label`

붙는 위치:
- fragment-level explicit labeling layer
- observer/result surface 인접층

역할:
- fragment 묶음 / retrieval / group read 를 돕는다

중요:
- 현재는 약한 슬롯임을 명시한다
- 이미 완성된 것처럼 서술하지 않는다
- 다음 단계 후보이지만 이번 턴에서 구현하지 않는다

---

## 4. Core Input-Layer Labeler Definition

### Definition
`core input-layer labeler` 는
외부 입력 표식(`external routing labels`)과
엔진 내부 판독 메타(`intake/core labels`)를 연결하는
입력 정규화 중심 계층이다.

### What It Owns
- 입력 재료의 최소 내부 분류
- processing profile 정규화
- material-grade / input-class / intake role 부여
- 외부 표식값을 엔진 내부 기준으로 매핑

### What It Does Not Own
- event/ticket/status operation classification 전체
- anchor/semantic/structural handle 전체
- fragment retrieval/grouping label 완성형
- UI/view-level labeling
- ontology 확정 전체

중요:
- core input-layer labeler 를 labeling 전체와 동일시하지 않는다
- 그렇다고 cheap-tag helper 로 축소하지도 않는다

---

## 5. Prohibited Confusions
아래 혼동은 금지한다.

1. `docrole / runmode / priority` 를 operation label 로 혼동하지 않는다.
2. `ticket_class / event_type` 를 input-layer core label 로 혼동하지 않는다.
3. anchor / meaning handle 을 단순 label 로 축소하지 않는다.
4. fragment/retrieval label 의 미래 슬롯을 현재 완성형처럼 서술하지 않는다.
5. `labeling exists` 와 `core labeler exists` 를 동일 문장으로 쓰지 않는다.

---

## 6. Current Reading Rule
현재 `vectorfl_replica` 의 labeling 은 아래처럼 읽는 것이 맞다.

- FAMILY A 는 입력 진입 표식층
- FAMILY B 는 엔진 내부 intake/core 판독층
- FAMILY C 는 실행/사건 운영층
- FAMILY D 는 의미 손잡이/anchor 층
- FAMILY E 는 아직 약한 미래 슬롯

즉 지금 필요한 것은
새 label 을 더 만드는 것이 아니라,
이미 있는 label family 들을 먼저 섞이지 않게 읽는 것이다.

---

## 7. Current Practical Consequence
- 문서형 입력은 이미 routing labels 와 intake/core labels 를 함께 가진다
- operation layer 는 별도 classification 을 이미 가진다
- anchorizer 는 meaning-side handle 을 이미 가진다
- `app/input_layer/labeler` 는 이들 사이를 수렴시키는 core slot 이지만 아직 contract-first 상태다

---

## 8. One-Line Conclusion
현재 `vectorfl_replica` 에는 labeling 이 이미 존재하며, 이번 계약의 목적은 그것을 하나의 만능 label 계층으로 합치는 것이 아니라 family 단위로 구획해 `core input-layer labeler` 의 경계를 먼저 잠그는 것이다.
