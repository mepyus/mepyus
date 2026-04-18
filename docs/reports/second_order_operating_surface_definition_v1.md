[[A]] [[OBJ:second_order_operating_surface_definition_v1]] [[SEM:surface_for_supervising_maturation_state_of_second_order_outputs]]

# second-order operating surface definition v1

## 1. purpose

- 이번 노트의 목적은 2차 보정 결과를 “값 목록”이 아니라 “숙성 상태”와 “열림 상태”로 볼 수 있는 표면을 정의하는 것이다.
- 현재 이 표면은 결과 graph보다 먼저 원문-값-연결-재독해를 따라가는 운영 콘솔로 읽어야 한다.

## 2. what the operating surface should show

- 지금 자라는 객체 후보
- 반복되는 question seed
- 숙성 중인 2차 보정값
- hold 상태인 상위 객체 후보
- residue 때문에 덜 살아나는 block
- domain-specific suspicion이 높은 해석
- reusable attitude hint가 누적되는 패턴
- segmentation collapse 경고
- scaffold dependency가 높은 판독
- empty ref 상태의 context unit
- naming은 있으나 supporting evidence가 약한 후보
- failure에도 reusable attitude가 살아남은 사례

## 3. minimal panels

- `growing_object_candidates_panel`
  - 최근 반복된 상위 객체 후보와 supporting asset
- `question_seed_panel`
  - 반복 출현한 question-inducing block / context unit / paragraph role seed
- `second_order_hold_panel`
  - hold candidate와 hold reason
- `residue_interference_panel`
  - summary-stage에서 반복적으로 뒤로 밀리는 residue와 피해 block
- `domain_split_panel`
  - domain-specific suspicion vs reusable attitude hint

## 4. comparison-domain update

- `claude_code_index` 비교 결과를 보면, 운용화면은 단순 후보 목록만 보여줘서는 부족하다.
- 아래 같은 붕괴/경고도 보여줘야 한다.

- `granularity_collapse_panel`
  - block/window가 단일 mega block으로 붕괴하는 경우를 표시
- `context_unit_validity_panel`
  - context unit 이름은 있으나 `present_window_refs`가 비어 있는 경우를 경고
- `domain_leakage_panel`
  - 현재 자산에 어울리지 않는 object naming overfire를 의심 신호로 표시
- `scaffold_dependency_panel`
  - heading / pointer / comparison axis / report wording 의존성이 높은 판독을 표시
- `failure_with_surviving_attitude_panel`
  - 실패했지만 reusable attitude는 살아남은 사례를 분리해 보여줌
- `intervention_priority_panel`
  - segmentation / pointer / heading 중 다음 최소 개입 우선순위를 표시
- `hold_reason_by_dependency_panel`
  - segmentation_hold / scaffold_hold / naming_hold / evidence_hold를 축별로 보여줌
- `segmentation_support_delta_panel`
  - support on/off에 따른 block/window diversity 변화와 reusable attitude survival delta를 보여줌
- `still_empty_ref_panel`
  - segmentation support 이후에도 비어 있는 context unit ref count를 보여줌
- `pointer_grounding_panel`
  - direct grounded / fallback grounded / empty ref 비율을 함께 보여줌
- `naming_support_ratio_panel`
  - naming-without-support / naming-with-fallback-support / better-supported-hold 비율을 보여줌
- `pointer_support_mode_panel`
  - 현재 probe가 direct candidate grounding인지, purpose-top-window fallback인지 감독 가능하게 함
- `heading_dependence_risk_panel`
  - explicit heading 없이는 hard fail인지, weak role probe 수준으로만 남는지 보여줌
- `role_probe_panel`
  - role_probe_success_count / role_probe_with_evidence_count / unsupported_role_naming_count를 보여줌
- `role_probe_strength_panel`
  - weak / weak_medium / medium 수준의 role-like hint 분포를 보여줌

즉 운용화면은 무엇이 자라는지만 아니라, 무엇이 아직 조기 고정되고 있는지도 감독 가능해야 한다.

## 5. why this matters

- 사용자는 엔진 내부 전체를 보는 게 아니라, 무엇이 숙성 중인지 감독하면 된다.
- 따라서 운용화면은 값 나열보다 `숙성 상태`를 먼저 보여줘야 한다.

## 6. one-line summary

> 다음 운용화면은 내부 값 전체를 펼치는 것이 아니라, 2차 보정 결과가 어떤 상태로 자라고 있는지를 감독 가능한 표면으로 보여줘야 한다.

## 7. integrated supervision additions

- `axis_status_panel`
  - segmentation / pointer / heading each: prerequisite_recovery / grounding_support / weak_role_probe
- `grounding_level_panel`
  - weak vs fallback vs direct grounded distribution
- `question_candidate_presence_panel`
  - question-inducing candidate non-zero 여부와 반복성
- `object_lift_hold_basis_panel`
  - current structural reasons for hold in one place
- `next_loop_entry_readiness_panel`
  - current loop readiness vs deny status
- `current_gate_blockers_panel`
  - question-inducing candidate absence
  - fallback grounding dominance
  - weak role-like only
  - pivot/compression non-recurrence
  - scaffold carryover risk
