# Issue Root Classifier v0

## 목적

이 문서는 새 `issue-root` 또는 입력 신호가 들어왔을 때
처음으로 어느 family / projection / route로 보내야 하는지 정하는
최소 classifier 규칙을 고정한다.

지금까지는 아래까지 있었다.

- bounded space
- upper family layer
- family invariant
- projection registry
- route registry
- route selection policy

이제 필요한 것은
처음 들어온 signal을 이 스택 어디로 태울지 정하는 입구 규칙이다.

## classifier의 역할

classifier는 아래를 한다.

1. incoming issue-root signal을 읽는다
2. 가장 맞는 `family_id` 를 고른다
3. 그 family 안의 첫 `projection_id` 를 고른다
4. 그 projection이 선호하는 `initial_route_id` 를 고른다
5. 애매하면 fallback family 또는 review 필요 상태로 둔다

즉 classifier는 완성된 해석기가 아니라
첫 진입점을 정하는 `entry router` 다.

## 최소 입력 필드

- `issue_id`
- `issue_title`
- `issue_summary`
- `signal_kind`
- `scope_objects`
- `requested_outcome`
- `operator_query`
- `current_artifacts`

`signal_kind` 예:

- `raw_input`
- `preprocess_ambiguity`
- `transition_blockage`
- `boundary_ambiguity`
- `operator_overview_request`
- `operator_search_query`

## 최소 출력 필드

- `classification_id`
- `issue_id`
- `selected_family_id`
- `selected_projection_id`
- `initial_route_id`
- `confidence`
- `classification_reason`
- `fallback_family_ids`
- `needs_review`

## 판단 규칙

### rule 1. family를 먼저 고른다

route나 projection을 먼저 고르지 않는다.

순서:

1. family
2. projection
3. route

### rule 2. signal_kind와 requested_outcome을 같이 본다

같은 raw signal이라도
원하는 결과가 다르면 다른 family로 갈 수 있다.

예:

- 같은 transition evidence라도
  blockage explanation이면 `fam_transition_thickening`
  operator summary면 `fam_operator_readout`

### rule 3. issue_title보다 current_artifacts가 더 강할 수 있다

표면 제목보다
실제 붙어 있는 artifact나 상태면이
더 강한 classification 신호가 될 수 있다.

### rule 4. 애매하면 review를 남기고 narrower family를 무리하게 선택하지 않는다

v0에서는 과감한 오분류보다
`needs_review=true`가 낫다.

## family별 v0 진입 규칙

## 1. fam_input_to_reading

아래 신호가 강하면 우선 선택한다.

- `signal_kind` 가 `raw_input`
- `signal_kind` 가 `preprocess_ambiguity`
- current artifact가 transcript, note, memo, article 같은 entry material
- requested outcome이 readable entry, split, preprocess 판단에 가까움

projection 우선순위:

1. `proj_preprocess_shaping`
   - raw transcript too noisy
   - uncertain-needs-probe
   - preprocess necessity ambiguity
2. `proj_input_ingest_visibility`
   - direct ingest viable
   - split-first entry 가능

## 2. fam_transition_thickening

아래 신호가 강하면 우선 선택한다.

- `signal_kind` 가 `transition_blockage`
- `signal_kind` 가 `boundary_ambiguity`
- current artifact에 phase decision, latent line, corridor report가 있음
- requested outcome이 blockage explanation, thickening/closure 판단에 가까움

projection 우선순위:

1. `proj_transition_preflight_reread`
   - active latent line
   - phase signal reread 필요
2. `proj_transition_corridor_validation`
   - staged lineage
   - boundary narrowing 필요
3. `proj_transition_operator_readout`
   - transition 결과를 바로 operator-facing 설명으로 보여줘야 할 때

## 3. fam_operator_readout

아래 신호가 강하면 우선 선택한다.

- `signal_kind` 가 `operator_overview_request`
- `signal_kind` 가 `operator_search_query`
- current artifact에 engine_state_latest, update events, readout payload가 있음
- requested outcome이 broad overview, detail readout, search answer에 가까움

projection 우선순위:

1. `proj_operator_board_readout`
   - overview first
   - state board needed
2. `proj_operator_search_readout`
   - explicit query
   - search route needed

## cross-family override 규칙

### 1. transition evidence with readout request

transition artifact가 있어도
requested outcome이 명백히 operator-facing explanation이면

- family는 `fam_transition_thickening`
- projection은 `proj_transition_operator_readout`

로 들어가게 한다.

즉 family root는 transition에 두고,
projection에서 readout을 선택한다.

### 2. input evidence with blockage request

raw input artifact가 있어도
질문이 “왜 지금 막혔는가” 쪽이면
입력 family에 머물지 않고
`fam_transition_thickening` 검토를 우선한다.

### 3. operator overview is not a preprocessing task

입력 artifact가 같이 있어도
요청이 broad overview이면
`fam_operator_readout`을 우선한다.

## v0 classifier output 예시

```json
{
  "classification_id": "cls_20260406_001",
  "issue_id": "issue_001",
  "selected_family_id": "fam_input_to_reading",
  "selected_projection_id": "proj_preprocess_shaping",
  "initial_route_id": "route_preprocess_compare_first",
  "confidence": "medium",
  "classification_reason": [
    "signal_kind=preprocess_ambiguity",
    "current artifact is noisy transcript",
    "requested outcome is preprocess judgment"
  ],
  "fallback_family_ids": [
    "fam_transition_thickening"
  ],
  "needs_review": false
}
```

## 현재 한계

### 1. classifier는 아직 rule-based 문서 수준이다

자동 분류기라기보다
entry routing contract에 가깝다.

### 2. signal normalization이 아직 없다

`signal_kind` 를 더 체계적으로 정리할 필요가 있다.

### 3. confidence도 정량화되지 않았다

v0에서는 `low/medium/high` 정도로만 충분하다.

## 현재 결론

이 classifier가 생기면
지금 구조는 처음 issue-root가 들어오는 순간부터
어느 family / projection / route로 타야 하는지 말할 수 있게 된다.

즉 스택은 아래로 닫힌다.

- issue-root
- family
- projection
- route
- route selection
