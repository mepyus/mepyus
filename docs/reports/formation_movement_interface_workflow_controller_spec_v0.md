# Formation-Movement Interface Workflow Controller Spec v0

## 1. status

```yaml
status: workflow_controller_spec
verdict: PASS_WITH_NOTE
purpose: make existing package assets run through a structured routing / state-transition / output policy layer
baseline_lock: false
schema_enforcement: false
implementation: false
runtime_manifest: false
validator_or_script: false
core7_expansion: false
object_family_expansion: false
```

## 2. why this spec exists

The current package has enough assets, but the execution layer is still too manual.

Current problem:

- users must over-specify the path
- package knowledge exists but is not orchestrated automatically
- the same ambiguity often requires explicit operator steering

So this spec defines a controller that turns:

```text
input
→ routing
→ state transition
→ output policy
→ Codex call decision
→ space reread / return
```

into a repeatable operating flow.

This is **not** implementation code.

It is the controller logic specification.

## 3. backend assets used by the controller

The controller should treat these as backend assets, not user-facing forms:

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- `docs/reports/formation_movement_interface_usage_manual_v0.md`
- `docs/reports/formation_movement_interface_cheat_sheet_v0.md`
- `docs/reports/formation_movement_interface_process_first_external_material_note_v0.md`
- `docs/reports/formation_movement_interface_llm_wiki_autoresearch_complete_cycle_note_v0.md`

Meaning:

- package draft:
  core state and transition logic
- usage manual:
  practical usage interpretation
- cheat sheet:
  user-facing compressed interaction pattern
- process-first note:
  line-first routing for external material
- complete-cycle note:
  output-return and reread behavior

## 4. controller top-level rule

Default controller behavior:

```text
애매하면 먼저 4줄 카드로 멈춘다.
```

Default public output:

```text
현재 판정:
이유:
다음 이동:
금지선:
```

The controller should hide deeper state unless one of the escalation conditions is met.

## 5. input router

### route A. external material

Trigger examples:

- “이 링크 넣어봐”
- “이 외부 자료 읽어봐”
- “이걸 공간에 넣을 만한지 봐줘”

Default route:

```text
external material
→ process-first line check
→ unclassified seed
→ reread_priority or framing_candidate
→ compare_only / hold / archive
```

### route B. Codex task request

Trigger examples:

- “이걸 Codex에게 맡겨”
- “Codex로 넘길 수 있어?”
- “바로 실행하지 말고 prepare부터 봐줘”

Default route:

```text
Codex task request
→ unclassified seed
→ boundary / expected_return_form / guardrail / reread_return_hook check
→ bounded_action_candidate or HOLD
→ prepare_worker_packet only if ready
```

### route C. user explanation request

Trigger examples:

- “이 설명 어때?”
- “너무 납작한지 봐줘”
- “final definition으로 올리지 말고 판정해줘”

Default route:

```text
user explanation
→ unclassified seed
→ L/R/T/X check
→ bounded_action_candidate draft or hold
→ refine / validation_return
```

### route D. overlap-heavy note

Trigger examples:

- “이건 A/C/T/X/R/L이 겹치는 것 같아”
- “단일 축으로 정리하지 말고 hold 먼저 봐줘”

Default route:

```text
overlap note
→ unclassified seed
→ reread_priority
→ overlap hold check
→ compare_only / reread_against_A_C_T_X_R_L
```

### route E. returned result

Trigger examples:

- “이 결과 다시 읽어줘”
- “final로 보지 말고 validation_return으로 봐줘”

Default route:

```text
returned result
→ validation_return
→ refine / hold / downgrade / archive_as_residue
→ promote only under exceptional conditions
```

## 6. route-specific front-door policy

### for external material

The controller must first ask internally:

```text
이미 살아 있는 내부 line/axis가 있는가?
이 자료는 formation-side first인가, movement-side first인가?
```

It should prefer:

```text
line-first / process-first
```

over:

```text
classification-first
```

### for Codex task

The controller must first ask internally:

```text
이 요청은 prepare 단계에 들어갈 만큼 bounded한가?
```

It should prefer:

```text
HOLD before prepare
```

over:

```text
packetization by vague intent
```

### for explanation

The controller must first ask internally:

```text
이 설명은 readable한가?
그리고 residue hook이 남아 있는가?
```

It should prefer:

```text
refine
```

over:

```text
canonical wording reuse
```

## 7. state machine

The controller uses these states:

```text
unclassified seed
reread_priority
framing_candidate
bounded_action_candidate
guarded_execution
validation_return
```

### seed entry rule

Always default to:

```text
unclassified seed
```

unless the input is already obviously a returned result.

### state transition rules

#### seed -> reread_priority

Use when:

- role is unclear
- overlap is high
- direct evidence / defensive logic / comparison frame split is unresolved

