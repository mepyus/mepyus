# root_level_file_classification_v1

이 문서는 현재 루트 폴더에 남아 있는 파일들이 **무엇인지**와
그 파일들을 **어떤 기준으로 읽어야 하는지**를 정리한 분류표다.

핵심:
- 루트 = 전부 다 같은 종류의 파일이 아니다
- 지금 루트에 있는 파일들은 대부분 과거 canonical asset 이거나 시스템 앵커다
- 즉 “잡다하게 섞여 있는 파일”처럼 보여도, 운영상 의미가 다른 층이 섞여 있는 상태다

## 1. 루트 파일을 읽는 5개 기준

### A. system_anchor
저장소 전체 현재 상태를 설명하거나 최상위 진입점 역할을 하는 파일

예:
- [vectorfl_status.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_status.md)
- [CURRENT.md](/Users/sungsookim/universe/vectorfl_replica/CURRENT.md)

### B. canonical_source_asset
이미 structured doc routing, receipt, provenance, source_ref 에 연결된 source 문서

예:
- 선언문
- 기준문
- 지시서
- handoff
- 외부 사례 입력 source asset

### C. reference_or_interpretation
철학 해석, 기술 사례 분석, 예시적 비교 재료처럼 참조성/해석성이 강한 문서

예:
- [vectorfl_philosophical_interpretation_v1.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_philosophical_interpretation_v1.md)
- [tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md](/Users/sungsookim/universe/vectorfl_replica/tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md)
- [external_case_example_saltlux_goover_relation_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/external_case_example_saltlux_goover_relation_reading_v0.md)

### D. operational_misc
session note나 보조 문서처럼 저위험 이동 후보인 파일

예:
- [codex_summary_today_session_close_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_summary_today_session_close_v1.md)

### E. root_symlink_anchor
실제 본문은 이미 `source_assets/` 아래에 있지만,
기존 root 경로를 계속 살리기 위해 루트에 symlink 로 남겨 둔 파일

## 2. 현재 루트 파일 실제 분류

### system_anchor
- [CURRENT.md](/Users/sungsookim/universe/vectorfl_replica/CURRENT.md)
- [vectorfl_status.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_status.md)

### canonical_source_asset / declaration
- 실제 배치 위치:
  - [source_assets/declarations](/Users/sungsookim/universe/vectorfl_replica/source_assets/declarations)
- root symlink anchor:
  - [codex_declaration_vectorfl_replica_material_and_operation_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_declaration_vectorfl_replica_material_and_operation_v1.md)
  - [vectorfl_declaration_thought_to_structure_v1.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_declaration_thought_to_structure_v1.md)
  - [vectorfl_declaration_space_as_personal_technology_v1.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_declaration_space_as_personal_technology_v1.md)
  - [vectorfl_replica_space_natural_aging_input_consistency_memory_first_declaration_v1.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_replica_space_natural_aging_input_consistency_memory_first_declaration_v1.md)

### canonical_source_asset / baseline
- 실제 배치 위치:
  - [source_assets/baselines](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines)
- root symlink anchor:
  - [codex_baseline_vectorfl_replica_intake_and_operation_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_baseline_vectorfl_replica_intake_and_operation_v1.md)
  - [codex_baseline_codex_gemini_session_batch_operation_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_baseline_codex_gemini_session_batch_operation_contract_v1.md)
  - [codex_baseline_session_id_and_gemini_log_link_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_baseline_session_id_and_gemini_log_link_contract_v1.md)
  - [exploration_baseline_stage1_space_readability_v1.md](/Users/sungsookim/universe/vectorfl_replica/exploration_baseline_stage1_space_readability_v1.md)

### canonical_source_asset / directive
- 실제 배치 위치:
  - [source_assets/directives](/Users/sungsookim/universe/vectorfl_replica/source_assets/directives)
