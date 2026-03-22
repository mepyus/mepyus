# engine work summary by file

## 1. summary

이 문서는 지금까지 민 엔진 작업을 파일 기준으로 정리한 요약이다.

핵심 방향은 아래였다.

- `space app`이 아니라 `연결 층위 엔진`으로 재정의
- `canonical 승인`과 `space 인정` 분리
- weak / blocked / review / proposal을 보류 자산으로 보존
- policy / fixture / lifecycle / ledger / runner 구조를 실제 운영 접합부로 고정
- approval phase를 열어 승인 문법을 코어 바깥 policy unit으로 끌어올림

## 2. core runtime files

### [live_input_space.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input_space.py)

역할:
- mixed pair 평가의 orchestrator
- evidence collect
- policy call
- output surface assemble

이번 phase에서 추가/변경된 것:
- possibility / review / canonical 흐름 유지
- executor / lifecycle / output surface 경계 주석 추가
- top-level lifecycle:
  - `trace_temperature`
  - `lifecycle_stage`
  - `lifecycle_reason`
- top-level timestamp:
  - `evaluated_at`
  - `state_signature`
- promotion review surface에 approval/lifecycle/timestamp 정보 연결
- approval policy 호출부로 전환:
  - coarse `bridge_mode`
  - approval grammar
  - canonical anchor approval
  - canonical review decision
  - canonical approval readiness

현재 읽기:
- 코어는 아직 크지만, 규칙을 직접 품는 파일이 아니라 orchestration 중심 파일로 이동 중

### [review_policy_types.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policy_types.py)

역할:
- review / lifecycle / space entry 관련 policy context/result 타입 정의

추가된 핵심 타입:
- `PromotionPolicyContext`, `PromotionPolicyResult`
- `CrossPathPolicyContext`, `CrossPathPolicyResult`
- `DirectOverlapFamilyPolicyContext`, `DirectOverlapFamilyPolicyResult`
- `DirectOverlapAggregatePolicyContext`, `DirectOverlapAggregatePolicyResult`
- `CanonicalizationPolicyContext`, `CanonicalizationPolicyResult`
- `SpaceEntryPolicyContext`, `SpaceEntryPolicyResult`
- `LifecyclePolicyContext`, `LifecyclePolicyResult`
- `ReviewTimestamp`

현재 읽기:
- review 계층의 입력/출력 경계선

### [review_policies.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_policies.py)

역할:
- review lane과 lifecycle 관련 정책 함수 모음

분리된 정책 축:
- `evaluate_promotion_review_policy(...)`
- `evaluate_cross_path_overlap_policy(...)`
- `evaluate_direct_overlap_family_policy(...)`
- `evaluate_direct_overlap_aggregate_policy(...)`
- `evaluate_canonicalization_family_policy(...)`
- `evaluate_space_entry_policy(...)`
- `evaluate_review_lifecycle_policy(...)`

현재 읽기:
- approval 이전 단계의 review grammar와 lifecycle grammar를 담는 정책 파일

### [review_output_surface.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_output_surface.py)

역할:
- policy 결과를 읽기 좋은 review surface로 조립

추가된 것:
- `assemble_promotion_review_surface(...)`
- `assemble_cross_path_review_surface(...)`
- 내부 sub-assembler
  - anchor
  - threshold
  - live-side
  - cross-path
  - canonicalization
  - direct overlap
  - space entry

현재 읽기:
- output surface boundary

### [approval_policy_types.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/approval_policy_types.py)

역할:
- 승인 정책 phase 전용 타입 정의

추가된 핵심 타입:
- `ApprovalGrammarContext`, `ApprovalGrammarResult`
- `CanonicalAnchorApprovalContext`, `CanonicalAnchorApprovalResult`
- `BridgeModeApprovalContext`, `BridgeModeApprovalResult`
- `CanonicalReviewDecisionContext`, `CanonicalReviewDecisionResult`
- `CanonicalApprovalStatusContext`, `CanonicalApprovalStatusResult`

