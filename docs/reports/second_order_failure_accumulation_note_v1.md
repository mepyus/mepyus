[[A]] [[OBJ:second_order_failure_accumulation_note_v1]] [[SEM:failure_as_second_order_evidence_before_object_lift]]

# second-order failure accumulation note v1

## 1. purpose

- 이 문서의 목적은 실패를 버그 목록으로 적는 것이 아니라, object lift hold의 근거가 되는 2차 자료로 축적하는 것이다.
- 즉 이 노트는 `무엇이 어디서 왜 실패했는가`를 다음 보정/보류 판단의 재료로 남기는 축적 노트다.

## 2. segmentation failure

- failure_id: `single_block_collapse_claude_code_index`
  - input_asset: `inputs/external_cases/claude_code_index.txt`
  - first_pass_state:
    - block_count: 1
    - window_count: 1
    - broad object/layer firing persists
  - second_order_reading_type:
    - question opening
    - multi-pass interpretation
    - purpose synthesis
  - failure_symptom:
    - candidate diversity 붕괴
    - `0_0` 단일 candidate 수렴
    - page flow / pivot 분화 약화
  - suspected_dependency:
    - segmentation scaffold
  - why_this_blocks_object_lift:
    - 다양한 rereading 조건이 없으면 상위 객체가 아니라 broad theme overfire만 남는다
  - reusable_attitude_survived: yes
  - update_after_segmentation_support:
    - collapse 자체는 완화됨
    - 하지만 이 failure는 `resolved`가 아니라 `transformed`
    - now becomes: diversity recovered but grounded second-order support still weak

## 3. role interpretation failure

- failure_id: `heading_mismatch_paragraph_role_claude_code_index`
  - input_asset: `inputs/external_cases/claude_code_index.txt`
  - first_pass_state:
    - youtube-style heading 부재
  - second_order_reading_type:
    - paragraph role interpretation
  - failure_symptom:
    - `Bundle-Unbundle 프레임워크` heading not found
    - 실행 자체가 실패
  - suspected_dependency:
    - heading scaffold
  - why_this_blocks_object_lift:
    - paragraph role support가 도메인 바깥에서 성립하는지 아직 전혀 확인되지 않았다
  - reusable_attitude_survived: partial
  - update_after_heading_probe:
    - hard execution failure는 줄었음
    - 대신 weak/fallback role-like reading만 남음
    - failure는 resolved가 아니라 `softened`

- failure_id: `role_mapping_rigidity_risk`
  - input_asset: `inputs/external_cases/claude_code_index.txt`
  - first_pass_state:
    - paragraph target을 식별할 수 있는 안정적 pointer 부족
  - second_order_reading_type:
    - paragraph role interpretation
  - failure_symptom:
    - role shift를 보기 전에 입력 선택 단계에서 경직됨
  - suspected_dependency:
    - pointer + heading scaffold
  - why_this_blocks_object_lift:
    - role shift 태도와 실행 기관이 분리되지 않으면 object lift support evidence가 과장될 수 있다
  - reusable_attitude_survived: partial
  - update_after_heading_probe:
    - rigid heading mapping은 약화됐지만
    - generalized paragraph role recovery 없이 weak hint만 남아 institution-level hold는 유지

- failure_id: `fallback_role_hint_without_direct_role_grounding`
  - input_asset: `inputs/external_cases/claude_code_index.txt`
  - first_pass_state:
    - segmentation + pointer support 이후 context unit evidence는 존재
  - second_order_reading_type:
    - heading-independent role probe
  - failure_symptom:
    - role-like hint는 생기지만 direct grounded role support는 없음
    - weak/fallback role hint에 머묾
  - suspected_dependency:
    - heading scaffold
    - pointer quality
  - why_this_blocks_object_lift:
    - role 이름이 아니라 role 생존 조건만 확인된 상태라 상위 객체 support로는 여전히 약하다
  - reusable_attitude_survived: yes

## 4. context-unit failure

