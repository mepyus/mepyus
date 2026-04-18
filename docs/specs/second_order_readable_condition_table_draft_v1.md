[[A]] [[OBJ:second_order_readable_condition_table_draft_v1]] [[SEM:readability_conditions_for_second_order_outputs_before_object_lift]]

# second-order readable condition table draft v1

## 1. purpose

- 이 표의 목적은 2차 판독값을 더 많이 만드는 것이 아니라, 어떤 입력 조건에서 어떤 2차 판독이 살아나는지와 어디서 깨지는지를 분리해 기록하는 것이다.
- 따라서 이 문서는 object lift 이전에 필요한 `판독 가능 조건표`다.

## 2. table fields

- second_order_reading_type
- required_input_conditions
- observed_success_cases
- observed_failure_cases
- scaffold_dependency_level
- reusable_attitude_survives
- why_hold
- notes

## 3. current condition rows

- `question_opening`
  - required_input_conditions:
    - object candidates가 2개 이상 함께 살아남음
    - relation hint가 `transition` 또는 `execution shift`까지 동반됨
    - 최소한 질문 의도 window가 단일 mega block으로 완전히 붕괴하지 않음
  - observed_success_cases:
    - `youtube_03_22`
  - observed_failure_cases:
    - `claude_code_index`에서는 태도는 유지되지만 사실상 `0_0` 단일 candidate로 수렴
    - `claude_code_index` segmentation support 이후에는 window diversity는 생겼지만 기존 threshold 기준 candidate는 0개가 됨
  - scaffold_dependency_level: medium
  - reusable_attitude_survives: yes
  - why_hold: block/window granularity가 무너지면 question opening이 있어도 비교 가능한 seed 구조는 약해진다
  - notes:
    - 읽힘 자체보다 `질문을 여는 구조가 여러 candidate로 분산되는가`가 중요하다
    - segmentation support는 필요조건이지만 sufficient condition은 아니다

- `relation_movement`
  - required_input_conditions:
    - 설명층 외에 실행/전략/검증 쪽 층이 함께 잡힘
    - local 또는 page rereading이 가능한 정도의 서술 흐름이 있음
  - observed_success_cases:
    - `youtube_03_22`
    - `claude_code_index` 일부
  - observed_failure_cases:
    - 극단적 단일 block 상태에서는 relation이 모두 한 블록에 뭉쳐 movement보다 broad tag처럼 약화됨
    - segmentation support 이후에도 movement가 broad tag로 남을 수 있어 pointer grounding이 추가로 필요함
  - scaffold_dependency_level: low_medium
  - reusable_attitude_survives: yes
  - why_hold: relation name은 유지돼도 실제 운동 방향이 분리되지 않으면 object lift 근거로는 약하다
  - notes:
    - 현재까지는 2차 판독 중 가장 재사용 가능성이 높은 태도다

- `residue_priority_shift`
  - required_input_conditions:
    - opening summary 또는 anchor 선두 경쟁이 있음
    - discourse / filler / source residue가 topic-bearing signal과 실제로 경쟁함
  - observed_success_cases:
    - `youtube_03_22`
    - `claude_code_index`
  - observed_failure_cases:
    - summary surface가 너무 거칠면 후순위화 전후 차이가 약하게 보임
  - scaffold_dependency_level: low
  - reusable_attitude_survives: yes
  - why_hold: 아직 summary-stage 중심 태도이며, extraction 전체로 확장하면 과잉 suppression 위험이 있다
  - notes:
    - 현재는 가장 안정적인 reusable attitude 후보지만 여전히 bounded surface adjustment로만 본다

