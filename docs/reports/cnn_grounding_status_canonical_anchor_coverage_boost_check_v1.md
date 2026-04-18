# cnn_grounding_status_canonical_anchor_coverage_boost_check_v1

## 1. cnn grounding_status 현재 상태

이번 턴에서 `choi_ai_classroom_cnn`를 먼저 택한 이유는, 지난 비교에서 이 자산은 `grounding_status`의 paragraph retrieval 자체는 비교적 맞게 잡히지만 canonical semantic coverage가 비어 있었기 때문이다. 즉 `transformer1`처럼 retrieval mismatch가 더 직접적인 경우보다, coverage-only bounded test로 적합했다.

보강 전 고정 상태:

- target row: `grounding_status`
- paragraph ref: `lines 69-70 @ 3:49`
- paragraph text:
  - `어, 결국은 다 똑같이 어, 폭포죠. 그렇죠? 똑같이 레이블은 폭포라고 할 수 있고 분류도 폭포로 해야 되죠.`
- row reread:
  - `match_score=1`
  - `match_confidence=low`
- active row fragment:
  - `anchor=None`
  - `anchors=[]`
- save/projection result:
  - `binding_source=first_pass_canonical`
  - but `primary_rule_key=semantic.row.grounding_status`

즉 보강 전 상태는:

- paragraph는 어느 정도 맞게 잡히지만
- row reread confidence는 low라 surface/save guard를 안정적으로 못 타고
- fragment에는 paragraph-side canonical semantic이 비어 있어서
- primary binding은 여전히 provisional row fallback에 머물렀다.

## 2. vlm 대비 cnn coverage 차이

`choi_ai_classroom_vlm`의 `grounding_status`는 아래처럼 닫힌다.

- paragraph text:
  - `네거티브하고 파지티브로 이렇게 막 비교하는 이런 대조 학습이 어 레이블 없이 이제 하게 됩니다. 아까는`
- row reread:
  - `match_score=3`
  - `match_confidence=high`
- fragment anchor:
  - `semantic.contrastive_learning`

반면 `choi_ai_classroom_cnn`의 차이는 다음 두 가지였다.

1. row paragraph alias 부족
- `grounding_status` lexicon이 `레이블`만 잡고 `분류`는 못 잡아서 score가 1에 머물렀다.

2. canonical semantic coverage 부족
- cnn paragraph는 `contrastive_learning` 문맥이 아니라
  `레이블은 ... / 분류도 ...` 같은 classification 문맥인데,
  이 문맥에 붙는 canonical semantic rule이 없었다.

즉 cnn은 retrieval이 완전히 틀린 게 아니라,
`row alias + paragraph semantic mapping`이 둘 다 한 칸씩 부족한 상태였다.

## 3. 최소 보강 후보와 선정 이유

이번 턴에서는 가장 작은 보강 2개만 택했다.

1. row paragraph alias 보강
- 파일: `app/runtime/segment_to_source_context_extractor.py`
- 변경:
  - `grounding_status` lexicon에 `분류` 추가
- 이유:
  - threshold를 건드리지 않고도 cnn paragraph가 row와 다시 닿는 score를 1 -> 2로 올릴 수 있는 최소 보강이다.

2. paragraph-side canonical semantic mapping 보강
- 파일: `app/input_layer/anchorizer/anchorizer.py`
- 변경:
  - `semantic.label_classification`
  - evidence text:
    - `레이블은`
    - `분류도`
- 이유:
  - cnn paragraph는 `contrastive_learning`이 아니라 label/classification grounding 문맥이다.
  - 기존 semantic set으로는 이 paragraph를 canonical semantic으로 올릴 수 없어서, paragraph-side coverage를 최소 단위로 보강했다.

이번 턴에서 하지 않은 것:

- confidence threshold 조정
- retrieval redesign
- transformer1 동시 해결
- broader schema 변경

## 4. 적용 결과

### 4-1. row reread 변화

보강 후 `extract_segment_source_context(...)` 결과:

