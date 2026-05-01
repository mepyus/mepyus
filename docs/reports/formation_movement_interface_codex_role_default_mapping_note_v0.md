# Formation-Movement Interface Codex Role Default Mapping Note v0

## 1. status

```yaml
status: mapping_note
focus: codex_role_default_by_route
verdict: PASS_WITH_NOTE
purpose: narrow the usability bottleneck by defining safer default Codex roles per route without expanding package structure
no_package_modification: true
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_runtime_manifest: true
no_validator_or_script: true
no_core7_expansion: true
no_object_family_expansion: true
```

## 2. why this note exists

The recent live-prompt test showed:

- route detection is mostly stable
- safe state selection is mostly stable
- user-facing 4-line closure is stable

But the same weak point repeated:

```text
purpose -> process location -> Codex role -> output shape
```

So this note does not add new ontology.

It only narrows one usability problem:

> when a route is already visible, what should Codex be by default?

Important terminology correction:

`no Codex` is not precise in this workspace.

Codex is already acting as interpreter, space/process reader, and user-facing output generator.

So this note should distinguish:

```text
Codex interpreter/output mode
```

from:

```text
Codex worker-role elevation
```

The corrected question is:

```text
should Codex stay in interpreter/output mode,
or be elevated into a bounded worker role?
```

## 3. source context

- `docs/reports/formation_movement_interface_workflow_controller_spec_v0.md`
- `docs/reports/formation_movement_interface_codex_coupling_diagnostic_note_v0.md`
- `docs/reports/formation_movement_interface_live_prompt_controller_behavior_validation_note_v0.md`
- `docs/reports/formation_movement_interface_package_draft_v0.md`

## 4. top-level rule

Codex should not be defaulted to execution.

The first default question is:

```text
does this route require Codex worker-role elevation now?
```

Only after that:

```text
if elevation is needed, what is the safest worker role?
```

## 5. route-by-route default mapping

## 5.1 route A. external material

### default state tendency

```text
unclassified seed
→ reread_priority or framing_candidate
```

### default Codex operating mode

```text
interpreter/output mode only
```

### when Codex role elevation becomes appropriate

Only when the material has already stabilized enough for:

- bounded comparison
- contrastive reread
- scene-by-scene internal contact check

Then:

```text
elevate Codex to bounded comparer
```

### default output shape

If interpreter/output mode only:

```text
4-line judgment card
```

If elevated to bounded comparer:

```text
comparison note
```

### guardrail

Do not move directly from external material to:

- executor
- doctrine importer
- evidence locker

### compressed rule

```text
external material는 기본적으로 interpreter/output mode에 머문다.
필요할 때만 bounded comparer로 승격한다.
```

## 5.2 route B. Codex task request

### default state tendency

```text
unclassified seed
→ HOLD or bounded_action_candidate
```

### default Codex operating mode

```text
gatekeeping interpreter mode
```

Reason:

The route is about possible worker-role elevation, not automatic Codex invocation.

### when Codex role elevation becomes appropriate

If the request has:

- boundary
- expected_return_form
- guardrail
- reread_return_hook

Then:

```text
elevate Codex to packet preparer
```

Only after execution constraints also exist:

```text
elevate Codex to executor
```

### default output shape

Before readiness:

```text
HOLD card
```

When ready for preparation:

```text
packet draft + blockers
```

When truly execution-ready:

```text
bounded execution result
→ validation_return
```

### guardrail

Never collapse:

```text
Codex task request = call Codex now
```

### compressed rule

```text
Codex task route는 기본적으로 gatekeeping interpreter mode.
조건이 생기면 packet preparer로 승격.
실행은 마지막 단계.
```

## 5.3 route C. user explanation request

### default state tendency

```text
unclassified seed
→ refine-oriented bounded_action_candidate or hold
```

### default Codex worker role

```text
elevate Codex to drafter
```

Reason:

This route is inherently about translation / reformulation / explanation shaping.

### default output shape

```text
2-3 explanation variants
+ flattening note
+ recommended branch
```

### when to avoid Codex

If the material is still too unripe and explanation would force flattening:

```text
interpreter/output mode only
→ reread / hold first
```

### guardrail

