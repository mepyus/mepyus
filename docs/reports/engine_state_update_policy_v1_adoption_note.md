[[A]] [[OBJ:engine_state_update_policy_v1_adoption_note]] [[SEM:adoption_note_for_engine_state_update_policy_lifecycle_lock]]

# engine_state_update_policy_v1_adoption_note

## 1. why latest is derived

- latest는 process console/UI를 위한 operating surface다.
- authoritative source는 history이고, latest는 그것의 파생 projection이다.
- 이렇게 해야 상태 drift나 UI 손상 시 history에서 다시 읽을 수 있다.

## 2. why append-first

- state를 overwrite하면 비교 기억과 상태 변화 이유를 잃는다.
- append-first는 weak/fallback/hold도 폐기하지 않고 history에 남긴다.

## 3. trigger summary

- `backfill`
  - 최초 state 생성 / legacy interpretation hydration
- `runtime_evidence`
  - 새 packet / trace / rereading evidence 반영
- `recompute`
  - policy나 tie-break 수정에 따른 재산출
- `manual_correction`
  - operator-approved correction

## 4. canonical field update read

- canonical 8필드는 전부 보수적으로 갱신한다.
- 특히 아래는 상향 과대판정 금지:
  - `direct_grounded`
  - `question_opening_present`
  - `low` carryover risk

## 5. backfill/runtime conflict

- runtime evidence가 더 최근이고 충분히 강하면 backfill보다 우선한다.
- 하지만 “더 최근”만으로는 부족하고, evidence quality가 더 중요하다.

## 6. maturation tie-break

- top-level canonical state는 더 강한 제한 상태를 우선 표면화한다.
- 현재 tie-break:
  1. `blocked`
  2. `fallback`
  3. `weak`
  4. `hold`
  5. `residue`
  6. `breathing`

- 이건 breathing을 부정하는 게 아니라, top-level state를 더 보수적으로 보여주는 규칙이다.

## 7. experimental namespace guard

- naming-heavy 해석은 canonical top-level에 올리지 않는다.
- `context unit`, `paragraph role`, `pivot/compression`, `business_power_shift`, `orchestration` 등은 계속 experimental namespace에 둔다.
- 이 guard가 있어야 엔진이 operating state보다 해석 이름을 먼저 굳히지 않는다.

## 8. current ambiguity

- `emergence_status`의 `minimal` vs `low` 경계는 아직 흔들릴 수 있다.
- `carryover_risk`의 `high` vs `prepared_scaffold_carryover`도 evidence granularity에 따라 달라질 수 있다.
- `traceability_status`의 `traceable` 승격은 앞으로 더 엄격한 source-return evidence가 필요할 수 있다.

## 9. one-line read

> 이번 adoption은 state를 더 많이 만들기 위한 것이 아니라, 이미 존재하는 canonical operating state가 어떤 근거와 어떤 trigger 아래 history에 남고 latest에 반영되는지 흔들리지 않는 lifecycle로 잠그기 위한 것이다.
