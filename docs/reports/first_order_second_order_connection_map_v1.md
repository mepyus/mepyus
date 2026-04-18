# first_order_second_order_connection_map_v1

## 1. Purpose

이 문서는 현재 `vectorfl_replica` 안에서
`1차 입력 구조`, `1.5차 probe bridge`, `2차 숙성 구조`, `운용 표면`
이 실제로 어떻게 이어져 있는지 한 장으로 정리한 연결도다.

핵심 목적:
- 지금 폴더 전체에 녹아 있는 철학과 실제 코드 구조를 같이 본다.
- 1차와 2차가 어디서 만나는지, 어디서 아직 평행하게 남아 있는지 본다.
- 최근 second-order 자산을 실패 목록이 아니라 기억/숙성 자산으로 다시 읽을 수 있게 한다.

---

## 2. One-Line Reading

현재 구조는 철학적으로는 `입력 -> 흔적 보존 -> 재독해 -> 숙성` 흐름에 맞게 가고 있다.
다만 구현상으로는 아직
`runtime memory graph 위 직접 재순환`
보다
`generated sidecar 위 재순환`
이 더 강하고,
일부 2차 기관은 아직 `youtube_03_22` scaffold를 끌고 있다.

---

## 3. Top-Level Map

### A. first-order input structure
원문 / 외부 자료 / 내부 문서
-> routing / intake
-> dust / fragment 생성
-> scene / flow / anchor / label 같은 1차 센서값 생성
-> trace / material / runtime downstream 저장

### B. 1.5-order probe bridge
1차 센서값
-> probe script가 다시 수집
-> object candidate / layer hint / relation hint / top windows / residue draft 생성

### C. second-order maturation structure
probe output
-> purpose synthesis
-> question-inducing review
-> multi-pass rereading
-> context unit candidate
-> paragraph role probe

### D. operating / memory surfaces
generated json / reports / receipts / latest boards / logs
-> 비교
-> hold
-> blocker
-> next loop gate
-> future rereading memory

즉 지금 구조는
`원문 -> 1차 흔적 -> probe bridge -> 2차 재독해 -> 기억 자산 표면`
으로 읽는 것이 정확하다.

그리고 이 표면은 결과 graph보다 먼저
운영자가 원문-값-연결-보류 상태를 따라가는 **운용면 / 과정면** 으로 읽어야 한다.

---

## 4. First-Order Core

### A. raw-to-dust ingress
핵심 파일:
- [inputter.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/inputter.py)
- [live_input.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input.py)

역할:
- source를 읽고
- source type에 따라 dust input을 만들고
- 1차 판독 대상 단위로 자른다.

철학적 위치:
- 1차는 정답 생성이 아니라 씨앗 흔적 보존층이다.
- 따라서 여기서 중요한 것은 이미 완성된 해석이 아니라
  미래 재독해를 버틸 수 있는 흔적을 남기는 일이다.

### B. first-order sensing
핵심 파일:
- [labeler.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/labeler.py)
- [dust_field.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/dust_field.py)

역할:
- dust input에 scene / flow / D-I-S / anchor 등을 붙인다.
- 1차 센서값을 만든다.

현재 읽기:
- 여기서 나오는 값은 ontology truth가 아니라 sensor reading이다.
- 동시에 later rereading을 위한 보존 흔적이다.

### C. persistence and first memory
핵심 파일:
- [live_input.py](/Users/sungsookim/universe/vectorfl_replica/app/core/runtime/live_input.py)

역할:
- labeled dust를 runtime downstream에 붙인다.
- material metadata, trace, pressure, seed, relation candidate 등으로 흘려 보낸다.

현재 읽기:
- 1차 출력값은 이미 기억을 가진 요소들이다.
- 따라서 2차는 이 값을 버리는 게 아니라 다시 만나게 해야 한다.

---

## 5. Routing Front Door vs First-Order Core

