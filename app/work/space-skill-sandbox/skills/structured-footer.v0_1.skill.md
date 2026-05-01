# Structured Footer Skill v0.1

## Status

```yaml
state: candidate
baseline: false
automation: false
implementation: false
```

## Trigger

Use after a sandbox run, worker result, or validation result when the user needs a compact decision surface.

## Steps

1. Identify whether the result is low-risk, needs validation, needs user judgment, or should be held.
2. Write one short factual summary.
3. Preserve one meaningful risk or say none.
4. Name the next action candidate.
5. Do not promote the result.

## Output

```text
status:
summary:
risk:
next:
```

## Status rule

```text
완료:
  low-risk, no transition needed

검증 필요:
  result moves forward, claim/evidence needs checking, or PASS_WITH_NOTE carries a note

사용자 판단 필요:
  baseline/schema/architecture/delete/security/privacy/install/automation/lock/promotion

보류:
  scope unclear, unsafe, contradictory, or missing required source material
```

## Forbidden

- extra status taxonomy
- approval wording
- baseline/lock wording
- summary as truth
- hiding notes from PASS_WITH_NOTE