Do not default to:

- final definition
- baseline wording
- single polished answer with no residue note

### compressed rule

```text
explanation route는 기본적으로 drafter 승격이 자연스럽다.
다만 아직 덜 익었으면 worker-role 승격을 미루고 interpreter/output mode에 머문다.
```

## 5.4 route D. overlap-heavy note

### default state tendency

```text
unclassified seed
→ reread_priority
```

### default Codex operating mode

```text
interpreter/output mode only
```

### when Codex role elevation becomes appropriate

Only when separation work is bounded enough:

- lens separation
- comparative reread
- overlap decomposition note

Then:

```text
elevate Codex to lens separator
```

### default output shape

If interpreter/output mode only:

```text
hold / reread card
```

If elevated to lens separator:

```text
lens-separated reread note
```

### guardrail

Do not use Codex here to force:

- single-axis cleanup
- premature synthesis
- strong wording lock

### compressed rule

```text
overlap route는 기본적으로 interpreter/output mode에 머문다.
필요할 때만 lens separator로 승격한다.
```

## 5.5 route E. returned result

### default state tendency

```text
validation_return
→ refine / hold / downgrade / archive_as_residue
```

### default Codex worker role

```text
elevate Codex to return summarizer
```

### possible secondary role

If the result must be contrasted against expectation or rewritten for reread:

```text
elevate Codex to comparer / rewrite assistant
```

### default output shape

```text
short validation return
```

Escalate only when needed to:

```text
full validation return
```

### guardrail

Do not use returned result route to silently turn:

- result into final closure
- summary into promotion

### compressed rule

```text
returned result route는 기본적으로 return summarizer.
필요하면 comparer나 rewrite assistant.
```

## 6. default mapping table

| route | safest default Codex mode / elevation | fallback if too early | typical output shape |
| --- | --- | --- | --- |
| external material | interpreter/output mode / bounded comparer later | reread_only | 4-line card / comparison note |
| Codex task request | gatekeeping interpreter mode / packet preparer later | HOLD | HOLD card / packet draft + blockers |
| user explanation | drafter elevation | hold first if too unripe | 2-3 explanation variants + flattening note |
| overlap-heavy note | interpreter/output mode / lens separator later | reread_priority | hold card / lens-separated reread note |
| returned result | return summarizer elevation | comparer or rewrite assistant if needed | short validation return / full validation return |

## 7. what this improves

This mapping makes three things clearer:

### A. Codex is not the same across routes

The same tool should not appear as:

- executor everywhere
- generic “analyze this” helper everywhere

### B. no worker-role elevation is a real default

Some routes are healthier when Codex stays in interpreter/output mode.

That is not failure.

That is proper coupling.

### C. output shape should follow route

The controller should not only choose whether Codex is called.

It should also choose what the Codex return should look like.

## 8. current usability gain

With this mapping, the user can stay close to short prompts like:

```text
이 링크 넣어봐
이거 Codex에게 맡겨도 돼?
이 설명 너무 납작한지 봐줘
이건 렌즈가 겹쳐 보이는데?
이 결과 final 말고 다시 읽어줘
```

while the controller more safely assumes:

- not all routes require worker-role elevation now
- not all Codex-task routes want execution
- different routes want different output shapes

## 9. remaining weak point

This note clarifies role defaults.

It does not yet fully solve:

```text
how route maturity upgrades the role automatically
```

Examples still needing more evidence:

- when external material crosses from no-Codex to comparer
- when explanation crosses from hold to drafter
- when overlap crosses from reread-only to lens separator

## 10. final judgment

Compressed judgment:

```text
Codex의 기본 operating mode와 worker-role elevation을 route별로 분리하면 controller의 수동 조향 부담이 꽤 줄어든다.
다만 role elevation timing은 아직 더 많은 실제 사례가 필요하다.
```

Overall verdict:

`PASS_WITH_NOTE`

## 11. recommended next use

Use this mapping as a controller-side default note.

Do not treat it as:

- final routing contract
- implementation instruction
- schema
- hard lock

The next useful live test should ask:

```text
in one real task, does the controller now keep Codex in the safer operating mode or elevate it into the right worker role without extra prompting?
```
