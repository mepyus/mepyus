# active asset canonical onboarding generalization v1

## 0. why this record exists

- 이번 기록의 목적은 `choi_ai_classroom_vlm`에서 한 번 성공한 canonical onboarding이 다른 active asset에도 반복되는지 검증하는 것이다.
- 구조나 schema를 다시 바꾸는 것이 아니라,
  - 어떤 asset은 같은 절차를 탈 수 있고
  - 어떤 asset은 어느 단계에서 끊기는지
  를 실제로 판정해 다음 supervisor 지시를 좁히기 위한 기록이다.

---

## 1. 대상 active asset 선정 이유

선정 대상:

1. `choi_ai_classroom_vlm`
   - 이유: 이미 first-pass canonical binding까지 성공한 기준 asset이다.
2. `choi_ai_classroom_transformer1`
   - 이유: 같은 `choi_ai_classroom_*` 계열이지만 원문 내용이 다르고, 같은 raw shape에서 canonical onboarding이 반복되는지 보기 좋다.
3. `choi_ai_classroom_cnn`
   - 이유: 같은 raw runtime shape를 가지면서도 object/object-context 성격이 조금 달라, anchor coverage와 reread quality 차이를 보기 좋다.

공통 조건 확인:

- 세 asset 모두 `selectedAsset` raw shape가 존재한다.
- 세 asset 모두 `source_file`이 있다.
- 세 asset 모두 `canonicalStateRows` 6개를 가진다.

즉 raw shape만 보면 세 asset 모두 onboarding 후보 자격은 있다.

---

## 2. asset별 onboarding 경로 추적

### 2-1. baseline success asset — `choi_ai_classroom_vlm`

#### current conditions

- source_file:
  - `inputs/external_cases/choi_ai_classroom_vlm.txt`
- canonicalStateRows:
  - `packet_texture`
  - `grounding_status`
  - `emergence_status`
  - `carryover_risk`
  - `maturation_state`
  - `traceability_status`
- reread:
  - object paragraph 복귀 가능
  - value paragraph 복귀 가능

#### onboarding trace

1. active asset first-pass fragment generation
2. object fragment 생성
3. row fragment 생성
4. paragraph/source canonical match
5. canonical-better upgrade
6. saved_connection reread loop 연결

#### actual result

- `state-grounding_status`
  - `binding_source=first_pass_canonical`
  - `primary_rule_key=semantic.contrastive_learning`
  - `scene=comparison`
  - `flow=contract`
- `state-traceability_status`
  - `binding_source=first_pass_canonical`
  - `primary_rule_key=semantic.embedding_space_distance`
  - `scene=evidence`
  - `flow=bridge`

#### reading quality

- object paragraph와 value paragraph가 둘 다 surface에서 읽힌다.
- canonical binding과 saved_connection 저장이 같이 닫힌다.

#### verdict

- onboarding success

---

### 2-2. comparison asset — `choi_ai_classroom_transformer1`

#### current conditions

- source_file:
  - `inputs/external_cases/choi_ai_classroom_transformer1.txt`
- canonicalStateRows:
  - `packet_texture`
  - `grounding_status`
  - `emergence_status`
  - `carryover_risk`
  - `maturation_state`
  - `traceability_status`
- onboarding readiness:
  - `ready_for_fragment_generation=True`

#### onboarding trace

1. active fragment generation:
  - object fragment 생성됨
  - row fragment 6개 생성됨
2. object reread:
  - `lines 11-12 @ 0:39`
  - object paragraph 확보
3. row reread:
  - `grounding_status -> lines 1-2 @ 0:08`
  - 하지만 `match_confidence=low`
4. fragment anchor enrichment:
  - `packet_texture`만 `semantic.embedding_space_distance`
  - `grounding_status`, `traceability_status` 등은 anchor 비어 있음
5. save path:
  - validated surface 기준으로는 value paragraph가 비어 canonical save 불가
  - script path로는 provisional fallback 저장은 가능

#### actual result

- `state-grounding_status`
  - projection 결과:
    - `binding_source=provisional_row_fallback`
    - `primary_rule_key=semantic.row.grounding_status`
  - save 결과:
    - object paragraph는 들어감
    - value paragraph는 비어 실제 reread가 아니라 original preview fallback으로 저장됨

#### where it breaks

- 끊기는 지점:
  - `row -> paragraph reread confidence gate`
  - 그리고 그 row paragraph에 canonical anchor가 붙지 않음

#### verdict

- onboarding partial / canonical binding fail

---

### 2-3. comparison asset — `choi_ai_classroom_cnn`

#### current conditions

- source_file:
  - `inputs/external_cases/choi_ai_classroom_cnn.txt`
- canonicalStateRows:
  - `packet_texture`
  - `grounding_status`
  - `emergence_status`
  - `carryover_risk`
  - `maturation_state`
  - `traceability_status`
- onboarding readiness:
  - `ready_for_fragment_generation=True`

#### onboarding trace

1. active fragment generation:
  - object fragment 생성됨
  - row fragment 6개 생성됨
2. object reread:
   - `lines 1-2 @ 0:11`
   - object paragraph 확보
3. row reread:
   - `grounding_status -> lines 69-70 @ 3:49`
   - 하지만 `match_confidence=low`
