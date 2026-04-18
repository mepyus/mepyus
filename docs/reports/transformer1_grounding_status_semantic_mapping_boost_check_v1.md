# transformer1_grounding_status_semantic_mapping_boost_check_v1

## 1. transformer1 현재 paragraph-side semantic mapping 상태

이번 턴에서 `transformer1 grounding_status`를 semantic mapping 검증 대상으로 본 이유는,
지난 턴에 retrieval lexicon 최소 보강만으로 paragraph가 이미 더 직접적인 후보로 옮겨갔기 때문이다.

고정된 현재 상태는 다음과 같았다.

- row:
  - `key=grounding_status`
  - `label=partially grounded`
- current paragraph:
  - `lines 691-692 @ 36:33`
  - `보통 이제 비전 트랜스포머에 보면은 예요 클래스 토큰으로부터 나온 걸 가지고 이미지 분류를 보통 하죠.네`
- reread:
  - `match_score=2`
  - `match_confidence=medium`
- fragment state:
  - `anchor=None`
  - `anchors=[]`
- save state:
  - `primary_rule_key=semantic.row.grounding_status`

즉 retrieval은 이제 충분히 더 직접적인 paragraph에 닿았는데,
그 paragraph를 canonical semantic으로 올릴 rule이 없어 canonicalization에서 멈춘 상태였다.

왜 semantic mapping 부재로 보는가:

- 현재 paragraph는 `클래스 토큰`, `이미지 분류`라는 강한 semantic signal을 갖는다.
- 하지만 기존 semantic rules에는 이 문구와 바로 맞물리는 canonical key가 없었다.
- 따라서 이 단계의 다음 병목은 confidence가 아니라 paragraph-side semantic mapping으로 보는 것이 타당했다.

## 2. 최소 보강 후보와 선정 이유

이번 턴에서 선택한 최소 보강은 1개 semantic rule 추가다.

파일:
- `app/input_layer/anchorizer/anchorizer.py`

추가한 canonical semantic:
- `semantic.class_token_classification`

증거 문구:
- `클래스 토큰`
- `이미지 분류`

선정 이유:

- retrieval은 이미 `클래스 토큰 -> 이미지 분류` 문단으로 옮겨가 있었다.
- 이 문단을 canonical semantic에 닿게 하는 가장 작은 paragraph-side mapping은
  문단이 실제로 말하는 메커니즘을 그대로 쓰는 것이다.
- `cnn`처럼 더 넓은 `label classification` bucket으로 덮는 것보다,
  이번 자산의 문단 의미를 더 직접적으로 반영한다.

이번 턴에서 하지 않은 것:

- threshold 조정
- retrieval lexicon 추가 확장
- broad taxonomy/schema 변경

## 3. 적용 결과

### 3-1. rebuilt fragment 변화

보강 후 rebuilt row fragment:

- fragment:
  - `frag_active_choi_ai_classroom_transformer1_grounding_status`
- anchor:
  - `semantic.class_token_classification`
- anchors:
  - `[semantic.class_token_classification]`

즉 paragraph-side canonical semantic mapping은 실제로 닫혔다.

### 3-2. projection 변화

보강 후 projection:

- `binding_source=first_pass_canonical`
- `value_key=semantic.class_token_classification`
- `primary_rule_key=semantic.class_token_classification`
- `scene=comparison`
- `flow=contract`

즉 `semantic.row.grounding_status` fallback에서 벗어났다.

### 3-3. saved row 변화

보강 후 save 결과:

- asset:
  - `choi_ai_classroom_transformer1`
- candidate:
  - `state-grounding_status`
- saved row:
  - `primary_rule_key=semantic.class_token_classification`
  - `binding_source=first_pass_canonical`
  - `value_paragraph_ref=lines 691-692 @ 36:33`
  - `value_paragraph_text=보통 이제 비전 트랜스포머에 보면은 예요 클래스 토큰으로부터 나온 걸 가지고 이미지 분류를 보통 하죠.네`
- scene / flow:
  - `comparison / contract`

즉 이번 bounded test에서는 paragraph-side semantic mapping 최소 보강만으로 value-side canonical binding이 실제로 닫혔다.

## 4. binding closed / semantic fidelity okay 분리 판정

### 4-1. binding closed

- 판정: `yes`

이유:

