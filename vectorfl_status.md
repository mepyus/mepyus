# vectorfl_status

## 0. Current Integrated Engine Pointer

현재 통합엔진 관련 자료 지도는 아래 문서가 우선 포인터다.

- [vectorfl_integrated_engine_asset_index_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/vectorfl_integrated_engine_asset_index_v0.md)
- [vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md)
- [integrated_engine_common_language_extraction_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_common_language_extraction_v1.md)
- [integrated_engine_vectorfl_surface_elevated_direction_note_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_vectorfl_surface_elevated_direction_note_v1.md)
- [integrated_engine_exploration_question_set_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_exploration_question_set_v1.md)
- [integrated_engine_exploration_question_set_v1_1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_exploration_question_set_v1_1.md)
- [integrated_engine_language_harvest_run_20260414_v1_1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_language_harvest_run_20260414_v1_1.md)
- [integrated_engine_common_language_extraction_v2.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_common_language_extraction_v2.md)
- [integrated_engine_common_language_extraction_v3.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_common_language_extraction_v3.md)
- [integrated_engine_common_language_round3_boundary_report_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_common_language_round3_boundary_report_v1.md)
- [integrated_engine_setup_working_lexicon_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_setup_working_lexicon_v0.md)
- [integrated_engine_transfer_packet_minimum_slots_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_transfer_packet_minimum_slots_v0.md)
- [integrated_engine_operating_object_slot_movement_rules_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_operating_object_slot_movement_rules_v0.md)
- [integrated_engine_anchor_object_minimum_fields_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_anchor_object_minimum_fields_v0.md)
- [integrated_engine_maturation_object_minimum_fields_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_maturation_object_minimum_fields_v0.md)
- [integrated_engine_screen_panel_classification_criteria_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_screen_panel_classification_criteria_v0.md)
- [integrated_engine_three_surface_representative_panel_layout_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_three_surface_representative_panel_layout_v0.md)
- [integrated_engine_three_surface_panel_connection_flow_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_three_surface_panel_connection_flow_v0.md)
- [integrated_engine_panel_render_contract_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_panel_render_contract_v0.md)
- [integrated_engine_working_lexicon_v1_candidate.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_working_lexicon_v1_candidate.md)
- [integrated_engine_working_protocol_v1_candidate.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_working_protocol_v1_candidate.md)
- [integrated_engine_working_interface_v1_candidate.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_working_interface_v1_candidate.md)
- [integrated_engine_current_reading_order_note_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_current_reading_order_note_v1.md)
- [integrated_engine_gemini_cli_orientation_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/integrated_engine_gemini_cli_orientation_v1.md)
- [vectorfl_space_asset_access_map_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/guides/vectorfl_space_asset_access_map_v0.md)

현재 통합엔진 PASS baseline:
- 통합엔진 v1 candidate 묶음은 final lock 이 아니라 current working baseline / current PASS baseline 으로 사용 가능하다.
- 사용자 기점 루프와 VectorFL 기점 재기동 루프는 모두 manifest / scaffold / document 수준 수동 운용에서 PASS 되었다.
- 3면 역할 분리, request / return / reflux packet 분리, panel read / render 기준은 현재 참조 기준에서 정합화되었다.
- 다음 채팅이나 다음 작업은 우선 `integrated_engine_working_lexicon_v1_candidate.md`, `integrated_engine_working_protocol_v1_candidate.md`, `integrated_engine_working_interface_v1_candidate.md` 3문서를 먼저 읽는다.

