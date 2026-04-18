[[A]] [[OBJ:minimal_scaffold_intervention_experiment_plan_v1]] [[SEM:minimal_experiment_order_for_scaffold_reduction_without_object_lift]]

# minimal scaffold intervention experiment plan v1

## 1. purpose

- 이 문서의 목적은 segmentation / pointer / heading을 한꺼번에 고치지 않고, 어떤 최소 실험을 어떤 순서로 할지 정하는 것이다.
- 즉 대공사 없이 reusable attitude를 가장 많이 살릴 intervention order를 잡는 계획서다.

## 2. intervention order

### experiment A — segmentation support probe

- priority: 1
- question:
  - block/window 붕괴만 조금 완화해도 question seed / relation movement / context unit 보존율이 올라가는가
- scope_limit:
  - splitter 전면 개편 금지
  - support/adaptor 수준의 최소 개입만 검토
- success_signal:
  - single mega block이 둘 이상 의미 단위로 분리됨
  - question candidate diversity가 조금이라도 회복됨
  - context unit ref가 비지 않는 쪽으로 개선 단서가 생김
- failure_signal:
  - block 수만 늘고 readable attitude는 그대로 약함

### experiment B — pointer stabilization probe

- priority: 2
- question:
  - naming은 살아 있는데 ref가 비는 문제를 최소 pointer anchor 보강으로 줄일 수 있는가
- scope_limit:
  - naming layer 확장 금지
  - evidence pointer와 readable unit 연결만 최소 보강
- success_signal:
  - context unit 또는 candidate summary가 실제 ref를 더 자주 가짐
  - naming-without-support 사례가 줄어듦
- failure_signal:
  - ref는 생기지만 여전히 의미 단위가 아니라 형식 포인터만 늘어남

### experiment C — heading-independent role probe

- priority: 3
- question:
  - heading이 없어도 paragraph role이 일부라도 살아날 수 있는가
  - 아니면 role 판독은 지금 단계에서 계속 hold가 맞는가
- scope_limit:
  - 기존 youtube-style role 체계 일반화 금지
  - role probe 수준에서만 제한
- success_signal:
  - paragraph role reading이 특정 heading 없이도 부분 실행됨
  - role shift evidence가 아주 일부라도 살아남음
- failure_signal:
  - role naming만 늘고 support structure는 여전히 빈약함

## 3. why this order

- segmentation first:
  - 가장 바닥에서 question opening / context unit / pivot을 동시에 좌우한다
- pointer second:
  - object lift hold의 직접 근거인 empty-ref / weak support를 줄이는 데 중요하다
- heading third:
  - 역할 판독에는 중요하지만 reusable attitude 전체 회복 폭은 상대적으로 좁다

## 4. what not to do

- object lift 구현 금지
- splitter 전체 재설계 금지
- 새 도메인 맞춤 naming 확장 금지
- evidence 없는 role/naming generalization 금지

## 5. one-line summary

> 최소 실험 순서는 segmentation → pointer → heading이다. 목적은 더 똑똑한 판정기를 만드는 것이 아니라, reusable attitude가 살아남을 발판을 가장 적은 개입으로 먼저 복구하는 것이다.
