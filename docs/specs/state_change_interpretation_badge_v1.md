[[A]] [[OBJ:state_change_interpretation_badge_v1]] [[SEM:derived_badge_layer_for_fast_state_change_reading]]

# state_change_interpretation_badge_v1

## 1. purpose

- 이번 badge layer의 목적은 diff/history 결과를 운영자가 더 빨리 읽게 하는 얇은 derived reading aid를 제공하는 것이다.
- badge는 canonical truth가 아니라 변화 읽기 가속 장치다.

## 2. inputs

- `changed_fields`
- `diff_class`
- `update_trigger_type`
- `provenance_only`
- `added/removed blockers`
- `added/removed comparison memory reasons`

## 3. primary badge set

- `provenance_only`
- `canonical_change`
- `packet_texture_shift`
- `grounding_shift`
- `emergence_shift`
- `carryover_shift`
- `maturation_shift`
- `traceability_shift`
- `blocker_shift`
- `comparison_memory_shift`
- `mixed_shift`
- `no_previous_state`

## 4. secondary badge set

- `runtime_update`
- `backfill_origin`
- `recompute`
- `manual_correction`

## 5. generation rules

- `provenance_only`
  - canonical 8필드 변화 없음
- `canonical_change`
  - changed fields 하나 이상
- `mixed_shift`
  - scalar 변화 2개 이상 또는 scalar + array 변화 동시 발생
- field-specific shift
  - changed fields에 해당 canonical field 포함 시 생성
- trigger badge
  - update trigger type에 따라 파생

## 6. display rules

- 1~3개 핵심 badge만 우선 노출
- 짧고 상태 중심 언어 사용
- 서사적 개선/악화 badge 금지
- experimental namespace 기반 badge 금지

## 7. process console attachment

- state panel diff summary
- latest lineage summary
- history timeline item

## 8. one-line lock

> `state_change_interpretation_badge_v1`는 canonical diff/history 결과를 과잉 해석 없이 provenance_only, canonical_change, field shift, trigger origin 정도로 빠르게 읽게 하는 얇은 derived badge layer다.
