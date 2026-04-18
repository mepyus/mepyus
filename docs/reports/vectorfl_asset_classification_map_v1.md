# vectorfl_asset_classification_map_v1

## 1. Purpose
이 문서는 `vectorfl_replica` 안에 이미 존재하는 자산을
`무엇을 위한 자산인가` 기준으로 빠르게 분류하기 위한 실전 지도다.

핵심 목적:
- 이미 가진 자산을 다시 만들지 않게 한다.
- 새 기능/프로그램 작업 전 어떤 family 가 이미 있는지 빠르게 확인하게 한다.
- 코드, 문서, 실행 기록, reference 가 서로 다른 자산이라는 점을 분명히 한다.

---

## 2. Top Asset Reading
현재 자산은 크게 아래 8개 family 로 읽는 것이 맞다.

1. 철학 / 운영 기준 자산
2. 구조 탐색 / status atlas 자산
3. 입력 / 라우팅 자산
4. fragment / measurement / observer 자산
5. 실행 / 운영 기록 자산
6. 조회 / receipt / command 자산
7. reference / calibration 자산
8. 실험 / probe / work 기록 자산

---

## 3. Asset Families

### A. 철학 / 운영 기준 자산
역할:
- 엔진을 어떤 철학과 운영 계약으로 읽을지 고정
- 새 기능이 코어를 훼손하지 않게 기준 제공

핵심 파일:
- [CURRENT.md](/Users/sungsookim/universe/vectorfl_replica/CURRENT.md)
- [vectorfl_status.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_status.md)
- [engine_philosophy_declaration_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/engine_philosophy_declaration_v1.md)
- [current_layer_baseline_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/current_layer_baseline_contract_v1.md)
- [codex_declaration_vectorfl_replica_material_and_operation_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_declaration_vectorfl_replica_material_and_operation_v1.md)
- [codex_baseline_vectorfl_replica_intake_and_operation_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_baseline_vectorfl_replica_intake_and_operation_v1.md)
- [codex_directive_vectorfl_replica_bootstrap_and_operation_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_directive_vectorfl_replica_bootstrap_and_operation_v1.md)
- [vectorfl_philosophical_interpretation_v1.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_philosophical_interpretation_v1.md)

재사용 포인트:
- 새 구조를 만들기 전에 반드시 먼저 보는 기준선

---

### B. 구조 탐색 / status atlas 자산
역할:
- repo 전체 구조를 다시 파악하는 비용을 줄임
- 폴더별 기관 역할과 우선순위를 빠르게 보여줌

핵심 파일:
- [app/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/folder_status.md)
- [scripts/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/scripts/folder_status.md)
- [runtime/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/runtime/folder_status.md)
- [references/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/folder_status.md)
- [app/runtime/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/runtime/folder_status.md)
- [app/input_layer/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/folder_status.md)
- [app/core/runtime/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/folder_status.md)
- [references/WashTank/preprocessed/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/folder_status.md)

재사용 포인트:
- 새 작업 시작 전 “무엇이 이미 있는가”를 찾는 첫 관문

---

### C. 입력 / 라우팅 자산
역할:
- 문서와 입력을 받아 `parse -> normalize -> register -> optional execute` 로 보냄
- 입력기를 repo-scale engine 안으로 흡수하는 front door

