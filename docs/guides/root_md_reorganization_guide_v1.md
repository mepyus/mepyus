# root_md_reorganization_guide_v1

이 문서는 루트에 섞여 있는 md 파일을 어떻게 읽고, 앞으로 어디에 둘지 정리하는 가이드다.

## 왜 바로 안 옮기나
- 루트 md 중 다수는 이미 structured doc routing 에 들어갔다.
- receipt, provenance, label packet, origin map, observer readout 이 기존 경로를 source_ref 로 들고 있다.
- 그래서 지금 한 번에 이동하면 추적성과 참조 안정성이 깨질 수 있다.

즉 현재 원칙은:
- 기존 루트 md = legacy canonical root assets 또는 root symlink anchors
- 새 md = 가능한 한 전용 폴더로 분리

## 앞으로의 기본 위치

### 선언문
- 위치: [source_assets/declarations](/Users/sungsookim/universe/vectorfl_replica/source_assets/declarations)
- 예:
  - `vectorfl_declaration_*`
  - `codex_declaration_*`

### 기준문 / baseline
- 위치: [source_assets/baselines](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines)
- 예:
  - `codex_baseline_*`
  - `exploration_baseline_*`

### 지시서 / directive
- 위치: [source_assets/directives](/Users/sungsookim/universe/vectorfl_replica/source_assets/directives)
- 예:
  - `codex_directive_*`
  - `thin_operation_rules_lock_v1.md`
  - `llm_response_structure_extraction_and_refinement_checkpoint_v0.md`

### handoff
- 위치: [source_assets/handoffs](/Users/sungsookim/universe/vectorfl_replica/source_assets/handoffs)
- 예:
  - `codex_handoff_*`

### 외부 사례 입력 source
- 위치: [source_assets/external_case_inputs](/Users/sungsookim/universe/vectorfl_replica/source_assets/external_case_inputs)
- 예:
  - `external_case_first_pass_*_input_*.md`

### 세션 메모 / close note
- 위치: [source_assets/session_notes](/Users/sungsookim/universe/vectorfl_replica/source_assets/session_notes)
- 예:
  - `codex_summary_today_session_close_v1.md`

## 현재 루트 md 읽기 분류

### root symlink anchor
- 아래 파일들 중 일부는 루트에서도 보이지만, 실제 본문은 `source_assets/` 아래에 있다.
- 루트 경로는 기존 receipt / provenance / source_ref 안정성을 위해 남겨 둔 anchor다.
- 즉 “루트에 보인다 = 실제 본문이 루트에 있다”로 읽지 않는다.

### 선언문 계열
- 루트 symlink anchor:
  - `codex_declaration_vectorfl_replica_material_and_operation_v1.md`
  - `vectorfl_declaration_thought_to_structure_v1.md`
  - `vectorfl_declaration_space_as_personal_technology_v1.md`
  - `vectorfl_replica_space_natural_aging_input_consistency_memory_first_declaration_v1.md`
- 실제 배치 위치:
  - [source_assets/declarations](/Users/sungsookim/universe/vectorfl_replica/source_assets/declarations)

### 기준문 / baseline 계열
- 루트 symlink anchor:
  - `codex_baseline_vectorfl_replica_intake_and_operation_v1.md`
  - `codex_baseline_codex_gemini_session_batch_operation_contract_v1.md`
  - `codex_baseline_session_id_and_gemini_log_link_contract_v1.md`
  - `exploration_baseline_stage1_space_readability_v1.md`
- 실제 배치 위치:
  - [source_assets/baselines](/Users/sungsookim/universe/vectorfl_replica/source_assets/baselines)

### 지시서 계열
- 루트 symlink anchor:
  - `codex_directive_*`
  - `thin_operation_rules_lock_v1.md`
  - `llm_response_structure_extraction_and_refinement_checkpoint_v0.md`
- 실제 배치 위치:
  - [source_assets/directives](/Users/sungsookim/universe/vectorfl_replica/source_assets/directives)

### handoff 계열
- 루트 symlink anchor:
  - `codex_handoff_structured_doc_routing_stability_baseline_lock_and_next_step_directive_v1.md`
- 실제 배치 위치:
  - [source_assets/handoffs](/Users/sungsookim/universe/vectorfl_replica/source_assets/handoffs)

### 외부 사례 입력 계열
- 루트 symlink anchor:
  - `external_case_first_pass_saltlux_raw_transcript_input_v2.md`
  - `external_case_first_pass_saltlux_secondary_summary_input_v1.md`
  - `external_case_first_pass_aifrontier_01_28_input_v1.md`
  - `external_case_first_pass_oh_my_opencode_input_v1.md`
  - `external_case_first_pass_enterprise_input_v1.md`
- 실제 배치 위치:
  - [source_assets/external_case_inputs](/Users/sungsookim/universe/vectorfl_replica/source_assets/external_case_inputs)

### 철학 / 해석 / 참고 계열
- `vectorfl_philosophical_interpretation_v1.md`
- `tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md`
- `external_case_example_saltlux_goover_relation_reading_v0.md`

### 임시 / legacy misc 후보
- `1.md`
- `basic1.md`
- `basic3.md`
- `basic4.md`
- `basic5.md`
- `canva.md`
- `openai_02_11.md`
- `AI_bulider_03_05.md`
- `claudecomplier_02_28.md`
- `youtube_01_28.md`
- `youtube_01_29.md`
- `youtube_01_30.md`
- `youtube_03_18.md`
- `youtube_03_22.md`

## 정리 원칙
1. 기존 canonical root asset 는 무작정 옮기지 않는다.
2. 저위험 항목은 실제 본문을 `source_assets/` 로 옮기고 루트에는 symlink anchor 를 남길 수 있다.
3. 새 source asset 는 `source_assets/` 아래 적절한 폴더로 넣는다.
4. raw input 은 [inputs](/Users/sungsookim/universe/vectorfl_replica/inputs) 아래에 둔다.
5. 해석 결과는 `docs/` 와 `runtime/` 으로 분리한다.
6. 고위험 canonical asset 이동은 migration batch 로 묶고 reference update 를 같이 한다.

## 다음 단계
- 지금은 분류 인덱스와 전용 폴더 기준을 잠근 상태다.
- 실제 물리 이동은 저위험 항목부터 진행하고, 고위험 canonical asset 은 나중에 batch migration 으로 다루는 것이 맞다.
