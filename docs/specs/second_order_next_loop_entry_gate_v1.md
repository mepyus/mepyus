[[A]] [[OBJ:second_order_next_loop_entry_gate_v1]] [[SEM:entry_gate_for_next_validation_loop_after_three_axis_integration]]

# second-order next loop entry gate v1

## 1. purpose

- 이 문서의 목적은 다음 반복 루프를 아무 추가 실험이 아니라, 명시적 진입 조건이 있는 검증 루프로 고정하는 것이다. 이 gate는 탈락 심사표가 아니라 아직 더 만나야 할 조건을 기억하는 구조다.

## 2. next loop tone lock

- 다음 루프는 object lift를 시도하는 루프가 아니다.
- 다음 루프의 목적은:
  - weak -> recurring weak
  - fallback grounded -> 일부 direct grounded
  - single-domain survival -> cross-domain partial survival
  - role-like hint -> evidence-linked repeated role-like hint
  를 검증하는 것이다.
- 따라서 이 gate는 승격 심사표가 아니라, 현재 열린 재독해가 어디서 아직 directness를 얻지 못했는지 표시하는 운영 게이트로 읽는다.

## 3. loop entry criteria

- segmentation / pointer / heading 이후 결과가 동일 형식에서 반복 재현될 것
- direct grounded recovery가 일부라도 확인될 것
- question-inducing candidate가 `0`을 벗어날 것
- role-like reading이 weak_medium을 넘는 사례가 생기거나, evidence-linked repeated role-like hint가 누적될 것
- scaffold dependency 감소가 일회성 patch가 아님을 보여줄 것

## 4. loop deny criteria

- fallback-only grounding이 대부분일 때
- question-inducing candidate가 계속 `0`일 때
- role 계열이 role-like hint 수준에만 머물 때
- pivot / compression이 거의 빈 상태일 때
- naming carryover가 support보다 더 강할 때
- 특정 파일에만 맞는 patch 흔적이 강할 때

## 5. minimum evidence before reopening

- comparison-domain evidence at least one more repeat
- direct grounded support at least partial
- candidate grounding quality improved beyond fallback-only
- hold reasons reduced on at least one axis without new overfire
- current gate blockers weakened on at least one repeated dimension:
  - question-inducing candidate absence
  - fallback grounding dominance
  - weak role-like only
  - pivot/compression non-recurrence
  - scaffold carryover risk

## 6. relation to object lift

- entry gate 통과는 곧 object lift 허용이 아니다
- entry gate 통과는 오직 다음 검증 루프를 열 수 있다는 뜻이다
- object lift 전단 재논의는 다음 조건까지 갖춰졌을 때만 가능하다:
  - direct grounded context units 반복 확보
  - question-inducing candidates cross-domain non-zero
  - repeated evidence-linked candidates without naming overfire

## 7. operator summary

- 운영자는 루프를 열기 전에
  - axis별 회복 상태
  - weak / fallback / direct 분포
  - hold reason 변화
  - naming carryover 여부
  를 먼저 확인해야 한다.

## 8. one-line summary

> 다음 루프는 승격 루프가 아니라, 현재 weak / fallback recovery가 반복 가능성과 directness를 얻는지 검증하는 조건부 루프이며, entry criteria를 만족하지 못하면 열지 않는다.
