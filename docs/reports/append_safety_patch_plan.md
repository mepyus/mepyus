# append_safety_patch_plan

## 1. 목표
- registry/provenance/event write 를 병렬 실행에서 덜 깨지게 만든다.
- append-only 철학을 유지하면서 latest surface overwrite 를 감사 가능하게 만든다.

## 2. 패치 범위
- phase 1
  - 공용 atomic write helper 추가
  - run_id / job_id 도입
  - registry/provenance row 에 idempotency key 추가
- phase 2
  - JSONL tail validator / recovery helper 추가
  - per-run commands / per-run board artifact 추가
  - latest board 는 pointer surface 로 축소

## 3. 변경 대상
- [scripts/process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
- [scripts/record_operation_event.py](/Users/sungsookim/universe/vectorfl_replica/scripts/record_operation_event.py)
- 신규 helper 후보:
  - `app/core/registry/atomic_io.py`
  - `app/core/events/event_append_guard.py`

## 4. 세부 계획

### A. atomic json rewrite
- `write_json()` 을 temp path write 후 `Path.replace()` 하는 helper 로 교체
- rewrite 전 현재 payload hash 와 row count 를 함께 계산해 debug trail 남김

### B. run identity
- structured doc routing 시작 시 `run_id` 생성
- receipt / events / provenance / commands / board 에 모두 남김
- observer ingest 의 returned `run_id` 와 별도여도 되지만 parent-child link 를 남김

### C. idempotency
- key shape 후보:
  - `structured-doc::<doc_ref>::<normalized_runmode>::<content_hash>`
- 같은 key 가 registry/provenance 에 있으면 append skip 또는 update-only 규칙 적용

### D. malformed tail recovery
- jsonl reader 가 마지막 line parse 실패 시:
  - raw tail backup
  - valid lines 만 복구
  - recovery event 기록

### E. latest surface split
- `operation_board_latest.md` 는 latest pointer 와 caution 만 유지
- 상세 board 는 `runtime/views/operation_board_<run_id>.md`
- commands 역시 `runtime/commands/structured_doc_routing_commands_<run_id>.md` 추가

## 5. 선행 결정 필요
- `run_id` 와 observer returned run id 를 통합할지 분리할지
- duplicate 처리 정책을 update 로 볼지 append skip 으로 볼지
- latest singleton 을 유지할지 symbolic pointer 개념으로 바꿀지

## 6. 완료 기준
- registry/provenance rewrite 가 atomic contract 를 따름
- run identity 가 receipt/events/manifests 에 남음
- per-run surface 가 생겨 latest overwrite 의 감사 흔적이 남음
- malformed tail recovery rule 이 문서와 코드에 모두 존재함
