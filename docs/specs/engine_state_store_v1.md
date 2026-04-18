[[A]] [[OBJ:engine_state_store_v1]] [[SEM:append_only_store_for_canonical_engine_operating_state_records]]

# engine_state_store_v1

## 1. purpose

- 이 store의 목적은 `engine_state_schema_v1` record를 자산 단위로 저장/조회/최신화하는 것이다.
- 여기서 store는 상위 의미 객체 저장소가 아니라 process-console operating state 저장면이다.

## 2. role

- asset_id 기준 latest state 조회
- asset_id 기준 append-only history 보존
- latest surface 생성
- schema_version 보존
- canonical / experimental 분리 보존

## 3. history vs latest

- history:
  - append-only
  - 상태 변화 기록을 잃지 않는다
  - later rereading / operator audit / state drift review에 사용된다

- latest:
  - 파생 surface
  - process console header / asset rail / state panel / compare entry가 직접 읽는다
  - history에서 재생성 가능해야 한다

## 4. storage layout

- history:
  - `runtime/state/engine_state_history/<asset_id>.jsonl`
- latest:
  - `runtime/views/engine_state_latest/<asset_id>.json`
  - `runtime/views/engine_state_latest/index.json`

## 5. append-only rule

- `append_state(record)`는 history에 먼저 append한다.
- latest는 append된 record를 기준으로 갱신한다.
- latest는 authoritative write target이 아니라 surface projection이다.

## 6. canonical vs experimental separation

- canonical top-level field:
  - `packet_texture`
  - `grounding_status`
  - `emergence_status`
  - `carryover_risk`
  - `maturation_state`
  - `traceability_status`
  - `comparison_memory_reason`
  - `gate_blocker_summary`

- experimental namespace only:
  - context unit names
  - paragraph role names
  - pivot/compression labels
  - high-level object naming

- guard:
  - 위 naming 계열이 top-level에 들어오면 sanitize 해서 `experimental_namespace` 아래로 내린다.

## 7. process-console connection

- latest surface는 아래 컴포넌트의 공통 data source가 된다.
  - header badge
  - asset rail
  - state panel
  - compare entry
  - latest state summary

## 8. schema version

- 현재 schema_version:
  - `engine_state_schema_v1`
- 이 값은 history / latest record 모두에 포함된다.
- 이후 enum이 변하거나 field가 바뀌면 version을 올리고 migration 여부를 별도 판단한다.

## 9. update policy linkage

- lifecycle rule은
  [engine_state_update_policy_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/specs/engine_state_update_policy_v1.md)
  를 따른다.
- store는 그 policy를 집행하는 저장면이고,
  - append-first
  - latest-is-derived
  - canonical contamination guard
  - evidence-backed state update
  를 코드에서 보장한다.

## 10. one-line lock

> `engine_state_store_v1`는 상위 해석 객체 저장소가 아니라, process-console 자산의 canonical operating state를 append-only history와 latest surface로 함께 보존하는 저장면이다.
