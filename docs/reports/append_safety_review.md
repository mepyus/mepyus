# append_safety_review

## 1. 현재 상태
- structured doc front door 는 [scripts/process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py) 에 있다.
- 이 경로는 `structured_internal_docs_registry_v1.json`, `ticket_registry_v1.json`, `provenance_link_index_v1.json`, `engine_event_ledger.jsonl`, `folder_activity/*.jsonl`, `runtime/receipts/*`, `runtime/views/operation_board_latest.md` 를 직접 갱신한다.
- 현재 append/write helper 는 `write_json()` 과 `append_jsonl()` 수준이며, file lock, temp-write-rename, idempotency key 는 없다.
- 기존 smoke 보고서도 [runtime/reports/core_input_layer_labeler_stabilization_smoke_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/reports/core_input_layer_labeler_stabilization_smoke_v1.md) 에서 registry/provenance race 흔적을 이미 지적했다.

## 2. 문제점 / 혼선 지점
- JSON registry 3종은 read-modify-write 방식이라 동시 실행 시 lost update 위험이 있다.
- provenance index 는 `row not in links` 검사 후 전체 파일 재기록이라 경쟁 상태에 취약하다.
- `engine_event_ledger.jsonl` 과 `folder_activity/*.jsonl` 는 append-only 이지만 partial line write, tail corruption, duplicate append 를 막는 장치가 없다.
- `runtime/views/operation_board_latest.md` 와 `runtime/commands/structured_doc_routing_commands_v1.md` 는 latest singleton 이라 동시 실행 시 마지막 실행이 이전 결과를 덮는다.
- receipt 와 generated file 은 개별 파일명에 run label 이 들어가 비교적 안전하지만, commands/board 는 per-run 분리가 없다.

## 3. 위험 파일 / 경로
- high risk
  - [runtime/manifests/structured_internal_docs_registry_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/structured_internal_docs_registry_v1.json)
  - [runtime/manifests/ticket_registry_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/ticket_registry_v1.json)
  - [runtime/manifests/provenance_link_index_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/provenance_link_index_v1.json)
- medium risk
  - [runtime/events/engine_event_ledger.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/events/engine_event_ledger.jsonl)
  - [runtime/events/folder_activity](/Users/sungsookim/universe/vectorfl_replica/runtime/events/folder_activity)
- overwrite-by-design risk
  - [runtime/views/operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)
  - [runtime/commands/structured_doc_routing_commands_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/commands/structured_doc_routing_commands_v1.md)

## 4. 최소 수정안
- registry/provenance write 를 공용 helper 로 모으고 temp file -> atomic rename 으로 바꾼다.
- 실행 단위마다 `job_id` 또는 `run_id` 를 생성해 receipt, events, provenance, command surface 에 함께 남긴다.
- registry/provenance row 에 `idempotency_key` 를 두고 같은 문서 재처리 시 중복 append 기준을 명시한다.
- JSONL append 에는 line flush 이후 tail validator 를 붙이고, malformed tail 발견 시 복구 루틴을 분리한다.
- latest board / commands 는 유지하되, 동시에 per-run board/commands artifact 를 별도 보관해 overwrite 를 감사 가능하게 만든다.

## 5. 파일 / 폴더 / 문서 영향 범위
- code
  - [scripts/process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
  - [scripts/record_operation_event.py](/Users/sungsookim/universe/vectorfl_replica/scripts/record_operation_event.py)
- runtime manifests/events/views/commands
  - [runtime/manifests](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests)
  - [runtime/events](/Users/sungsookim/universe/vectorfl_replica/runtime/events)
  - [runtime/views](/Users/sungsookim/universe/vectorfl_replica/runtime/views)
  - [runtime/commands](/Users/sungsookim/universe/vectorfl_replica/runtime/commands)

## 6. 패치 여부
- 이번 턴에서는 문서화만 수행했다.
- 이유: 경합 리스크는 명확하지만, write contract 를 먼저 잠그지 않은 상태에서 부분 패치부터 들어가면 기존 receipt/board semantics 를 깨뜨릴 수 있다.

## 7. 아직 남은 리스크
- 현재 구조는 sequential usage 에는 버티지만 parallel-safe 하다고 볼 수 없다.
- existing singleton views 는 append-only 철학과 부분 충돌한다.
- malformed tail recovery procedure 가 아직 코드화되지 않았다.

## 8. 다음 단계 추천
1. append helper contract 를 먼저 잠근다.
2. run-scoped artifact naming 과 idempotency key 형식을 정한다.
3. 그 다음 registry/provenance/event writer 를 한 번에 교체한다.
