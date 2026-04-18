[[A]] [[OBJ:state_validation_fixture_v1]] [[SEM:representative_validation_fixture_for_canonical_engine_operating_state]]

# state_validation_fixture_v1

## 1. purpose

- 이번 fixture의 목적은 representative asset 4개에서 canonical operating state layer의 repeatability를 검증하는 것이다.
- 이 fixture는 promotion이 아니라 validation이다.

## 2. fixture assets

- `youtube_03_22`
- `openai_02_11`
- `knowledge_editing_youtube`
- `gary_tan_brain`

## 3. validation axes

- schema validity
- model/store validity
- latest/history consistency
- policy consistency
- canonical field stability
- experimental leakage guard

## 4. expected verdict language

- `expected_state_match`
- `acceptable_drift`
- `policy_violation`

## 5. fixture storage

- expected:
  - `runtime/validation/state_fixture_expected/*.json`
- results:
  - `runtime/validation/state_fixture_results/*.json`
  - `runtime/validation/state_fixture_results/index.json`

## 6. canonical priority

- 검증의 직접 대상은 canonical 8필드다.
- experimental namespace 값은 참고만 하되 verdict를 흔들지 않는다.

## 7. allowable drift

- `comparison_memory_reason`
- `gate_blocker_summary`

위 두 field는 exact equality보다 subset/superset 허용이 더 적절하다.

## 8. one-line lock

> `state_validation_fixture_v1`는 representative asset 4개를 기준으로 canonical operating state layer의 schema/store/policy/latest 반복성을 검증하는 고정 fixture다.