#### seed -> framing_candidate

Use when:

- candidate role is visible
- bounded comparison use is plausible
- promotion barrier can be stated

#### seed -> bounded_action_candidate

Use only when:

- actionable question exists
- boundary exists
- expected return form exists
- reread return hook exists

#### bounded_action_candidate -> guarded_execution

Use only when:

- execution_constraint exists
- guardrail exists
- fallback_policy exists
- trust_scope exists
- expected_return_form exists
- reread_return_hook exists

If any of these are missing:

```text
stay in prepare / HOLD
```

#### any state -> validation_return

Use whenever a meaningful output or result has come back.

## 8. controller output policy

### default output level

Always return a 4-line card first:

```text
현재 판정:
이유:
다음 이동:
금지선:
```

### medium output level

Open formed-sidecar detail only if:

- state is contested
- compare-only needs justification
- promotion barrier needs explicit explanation

### full output level

Generate a full note or report only if:

- repeated ambiguity remains after 4-line handling
- a reusable comparison object is being created
- output must be reread inside the space
- trust_scope / object_type / hierarchy may change

## 9. Codex call policy

The controller should not call Codex just because the input is complex.

Codex should be called when one of these is true:

- bounded comparison output is needed
- translation into user-facing explanation needs structured drafting
- bounded task packet is ready for preparation
- a returned output needs structured compare/rewrite

Codex should not be called when:

- the task is still unresolved at `reread_priority`
- the user only needs a 4-line judgment card
- boundary is too weak for even `allowed_to_prepare`

## 10. space insertion policy

Space insertion should mean:

```text
reusable reread-support object placement
```

not:

- save the link
- import doctrine
- lock an axis

The controller should insert into space when:

- a comparison object has stable role clarity
- the object can be reused across more than one scene
- the object still has an explicit promotion barrier

## 11. validation return policy

### default short form

Use:

```text
observed_result:
reread_trigger:
next_recommended_state:
```

### upgrade to full validation return when

- promotion risk appears
- baseline risk appears
- schema risk appears
- object_type changes
- trust_scope changes
- explanation flattening is strong
- overlap ambiguity is itself part of the result
- expected_return_form and actual result diverge significantly

## 12. stop / hold policy

The controller must stop expansion when:

```text
구조는 버티고 있음
READY_FOR_CLARIFICATION_PATCH 없음
남은 문제는 threshold/example 부족
지금 patch하면 operator cost가 늘어날 위험이 있음
```

Correct response:

- hold structure expansion
- keep package as `package_candidate`
- collect natural weak examples only when they arise in real work

## 13. user-facing triggers the controller should understand

The controller should map these natural prompts automatically.

### external material

```text
이거 넣어봐
이 링크 읽어봐
공간에 넣을 만한지 봐줘
```

### Codex task

```text
이걸 Codex에게 맡겨도 돼?
바로 실행 말고 prepare부터 봐줘
```

### explanation

```text
이 설명 너무 납작한지 봐줘
final definition으로는 올리지 마
```

### overlap

```text
이건 여러 렌즈가 겹치는 것 같은데
단일 축으로 정리하지 마
```

### return

```text
이 결과 다시 읽어줘
final로 닫지 말고 validation_return으로 봐줘
```

## 14. what the controller should do silently

The controller should silently:

- assign seed state
- choose the first internal line/axis when possible
- decide whether the case is formation-first or movement-first
- block promotion by default
- block execution unless readiness is explicit
- choose short vs full validation level

The user should not have to request these explicitly every time.

## 15. what the controller should never do

- never force Core 7 as user input
- never add new weak-signal-only state names
- never auto-promote because multiple `PASS_WITH_NOTE` cases exist
- never treat `prepare_worker_packet` as execution
- never treat `validation_return` as final by default
- never import external workflow as internal doctrine automatically

## 16. recommended next phase

This spec suggests the next correct phase is:

```text
controller-driven usage
```

not:

- more package expansion
- more weak-signal rounds by default
- immediate clarification patch

Meaning:

- use this controller spec as the hidden execution layer
- keep user-facing interaction at the 4-line-card level by default
- open deeper package logic only when escalation conditions are met

## 17. verdict

`PASS_WITH_NOTE`

Reason:

- the package assets are now organized into a coherent control flow
- the main remaining gap is real implementation, not conceptual routing
- the note is that this is still a spec, so actual automatic behavior depends on disciplined use

## 18. intentionally not changed

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- any validation case
- any weak-signal document
- Core 7
- object family 5종
- no baseline lock
- no schema enforcement
- no implementation
- no runtime manifest
- no validator/script

## 19. unresolved questions

- how much silent inference should the controller do before it becomes too opaque?
- when should the controller automatically escalate from 4-line card to medium/full note?
- should some high-frequency real-work scenes get fixed route presets later?
