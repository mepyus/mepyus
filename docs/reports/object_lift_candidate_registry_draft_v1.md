[[A]] [[OBJ:object_lift_candidate_registry_draft_v1]] [[SEM:holding_room_for_pre_object_lift_candidates]]

# object-lift candidate registry draft v1

## 1. purpose

- 이 문서는 상위 객체 확정 저장소가 아니라, 승격 전 후보 보관소다.

## 2. registry fields

- candidate_name
- observed_in_assets
- source_patterns
- second_order_support
- domain_specific_suspicion
- candidate_status
- hold_reason
- next_check

## 3. current candidates

- `business_power_shift`
  - observed_in_assets: `youtube_03_22`
  - source_patterns: agent app, bundle-unbundle, moat, workflow transition
  - second_order_support: question-inducing block review, purpose synthesis, paragraph role reading
  - domain_specific_suspicion: high
  - candidate_status: hold
  - hold_reason: AI/agent business transition에 강하게 묶여 있고, 비교 도메인에서 segmentation failure와 naming leakage를 넘지 못했다
  - next_check: non-AI technical domain에서 유사 power-shift reading이 뜨는지 보기

- `orchestration`
  - observed_in_assets: `youtube_03_22`
  - source_patterns: agent interface, delegated execution, external tool/domain coordination
  - second_order_support: purpose synthesis, context unit reconstruction
  - domain_specific_suspicion: medium_high
  - candidate_status: hold
  - hold_reason: 이름 자체가 상위 개념이어서 과잉 일반화 위험이 크고, context-unit ref 안정성이 아직 부족하다
  - next_check: code/tool domain에서 반복되는지 보기

- `domain_to_component_reframing`
  - observed_in_assets: `youtube_03_22`
  - source_patterns: 앱 대체, 기존 도메인 부품화, 대리 조작 레이어
  - second_order_support: question-inducing block review, paragraph role reading
  - domain_specific_suspicion: high
  - candidate_status: hold
  - hold_reason: 아직 AI agent application 문맥 외 근거가 부족하고, paragraph role layer가 heading dependency를 벗어나지 못했다
  - next_check: 다른 기술 도메인에서 상위 인터페이스가 하위 시스템을 부품화하는 사례를 확인

## 3. comparison-domain caution added

- `claude_code_index` 비교 결과는 새로운 object-lift candidate를 즉시 추가하라는 신호보다, 기존 후보를 계속 hold해야 한다는 증거로 읽는 편이 맞다.
- 특히 아래가 더 선명해졌다.
  - 이름 수준의 객체는 다른 도메인에서 쉽게 leakage 또는 overfire가 생긴다
  - object lift 이전에는 `이름이 다시 떴는가`보다 `그 이름을 떠오르게 한 조건이 유지됐는가`를 먼저 봐야 한다

### current no-add decision

- no new candidate added from `claude_code_index`
  - reason: 비교 도메인에서는 새 상위 객체보다 `single operational block collapse`, `AI object vocabulary overfire`, `heading dependency` 같은 보류 사유가 더 강하게 드러났다
  - implication: registry는 당분간 후보 보관소이면서 동시에 `왜 아직 올리지 않는가`를 기록하는 장소로 기능해야 한다

### structured hold dimensions

- segmentation_hold:
  - block/window collapse가 심하면 상위 객체 support를 약화시킴
- scaffold_hold:
  - heading dependency, empty ref context unit이 있으면 구조 support가 불충분함
- naming_hold:
  - object naming carryover 또는 overfire가 있으면 이름 자체를 승격 근거로 쓰면 안 됨
- evidence_hold:
  - reusable attitude는 살아도 cross-domain evidence가 아직 부족함

### current intervention order connection

- first_check_axis: segmentation
- second_check_axis: pointer
- third_check_axis: heading

즉 registry의 hold 이유는 단순 보수성 메모가 아니라, 어떤 dependency axis를 먼저 줄여야 하는지와 직접 연결된다.

### update after segmentation support probe

- segmentation support applied: yes
- current read:
  - collapse 완화만으로는 candidate 승격 근거가 충분히 생기지 않았다
  - support 이후에도 object naming은 여전히 hold이며, grounding 부족이 더 선명해졌다
- implication:
  - registry candidate는 계속 hold
  - next check는 pointer axis에서 grounding이 살아나는지 보는 쪽으로 이동

### update after pointer stabilization probe

- pointer stabilization applied: yes
- current read:
  - 일부 context unit과 naming 후보는 `better-supported hold` 상태로 이동했다
  - 그러나 direct grounded support는 아직 부족하고, fallback evidence에 많이 기대고 있다
- implication:
  - registry candidate는 계속 hold
  - hold reason은 이제 `unsupported naming`뿐 아니라 `fallback-only grounding`도 함께 포함해야 한다

### update after heading-independent role probe

- heading probe applied: yes
- current read:
  - role-like reading은 일부 살아났지만 generalized paragraph role support는 여전히 부족하다
  - role-related candidate를 새로 승격할 근거는 아니다
- implication:
  - registry candidate는 계속 hold
  - hold reason에는 `weak role-like reading only`도 추가되어야 한다

### integrated candidate state wording

- `better-supported hold`
  - evidence coverage improved, but mostly fallback
- `weak repeated but still hold`
  - pattern survives across probes, but not strongly enough for lift
- `not-yet-direct`
  - grounding improved, but direct support is still absent
- `gate-blocked hold`
  - common blockers:
    - question-inducing candidate absence
    - fallback grounding dominance
    - weak role-like only
    - pivot/compression non-recurrence
    - scaffold carryover risk

## 4. one-line summary

> object lift 전에는 상위 객체를 확정하지 말고, 이름과 근거와 hold 이유를 가진 후보 보관소에 먼저 넣는다.
