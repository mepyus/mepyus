# row paragraph canonical anchor coverage check v1

## 0. why this check came first

- 이전 턴 일반화 검증에서 `transformer1`, `cnn`은 onboarding readiness와 active fragment generation은 통과했다.
- 그러나 `state-grounding_status`에서 value-side canonical binding이 공통으로 실패했다.
- 이때 바로 confidence threshold를 건드리면 원인을 가릴 수 없으므로,
  먼저 `grounding_status` row paragraph에 canonical anchor가 실제로 충분히 붙는지부터 비교했다.

즉 이번 턴의 질문은:

- `low confidence`가 주 병목인가
- 아니면 그 전에 `row paragraph canonical anchor coverage`가 비어 있는가

---

## 1. asset별 grounding_status reread 경로 비교

비교 대상:

- `choi_ai_classroom_vlm`
- `choi_ai_classroom_transformer1`
- `choi_ai_classroom_cnn`

기준 row:

- `grounding_status`

### 1-1. choi_ai_classroom_vlm

- source_file:
  - `inputs/external_cases/choi_ai_classroom_vlm.txt`
- paragraph retrieval:
  - `lines 415-416 @ 22:10`
  - `네거티브하고 파지티브로 이렇게 막 비교하는 이런 대조 학습이 어 레이블 없이 이제 하게 됩니다. 아까는`
- reread confidence:
  - `high`
- fragment anchor:
  - `semantic.contrastive_learning`
- fragment anchors:
  - `semantic.contrastive_learning`
- scene / flow:
  - `comparison / contract`
- result:
  - value-side canonical binding 성립

### 1-2. choi_ai_classroom_transformer1

- source_file:
  - `inputs/external_cases/choi_ai_classroom_transformer1.txt`
- paragraph retrieval:
  - `lines 1-2 @ 0:08`
  - `네, 오늘 다섯 번째 강의고요. 어, 트랜스포머에 대해서`
- reread confidence:
  - `low`
- fragment anchor:
  - `None`
- fragment anchors:
  - `[]`
- scene / flow:
  - `comparison / contract`
- result:
  - paragraph 복귀는 됐지만 value-side canonical binding 실패

### 1-3. choi_ai_classroom_cnn

- source_file:
  - `inputs/external_cases/choi_ai_classroom_cnn.txt`
- paragraph retrieval:
  - `lines 69-70 @ 3:49`
  - `어, 결국은 다 똑같이 어, 폭포죠. 그렇죠? 똑같이 레이블은 폭포라고 할 수 있고 분류도 폭포로 해야 되죠.`
- reread confidence:
  - `low`
- fragment anchor:
  - `None`
- fragment anchors:
  - `[]`
- scene / flow:
  - `comparison / contract`
- result:
  - paragraph 복귀는 됐지만 value-side canonical binding 실패

---

## 2. vlm 대비 transformer1/cnn 차이

가장 중요한 차이:

1. `VLM`
   - row paragraph에 `네거티브 / 파지티브 / 레이블 없이`가 실제로 있다.
   - 현재 anchorizer semantic rule이 이 단락에 직접 걸린다.
   - 그래서:
     - row paragraph retrieval
     - canonical anchor attachment
     - canonical binding
     가 한 번에 닫힌다.

2. `transformer1`
   - grounding_status로 선택된 paragraph가 `트랜스포머 소개 문장`으로 떨어진다.
   - row lexicon(`레이블`, `파지티브`, `네거티브`, `기준에 따라서`) hit가 없다.
   - anchorizer도 붙일 anchor가 없다.

3. `cnn`
   - grounding_status paragraph는 `레이블은 폭포`라는 분류 설명으로 잡히긴 한다.
   - 하지만 현재 anchorizer rule에는 `레이블`만 있고,
     `분류/분류도/폭포 같은 같은-class 분류 문맥`을 canonical semantic으로 올리는 rule이 없다.
   - 그래서 anchor가 비어 있다.

즉 차이는 단순히 confidence 수치보다 앞선다.

- `vlm`은 row paragraph 자체가 canonicalizable 하다.
- `transformer1/cnn`은 row paragraph가 canonicalizable하지 않거나, 현재 canonical rule coverage 바깥에 있다.

---

## 3. canonical anchor coverage 부족 양상

### 3-1. row가 참조 가능한 paragraph 후보 수

- 세 asset 모두 `grounding_status -> paragraph` 복귀 자체는 된다.
- 즉 “paragraph를 못 찾는다”가 1차 문제는 아니다.

### 3-2. paragraph 후보의 canonical anchor quality

- `vlm`
  - strong
  - paragraph 자체가 semantic rule과 직접 맞물린다.
- `transformer1`
  - none
  - 선택된 paragraph가 row semantics와 거의 닿지 않는다.
