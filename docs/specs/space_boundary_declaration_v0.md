# Space Boundary Declaration v0

이 문서는 현재 저장소에서 관찰된 공간 경계를 짧게 잠그는 선언문이다.  
이 boundary는 완전 분리된 층도가 아니라, 실제 운용에서 일부가 겹쳐 보이는 중첩 boundary reading이다.  
새 아키텍처를 정의하지 않고, 현재 운영면에 이미 드러난 층만 압축한다.

## 1. baseline layer

- 역할: 현재 공간의 해석 기준선과 금지 규칙을 잠그는 층
- 성격: 직접 덮어쓰기보다 기준 유지 우선
- note: operating layer, governance surface와 실제 운용에서는 일부 겹쳐 보인다
- 포함 예:
  - [CURRENT.md](/Users/sungsookim/universe/vectorfl_replica/CURRENT.md)
  - [vectorfl_status.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_status.md)
  - [current_layer_baseline_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/current_layer_baseline_contract_v1.md)

## 2. operating layer

- 역할: 입력, 구조화, 비교, reread, route selection, surface construction이 실제로 일어나는 층
- 성격: 분산되어 있으나 현재 공간의 실작동면을 이룸
- note: baseline, ledger, current-reading surface와 분리돼 있으면서도 실제 운용에서는 서로 접속한다
- 포함 예:
  - [app/core](/Users/sungsookim/universe/vectorfl_replica/app/core)
  - [app/runtime](/Users/sungsookim/universe/vectorfl_replica/app/runtime)
  - [scripts](/Users/sungsookim/universe/vectorfl_replica/scripts)
  - [app/work/observer_ingest_min](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min)
  - [app/work/external_input_preprocess](/Users/sungsookim/universe/vectorfl_replica/app/work/external_input_preprocess)

## 3. ledger layer

- 역할: 과거 사실, provenance, event, line history, log를 append-only로 보존하는 층
- 성격: overwrite보다 append 우선
- 원칙:
  - append-only ledger는 rewrite하지 않는다
  - 과거 경로/사실도 기록 일부로 본다
- 포함 예:
  - [runtime/events](/Users/sungsookim/universe/vectorfl_replica/runtime/events)
  - [runtime/logs](/Users/sungsookim/universe/vectorfl_replica/runtime/logs)
  - [runtime/manifests/origin_maps](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/origin_maps)
  - [line_registry.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/line_registry.json)

## 4. active surface

- 역할: 현재 상태와 읽기 결과를 바로 읽게 하는 현재 읽기면(current-reading surface)
- 성격: 현재 구조를 반영해야 하며 refresh 가능
- note: 표면구성기가 만들어 내는 면이자, governance가 보호하는 현재면이다
- 포함 예:
  - [runtime/current_phase.json](/Users/sungsookim/universe/vectorfl_replica/runtime/current_phase.json)
  - [runtime/preflight_last_decision.json](/Users/sungsookim/universe/vectorfl_replica/runtime/preflight_last_decision.json)
  - [runtime/breadcrumbs.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/breadcrumbs.jsonl)
  - [runtime/views](/Users/sungsookim/universe/vectorfl_replica/runtime/views)
  - [observer_ingest_min/generated](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/generated)

## 5. replayable residue

- 역할: 재생성 가능하지만 현재 읽기나 비교에 당장은 유용한 잔여층
- 성격: 유지 가능하지만 축약/대표본화 대상
- note: active surface와 겹쳐 보일 수 있으나, 현재면보다 대표본화 가능성이 더 큰 층이다
- 포함 예:
  - 일부 generated split units
  - 반복 probe / 반복 validation output
  - flow candidate observation trace류

## 6. reference layer

- 역할: 외부 자료와 외부 레퍼런스를 보관하는 바깥 비교층
- 성격: 먼저 그 자료 자체로 읽고, 마지막에만 우리 공간으로 번역
- 포함 예:
  - [references](/Users/sungsookim/universe/vectorfl_replica/references)
  - [reference_reading_order_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/reviews/reference_reading_order_v0.md)

## 7. protection clauses

- baseline layer는 직접 덮어쓰기보다 기준 유지 우선이다.
- ledger layer는 append-only 우선이며, 사실 기록을 임의로 재서술하지 않는다.
- active surface는 현재 읽기 frame과 next hop을 담는 보호 대상이다.
- `mixed hold`, `observer-only`, `promotion 금지`가 걸린 hold profile은 보호 성격으로 읽는다.
- reference layer는 곧바로 VectorFL ontology로 평탄화하지 않는다.

## 8. boundary note

현재 공간의 경계는 완전히 깔끔한 층분리가 아니라, `baseline / operating / ledger / current-reading surface / residue / reference`가 중첩된 형태로 드러난다.  
따라서 이 선언은 완전한 분리도보다 `현재 잠글 수 있는 경계 읽기`로 이해해야 한다.
