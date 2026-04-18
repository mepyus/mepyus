# Governance Surface Summary v0

이 문서는 현재 저장소에 분산된 제동/감독 요소를 한 장으로 읽기 위한 요약면이다.  
새 governance 체계를 발명하지 않고, 이미 작동 중인 제동 지점만 압축한다.

즉 이 문서는 중앙 통제 모듈 다이어그램이 아니라, 현재 저장소에 흩어진 분산 surface 결합과 distributed stop points의 압축 지도다.

## 1. current layer baseline

- 핵심 위치:
  - [current_layer_baseline_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/current_layer_baseline_contract_v1.md)
- 무엇을 잠그는가:
  - 현재 레이어는 빠른 정답 확정층이 아니다
  - `mixed hold`는 실패 더미가 아니라 productive hold corridor다
  - stable closure 없는 상태에서 canonical 승격 논의 금지
  - observer split은 가능하지만 코어 truth로 조기 승격 금지
- 어디서 멈추는가:
  - `bridge 있음 + stable closure 없음`에서 mixed/confirmed_hold로 멈춘다

## 2. current_phase

- 핵심 위치:
  - [current_phase.json](/Users/sungsookim/universe/vectorfl_replica/runtime/current_phase.json)
- 무엇을 보여주는가:
  - 현재 reading frame
  - active latent lines
  - signals
  - decision
  - decision reason
  - next check trigger
- 어디서 멈추는가:
  - 현재 어떤 line/frame으로 읽는지, 다음 check 전에 무엇을 유지할지 여기서 잠긴다
- note:
  - `current_phase` 와 `preflight` 는 boundary 문서의 `현재 읽기면(current-reading surface)` 보호와 같은 현실을 가리킨다

## 3. preflight decision

- 핵심 위치:
  - [preflight_last_decision.json](/Users/sungsookim/universe/vectorfl_replica/runtime/preflight_last_decision.json)
- 무엇을 보여주는가:
  - preflight 직전/직후의 판단 요약
  - thickening / hold / next action 근거
- 어디서 멈추는가:
  - 실제 run 전에 현재 전환/closure 상태를 다시 확인하는 제동점으로 작동한다
- note:
  - current_phase와 함께 단일 중앙 모듈이 아니라 현재면 보호를 담당하는 분산 surface 결합으로 읽는다

## 4. promotion 금지

- 핵심 위치:
  - [current_layer_baseline_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/current_layer_baseline_contract_v1.md)
  - [line_promotion_log.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/logs/line_promotion_log.jsonl)
- 무엇을 금지하는가:
  - stable closure 없는 승격
  - re-entry만으로 canonical 확정
  - observer 결과를 core truth로 오인하는 것
- 어디서 멈추는가:
  - line이 보이더라도 승격 논의는 stable closure 증거 전까지 중지된다

## 5. observer-only / mixed hold

- 핵심 위치:
  - [current_layer_baseline_contract_v1.md](/Users/sungsookim/universe/vectorfl_replica/app/work/current_layer_baseline/current_layer_baseline_contract_v1.md)
  - [current_phase.json](/Users/sungsookim/universe/vectorfl_replica/runtime/current_phase.json)
- 무엇을 뜻하는가:
  - mixed는 버릴 대상이 아니라 re-entry 가능한 hold corridor다
  - specificity나 split candidate가 보여도 observer layer에서 유지할 수 있다
- 어디서 멈추는가:
  - 현재는 closure 도달 여부가 경계이며, observer insight가 바로 core rewrite로 넘어가지 않는다

## 6. append guard

- 핵심 위치:
  - [event_append_guard.py](/Users/sungsookim/universe/vectorfl_replica/app/core/events/event_append_guard.py)
  - [engine_event_ledger.jsonl](/Users/sungsookim/universe/vectorfl_replica/runtime/events/engine_event_ledger.jsonl)
- 무엇을 보호하는가:
  - append-only event ledger
  - tail recovery / locked append / 손상된 tail 복구
- 어디서 멈추는가:
  - runtime event 기록은 임의 overwrite가 아니라 guarded append를 통해서만 누적된다

## 6A. distributed governance note

- current layer baseline
- current_phase
- preflight decision
- promotion 금지
- observer-only / mixed hold
- append guard

위 요소들은 하나의 중앙 governance module이 아니라, 서로 다른 문서와 surface에 걸쳐 있는 distributed stop points로 작동한다.

## 7. governance가 다루는 단위

현재 governance surface는 line만 다루지 않는다. 함께 다루는 단위는 다음과 같다.

- fragment / source material
- event
- hint
- phase decision
- surface
- residue
- trace

즉 governance는 line 승격만 통제하는 것이 아니라, 입력 이후의 관찰/판단/기록/보존 리듬 전체를 제동한다.

## 8. one-page stop map

이 stop map은 중앙 통제 모듈의 흐름도보다, 현재 저장소에 흩어진 분산된 stop points를 한 장으로 압축한 지도다.

- 입력이 들어와도 ambiguity가 크면 direct flattening 대신 preprocess/observer로 기운다.
- line이 보여도 stable closure가 없으면 mixed hold에서 멈춘다.
- observer split이 보여도 core truth 승격 전에 observer-only에 머문다.
- current_phase와 preflight는 다음 hop 전의 판단을 잠근다.
- event/history는 append guard 아래에서만 남는다.

## 9. summary judgment

현재 저장소의 governance surface는 하나의 중앙 통제 모듈보다, `baseline contract + current phase profile + preflight decision + promotion 금지 규칙 + observer-only mixed hold + append guard`의 분산 결합으로 존재한다.  
즉 이미 강하게 존재하지만, 단일 대시보드보다 여러 보호면에 나뉘어 잠겨 있는 governance다.
