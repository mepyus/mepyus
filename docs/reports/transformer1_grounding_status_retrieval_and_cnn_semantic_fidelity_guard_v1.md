# transformer1_grounding_status_retrieval_and_cnn_semantic_fidelity_guard_v1

## 1. transformer1 현재 mismatch 상태

이번 턴에서 `transformer1`을 retrieval lexicon 검증 대상으로 잡은 이유는,
지난 비교에서 이 자산의 `grounding_status`는 `cnn`과 달리 paragraph-side canonical semantic coverage를 보기 전에
먼저 row가 어떤 paragraph를 잡는지가 더 불안정해 보였기 때문이다.

보강 전 기준 상태:

- asset: `choi_ai_classroom_transformer1`
- target row: `grounding_status`
- row label: `partially grounded`
- retrieval result:
  - `paragraph_ref = lines 591-592 @ 31:17`
  - `paragraph_text = 통과시켜 가지고 뭐 분류하거나 회기시키는 겁니다. 그 문장을 가지고 뭐 분류를 한다 그러면이 문장이 뭐`
  - `match_score = 1`
  - `match_confidence = low`
- active row fragment:
  - `anchor = None`
  - `anchors = []`

왜 retrieval mismatch로 봤는가:

- 이 문단은 generic sentence classification / regression 설명에 가깝다.
- `grounding_status`가 기대하는 “output grounding” 또는 “무엇을 기준으로 결과를 읽는가”와 아주 멀진 않지만,
  `transformer1` 문맥 안에서는 더 직접적인 paragraph 후보가 따로 있었다.
- 실제로 같은 문서 안에:
  - `클래스 토큰으로부터 나온 걸 가지고 이미지 분류`
  같은 더 target-like paragraph가 존재했다.

즉 `transformer1`의 문제는 “아예 paragraph를 못 찾는다”보다,
`row semantics를 더 직접적으로 담은 paragraph를 아직 못 고른다` 쪽에 가까웠다.

## 2. transformer1 최소 lexicon 검증 결과

이번 턴에서는 broad retrieval redesign 없이,
`grounding_status` row lexicon에 `클래스 토큰`만 최소 추가했다.

수정 이유:

- `transformer1` 문서 안에서 실제로 더 적절한 paragraph가
  `클래스 토큰 -> 이미지 분류`
  문맥에 있었다.
- 이건 row semantics와 paragraph semantics를 더 직접적으로 잇는 가장 작은 alias였다.

적용 후 retrieval 결과:

- `paragraph_ref = lines 691-692 @ 36:33`
- `paragraph_text = 보통 이제 비전 트랜스포머에 보면은 예요 클래스 토큰으로부터 나온 걸 가지고 이미지 분류를 보통 하죠.네`
- `match_score = 2`
- `match_confidence = medium`

즉 lexicon 1개 보강만으로:

- before: generic sentence classification paragraph
- after: class token -> image classification paragraph

로 이동했다.

이후 상태:

- value-side paragraph reread는 이제 surface/save guard를 통과할 수 있다.
- 하지만 rebuilt fragment는 여전히
  - `anchor=None`
  - `anchors=[]`
  상태였다.
- save 결과도 여전히:
  - `primary_rule_key = semantic.row.grounding_status`
  - `binding_source = first_pass_canonical`
  에 머물렀다.

따라서 `transformer1`의 주 병목 판정은 다음과 같다.

1. 1차 병목
- retrieval lexicon 부족이 맞다.
- 적절한 paragraph로 옮겨가는 데 실제 효과가 있었다.

2. 다음 병목
- paragraph-side canonical semantic mapping 부족
- 즉 retrieval만 고치면 끝나는 건 아니고, 그 다음 바로 semantic coverage 부족이 드러난다.

## 3. cnn semantic fidelity guard 결과

이번 턴에서는 `cnn`의 성공도 다시 점검했다.

현재 `cnn grounding_status` 저장 상태:

- row label: `partially grounded`
- paragraph:
  - `어, 결국은 다 똑같이 어, 폭포죠. 그렇죠? 똑같이 레이블은 폭포라고 할 수 있고 분류도 폭포로 해야 되죠.`
- closure:
  - `primary_rule_key = semantic.label_classification`
  - `binding_source = first_pass_canonical`
  - `scene = comparison`
  - `flow = contract`

