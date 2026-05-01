# external-material-intake.skill.md

## Status

```yaml
state: candidate
baseline: false
automation: false
```

## Trigger

Use when the user gives one external material and asks whether it can be used in the space.

Examples:

- "이 자료 공간에 넣어봐"
- "이 외부 도구 우리 구조에서 쓸 수 있어?"
- "이걸 내부 기준과 비교해줘"

## Goal

Read one external material through the user's space criteria without immediately adopting or implementing it.

Return a compact judgment that lets the user decide proceed / hold / user-review-needed.

## Steps

1. Read external material structure.
2. Reference at most 1-2 internal criteria.
3. Compare structure.
4. Create one small dry-run or translation example.
5. Self-check for implementation drift and external authority bias.
6. Return a 4-line footer.

## External structure read

Capture:

- material name
- location/source
- maker's problem
- problem the structure solves
- core components
- operating flow
- hidden assumptions
- risks

## Internal reference rule

Use at most 1-2 internal criteria.

If the right internal reference cannot be found, write:

```text
internal reference missing
```

Do not read the whole deep space.

## Compare as

```text
Same:
Similar but dangerous:
Different:
Borrow later:
Reject for now:
```

## Small dry-run

Make one tiny application example.

Allowed:

- translate the external idea into a candidate lens
- test a footer shape
- test a worker-guide hint

Forbidden:

- implementation
- file modification
- schema creation
- UI design
- automation proposal
- baseline promotion

## Self-check

Answer:

```text
implementation_drift:
external_authority_bias:
internal_conflict:
user_judgment_required:
recommended_position:
```

## Footer

Return:

```text
status:
summary:
risk:
next:
```

## Do not

- Do not summarize only.
- Do not treat external material as truth.
- Do not jump from research to implementation.
- Do not turn a candidate into a locked rule.
- Do not expand this skill into a general automation system.