핵심:
- 파일을 지금 당장 이동하지 않는다.
- `사용자면 / 벡터플면 / 엔진면` 3면 구조를 기준으로 현재 자산의 역할을 먼저 목록화한다.
- 현재 3면은 기존 벡터플/엔진 내부 구조를 표면별로 번역해 펼친 본체 구조로 읽고, CLI/에이전트/팀/자동화는 본체를 대체하지 않는 선택적 도구층으로 읽는다.
- 사용자면은 목적/범위/재료 문맥, 벡터플면은 line/relation/gap/pending 같은 중간 형성체 판독, 엔진면은 ingest/process/validate/trace-memory-return이 핵심이다.
- 통합엔진 셋업과 assistant 해석 안정성에 바로 쓸 공통 언어 후보는 `integrated_engine_common_language_extraction_v1.md` 에 Track A / Track B 데이터셋으로 적립한다.
- 반복 탐색용 질문 프레임은 `integrated_engine_exploration_question_set_v1.md` 를 사용하고, 산출은 raw 표현 / 해석 / 사람 말 재서술 / unresolved / source_refs 중심으로 남긴다.
- 반복 탐색용 최신 프로토콜은 `integrated_engine_exploration_question_set_v1_1.md` 이며, source priority / freshness_note / previous-run overlap / stable candidate 판단을 포함한다.
- v1.1 첫 실행 결과는 `integrated_engine_language_harvest_run_20260414_v1_1.md` 에 남기고, `integrated_engine_common_language_extraction_v1.md` 는 harvest_round_1 비교 기준으로 사용한다.
- `integrated_engine_common_language_extraction_v2.md` 와 `integrated_engine_common_language_extraction_v3.md` 는 round_2/round_3 수확 결과이며, round_3는 새 body lock 추가 없이 extension / future-layer / unresolved 경계를 좁힌다.
- 언어 적립 쪽 현재 읽기 순서는 `integrated_engine_current_reading_order_note_v1.md` 를 따른다: v1.1 protocol -> harvest_round_1 -> harvest_round_2 -> harvest_round_3/boundary -> working lexicon.
- 현재 셋업 실사용 언어는 `integrated_engine_setup_working_lexicon_v0.md` 를 기준으로 삼고, Gemini/외부 CLI 작업자는 `integrated_engine_gemini_cli_orientation_v1.md` 를 먼저 읽게 한다.
- 전달 패킷 최소 슬롯 v0는 `integrated_engine_transfer_packet_minimum_slots_v0.md` 에 두며, request / return / reflux 3종과 공통 슬롯 + 타입별 최소 슬롯을 저강도 운용 테스트용 공통 전달체로만 읽는다.
- 운영 객체 슬롯 이동 규칙 v0는 `integrated_engine_operating_object_slot_movement_rules_v0.md` 에 두며, inbox -> vectorfl_review -> engine_processing / external_support -> validation -> return_ready -> closed 흐름을 final state machine이 아니라 저강도 운용 테스트용 이동 문법으로만 읽는다.
- 앵커 객체 최소 필드 v0는 `integrated_engine_anchor_object_minimum_fields_v0.md` 에 두며, scope / governs_what / locked_boundary / comparison_rule 를 중심으로 비교/경계/위치 판단 기준점으로만 읽는다.
- 숙성 객체 최소 필드 v0는 `integrated_engine_maturation_object_minimum_fields_v0.md` 에 두며, origin_refs / current_position / maturity_stage / linked_objects 를 중심으로 line/axis/note/harvest/comparison material 의 연결과 발현 가능성을 보존하는 언어로만 읽는다.
- 화면 패널 분류 기준 v0는 `integrated_engine_screen_panel_classification_criteria_v0.md` 에 두며, 화면을 기능 버튼 모음이 아니라 앵커 표현 / 숙성 표현 / 운영 표현의 표현면으로 읽는 기준으로만 사용한다.
- 3면별 대표 패널 배치 초안 v0는 `integrated_engine_three_surface_representative_panel_layout_v0.md` 에 두며, 사용자면=운영 흐름, 벡터플면=숙성 캔버스, 엔진면=실행 상태를 중앙 패널로 두는 역할 분리 기준으로만 사용한다.
- 3면별 패널 간 연결 흐름 v0는 `integrated_engine_three_surface_panel_connection_flow_v0.md` 에 두며, 사용자 요청 -> 벡터플 검토 -> 엔진 처리 / 외부 지원 -> 벡터플 검증 -> 사용자 결정 / 공간 환류를 패킷과 로그 단위로 읽는 대표 연결 문법으로만 사용한다.
- 패널별 render contract v0는 `integrated_engine_panel_render_contract_v0.md` 에 두며, 각 패널이 manifest 전체가 아니라 자기 질문에 필요한 최소 필드만 표시하는 표시 계약으로만 읽는다.
- 통합엔진 v0 최소 운용 문법은 문서-매니페스트-스캐폴드 수준에서 PASS 되었고, 사용자 기점 루프와 VectorFL 기점 재기동 루프까지 working lexicon / working protocol / working interface v1 candidate 3문서에 current PASS baseline 으로 반영되었다.
- `integrated_engine_working_lexicon_v1_candidate.md`, `integrated_engine_working_protocol_v1_candidate.md`, `integrated_engine_working_interface_v1_candidate.md` 는 다음 채팅/다음 작업의 우선 참조 시작점이며, final lock 이 아니라 current working baseline 이다.
- 벡터플면은 현재 단순 workflow hub로 잠그지 않되, CLI 조율 / 업무 흐름 / 엔진 요청-환류 / 공간 변화 실마리를 번역하는 중심 운영 허리 후보로 별도 방향 기록을 둔다.
- 스크립트/문서/재료는 `vectorfl_space_asset_access_map_v0.md` 기준으로 먼저 찾고, 필요할 때만 repo-wide search로 내려간다.
- `runtime/views/vectorfl_dual_surface.tsx` 와 `runtime/views/vectorfl_dual_surface_app/` 는 현재 사용자면/벡터플면 작업의 소스 축이다.
- `/vectorfl-engine/operate` 는 현재 Python 쪽 engine-facing operating shell 로 남아 있지만, 사용자면과 엔진면을 직접 붙이는 본체 해석으로 읽지 않는다.
- Paper/proper/operable/page_shell 계열은 lineage/reference 로 유지하되 현재 surface 역할과 혼동하지 않는다.

## 1. What This Repository Is
이 저장소는 하나의 단순 앱이 아니라, 아래 4층이 같이 있는 엔진 작업공간이다.

1. `app/`
   - 현재 엔진 코드
   - 입력층, 코어, 런타임, 측정, fragment, work 실험 폴더
2. `scripts/`
   - ingest, view build, observer 적용, smoke check 같은 실행 스크립트
3. `runtime/`
   - 실행 결과와 generated artifact 가 쌓이는 공간
4. `references/`
   - 내부 reference 저장소
   - WashTank / vectorfl / vectorfl_next / gemini session 같은 과거 자산과 비교 기준

가장 짧게 말하면:
이 저장소는 `입력 -> fragment/anchor/measurement -> observer -> report/view` 흐름과, `reference -> preprocessed -> ingest queue` 흐름이 같이 공존하는 엔진 작업공간이다.

최근 운영 골격까지 포함해 다시 말하면:
이 저장소는 `재료 -> 라우팅 -> 실행/기록 -> 조회` 흐름과, `reference -> preprocessed -> selective ingest` 흐름이 함께 있는 repo-scale engine 이다.

---

## 2. Current Engine Definition
현재 baseline 은 [CURRENT.md](/Users/sungsookim/universe/vectorfl_replica/CURRENT.md) 에 잡혀 있다.

여기서 중요한 현재 정의는 이렇다.

- 중심 객체는 `fragment`
- fragment 는 아래를 붙들고 있어야 한다
  - source linkage
  - anchor handles
  - processing values
  - provenance steps
  - measurement records
- 현재 방향은
  - `source -> fragment -> anchor + processing values -> measurement retention -> observer layer -> source/space projection`

즉 지금 엔진은 “정답 바로 확정”보다
`fragment를 중심으로 source/anchor/measurement/observer를 유지하고 보고하는 구조`
에 가깝다.

---

