# stage1_space_readability_current_asset_map_v1

## 목적
현재 repo 안에서 새 입력을 응결핵처럼 놓고 기존 자산과의 관계를 읽을 때
재사용 가능한 축을 자산 단위로 정리한다.

## A. label / anchor / input formation assets

### 1. structured doc routing label packet
- asset:
  - [scripts/process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
  - [runtime/manifests/label_packets](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/label_packets)
- role:
  - 새 입력의 `docrole`, `runmode`, `priority`, core intake label을 정규화한다.
- strength:
  - 새 입력 1건에 대해 최소 label/family를 안정적으로 생성한다.
- limitation:
  - relation kind나 relation reason까지는 직접 만들지 않는다.

### 2. observer_ingest_min outputs
- asset:
  - [app/work/observer_ingest_min/run_observer_ingest_min.py](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py)
  - [app/work/observer_ingest_min/contracts/observer_output_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/contracts/observer_output_contract_v1.md)
  - [app/work/observer_ingest_min/generated](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/generated)
- role:
  - 입력 원문을 split/trace/operator summary까지 최소 형성면으로 만든다.
- strength:
  - 입력-형성 뷰의 바닥으로 즉시 재사용 가능하다.
- limitation:
  - relation 판독면이 아니라 formation trace 면에 머문다.

## B. pointer / evidence / readback assets

### 3. latest pointer surfaces
- asset:
  - [runtime/views/operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)
  - [runtime/commands/structured_doc_routing_commands_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/commands/structured_doc_routing_commands_v1.md)
  - [docs/contracts/operation_surface_pointer_spec_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/operation_surface_pointer_spec_v1.md)
- role:
  - latest run을 빠르게 가리키는 representative pointer surface.
- strength:
  - receipt, per-run board, per-run commands, provenance compacted로 즉시 내려갈 수 있다.
- limitation:
  - 의미 판독 자체를 담지 않고 run-level operation pointer만 제공한다.

### 4. per-run evidence surfaces
- asset:
  - [runtime/views](/Users/sungsookim/universe/vectorfl_replica/runtime/views)
  - [runtime/commands](/Users/sungsookim/universe/vectorfl_replica/runtime/commands)
  - [runtime/receipts](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts)
- role:
  - 개별 실행 단위의 evidence-bearing artifact.
- strength:
  - 어떤 입력이 어떤 산출을 만들었는지 run 단위로 회수 가능하다.
- limitation:
  - 여러 run을 묶어 탐색 해석으로 번역하는 층은 약하다.

## C. provenance / trace assets

### 5. provenance index + compacted surface
- asset:
  - [runtime/manifests/provenance_link_index_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/provenance_link_index_v1.json)
  - [runtime/views/provenance_compacted_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/provenance_compacted_latest.md)
  - [docs/reports/provenance_accumulation_review_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/provenance_accumulation_review_v1.md)
- role:
  - source_doc_ref -> derived_target_ref 관계와 반복 누적 패턴을 보존한다.
- strength:
  - write_trace / evidence_refs / reingest 패턴 확인에 바로 쓸 수 있다.
- limitation:
  - relation_reason, borrowable_structure 같은 탐색 해석 필드는 없다.

### 6. origin maps
- asset:
  - [runtime/manifests/origin_maps](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/origin_maps)
  - [docs/contracts/origin_map_minimum_fields_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/origin_map_minimum_fields_v1.md)
- role:
  - 파생물에서 원문으로 돌아가는 최소 provenance handle.
- strength:
  - 공통 근거 재하강 경로로 재사용 가능하다.
- limitation:
  - 의미 판독이 아니라 source return handle이다.

## D. session / observer / user-language assets

### 7. Gemini observer session logs
- asset:
  - [runtime/observer/gemini](/Users/sungsookim/universe/vectorfl_replica/runtime/observer/gemini)
  - [codex_baseline_codex_gemini_session_batch_operation_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_baseline_codex_gemini_session_batch_operation_contract_v1.md)
  - [codex_baseline_session_id_and_gemini_log_link_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_baseline_session_id_and_gemini_log_link_contract_v1.md)
- role:
  - run 묶음을 session 단위로 읽고 사용자 언어 브리핑을 남기는 observer lane.
- strength:
  - 사용자 언어 번역층으로 재사용할 여지가 가장 크다.
- limitation:
  - 아직 exploration-specific relation template은 없다.

### 8. external case relation reading assets
- asset:
  - [external_case_example_saltlux_goover_relation_reading_v0.md](/Users/sungsookim/universe/vectorfl_replica/external_case_example_saltlux_goover_relation_reading_v0.md)
  - [docs/contracts/external_case_relation_reading_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/external_case_relation_reading_contract_v1.md)
- role:
  - 외부 기술 사례를 비교축 / 구조 차용 재료 / 분리 유지 판단 재료로 읽는 예시와 최소 필드.
- strength:
  - relation_kind / relation_reason / user_language_summary / future_use_hint를 이미 우리 문법으로 보여준다.
- limitation:
  - runtime observation artifact와 직접 연결된 표준 저장 위치는 아직 없다.

## E. document-layer semantic anchors

### 9. guides / contracts / reports / declarations / baselines
- asset:
  - [docs/guides](/Users/sungsookim/universe/vectorfl_replica/docs/guides)
  - [docs/contracts](/Users/sungsookim/universe/vectorfl_replica/docs/contracts)
  - [docs/reports](/Users/sungsookim/universe/vectorfl_replica/docs/reports)
  - root structured docs
- role:
  - 탐색 시 기존 철학, 운영 원칙, 설계 계약과 새 입력을 대면시키는 문서 레이어.
- strength:
  - 새 입력이 “우리와 같은가/다른가/차용 가능한가”를 비교하는 기준축으로 실전적이다.
- limitation:
  - 문서 간 관계 판독은 현재 사람이 해석해 기록해야 하며 자동 relation layer는 얕다.

## 현재 총평
- 이미 강한 것:
  - input formation
  - pointer/evidence/readback
  - provenance trace
  - session/run separation
  - external-case reading grammar seed
- 아직 약한 것:
  - relation kind를 표준 runtime 산출로 남기는 층
  - relation reason / borrowable structure / not adopted reason의 표준 기록 위치
  - exploration 결과를 session/run/pointer와 묶는 exploration observation artifact
