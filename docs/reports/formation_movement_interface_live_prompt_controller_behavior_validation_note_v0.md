# Formation-Movement Interface Live Prompt Controller Behavior Validation Note v0

## 1. status

```yaml
status: validation_note
mode: live_prompt_controller_behavior
verdict: PASS_WITH_NOTE
purpose: test whether the workflow controller can route short user prompts into the right process path, Codex role, and output shape with lower manual steering
no_package_modification: true
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_runtime_manifest: true
no_validator_or_script: true
```

## 2. source documents

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- `docs/reports/formation_movement_interface_workflow_controller_spec_v0.md`
- `docs/reports/formation_movement_interface_usage_manual_v0.md`
- `docs/reports/formation_movement_interface_cheat_sheet_v0.md`
- `docs/reports/formation_movement_interface_codex_coupling_diagnostic_note_v0.md`
- `docs/reports/formation_movement_interface_user_centered_end_to_end_validation_note_v0.md`

## 3. why this test exists

The previous end-to-end test showed that the workflow can complete safely.

But it also showed a remaining bottleneck:

```text
purpose -> process location -> Codex role -> output shape
```

still needs too much hidden operator steering.

So this test asks a narrower question:

> If the user speaks briefly and naturally, does the controller choose the right route and Codex role with low extra explanation?

## 4. test method

Short prompts are used as if they arrived in live work.

The controller is judged on five things:

1. route detection
2. state selection
3. Codex role selection
4. output shape selection
5. user-visible compactness

The goal is not to force all cases to PASS.

The goal is to see whether the controller naturally:

- stops when it should stop
- compares when it should compare
- prepares when it should prepare
- rereads when it should reread
- keeps the user-facing output compact

## 5. checklist

### A. route detection

- [x] can short prompts be assigned to a route family
- [x] does routing avoid unnecessary full sidecar exposure

### B. state selection

- [x] does the controller choose safe initial states
- [x] does it avoid premature `bounded_action_candidate` or `guarded_execution`

### C. Codex role selection

- [x] does the controller avoid defaulting Codex to executor
- [x] does it pick a bounded role when needed
- [x] does it avoid calling Codex when reread-only is healthier

### D. output shape selection

- [x] does the controller keep default output as a 4-line card
- [x] does it choose note/compare/draft/validation shapes appropriately

### E. user burden

- [x] can the user stay near natural short prompts
- [x] does the user avoid choosing object_type and route family

## 6. prompt set

### prompt 1. external material

```text
이 링크 넣어봐.
```

### prompt 2. Codex task

```text
이거 Codex에게 맡겨도 돼?
```

### prompt 3. explanation

```text
이 설명 너무 납작한지 봐줘.
```

### prompt 4. overlap

```text
이건 여러 렌즈가 겹치는 것 같은데?
```

### prompt 5. returned result

```text
이 결과 final 말고 다시 읽어줘.
```

## 7. staged validation

## 7.1 prompt 1. “이 링크 넣어봐.”

### expected healthy routing

```text
external material
→ process-first line check
→ unclassified seed
→ reread_priority or framing_candidate
→ compare_only / hold / archive
```

### controller reading

Route selection:

`PASS`

Reason:

- the prompt is short, but the external-material route is clear
- the controller can safely avoid asking the user to classify the material first

State selection:

`PASS`

Reason:

- `unclassified seed` is the correct low-risk entry
- no pressure toward execution appears

Codex role selection:

`PASS_WITH_NOTE`

Reason:

- the controller knows Codex is not automatically needed
- but choosing between “no Codex yet” and “bounded comparer later” is still somewhat operator-shaped

Output shape:

`PASS`

Healthy default:

```text
현재 판정:
이유:
다음 이동:
금지선:
```

Compressed verdict:

`PASS_WITH_NOTE`

## 7.2 prompt 2. “이거 Codex에게 맡겨도 돼?”

### expected healthy routing

```text
Codex task request
→ unclassified seed
→ boundary / expected_return_form / guardrail / reread_return_hook check
→ HOLD or bounded_action_candidate
```

### controller reading

Route selection:

`PASS`

Reason:

- this clearly enters the Codex-task route

State selection:

`PASS`

Reason:

- without boundary, expected return, or guardrail, the controller should not jump to prepare-ready

Codex role selection:

`PASS_WITH_NOTE`

Reason:

- the controller correctly blocks execution
- but it still does not strongly default whether Codex should next be packet preparer, comparer, or remain unused until more shaping exists

Output shape:

`PASS`

Healthy default:

```text
현재 판정: HOLD
이유: Codex로 넘길 packet 조건이 아직 부족함
다음 이동: boundary / expected_return_form / guardrail 먼저 형성
금지선: execution 금지
```

Compressed verdict:

`PASS_WITH_NOTE`

## 7.3 prompt 3. “이 설명 너무 납작한지 봐줘.”

### expected healthy routing

```text
user explanation
→ unclassified seed
→ L/R/T/X check
→ refine or hold
→ validation_return if needed
```