## 3. Philosophy And Current Layer Contract
현재 엔진 철학과 운영 계약은 아래 문서가 잡고 있다.

### A. 상위 철학
- [engine_philosophy_declaration_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/engine_philosophy_declaration_v1.md)

핵심:
- 정답 우선이 아니라 `위치값 우선`
- 완전한 정합성보다 `반복과 재등장 속의 일관성`
- mixed 는 실패가 아니라 `productive hold`
- 숙성 가능한 값을 빨리 버리지 않는다

### B. 현재 레이어 운영 계약
- [current_layer_baseline_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/current_layer_baseline_contract_v1.md)

핵심:
- bridge 없음 -> unreadable 쪽
- bridge 있음 + stable closure 없음 -> `mixed / confirmed_hold`
- bridge 있음 + stable closure 도달 -> `canonical / stable_reading`
- 현재 레이어는
  - 조기 폐기 방지
  - hold 이유 기록
  - 재진입 가능성 보존
  - observer-first 운영

즉 이 둘이 현재 엔진의 철학 헌법과 운영 계약이다.

---

## 3A. Current Operation Skeleton
최근 추가된 운영 골격은 아래 문서와 산출면에 잠겨 있다.

### A. structured doc routing
- [document_routing_markers_policy_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/document_routing_markers_policy_v1.md)
- [structured_doc_routing_header_template_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/templates/structured_doc_routing_header_template_v1.md)
- [document_routing_alias_map_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/document_routing_alias_map_v1.json)
- [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)

핵심:
- 구조화 문서는 바로 실행되지 않고 먼저 parse / normalize / register 된다
- `RUNMODE` 가 없으면 기본은 `ingest_only`
- `ingest_then_execute` 일 때만 ticket/execution 으로 내려간다

### B. append-only operation event skeleton
- [event_schema_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/events/event_schema_v1.md)
- [engine_event_ledger.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/events/engine_event_ledger.jsonl)
- [record_operation_event.py](/Users/sungsookim/universe/vectorfl_replica/scripts/record_operation_event.py)

핵심:
- 실행은 작은 사건으로 먼저 남긴다
- status 문서는 later compaction 설명층이다

### C. receipts / latest views / commands surface
- [operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)
- [structured_doc_routing_commands_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/commands/structured_doc_routing_commands_v1.md)
- [runtime/receipts](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts)

핵심:
- 여러 registry/ledger/generated 파일을 receipt 와 latest board 로 다시 읽는다

### D. origin map / provenance return handle
- [origin_map_minimum_fields_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/origin_map_minimum_fields_v1.md)
- [origin_map_minimum_v1.py](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/source_locator/origin_map_minimum_v1.py)
- [runtime/manifests/origin_maps](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/origin_maps)

핵심:
- 파생물은 원본 복귀용 최소 provenance 손잡이를 가질 수 있다
- origin map 은 입력 시 수동 필드가 아니라 파생 시점 자동 부착 축이다

### E. LLM 답변 구조 증류 / 정련 기준
- [llm_response_structure_extraction_and_refinement_checkpoint_v0.md](/Users/sungsookim/universe/vectorfl_replica/llm_response_structure_extraction_and_refinement_checkpoint_v0.md)
- [llm_response_structure_slot_catalog_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/llm_response_structure_slot_catalog_v0.md)
- [llm_standard_doc_structure_slot_mapping_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/llm_standard_doc_structure_slot_mapping_v0.md)
- [llm_distillation_engine_attachment_feasibility_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/llm_distillation_engine_attachment_feasibility_v0.md)
- [refinement_checkpoint_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/refinement_checkpoint_contract_v1.md)

핵심:
- LLM 자체를 엔진 코어에 넣지 않고, 답변에서 반복되는 판단 구조를 슬롯으로 증류해 붙이는 방향을 고정
- 선언문 / 기준문 / 지시서와 LLM 답변 구조의 겹침을 재발견해 엔진용 추출 스키마 후보로 사용
- 풍부한 해석은 외곽 observation/report 레이어에 두고, 코어는 주기적 정련으로 다시 작고 단단하게 유지

### F. Thin Operation Rules
- [thin_operation_rules_lock_v1.md](/Users/sungsookim/universe/vectorfl_replica/thin_operation_rules_lock_v1.md)
- [core_promotion_checklist_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/core_promotion_checklist_v1.md)
- [exploration_observation_layer_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/exploration_observation_layer_v1.md)
- [refinement_trigger_rules_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/refinement_trigger_rules_v1.md)
- [runtime/contracts](/Users/sungsookim/universe/vectorfl_replica/runtime/contracts)
- [runtime/observer/exploration](/Users/sungsookim/universe/vectorfl_replica/runtime/observer/exploration)

핵심:
- 코어 승격 기준을 즉시 엔진 로직으로 박지 않고 checklist로 먼저 잠금
- 탐색 결과를 session/run 기준 observer sidecar로 반복 기록할 수 있는 얇은 경로 확보
- refinement 개시를 막연한 감각이 아니라 trigger 규칙으로 잠금

### G. 입력 / source asset 정리 기준
- [input_dropzones.md](/Users/sungsookim/universe/vectorfl_replica/docs/guides/input_dropzones.md)
- [root_md_reorganization_guide_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/guides/root_md_reorganization_guide_v1.md)
- [source_assets/README.md](/Users/sungsookim/universe/vectorfl_replica/source_assets/README.md)

핵심:
- raw 입력은 `inputs/` 아래에 둔다
- 새 source asset 는 가능한 한 `source_assets/` 아래 전용 폴더에서 시작한다
- 기존 루트 md는 provenance 안정성 때문에 바로 이동하지 않고 `legacy canonical root assets` 로 먼저 분류 관리한다

---

## 4. app/ Structure
전체 인덱스는 [app/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/folder_status.md) 에 있다.

