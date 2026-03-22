# lifecycle pruning draft

## 1. current diagnosis
- 현재 엔진은 weak trace, blocked path, proposal trace, review vector를 적극 보존한다
- 이 철학은 맞지만, 모두를 같은 온도의 계층에 두면 나중에 hot path 가 과포화될 위험이 있다
- 현재 부족한 것은 `무엇을 남길까`가 아니라 `어떤 층에 남길까`에 대한 lifecycle 설계다

## 2. storage layer proposal

### hot
- 의미:
  - 현재 active review / current possibility / current candidate
  - 새 input 과 바로 상호작용하는 계층
- 조회 특성:
  - 빠른 조회
  - 작은 payload
  - 현재 상태 중심

### warm
- 의미:
  - 지금은 비활성이지만 다시 올릴 가치가 있는 요약 상태
  - condensed review history
  - strongest evidence
  - last seen state
- 조회 특성:
  - 중간 빈도의 재검토
  - history 요약 유지

### cold
- 의미:
  - raw proposal trace
  - full blocker history
  - token pair 로그
  - process log
  - 장기 분석용 데이터
- 조회 특성:
  - 느려도 됨
  - 분석 / 감사용

## 3. current payload mapping

### hot candidate
- current gate vector
- current blockers
- current best_local_ref
- current ready families
- current direct overlap candidate families
- current space_entry_state
- current review_state

### warm candidate
- condensed proposal summary
- support counts
- strongest proposal tokens
- threshold review vector
- cross-path family count
- last_seen state
- last meaningful blocker

### cold candidate
- raw proposal trace
- token pair alignment logs
- family canonicalization history
- blocker history
- process log
- full review payload snapshots

## 4. lifecycle questions
- 몇 번 연속 재평가했는데 상태 변화가 없으면 hot 에서 warm 으로 내릴 것인가
- `translation_missing` 가 장기 유지되면 cold 로 내릴 것인가
- `space pre-entry` 후보는 어떤 event 가 생기면 hot 으로 다시 승격할 것인가
- canonical 되지 못한 proposal trace 는 어떤 간격으로 condensed 요약을 만들 것인가
- warm 에서 cold 로 갈 때 어떤 필드만 유지할 것인가

## 5. suggested minimal retention fields

### hot
- `bridge_mode`
- `review_state`
- `translation_gate`
- `processing_gate`
- `observer_gate`
- `best_local_ref`
- `direct_overlap_candidate_families`
- `space_entry_state`
- `next_review_blocker`

### warm
- `last_seen`
- `support_density_class`
- `cross_path_overlap_family_count`
- `cross_path_overlap_quality_class`
- `canonicalizable_token_pair_count`
- `strongest proposal families`
- `stable blocker summary`

### cold
- `full promotion_review payload`
- `proposal trace`
- `token pair history`
- `blocker history`
- `process log`

## 6. pruning principle
- pruning 은 삭제보다 `temperature downshift` 로 먼저 본다
- 즉 대부분은
  - hot -> warm
  - warm -> cold
로 내리고
- hard delete 는 마지막 단계에서만 고려한다

## 7. what not changed
- 실제 cold storage 구현 안 함
- DB schema 변경 안 함
- TTL 자동화 안 함
- pruning job 안 만듦

## 8. next recommendation
- 다음 실제 코드화는 storage 구현보다 `temperature tag` 부터 시작하는 것이 낫다
- 예:
  - `trace_temperature = hot|warm|cold`
  - `last_reviewed_at`
  - `last_state_change_at`

## 9. final sentence
- 이 엔진은 weak trace 를 버리는 엔진이 아니라, 온도를 낮추며 보존하는 엔진으로 가야 한다
- 따라서 pruning 의 본질은 삭제보다 `lifecycle tiering` 이다
