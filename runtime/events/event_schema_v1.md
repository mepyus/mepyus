# event_schema_v1

## 1. 목적
이 문서는 `vectorfl_replica` 의 append-only 운영 기록을 위한 최소 이벤트 스키마를 고정한다.

## 2. 기본 원칙
- event 는 append-only 로 남긴다.
- event 는 사실 기록이다.
- event 는 label / ticket / status 와 역할이 다르다.
- status 문서는 event 를 나중에 compaction 한 설명층이다.

## 3. 최소 필드
- `event_id`
- `event_type`
- `timestamp`
- `actor`
- `target_ref`
- `source_doc_ref`
- `ticket_ref`
- `status`
- `notes`

## 4. 선택 필드
- `folder_ref`
- `output_ref`
- `derived_from`
- `label_refs`
- `metadata`

## 5. 최소 event_type 예시
- `doc_registered`
- `routing_normalized`
- `ticket_created`
- `execution_started`
- `file_created`
- `file_updated`
- `script_registered`
- `script_run`
- `output_generated`
- `receipt_written`
- `board_updated`
- `run_failed`
- `status_compaction_needed`
- `status_compacted`

## 6. 저장 위치

### global ledger
- `runtime/events/engine_event_ledger.jsonl`

### folder activity logs
- `runtime/events/folder_activity/app.folder_activity_log.jsonl`
- `runtime/events/folder_activity/scripts.folder_activity_log.jsonl`
- `runtime/events/folder_activity/runtime.folder_activity_log.jsonl`
- `runtime/events/folder_activity/references.folder_activity_log.jsonl`

## 7. compaction 연결
status 문서는 아래를 직접 대체하지 않는다.
- global ledger
- folder activity logs

대신 status 문서는 아래를 요약한다.
- 어떤 사건이 최근 있었는가
- 어떤 이벤트 범위까지 반영되었는가
- 어떤 compaction 이 필요한가