- `cnn`
  - weak-to-none
  - paragraph는 `레이블/분류` 문맥이지만, 현재 canonical semantic rule coverage에는 안 잡힌다.

### 3-3. row label / scene / flow와 paragraph의 정합성

- 세 asset 모두 fragment에는 `scene=comparison`, `flow=contract`가 붙는다.
- 그러나 `transformer1/cnn`에서는 이 축값이 paragraph anchor와 실제로 닿지 않는다.
- 즉 scene/flow는 있어도 value-side canonical key를 일으키는 anchor가 없다.

### 3-4. coverage 부족의 성격

- `transformer1`
  - anchor가 약한 것이 아니라,
  - 현재 row retrieval 자체가 row semantics와 다른 paragraph를 고른다.
- `cnn`
  - paragraph는 비교적 row semantics와 닿지만,
  - canonical anchor rule coverage가 부족하다.

즉 두 자산 모두 low confidence이긴 하지만,
그 low confidence 앞단에서 드러나는 failure surface는 다르다.

---

## 4. 최소 보강 후보

이번 턴에서는 수정하지 않고, 가장 작은 보강 후보만 추렸다.

### 후보 1. grounding_status row paragraph canonical semantic coverage 보강

- 대상:
  - `cnn`
- 이유:
  - 현재 paragraph는 `레이블`, `분류`, 같은-class classification 문맥을 갖는다.
  - 이건 `contrastive_learning`은 아니더라도 별도 grounding/classification semantic으로 canonicalize할 여지가 있다.
- 의미:
  - anchor coverage가 넓어지면 value-side canonical binding 실패가 줄어드는지 가장 직접적으로 볼 수 있다.

### 후보 2. grounding_status row retrieval lexicon 보강

- 대상:
  - `transformer1`
- 이유:
  - 지금은 row paragraph 선택이 너무 앞 문장으로 떨어져 row semantics와 안 맞는다.
  - 즉 여기선 anchorizer보다 먼저 retrieval lexicon이 맞는 paragraph를 고르게 해야 한다.

---

## 5. 주 병목 판정

- 판정:
  - **주 병목은 우선 canonical anchor coverage 부족이 맞다.**
  - 다만 asset에 따라 형태가 다르다.

세부 판정:

1. `vlm`
   - canonical anchor coverage가 충분해서 canonical binding까지 닫힌다.

2. `cnn`
   - paragraph 복귀는 됐다.
   - 하지만 paragraph가 canonical semantic으로 번역되지 않는다.
   - 이 경우는 `anchor coverage 부족`이 직접 병목이다.

3. `transformer1`
   - paragraph 복귀는 됐지만 row semantics와 무관한 앞 문장으로 떨어진다.
   - 여기서는 `retrieval mismatch`가 더 직접적인 병목이다.
   - 하지만 그 결과도 결국 value-side canonical anchor가 0개라는 동일 failure surface로 나타난다.

종합하면:

- 지금 단계에서 confidence scoring은 결과 지표에 가깝다.
- 먼저 다져야 할 것은
  1. target row가 semantic적으로 맞는 paragraph를 고르게 하는 것
  2. 그 paragraph를 canonical anchor로 붙잡는 coverage
이다.

즉 다음 순서는:

- confidence 조정
  가 아니라
- `row retrieval + row paragraph canonical anchor coverage`
  검증/보강
이 맞다.

---

## 6. 다음 supervisor 지시를 위한 메모

이번 턴에서 확인된 것:

- 왜 coverage를 먼저 의심했는지:
  - paragraph 복귀는 되는데 canonical binding이 안 닫혔기 때문이다.
- `vlm`과 비교해 본 차이:
  - `vlm`은 target row paragraph가 canonicalizable했다.
  - `transformer1/cnn`은 그렇지 않았다.
- 왜 다음 턴이 confidence 조정보다 coverage 검증으로 좁혀졌는지:
  - 현재 `low confidence`는 원인이라기보다 결과에 더 가깝다.
  - canonical anchor가 없는 paragraph를 confidence만 높여도 binding은 닫히지 않는다.

다음 턴에서 먼저 좁힐 질문:

1. `cnn grounding_status` paragraph를 canonical semantic으로 붙잡을 최소 anchor coverage 보강이 가능한가?
2. `transformer1 grounding_status`는 retrieval lexicon을 바꾸면 row semantics에 맞는 paragraph가 실제로 나오는가?

---

## 7. one-line summary

> grounding_status 계열 value-side canonical binding 실패의 주 병목은 지금 단계에서 confidence threshold 자체보다, row가 실제로 canonicalizable paragraph를 잡고 있는지와 그 paragraph에 충분한 canonical anchor coverage가 붙는지의 문제로 보는 것이 더 정확하다.