### A. `app/core/`
- [app/core/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/core/folder_status.md)
- 엔진의 코어 뼈대
- 하위:
  - `events/`
  - `formation/`
  - `ingest/`
  - `models/`
  - `registry/`
  - `runtime/`
  - `schemas/`
  - `state/`

즉 core 는 “무엇을 저장하고 어떤 상태/계약으로 다룰지” 쪽이다.

대표 파일:
- [formation_service.py](/Users/sungsookim/universe/vectorfl_replica/app/core/formation_service.py)
- [states.py](/Users/sungsookim/universe/vectorfl_replica/app/core/states.py)

### B. `app/input_layer/`
- [app/input_layer/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/folder_status.md)
- 입력층
- 하위:
  - `segmenter/`
  - `labeler/`
  - `anchorizer/`
  - `source_locator/`

즉 입력을 어떻게 자르고, 어떤 라벨/앵커/위치를 붙일지의 작업장이다.

최근에는 `source_locator` 아래 `origin_map_minimum_v1.py` 가 추가되어,
입력기 하위에서 `source return / provenance handle` 까지 준비하는 레이어로 확장됐다.

### C. `app/fragment/`
- fragment schema / projector / store 계층
- 현재 엔진이 fragment 중심이라는 점에서 매우 중요하다

대표 파일:
- [schema.py](/Users/sungsookim/universe/vectorfl_replica/app/fragment/schema.py)
- [projector.py](/Users/sungsookim/universe/vectorfl_replica/app/fragment/projector.py)
- [store.py](/Users/sungsookim/universe/vectorfl_replica/app/fragment/store.py)

### D. `app/measurement/`
- 측정/observer 관련 보조 계층

대표 파일:
- [ambient_probe.py](/Users/sungsookim/universe/vectorfl_replica/app/measurement/ambient_probe.py)
- [observer.py](/Users/sungsookim/universe/vectorfl_replica/app/measurement/observer.py)
- [seed_bank.py](/Users/sungsookim/universe/vectorfl_replica/app/measurement/seed_bank.py)

### E. `app/runtime/`
- [app/runtime/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/runtime/folder_status.md)
- 실제 runtime/view/report 동작 계층
- 현재 엔진을 “움직이게 하는” py 파일이 가장 많이 모여 있는 곳

대표 파일과 역할:
- [inputter.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/inputter.py)
  - 입력 runtime 진입점 성격
- [labeler.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/labeler.py)
  - runtime label 처리
- [observer.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/observer.py)
  - observer layer runtime
- [connection_engine.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/connection_engine.py)
  - 연결/브리지 성격의 runtime
- [reporting.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/reporting.py)
  - 리포트 산출
- [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/viewer_server.py)
  - viewer server
- [graph_view.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/graph_view.py)
  - 그래프/뷰 투영
- [reactive_space_report.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/reactive_space_report.py)
  - reactive space 보고
- [stage0_handoff.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/stage0_handoff.py)
  - stage0 handoff 성격
- [workspace_manifest.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/workspace_manifest.py)
  - workspace 수준 manifest
- [workspace_report.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/workspace_report.py)
  - workspace 수준 요약/리포트

즉 runtime 은
`input -> observer -> report/view -> workspace artifact`
를 가능하게 하는 층이다.

### F. `app/work/`
- [app/work/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/work/folder_status.md)
- 현재 우리가 실제로 probe, 계약, 정리, 실험을 쌓아온 폴더
- 코드보다 `규정 / spec / 실험 기록 / 해석 결과` 가 많이 쌓여 있다

중요 work 폴더:
- [current_layer_baseline](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline)
  - 철학 선언과 현재 계약
- [observer_ingest_min](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min)
  - 입력을 쉽게 넣고 split/trace/요약을 확인하는 최소 실행면
- [workbench_stage1](/Users/sungsookim/universe/vectorfl_replica/app/work/workbench_stage1)
  - canonical / mixed reading grammar 쪽
- [result_value_bundle_stage1](/Users/sungsookim/universe/vectorfl_replica/app/work/result_value_bundle_stage1)
  - result-value bundle / compare card
- [youtube_transcript_probe_0322](/Users/sungsookim/universe/vectorfl_replica/app/work/youtube_transcript_probe_0322)
  - 긴 transcript read-only probe
- [youtube_transcript_probe_0322_b](/Users/sungsookim/universe/vectorfl_replica/app/work/youtube_transcript_probe_0322_b)
  - round2 probe
- [mixed_reentry_probe_stage1](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_reentry_probe_stage1)
  - mixed hold re-entry 검증
- [mixed_reentry_observer_stage2](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_reentry_observer_stage2)
  - corridor accumulation 관찰
- [mixed_corridor_boundary_probe_stage3](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_corridor_boundary_probe_stage3)
  - reinforcing/adjacent/off-axis 경계 검증
- [mixed_corridor_format_disentangle_stage4](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_corridor_format_disentangle_stage4)
  - meaning vs format disentangle
- [technical_business_corridor_decompose_stage5](/Users/sungsookim/universe/vectorfl_replica/app/work/technical_business_corridor_decompose_stage5)
  - technical->business corridor 분해
- [transition_mixed_close_reading](/Users/sungsookim/universe/vectorfl_replica/app/work/transition_mixed_close_reading)
  - transition-led mixed 세부 판독
- [transition_mixed_surface_refine](/Users/sungsookim/universe/vectorfl_replica/app/work/transition_mixed_surface_refine)
  - readable surface 강화

즉 `app/work` 은 현재 엔진 사고의 기록과 실험 로그 그 자체다.

---

## 5. Which md Files Are “Rules” Or “Declarations”
현재 기준으로 “규정/선언/기준선” 으로 먼저 봐야 할 md 는 아래다.

### A. 루트 현재 상태
- [CURRENT.md](/Users/sungsookim/universe/vectorfl_replica/CURRENT.md)
  - 현재 runtime baseline
  - 현재 policy baseline
  - current gaps
  - current priority

