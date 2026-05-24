# VectorFL Live Task Operation Index v0

2026-05-09

## 0. Status

Current status:

```text
LIVE_TASK_OPERATION_READY_WITH_WATCH
```

Meaning:

- The structure-building round is closed.
- The system should now be applied to real tasks.
- This list is not registry, schema, baseline, automation, or routing authority.
- This is a live-use task operation index with watch.

## 1. Core Operating Anchor

Core sentence:

```text
공간은 원칙을 지킨 결과가 아니라, 쓸 수 있는 판단을 회수한다.
```

Current operating meaning:

- The goal is not to accumulate more material.
- The goal is not to trust worker output directly.
- The goal is to recover usable judgment and improve next-work conditions.

## 2. Current Main Flow

```text
User Purpose
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

## 3. Active Operating Maps

### 3.1 Runtime Observation Map

Role:

Read current runtime position and pointers without full runtime JSON dump.

Use when:

- checking runtime state
- finding what latest return points to
- reading pointers before opening logs/artifacts

Watch:

Runtime state is an observation signal / pointer, not truth.

### 3.2 One-Neighbor Rule

Role:

When a missing layer appears, read one closest semantic neighbor instead of expanding broadly.

Use when:

- runtime pulse points to a `structured_return`
- a result cannot explain why
- exactly one evidence neighbor is needed

Do not:

- expand to full logs by default
- read raw trace by default
- read everything just in case

### 3.3 Validation Target Placement Map

Role:

Read `validation_target` as a controlled pause, not a failure.

Use when:

- worker/runtime output returns `validation_target`
- an external fragment is useful but thin
- verification is needed before promotion, implementation, or structural reuse

Core criterion:

```text
validation_target is not a failure.
validation_target is a controlled pause before promotion, implementation, or structural reuse.
```

### 3.4 Result Usefulness Gate

Role:

Judge whether a returned result is actually useful.

Gate questions:

1. Did it answer the user purpose?
2. Did it recover reusable judgment?
3. Did it clarify route / camera / lens / placement?
4. Did it expose missing evidence?
5. Did it reduce future confusion?
6. Did it prevent unsafe promotion / implementation?
7. Did it improve next-work conditions?

Status:

```text
accepted with downshift
```

### 3.5 Return Placement Mini-Map

Role:

Decide where the result belongs.

Placements:

1. `RETURN_TO_SPACE_VALUE`
2. `RETURN_TO_SPACE_VALUE_WITH_WATCH`
3. `WATCH`
4. `NEEDS_ONE_MORE_NEIGHBOR`
5. `BOUNDED_IMPLEMENTATION_PREP`
6. `HOLD`
7. `RAW_TRACE`

Watch:

Most good results should initially be placed as `RETURN_TO_SPACE_VALUE_WITH_WATCH`.

### 3.6 Compounding Check Mini-Map

Role:

Check whether the result actually improves next-work conditions.

Core criterion:

```text
Compounding does not mean accumulating more material.
Compounding means the next judgment starts from better conditions than the previous one.
```

Korean criterion:

```text
복리는 자료가 더 많이 쌓이는 것이 아니다.
복리는 다음 판단이 이전보다 더 좋은 조건에서 시작되는 것이다.
```

## 4. Active Structural Anchors

### 4.1 Fixed 3-Surface Body

Current fixed body:

1. User Surface
2. VectorFL Surface
3. Engine Surface

### 4.2 CLI Placement

Core judgment:

```text
CLI is provider, not surface.
```

Korean:

```text
CLI는 네 번째 surface가 아니다.
CLI는 User / VectorFL / Engine 위에 붙는 backend / tool-provider / execution-control layer다.
```

Placement:

```text
RETURN_TO_SPACE_VALUE_WITH_WATCH
```

## 5. Active Role Split

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

Watch:

- Save Codex token budget.
- Let Gemini absorb broader burden first when broad synthesis is needed.

## 6. Current Watch List

1. Paperclip LF07
2. OpenClaw LF01/02
3. OpenHarness LF09
4. `started_at` missing
5. runtime metadata thinness
6. full logs / raw traces expansion too early
7. UI convergence risk
8. guide / baseline / registry hardening too early
9. ceremony bloat
10. external fragment promotion risk

## 7. Current Stop List

Do not:

1. promote to baseline
2. create schema
3. create registry
4. create automation
5. redesign API
6. redesign UI
7. start broad implementation
8. expand full logs by default
9. promote external fragments
10. model CLI as fourth surface
11. auto-update `OPERATING_GUIDE`
12. keep expanding structure rounds

## 8. Live Task Intake Checklist

For a new material/request, check:

1. Why put this material into the space?
2. What judgment is being made?
3. What camera is needed now?
4. What lens is needed now?
5. What is the smallest sufficient context?
6. Is one neighbor needed, or is this enough?
7. What placement should the result receive?
8. Did the result improve next-work conditions?

## 9. Default Camera List

1. external material interpretation camera
2. internal structure re-centering camera
3. runtime / worker result review camera
4. implementation readiness camera
5. validation target camera
6. closeout / handoff camera
7. live task operation camera

## 10. Default Lens List

1. Result Usefulness Lens
2. Validation Need Lens
3. Return Placement Lens
4. Compounding Lens
5. Camera/Lens Fit Lens
6. Smallest Sufficient Context Lens
7. Runtime Observation Lens
8. One-Neighbor Lens

## 11. Current Ready State

Current readiness:

```text
READY_FOR_LIVE_TASK
```

From the next input:

- do not create more structure by default
- process the real task
- pass results through the usefulness gate
- decide placement
- check compounding
- split Codex/Gemini only when needed

## 12. Short Operating Card

When material arrives:

1. identify purpose
2. choose camera/lens
3. read small
4. add one neighbor only if needed
5. do not trust the result directly
6. check usefulness
7. place the result
8. check whether next-work conditions improved

## 13. Final Note

This index is the current operating table of contents for live task use.

It is not a registry, schema, baseline, guide authority, or automation.

It should be used to process real tasks, not to continue structure-building by default.
