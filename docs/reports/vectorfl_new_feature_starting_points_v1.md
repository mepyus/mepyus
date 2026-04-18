# vectorfl_new_feature_starting_points_v1

## 1. Purpose
이 문서는 새 기능이나 새 프로그램을 만들 때
`어디부터 열어야 하는가` 를 빠르게 결정하기 위한 시작점 지도다.

핵심 목적:
- 이미 있는 스크립트/코드를 재사용하게 한다.
- 불필요한 재작업을 줄인다.
- 기능 종류에 따라 시작 경로를 다르게 잡게 한다.

---

## 2. Default Start Order
특별한 경우가 아니면 아래 순서로 시작하는 것이 맞다.

1. [vectorfl_status.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_status.md)
2. 관련 top-level `folder_status.md`
3. 관련 policy / spec / contract
4. 관련 실행 스크립트
5. 그 다음 실제 코드

즉 먼저 지도를 보고, 그 다음 실행면을 보고, 마지막에 코드로 내려간다.

---

## 3. Starting Point By Goal

### A. 구조화 문서를 넣고 처리하고 싶다
먼저 열 것:
- [document_routing_markers_policy_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/document_routing_markers_policy_v1.md)
- [structured_doc_routing_header_template_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/templates/structured_doc_routing_header_template_v1.md)
- [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
- [structured_internal_docs_registry_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/structured_internal_docs_registry_v1.json)

왜 여기서 시작하나:
- 현재 문서형 입력의 공식 진입점이 여기 있기 때문이다.

---

### B. 처리 결과를 한 번에 보고 싶다
먼저 열 것:
- [operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)
- [runtime/receipts](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts)
- [structured_doc_routing_commands_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/commands/structured_doc_routing_commands_v1.md)

왜 여기서 시작하나:
- ledger/registry/generated 결과를 직접 뒤지는 비용을 줄여준다.

---

### C. 작업 흔적과 provenance를 남기고 싶다
먼저 열 것:
- [event_schema_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/events/event_schema_v1.md)
- [record_operation_event.py](/Users/sungsookim/universe/vectorfl_replica/scripts/record_operation_event.py)
- [ticket_registry_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/ticket_registry_v1.json)
- [provenance_link_index_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/provenance_link_index_v1.json)

왜 여기서 시작하나:
- 지금 운영 골격의 핵심은 append-only 기록이기 때문이다.

---

### D. 입력 분절 / 라벨 / 앵커 / 위치를 건드리고 싶다
먼저 열 것:
- [app/input_layer/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/folder_status.md)
- [app/input_layer/source_locator/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/source_locator/folder_status.md)
- [app/input_layer/source_locator/origin_map_minimum_v1.py](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/source_locator/origin_map_minimum_v1.py)

왜 여기서 시작하나:
- 입력기 front door 와 provenance ingress 가 이 family 에 있기 때문이다.

---

### E. fragment / observer / connection 계산을 재사용하고 싶다
먼저 열 것:
- [app/fragment/schema.py](/Users/sungsookim/universe/vectorfl_replica/app/fragment/schema.py)
- [app/fragment/store.py](/Users/sungsookim/universe/vectorfl_replica/app/fragment/store.py)
- [app/runtime/observer.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/observer.py)
- [app/runtime/connection_engine.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/connection_engine.py)
- [app/core/runtime/connection_engine.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/connection_engine.py)

왜 여기서 시작하나:
- 현재 의미/연결 계산 family 의 중심이 여기 있다.

주의:
- `app/runtime` 와 `app/core/runtime` 은 같은 층이 아니다.
- 먼저 active layer 를 보고, 더 깊은 로직이 필요할 때 legacy bank 로 내려간다.

---

### F. report / view / workspace surface 를 만들고 싶다
먼저 열 것:
- [scripts/build_source_view.py](/Users/sungsookim/universe/vectorfl_replica/scripts/build_source_view.py)
- [scripts/build_measurement_view.py](/Users/sungsookim/universe/vectorfl_replica/scripts/build_measurement_view.py)
- [scripts/build_space_graph_view.py](/Users/sungsookim/universe/vectorfl_replica/scripts/build_space_graph_view.py)
- [app/runtime/reporting.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/reporting.py)
- [app/runtime/workspace_manifest.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/workspace_manifest.py)

왜 여기서 시작하나:
- 이미 결과 표면을 만드는 build/run family 가 존재한다.

---

### G. 새 프로그램 구조를 reference 에서 가져오고 싶다
먼저 열 것:
- [references/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/folder_status.md)
- [references/WashTank/preprocessed/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/folder_status.md)
- [reference_preprocessor_schema.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/reference_preprocessor_schema.md)
- [fragment_queue_policy_v1.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/fragment_queue_policy_v1.md)

왜 여기서 시작하나:
- 이미 “reference source -> preprocessed -> selective ingest” 구조가 있기 때문이다.

추천 reference:
- `officeout`, `officein`, `ehandler`, `inspection`, `washingwaiting`

---

### H. 기존 판단 실험과 비교하면서 만들고 싶다
먼저 열 것:
- [app/work/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/work/folder_status.md)
- [app/work/current_layer_baseline](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline)
- relevant probe stage folders

왜 여기서 시작하나:
- 지금 구조는 prior experiments 와의 비교를 전제로 강해진다.

---

## 4. Practical Reuse Shortcuts

### 새 structured-doc workflow가 필요할 때
- 기존 자산:
  - routing policy
  - routing wrapper
  - event recorder
  - receipt / board
- 새로 만들 필요 없는 것:
  - 문서 role header 체계
  - 최소 ticket/event/provenance skeleton

### 새 reference-based feature가 필요할 때
- 기존 자산:
  - WashTank preprocessor runner
  - fragment queue policy
  - reference sheets / compare boards
- 새로 만들 필요 없는 것:
  - source -> preprocessed -> ingest queue 기본 골격

### 새 operator-facing summary가 필요할 때
- 기존 자산:
  - receipt format
  - latest board seed
  - build_* view scripts
- 새로 만들 필요 없는 것:
  - 완전 새로운 dashboard 개념

---

## 5. Common Mistakes To Avoid
- 상위 status/atlas를 안 보고 바로 코드부터 열기
- `app/runtime` 와 root `runtime/` 를 혼동하기
- `app/runtime` 와 `app/core/runtime` 를 같은 층으로 읽기
- reference source 와 preprocessed lane 을 같은 층으로 읽기
- 모든 입력에 full flow를 강제하기

---

## 6. Current Best Entry Points
가장 실전적인 진입점은 아래 다섯 개다.

1. [vectorfl_status.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_status.md)
2. [scripts/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/scripts/folder_status.md)
3. [app/input_layer/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/folder_status.md)
4. [references/WashTank/preprocessed/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/references/WashTank/preprocessed/folder_status.md)
5. [runtime/views/operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)

---

## 7. One-Line Conclusion
새 기능이나 새 프로그램을 만들 때는 먼저 `무엇을 새로 만들까`가 아니라, `이미 있는 family 중 무엇을 가져다 쓸까`를 묻는 것이 맞고, 그 시작점은 status atlas 와 routing/reference/work families 에 이미 정리돼 있다.
