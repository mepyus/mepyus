[[A]] [[OBJ:second_order_scaffold_reduction_priority_matrix_v1]] [[SEM:priority_matrix_for_reducing_scaffold_dependency_before_object_lift]]

# second-order scaffold reduction priority matrix v1

## 1. purpose

- 이 문서의 목적은 segmentation / pointer / heading 중 무엇부터 손대야 reusable attitude가 가장 많이 살아나는지 우선순위를 정하는 것이다.
- 즉 감으로 고치지 않고 `영향도 / 비용 / 위험` 기준으로 intervention 순서를 고정하기 위한 matrix다.

## 2. matrix fields

- dependency_axis
- affected_second_order_readings
- failure_symptoms
- reusable_attitude_impact
- intervention_cost
- intervention_risk
- expected_gain
- priority_rank
- notes

## 3. current priority rows

- `segmentation`
  - affected_second_order_readings:
    - question opening
    - context unit
    - pivot / compression
    - paragraph role support
  - failure_symptoms:
    - single block collapse
    - window diversity 부족
    - candidate spread 붕괴
  - reusable_attitude_impact:
    - question opening / relation movement / context reconstruction 전부의 바닥에 영향을 줌
  - intervention_cost: medium
  - intervention_risk: medium
  - expected_gain: very_high
  - priority_rank: 1
  - notes:
    - 가장 바닥의 기반 축이다
    - block/window 다양성이 조금만 살아나도 여러 2차 판독이 동시에 회복될 가능성이 있다

- `pointer`
  - affected_second_order_readings:
    - context unit
    - local/page/comparison rereading
    - candidate evidence anchoring
  - failure_symptoms:
    - empty-ref context unit
    - naming without support
    - evidence pointers는 있으나 실제 단위 ref는 약함
  - reusable_attitude_impact:
    - relation movement 태도는 남아도 grounded unit으로 못 남는 문제를 줄여 준다
  - intervention_cost: medium_low
  - intervention_risk: low_medium
  - expected_gain: high
  - priority_rank: 2
  - notes:
    - object lift hold의 직접 원인인 `ref 부족`을 줄이는 축이다
    - naming보다 evidence anchoring을 먼저 강화하는 데 유리하다

- `heading`
  - affected_second_order_readings:
    - paragraph role
    - 일부 local context selection
  - failure_symptoms:
    - heading mismatch
    - role interpretation 실행 실패
  - reusable_attitude_impact:
    - role shift 태도 복구에는 중요하지만 reusable attitude 전체를 살리는 가장 바닥 축은 아니다
  - intervention_cost: medium
  - intervention_risk: medium_high
  - expected_gain: medium
  - priority_rank: 3
  - notes:
    - 현재는 가장 scaffold-bound 한 기관이다
    - heading-independent probe는 가치 있지만 segmentation/pointer보다 뒤에서 보는 편이 맞다

## 4. current priority judgment

- 1순위는 `segmentation`이다.
  - 이유: single block collapse가 생기면 question seed / context unit / pivot / role support가 동시에 약해진다.
- 2순위는 `pointer`다.
  - 이유: naming만 남고 ref가 비는 문제는 object lift hold의 직접 근거이기 때문이다.
- 3순위는 `heading`이다.
  - 이유: paragraph role에는 중요하지만 reusable attitude 전체를 회복시키는 폭은 앞 두 축보다 좁다.

## 5. one-line summary

> 지금 2차 판독 구조에서 가장 먼저 줄여야 할 scaffold dependency는 segmentation이고, 그다음은 pointer, 마지막이 heading이다. 우선순위 없이 손대지 않는다.