### B. 철학 / 운영 계약
- [engine_philosophy_declaration_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/engine_philosophy_declaration_v1.md)
- [current_layer_baseline_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/current_layer_baseline_contract_v1.md)

### C. observer ingest 최소 실행면 계약
- [observer_ingest_min_spec.md](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/observer_ingest_min_spec.md)
- [observer_ingest_min_terminal_usage.md](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/observer_ingest_min_terminal_usage.md)

### D. WashTank reference 처리 계약
- [reference_preprocessor_schema.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/reference_preprocessor_schema.md)
- [reference_preprocessor_runner_v0_spec.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/reference_preprocessor_runner_v0_spec.md)
- [fragment_queue_policy_v1.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/fragment_queue_policy_v1.md)
- [wash_tank_reference_work_record_v1.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/wash_tank_reference_work_record_v1.md)

### E. folder_status 인덱스
- [app/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/folder_status.md)
- [references/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/folder_status.md)

### F. 최근 운영 골격 문서
- [document_routing_markers_policy_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/document_routing_markers_policy_v1.md)
- [origin_map_minimum_fields_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/origin_map_minimum_fields_v1.md)
- [codex_material_and_operation_docs_index_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/codex_material_and_operation_docs_index_v1.md)

즉 이 문서들이 현재 “무엇이 규정이고 무엇이 작업 로그인가” 를 가르는 첫 번째 진입점이다.

---

## 6. Which Python Files Matter Most Right Now
지금 상태에서 “엔진을 가능하게 하는 py” 를 크게 나누면 이렇다.

### A. 입력 / fragment / observer 실행면
- [app/runtime/inputter.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/inputter.py)
- [app/runtime/labeler.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/labeler.py)
- [app/runtime/observer.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/observer.py)
- [app/fragment/projector.py](/Users/sungsookim/universe/vectorfl_replica/app/fragment/projector.py)
- [app/fragment/store.py](/Users/sungsookim/universe/vectorfl_replica/app/fragment/store.py)

### B. 리포트 / 뷰 / workspace
- [app/runtime/reporting.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/reporting.py)
- [app/runtime/viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/viewer_server.py)
- [app/runtime/graph_view.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/graph_view.py)
- [app/runtime/workspace_manifest.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/workspace_manifest.py)
- [app/runtime/workspace_report.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/workspace_report.py)

### C. 측정 / ambient / seed bank
- [app/measurement/ambient_probe.py](/Users/sungsookim/universe/vectorfl_replica/app/measurement/ambient_probe.py)
- [app/measurement/observer.py](/Users/sungsookim/universe/vectorfl_replica/app/measurement/observer.py)
- [app/measurement/seed_bank.py](/Users/sungsookim/universe/vectorfl_replica/app/measurement/seed_bank.py)

### D. 실험 실행기
- [run_observer_ingest_min.py](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py)
- [run_workbench_stage1.py](/Users/sungsookim/universe/vectorfl_replica/app/work/workbench_stage1/run_workbench_stage1.py)
- [run_result_value_compare_card_stage1.py](/Users/sungsookim/universe/vectorfl_replica/app/work/result_value_bundle_stage1/run_result_value_compare_card_stage1.py)
- [run_youtube_transcript_probe_0322.py](/Users/sungsookim/universe/vectorfl_replica/app/work/youtube_transcript_probe_0322/run_youtube_transcript_probe_0322.py)
- [run_transcript_probe_round2.py](/Users/sungsookim/universe/vectorfl_replica/app/work/youtube_transcript_probe_0322_b/run_transcript_probe_round2.py)
- [run_mixed_reentry_probe_stage1.py](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_reentry_probe_stage1/run_mixed_reentry_probe_stage1.py)
- [run_mixed_reentry_observer_stage2.py](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_reentry_observer_stage2/run_mixed_reentry_observer_stage2.py)
- [run_mixed_corridor_boundary_probe_stage3.py](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_corridor_boundary_probe_stage3/run_mixed_corridor_boundary_probe_stage3.py)
- [run_mixed_corridor_format_disentangle_stage4.py](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_corridor_format_disentangle_stage4/run_mixed_corridor_format_disentangle_stage4.py)
- [run_technical_business_corridor_decompose_stage5.py](/Users/sungsookim/universe/vectorfl_replica/app/work/technical_business_corridor_decompose_stage5/run_technical_business_corridor_decompose_stage5.py)
- [run_transition_mixed_close_reading.py](/Users/sungsookim/universe/vectorfl_replica/app/work/transition_mixed_close_reading/run_transition_mixed_close_reading.py)
- [run_transition_mixed_surface_refine.py](/Users/sungsookim/universe/vectorfl_replica/app/work/transition_mixed_surface_refine/run_transition_mixed_surface_refine.py)

즉 py 파일은 크게
`코어 runtime`, `측정/observer`, `실험 실행기`
세 층으로 읽으면 된다.

