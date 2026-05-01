# Formation-Movement Interface Space-Process-Routing Diagnostic Note v0

## 1. status

```yaml
status: diagnostic_note
verdict: PASS_WITH_NOTE
purpose: inspect current bottlenecks in space, process, routing, and contract activation using the user's usability criteria
no_package_modification: true
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_runtime_manifest: true
no_validator_or_script: true
```

## 2. diagnostic frame

This note does not ask:

- did the package logic survive?

It asks:

- does the current system feel usable?
- does the space behave like a process field or like a document store?
- does routing reduce operator burden or increase it?
- do contracts activate quickly under variation, or only under familiar cases?

Diagnostic axes:

1. space
2. process
3. routing
4. contract activation

## 3. executive judgment

Compressed diagnosis:

```text
공간은 판독 기록에는 강하지만 공정 순환에는 아직 약하다.
프로세스는 단계는 있으나 default flow가 약하다.
라우팅은 입력 타입은 보지만 공정 위치와 성숙도를 충분히 반영하지 못한다.
계약은 존재하지만 변주 입력에 빠르게 발동되는 mapping layer가 약하다.
```

This means:

- the system is not conceptually broken
- the main bottleneck is orchestration usability, not missing theory

## 4. axis 1: space

### what is working

- the space can preserve provisional objects
- merged external materials can enter as reusable reread-support objects
- outputs can be reread back into the space
- space is no longer only a raw memory dump

Evidence:

- external comparison clusters are preserved with promotion barriers
- complete-cycle note shows output reread back into the space

### what is weak

- space still behaves more strongly as a note/result repository than as a self-evident process field
- entering the space often still means “write another note” rather than “join an already-running circulation path”
- line/axis contact exists, but automatic recirculation remains weak

### diagnosis

```text
공간은 저장소에서 공정장으로 이동 중이지만,
아직 공정장으로서의 기본 흐름이 충분히 자동화되지는 않았다.
```

### verdict

`PASS_WITH_NOTE`

## 5. axis 2: process

### what is working

- the process has real stages:
  - seed
  - reread / framing
  - bounded action
  - execution gate
  - validation return
- input-stage and return-stage are both conceptually defined
- complete-cycle notes show that output-return reread is possible

### what is weak

- the process still depends on explicit operator steering
- there is no strong default path that says:

```text
if input type X and maturity Y, do this next unless blocked
```

- users still feel the segmentation between ingest / compare / space / Codex / reread

### diagnosis

```text
프로세스는 있다.
하지만 “기본 흐름”이 아니라 “수동 조립 가능한 단계 세트”에 더 가깝다.
```

### verdict

`PASS_WITH_NOTE`

## 6. axis 3: routing

### what is working

- routing families are now visible:
  - external material
  - Codex task
  - explanation
  - overlap
  - returned result
- process-first routing improved external material handling
- line-first routing reduced some abstract overclassification

### what is weak

- routing is still too type-centric
- it still under-reads:
  - current process location
  - maturity / ripeness
  - whether Codex is needed as translator, comparer, or executor
- similar inputs with different maturity can still fall into the same route too early

### diagnosis

```text
라우팅은 “무슨 종류의 입력인가”는 보지만,
“지금 공정의 어디쯤 와 있는가”는 아직 덜 본다.
```

### verdict

`PASS_WITH_NOTE`

## 7. axis 4: contract activation

### what is working

- strong contracts now exist:
  - `prepare != execute`
  - `validation_return != final`
  - external material is not auto-evidence
  - `reread_priority / hold / refine` are healthy branches
- under strong and weak cases, these contracts hold

### what is weak

- contracts still activate fastest on familiar examples
- variation mapping is weak:
  a slightly transformed case often needs explicit reread rather than immediate contract application
- this makes the system feel slower than it should

### diagnosis

```text
계약은 있다.
하지만 그 계약을 변주 입력에 빠르게 사상하는 mapping layer가 약하다.
```

### verdict

`PASS_WITH_NOTE`

## 8. strongest current bottlenecks

### bottleneck 1. too much visible segmentation

User-visible feeling:

```text
external ingest / compare / space insertion / Codex / validation 이 다 따로 노는 것 같다
```

Why:

- backend steps are conceptually valid
- but they are still too visible as separate operations

### bottleneck 2. process is richer than front-door

User-visible feeling:

```text
문서는 많고 기준도 있는데, 실제로는 내가 일일이 길게 지시해야 한다
```

Why:

- controller spec exists
- but the operating layer is not yet internalized into default behavior

### bottleneck 3. contract activation is case-shaped

User-visible feeling:

```text
익숙한 사례는 잘 읽는데, 새 변주가 오면 다시 많이 설명해야 한다
```

Why:

- contracts were built from concrete cases
- mapping from new variation to existing contract remains weak

## 9. what this means operationally

The current system should be read as:

```text
framework-rich
controller-light
mapping-weak
```

It is not:

```text
broken
```

It is:

```text
usable but still operator-dependent
```

## 10. what should happen next

This diagnosis suggests:

- do not add new theory first
- do not add new object families
- do not expand Core 7
- do not rush another patch

Instead:

- strengthen default flow behavior
- make routing see process location and maturity
- make contract activation less case-specific
- keep user-facing behavior at 4-line-card level whenever possible

## 11. recommended focus areas

### highest priority

`routing + contract activation`

Why:

- this is where usability pain is most strongly felt
- this is also where improvement can reduce operator burden without changing ontology

### second priority

`space as process field`

Why:

- space should feel like a running circulation path, not only a place where notes accumulate

### lower immediate priority

`new weak-signal documentation`

Why:

- the current bottleneck is not evidence scarcity alone
- it is orchestration and activation

## 12. practical summary card

```text
현재 판정: 구조는 충분하지만 사용성 병목이 있다
이유: 공간은 공정장으로 완전히 작동하지 않고, 프로세스는 기본 흐름이 약하며, 라우팅과 계약 발동이 변주를 빨리 흡수하지 못한다
다음 이동: 공간 / 프로세스 / 라우팅 / 계약발동을 기준으로 default flow와 mapping layer를 보강한다
금지선: 새 이론 추가, Core 7 확장, object family 추가, immediate patch rush 금지
```

## 13. verdict

`PASS_WITH_NOTE`

Reason:

- the current package survived both strong and weak cases
- the problem is no longer primarily conceptual
- the bottleneck is orchestration usability and variation handling

## 14. intentionally not changed

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- any validation case
- any weak-signal document
- `docs/reports/formation_movement_interface_workflow_controller_spec_v0.md`
- Core 7
- object family 5종
- no baseline lock
- no schema enforcement
- no implementation
- no runtime manifest
- no validator/script

## 15. unresolved questions

- how much routing should depend on process location vs input type?
- what is the minimum mapping layer needed for faster contract activation?
- how can space feel more like a process field without exposing more internal complexity to the user?
