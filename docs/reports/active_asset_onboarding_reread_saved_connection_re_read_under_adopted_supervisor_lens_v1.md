# active asset / onboarding / reread / saved_connection 판정 재기록

## 0. 왜 이 재기록이 필요한가

- `narrow mechanism closure detector + widening trigger candidate contract v1.1`이 감독 기준 후보로 채택되었다.
- 따라서 이제부터 active asset / onboarding / reread / saved_connection 관련 판정은
  아래 순서로 다시 읽어야 한다.
  1. `binding closed`
  2. `semantic fidelity`
  3. `output-worthiness`
  4. `meaning-context sufficiency`
  5. `detector`
  6. `widening trigger`
- 이 문서는 기존 성공/실패 판정을 이 렌즈 아래에서 다시 정렬해,
  이후 감독 판단의 기준점을 하나로 맞추기 위한 재기록이다.

## 1. 적용 대상과 범위

이번 재기록은 아래 active asset / row를 중심으로 한다.

- `choi_ai_classroom_vlm / grounding_status`
- `choi_ai_classroom_cnn / grounding_status`
- `choi_ai_classroom_transformer1 / grounding_status`

이 셋을 중심으로 본 이유:
- onboarding
- reread
- saved_connection
- semantic fidelity guard
- widening 검증
이 모두 실제로 축적되어 있는 자산군이기 때문이다.

보조 reference:
- `carryover_risk / vlm`
  - pre-closure context-bearing watchpoint의 경계 사례로만 사용

## 2. 감독 렌즈 순서 재기록

### 2-1. `choi_ai_classroom_vlm / grounding_status`

#### binding closed

- `yes`
- `binding_source=first_pass_canonical`
- `primary_rule_key=semantic.contrastive_learning`
- onboarding / reread / saved_connection 모두 canonical path로 닫힌다.

#### semantic fidelity

- 판정:
  - `row-meaning-faithful closure`
- 이유:
  - value paragraph가 `positive / negative / label-free comparison`을 직접 설명하며,
    `partially grounded` row 의미를 비교적 직접적으로 운반한다.

#### output-worthiness

- `yes`
- 현재 paragraph는 surface reread와 saved_connection value unit으로 바로 쓸 수 있다.

#### meaning-context sufficiency

- `strong`
- current unit만으로도 row 의미가 충분히 읽히고,
  surrounding context도 같은 explanatory arc를 이어 준다.

#### detector

- `off`
- 이유:
  - `narrow mechanism closure`가 아니라 `row-meaning-faithful closure`에 가깝기 때문이다.

#### widening trigger

- `off`
- 이유:
  - widening이 필요하지 않다.
  - current paragraph가 이미 충분하다.

#### lens-based verdict

- `onboarding success / reread success / saved_connection success`
- 감독 렌즈 기준으로도 가장 안정적인 success asset이다.

---

### 2-2. `choi_ai_classroom_cnn / grounding_status`

#### binding closed

- `yes`
- 현재는 최소 보강 이후:
  - `binding_source=first_pass_canonical`
  - `primary_rule_key=semantic.label_classification`
- onboarding / reread / saved_connection 모두 canonical closure까지 닫힌다.

#### semantic fidelity

- 판정:
  - `acceptable but narrow mechanism closure`
- 이유:
  - paragraph는 실제로 `레이블은 폭포`, `분류도 폭포`를 말하며 grounding을 설명한다.
  - 하지만 `partially grounded` 전체보다 `label/classification` 쪽으로 더 좁게 닫힌다.

#### output-worthiness

- `yes`
- current paragraph 자체는 읽기/출력 단위로 최소 성립한다.

#### meaning-context sufficiency

- `minimum sufficient`
- 이유:
  - current unit만으로도 의미는 읽히지만,
  - row 의미 전체를 안정적으로 싣기엔 예시(`폭포`) 의존이 크다.

#### detector

- `on`
- 이유:
  - `binding closed = yes`
  - `semantic fidelity = acceptable but narrow mechanism closure`
  - `output-worthiness = yes`
  - `meaning-context sufficiency = minimum sufficient`
  를 모두 만족한다.

#### widening trigger

- `on`
- 이유:
  - `current + next`가 `레이블링 비용 / 변형 속에서도 유지되는 기준` 쪽으로 같은 explanatory arc를 이어 주며
    row 의미를 더 직접적으로 보강한다.

#### lens-based verdict

