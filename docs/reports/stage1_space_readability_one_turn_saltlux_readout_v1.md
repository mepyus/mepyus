# stage1_space_readability_one_turn_saltlux_readout_v1

## 목적
`Saltlux / ontology / graph rag / multi-agent` 입력을
현재 엔진 자산 기준으로 어느 정도까지 의미 판독으로 반환할 수 있는지
한 번의 샘플 readout으로 보여준다.

## input
- primary source:
  - [tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md](/Users/sungsookim/universe/vectorfl_replica/tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1.md)
- relation example:
  - [external_case_example_saltlux_goover_relation_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/external_case_example_saltlux_goover_relation_reading_v0.md)

## focus
- focus_anchor:
  - `ontology`
  - `graph_rag`
  - `role_based_agent`
  - `grounding`
- focus_labels:
  - `reference`
  - `external_case`
  - `structure_comparison_material`

## related assets now
- [external_case_relation_reading_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/external_case_relation_reading_contract_v1.md)
- [observation_probe_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/observation_probe_contract_v1.md)
- [operation_surface_pointer_spec_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/operation_surface_pointer_spec_v1.md)
- [codex_baseline_codex_gemini_session_batch_operation_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_baseline_codex_gemini_session_batch_operation_contract_v1.md)
- [vectorfl_declaration_thought_to_structure_v1.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_declaration_thought_to_structure_v1.md)
- [vectorfl_declaration_space_as_personal_technology_v1.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_declaration_space_as_personal_technology_v1.md)

## relation readout

### A. structure borrowable
- relation_kind:
  - `STRUCTURE_BORROWABLE`
- user-language reading:
  - 이 사례는 “지식의 뼈대와 실행층을 섞지 않는다”는 점에서 우리 엔진 구조와 닿는다.
  - 그대로 복제 대상은 아니지만, 역할 분리와 read-only observer 분리 원리는 차용 가능하다.
- relation_reason:
  - 우리 쪽에도 contracts/policies/guides 분리, Codex/Gemini/User 역할 분리, latest/per-run pointer/evidence 분리가 이미 있다.
- borrowable_structure:
  - 의미층과 실행층을 분리하는 원리
  - 결과를 근거면과 읽기면으로 나누는 원리

### B. different meaning, same context
- relation_kind:
  - `DIFFERENT_MEANING_SAME_CONTEXT`
- user-language reading:
  - 저쪽은 ontology/graph를 더 강한 기준면으로 쓰고, 우리는 provenance/evidence/readback을 중심으로 둔다.
  - 구현은 다르지만 “결과를 다시 근거와 대조한다”는 문제의식은 같은 맥락이다.
- relation_reason:
  - `grounding` 과 우리 `receipt/provenance/pointer` 는 다른 층에서 같은 문제를 푼다.

### C. same context, different flow
- relation_kind:
  - `SAME_CONTEXT_DIFFERENT_FLOW`
- user-language reading:
  - Saltlux는 ontology 선고정 경향이 강하고, 우리는 후 구조화와 응결 우선 쪽이다.
  - 같은 문제권을 다루지만 흐름이 다르므로 바로 코어에 넣으면 안 된다.
- not_adopted_reason:
  - 현재 우리 엔진은 희미한 연결 보존과 후 구조화를 핵심으로 삼고 있다.

### D. separated for now
- relation_kind:
  - `SEPARATED`
- user-language reading:
  - enterprise orchestration, hard ontology schema, 전역 command center 구상은 지금 단계에서 분리 유지가 맞다.
- separation_reason:
  - 현재 단계 목표는 stage1 readability와 bounded observation이지, 기업형 orchestration 재현이 아니다.

## write trace available now
- receipt:
  - [doc_tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1_operation_receipt.md](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts/doc_tech_analysis_saltlux_goover_ontology_based_multi_agent_system_v1_operation_receipt.md)
- pointer:
  - [operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)
- provenance:
  - [provenance_compacted_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/provenance_compacted_latest.md)
- exploration grammar seed:
  - [external_case_example_saltlux_goover_relation_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/external_case_example_saltlux_goover_relation_reading_v0.md)

## current limit
- 현재 이 판독은 문서 예시와 사람이 읽는 해석에 기대고 있다.
- runtime 표준 산출로 `relation_kind`, `relation_reason`, `borrowable_structure`가 자동 반환되지는 않는다.

## future use hint
- 탐색 기능 정의 예시
- relation reasoning sidecar template 입력
- Gemini observer briefing seed
- “구조 차용 가능 / 분리 유지” 분류 예시
