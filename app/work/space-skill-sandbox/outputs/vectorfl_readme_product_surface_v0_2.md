# VectorFL

## What VectorFL is

VectorFL is a judgment-recovery layer for messy work material.

It reads inputs, tool results, notes, traces, or partial outputs and asks one question:

```text
What can we safely use from this, and what should happen next?
```

VectorFL is not a note app, schema system, automation layer, registry, or baseline. It does not preserve everything or turn weak material into authority.

It helps a user decide whether a result should be used, watched, validated, held, discarded, or prepared for a narrow next step.

## Map-not-Manual flow

VectorFL works like a map:

1. Read only the relevant material.
2. Recover the usable judgment.
3. Mark what is uncertain or unsafe.
4. Place the result.
5. Name the next small action.

The goal is not to prove that a tool followed rules. The goal is to recover judgment that improves the next task.

## Core Idea

```text
공간은 원칙을 지킨 결과가 아니라, 쓸 수 있는 판단을 회수한다.
```

Meaning:

The point is not that a tool followed the rules. The point is whether the result gives the user something usable.

## How Users Ask

You can ask in normal language:

```text
이 자료를 우리 구조 기준으로 읽어봐.
이 결과 회수해줘.
요약 말고 쓸 값만 뽑아줘.
이걸 실제로 검증해봐.
다음 작업에 쓸 수 있는 판단이 있어?
```

## Default Output Card

VectorFL usually returns:

```text
Purpose:
What was read:
What was not read:
Recovered judgment:
Placement:
Watch:
Next action:
```

## What Counts as Useful

A result is useful when it:

1. answers the user purpose
2. recovers reusable judgment
3. clarifies route / reading angle / placement
4. exposes missing evidence
5. reduces future confusion
6. prevents unsafe promotion or implementation
7. improves the next-work condition

## Result Placement in Plain Language

```text
RETURN_TO_SPACE_VALUE
= 쓸 수 있는 판단

RETURN_TO_SPACE_VALUE_WITH_WATCH
= 쓸 수 있지만 조심해서 써야 하는 판단

WATCH
= 유용해 보이지만 아직 승격 불가

NEEDS_ONE_MORE_NEIGHBOR
= 근거 하나 더 필요

BOUNDED_IMPLEMENTATION_PREP
= 좁은 구현 준비 가능

HOLD
= 보류 / 진행하지 않음

RAW_TRACE
= 기록만 보관
```

## Example

User says:

> 이 자료를 우리 구조 기준으로 읽어봐.

VectorFL responds:

### 목적

이 자료가 다음 작업에 쓸 수 있는 판단을 주는지 확인.

### 읽은 것

사용자가 제공한 자료의 핵심 주장과 적용 가능성.

### 안 읽은 것

전체 로그, raw trace, 관련 없는 파일.

### 회수한 판단

이 자료는 "사용자 요청을 자연어로 받아 내부 운영 구조로 번역해야 한다"는 판단에 쓸 수 있음.

### 배치

```text
RETURN_TO_SPACE_VALUE_WITH_WATCH
= 쓸 수 있지만 조심해서 써야 하는 판단.
```

### 조심할 점

바로 schema나 automation으로 승격하지 않음.

### 다음 행동

다음 Live Task에서 이 판단을 실제 입력에 적용.

## What VectorFL Avoids

VectorFL avoids:

- treating summaries as final truth
- reading full logs by default
- promoting candidates too early
- turning external examples into authority
- making users choose internal categories
- building schema, registry, or automation before real need

## Runtime / Tool Caution

Runtime state and tool outputs are signals, not truth. They can point to a useful next artifact, but the artifact still needs judgment.

## Current Status

```text
LIVE_TASK_OPERATION_READY_WITH_WATCH
```

VectorFL is ready for live task use with watch. It is not baseline, schema, registry, automation, or production workflow.

## Internal Note

Internal operators may use camera/lens, one-neighbor reading, usefulness gates, and return placement maps. New users do not need to choose those categories.