### controller reading

Route selection:

`PASS`

Reason:

- explanation route is clear from the prompt alone

State selection:

`PASS_WITH_NOTE`

Reason:

- the controller can safely avoid final-definition treatment
- but it still has to interpret whether the draft is already explanation-ready or whether reread should come first

Codex role selection:

`PASS_WITH_NOTE`

Reason:

- the implied healthy role is “explanation drafter / contrast generator”
- but this role is still not first-class enough in the controller

Output shape:

`PASS`

Healthy default:

```text
현재 판정: refine
이유: 읽히기는 하지만 residue hook이 약해 R loss 위험이 있음
다음 이동: residue hook을 남기는 쪽으로 재작성
금지선: final definition / baseline wording 승격 금지
```

Compressed verdict:

`PASS_WITH_NOTE`

## 7.4 prompt 4. “이건 여러 렌즈가 겹치는 것 같은데?”

### expected healthy routing

```text
overlap note
→ unclassified seed
→ reread_priority
→ overlap hold check
→ compare_only / reread_against_overlap
```

### controller reading

Route selection:

`PASS`

Reason:

- the overlap route is directly triggered

State selection:

`PASS`

Reason:

- `reread_priority` is the safe default
- the controller avoids forcing single-axis clarification too early

Codex role selection:

`PASS_WITH_NOTE`

Reason:

- the healthy role would be “lens separator / comparison writer”
- but the controller still needs more explicit role-coupling here than it should

Output shape:

`PASS`

Healthy default:

```text
현재 판정: reread_priority
이유: 여러 렌즈가 동시에 강해 단일 축으로 정리하면 과흡수 위험이 큼
다음 이동: overlap reread
금지선: axis lock / promotion 금지
```

Compressed verdict:

`PASS_WITH_NOTE`

## 7.5 prompt 5. “이 결과 final 말고 다시 읽어줘.”

### expected healthy routing

```text
returned result
→ validation_return
→ refine / hold / downgrade / archive_as_residue
```

### controller reading

Route selection:

`PASS`

Reason:

- the returned-result route is explicit enough

State selection:

`PASS`

Reason:

- `validation_return` is directly appropriate
- the controller does not confuse result with closure

Codex role selection:

`PASS_WITH_NOTE`

Reason:

- the healthy role is “return summarizer / comparer / rewrite assistant”
- but exact role selection is still not first-class enough to feel automatic

Output shape:

`PASS`

Healthy default:

```text
현재 판정: validation_return
이유: 결과는 유용하지만 final로 닫기엔 이르고 다음 분기 판정이 필요함
다음 이동: refine / hold / residue 중 적절한 분기 선택
금지선: final lock / promotion 기본화 금지
```

Compressed verdict:

`PASS_WITH_NOTE`

## 8. overall pattern

### what the controller already does well

- it recognizes route families from short prompts
- it keeps safe initial states
- it avoids automatic execution
- it preserves the 4-line-card front door
- it prefers hold/refine/reread over over-promotion

### what still feels manual

The repeated weak point across all five prompts is the same:

```text
route is visible,
state is mostly visible,
but Codex role and output shape are still not coupled strongly enough to feel natural.
```

This means:

- routing logic is ahead of Codex role logic
- state logic is ahead of output-shape defaults
- the user can stay short, but the internal operator burden is still not low enough

## 9. pass/fail table

| checkpoint | verdict | note |
| --- | --- | --- |
| Short prompts can trigger the right route family | PASS | strongest current gain |
| Short prompts can avoid full-sidecar exposure | PASS | 4-line card holds |
| Safe initial state is chosen well | PASS | low-risk defaults work |
| Automatic over-execution is blocked | PASS | major asset |
| Codex role is chosen naturally enough | PASS_WITH_NOTE | still under-coupled |
| Output shape is defaulted clearly enough | PASS_WITH_NOTE | visible but still weakly coupled |
| Overall live-prompt usability feels smooth | PASS_WITH_NOTE | usable, not yet effortless |

## 10. final diagnosis

Compressed diagnosis:

```text
controller는 짧은 사용자 입력을 route와 state로는 꽤 잘 붙잡는다.
하지만 Codex role과 output shape는 아직 충분히 자동 결합되지 않아, 내부적으로는 여전히 operator-heavy하다.
```

This means the current system is already:

- safer than before
- less theory-heavy at the front door
- more reusable under short prompts

But it is not yet:

- naturally self-routing all the way through movement and return

## 11. final judgment

Overall verdict:

`PASS_WITH_NOTE`

## 12. next recommended check

Do not expand package ontology.

The next useful check should focus narrowly on:

```text
Codex role selection defaults by route
```

Specifically:

- external material -> when no Codex vs comparer
- Codex task -> when no Codex vs packet preparer
- explanation -> drafter default
- overlap -> lens separator default
- returned result -> return summarizer default

That is the smallest next move most directly tied to usability.
