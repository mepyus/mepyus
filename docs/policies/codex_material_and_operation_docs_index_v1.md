# codex_material_and_operation_docs_index_v1

## 1. 목적
이 문서는 `vectorfl_replica` 의 문서형 운영 재료 중
현재 최상위 3종 세트를 한 번에 가리키는 index 이다.

이 index 의 목적은 아래와 같다.

- 선언문 / 기준문 / 지시서의 역할을 분리해 읽게 한다.
- Codex가 다음 작업에서 어떤 문서를 먼저 열어야 하는지 빠르게 안내한다.
- 구조화 문서가 엔진 재료라는 사실을 문서 경로 차원에서도 고정한다.

## 2. 3종 세트

### A. 선언문
- [codex_declaration_vectorfl_replica_material_and_operation_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_declaration_vectorfl_replica_material_and_operation_v1.md)
- 역할:
  - 왜 이런 엔진으로 읽는지
  - 문서 재료가 왜 핵심인지
  - Codex 실행이 어디에 위치하는지

### B. 기준문
- [codex_baseline_vectorfl_replica_intake_and_operation_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_baseline_vectorfl_replica_intake_and_operation_v1.md)
- 역할:
  - intake policy
  - input class / processing profile / material grade
  - label / ticket / event / status 역할 분리
  - append-only first / compaction later 기준

### C. 지시서
- [codex_directive_vectorfl_replica_bootstrap_and_operation_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_directive_vectorfl_replica_bootstrap_and_operation_v1.md)
- 역할:
  - 이번 턴에 실제로 무엇을 설치할지
  - event ledger / doc registry / status compaction 연결점
  - 최소 운영 골격 부트스트랩

## 3. Companion Structured Material

### A. 철학적 해석 문서
- [vectorfl_philosophical_interpretation_v1.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_philosophical_interpretation_v1.md)
- 역할:
  - VectorFL / vectorfl_replica 를 의미 숙성 엔진으로 해석
  - fragment / hold / observer / reference / status / append-only 기록의 철학적 근거 제공
  - 실행 지시 이전의 상위 해석 재료이자 별도 ingest 대상 문서

### B. 공간 자연숙성 선언문
- [vectorfl_replica_space_natural_aging_input_consistency_memory_first_declaration_v1.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_replica_space_natural_aging_input_consistency_memory_first_declaration_v1.md)
- 역할:
  - 공간을 강하게 재정의하지 않고 살아 있게 보존하는 운영 원칙 고정
  - 입력기 일관성, 기록/기억 우선, 필요 시 관측이라는 현재 국면의 우선순위 명시
  - 구조화 문서를 입력 재료이자 캘리브레이션 코퍼스로 다루는 방향을 선언 차원에서 잠금

### C. 엔진 잠금 전 사전 셋업 번들
- [codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md)
- 역할:
  - 새 회사/새 프로그램 시나리오를 기준으로 엔진 잠금 전 바닥 셋업 우선순위 고정
  - 선언문/기준문/지시서를 한 번에 담아 intake 후 실행 가능한 작업 묶음으로 제공
  - append safety, 기억층 분리, calibration reference, code reference, operation surface, observation contract, boundary slot 산출을 직접 지시

### D. 프로그램 단 변화분 운용 지시서
- [codex_directive_program_level_upgrade_delta_based_program_operation_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_directive_program_level_upgrade_delta_based_program_operation_v1.md)
- 역할:
  - 전체 재스캔 중심 운영에서 변화분 기록 + 부분 갱신 + 읽기면 렌더 구조로 전환
  - `folder_changes`, `folder_inventory`, `folder_status` 의 3층 분리 기준 고정
  - 새 폴더/문서/규칙이 생길 때 append-only change log 와 국소 inventory 갱신을 우선하도록 지시

### E. folder_status 렌더 계약
- [folder_status_render_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/folder_status_render_contract_v1.md)
- 역할:
  - `folder_status.md` 를 원장이 아니라 inventory 기반 읽기면으로 고정
  - change log -> inventory -> status render 순서를 계약 차원에서 잠금

### F. 변화분 inventory 운용 가이드 / 리뷰
- [folder_inventory_workflow.md](/Users/sungsookim/universe/vectorfl_replica/docs/guides/folder_inventory_workflow.md)
- [folder_inventory_delta_sync_review_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/space_structure/folder_inventory_delta_sync_review_v1.md)
- 역할:
  - 사용자가 변화분 기반 반영 흐름을 빠르게 따라갈 수 있게 설명
  - 최소 구현 범위와 현재 적용 상태를 review 문서로 남김