- `context_unit`
  - required_input_conditions:
    - multi-pass rereading에서 pass 간 차이가 실제로 발생함
    - block/window refs가 비지 않고 local/page/comparison 축이 살아 있음
    - pointer granularity가 context unit을 다시 묶을 수 있을 만큼 충분함
  - observed_success_cases:
    - `youtube_03_22`
  - observed_failure_cases:
    - `claude_code_index`에서는 unit 이름은 남아도 `present_window_refs`가 비는 현상 발생
    - segmentation support 이후에도 `present_window_refs`가 계속 비어 있음
    - pointer stabilization 이후에는 ref empty는 줄었지만 `fallback_grounded` 수준이라 direct grounding은 여전히 없음
  - scaffold_dependency_level: high
  - reusable_attitude_survives: partial
  - why_hold: 현재 context unit은 발생 조건보다 기존 dialogue scaffold 이름을 더 많이 끌고 있다
  - notes:
    - context unit은 읽힘보다 `ref 안정성`이 더 중요하다
    - segmentation만으로는 naming survives / ref empty 문제를 풀지 못했다
    - pointer stabilization은 필요했고 실제로 empty-ref는 줄였지만, 아직 `fallback evidence` 수준이어서 object lift support로는 부족하다

- `paragraph_role`
  - required_input_conditions:
    - heading 또는 paragraph pointer가 비교적 안정적임
    - local/page/comparison 축을 실제로 다시 걸 수 있음
    - 선택할 paragraph target이 형식적으로 식별 가능함
  - observed_success_cases:
    - `youtube_03_22`
  - observed_failure_cases:
    - `claude_code_index`에서는 heading mismatch로 실행 자체가 실패
    - heading-independent probe 이후에는 role-like reading은 생기지만 전부 fallback-grounded이고 paragraph role generalization까지는 못 감
  - scaffold_dependency_level: very_high
  - reusable_attitude_survives: partial
  - why_hold: role shift 태도는 흥미롭지만 현재 기관은 youtube-style heading scaffold 의존성이 높다
  - notes:
    - 지금은 paragraph role을 일반화하기보다 어떤 포인터 구조가 있어야 실행 가능한지 먼저 봐야 한다
    - heading-independent cue는 `hard failure -> weak role-like reading` 전환에는 도움을 줬지만, 아직 institution-level recovery로 보긴 어렵다

- `pivot_or_compression`
  - required_input_conditions:
    - page flow를 읽을 만큼 block diversity가 있음
    - relation movement가 broad tag가 아니라 흐름 전환으로 분리됨
  - observed_success_cases:
    - `youtube_03_22`
  - observed_failure_cases:
    - `claude_code_index`에서는 `pivot` 이름은 남지만 single block collapse 때문에 흐름 분화가 약하다
    - segmentation support 이후에는 `pivot_windows`가 오히려 비어 support만으로는 회복이 안 됨
    - pointer stabilization 이후에도 direct pivot grounding은 회복되지 않음
  - scaffold_dependency_level: high
  - reusable_attitude_survives: partial
  - why_hold: 흐름 기반 판독은 segmentation 안정성과 page-level structure를 강하게 요구한다
  - notes:
    - 지금은 page flow 태도와 flow scaffold를 분리해서 봐야 한다
    - segmentation이 필요하지만 pointer/comparison anchor 없이는 충분하지 않다
    - pointer support는 context-unit grounding에는 도움을 줬지만 pivot/compression recovery로 곧바로 이어지지 않았다

## 4. one-line summary

> object lift 전에는 2차 판독값 자체보다, 어떤 입력 조건과 scaffold 위에서 그 판독이 살아나고 어디서 무너지는지를 조건표로 먼저 남겨야 한다.

## 5. three-axis integration note

- current level summary:
  - `segmentation` mainly recovers prerequisites
  - `pointer` mainly improves grounding coverage
  - `heading` mainly allows weak role-like probing
- level distinction:
  - `weak`: role-like or pattern-like survival without strong grounding
  - `fallback`: evidence exists but via indirect stitching/support
  - `direct`: evidence points are directly and repeatedly attached without fallback dependence
- current read:
  - most recovered second-order institutions remain at `weak` or `fallback`
  - therefore readable conditions have improved, but object lift conditions have not yet been met
- next judgment note:
  - readable condition improvement alone is not enough
  - current gate blockers must weaken on repeated dimensions before reopening the next loop
