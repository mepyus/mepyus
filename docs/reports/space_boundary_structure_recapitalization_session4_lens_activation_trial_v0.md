# Space-Boundary Structure Recapitalization Session 4 Lens Activation Trial v0

## 1. status

```yaml
session: 4
session_name: lens_activation_live_output_trial
verdict: PASS_WITH_NOTE
baseline_lock: false
schema_enforcement: false
implementation: false
```

## 2. purpose

Make lens selection visible enough in live use without turning user-facing output into a heavy report.

## 3. trial material

Two materials were compared:

1. Codex output: `formation_movement_interface_space_asset_goal_alignment_audit_v0.md`
2. Runtime evidence: `phase1_36_execution_split_space_check_question_packet/result`

## 4. lens pass

| Material | Selected lenses | What changed because of the lenses |
| --- | --- | --- |
| Codex output | user-intent, feature-direction, risk, residue | read as validation_return / framing_support, not final structure |
| Runtime evidence | evidence, routing, return, risk | read as behavior evidence / evidence_residue, not source intent |

## 5. compact live output shape

Recommended live output:

```text
현재 판정:
이유:
선택 렌즈:
다음 이동:
금지선:
```

If feature direction matters, add one line:

```text
기능/방향 후보:
```

This is slightly more than the old 4-line card, but still light enough.

## 6. example output

```text
현재 판정: validation_return / framing_support
이유: Codex 보고서는 구조 확정이 아니라 현재 자산의 방향 점검을 공간으로 되돌리는 재료입니다.
선택 렌즈: user-intent / feature-direction / risk / residue
다음 이동: Codex output과 runtime evidence를 비교해 return-to-space 습관을 검증합니다.
금지선: final answer, baseline lock, schema화 금지
```

## 7. validation

```yaml
lenses_changed_reading: PASS
user_output_stayed_light: PASS_WITH_NOTE
direction_supported_not_taxonomy: PASS
required_new_schema: false
```

## 8. remaining ambiguity

- whether every material needs visible lens line
- whether lens line should be omitted for trivial tasks
- whether feature/direction candidate should appear only when the user intent is functional

## 9. next safest move

```text
Run Session 5 to map user intent to Codex role and output shape.
```