- root symlink anchor:
  - [codex_directive_core_input_layer_labeler_realization_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_directive_core_input_layer_labeler_realization_v1.md)
  - [codex_directive_document_routing_markers_and_operation_receipt_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_directive_document_routing_markers_and_operation_receipt_v1.md)
  - [codex_directive_label_family_separation_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_directive_label_family_separation_contract_v1.md)
  - [codex_directive_origin_map_minimum_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_directive_origin_map_minimum_v1.md)
  - [codex_directive_program_level_upgrade_delta_based_program_operation_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_directive_program_level_upgrade_delta_based_program_operation_v1.md)
  - [codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md)
  - [codex_directive_vectorfl_replica_bootstrap_and_operation_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_directive_vectorfl_replica_bootstrap_and_operation_v1.md)
  - [thin_operation_rules_lock_v1.md](/Users/sungsookim/universe/vectorfl_replica/thin_operation_rules_lock_v1.md)
  - [llm_response_structure_extraction_and_refinement_checkpoint_v0.md](/Users/sungsookim/universe/vectorfl_replica/llm_response_structure_extraction_and_refinement_checkpoint_v0.md)

### canonical_source_asset / handoff
- 실제 배치 위치:
  - [source_assets/handoffs](/Users/sungsookim/universe/vectorfl_replica/source_assets/handoffs)
- root symlink anchor:
  - [codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md)

### canonical_source_asset / external_case_input
- 실제 배치 위치:
  - [source_assets/external_case_inputs](/Users/sungsookim/universe/vectorfl_replica/source_assets/external_case_inputs)
- root symlink anchor:
  - [external_case_first_pass_saltlux_raw_transcript_input_v2.md](/Users/sungsookim/universe/vectorfl_replica/external_case_first_pass_saltlux_raw_transcript_input_v2.md)
  - [external_case_first_pass_saltlux_secondary_summary_input_v1.md](/Users/sungsookim/universe/vectorfl_replica/external_case_first_pass_saltlux_secondary_summary_input_v1.md)
  - [external_case_first_pass_aifrontier_01_28_input_v1.md](/Users/sungsookim/universe/vectorfl_replica/external_case_first_pass_aifrontier_01_28_input_v1.md)
  - [external_case_first_pass_oh_my_opencode_input_v1.md](/Users/sungsookim/universe/vectorfl_replica/external_case_first_pass_oh_my_opencode_input_v1.md)
  - [external_case_first_pass_enterprise_input_v1.md](/Users/sungsookim/universe/vectorfl_replica/external_case_first_pass_enterprise_input_v1.md)
  - [external_case_first_pass_v1.md](/Users/sungsookim/universe/vectorfl_replica/external_case_first_pass_v1.md)

### reference_or_interpretation
- [vectorfl_philosophical_interpretation_v1.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_philosophical_interpretation_v1.md)
- [tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md](/Users/sungsookim/universe/vectorfl_replica/tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md)
- [external_case_example_saltlux_goover_relation_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/external_case_example_saltlux_goover_relation_reading_v0.md)
- [codex_content_pack.md](/Users/sungsookim/universe/vectorfl_replica/codex_content_pack.md)
- [codex_processor_standard.md](/Users/sungsookim/universe/vectorfl_replica/codex_processor_standard.md)

### operational_misc
- 실제 배치 위치:
  - [source_assets/session_notes/codex_summary_today_session_close_v1.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/session_notes/codex_summary_today_session_close_v1.md)
- root symlink anchor:
  - [codex_summary_today_session_close_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_summary_today_session_close_v1.md)

## 3. 앞으로의 기준

### 네가 신경 써야 하는 것
- raw 파일은 [inputs](/Users/sungsookim/universe/vectorfl_replica/inputs) 아래에 넣는다
- 루트에 새 md를 넣지 않는다

### 내가 지켜야 하는 것
- 새 source md를 만들 때는 [source_assets](/Users/sungsookim/universe/vectorfl_replica/source_assets) 아래에 둔다
- 기존 루트 canonical asset은 이동 전에 batch migration 기준을 먼저 만든다
- 새 문서 생성 시 source 위치를 문서 안에도 분명히 남긴다

## 4. 한 줄 정리
현재 루트 파일들은 “아무거나 섞인 잡파일”이 아니라,
`system anchor + canonical source asset + reference/interpretation + operational misc + root symlink anchor`
로 읽어야 한다.