현재 읽기:
- approval phase의 입력/출력 경계선

### [approval_policies.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/approval_policies.py)

역할:
- approval phase 정책 함수 모음

현재 분리된 승인 축:
- `evaluate_approval_grammar_policy(...)`
- `evaluate_canonical_anchor_approval_policy(...)`
- `evaluate_bridge_mode_approval_policy(...)`
- `evaluate_canonical_review_decision_policy(...)`
- `evaluate_canonical_approval_status_policy(...)`

현재 읽기:
- threshold 변경 전 단계의 approval grammar 본진

## 3. fixture / operation files

### [review_fixture_manifest.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_fixture_manifest.py)

역할:
- fixture/control manifest loader

핵심:
- immutable regression fixture와 mutable exploration control 분리
- manifest field:
  - `fixture_kind`
  - `expected_bridge_mode`
  - `expected_review_state`
  - `expected_lifecycle_temperature`
  - `expected_lifecycle_stage`
  - `allowed_drift`

현재 읽기:
- fixture boundary

### [review_state_ledger.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/review_state_ledger.py)

역할:
- persisted review ledger read/write

핵심:
- `last_reviewed_at`
- `last_state_signature`
- `last_bridge_mode`
- `last_review_state`
- `last_trace_temperature`
- `last_lifecycle_stage`
- `review_count`
- `summarize_review_state_entry(...)`
  - `revisit_recommended`
  - `warm_downgrade_candidate`

현재 읽기:
- ledger body의 운영 접합부

### [run_review_fixture_check.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_review_fixture_check.py)

역할:
- fixture manifest를 읽고 현재 runtime 판정을 점검하는 lightweight runner

핵심:
- immutable / mutable 분리 확인
- bridge/review/lifecycle expectation 확인
- `state_signature` diff 확인
- ledger baseline 비교
- persisted review count 갱신

현재 읽기:
- 운영 검증 entrypoint

## 4. supporting runtime work files

### [imported_material_contract.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/imported_material_contract.py)

역할:
- imported docs의 post-materialization contract 복원

복원한 축:
- `anchor_bundle`
- `processing_values`
- `transformable_handles`
- `source_local_ref`
- translated handles additive attachment

### [imported_material_probe.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/imported_material_probe.py)

역할:
- imported upstream contract / flatten / local readiness / processing flatness probe

사용한 지표 예:
- presence ratio
- local_ref 분화
- signature unique ratio
- flatness score
- translation effect

### [local_ref_handle_translation.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/local_ref_handle_translation.py)

역할:
- local_ref-scoped bounded translation helper

핵심:
- `source_local_ref` 범위에서만 translated handles 생성
- `original_handle / translated_handle / translation_basis / translation_scope / translation_confidence`
  추적

### [labeler.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/labeler.py)

역할:
- imported docs processing refinement

핵심:
- processor_compare 문서 계열에 local cue refinement 추가
- `doc_005`, `doc_006` processing flatness 완화

### [live_input.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input.py)

역할:
- live input metadata assembly

핵심:
- observer-aware baseline
- processing / anchor / transformable handle handoff 유지

### [runtime_space_anchor_sync.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/runtime_space_anchor_sync.py)

역할:
- local space baseline sync

핵심:
- `processing_baseline`
- `observer_or_ambiguity_trace`
- `state_transition_summary`
- `bridge_exposure_count`

## 5. persisted/runtime data files

### [review_fixture_manifest_v0.json](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/review_fixture_manifest_v0.json)

역할:
- fixture/control manifest source

현재 기준:
- immutable regression fixture 3개
- mutable exploration control 3개

### [review_state_ledger.json](/Users/sungsookim/universe/vectorfl_replica/runtime/review_ledgers/review_state_ledger.json)

역할:
- fixture별 persisted review state

