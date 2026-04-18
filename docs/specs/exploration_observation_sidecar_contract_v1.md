# exploration_observation_sidecar_contract_v1

## purpose

이 문서는 `runtime/observer/exploration/` 아래에 남기는
exploration sidecar의 최소 canonical contract를 잠그기 위한 spec이다.

이 contract의 목적은
탐색 결과를 코어 판단으로 과장하지 않으면서도,
반복 가능한 json/md 쌍으로 남겨 later reread와 selective adoption을 가능하게 하는 것이다.

## verdict

- `runtime/observer/exploration/`는 유효한 canonical sidecar lane이다
- 기본 산출 단위는 `json + md` 쌍이다
- 이 lane은 observation readout을 소유하지만 governance decision을 소유하지 않는다
- 이 spec은 heavy ontology나 global relation engine을 요구하지 않는다

## folder placement

canonical path는 아래다.

- json:
  - `runtime/observer/exploration/json/<observation_id>.json`
- md:
  - `runtime/observer/exploration/md/<observation_id>.md`

현재 lane은 아래 둘을 모두 가져야 한다.

- machine-readable sidecar
- operator-readable readout

## ownership

### this lane owns

- exploration observation readout
- candidate slot listing
- keep/defer/outer classification readout
- bounded future-use hint
- next action hint
- observation-scoped notes

### this lane does not own

- core promotion verdict
- operating state promotion
- runtime heuristic mutation
- global ontology locking
- direct implementation mandate

즉 이 lane은
`what was seen and how it is temporarily held`
를 기록하지만,
`what must now be adopted`
를 결정하지는 않는다.

## minimal json fields

json sidecar는 최소 아래 필드를 가진다.

- `schema`
- `exploration_id`
- `observed_at`
- `source_ref`
- `source_type`
- `observation_type`
- `candidate_slots`
- `kept_as_core_candidate`
- `kept_as_outer_candidate`
- `deferred_items`
- `deferred_reason`
- `future_use_hint`
- `next_action_hint`
- `notes`

## optional json fields

필요할 때만 아래 필드를 붙일 수 있다.

- `session_id`
- `run_id`
- `related_receipts`
- `related_reports`
- `record_target`
- `relation_kind`
- `relation_reason`
- `hold_reason`
- `separation_reason`
- `not_adopted_reason`
- `borrowable_structure`
- `user_language_summary`

원칙:

- optional field는 observation 밀도를 높일 때만 붙인다
- 빈칸을 억지로 채우지 않는다
- 없는 판단을 있는 것처럼 만들지 않는다

## markdown companion contract

md readout는 아래 3개 section을 기본으로 가진다.

1. `context`
2. `readout`
3. `next`

### context

반드시 포함:

- `exploration_id`
- `observed_at`
- `source_ref`
- `source_type`
- `observation_type`

선택 포함:

- `session_id`
- `run_id`

### readout

반드시 포함:

- `candidate_slots`
- `kept_as_core_candidate`
- `kept_as_outer_candidate`
- `deferred_items`
- `deferred_reason`

### next

반드시 포함:

- `future_use_hint`
- `next_action_hint`
- `notes`

## observation types

현재 허용되는 얇은 분류 예시는 아래다.

- `pattern_seen`
- `external_case_first_pass`
- `comparison_observation`
- `defer_readout`
- `candidate_split_readout`

원칙:

- observation type은 작은 읽기 범주여야 한다
- 새로운 type이 필요해도 taxonomy를 과하게 늘리지 않는다

## interpretation rules

### keep vs outer vs defer

- `kept_as_core_candidate`
  - 현재 코어 논의에 올려둘 가치가 있는 observation slot
- `kept_as_outer_candidate`
  - 외곽 구조나 later attachment로는 유효한 slot
- `deferred_items`
  - 지금 당장 올리거나 구현하지 않는 slot

중요:

- 이것은 promotion verdict가 아니다
- 단지 observation readout의 bounded holding pattern이다

### future use hint

- future use hint는 가능성 메모다
- adopt 명령이나 implementation promise가 아니다

### next action hint

- 다음 reread 또는 bounded validation을 제안할 수 있다
- 직접적인 core patch opening을 강제하지 않는다

## naming rule

권장 naming은 아래 중 하나다.

- `explore_<timestamp>_<short_slug>`
- `external_case_first_pass_<case_name>_v1`
- `<bounded_probe_name>_<case_name>_v1`

원칙:

- json과 md는 같은 observation id를 공유한다
- one observation, one pair를 유지한다

## relation to other layers

### relation to `docs/reports`

- `docs/reports`는 더 넓은 해석 문서다
- exploration sidecar는 그보다 얇은 observation packet이다

### relation to `runtime/contracts`

- exploration sidecar는 관찰 readout이고
- `runtime/contracts`는 promotion/refinement 판단 표면이 될 수 있다

### relation to `app/`

- 이 lane은 code owner가 아니다
- sidecar 결과가 runtime code ownership을 먹으면 안 된다

## non-goals

- no global relation engine
- no ontology freeze
- no automatic promotion
- no deep scoring layer
- no mandatory UI layer

## close-out

한 줄로 잠그면:

`runtime/observer/exploration/`는
탐색 결과를 과장 없이 붙잡는 json/md 쌍의 bounded observation lane이다.