guard 질문에 대한 판정:

### 3-1. 이 closure가 grounding_status 의미를 실제로 포착하는가?

- `부분적으로는 yes`
- 이 paragraph는 분명히 `레이블 / 분류`를 통해 output이 어떻게 grounded되는지를 말한다.
- 즉 completely empty closure는 아니다.

### 3-2. 다른 의미 bucket으로 우회 closure된 것은 아닌가?

- `부분적으로는 yes`
- `grounding_status`의 의미를 매우 좁게 `label classification` 쪽으로 당겨서 닫은 면이 있다.
- `vlm`의 `semantic.contrastive_learning`처럼 row semantics와 더 직접적/풍부하게 맞물린 closure보다는 좁다.

### 3-3. output/read unit으로 쓸 때 어색함은 없는가?

- 완전히 어색하진 않다.
- 다만 row label이 `partially grounded`인데 saved binding은 `semantic.label_classification`으로 닫히므로,
  나중에 이 row를 일반 규칙으로 올릴 때는 `grounding_status = label classification`으로 과잉 고정될 위험이 있다.

### 3-4. “값은 맞는데 문장은 비는” 상태인가?

- `no`
- 문장은 실제로 채워져 있고, paragraph도 label/classification grounding 문맥을 담고 있다.
- 문제는 “빈 closure”가 아니라 “다소 좁은 semantic closure”다.

cnn 성공 케이스 판정:

- `구조적으로는 성공했지만 semantic drift 주의가 필요한 성공`

## 4. 두 자산 비교 판정

공통점:

- 둘 다 `source_file + canonicalStateRows`를 가진다.
- 둘 다 최소 alias 보강만으로 row reread 품질은 올라갈 수 있다.

차이:

- `cnn`
  - retrieval은 이미 비교적 맞았고
  - coverage 보강으로 canonical semantic까지 닫혔다
  - 하지만 semantic fidelity는 약간 좁은 성공이다
- `transformer1`
  - 이번 턴에서 retrieval은 더 맞는 paragraph로 옮겨갔다
  - 그러나 canonical semantic mapping은 여전히 비어 있다

즉 두 자산을 합치면:

- `retrieval`과 `semantic closure`는 별개 병목이다
- `cnn`은 coverage-first 사례
- `transformer1`은 retrieval-first 후 semantic-second 사례

## 5. 현재 기관 수준 판정

- 판정: `특정 조건부 기관으로 볼 수 있음`

이유:

- `choi_ai_classroom_vlm`: retrieval + semantic fidelity 둘 다 상대적으로 양호
- `choi_ai_classroom_cnn`: 구조적 closure는 성공했지만 semantic drift 주의 필요
- `choi_ai_classroom_transformer1`: retrieval은 개선됐지만 canonical semantic mapping이 아직 비어 있음

즉 canonical onboarding은 더 이상 lucky case는 아니다.
하지만 아직 “일반 기관 직전”이라고 보기에는

- asset별 병목 위치가 다르고
- semantic fidelity guard가 아직 필요하다.

현재 상태는:

- `조건부 기관`
- 또는 더 엄격히 말하면 `partial institution with asset-sensitive bottlenecks`

## 6. 다음 supervisor 지시를 위한 메모

이번 턴에서 확인된 다음 우선순위는 두 갈래다.

1. `transformer1 grounding_status` paragraph-side semantic mapping 최소 보강 검증
- retrieval은 이번 턴에서 더 직접적인 paragraph로 이동했다
- 따라서 다음 병목은 semantic coverage인지 실제로 검증할 수 있다

2. `cnn semantic fidelity guard`를 다른 성공 케이스에도 붙여 비교
- 앞으로는 `닫힘`과 `의미 충실도`를 계속 분리해서 봐야 한다
- 그렇지 않으면 metric closure를 institution success로 과대 판정할 위험이 있다

이번 턴이 왜 다음을 이렇게 좁히는가:

- `transformer1`은 이제 retrieval 병목만 탓할 수 없는 단계까지 왔다
- `cnn`은 성공했지만, semantic drift 방어 없이 일반화 승격으로 가기엔 아직 이르다

따라서 다음 supervisor 지시는
`transformer1 semantic mapping 보강 검증`
또는
`cnn/vlm semantic fidelity comparative guard`
중 하나로 좁히는 게 맞다.