- `onboarding success / reread success / saved_connection success`
- 단, `semantic fidelity guard required success`
- 기존 단순 성공 판정은 이제
  - `closure success`
  - `semantic fidelity okay but narrow`
  - `widening helpful`
  로 분해해 읽어야 한다.

---

### 2-3. `choi_ai_classroom_transformer1 / grounding_status`

#### binding closed

- `yes`
- 최소 보강 이후:
  - `binding_source=first_pass_canonical`
  - `primary_rule_key=semantic.class_token_classification`

#### semantic fidelity

- 판정:
  - `acceptable but narrow mechanism closure`
- 이유:
  - `클래스 토큰 -> 이미지 분류` 메커니즘은 row 의미와 직접적으로 닿는다.
  - 하지만 `partially grounded` 전체보다 `class-token classification` 메커니즘 하나에 설명이 집중된다.

#### output-worthiness

- `yes`
- current paragraph는 read unit으로 최소 성립한다.

#### meaning-context sufficiency

- `minimum sufficient`
- 이유:
  - mechanism 설명은 읽히지만,
  - row 의미 전체를 충분히 운반하는 수준은 아니다.

#### detector

- `on`
- 이유:
  - `binding closed = yes`
  - `semantic fidelity = acceptable but narrow mechanism closure`
  - `output-worthiness = yes`
  - `meaning-context sufficiency = minimum sufficient`
  가 모두 성립한다.

#### widening trigger

- `on`
- 이유:
  - `current + next`가 classifier/head 문맥을 이어 주며,
    abrupt한 mechanism-only closure를 조금 완화한다.

#### lens-based verdict

- `onboarding success / reread success / saved_connection success`
- 단, `semantic fidelity guard required success`
- cnn보다는 row 의미와 더 직접적이지만,
  여전히 detector/widening 대상으로 읽어야 한다.

---

### 2-4. 보조 경계 사례: `choi_ai_classroom_vlm / carryover_risk`

#### binding closed

- `no`
- `anchor=None`, `anchors=[]`

#### semantic fidelity

- canonical closure가 없으므로 `closure 이후 semantic fidelity 판정 대상 아님`

#### output-worthiness

- `yes`

#### meaning-context sufficiency

- `minimum sufficient`

#### detector

- `off`
- 이유:
  - `binding closed = no`이므로 detector 전제가 성립하지 않는다.

#### widening trigger

- `off`
- 이유:
  - next sentence가 실제로 보강적이어도,
    pre-closure 단계에서는 widening trigger를 직접 적용하지 않는다.

#### lens-based verdict

- `onboarding partial / reread partial / saved_connection canonical success 아님`
- 이 사례는 pre-closure context-bearing watchpoint 사례로만 유지한다.

## 3. 기존 성공/실패 판정의 재정렬

### 이전의 단순 판정

- `vlm`: success
- `cnn`: success after minimal boost
- `transformer1`: success after minimal boost
- `carryover_risk / vlm`: partial / no canonical closure

### 채택된 감독 렌즈 아래의 재정렬

- `vlm / grounding_status`
  - `stable success`
  - detector/widening 불필요
- `cnn / grounding_status`
  - `guarded success`
  - detector on, widening on
- `transformer1 / grounding_status`
  - `guarded success`
  - detector on, widening on
- `vlm / carryover_risk`
  - `pre-closure partial`
  - detector off, widening off, watchpoint only

## 4. 이 재기록으로 바뀌는 점

이제부터 active asset / onboarding / reread / saved_connection 관련 판정은
단순히 `closure 성공/실패`로 적지 않는다.

반드시 아래 순서를 유지한다.

1. `binding closed`
2. `semantic fidelity`
3. `output-worthiness`
4. `meaning-context sufficiency`
5. `detector`
6. `widening trigger`

즉 같은 `success`라도:
- `stable success`
- `guarded success`
- `pre-closure partial`
로 다시 구분해 읽는다.

## 5. watchpoint

1. `binding closed = yes`를 곧바로 `semantic fidelity okay`로 읽지 말 것
2. `output-worthiness = yes`를 곧바로 `row 의미 충분`으로 읽지 말 것
3. `narrow mechanism closure`는 success여도 detector 대상임을 유지할 것
4. pre-closure 상태에서 next sentence가 보강적으로 보여도 widening trigger로 바로 넘기지 말 것

## 6. 한 줄 판정

- 채택된 감독 렌즈 아래에서 기존 active asset 판정은 `closure success` 중심 판정에서 벗어나, `stable success / guarded success / pre-closure partial`로 다시 읽혀야 한다.