- fragment anchor가 실제로 생겼고
- projection이 fallback row key를 벗어났고
- save 결과도 `semantic.class_token_classification`으로 바뀌었다.

### 4-2. semantic fidelity okay

- 판정: `부분적 yes`

이유:

- 이 paragraph는 실제로 “트랜스포머 output을 무엇으로 분류에 연결하는가”를 설명한다.
- `클래스 토큰 -> 이미지 분류`는 `grounding_status`의 한 concrete grounding mechanism을 직접 드러낸다.
- 그래서 `cnn`의 `semantic.label_classification`보다 row 의미에 더 직접적으로 닿는다.

하지만 한계도 있다.

- row label이 `partially grounded`인데,
  지금 closure는 그중에서도 `class-token-based classification grounding` 한 가지 메커니즘으로 좁혀 닫힌다.
- 따라서 “grounding_status 전체 의미”를 다 담는다고 보긴 어렵다.

최종 분리 판정:

- `binding closed`: yes
- `semantic fidelity okay`: yes, but narrow-mechanism closure

## 5. output-worthiness / meaning-context sufficiency 보조 판정

이번 턴에서는 분절문/의미문장이 출력 가능한 최소 의미 단위인지도 같이 보았다.

현재 paragraph와 문맥:

- current:
  - `보통 이제 비전 트랜스포머에 보면은 예요 클래스 토큰으로부터 나온 걸 가지고 이미지 분류를 보통 하죠.네`
- surrounding context:
  - prev:
    - `달아서 테스크를 수행하는 겁니다. 요렇게 하는 방법이 많이 쓰여요. 그래서 어`
  - next:
    - `그래서 어 클래시파이어를 여기다다는 경우들이 더 많습니다. 그리고 내가 뭐 토큰 레벨 다 뭐`

판정:

- `output-worthiness`: `yes`
- `meaning-context sufficiency`: `minimum sufficient`

이유:

- 문단 하나만으로도 “class token이 classification output을 담당한다”는 메커니즘이 읽힌다.
- 주변 문맥도 classifier/head 쪽으로 이어져서 완전히 뜬금없는 한 문장이 아니다.

다만 아직 약한 점:

- 이건 여전히 “grounding 상태 전체”보다는 특정 output mechanism 한 조각에 가깝다.
- 즉 읽기 단위로는 쓸 수 있지만, row semantics 전체의 충분 조건이라고 보긴 이르다.

## 6. 현재 기관 수준에 주는 의미

이번 결과가 주는 의미는 두 가지다.

1. `transformer1`도 이제
- retrieval lexicon 보강
- paragraph-side semantic mapping 보강
두 단계를 거치면 value-side canonical binding이 실제로 닫힌다.

2. 하지만 `cnn`, `transformer1` 둘 다
- row semantics 전체를 직접 canonicalize했다기보다
- 각 자산이 가진 concrete mechanism bucket으로 닫히는 경향이 있다.

따라서 현재 canonical onboarding 기관 수준은:

- `조건부 기관`
- 또는 더 엄격히 말하면
  `binding closure is reproducible, but semantic fidelity still needs guard`

즉 일반화는 전진했지만,
closure 자체와 semantic fidelity를 분리해서 계속 봐야 한다.

## 7. 다음 supervisor 지시를 위한 메모

이번 턴이 다음을 좁히는 이유는 분명하다.

- `transformer1`도 이제 retrieval-only 문제가 아니라 semantic mapping까지 닫혔다.
- 따라서 다음 단계는 “더 닫히는가”가 아니라 “이 closure들이 row semantics를 과도하게 좁히지 않는가”를 비교 검증하는 쪽으로 옮겨간다.

가장 적절한 다음 지시 후보:

1. `cnn / transformer1 / vlm grounding_status semantic fidelity comparative guard`
- 세 자산의 closure를 나란히 놓고
- row semantics 전체 대비 얼마나 좁거나 넓은지 비교

2. `meaning-unit widening check`
- 현재 paragraph 단위가 너무 얇아서 mechanism-only closure로 가는지
- 아니면 이 정도 단위가 실제 reread/output 단위로 충분한지 재검증

즉 다음은 “닫힘 더 만들기”보다
`닫힌 것들이 얼마나 의미에 충실한가`
를 일반화 관점에서 보는 쪽이 맞다.