- failure_id: `empty_ref_context_unit_claude_code_index`
  - input_asset: `inputs/external_cases/claude_code_index.txt`
  - first_pass_state:
    - multi-pass는 형식상 실행됨
  - second_order_reading_type:
    - context unit reconstruction
  - failure_symptom:
    - context unit name survives
    - `present_window_refs` empty
  - suspected_dependency:
    - source pointer scaffold
    - comparison scaffold
  - why_this_blocks_object_lift:
    - 이름은 있는데 pointer가 없으면 맥락 단위가 아니라 wording scaffold일 가능성이 높다
  - reusable_attitude_survived: partial
  - update_after_segmentation_support:
    - segmentation support 이후에도 계속 유지됨
    - next dependency axis는 pointer임이 더 선명해짐
  - update_after_pointer_support:
    - empty-ref 자체는 줄었음
    - 하지만 `fallback_grounded` 수준이라 direct evidence recovery는 아직 아님
    - failure는 resolved가 아니라 `weakened`

- failure_id: `context_unit_boundary_instability`
  - input_asset: `inputs/external_cases/claude_code_index.txt`
  - first_pass_state:
    - pass difference는 있으나 supporting windows가 거의 없음
  - second_order_reading_type:
    - multi-pass interpretation
  - failure_symptom:
    - context unit 경계가 실제 자료보다 기존 dialogue 단위 이름에 더 의존
  - suspected_dependency:
    - youtube dialogue scaffold
  - why_this_blocks_object_lift:
    - 경계 안정성이 없으면 상위 객체 support로 쓰기 어렵다
  - reusable_attitude_survived: yes

## 5. naming failure

- failure_id: `ai_object_vocabulary_overfire_claude_code_index`
  - input_asset: `inputs/external_cases/claude_code_index.txt`
  - first_pass_state:
    - code/tool/usage oriented source
  - second_order_reading_type:
    - purpose synthesis
    - multi-pass interpretation
  - failure_symptom:
    - `AI의 미래`, `일의 미래`, `에이전트 애플리케이션` naming carryover
  - suspected_dependency:
    - domain-language scaffold
  - why_this_blocks_object_lift:
    - 이름이 뜬다고 상위 객체가 실제로 존재한다고 볼 수 없다
  - reusable_attitude_survived: yes

- failure_id: `naming_without_supporting_structure`
  - input_asset: `inputs/external_cases/claude_code_index.txt`
  - first_pass_state:
    - object names do appear
  - second_order_reading_type:
    - question block review
    - purpose synthesis
  - failure_symptom:
    - naming은 남는데 supporting context structure는 약함
  - suspected_dependency:
    - segmentation + context scaffold
  - why_this_blocks_object_lift:
    - 이름과 구조 support가 분리되어 있으면 object lift는 premature다
  - reusable_attitude_survived: yes
  - update_after_segmentation_support:
    - names are now distributed across many windows
    - but support structure is still not sufficiently grounded
    - naming-without-support remains active
  - update_after_pointer_support:
    - 일부 naming은 fallback evidence pointer를 가짐
    - 하지만 support quality가 direct가 아니라 weak/fallback이어서 hold는 유지됨

- failure_id: `fallback_grounding_without_direct_candidate`
  - input_asset: `inputs/external_cases/claude_code_index.txt`
  - first_pass_state:
    - segmentation support 이후 window diversity는 존재
  - second_order_reading_type:
    - context unit reconstruction
  - failure_symptom:
    - empty-ref는 줄었지만 direct candidate가 아니라 purpose top windows fallback으로 grounding됨
  - suspected_dependency:
    - pointer scaffold
    - question-opening stability
  - why_this_blocks_object_lift:
    - fallback evidence만으로는 상위 객체나 pivot/compression의 grounded support라고 보기 어렵다
  - reusable_attitude_survived: yes

## 6. why failure matters

- 실패는 단지 “못 읽었다”는 뜻이 아니다.
- 실패는:
  - 어떤 scaffold가 필요했는지
  - 어떤 reusable attitude는 남았는지
  - 어떤 층은 아직 도메인에 묶여 있는지
  를 분명하게 드러내 준다.
- 따라서 failure accumulation은 object lift 보류의 소극적 변명이 아니라, 미래 보정의 정확한 출발점이다.

## 7. one-line summary

> 지금 필요한 것은 실패를 숨기거나 즉시 고치는 것이 아니라, segmentation failure / role failure / empty-ref failure / naming failure를 2차 자료로 축적해 object lift hold의 근거와 다음 보정의 방향을 더 선명하게 만드는 것이다.

## 8. integrated hold read

- three-axis interventions changed several failures from `hard fail` to `softened fail`
- but softened fail is still hold evidence
- current major hold evidence classes:
  - `fallback-only grounding`
  - `weak role-like reading only`
  - `candidate still zero`
  - `naming carryover risk`
- these classes should now be read as common gate blockers, not just local failure labels