### A. routing front door
핵심 파일:
- [process_structured_doc_with_routing.py](/Users/sungsookim/universe/vectorfl_replica/scripts/process_structured_doc_with_routing.py)
- [engine_input_lane_baseline_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/policies/engine_input_lane_baseline_v1.md)

역할:
- declaration / baseline / directive / external_input 같은 lane 분기
- registry / ticket / provenance / receipt 연결
- structured doc intake wrapper

판정:
- 이것은 input front door다.
- 하지만 2차 숙성 루프와 직접 이어진 재순환 기관은 아니다.

### B. current connection status
현재는
- routing front door
- 1차 코어
- 2차 숙성 계층
이 철학적으로는 같은 구조 아래 있지만,
실행 경로는 아직 완전히 하나로 접히지 않았다.

즉:
- front door는 front door
- 1차 코어는 1차 코어
- 2차는 sidecar generated rereading 계층
으로 남아 있다.

---

## 6. The 1.5-Order Bridge

핵심 파일:
- [run_dialogue_asset_probe.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_dialogue_asset_probe.py)

이 스크립트의 위치는 중요하다.

이건 단순 실험 스크립트가 아니라
현재 구조에서 사실상
`1차 -> 2차`
를 이어 주는 bridge다.

역할:
- build_dust_inputs_from_source
- label_dust_inputs
- probe packet 생성
- overall object / layer / relation / question-intent / residue 초안 생성

즉 지금 구조에서 1차와 2차의 실제 만남은
`runtime memory graph 직접 연결`
보다는
이 probe bridge를 통한 `generated packet`
형태로 발생한다.

현재 판정:
- 철학적으로는 `re-readable memory packet bridge` 로 읽는 것이 맞다.
- 구현상으론 아직 generated sidecar 의존이 강하다.
- 문제는 bridge 존재 자체가 아니라, packet 안에 asset-specific scaffold가 섞인다는 점이다.

---

## 7. Second-Order Maturation Layer

### A. purpose synthesis
파일:
- [run_dialogue_asset_purpose_synthesis.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_dialogue_asset_purpose_synthesis.py)

역할:
- 1.5차 probe를 다시 읽어
- object opening / layer opening / relation movement / era question을 synthesis한다.

현재 상태:
- 2차 재독해 기관으로 성립했다.
- 다만 아직 dialogue/AI-specific wording carryover가 남아 있어 새 층위를 여는 대신 기존 phrasing로 재기술할 위험이 있다.

### B. question-inducing block review
파일:
- [run_question_inducing_block_review.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_question_inducing_block_review.py)

역할:
- 질문 유도력이 강한 block/window를 찾는다.
- residue를 summary-stage priority 문제로 다시 읽는다.

현재 상태:
- 좋은 응축핵 후보 추출기다.
- 하지만 cross-domain에선 candidate absence가 반복된다.

### C. multi-pass rereading and context unit reconstruction
파일:
- [run_multi_pass_interpretation_training.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_multi_pass_interpretation_training.py)

역할:
- 같은 자산을 다른 해석 레이어로 다시 읽는다.
- context unit 후보를 세운다.

현재 상태:
- 철학적으로는 사용자 사고 방식을 학습하는 핵심 기관이다.
- 그러나 코드상으론 아직
  `agent_interface_transition_unit`,
  `future_of_work_supervisor_unit`,
  `model_eval_shift_unit`
  같은 hardcoded scaffold가 남아 있다.

즉:
- 재독해 태도는 살아 있다.
- context unit institution은 아직 scaffold-bound 하다.
- 더 정확히는, 새 맥락 단위를 여는 대신 기존 unit을 다시 덮어씌우는 조기 고정점이 남아 있다.

### D. paragraph role probe
파일:
- [run_paragraph_role_interpretation_training.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_paragraph_role_interpretation_training.py)

역할:
- local / page / comparison 맥락에서 paragraph role을 다시 읽는다.