- paragraph ref:
  - `lines 69-70 @ 3:49`
- paragraph text:
  - `어, 결국은 다 똑같이 어, 폭포죠. 그렇죠? 똑같이 레이블은 폭포라고 할 수 있고 분류도 폭포로 해야 되죠.`
- reread score/confidence:
  - before: `1 / low`
  - after: `2 / medium`

즉 row alias 하나(`분류`)만 추가해도 cnn `grounding_status`는 surface/save guard를 탈 수 있는 최소 reread 품질에 도달했다.

### 4-2. active fragment canonicalization 변화

보강 후 재생성한 active row fragment:

- fragment: `frag_active_choi_ai_classroom_cnn_grounding_status`
- anchor:
  - `semantic.label_classification`
- label:
  - `label classification`
- scene / flow:
  - `comparison / contract`

즉 paragraph-side canonical semantic coverage가 실제로 비어 있지 않게 되었다.

### 4-3. projection / save 결과

보강 후 projection:

- `binding_source=first_pass_canonical`
- `value_key=semantic.label_classification`
- `primary_rule_key=semantic.label_classification`
- `scene=comparison`
- `flow=contract`

보강 후 save 결과:

- asset:
  - `choi_ai_classroom_cnn`
- candidate:
  - `state-grounding_status`
- saved row:
  - `primary_rule_key=semantic.label_classification`
  - `binding_source=first_pass_canonical`
  - `value_paragraph_ref=lines 69-70 @ 3:49`
  - `value_paragraph_text=어, 결국은 다 똑같이 어, 폭포죠...`

즉 이번 턴의 최소 보강만으로 cnn `grounding_status`는 실제 value-side canonical binding까지 닫혔다.

## 5. binding 성공/실패 판정

- 판정: `성공`

이번 자산에서는 confidence를 직접 조정하지 않고도,

- row alias 보강
- paragraph-side canonical semantic 보강

이 두 가지 최소 개입만으로 value-side canonical binding이 닫혔다.

따라서 cnn `grounding_status`의 주 병목은 이번 bounded test 범위 안에서는 confidence rule 자체보다 canonical anchor coverage가 맞았다.

## 6. 일반화 최소 조건에 주는 의미

이번 결과가 보여준 일반화 최소 조건은 다음과 같다.

필수 조건:

1. active asset이 `source_file + canonicalStateRows`를 갖는다
2. target row가 paragraph reread로 최소 `medium`까지는 닿는다
3. 그 paragraph에 붙는 canonical semantic anchor가 실제로 존재한다

optional but helpful:

- row lexicon이 paragraph 문맥을 한 토큰 이상 더 잘 잡아준다
- paragraph-side semantic rule이 row semantics와 직접 연결된다

즉 onboarding 일반화의 최소 조건에 이번 턴이 추가한 것은:

- `row -> paragraph` alias coverage
- `paragraph -> canonical semantic` coverage

이 둘이 함께 있어야 cnn 같은 자산도 `first_pass_canonical` value binding으로 닫힌다는 점이다.

## 7. 다음 supervisor 지시를 위한 메모

이번 턴은 왜 `cnn`을 먼저 봤는지 명확하다.

- `transformer1`은 retrieval mismatch가 더 직접적이라 coverage-only test로는 경계를 흐린다.
- `cnn`은 paragraph가 이미 꽤 맞게 잡혀 있었기 때문에, coverage 보강이 병목인지 bounded test 하기에 적합했다.

이번 결과로 다음 턴 후보는 두 갈래로 좁혀진다.

1. `transformer1 grounding_status` row retrieval lexicon 검증
- cnn과 달리 retrieval mismatch가 더 큰지 확인

2. 다른 active asset에서도
- `row alias + paragraph canonical semantic`
  조합이 onboarding 최소 조건으로 반복되는지 교차 검증

현재로선 다음 턴 1순위는 `transformer1 grounding_status retrieval lexicon 검증`이 더 적합하다.
이유는 cnn에서는 coverage-first 가설이 이미 한 번 닫혔기 때문이다.
