[[A]] [[OBJ:engine_state_schema_v1]] [[SEM:canonical_operating_state_schema_for_process_console_assets]]

# engine_state_schema_v1

## 1. purpose

- 이번 스키마의 목적은 최근 process-trace / memory packet / second-order 자산에서 나온 값을
  object promotion이 아니라 **engine operating state** 로 먼저 고정하는 것이다.
- 즉 이 스키마는
  - 무엇을 읽었는가
  보다
  - 지금 이 자산이 어떤 상태로 읽히고 있는가
  를 canonical field로 보존한다.

## 2. canonical field set

- 아래 8개를 canonical engine value로 채택한다.
  - `packet_texture`
  - `grounding_status`
  - `emergence_status`
  - `carryover_risk`
  - `maturation_state`
  - `traceability_status`
  - `comparison_memory_reason`
  - `gate_blocker_summary`

## 3. full record shape

- 최소 record field:
  - `asset_id`
  - `asset_name`
  - `source_type`
  - `schema_version`
  - `packet_texture`
  - `grounding_status`
  - `emergence_status`
  - `carryover_risk`
  - `maturation_state`
  - `traceability_status`
  - `comparison_memory_reason`
  - `gate_blocker_summary`
  - `state_notes`
  - `evidence_refs`
  - `updated_at`

- optional provenance metadata:
  - `update_trigger_type`
  - `update_reason`

## 4. allowed values

### A. `packet_texture`

- allowed:
  - `moderately_open`
  - `structured_open_low_emergence`
  - `overcompressed_closure_heavy`
  - `overcompressed_breathing`

- role:
  - 1.5차 memory packet의 질감 상태
  - 2차의 문제를 2차만의 문제로 과잉 해석하지 않게 하는 바닥 값

### B. `grounding_status`

- allowed:
  - `direct_grounded`
  - `partially_grounded`
  - `fallback_grounded`
  - `empty_ref_risk`

- role:
  - 현재 판독이 source에 얼마나 직접 닿아 있는지 표시

### C. `emergence_status`

- allowed:
  - `question_opening_present`
  - `minimal_emergence`
  - `low_emergence`
  - `no_emergence`

- role:
  - 2차 재독해에서 열린 움직임이 있었는지 표시

### D. `carryover_risk`

- allowed:
  - `low`
  - `medium`
  - `high`
  - `prepared_scaffold_carryover`

- role:
  - prepared scaffold / pre-shaped rereading 의존 위험도 표시

### E. `maturation_state`

- allowed:
  - `hold`
  - `residue`
  - `weak`
  - `fallback`
  - `blocked`
  - `breathing`

- role:
  - 현재 자산을 실패가 아니라 상태 기억으로 관리하는 핵심 field

### F. `traceability_status`

- allowed:
  - `traceable`
  - `partially_traceable`
  - `not_traceable`

- role:
  - process console 상에서
    `source -> 1차 -> 1.5차 -> 2차 -> 상태`
    흐름 추적 가능 여부 표시

### G. `comparison_memory_reason`

- allowed:
  - `same_compressed_family`
  - `same_fallback_dominance`
  - `breathing_contrast`
  - `similar_carryover_pattern`
  - `similar_grounding_failure_surface`

- role:
  - 자산 간 비교 기억 진입 키
  - ontology 값이 아니라 comparative navigation field

### H. `gate_blocker_summary`

- allowed:
  - `question_inducing_candidate_absence`
  - `fallback_grounding_dominance`
  - `weak_role_like_only`
  - `pivot_compression_non_recurrence`
  - `scaffold_carryover_risk`

- role:
  - 현재 병목을 구조적으로 관리하는 최소 blocker set

## 5. promotion guard

- 아래 값들은 이번 단계에서 canonical engine state field에 넣지 않는다.
  - context unit 이름
  - paragraph role 이름
  - pivot 확정 라벨
  - compression 확정 라벨
  - `business_power_shift` 같은 상위 의미 객체명
  - `orchestration` 같은 고차 해석 객체
  - scaffold carryover가 강한 naming 계열

- 이유:
  - 아직 weak/fallback probe 비중이 높다
  - prepared scaffold carryover 위험이 남아 있다
  - direct grounding과 반복 회복이 아직 충분히 안정되지 않았다

- 현재 위치:
  - `experimental_namespace`
  - comparison memory note
  - operator reading aid
  - future promotion candidate

## 6. UI connection

- 이 스키마는 아래 표면에서 바로 공통 사용 가능해야 한다.
  - badge
  - filter
  - sort
  - state panel
  - compare entry
  - process console header

## 7. source of truth

- code-level enums:
  - [states.py](/Users/sungsookim/universe/vectorfl_replica/app/core/states.py)
- immutable record:
  - [entities.py](/Users/sungsookim/universe/vectorfl_replica/app/core/models/entities.py)
- json schema:
  - [engine_state_schema_v1.json](/Users/sungsookim/universe/vectorfl_replica/app/core/schemas/engine_state_schema_v1.json)

## 8. one-line lock

> `engine_state_schema_v1`은 상위 의미 객체를 canonicalize하는 스키마가 아니라, process-console 자산이 지금 어떤 packet 질감 / grounding / emergence / carryover / maturation / traceability 상태에 있는지를 엔진이 직접 사용할 수 있게 고정하는 operating-state schema다.