현재 상태:
- role-like reading의 가능성은 보여 준다.
- 그러나 `Bundle-Unbundle`, `GTC`, `RLVR` 중심 scaffold carryover가 강하다.
- 그래서 아직 generalized role institution이 아니라 weak probe다.
- 이건 단순 role failure가 아니라 열린 role rereading을 조기 고정시키는 흔적으로 읽는 편이 정확하다.

---

## 8. Where Philosophy Matches the Code

현재 구조에서 철학과 잘 맞는 부분:

### A. 1차와 2차를 분리해서 본다
- 1차는 센서값
- 2차는 재독해 / 보정 / 축적

이건 코드와 문서 모두에 분명히 반영돼 있다.

### B. weak / fallback / hold를 버리지 않는다
- recent second-order reports는 failure list가 아니라 memory asset으로 재배치돼 있다.
- hold는 rejection이 아니라 deferred openness로 읽힌다.

### C. 반복은 스크립트가 맡고, 구조 판정은 운영자가 한다
- segmentation / pointer / heading 실험
- gated validation
- blocker integration

이 흐름은 “토큰 대신 loop/script로 숙성한다”는 운영 철학과 맞다.

---

## 9. Where the Structure Still Misses the Philosophy

### A. sidecar-first rereading
이상적인 철학:
- runtime memory 위 재순환

현재 구현:
- generated json sidecar 위 재순환

즉 기억은 살아 있지만,
직접적인 runtime memory graph re-entry는 아직 약하다.

### B. discovered layers보다 pre-shaped reading이 더 강한 구간
현재 일부 2차 스크립트는
새 층위를 발견하기보다
이미 강하게 형성된 dialogue scaffold에 다시 끌리는 경향이 있다.

즉:
- 사용자는 새 의미면이 열리길 원한다.
- 현재 일부 코드는 기존 unit/role/target을 재사용하는 쪽이 더 강하다.

### C. SSOT ambiguity in runtime lane
현재 `app/core/runtime/*`와 `app/runtime/*`가 같이 존재하고
서로 import한다.

이건 당장 파손은 아니지만,
1차 코어의 단일 중심을 흐릴 수 있다.

---

## 10. Current Correct Reading

현재 폴더 전체를 정확히 읽으면:

- 우리는 이미 1차와 2차를 분리한 엔진을 만들고 있다.
- 1차는 입력 구조와 흔적 보존층으로 성립했다.
- 2차는 재독해/숙성 계층으로 성립했다.
- recent blocker / gate / hold 자산은 실패물이 아니라 기억 자산이다.
- 다만 1차와 2차의 연결은 아직 `direct runtime memory recirculation`보다
  `probe/generated bridge recirculation`에 더 가깝다.
- 그리고 2차 일부 기관은 아직 특정 AI dialogue scaffold에 묶여 있다.

즉 지금은 철학이 잘못된 상태가 아니라,
철학을 더 정확히 구현하기 위해
운용화면 / memory packet / scaffold 조기 고정 지점을 더 선명히 봐야 하는 단계다.

---

## 11. What This Means for the Engine

현재 엔진을 한 문장으로 다시 정의하면:

> 현재 엔진은 1차에서 입력 흔적을 기억으로 남기고, 1.5차 probe bridge를 통해 2차 재독해 계층으로 올려 숙성시키는 구조까지 왔지만, 아직 그 재순환은 runtime memory 직접 재진입보다 generated sidecar와 scaffolded rereading에 더 의존하는 과도기형 숙성 엔진이다.

---

## 12. One-Line Conclusion

현재 `vectorfl_replica`는 네 철학대로 `입력 구조`와 `내부 숙성 구조`를 분리해 놓았고 둘 사이 bridge도 만들었지만, 2차 일부 기관은 아직 scaffold-bound 하며 1차와 2차의 실제 연결은 runtime memory direct loop보다 generated probe bridge 중심으로 작동하고 있다.
