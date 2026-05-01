# Space-Boundary Structure Recapitalization Session 5 Intent-to-Codex-Role Mapping Trial v0

## 1. status

```yaml
session: 5
session_name: intent_to_codex_role_mapping_check
verdict: PASS_WITH_NOTE
baseline_lock: false
schema_enforcement: false
implementation: false
```

## 2. purpose

Test whether user intent can determine Codex's role without requiring the user to explicitly steer every step.

## 3. sample inputs

### input 1

```text
이 재료 넣어봐
```

Decision:

```yaml
source_surface: unknown until inspected
Codex_role: interpreter/output mode
possible_elevation: bounded comparer only if concrete comparison target appears
output_shape: boundary material card + selected lenses + safe next move
```

### input 2

```text
이 결과 다시 공간에 넣어봐
```

Decision:

```yaml
source_surface: Codex output / generated artifact / worker return
Codex_role: return summarizer / interpreter
possible_elevation: bounded comparer if compared against prior line
output_shape: validation_return + next_recommended_state
```

### input 3

```text
이걸 작업으로 옮길 수 있어?
```

Decision:

```yaml
source_surface: action request
Codex_role: gatekeeping interpreter
possible_elevation: packet preparer only if boundary, expected return, guardrail, and return hook exist
output_shape: readiness card or packet draft + blockers
```

## 4. mapping table

| User intent | Default Codex mode | Elevation condition | Output shape |
| --- | --- | --- | --- |
| material intake | interpreter/output | comparison target exists | material card + lens pass |
| return to space | return summarizer | needs comparison/refinement | validation_return |
| action transfer | gatekeeping interpreter | packet conditions ready | readiness card or packet draft |
| execution request | gatekeeping interpreter | execution constraints complete | guarded execution + validation_return |
| explanation refinement | rewrite assistant | draft variants needed | explanation draft + flattening note |

## 5. validation

```yaml
role_selection_followed_intent: PASS
prepare_execute_separation_preserved: PASS
output_shape_clearer: PASS_WITH_NOTE
user_steering_reduced: PASS_WITH_NOTE
```

## 6. purpose / direction check

Where Codex may have over-converged:

```text
the mapping table may look like a fixed router, but it is still a trial note.
```

What should not become a rule yet:

- exact role names as schema
- required output shape for every input
- automatic execution permission

Next safest move:

```text
Run Session 6 and force return-to-space reading on one session output.
```

