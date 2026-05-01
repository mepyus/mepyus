# Space-Boundary Live Use Session 5 Codex Role Defaulting Trial v0

## 1. status

```yaml
session: 5
package: space_boundary_live_use_stabilization
verdict: PASS_WITH_NOTE
baseline_lock: false
schema_enforcement: false
implementation: false
```

## 2. purpose

Test whether Codex role can be selected by user intent and process location in live-like prompts.

## 3. prompt trials

| Prompt | Source surface | Codex role | Output shape | Guardrail |
| --- | --- | --- | --- | --- |
| `이 재료 넣어봐` | unknown boundary material | interpreter/output mode | material card + lenses | no execution |
| `이 결과 다시 공간에 넣어봐` | generated output / return | return summarizer | validation_return | not final |
| `이걸 작업으로 옮길 수 있어?` | action request | gatekeeping interpreter | readiness card / blockers | prepare != execute |
| `이 로그가 뭘 말하는지 봐줘` | runtime evidence | interpreter/output mode, hybrid if needed | evidence card | evidence != intent |

## 4. observed pattern

Codex role can default from:

```text
user intent + source surface + process location
```

without requiring the user to say:

- compare only
- do not execute
- return to space
- interpret the log as evidence

## 5. validation

```yaml
role_selection_by_intent: PASS
prepare_execute_preserved: PASS
runtime_evidence_boundary_preserved: PASS
user_steering_reduced: PASS_WITH_NOTE
fixed_router_risk: PASS_WITH_NOTE
```

## 6. what not to lock

- exact role table
- automatic role router
- execution permission
- required output shape

## 7. next

```text
Session 6 mini end-to-end trial.
```

