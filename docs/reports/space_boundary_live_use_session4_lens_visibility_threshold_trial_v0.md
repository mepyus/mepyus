# Space-Boundary Live Use Session 4 Lens Visibility Threshold Trial v0

## 1. status

```yaml
session: 4
package: space_boundary_live_use_stabilization
verdict: PASS_WITH_NOTE
baseline_lock: false
schema_enforcement: false
implementation: false
```

## 2. purpose

Decide how much lens information should appear in user-facing output during live use.

## 3. compared output levels

### level 1. 4-line card only

Pros:

- lightest
- easiest to read

Cons:

- hides why the material was read that way
- repeats earlier problem where lens values disappear

### level 2. 4-line card + selected lenses

Pros:

- still light
- makes reading method visible
- prevents hidden convergence

Cons:

- slightly heavier than original 4-line card

### level 3. 4-line card + selected lenses + feature/direction candidate

Pros:

- best when material affects future function or purpose

Cons:

- too heavy for trivial material
- may overproduce feature candidates

## 4. threshold decision

Default:

```text
Level 2 for non-trivial boundary material.
```

Use Level 3 only when:

- user intent is functional
- material changes direction
- material suggests a feature/purpose candidate
- movement decision depends on the feature-direction lens

Use Level 1 only for:

- trivial material
- already settled follow-up
- simple retrieval confirmation

## 5. validation

```yaml
reduces_user_burden_without_hiding_reading: PASS
lens_visibility_not_mandatory_for_trivial_cases: PASS
feature_direction_not_forced: PASS
```

## 6. user-facing card model

```text
현재 판정:
이유:
선택 렌즈:
다음 이동:
금지선:
```

Optional:

```text
기능/방향 후보:
```

## 7. next

```text
Session 5 Codex role defaulting live trial.
```

