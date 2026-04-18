# vectorfl_input_system_upgrade_priorities_v1

## 1. Purpose
이 문서는 현재 입력기에서 다음에 무엇을 보강해야 하는지
우선순위 기준으로 정리한 작업 지도다.

핵심 목적:
- 입력기 보강을 과도하게 넓히지 않는다.
- 지금 실제로 가치가 큰 보강 순서를 고정한다.
- “무엇이 부족한가”를 기능적 결핍이 아니라 구조 정리 관점에서 본다.

---

## 2. Priority Rule
현재 입력기 보강은 아래 순서가 맞다.

1. `labeler` 실체화
2. `segmenter` 계약화
3. routing wrapper 와 core input layer 연결 명시
4. `observer_ingest_min` 과 input core 관계 정리
5. later: manifests / provenance 세분화

즉 지금은 새 fancy intake 를 만드는 턴이 아니라,
이미 있는 입력기 조각들을 더 일관되게 묶는 턴이 맞다.

---

## 3. Priority 1 — labeler 실체화
현재 상태:
- `labeler` 는 status 에선 중요한 하위 영역
- 실제 구현 파일은 없음

왜 가장 먼저인가:
- 지금은 routing metadata, doc role, material grade, status labels, engine component labels 가
  여러 레이어에 흩어져 있다.
- 입력기 안에서 “무엇을 라벨이라 부를 것인가”를 받쳐주는 코어 부품이 비어 있다.

최소 목표:
- `input label` 과 `operation metadata label` 을 구분해서 담을 수 있는 최소 helper
- retrieval/grouping 목적의 lightweight labeling layer

주의:
- 거대한 ontology 편집기로 가면 안 된다.
- 최소 label assignment/helper 수준이 맞다.

---

## 4. Priority 2 — segmenter 계약화
현재 상태:
- `experimental_segmenter.py`
- `experimental_segmenter_v2.py`
- 실험층 위주

왜 중요한가:
- split 은 입력기의 가장 앞단인데, 현재는 experimental bank 와 `observer_ingest_min` 실용 split 이 분리돼 있다.
- 이 상태가 길어지면 core input layer 와 운영 split 면이 계속 따로 논다.

최소 목표:
- `current preferred split rule` 을 한 장으로 잠그기
- 어떤 입력에 어떤 split mode 를 우선 쓰는지 명시
- experimental bank 와 current preferred path 구분

주의:
- 이번 단계에서 완전한 universal splitter 를 만들 필요는 없다.
- 먼저 “현행 truth” 만 잠그면 된다.

---

## 5. Priority 3 — routing wrapper 와 input layer 연결 명시
현재 상태:
- structured doc intake 는 `scripts/process_structured_doc_with_routing.py`
- core 부품층은 `app/input_layer`

왜 중요한가:
- 지금은 문서형 입력 front door 가 코어 입력층 밖에서 돌아간다.
- 구조는 괜찮지만, 장기적으로는 둘 관계가 더 명시돼야 탐색성이 좋아진다.

최소 목표:
- wrapper 가 어떤 input-layer 기능을 사실상 대체/우회/호출하는지 문서로 명시
- later 에 어떤 부분을 input core 로 내릴지 구분

주의:
- 이번 단계에서 곧바로 리팩터링할 필요는 없다.
- 문서/contract 수준 연결 명시가 먼저다.

---

## 6. Priority 4 — observer_ingest_min 과 input core 관계 정리
현재 상태:
- `observer_ingest_min` 이 실제 split/trace/operator summary 면으로 강함
- 그러나 위치는 `app/work` 실험/실용 lane 쪽

왜 중요한가:
- 실제론 많은 입력이 여기로 들어가는데, status 상으로는 core input truth 처럼 읽히지 않는다.
- 장기적으로는 `실용 operator ingest` 와 `input core` 의 관계를 더 명확히 해야 한다.

최소 목표:
- `observer_ingest_min = operator-facing practical intake surface`
- `app/input_layer = core components`
이 관계를 한 장으로 잠그기

주의:
- 바로 코어로 승격할지 여부는 다음 문제다.
- 지금은 역할 정의가 먼저다.

---

## 7. Priority 5 — later manifest/provenance refinement
현재 상태:
- origin map minimum
- doc/ticket/provenance registry
- append-only ledger

왜 후순위인가:
- 현재도 충분히 작동한다.
- 지금 더 시급한 건 split/label/front door 쪽이다.

later 목표:
- `runtime/manifests` 내부 family 분화
- origin map beyond receipt_seed
- richer fragment-level provenance

---

## 8. What Not To Do Next
- 모든 입력 타입 universal intake 를 한 번에 만들기
- 거대한 ontology/label namespace 설계부터 들어가기
- receipt/board UI 확장부터 하기
- origin graph 를 갑자기 무겁게 확장하기

즉 지금은 intake 정리 턴이지, 거대 intake platform 턴이 아니다.

---

## 9. Recommended Next Move
가장 자연스러운 다음 한 걸음은 아래 둘 중 하나다.

1. `input label minimum contract v1`
2. `current preferred segmentation path note v1`

이 둘이 있으면 입력기 코어가 훨씬 선명해진다.

---

## 10. One-Line Conclusion
현재 입력기 보강의 핵심은 새 intake 엔진을 더 만드는 것이 아니라, 이미 있는 `routing / segmenter / anchorizer / source locator / observer ingest surface` 를 하나의 현재 구조로 더 명확히 묶는 것이다.
