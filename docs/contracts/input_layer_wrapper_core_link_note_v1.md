# input_layer_wrapper_core_link_note_v1

## 1. Purpose
이 문서는 structured doc intake 에서
wrapper 와 core input-layer labeler 의 책임 경계를 잠그는 최소 연결 노트다.

핵심 목적:
- wrapper 가 labeler 전체를 대신한다고 읽히는 것을 막는다
- labeler 가 routing/event/ticket 전부를 먹는다고 읽히는 것을 막는다
- packet 생성과 operation 생성 책임을 분리한다

---

## 2. Core Declaration
- wrapper 는 intake orchestration / routing flow 연결층이다.
- core input-layer labeler 는 external routing labels 를 core intake labels 로 정규화하여 `label_packet` 으로 조립하는 입력 정규화 중심 계층이다.
- wrapper 는 labeler 를 호출하지만, operation label / event / ticket 생성을 labeler 책임으로 넘기지 않는다.
- labeler 는 routing / event / ticket / anchor 전체를 흡수하지 않는다.

---

## 3. Responsibility Split

### wrapper responsibility
- 문서 입력 흐름 수용
- routing marker 파싱
- 적절한 순서로 core labeler 호출
- label packet 저장 위치 연결
- registry / manifest / operation 흐름으로 handoff
- optional execution / receipt / board 연결

### core labeler responsibility
- external routing labels 정규화
- core intake labels 조립
- label packet 생성

### explicitly outside current core labeler
- ticket / event / status operation classification
- anchor / meaning-side handles
- fragment retrieval / grouping labels
- UI / view-level labeling
- broader non-structured-doc labeling 전반

---

## 4. Handoff Boundary
현재 handoff 흐름은 아래처럼 읽는 것이 맞다.

1. input doc received
2. routing markers parsed
3. wrapper calls core labeler
4. core labeler returns `label_packet`
5. wrapper stores / attaches packet
6. downstream operation / ticket / event layers continue separately

중요:
- packet 생성과 operation 생성은 같은 흐름 안에 있지만 같은 책임은 아니다
- wrapper 는 orchestration 쪽이고, labeler 는 normalization/packet 쪽이다

---

## 5. Current Practical Reading
- [scripts/process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py) 는 현재 structured doc intake wrapper 다
- [app/input_layer/labeler/labeler.py](/Users/sungsookim/universe/vectorfl_replica/app/input_layer/labeler/labeler.py) 는 current core input-layer labeler 다
- 현재 구조는 `wrapper -> core labeler -> downstream operation` 으로 읽는 것이 맞다

---

## 6. One-Line Conclusion
현재 structured doc intake 에서 wrapper 는 흐름을 조직하고, core input-layer labeler 는 label normalization 과 packet 조립을 맡으며, operation/ticket/event 는 그 다음 층에서 따로 계속된다.
