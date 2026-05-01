# Structured Footer Lens

## Status

```yaml
state: lens_candidate
baseline: false
implementation: false
automation: false
```

## What this lens solves

Workers often return long logs or confident summaries that leave the user to decide what actually happened.

This lens lowers a worker result into four decision lines:

```text
status:
summary:
risk:
next:
```

## Core distinction

```text
완료 != 승인
완료 != lock
완료 != baseline
summary != truth
PASS_WITH_NOTE != ignore note
```

## Status choices

- 완료
- 검증 필요
- 사용자 판단 필요
- 보류

## Read as

- `완료`: low-risk task ended and no further decision is needed
- `검증 필요`: output must be checked before next task
- `사용자 판단 필요`: sovereignty boundary is touched
- `보류`: unsafe or unclear; do not proceed

## Do not

- Do not add many status categories.
- Do not use maturation labels such as Canonical/Maturing as runtime status.
- Do not hide risk to make the footer short.
- Do not treat footer as evidence.
