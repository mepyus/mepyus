# Integrated Engine 2026-04-17 Obsidian Source Ingest Classification v0

## Verdict

PASS

## Purpose

This note records the five 2026-04-17 Obsidian notes provided by the user and classifies what should be locked now, what should become a patch candidate, what should stay as reference, and what should remain hold.

This is not a UI implementation patch. It is an intake and classification step so the next integrated-engine work starts from the user's current intent instead of from yesterday's narrower CLI-on-top path alone.

## Source Notes Read

| source note | primary role | classification |
| --- | --- | --- |
| `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/04-17/패널 정리 1.md` | panel relationship and 4-layer packet mapping | lock + patch candidate |
| `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/04-17/통합엔진 구조화 3.md` | integrated-engine body/process/lens framing | lock |
| `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/04-17/언어 매핑 2.md` | surface-language guidance for active core panels | patch candidate |
| `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/04-17/바디 정리5.md` | body/material/metabolism diagnosis | lock + next design gate |
| `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/04-17/구조화4.md` | body re-establishment summary with material classes | lock |

## Locked Now

### 1. The Body / Process / Lens Distinction

- Body: the fixed User / VectorFL / Engine 3-surface structure.
- Process frame: the common operating physiology that every task should pass through.
- Lens: the temporary purpose of a task such as translation, validation, implementation, self-learning, alignment, or external-material analysis.

This means new work should not be read as "add one more card or feature" first. It should be read as whether the body can digest another lens without losing the fixed 3-surface structure.

### 2. Work Packet As The Basic Screen Unit

The screen should not be understood as a pile of panels. The basic unit is a work packet.

Minimum packet layers:

1. outer frame: what work is active, why, current position, next candidate route
2. internal evidence: source material, line, axis, failure trace, instruction, prior routine, conflict/gap
3. mediation/guard: owner, tool, surface route, hold/reread/deposit state, do/do-not
4. trace/record: recent turn, mark history, state transition, failure/reflux/deposit state

### 3. Internal Search Gate Must Precede Execution

The current CLI-on-top path is useful but insufficient if it lets the user go straight from instruction to CLI execution.

Locked operating process:

```text
instruction intake
-> internal search
-> evidence bundle
-> VectorFL mediation / packet shaping
-> User organization
-> Engine processing
-> VectorFL reflux
-> record / sedimentation
```

This is the difference between an integrated engine and a UI wrapper around CLI.

### 4. Core Materials Of The Body

The body must digest five core materials:

- purpose
- memory
- process
- decision
- sedimentation

These are circular, not linear:

```text
purpose -> memory -> process -> decision -> sedimentation -> memory
```

### 5. Derived Materials

Derived materials grow from the core:

- event
- interpretation
- external translation
- self-structuring
- emotion / pressure

These should not be flattened into simple logs or TODOs. They are diagnostic and growth material.

### 6. Memory Is Metabolism, Not Storage

The weak point identified by the source notes is not lack of memory. It is that memory is not yet a forced prior input to the current task.

Locked meaning:

```text
memory must become "the past that changes the current task"
```

Memory capture triggers:

- friction
- repetition
- reusability
- structural-change potential
- connection power

### 7. Human Surface Language Direction

The UI should show human-readable language first and keep internal labels as secondary badges.

Locked rule:

```text
human phrase first; internal label as badge
```

This is not final glossary work. It is an operating readability rule.

## Patch Candidates

These are valid next implementation candidates, but should be done in bounded patches after today's lock:

1. Active core panel title/description replacement.
2. Work-packet framing over current surface sections.
3. Internal evidence layer / internal-search gate visual slot.
4. Surface-language replacement for route buttons:
   - `user_assignment_candidate` -> 사용자 확인/배정 후보
   - `engine_request_candidate` -> 엔진 처리 검토 후보
   - `validation_target` -> 다시 검토 대상
   - `deposit_candidate` -> 보관 후보
   - `not_ingested` -> 아직 보관 안 됨
5. OperationLogPanel reframing as work memory, not generic log.
6. Support panel classification as internal evidence / trace / hold.

## Reference Only

These ideas should inform design but are not direct implementation orders yet:

- body as digestive/metabolic system
- camera frame / lens metaphor
- emotion / pressure as diagnostic material
- self-learning as official work frame
- self-structuring as body maintenance process

## Hold

Do not open these from the source notes yet:

- new surface
- full governance/policy layer
- persistence
- multi-work overview dashboard
- Gemini adapter
- async/background runner expansion
- final glossary
- external translation harvest
- deletion of old panels

## Next Operating Consequence

Yesterday's first path remains useful, but today's start point changes the evaluation lens:

```text
Do not only ask "does CLI run from the UI?"
Also ask "does the screen read as a work packet passing through memory, process, decision, and sedimentation?"
```

