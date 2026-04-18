[[A]] [[OBJ:engine_state_runtime_update_bridge_v1]] [[SEM:bridge_spec_for_connecting_runtime_evidence_to_canonical_operating_state_lifecycle]]

# engine_state_runtime_update_bridge_v1

## 1. purpose

- 이번 bridge의 목적은 runtime evidence를 canonical operating state lifecycle에 연결하는 것이다.
- 이 bridge는 latest를 직접 overwrite하지 않고, runtime evidence를 patch/proposal로 normalize한 뒤 history append와 latest regeneration으로 연결한다.

## 2. bridge responsibilities

- runtime evidence 수집
- canonical patch/proposal 생성
- update policy 적용
- history append
- latest derived regeneration
- state update event surface 기록

## 3. accepted evidence families

- packet evidence
  - packet texture 판독
  - packet compression / opening note
  - bridge confidence / grouping correction
- rereading evidence
  - emergence 판독
  - question opening / relation movement 관련 상태 요약
  - blocker confirmation
  - carryover correction note
- grounding / traceability evidence
  - source ref coverage 증가/감소
  - empty-ref risk 확인
  - traceability chain 연결/단절 확인
- operator-approved correction
  - evidence와 correction reason이 명시된 경우만 허용

## 4. runtime update flow

1. runtime artifact 또는 evidence 발생
2. asset_id resolve
3. latest canonical state load
4. incoming evidence normalize
5. partial state patch/proposal 생성
6. `engine_state_update_policy_v1` 적용
7. valid proposal이면 history append
8. latest regenerate/write
9. state update event surface write
10. process console은 same latest path로 최신 상태를 읽음

## 5. code split

- bridge:
  - [engine_state_runtime_update_bridge.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/engine_state_runtime_update_bridge.py)
- patch builder:
  - [engine_state_update_patch_builder.py](/Users/sungsookim/universe/vectorfl_replica/app/runtime/engine_state_update_patch_builder.py)
- store:
  - [engine_state_store.py](/Users/sungsookim/universe/vectorfl_replica/app/core/state_store/engine_state_store.py)
- policy:
  - [engine_state_update_policy.py](/Users/sungsookim/universe/vectorfl_replica/app/core/state_store/engine_state_update_policy.py)

## 6. patch builder rules

- runtime evidence를 full record로 바로 쓰지 않는다.
- 먼저 `proposed_changes`만 가진 partial patch/proposal을 만든다.
- canonical 8필드와 `state_notes`만 직접 patch 대상으로 본다.
- naming-heavy / scaffold-heavy / high-level object 계열은 `experimental_namespace`로만 보낸다.
- `comparison_memory_reason`, `gate_blocker_summary`는 기본적으로 merge하고, 필요할 때만 replace-array mode를 사용한다.
- evidence refs는 previous latest와 merge해 latest evidence가 지나치게 얇아지지 않게 한다.

## 7. latest / history rule

- authoritative source는 history다.
- latest는 derived surface다.
- bridge는 history append 뒤에 latest를 regenerate한다.
- process console은 history를 직접 읽지 않고 계속 latest만 읽는다.

## 8. event surface

- bridge는 `runtime/views/engine_state_update_events/` 아래에 asset별 latest update event와 index를 남긴다.
- event surface 최소 정보:
  - `asset_id`
  - `update_trigger_type`
  - `update_reason`
  - `evidence_type`
  - `evidence_summary`
  - `changed_canonical_fields`
  - `evidence_refs`
  - `updated_at`

## 9. guard rules

- canonical 8필드 외 naming-heavy field는 top-level canonical patch에 올리지 않는다.
- runtime update는 evidence refs 없이는 canonical drift를 만들지 않는다.
- ambiguous한 경우 상향 승격보다 no-drift append 또는 note 보강을 우선한다.
- process console은 experimental namespace를 기본 숨김으로 유지한다.

## 10. one-line lock

> `engine_state_runtime_update_bridge_v1`는 runtime evidence를 canonical state patch로 normalize해 policy를 통과시킨 뒤 history append와 latest regeneration으로 연결하고, process console이 같은 latest path를 통해 자연스럽게 새 상태를 읽게 만드는 bridge 규정이다.
