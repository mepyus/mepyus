# Formation-Movement Interface Codex Coupling Diagnostic Note v0

## 1. status

```yaml
status: diagnostic_note
focus: package_to_codex_coupling
verdict: PASS_WITH_NOTE
purpose: inspect whether the current assets connect to Codex naturally and goal-directionally
no_package_modification: true
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_runtime_manifest: true
no_validator_or_script: true
```

## 2. question

The core question is not:

- can Codex be used?

It is:

- does the current package make Codex a natural part of the flow?
- does Codex receive inputs in a purpose-shaped way?
- does Codex return outputs that the space can naturally reread?
- or does Codex still feel like an extra manual sub-step that has to be explicitly invoked each time?

## 3. compressed diagnosis

```text
현재 시스템은 Codex를 “호출 가능한 도구”로는 잘 다루지만,
아직 “목적지향 공정의 자연스러운 운동기관”으로는 덜 연결되어 있다.
```

More concretely:

- entry into Codex is partially structured
- return from Codex is conceptually structured
- but the middle layer that turns user purpose into the right Codex role is still too manual

## 4. what already works

### A. Codex is no longer treated as automatic execution

The package successfully established:

- `prepare_worker_packet != execution`
- `allowed_to_prepare != allowed_to_execute`
- `validation_return != final`

This is a real gain.

It means Codex is no longer a silent shortcut to action.

### B. Codex can already play multiple roles in theory

From the existing notes, Codex is already being used as:

- bounded comparer
- explanation drafter
- one-shot packet preparer
- structured output generator

So the package is not locked to a single “Codex = execution worker” model.

### C. return-to-space logic exists

The complete-cycle notes already define:

```text
Codex-style comparison output
→ space reread of that output
→ line / axis / lens placement
→ validation-style return
```

So the conceptual loop is present.

## 5. what is still weak

### A. Codex role selection is not yet automatic enough

Right now the user often still has to imply or explicitly say:

- use Codex only as comparer
- do not execute
- just prepare the packet
- read this as validation_return

This means the package has rules, but not yet a strong enough **Codex role router**.

The missing internal question is:

```text
지금 Codex는 비교기인가, 번역기인가, 준비기인가, 실행기인가, 환류 재작성기인가?
```

### B. purpose is not yet strongly shaping Codex invocation

Current routing looks at input type well enough:

- external material
- Codex task
- explanation
- overlap
- returned result

But a stronger Codex coupling needs:

```text
current purpose
→ needed Codex role
→ safe output shape
```

At the moment, this mapping is still weak.

### C. Codex output shape is not yet defaulted enough

The package knows output should come back as validation material.

But it still does not strongly default the output shape by route.

Examples:

- external material compare:
  should default to comparison note
- Codex prepare:
  should default to packet draft + blockers
- explanation:
  should default to 2-3 draft variants + flattening note
- overlap:
  should default to lens-separated reread note

These are implied, but not yet tightly coupled to the controller.

## 6. current coupling level by stage

### stage 1. user input -> Codex entry

Current state:

`partially coupled`

Why:

- the controller spec routes Codex tasks
- but the user still often has to explicitly steer how Codex should be used

### stage 2. package state -> Codex role

Current state:

`weakly coupled`

Why:

- states exist (`reread_priority`, `framing_candidate`, `bounded_action_candidate`, etc.)
- but the mapping from state to Codex role is not yet first-class

Needed pattern:

```text
framing_candidate + compare_only
→ Codex = comparer

bounded_action_candidate + explanation route
→ Codex = drafter

bounded_action_candidate + prepare route
→ Codex = packet preparer

guarded_execution
→ Codex = executor

validation_return
→ Codex = return summarizer / comparer / rewrite assistant
```

### stage 3. Codex output -> space reread

Current state:

`conceptually coupled, operationally light`

Why:

- the complete-cycle notes show how this should work
- but in live usage the output still feels manually wrapped into notes rather than automatically re-entering the space

## 7. main bottleneck

The main bottleneck is not that Codex is disconnected.

It is that Codex is connected mainly at the edges:

```text
input -> maybe call Codex
output -> maybe reread in space
```

But the middle layer is weak:

```text
purpose -> process location -> Codex role -> output shape
```

This is why the flow still feels operator-heavy.

## 8. what natural Codex coupling should look like

The desired flow is:

```text
user purpose arrives
→ controller detects process location
→ controller chooses Codex role automatically
→ Codex produces the route-appropriate output shape
→ output re-enters space as validation/reread material
→ user sees only the 4-line card unless escalation is needed
```

This would make Codex feel less like:

- a tool that must be manually instructed every time

and more like:

- the movement organ that the process naturally delegates to when needed

## 9. concrete missing layer

What is missing is not a new ontology.

It is a **Codex role coupling layer**.

Minimum needed mapping:

### route: external material

- if line-first reread only:
  Codex not called
- if bounded compare needed:
  Codex = comparer

### route: Codex task

- if boundary weak:
  Codex not called
- if prepare-ready:
  Codex = packet preparer
- if execution-ready:
  Codex = executor under guardrails

### route: explanation

- Codex = explanation drafter / contrast generator

### route: overlap

- Codex = lens separator / comparison writer

### route: returned result

- Codex = output condenser / comparer / rewrite assistant

## 10. what this means for our assets

Current assets are already enough to support this coupling.

They are just not yet arranged in a Codex-specific activation chain.

Current backend assets already contain:

- state machine
- route families
- prepare/execute separation
- validation_return logic
- process-first external routing
- complete-cycle reread pattern

So the problem is not missing material.

The problem is:

```text
Codex-specific activation logic is not explicit enough.
```

## 11. current verdict by usability criteria

### naturalness

`PASS_WITH_NOTE`

Reason:

- Codex is no longer misused as blind execution
- but it still does not feel automatically placed in the flow

### goal-directedness

`PASS_WITH_NOTE`

Reason:

- current purpose exists in the package
- but Codex role is not yet strongly derived from purpose

### continuity

`PASS_WITH_NOTE`

Reason:

- output-return continuity exists conceptually
- but live flow still feels segmented

## 12. practical summary card

```text
현재 판정: Codex 연결은 부분적으로 성공했지만 아직 자연스럽게 흐르지는 않는다
이유: prepare/execute 분리와 validation_return은 잘 잡혔지만, 목적→공정위치→Codex 역할→출력형식의 연결이 아직 약하다
다음 이동: Codex role coupling layer를 명시해 route별 기본 Codex 역할과 출력형식을 고정한다
금지선: Codex를 다시 generic executor로 되돌리거나, 사용자에게 매번 role을 직접 고르게 만들지 않는다
```

## 13. verdict

`PASS_WITH_NOTE`

Reason:

- the package already contains the right primitives
- the missing part is orchestration-level coupling, not conceptual direction

## 14. intentionally not changed

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- `docs/reports/formation_movement_interface_workflow_controller_spec_v0.md`
- any validation case
- Core 7
- object family 5종
- no baseline lock
- no schema enforcement
- no implementation
- no runtime manifest
- no validator/script

## 15. unresolved questions

- how explicit should Codex role mapping become before the system feels too rigid?
- should route-to-role mapping be stable defaults or only soft preferences?
- when should Codex be skipped entirely even if a route usually uses it?