### G. LLM 답변 구조 증류 / 정련 기준
- [llm_response_structure_extraction_and_refinement_checkpoint_v0.md](/Users/sungsookim/universe/vectorfl_replica/llm_response_structure_extraction_and_refinement_checkpoint_v0.md)
- [llm_response_structure_slot_catalog_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/llm_response_structure_slot_catalog_v0.md)
- [llm_standard_doc_structure_slot_mapping_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/llm_standard_doc_structure_slot_mapping_v0.md)
- [llm_distillation_engine_attachment_feasibility_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/llm_distillation_engine_attachment_feasibility_v0.md)
- [refinement_checkpoint_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/refinement_checkpoint_contract_v1.md)
- 역할:
  - LLM 답변의 문장 표면이 아니라 판단 슬롯을 증류 대상으로 고정
  - 선언문 / 기준문 / 지시서와 LLM 답변 구조의 겹침을 매핑
  - 현재 엔진에 무엇이 바로 붙고, 무엇이 sidecar / observation 레이어가 필요한지 bounded하게 판정
  - 풍부한 해석은 외곽에 두고 코어는 다시 작고 단단하게 정련하는 기준 제공

### H. Thin Operation Rules Lock
- [thin_operation_rules_lock_v1.md](/Users/sungsookim/universe/vectorfl_replica/thin_operation_rules_lock_v1.md)
- [core_promotion_checklist_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/core_promotion_checklist_v1.md)
- [exploration_observation_layer_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/exploration_observation_layer_v1.md)
- [refinement_trigger_rules_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/refinement_trigger_rules_v1.md)
- [core_promotion_checklist_example_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/core_promotion_checklist_example_v1.json)
- [refinement_trigger_check_sample_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts/refinement_trigger_check_sample_v1.json)
- [exploration_observation_sample_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/observer/exploration/json/exploration_observation_sample_v1.json)
- [exploration_observation_sample_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/observer/exploration/md/exploration_observation_sample_v1.md)
- 역할:
  - 코어 승격 기준, 탐색 observation sidecar, 정련 trigger를 얇은 운영 규칙으로 잠금
  - 코어 대수술 없이 반복 가능한 observer/runtime 기록 슬롯을 확보
  - 다음 탐색 사례와 정련 사례를 같은 형식으로 누적할 수 있는 최소 표면 제공

### I. Flow-Aware Operating Entry Set
- [phase1_25_flow_aware_operating_entrypoint_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_operating_entrypoint_v0.md)
- [phase1_25_flow_aware_reader_operator_index_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_reader_operator_index_v0.md)
- [phase1_25_flow_aware_trigger_checklist_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_25_flow_aware_trigger_checklist_v0.md)
- [phase1_26_flow_aware_reopen_path_map_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_26_flow_aware_reopen_path_map_v0.md)
- [phase1_27_flow_aware_evidence_log_template_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_27_flow_aware_evidence_log_template_v0.md)
- [phase1_27_flow_aware_reopen_permission_boundary_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_27_flow_aware_reopen_permission_boundary_v0.md)
- [phase1_28_flow_aware_evidence_log_storage_convention_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/phase1_28_flow_aware_evidence_log_storage_convention_v0.md)
- [runtime/reopen_evidence_logs/flow_aware/README.md](/Users/sungsookim/universe/vectorfl_replica/runtime/reopen_evidence_logs/flow_aware/README.md)
- 역할:
  - global default 유지 위에서 bounded flow-aware selection을 운용하는 reader/operator entry set
  - allow-list / block-list / protected default / unresolved hold를 한 번에 참조하게 함
  - trigger-based reopen만 허용하고, evidence log 저장 위치와 기록 형식까지 실제 파일 경로 기준으로 고정
## 4. 현재 읽기 순서
1. 선언문
2. 기준문
3. 지시서
4. 철학적 해석 문서
5. 공간 자연숙성 선언문
6. 엔진 잠금 전 사전 셋업 번들
7. 프로그램 단 변화분 운용 지시서
8. folder_status 렌더 계약
9. 변화분 inventory 운용 가이드 / 리뷰
10. LLM 답변 구조 증류 / 정련 기준
11. Thin Operation Rules Lock
12. Flow-Aware Operating Entry Set
## 5. 운영 연결점
이 문서군은 아래 운영 구조와 직접 연결된다.

- `runtime/events/`
  - append-only event ledger
- `runtime/manifests/`
  - doc registry / ticket registry / provenance link
- `runtime/manifests/folder_changes/`
  - folder-level change log
- `runtime/manifests/folder_inventory/`
  - folder current-state inventory
- `*_status.md`
  - inventory 기반 읽기면
- `runtime/reopen_evidence_logs/flow_aware/`
  - trigger-based bounded reopen evidence log landing spot
## 6. 현재 판정
- 이 문서들은 단순 prompt archive 가 아니라 `structured_internal_doc` 로 읽는다.
- material grade 는 기본적으로 `grade_a`
- processing profile 은 `minimal_preprocess` 또는 `execution_coupled`
- execution linkable 은 `yes`
