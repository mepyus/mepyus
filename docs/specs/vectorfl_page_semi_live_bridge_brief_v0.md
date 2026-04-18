# VectorFL Page Semi-Live Bridge Brief v0

이 문서는 현재 저장소에 이미 존재하는 runtime 자산을  
`VectorFL Page shell`에 부분적으로 연결하는 semi-live bridge 기준을 잠근다.

목적은 full live integration 이전에,
`current_phase`, `preflight_last_decision`, `engine_state_latest` 같은
실제 runtime surface를 현재 shell 의미체계 안으로 안전하게 끌어오는 것이다.

## 1. Core Sentence

Semi-live bridge는  
mock shell의 의미 구조를 유지한 채,
실제 runtime surface에서 가져올 수 있는 정보만 보수적으로 덮어써서
`current-reading`, `queue`, `governance carry`, `trace hint`를 더 현재 상태에 가깝게 만드는 단계다.

## 2. Allowed Runtime Sources

- `runtime/current_phase.json`
- `runtime/preflight_last_decision.json`
- `runtime/views/engine_state_latest/index.json`

## 3. Allowed Overrides

- current-reading headline/body의 일부
- governance reason / next check / drift risk 요약
- queue row preview
- trace/history preview 일부
- intake/source note 일부

## 4. What Must Not Drift

- runtime source가 곧 canonical ontology처럼 보이는 것
- current-reading body가 raw runtime dump가 되는 것
- trace가 generic log feed로 drift하는 것
- programs/connections가 live control dashboard처럼 보이는 것

## 5. Final Lock Sentence

현재 기준은 다음 문장으로 잠근다.

`VectorFL Page의 semi-live bridge는 current_phase, preflight_last_decision, engine_state_latest를 보수적으로 번역해 shell의 current-reading/queue/governance/trace를 현재 상태에 더 가깝게 만들되, shell의 의미 구조를 runtime raw surface에 종속시키지 않아야 한다.`