4. fragment anchor enrichment:
   - `packet_texture -> semantic.embedding_space_distance`
   - `emergence_status -> semantic.retrieval_ranking_clustering`
   - `traceability_status -> semantic.topic_similarity`
   - 그러나 `grounding_status`는 anchor 비어 있음
5. save path:
   - `state-grounding_status`는 canonical binding으로 못 올라감
   - object 쪽은 `object.model.cnn`으로 잡히지만, value 쪽이 fallback에 머묾

#### actual result

- `state-grounding_status`
  - projection 결과:
    - `binding_source=provisional_row_fallback`
    - `primary_rule_key=semantic.row.grounding_status`
  - save 결과:
    - object key는 `object.model.cnn`
    - value key는 여전히 provisional row key

#### where it breaks

- 끊기는 지점:
  - `grounding_status` row reread confidence low
  - 해당 row paragraph의 canonical anchor 부재

#### verdict

- onboarding partial / object-side only canonical success

---

## 3. 성공 조건 / 실패 조건

### 성공 조건

`choi_ai_classroom_vlm`에서 실제로 성립한 조건:

1. `source_file` 존재
2. `canonicalStateRows` 존재
3. object paragraph reread 가능
4. target row의 paragraph reread가 `medium/high` confidence
5. 그 row paragraph에 실제 canonical anchor가 붙음
6. save 시 validated reading_context가 object/value 양쪽 모두 채워짐
7. 같은 connection이 이미 있어도 canonical-better upgrade 가능

### 실패 조건

`transformer1`, `cnn`에서 실제로 드러난 실패 조건:

1. raw shape는 충분함
2. fragment generation도 됨
3. 하지만 target row reread가 `low confidence`
4. row paragraph canonical anchor가 비거나 target row와 안 맞음
5. 따라서 value-side canonical binding 실패
6. 결과적으로 saved_connection은 provisional fallback으로 저장되거나, validated surface 기준에선 저장 불가

즉 문제는 surface보다는 더 앞의
- row reread quality
- row paragraph anchor coverage
쪽이다.

---

## 4. 공통 최소 조건

canonical onboarding이 성립하는 최소 조건:

1. `asset_id`
2. `source_file`
3. `canonicalStateRows`
4. object paragraph reread 가능
5. value row paragraph reread가 최소 `medium` 이상
6. value row paragraph에서 canonical anchor를 실제로 추출 가능
7. save path가 object/value reread를 둘 다 요구하는 validated route를 타야 함

optional but helpful:

- row별 `scene/flow` 기본 매핑
- object paragraph용 intro/context extractor
- 기존 provisional save를 canonical로 교체하는 dedupe upgrade

---

## 5. 현재 병목

가장 큰 병목 1:

- `row -> paragraph reread confidence`
- 지금 다른 active asset에서는 row paragraph는 찾더라도 대부분 `low confidence`에 머문다.
- 이 때문에 surface validated save가 value-side reread를 비운다.

가장 큰 병목 2:

- `row paragraph anchor coverage`
- row paragraph가 canonical anchor 없이 저장되면 canonical binding까지 못 올라간다.
- 즉 fragment generation만으로는 충분하지 않고, row paragraph 수준 anchorizer coverage가 필요하다.

보조 병목:

- script path는 provisional fallback 저장을 허용하지만, surface validated save 기준과는 어긋날 수 있다.
- 따라서 일반화 검증은 script 결과보다 validated surface 기준을 우선 봐야 한다.

---

## 6. 기관 판정

- 판정: `특정 조건부 기관으로 볼 수 있음`

이유:

- lucky case만은 아니다.
  - `transformer1`, `cnn`도 같은 raw shape에서 같은 onboarding path를 탔다.
  - fragment generation, object reread, save loop 진입까지는 반복됐다.
- 하지만 아직 fully general institution도 아니다.
  - value-side canonical binding은 asset별 row reread quality와 anchor coverage에 크게 좌우된다.
  - 즉 현재는 `조건부로 작동하는 기관`이다.

한 줄로 말하면:

- path는 reusable하다.
- binding success는 아직 asset content quality와 row-specific reread/anchor coverage에 묶여 있다.

---

## 7. 다음 supervisor 지시를 위한 메모

다음 턴에서 먼저 좁혀야 할 방향:

1. `row reread confidence`를 높이는 쪽인지
2. `row paragraph anchor coverage`를 넓히는 쪽인지

현재 검증 기준상 더 직접적인 우선순위는:

- `grounding_status` 같은 target row가 왜 `low confidence`로 떨어지는지
- 그리고 그 paragraph에 왜 canonical anchor가 안 붙는지

즉 다음 supervisor 지시는

- `active asset canonical onboarding path` 자체를 다시 바꾸는 방향이 아니라
- `다른 active asset에서 value-side canonical binding이 안 붙는 직접 원인`
을 더 좁혀서 보게 만드는 쪽이 맞다.

추천되는 다음 질문:

- `grounding_status` row reread confidence를 결정하는 현재 lexicon / mapping 기준이 너무 asset-specific인가?
- row paragraph anchorizer coverage를 늘리면 transformer1/cnn도 canonical binding으로 올라가는가?

---

## 8. one-line summary

> active asset canonical onboarding은 `choi_ai_classroom_vlm`에만 우연히 먹힌 lucky case는 아니지만, 아직 `source_file + canonicalStateRows + medium/high row reread + row paragraph anchor coverage`가 맞아야만 fully canonical binding으로 닫히는 조건부 기관 단계에 머물러 있다.
