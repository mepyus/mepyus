# engine_overview

## 목적
이 문서는 지금 만든 엔진 구조를 사용자가 한눈에 이해할 수 있게 설명하는 개요 문서다.

한 줄 정의:

**문서를 넣으면 기록되고, 안전하게 쌓이고, 가볍게 조회되는 엔진이다.**

## 이 엔진을 어떻게 읽어야 하나
이 저장소는 단순 데이터 저장소가 아니다.
이 저장소는 문서와 실행 흔적이 들어오고, 기록되고, 나중에 다시 읽히는
**운영 흔적 보존 엔진**으로 읽는 것이 맞다.

즉 중요한 것은:
- 입력이 들어오는가
- 기록이 남는가
- 덜 깨지는가
- 나중에 다시 읽기 쉬운가

## 4층 구조

### 1. 입력층
여기서는 문서나 운영 재료가 들어온다.

예:
- structured doc
- 기준선 문서
- handoff 문서
- 운영 메모

대표 경로:
- [scripts/process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
- [runtime/manifests/document_routing_alias_map_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/document_routing_alias_map_v1.json)

### 2. 처리 / 기록층
여기서는 입력을 정규화하고, registry / provenance / event / receipt를 남긴다.

대표 경로:
- [runtime/manifests/structured_internal_docs_registry_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/structured_internal_docs_registry_v1.json)
- [runtime/manifests/provenance_link_index_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/provenance_link_index_v1.json)
- [runtime/events/engine_event_ledger.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/events/engine_event_ledger.jsonl)
- [runtime/receipts](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts)

### 3. 정리층
여기서는 raw 흔적을 지우지 않고, 더 읽기 쉽게 정리한다.

예:
- provenance compacted latest
- review / preview / bounded hygiene 결과

대표 경로:
- [runtime/views/provenance_compacted_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/provenance_compacted_latest.md)
- [runtime/manifests/provenance_compaction](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/provenance_compaction)

### 4. 조회층
여기서는 사람이 현재 상태를 빠르게 본다.

예:
- latest board
- latest commands
- per-run board
- per-run commands

대표 경로:
- [runtime/views/operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)
- [runtime/commands/structured_doc_routing_commands_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/commands/structured_doc_routing_commands_v1.md)

## latest vs per-run

### latest
- 대표 surface
- 지금 가장 최근 상태를 빠르게 가리킨다
- pointer 중심이다
- 얇아야 한다

대표 예:
- [runtime/views/operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)
- [runtime/commands/structured_doc_routing_commands_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/commands/structured_doc_routing_commands_v1.md)

### per-run
- 근거 surface
- 특정 run의 상세 결과를 보관한다
- 내용이 그대로 살아 있다

대표 예:
- [runtime/views](/Users/sungsookim/universe/vectorfl_replica/runtime/views)
- [runtime/commands](/Users/sungsookim/universe/vectorfl_replica/runtime/commands)

## raw vs compacted

### raw
- 원본 흔적
- 감사와 복구의 기준
- 지우지 않는 것이 기본

### compacted
- 읽기 쉬운 보조 surface
- raw를 대체하지 않음
- 운영 가독성을 높이기 위한 층

## 왜 append-only / atomic / lock / recovery / pointer가 중요한가
- append-only:
  - 흔적을 먼저 남긴다
- atomic:
  - 중간에 깨진 파일이 생길 가능성을 줄인다
- lock:
  - 동시에 기록할 때 덜 깨지게 한다
- recovery:
  - ledger tail이 깨져도 정상 부분을 살릴 수 있게 한다
- pointer:
  - latest surface를 얇게 유지하고, 상세는 per-run에 남긴다

## 폴더 역할도 같이 기억하면 좋다
- `contracts/` = 법 / 절대 기준
- `policies/` = 운영 규정
- `reports/` = 분석 / 결과
- `guides/` = 사용 설명서 / 운영 메뉴얼

## 한 줄 결론
이 엔진은 파일을 모아두는 저장소가 아니라,
문서와 실행 흔적이 살아남고 다시 읽히는 운영 엔진이다.
