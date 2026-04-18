[[A]] [[OBJ:engine_state_update_policy_v1]] [[SEM:lifecycle_policy_for_canonical_engine_operating_state_updates]]

# engine_state_update_policy_v1

## 1. purpose

- 이번 policy의 목적은 `engine_state_schema_v1` 기반 canonical operating state가
  언제 어떤 근거로 history에 append되고 latest에 반영되는지를 명확히 규정하는 것이다.
- 즉 이 policy는 새로운 의미 객체 정책이 아니라 state lifecycle policy다.

## 2. top-level principles

### A. append-first

- state update는 overwrite가 아니라 append-first다.
- authoritative source는 history이고, latest는 append 결과의 파생 표면이다.

### B. latest-is-derived

- latest는 본원장이 아니라 process console/UI를 위한 derived surface다.
- latest 손상 시 history에서 재생성 가능해야 한다.

### C. canonical-before-interpretive

- 직접 관리 대상은 canonical 8필드다.
  - `packet_texture`
  - `grounding_status`
  - `emergence_status`
  - `carryover_risk`
  - `maturation_state`
  - `traceability_status`
  - `comparison_memory_reason`
  - `gate_blocker_summary`

- naming-heavy 해석은 direct 관리 대상이 아니다.

### D. no-forced-promotion

- 애매한 값은 상향 과대판정하지 않는다.
- direct / question_opening_present / low carryover 같은 상향값은 더 강한 근거가 필요하다.

### E. source-return safety

- state-changing update는 `evidence_refs`를 동반해야 한다.

## 3. accepted update triggers

- `backfill`
  - legacy report / comparative memory / representative asset에서 최초 state 생성 또는 보강
- `runtime_evidence`
  - new process-trace / packet / rereading evidence로 재판정할 충분한 근거가 생긴 경우
- `recompute`
  - policy/enum/tie-break 변경으로 latest 재생성이 필요한 경우
- `manual_correction`
  - 운영자가 명시적으로 correction을 승인한 경우

## 4. update sequence

1. incoming record validate
2. canonical vs experimental separation check
3. history append
4. latest projection regenerate
5. latest surface write
6. receipt/log 기록

## 5. latest selection rule

- 기본적으로 latest는 newest valid record를 따른다.
- 단, 아래는 latest 반영 금지 또는 quarantine 대상이다.
  - malformed enum values
  - forbidden canonical contamination
  - missing evidence on state-changing update
  - invalid schema_version path

## 6. field-specific update rules

### A. `packet_texture`

- update 허용:
  - packet evidence가 새로 생겼을 때
  - bridge/payload 분석으로 texture 판정이 달라질 때
- 보수 규칙:
  - compressed -> open 상향은 쉽게 하지 않는다
  - ambiguous하면 기존 texture 유지 + note 추가

### B. `grounding_status`

- update 허용:
  - source ref coverage 변화
  - empty_ref risk 확인
  - fallback -> partial/direct 전환의 충분한 근거
- 보수 규칙:
  - `direct_grounded`는 가장 엄격하게 사용

### C. `emergence_status`

- update 허용:
  - question opening sign 새 확인
  - minimal emergence 반복 확인
  - 조기 고정 evidence로 no/low로 하향 필요 시
- 보수 규칙:
  - `question_opening_present` 남발 금지
  - 애매하면 더 낮은 emergence를 유지

### D. `carryover_risk`

- update 허용:
  - prepared scaffold carryover evidence 새 확인
  - carryover correction 결과 반영
- 보수 규칙:
  - `prepared_scaffold_carryover`는 high의 일반형이 아니라 구체 evidence가 있을 때만 사용

### E. `maturation_state`

- update 허용:
  - hold / residue / weak / fallback / blocked / breathing 상태 변화를 뒷받침하는 새 근거 등장
- tie-break:
  1. `blocked`
  2. `fallback`
  3. `weak`
  4. `hold`
  5. `residue`
  6. `breathing`

### F. `traceability_status`

- update 허용:
  - source -> first-pass -> one-point-five -> second-order -> state 경로의 실제 확인/붕괴
- 승격 규칙:
  - `traceable`은 최소 핵심 단계 연결 evidence가 복수로 있을 때만 사용

### G. `comparison_memory_reason`

- update 허용:
  - compare strip navigation reason 추가
  - similarity pattern 새 확인
- 규칙:
  - array field
  - 문장형 남발 금지
  - enum 중심 유지

### H. `gate_blocker_summary`

- update 허용:
  - blocker integration report 갱신
  - blocker relief/new blocker confirmation
- 규칙:
  - array field
  - 해소되어도 history는 보존, latest에서만 제거 가능

## 7. backfill vs runtime conflict

- 우선순위:
  1. valid runtime evidence update
  2. valid operator-approved correction
  3. valid recompute record
  4. legacy backfill record

- 단서:
  - 더 최근이라는 이유만으로 자동 승격 금지
  - evidence quality가 낮으면 기존 보수값 유지

## 8. experimental namespace guard

- 아래 naming-heavy field는 canonical top-level 유입 금지:
  - `context_unit_name`
  - `paragraph_role_name`
  - `pivot_label`
  - `compression_label`
  - `business_power_shift`
  - `orchestration`

- 이 값들은 `experimental_namespace` 아래에서만 허용한다.
- experimental 값은 canonical update trigger가 될 수 없다.

## 9. provenance fields

- policy-managed provenance field:
  - `schema_version`
  - `update_trigger_type`
  - `update_reason`
  - `evidence_refs`
  - `updated_at`

## 10. validation hooks

- enum validation
- canonical contamination check
- evidence presence check
- latest recompute consistency check

## 11. code linkage

- policy helper:
  - [engine_state_update_policy.py](/Users/sungsookim/universe/vectorfl_replica/app/core/state_store/engine_state_update_policy.py)
- store:
  - [engine_state_store.py](/Users/sungsookim/universe/vectorfl_replica/app/core/state_store/engine_state_store.py)

## 12. one-line lock

> `engine_state_update_policy_v1`는 canonical operating state가 임의 overwrite가 아니라 evidence-backed append-first lifecycle을 통해 history에 남고 latest에 반영되도록 만드는 생애주기 규칙이다.
