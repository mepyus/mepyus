# mixed corridor boundary probe stage3 spec

## 1. 목적

- mixed hold corridor가 reinforcing / adjacent / off-axis 입력에 어떻게 다르게 반응하는지 시험해, topic resonance와 corridor specificity를 구분한다.

## 2. 현재 잠긴 baseline

- mixed hold corridor는 re-entry 가능한 corridor다.
- observer accumulation은 확인됐지만 `stable_closure_reached` 는 없다.
- re-entry accumulation은 곧바로 canonical promotion을 뜻하지 않는다.

## 3. 왜 boundary challenge가 필요한가

- 지금까지는 corridor를 잘 건드릴 입력 위주로 관찰했다.
- 따라서 current reinforcement가 true corridor specificity인지, 아니면 broad topic resonance인지 별도 검증이 필요하다.

## 4. 3개 입력 그룹 정의

- `reinforcing`
  - 같은 arrival axis를 다시 강하게 건드릴 가능성이 높은 입력
- `adjacent`
  - 주제권은 비슷하지만 corridor 도착축은 덜 직접적인 입력
- `off_axis`
  - 기술/AI 언급은 있어도 현재 corridor 전환축과는 다른 입력

## 5. match type 정의

- `anchor_only_echo`
- `bridge_partial_echo`
- `arrival_axis_match`
- `corridor_specific_reentry`
- `no_meaningful_match`

## 6. specificity judgment 정의

- `specific`
- `broad_but_noisy`
- `topic_only`
- `unclear`

판정은 단어 반복보다 `transition corridor + arrival axis + bridge direction` 보강을 우선한다.

## 7. 비목표

- 코어 수정
- canonical promotion rule 추가
- mixed/canonical 경계 변경
- observer 결과를 곧바로 core truth로 승격

## 8. 성공 조건

- 3개 입력 그룹이 분리 등록된다.
- corridor별 반응 차이가 그룹 단위로 비교된다.
- topic resonance와 corridor specificity를 구분하기 시작한다.
- false positive watch가 생긴다.
- `stable_closure_reached` 부재를 다시 보수적으로 확인한다.
