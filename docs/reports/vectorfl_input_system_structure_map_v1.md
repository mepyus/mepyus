# vectorfl_input_system_structure_map_v1

## 1. Purpose
이 문서는 현재 `vectorfl_replica` 입력기 구조를
`실제 어디가 front door 이고, 어디가 코어 부품층이며, 어디서 산출이 나오는가`
기준으로 한 장에 정리한 구조도다.

핵심 목적:
- 입력기가 지금 어떤 상태인지 한 번에 보이게 한다.
- 문서형 입력과 일반 입력이 어떤 경로를 타는지 구분한다.
- 다음 보강 작업 전 현재 구조를 오해하지 않게 한다.

---

## 2. One-Line Reading
현재 입력기는 하나의 단일 모듈이 아니라,
**`scripts` 의 문서형 routing front door + `app/input_layer` 의 코어 부품층 + `observer_ingest_min` 의 실용 split/trace 산출면** 으로 나뉜 3분화 구조다.

---

## 3. Current Input Flow

### A. structured doc flow
`structured doc`
-> [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
-> parse / normalize
-> doc registry / ticket / event
-> [run_observer_ingest_min.py](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py)
-> generated outputs
-> origin map seed
-> receipt / latest board

### B. core input component flow
`raw input material`
-> `segmenter`
-> `anchorizer`
-> `source_locator`
-> `fragment / measurement / runtime downstream`

즉 실제 운영 경로와 코어 입력 부품 경로가 완전히 하나로 합쳐진 상태는 아니다.

---

## 4. Input Families

### A. routing front door
역할:
- 문서 라우팅 표식 파싱
- alias 정규화
- runmode 결정
- registry/ticket/event 연결

핵심 파일:
- [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
- [document_routing_markers_policy_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/document_routing_markers_policy_v1.md)
- [structured_doc_routing_header_template_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/templates/structured_doc_routing_header_template_v1.md)
- [document_routing_alias_map_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/document_routing_alias_map_v1.json)

현재 판정:
- 문서형 입력의 실제 front door
- input layer core 가 아니라 operating-arm wrapper

---

### B. split / fragmentization layer
역할:
- 입력을 dust/fragment 후보로 자르는 층

핵심 파일:
- [experimental_segmenter.py](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/segmenter/experimental_segmenter.py)
- [experimental_segmenter_v2.py](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/segmenter/experimental_segmenter_v2.py)
- [run_observer_ingest_min.py](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/run_observer_ingest_min.py)

현재 판정:
- `app/input_layer/segmenter` 는 experimental split layer
- 실제 실용 split 확인은 `observer_ingest_min` 이 더 강함

---

### C. anchorization layer
역할:
- 입력/fragment 에 anchor handle 부여
- known object / semantic / structural 신호 부착

핵심 파일:
- [anchorizer.py](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/anchorizer/anchorizer.py)

현재 판정:
- 코어 의미 고정층
- 단순 키워드 태깅보다 강한 실체가 있음

---

### D. source location / provenance ingress layer
역할:
- 원본 위치 추적
- origin map seed 생성
- source return handle 준비

핵심 파일:
- [locator.py](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/source_locator/locator.py)
- [origin_map_minimum_v1.py](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/source_locator/origin_map_minimum_v1.py)
- [origin_map_minimum_fields_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/contracts/origin_map_minimum_fields_v1.md)

현재 판정:
- locator-only utility 가 아니라 provenance ingress helper

---

### E. labeling layer
역할:
- 입력 class / role / grouping / retrieval label 부여

현재 상태:
- [app/input_layer/labeler/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/labeler/folder_status.md)
- 실질 코드 파일 부재

현재 판정:
- concept slot 은 있음
- implementation 은 비어 있음

---

## 5. Input-Related Runtime Assets

### metadata / registry
- [structured_internal_docs_registry_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/structured_internal_docs_registry_v1.json)
- [ticket_registry_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/ticket_registry_v1.json)
- [provenance_link_index_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/provenance_link_index_v1.json)

### event / receipt / board
- [engine_event_ledger.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/events/engine_event_ledger.jsonl)
- [runtime/receipts](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts)
- [operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)

이 자산들은 입력기 바깥 부산물이 아니라,
현재 입력기가 repo 전체에 흡수된 결과 표면이다.

---

## 6. Current Strengths
- structured doc intake 는 이미 강하다
- runmode / routing 이 붙어 있다
- provenance/origin seed 가 붙는다
- event/ticket/receipt 로 운영 객체화 된다
- anchor layer 는 실체가 있다

---

## 7. Current Weak Spots
- `labeler` 실체 부재
- `segmenter` 가 아직 experimental bank
- wrapper 와 core input layer 의 연결 계약이 약하다
- `observer_ingest_min` 과 core input layer 의 역할 경계가 아직 분리된 상태다

---

## 8. Correct Current Reading
- `app/input_layer` = 입력기 코어 부품층
- `scripts/process_structured_doc_with_routing.py` = 문서형 입력 front door
- `observer_ingest_min` = 현재 가장 실용적인 split/trace 확인면

즉 지금 입력기는 `완성된 단일 intake engine` 이 아니라
`운영 intake + 코어 부품 + 실용 split surface` 가 분리된 구조로 읽는 것이 맞다.

---

## 9. One-Line Conclusion
현재 입력기는 약한 것이 아니라 `문서형 입력엔 강하고, 코어 input layer 는 아직 정리 중인 과도기형 구조`로 보는 것이 정확하다.