### E. 운영 진입점 / 기록 계층
- [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
- [record_operation_event.py](/Users/sungsookim/universe/vectorfl_replica/scripts/record_operation_event.py)
- [origin_map_minimum_v1.py](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/source_locator/origin_map_minimum_v1.py)

즉 최근에는 `입력기 -> 실행 -> 기록 -> 조회` 흐름 자체도 명시적 py 계층으로 올라왔다.

---

## 7. app/runtime Detailed Responsibility Map
이 섹션은 “파일 이름은 보이는데 정확히 뭘 여는 게 맞나”를 줄이기 위한 1차 책임 인덱스다.

- [bootstrap.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/bootstrap.py)
  - runtime 초기화와 기동 진입점 성격
- [connection_engine.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/connection_engine.py)
  - fragment/material 사이 연결 계산과 브리지 판단 계열
- [dust_field.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/dust_field.py)
  - dust/ambient field 계열의 runtime projection
- [file_store.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/file_store.py)
  - runtime 산출물 파일 저장/불러오기 계층
- [graph_view.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/graph_view.py)
  - 그래프형 시각화/투영 산출
- [inputter.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/inputter.py)
  - 입력을 runtime 쪽으로 실제 흘려보내는 진입점
- [labeler.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/labeler.py)
  - runtime label 계산/부착 계층
- [live_input.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/live_input.py)
  - live input 또는 stream형 입력 연결 계층
- [observer.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/observer.py)
  - observer layer runtime 기록과 판독
- [operator_ui_state.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/operator_ui_state.py)
  - operator-facing UI state 정리 계층
- [reactive_space_report.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/reactive_space_report.py)
  - reactive space 상태를 report로 묶는 계층
- [region_atlas.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/region_atlas.py)
  - region/atlas 계열 공간 정리
- [reporting.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/reporting.py)
  - source/measurement/report 산출 공통 계층
- [reread_audit.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/reread_audit.py)
  - reread/재판독 감사 흔적 정리
- [scale_review.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/scale_review.py)
  - scale/밀도/확장성 점검 계층
- [semantic_terrain_fields.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/semantic_terrain_fields.py)
  - semantic terrain field 계산
- [semantic_terrain_geometry.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/semantic_terrain_geometry.py)
  - semantic terrain geometry 계산
- [sparse_presence_review.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/sparse_presence_review.py)
  - sparse signal/presence 점검
- [stage0_handoff.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/stage0_handoff.py)
  - stage0 handoff artifact 생성/유지
- [terrain_map.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/terrain_map.py)
  - terrain map 계열 projection
- [viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/viewer_server.py)
  - 로컬 viewer 서버
- [workspace_manifest.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/workspace_manifest.py)
  - workspace 수준 manifest/메타데이터 산출
- [workspace_report.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/workspace_report.py)
  - workspace 수준 요약 리포트 산출

실전 팁:
- 입력이 왜 이렇게 붙었는지 보려면 `inputter.py`, `labeler.py`, `observer.py`
- 산출물이 어디로 가는지 보려면 `file_store.py`, `reporting.py`, `workspace_manifest.py`
- 공간/뷰 쪽을 보려면 `graph_view.py`, `viewer_server.py`, `semantic_terrain_*`, `terrain_map.py`

---

## 8. scripts/ Folder
루트 `scripts/` 는 app/work 아래 실행기와 별개로, 현재 runtime를 다루는 도우미 스크립트 모음이다.

중요 스크립트:
- [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
  - structured doc parse / normalize / register / execute / receipt / board 진입점
- [record_operation_event.py](/Users/sungsookim/universe/vectorfl_replica/scripts/record_operation_event.py)
  - append-only operation event 기록기
- [ingest_fragments.py](/Users/sungsookim/universe/vectorfl_replica/scripts/ingest_fragments.py)
  - fragment batch ingest
- [build_source_view.py](/Users/sungsookim/universe/vectorfl_replica/scripts/build_source_view.py)
  - source-side 뷰 생성
- [build_measurement_view.py](/Users/sungsookim/universe/vectorfl_replica/scripts/build_measurement_view.py)
  - measurement view 생성
- [build_space_graph_view.py](/Users/sungsookim/universe/vectorfl_replica/scripts/build_space_graph_view.py)
  - space/graph view 생성
- [build_dust_field_view.py](/Users/sungsookim/universe/vectorfl_replica/scripts/build_dust_field_view.py)
  - dust field view 생성
- [apply_internal_observer.py](/Users/sungsookim/universe/vectorfl_replica/scripts/apply_internal_observer.py)
  - observer 적용
- [record_observer_samples.py](/Users/sungsookim/universe/vectorfl_replica/scripts/record_observer_samples.py)
  - observer sample 기록

실전 읽기:
- structured doc 를 처리하려면 `process_structured_doc_with_routing.py`
- 사건을 직접 append 하려면 `record_operation_event.py`
- legacy ingest/view build 를 따라가려면 `ingest_fragments.py`, `build_*`, `run_viewer_server.py`

---

## 9. runtime/ As Result Surface
루트 [runtime/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/runtime/folder_status.md) 는 이제 단순 generated artifact 창고가 아니라,
아래를 함께 품는 결과 표면으로 읽는 것이 맞다.

- `events/` = append-only operation ledger
- `manifests/` = doc registry / ticket registry / provenance / origin map
- `reports/` = 사람이 읽는 report 산출
- `receipts/` = 문서 처리 단일 영수증
- `views/` = latest operation board 같은 최신 조회면
- `commands/` = 재실행용 command surface

즉 runtime 은 이제 `산출물 보관`과 `운영 조회면` 이 함께 있는 결과 표면이다.

---

## 10. references/ As Reuse And Calibration Lane
`references/` 는 여전히 calibration memory 이지만,
현재는 단순 비교 자산을 넘어서 재사용 탐색 레인으로도 읽는 것이 맞다.

특히 [references/WashTank/preprocessed/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/folder_status.md) 에 잠긴 구조는 아래 재사용 흐름에 직접 쓸 수 있다.

- reference source
- observer sheet
- preprocessed fragment sidecar
- selective ingest queue

즉 새 프로그램/기능을 만들 때는
- 먼저 `folder_status`
- 그 다음 `reference_preprocessor_schema`
- 그 다음 `runner / queue policy`
순으로 열면 재사용 가능한 구조 재료를 찾기 쉽다.
- [record_observer_template.py](/Users/sungsookim/universe/vectorfl_replica/scripts/record_observer_template.py)
  - observer template 기록
- [run_replica_smoke_check.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_replica_smoke_check.py)
  - smoke check
- [run_review_fixture_check.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_review_fixture_check.py)
  - fixture/review check
- [run_viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_viewer_server.py)
  - viewer server 실행

즉 `scripts/` 는 엔진 운영 유틸리티 레이어다.

---

## 9. scripts Detailed Responsibility Map
이 섹션은 “어떤 스크립트를 언제 써야 하나”를 빠르게 판단하기 위한 1차 인덱스다.

- [ingest_fragments.py](/Users/sungsookim/universe/vectorfl_replica/scripts/ingest_fragments.py)
  - fragment batch ingest 실행
- [build_source_view.py](/Users/sungsookim/universe/vectorfl_replica/scripts/build_source_view.py)
  - source-side 리포트/뷰 생성
- [build_measurement_view.py](/Users/sungsookim/universe/vectorfl_replica/scripts/build_measurement_view.py)
  - measurement-side 리포트/뷰 생성
- [build_space_graph_view.py](/Users/sungsookim/universe/vectorfl_replica/scripts/build_space_graph_view.py)
  - space/graph view 생성
- [build_dust_field_view.py](/Users/sungsookim/universe/vectorfl_replica/scripts/build_dust_field_view.py)
  - dust field view 생성
- [apply_internal_observer.py](/Users/sungsookim/universe/vectorfl_replica/scripts/apply_internal_observer.py)
  - observer 판정/기록 적용
- [record_observer_samples.py](/Users/sungsookim/universe/vectorfl_replica/scripts/record_observer_samples.py)
  - observer sample 기록
- [record_observer_template.py](/Users/sungsookim/universe/vectorfl_replica/scripts/record_observer_template.py)
  - observer template 생성/기록
- [apply_anchor_engine_to_processor_docs.py](/Users/sungsookim/universe/vectorfl_replica/scripts/apply_anchor_engine_to_processor_docs.py)
  - processor compare 문서에 anchor engine 적용
- [import_processor_compare_docs.py](/Users/sungsookim/universe/vectorfl_replica/scripts/import_processor_compare_docs.py)
  - processor compare 문서 import
- [register_processor_compare_doc_bridges.py](/Users/sungsookim/universe/vectorfl_replica/scripts/register_processor_compare_doc_bridges.py)
  - processor compare 문서 간 bridge 등록
- [recover_imported_material_contract.py](/Users/sungsookim/universe/vectorfl_replica/scripts/recover_imported_material_contract.py)
  - imported material contract 회복/정리
- [refine_imported_processing_profiles.py](/Users/sungsookim/universe/vectorfl_replica/scripts/refine_imported_processing_profiles.py)
  - import된 processing profile 정련
- [backfill_live_input_bridges.py](/Users/sungsookim/universe/vectorfl_replica/scripts/backfill_live_input_bridges.py)
  - live input bridge backfill
- [backfill_possibility_bridges.py](/Users/sungsookim/universe/vectorfl_replica/scripts/backfill_possibility_bridges.py)
  - possibility bridge backfill
- [sync_runtime_space_anchor_metadata.py](/Users/sungsookim/universe/vectorfl_replica/scripts/sync_runtime_space_anchor_metadata.py)
  - runtime space anchor metadata 동기화
- [commonize_runtime_observer_baseline.py](/Users/sungsookim/universe/vectorfl_replica/scripts/commonize_runtime_observer_baseline.py)
  - observer baseline 공통화/정리
- [run_replica_smoke_check.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_replica_smoke_check.py)
  - 저장소 smoke check
- [run_review_fixture_check.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_review_fixture_check.py)
  - review fixture 점검
- [run_viewer_server.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_viewer_server.py)
  - 로컬 viewer server 기동

실전 팁:
- ingest/리포트만 보면 `ingest_fragments.py`, `build_*_view.py`
- observer 계열이면 `apply_internal_observer.py`, `record_observer_*`
- processor compare 계열이면 `import_processor_compare_docs.py`, `register_processor_compare_doc_bridges.py`
- 안전 점검이면 `run_replica_smoke_check.py`, `run_review_fixture_check.py`

---

## 10. app/work Priority Map
`app/work` 는 실험 폴더가 많아서 우선순위를 먼저 잡아야 한다.

### first-read
- [current_layer_baseline](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline)
  - 철학 + 운영 계약
- [observer_ingest_min](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min)
  - 입력을 쉽게 넣고 split/trace를 보는 최소 실행면

### reading / grammar family
- [workbench_stage1](/Users/sungsookim/universe/vectorfl_replica/app/work/workbench_stage1)
  - canonical/mixed reading grammar
- [result_value_bundle_stage1](/Users/sungsookim/universe/vectorfl_replica/app/work/result_value_bundle_stage1)
  - result-value bundle / compare card

### transcript / mixed corridor family
- [youtube_transcript_probe_0322](/Users/sungsookim/universe/vectorfl_replica/app/work/youtube_transcript_probe_0322)
- [youtube_transcript_probe_0322_b](/Users/sungsookim/universe/vectorfl_replica/app/work/youtube_transcript_probe_0322_b)
- [mixed_reentry_probe_stage1](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_reentry_probe_stage1)
- [mixed_reentry_observer_stage2](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_reentry_observer_stage2)
- [mixed_corridor_boundary_probe_stage3](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_corridor_boundary_probe_stage3)
- [mixed_corridor_format_disentangle_stage4](/Users/sungsookim/universe/vectorfl_replica/app/work/mixed_corridor_format_disentangle_stage4)
- [technical_business_corridor_decompose_stage5](/Users/sungsookim/universe/vectorfl_replica/app/work/technical_business_corridor_decompose_stage5)
- [transition_mixed_close_reading](/Users/sungsookim/universe/vectorfl_replica/app/work/transition_mixed_close_reading)
- [transition_mixed_surface_refine](/Users/sungsookim/universe/vectorfl_replica/app/work/transition_mixed_surface_refine)

### secondary utility / support
- [processor_compare](/Users/sungsookim/universe/vectorfl_replica/app/work/processor_compare)
- [evaluations](/Users/sungsookim/universe/vectorfl_replica/app/work/evaluations)
- [experiments](/Users/sungsookim/universe/vectorfl_replica/app/work/experiments)
- [prompts](/Users/sungsookim/universe/vectorfl_replica/app/work/prompts)

실전 팁:
- 철학/정책 질문이면 `current_layer_baseline`
- 입력 넣기 질문이면 `observer_ingest_min`
- mixed/canonical 판독 질문이면 `workbench_stage1`
- transcript probe 흐름이면 `youtube_*` 와 `mixed_*`

---

## 11. references/ Folder
전체 인덱스는 [references/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/folder_status.md) 에 있다.

여기서 중요한 건 `reference` 가 그냥 보관함이 아니라, 두 레인으로 읽힌다는 점이다.

### A. space material lane
- 구조 재료
- 판단 흐름
- 재사용 패턴

### B. input calibration lane
- 과절단/미절단 교정
- identity / state / routing 분리 기준
- special subflow 보존 기준

현재 가장 많이 정리된 reference family:
- [references/WashTank/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/folder_status.md)
- [references/WashTank/preprocessed/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/folder_status.md)

여기에서 지금까지 잠근 것:
- reference source 보존
- observer 문서화
- preprocessed fragment sidecar
- runner v0
- fragment queue policy v1

즉 `references` 는 과거 자산 저장소이면서, 동시에 현재 엔진을 교정하는 기준 창고다.

---

## 12. references Detailed Reading Order
references 는 크고 다양하므로 아래 순서가 효율적이다.

### first-read
- [references/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/folder_status.md)
- [references/WashTank/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/folder_status.md)
- [references/WashTank/preprocessed/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/folder_status.md)

### reference repo baselines
- [references/vectorfl/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/vectorfl/folder_status.md)
- [references/vectorfl_next/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/vectorfl_next/folder_status.md)
- [references/vectorfl_next_gemini_session/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/vectorfl_next_gemini_session/folder_status.md)

### WashTank-specific contracts already made
- [wash_tank_reference_work_record_v1.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/wash_tank_reference_work_record_v1.md)
- [fragment_queue_policy_v1.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/fragment_queue_policy_v1.md)
- [reference_preprocessor_runner_v0_summary.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/reference_preprocessor_runner_v0_summary.md)

---

## 13. runtime/ Folder At Repo Root
루트 `runtime/` 은 현재 실행 결과와 generated artifact 가 쌓이는 공간이다.

중요한 읽기:
- source documents
- reports
- manifests
- staged runtime artifacts

즉 `app/runtime` 이 코드를 담고 있다면,
루트 `runtime/` 은 그 코드가 만든 결과를 담고 있다.

---

## 14. docs/, tests/, data/
이 셋은 현재 대화에서 주력은 아니지만 역할은 분명하다.

- `docs/`
  - 보조 설명/정책/문서 계층
  - 빠른 목록 인덱스: [docs/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/docs/folder_status.md)
  - 최근에는 `folder_changes` / `folder_inventory` / `folder_status render` 구조와 직접 연결된다
- `tests/`
  - fixture / unit / integration test 계층
- `data/`
  - 입력 데이터나 실험 보조 데이터 계층

이 셋도 앞으로 `folder_status` 를 같이 보면 탐색이 쉬워진다.

추가로 현재 운영 기준은:
- 전체 재스캔보다 `변화분 기록 + 국소 inventory 갱신 + status render` 를 우선한다
- 관련 기준 문서:
  - [codex_directive_program_level_upgrade_delta_based_program_operation_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_directive_program_level_upgrade_delta_based_program_operation_v1.md)
  - [folder_status_render_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/folder_status_render_contract_v1.md)
  - [folder_inventory_workflow.md](/Users/sungsookim/universe/vectorfl_replica/docs/guides/folder_inventory_workflow.md)

---

## 15. If You Want To Understand The Engine In One Pass
아래 순서면 “철학 -> 현재 baseline -> 코드 구조 -> 실험 -> reference” 를 한 번에 잡을 수 있다.

1. [vectorfl_status.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_status.md)
2. [CURRENT.md](/Users/sungsookim/universe/vectorfl_replica/CURRENT.md)
3. [app/work/current_layer_baseline/current_layer_baseline_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/current_layer_baseline_contract_v1.md)
4. [app/work/current_layer_baseline/engine_philosophy_declaration_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/engine_philosophy_declaration_v1.md)
5. [app/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/folder_status.md)
6. [app/runtime/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/runtime/folder_status.md)
7. [app/work/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/work/folder_status.md)
8. [references/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/folder_status.md)
9. [references/WashTank/preprocessed/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/folder_status.md)

이 순서면 “무슨 엔진인가 / 어떤 계약인가 / 어떤 코드가 움직이나 / 어떤 reference가 교정 자산인가”가 이어진다.

---

## 16. Best First-Read Order
처음 저장소를 다시 파악할 때는 이 순서가 가장 효율적이다.

1. [vectorfl_status.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_status.md)
2. [CURRENT.md](/Users/sungsookim/universe/vectorfl_replica/CURRENT.md)
3. [app/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/folder_status.md)
4. [app/work/current_layer_baseline/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/folder_status.md)
5. [app/work/observer_ingest_min/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/folder_status.md)
6. [references/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/folder_status.md)
7. [references/WashTank/preprocessed/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/folder_status.md)

이 순서면:
- 현재 엔진 정의
- 철학/운영 계약
- app 구조
- 실험/입력면
- reference 창고
를 빠르게 한 바퀴 돈다.

---

## 17. Current One-Line Reading
현재 `vectorfl_replica` 는
`fragment 중심 엔진 + observer-first 해석층 + work probe 기록층 + reference preprocessor/queue 실험층`
이 같이 돌아가는 저장소다.

즉 이 저장소의 강점은 단일 기능이 아니라,
`입력 -> fragment/anchor/measurement -> observer -> report/view`
와
`reference -> preprocessed -> selective ingest`
를 한 공간에서 같이 다룬다는 점이다.
