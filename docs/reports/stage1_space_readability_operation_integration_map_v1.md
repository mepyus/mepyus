# stage1_space_readability_operation_integration_map_v1

## 목적
탐색 결과가 현재 엔진의
- 입력층
- 처리/기록층
- 정리층
- 조회층
- change-based operation
- session / observer
- docs / runtime 배치

와 각각 어떻게 접속되는지 한 장으로 정리한다.

## 1. 입력층 접속

### current connection
- source:
  - [scripts/process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
  - [runtime/manifests/label_packets](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/label_packets)
  - [app/work/observer_ingest_min/generated](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/generated)
- meaning:
  - 새 입력은 structured doc routing으로 들어오고
  - label packet과 observer_ingest_min outputs를 통해 최소 형성 흔적을 남긴다.

### exploration implication
- 탐색 결과의 `input_ref`, `input_summary`, `focus_labels`, `focus_anchor` 는 이 층의 산출을 재사용해야 한다.
- 탐색은 입력층을 대체하지 않고, 입력층 위에서 relation readout을 얹는다.

## 2. 처리/기록층 접속

### current connection
- source:
  - [runtime/manifests/structured_internal_docs_registry_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/structured_internal_docs_registry_v1.json)
  - [runtime/manifests/provenance_link_index_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/provenance_link_index_v1.json)
  - [runtime/events/engine_event_ledger.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/events/engine_event_ledger.jsonl)
  - [runtime/receipts](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts)
  - [runtime/views](/Users/sungsookim/universe/vectorfl_replica/runtime/views)
  - [runtime/commands](/Users/sungsookim/universe/vectorfl_replica/runtime/commands)
- meaning:
  - 현재 엔진은 입력이 어떤 기록을 만들었는지 이미 충분히 남긴다.

### exploration implication
- 탐색 결과의 `write_trace`, `evidence_refs`, `related_run_ids` 는 이 층과 직접 연결되어야 한다.
- 다만 `relation_kind`, `relation_reason`, `borrowable_structure` 는 아직 이 층의 표준 필드가 아니다.

### bounded rule
- 지금 단계에서는 처리/기록층 core schema를 늘리지 않는다.
- 탐색 판독은 sidecar observation 또는 별도 note로 붙이고, core trace는 pointer로만 재사용한다.

## 3. 정리층 접속

### current connection
- source:
  - [runtime/views/provenance_compacted_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/provenance_compacted_latest.md)
  - [runtime/manifests/provenance_compaction](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/provenance_compaction)
  - [docs/reports/provenance_accumulation_review_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/reports/provenance_accumulation_review_v1.md)
- meaning:
  - provenance hygiene는 이미 반복 흔적과 중복 노이즈를 다시 읽는 정리층이다.

### exploration implication
- 탐색 결과도 나중에
  - 잘못된 차용
  - 중복된 relation readout
  - 오래된 separation 판단
를 다시 읽고 정리할 수 있어야 한다.

### bounded rule
- 지금은 exploration 결과를 provenance index에 직접 넣지 않는다.
- 대신 observer/exploration sidecar로 남기고, 나중에 정리층에서 다시 읽을 수 있게 pointer를 유지한다.

## 4. 조회층 접속

### current connection
- source:
  - [runtime/views/operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)
  - per-run boards
  - per-run commands
  - receipts
- meaning:
  - latest는 representative pointer, per-run은 evidentiary surface라는 분리가 이미 있다.

### exploration implication
- 탐색 페이지도 새 저장 체계를 먼저 만들기보다
  - latest pointer
  - per-run evidence
  - provenance compacted
  - observer log
를 재배치해서 읽는 것이 우선이다.

### bounded rule
- latest board를 relation dashboard로 확장하지 않는다.
- 탐색 readout은 별도 observation artifact를 두고 latest/per-run은 근거면으로만 재사용한다.

## 5. change-based operation 접속

### current connection
- source:
  - [runtime/manifests/folder_changes/folder_change_log.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/folder_changes/folder_change_log.jsonl)
  - [runtime/manifests/folder_inventory](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/folder_inventory)
  - rendered `folder_status.md`
- meaning:
  - 현재 운영 기준은 전체 재독해가 아니라 change log + inventory + partial sync + rendered status다.

### exploration implication
- 탐색 결과도 장기적으로
  - 새 observation note 생성
  - sidecar json 추가
  - 관련 folder inventory 갱신
  - rendered status 재렌더
흐름으로 붙는 것이 맞다.

### bounded rule
- 탐색 결과 자체를 모든 change log 사실로 자동 승격하지 않는다.
- 우선은 파일 생성/갱신 사건을 change log에 남기고, relation semantics는 sidecar 본문에 둔다.

## 6. session / observer 접속

### current connection
- source:
  - [runtime/observer/gemini](/Users/sungsookim/universe/vectorfl_replica/runtime/observer/gemini)
  - session baseline docs
  - related run pointers
- meaning:
  - run은 개별 실행, session은 작업 묶음, Gemini는 후단 observer라는 기준이 이미 잠겨 있다.

### exploration implication
- 탐색 결과는 개별 run만으로 끝내지 않고 session 기억 위에 놓는 것이 맞다.
- `related_run_ids` 와 `related_session_ids` 가 같이 있어야 한다.
- Gemini는 탐색 결과에 대해 브리핑 / 요약 / 의심 지점 표시를 줄 수 있다.

### bounded rule
- Gemini output은 engine data가 아니라 observer readout으로만 남긴다.
- 탐색 관련 Gemini 결과도 `runtime/observer/gemini/`에만 둔다.

## 7. docs / runtime 배치 접속

### docs/contracts
- 역할:
  - 탐색 최상위 정의
  - 결과 최소 필드
  - 관계 판독 불변 기준
- current examples:
  - [stage1_exploration_result_minimum_fields_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/stage1_exploration_result_minimum_fields_contract_v1.md)
  - [external_case_relation_reading_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/external_case_relation_reading_contract_v1.md)

### docs/reports
- 역할:
  - 실제 사례 readout
  - 자산 맵
  - 갭 분석
  - bounded attachment plan

### docs/templates
- 역할:
  - exploration note / sidecar를 쓸 때 빠지기 쉬운 항목 강제
- current example:
  - [stage1_exploration_observation_note_template_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/templates/stage1_exploration_observation_note_template_v1.md)

### runtime/observer
- 역할:
  - session별 관찰 로그
  - Gemini 후단 판독 결과
  - 앞으로 exploration observation artifact를 담을 가장 자연스러운 런타임 레인

## 8. one-line integration verdict
탐색 기능은 현재 엔진 바깥의 새 시스템이 아니라,
**입력층에서 focus를 잡고, 처리/기록층의 pointer/evidence/provenance를 재사용하며, 정리층에서 나중 점검 가능성을 남기고, 조회층에서는 latest/per-run/observer를 재배치해서 읽는 보조 해석 절차**로 붙이는 것이 맞다.
