# vectorfl_current_labeling_state_v1

## 1. Purpose
이 문서는 현재 `vectorfl_replica` 입력기를 통과할 때
`실제로 어떤 라벨이 붙고 있는지`와
`무엇이 아직 코어 labeler 로 잠기지 않았는지`를 구분해서 정리한 상태 문서다.

---

## 2. One-Line Answer
현재 엔진은 **라벨이 안 붙는 것이 아니라, 라벨이 여러 레이어에 이미 붙고 있다.**
다만 그 라벨 체계가 아직 `app/input_layer/labeler` 라는 독립 코어 모듈로 계약화되거나 구현되지는 않았다.

---

## 3. What Is Already Labeled

### A. document routing labels
붙는 곳:
- [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
- [document_routing_alias_map_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/document_routing_alias_map_v1.json)

대표 라벨:
- `docrole`
  - `directive`
  - `baseline`
  - `declaration`
  - `summary`
  - `memo`
  - `philosophical_interpretation`
- `runmode`
  - `ingest_only`
  - `ingest_then_execute`
  - `reference_only`
  - `execute_only`
- `priority`
  - `high`
  - `normal`
  - `low`

의미:
- 문서 입력이 어떤 역할인지
- 어떻게 처리해야 하는지
- 얼마나 우선순위가 높은지

현재 판정:
- 잘 붙고 있음
- 문서형 입력의 핵심 운영 라벨 층

---

### B. structured doc registry labels
붙는 곳:
- [structured_internal_docs_registry_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/structured_internal_docs_registry_v1.json)

대표 라벨:
- `input_class`
  - `structured_internal_doc`
- `processing_profile`
  - `minimal_preprocess`
  - `execution_coupled`
- `material_grade`
  - `grade_a`
- `role`
  - `declaration`
  - `baseline`
  - `directive`
  - `philosophical_interpretation`
- `execution_linkable`
  - `true`

의미:
- 문서를 어떤 등급의 엔진 재료로 볼지
- 실행과 연결 가능한지
- 어떤 처리 profile 로 들어오는지

현재 판정:
- 잘 붙고 있음
- document intake / registry 층의 메타 라벨

---

### C. ticket / event / status-related classification labels
붙는 곳:
- [ticket_registry_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/ticket_registry_v1.json)
- [event_schema_v1.md](/Users/sungsookim/universe/vectorfl_replica/runtime/events/event_schema_v1.md)
- 각 `folder_status.md`

대표 값:
- `ticket_class`
  - `operation_bootstrap`
  - `status_operation`
  - `structured_doc_intake`
  - `structured_doc_routing`
- `event_type`
  - `doc_registered`
  - `routing_normalized`
  - `ticket_created`
  - `execution_started`
  - `output_generated`
  - `receipt_written`
  - `board_updated`

의미:
- 이것이 어떤 종류의 작업인지
- 실제 어떤 사건이 일어났는지

현재 판정:
- 잘 붙고 있음
- 다만 이건 input-layer label 이라기보다 operation-layer 분류값

---

### D. anchor-side meaning handles
붙는 곳:
- [anchorizer.py](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/anchorizer/anchorizer.py)

대표 값:
- object anchors
- semantic rules
- structural rules

의미:
- fragment/input 에 의미 손잡이를 부여
- object / semantic / structure 수준의 고정점 제공

현재 판정:
- 라벨이라기보다 anchor handle 에 더 가까움
- 하지만 실제 의미 분류의 일부 역할도 수행 중

---

## 4. What Is Not Yet Locked As Core Labeler

### A. input-layer independent labeler module
현재 상태:
- [app/input_layer/labeler/folder_status.md](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/labeler/folder_status.md)
- 구현 파일 없음

비어 있는 이유:
- 지금 라벨은 `scripts`, `registry`, `manifest`, `status`, `ticket` 층에 분산돼 있음
- 하지만 `입력기 코어 label assignment` 라는 독립 모듈은 없음

즉 아직 없는 것:
- input material 에 붙는 코어 label helper
- label namespace 최소 정의
- label assignment entrypoint

---

### B. label family separation contract
현재는 아래가 실질적으로 존재하지만, 계약 문서로 잠기진 않음.

1. document routing labels
2. registry metadata labels
3. operation/ticket/event classification values
4. fragment/meaning-side labels or handles

문제:
- 서로 다른 층의 라벨이 실제로는 존재하는데
- 아직 한 문서에서 “이건 어떤 종류의 label 이다”라고 분리해 놓지 않았다

즉 아직 없는 것:
- `input label`
- `operation label`
- `retrieval/grouping label`
- `meaning-side label`
사이의 최소 구획 계약

---

### C. fragment-level explicit labeling layer
현재 상태:
- fragment 에 source/anchor/provenance/measurement 는 잘 들어갈 준비가 되어 있음
- 하지만 fragment-level label assignment 는 anchor에 비해 약하게 보임

즉 아직 약한 것:
- fragment group label
- reusable retrieval label
- observer/result side grouping label

---

## 5. Correct Current Reading

### 이미 있는 것
- 운영 메타 라벨은 이미 붙는다
- 문서 라우팅 라벨도 이미 붙는다
- ticket/event classification 도 이미 붙는다

### 아직 없는 것
- input-layer 코어 `labeler` 모듈
- 라벨 family 분리 contract
- fragment-level explicit label layer

즉 현재 상태는
**“labeling exists, but core labeler is not yet consolidated”**
라고 읽는 것이 맞다.

---

## 6. Practical Conclusion
현재 질문에 대한 가장 정확한 답은 아래다.

- 입력기를 통과할 때 라벨은 붙는다
- 특히 문서형 입력과 운영 메타 라벨은 꽤 잘 붙는다
- 하지만 그 라벨 체계가 아직 `app/input_layer/labeler` 라는 독립 코어 모듈로 정리되거나 잠기진 않았다

즉 문제는
`라벨이 없다`
가 아니라
`라벨이 여러 레이어에 흩어져 있고 코어 labeler 로 정리되지 않았다`
이다.

---

## 7. One-Line Conclusion
현재 `vectorfl_replica` 는 이미 라벨을 붙이고 있지만, 아직 그것을 하나의 `코어 입력기 labeler` 로 부르기에는 계약과 구현이 분산돼 있는 상태다.
