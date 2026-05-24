# VectorFL Space & Usage Specification v0.1

## 0. Status

```text
USAGE_SPEC_CANDIDATE_WITH_WATCH
```

This is an internal operating specification for Supervisor / Gemini / Claude / Codex work.

It is not:

- baseline
- schema
- registry
- automation
- API contract
- routing authority
- production workflow
- replacement for user judgment

## 1. Core Operating Sentence

```text
공간은 원칙을 지킨 결과가 아니라, 쓸 수 있는 판단을 회수한다.
```

Operating meaning:

- Do not preserve everything.
- Do not trust tool output directly.
- Recover useful judgment.
- Improve the next-work condition.

## 2. Full Operating Loop

```text
User Purpose
-> Prompt Intake Gateway
-> Camera Selection
-> Lens Selection
-> Smallest Sufficient Context
-> One Neighbor if needed
-> Mission Packet / Map
-> Worker Result
-> Result Usefulness Gate
-> Return Placement
-> Compounding Check
-> Next Work
```

Status:

```text
live-use candidate with watch
```

## 3. Prompt Intake Gateway

Before using tools, identify:

```text
purpose:
material:
decision needed:
missing evidence:
smallest sufficient context:
expected useful result:
```

Do not route by keyword alone. Korean prompts such as `정리해줘` must be resolved by context.

## 4. Camera / Lens

Camera means:

```text
where / what surface are we observing?
```

Lens means:

```text
how / by what interpretive question are we reading it?
```

Important downshift:

```text
Camera/Lens are flexible operating filters, not enums, schemas, or required fields.
```

Use them to make reading sharper. Do not make the user choose internal categories.

## 5. Smallest Sufficient Context

Start with the smallest context that can answer the current task.

Do not load all maps, logs, docs, profiles, and runtime data by habit.

If the current context is insufficient, state:

```text
missing_layer:
why_current_context_is_insufficient:
requested_neighbor:
expected_useful_result_from_neighbor:
```

Request exactly one neighbor unless the user explicitly approves broader reading.

## 6. One-Neighbor Rule

Use one semantic neighbor when:

- runtime state points to an artifact
- result shape lacks the reason why
- validation target needs one source
- a package metadata layer points to one semantic file

Do not:

- read full logs by default
- read raw trace by default
- expand to a directory by habit
- treat missing context as permission for broad repo inspection

## 7. Runtime State Boundary

Runtime state is an observation signal / pointer.

Read small:

```text
schema_version
surface_role
current_posture
guard
latest_return pointer
recent count
available actions
package event count
staleness/error signal
```

Do not dump by default:

```text
full JSON
full recent arrays
full package events
previews
notebooks
manifests
registries
logs
raw traces
```

Runtime state is not truth. It tells the worker what to inspect next.

## 8. Result Usefulness Gate

Ask:

1. Did it answer the user purpose?
2. Did it recover reusable judgment?
3. Did it clarify route / camera / lens / placement?
4. Did it expose missing evidence?
5. Did it reduce future confusion?
6. Did it prevent unsafe promotion or implementation?
7. Did it improve the next-work condition?

If not, place as watch, hold, raw trace, or request one neighbor.

## 9. Return Placement

Use:

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

Default safety:

Most good results should first be `RETURN_TO_SPACE_VALUE_WITH_WATCH`.

## 10. Validation Target

`validation_target` is not failure.

It means:

```text
controlled pause before promotion, implementation, or structural reuse
```

Use when:

- useful but thin output needs confirmation
- implementation needs build/test/run check
- worker result is plausible but not verified
- external fragment should not be promoted

## 11. Compounding Check

Ask:

```text
What does this recovered judgment make easier next time?
```

If nothing improves, do not invent a lesson. Place as raw trace, watch, or hold.

Compounding does not mean accumulating more material.

Compounding means:

```text
the next judgment starts from better conditions than the previous one
```

## 12. Worker Role Split

### User

- final direction
- priority
- promotion approval

### Supervisor / ChatGPT

- route choice
- downshift
- provenance separation
- user-facing judgment
- accept / watch / hold / next judgment

### Gemini

- broad reading
- external material interpretation
- candidate comparison
- execution review
- closeout
- compounding judgment

### Codex

- file-grounded narrow check
- structure confirmation
- surgical repo patch
- build/test/run
- actual repo-touch execution

Current practice:

```text
Codex tokens are conserved.
Gemini absorbs broader synthesis when broad work is needed.
Codex handles narrow repo-grounded action when approved.
```

Do not freeze these roles into permanent identity doctrine. Treat them as current live-use roles with watch.

## 13. Guardrails

Do not:

- promote to baseline
- create schema
- create registry
- create automation
- redesign API by default
- redesign UI by default
- start broad implementation
- expand full logs by default
- promote external fragments
- model CLI as fourth surface
- auto-update `OPERATING_GUIDE`
- continue structure rounds by default

## 14. Live Task Success Criteria

A live task succeeds when:

1. purpose is clear
2. camera/lens are appropriate enough
3. context stays small unless a missing layer appears
4. one neighbor is requested when needed
5. result usefulness is judged
6. placement is explicit
7. missing evidence is visible
8. next-work condition improves or the result is safely held

## 15. Current Active Status

```text
LIVE_TASK_OPERATION_READY_WITH_WATCH
READY_FOR_LIVE_TASK
```

The next default move is real task application, not more structure creation.

## 16. Internal Operator Reminder

This document is a map, not law.

Use it to preserve judgment quality while keeping the user-facing surface simple.