핵심 파일:
- [app/input_layer/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/folder_status.md)
- [app/input_layer/source_locator/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/source_locator/folder_status.md)
- [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
- [document_routing_markers_policy_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/document_routing_markers_policy_v1.md)
- [structured_doc_routing_header_template_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/templates/structured_doc_routing_header_template_v1.md)
- [document_routing_alias_map_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/document_routing_alias_map_v1.json)
- [origin_map_minimum_v1.py](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/source_locator/origin_map_minimum_v1.py)
- [origin_map_minimum_fields_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/origin_map_minimum_fields_v1.md)

재사용 포인트:
- 정제된 문서 입력
- 라우팅/런모드 처리
- origin map 최소 provenance 손잡이

---

### D. fragment / measurement / observer 자산
역할:
- fragment 중심 저장과 observer 지원을 담당
- 입력을 의미 형성 가능한 단위로 붙잡음

핵심 파일:
- [app/fragment/schema.py](/Users/sungsookim/universe/vectorfl_replica/app/fragment/schema.py)
- [app/fragment/store.py](/Users/sungsookim/universe/vectorfl_replica/app/fragment/store.py)
- [app/fragment/projector.py](/Users/sungsookim/universe/vectorfl_replica/app/fragment/projector.py)
- [app/measurement/observer.py](/Users/sungsookim/universe/vectorfl_replica/app/measurement/observer.py)
- [app/measurement/ambient_probe.py](/Users/sungsookim/universe/vectorfl_replica/app/measurement/ambient_probe.py)
- [app/measurement/seed_bank.py](/Users/sungsookim/universe/vectorfl_replica/app/measurement/seed_bank.py)
- [app/runtime/observer.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/observer.py)
- [app/runtime/connection_engine.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/connection_engine.py)

재사용 포인트:
- fragment 저장 구조
- observer 지원
- connection / evidence 계산

---

### E. 실행 / 운영 기록 자산
역할:
- append-only event
- ticket / doc registry / provenance link
- later compaction 기반

핵심 파일:
- [record_operation_event.py](/Users/sungsookim/universe/vectorfl_replica/scripts/record_operation_event.py)
- [event_schema_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/events/event_schema_v1.md)
- [engine_event_ledger.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/events/engine_event_ledger.jsonl)
- [structured_internal_docs_registry_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/structured_internal_docs_registry_v1.json)
- [ticket_registry_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/ticket_registry_v1.json)
- [provenance_link_index_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/provenance_link_index_v1.json)

재사용 포인트:
- 작업 사건 기록
- 문서-티켓-결과 추적
- later receipt/compaction 자료

---

### F. 조회 / receipt / command 자산
역할:
- registry/ledger/generated 결과를 사람이 한 번에 확인하는 표면

핵심 파일:
- [operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)
- [structured_doc_routing_commands_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/commands/structured_doc_routing_commands_v1.md)
- [runtime/receipts](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts)

재사용 포인트:
- 최근 처리 확인
- 재실행 명령 확인
- 여러 파일로 흩어진 결과를 receipt로 묶기

---

### G. reference / calibration 자산
역할:
- 과거 구조와 현재 입력/판독을 비교 교정
- 새 프로그램 만들 때 구조 재료로 재사용

핵심 파일:
- [references/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/folder_status.md)
- [references/WashTank/preprocessed/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/folder_status.md)
- [run_reference_preprocessor_v0.py](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/run_reference_preprocessor_v0.py)
- [reference_preprocessor_schema.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/reference_preprocessor_schema.md)
- [fragment_queue_policy_v1.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/fragment_queue_policy_v1.md)
- [fragment_ingest_queue_v1_sample.json](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/fragment_ingest_queue_v1_sample.json)

재사용 포인트:
- source -> preprocessed -> ingest queue 구조
- 페이지/프로그램 구조 재활용
- calibration lane

---

### H. 실험 / probe / work 기록 자산
역할:
- 현재 엔진이 왜 이렇게 읽히는지 보여주는 실험 기억
- 새로운 판단 규칙을 만들기 전 비교 근거 제공

핵심 위치:
- [app/work/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/work/folder_status.md)
- [app/work/current_layer_baseline](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline)
- [app/work/observer_ingest_min](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min)
- mixed/corridor stage 폴더들

재사용 포인트:
- 기존 판단 실험 재검토
- 새 규칙 도입 전 prior evidence 확인

---

## 4. What Is Already Strong
- 철학 / baseline 문서층
- status atlas 기반 구조 탐색
- structured doc routing
- append-only event skeleton
- receipt / latest board seed surface
- WashTank reference preprocessed lane

---

## 5. What Is Still Thin
- `app/runtime` vs `app/core/runtime` 경계 압축 설명
- `runtime/manifests` 내부 family 세분화
- specialized/backfill scripts family taxonomy

---

## 6. Current Practical Rule
새 작업 전에 아래 순서로 보는 것이 가장 효율적이다.

1. [vectorfl_status.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_status.md)
2. 관련 top-level [folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/folder_status.md)
3. 관련 family 의 `status / policy / spec`
4. 그 다음 실제 코드/스크립트

---

## 7. One-Line Conclusion
현재 `vectorfl_replica` 는 단순 코드 저장소가 아니라, 이미 `철학 / 입력 / 실행 / 기록 / 조회 / reference 재사용` 자산을 각각 가진 repo-scale engine 작업공간으로 읽는 것이 맞다.