현재 기준:
- 각 fixture의 마지막 읽힘과 signature, review count 저장

## 6. key policy/report documents

### engine definition / philosophy

- [engine_definition_and_structure_20260321.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/engine_definition_and_structure_20260321.md)
- [space_is_a_view_not_the_engine_20260321.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/space_is_a_view_not_the_engine_20260321.md)
- [space_vs_canonical_policy_split_20260321.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/space_vs_canonical_policy_split_20260321.md)
- [engine_body_structure_draft_v0.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/engine_body_structure_draft_v0.md)

역할:
- 엔진 본체 정의
- canonical과 space의 분리
- ledger/layer/workbench/projection 구조 정의

### checkpoints / architecture stabilization

- [engine_space_entry_checkpoint_20260321.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/engine_space_entry_checkpoint_20260321.md)
- [policy_executor_boundary_round1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/policy_executor_boundary_round1.md)
- [policy_executor_boundary_round2.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/policy_executor_boundary_round2.md)
- [policy_executor_boundary_round3.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/policy_executor_boundary_round3.md)
- [policy_executor_boundary_round4.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/policy_executor_boundary_round4.md)
- [policy_executor_boundary_stabilization.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/policy_executor_boundary_stabilization.md)
- [fixture_control_operation_stabilization.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/fixture_control_operation_stabilization.md)
- [lifecycle_ledger_semantics_stabilization.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/lifecycle_ledger_semantics_stabilization.md)

역할:
- 구조 완성선
- stabilization 고정선

### operation / verification

- [review_fixture_manifest_round1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/review_fixture_manifest_round1.md)
- [review_fixture_check_round1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/review_fixture_check_round1.md)
- [review_fixture_check_round2.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/review_fixture_check_round2.md)
- [review_fixture_check_round3.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/review_fixture_check_round3.md)
- [review_timestamp_round1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/review_timestamp_round1.md)

역할:
- fixture / lifecycle / timestamp / ledger 운영 검증

### phase choice / approval phase

- [next_phase_options_draft.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/next_phase_options_draft.md)
- [approval_policy_phase_round1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/approval_policy_phase_round1.md)
- [approval_policy_phase_round2.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/approval_policy_phase_round2.md)
- [approval_policy_phase_round3.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/approval_policy_phase_round3.md)
- [approval_policy_phase_round4.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/approval_policy_phase_round4.md)
- [approval_policy_phase_round5.md](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare/reports/approval_policy_phase_round5.md)

역할:
- 다음 Phase 선택
- approval phase 진입
- approval policy extraction 경과

## 7. current state by theme

### engine body

- ledger + layer + local workbench + projection 구조로 재정의 완료

### policy structure

- review policy와 approval policy가 분리되기 시작했고, approval phase는 핵심 결정부까지 상당수 분리됨

### operation structure

- fixture manifest
- fixture runner
- lifecycle grammar
- timestamp
- persisted ledger
까지 고정

### current main case

- `probe -> doc_006`
  - `possibility_candidate / candidate`
  - `space_entry_state = structural_led_space_pre_entry`
  - `canonical_review_focus_class = cross_path_corroboration`
  - `canonical_approval_readiness_class = cross_path_corroboration_pending`

### current controls

- `probe -> doc_005`, `probe -> doc_004`
  - `none / translation_missing`
  - `warm / blocked_waiting_revisit`

## 8. final reading

지금까지의 작업은 크게 세 층으로 요약된다.

1. 엔진 철학과 본체 정의 정리
2. policy / fixture / lifecycle / ledger 구조 안정화
3. approval phase 진입과 승인 문법 분리

즉 현재 엔진은:

**입력-라벨-앵커 결과 위에서 canonical / possibility / review / blocker / proposal / pre-entry를 저장·보류·재판독하는 연결 층위 엔진이며, 그 본체는 ledger와 layer이고, local workbench가 실제 판단 현장이다.**
