[[A]] [[OBJ:repeated_second_order_pattern_table_draft_v1]] [[SEM:pattern_first_table_before_object_lift]]

# repeated second-order pattern table draft v1

## 1. purpose

- object lift 이전에는 객체명보다 반복 패턴을 먼저 정리한다.

## 2. table schema draft

- pattern_id
- pattern_type
- supporting_assets
- supporting_first_pass_patterns
- rereading_modes
- repeated_outputs
- readable_conditions
- repeated_failures
- domain_specific_suspicion
- reusable_attitude_hint
- candidate_status
- hold_reason

## 3. current draft rows

- `pattern_question_opening_transition`
  - pattern_type: repeated question opening
  - supporting_assets: `youtube_03_22`
  - supporting_first_pass_patterns: object candidates, relation hints, top question-intent windows
  - rereading_modes: purpose synthesis, question block review
  - repeated_outputs: question-inducing candidate, question_seed_block
  - domain_specific_suspicion: high_ai_agent_transition
  - reusable_attitude_hint: 질문 opening은 객체 다중 생존 + transition/execution shift 조합에서 잘 뜬다
  - candidate_status: hold
  - hold_reason: 아직 AI 도메인 밖 반복 확인이 없다

- `pattern_context_unit_from_pass_difference`
  - pattern_type: repeated context-unit reconstruction
  - supporting_assets: `youtube_03_22`
  - supporting_first_pass_patterns: top objects, top layers, question-inducing candidates
  - rereading_modes: multi-pass interpretation
  - repeated_outputs: context unit, pivot, compression node
  - domain_specific_suspicion: medium
  - reusable_attitude_hint: pass 차이가 클수록 문단보다 살아 있는 context unit이 드러난다
  - candidate_status: hold
  - hold_reason: 다른 도메인 반복 확인이 아직 없다

- `pattern_role_shift_by_context_frame`
  - pattern_type: repeated role shift
  - supporting_assets: `youtube_03_22`
  - supporting_first_pass_patterns: context unit, local/page/comparison rereading
  - rereading_modes: paragraph role interpretation
  - repeated_outputs: question_seed_block, strategy_pivot_block, compression_node
  - domain_specific_suspicion: medium_high
  - reusable_attitude_hint: 같은 단락도 context frame이 바뀌면 역할이 이동한다
  - candidate_status: hold
  - hold_reason: 현재는 heading-driven selection이 포함되어 있다

- `pattern_single_operational_block_collapse`
  - pattern_type: domain comparison collapse pattern
  - supporting_assets: `claude_code_index`
  - supporting_first_pass_patterns: single block, single window, broad object/layer firing
  - rereading_modes: purpose synthesis, question block review, multi-pass interpretation
  - repeated_outputs: one mega candidate window, weak pass difference, blank context unit refs
  - domain_specific_suspicion: high_format_dependency
  - reusable_attitude_hint: split가 약한 입력에서는 2차 보정 태도가 유지되어도 granularity는 쉽게 무너질 수 있다
  - candidate_status: collect_only
  - hold_reason: 아직 다른 non-dialogue domain과 비교가 없다

- `pattern_ai_object_vocabulary_overfire`
  - pattern_type: domain leakage pattern
  - supporting_assets: `claude_code_index`
  - supporting_first_pass_patterns: AI-derived object candidates on code/tool asset
  - rereading_modes: purpose synthesis, multi-pass interpretation
  - repeated_outputs: `AI의 미래`, `일의 미래`, `에이전트 애플리케이션` overfire
  - readable_conditions: AI dialogue naming scaffold가 잔존하는 상태
  - repeated_failures: naming은 살아도 supporting context structure는 약함
  - domain_specific_suspicion: very_high
  - reusable_attitude_hint: 객체명보다 객체가 떠오르는 조건을 먼저 분리해야 과잉 일반화를 막을 수 있다
  - candidate_status: hold
  - hold_reason: naming layer가 아직 AI dialogue scaffold를 강하게 끌고 있다

- `pattern_heading_dependency_role_failure`
  - pattern_type: repeated failure pattern
  - supporting_assets: `claude_code_index`
  - supporting_first_pass_patterns: paragraph pointer 부족, heading mismatch
  - rereading_modes: paragraph role interpretation
  - repeated_outputs: role reading not executed
  - readable_conditions: stable heading or equivalent paragraph pointer needed
  - repeated_failures: heading not found, role selection fails before rereading
  - domain_specific_suspicion: very_high_format_dependency
  - reusable_attitude_hint: role shift 태도와 role-reading 기관을 분리해서 축적해야 한다
  - candidate_status: collect_only
  - hold_reason: 역할 이동 자체보다 heading scaffold dependency가 더 크게 드러난다

- `pattern_empty_ref_context_unit`
  - pattern_type: repeated failure pattern
  - supporting_assets: `claude_code_index`
  - supporting_first_pass_patterns: weak window diversity, pass difference without anchors
  - rereading_modes: multi-pass interpretation
  - repeated_outputs: context unit names survive but refs empty
  - readable_conditions: non-empty window refs and pointer granularity
  - repeated_failures: context-unit wording survives without grounded references
  - domain_specific_suspicion: high_scaffold_dependency
  - reusable_attitude_hint: context unit은 naming보다 pointer grounding부터 봐야 한다
  - candidate_status: collect_only
  - hold_reason: ref가 비면 context unit은 아직 lift support가 아니다

## 4. one-line summary

> object lift 이전에는 `객체명`보다 `반복되는 2차 패턴`을 먼저 표로 묶어야 한다.
