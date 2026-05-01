# Formation-Movement Interface User Surface Explanation Validation Case v0

Date: 2026-04-24

## 1. status

- `validation_case`
- `dry_run_only`
- `no package modification`
- `no baseline lock`
- `no schema enforcement`
- `no implementation`
- `no final definition promotion`

Source package:

- `docs/reports/formation_movement_interface_package_draft_v0.md`

Validation target:

- Test whether the package can handle user-surface explanation without flattening the space into a generic tool description.
- Test whether the package can separate L/R/T/X overlap, keep User Surface to a 3-4 line judgment card, and return explanation drafts as validation material rather than final wording.

## 2. case setup

Chosen question:

> 통합엔진이 뭐야?

Scenario:

- A user asks for the meaning of the integrated engine.
- The goal is to produce a user-surface explanation the user can understand.
- The explanation must not become final definition, baseline wording, or product slogan.
- The output is only a `user_surface_explanation_draft`, to be recovered later as validation material.

Boundary:

- No package modification.
- No baseline wording.
- No final definition promotion.
- No execution or worker handoff.

## 3. seed sidecar application

Operational minimum only:

```text
current_purpose: 통합엔진을 사용자면에서 3-4줄로 설명할 수 있는지 확인
source_trace: formation_movement_interface_package_draft_v0 + current conversation
initial_boundary: final definition 금지, baseline wording 금지, user surface draft만 허용
object_type: unclassified
```

Validation points:

- PASS: seed stage does not force `object_type`.
- PASS: the user does not fill Core 7.
- PASS: user input stays at `current_purpose`, `source_trace`, and `initial_boundary` level.

## 4. formed sidecar application

VectorFL rereads the explanation request and assigns provisional identity.

Dry-run judgment:

```text
object_type: bounded_action_candidate
provisional_status: explanation_draft_candidate / PASS_WITH_NOTE
boundary: user-surface explanation draft only; no baseline wording; no final definition; no product slogan
next_allowed_move: prepare_user_surface_draft
needed_reread_question: Is the main failure mode lens mismatch (L), residue loss (R), immaturity (T), or translation weakness (X)?
candidate_role: user_surface_explanation_draft candidate
source_trace: formation_movement_interface_package_draft_v0 + current conversation
```

Reasoning:

- `reread_priority` is plausible if the concept is too immature.
- `framing_candidate` is plausible if the work is only conceptual framing.
- `bounded_action_candidate` is the best fit here because a bounded explanation draft can be produced without execution.

Formed-sidecar questions:

- Can this move directly to a user-surface draft?
- Or is the concept still immature enough to remain reread-only?
- If the explanation fails, is the center of failure L, R, T, or X?
- If the explanation is too internal, is that an L failure?
- If the explanation is too easy, is that R loss / flattening?
- If the concept wobbles, is that T?
- If the expression structure is missing, is that X?

## 5. explanation candidate comparison

### A. internal-language-heavy explanation

Draft:

> 통합엔진은 사용자면, VectorFL면, 엔진면을 따라 목적-형성-운동을 연결하고, line/relation/gap/pending/reflux를 intermediate formation으로 읽은 뒤 process/validate/trace-memory-return으로 회수하는 구조다.

Judgment:

- L suitability: FAIL
- R preservation: PASS
- T stability: PASS_WITH_NOTE
- X transformation quality: FAIL
- user surface suitability: FAIL
- promotion forbidden: PASS

Reason:

The structure is accurate, but it stays too close to internal body language. It misses the user-facing camera position.

### B. over-flattened easy explanation

Draft:

> 통합엔진은 네 생각을 정리하고 AI 작업을 연결해 주는 도구야.

Judgment:

- L suitability: PASS
- R preservation: FAIL
- T stability: PASS_WITH_NOTE
- X transformation quality: PASS_WITH_NOTE
- user surface suitability: PASS_WITH_NOTE
- promotion forbidden: PASS

Reason:

The user can understand it, but the explanation collapses the system into a generic note/automation tool. It loses intermediate layer, reread, provisionality, and return structure.

### C. balanced explanation

Draft:

> 통합엔진은 네가 지금 풀고 싶은 일을 바로 실행으로 넘기지 않고, 먼저 중간 구조로 읽고 정리한 뒤 필요한 작업만 조심스럽게 움직이게 해 주는 운영 구조야.  
> 그래서 그냥 자동화 도구라기보다, 지금 목적에 맞게 자료와 판단을 다시 읽고, 실행 결과도 다시 검토 재료로 돌려보내는 시스템에 가까워.  
> 즉 생각을 정리하는 층과 실제 작업을 움직이는 층을 이어 주되, 성급한 확정 없이 단계적으로 다루게 만드는 엔진이라고 보면 돼.

Judgment:

- L suitability: PASS
- R preservation: PASS_WITH_NOTE
- T stability: PASS_WITH_NOTE
- X transformation quality: PASS
- user surface suitability: PASS
- promotion forbidden: PASS

Reason:

The draft stays readable from the user camera while leaving a trace of intermediate layer, reread, and non-final movement. It is still a draft, not a locked definition.

## 6. surface-specific visibility application

### A. User Surface judgment card

```text
현재 판정: 통합엔진 설명은 가능하지만, 최종 정의가 아니라 사용자면 초안으로만 둡니다.
이유: 너무 내부적으로 말하면 L 실패이고, 너무 쉽게 말하면 R 손실이 생깁니다.
다음 이동: 균형 설명 초안을 validation_return으로 회수해 다시 읽습니다.
금지선: baseline wording, final definition, product slogan 승격은 금지입니다.
```

Check:

- PASS: User Surface stays to 4 lines.

### B. VectorFL Surface view

```text
object_type: bounded_action_candidate
provisional_status: explanation_draft_candidate / PASS_WITH_NOTE
boundary: user-surface draft only; no final definition; no baseline wording
needed_reread_question: Is the explanation failure centered on L, R, T, or X?
candidate_role: user_surface_explanation_draft candidate
L/R/T/X assessment: A = L failure, B = R-loss/flattening, C = balanced but still provisional
flattening risk: high for B, medium-low for C, low relevance for A because A fails before flattening
source_trace: formation_movement_interface_package_draft_v0 + current conversation
next_allowed_move draft: validate_balanced_explanation_draft
```

Check:

- PASS: full formation reading remains on VectorFL surface.

### C. Engine Surface view

No execution in this case.

```text
action_shape 후보: user_surface_explanation_draft
execution_constraint: no execution / draft only
guardrail: no final definition / no baseline wording / no product slogan
expected_return_form 후보: balanced explanation draft + L/R/T/X assessment + flattening risk note
fallback_policy 필요 여부: low, but useful if explanation collapses into internal jargon or generic tool language
trust_scope 필요 여부: optional note only; draft is not executable and not promotable
reread_return_hook: return draft to VectorFL as validation material
```

Check:

- PASS: engine-facing view marks this as draft-only, not executable.

### D. Return / Validation Surface view

Short validation return based on explanation C:

```text
observed_result: A balanced user-surface explanation draft is possible without forcing final definition or losing all intermediate-layer signal.
reread_trigger: Recheck whether the draft preserves enough residue to avoid collapsing into generic note/automation language.
next_recommended_state: refine balanced explanation draft; keep as user_surface_explanation_draft candidate
```

Check:

- PASS: short return is enough for this dry-run.

## 7. flattening / R-loss check

Required questions:

- Did the explanation become too easy and lose distinctiveness? Yes, explanation B did.
- Did at least one of intermediate layer, reread, provisionality, or residue survive in user language? Yes, explanation C preserved intermediate reading, reread, and staged movement.
- Is there a hook for going deeper later? Yes, explanation C leaves a path back to structure and reread.
- Did the system collapse into "just a note tool" or "just an AI automation tool"? Yes, B did.
- If R loss is strong, should the return branch be refine or hold? `refine` is correct here because a better explanation candidate already exists; hold is unnecessary.

Judgment:

`PASS_WITH_NOTE`

Reason:

Flattening risk is real, but the package can detect it and keep the better explanation draft provisional.

## 8. short / full validation return judgment

Short validation return is used by default here:

```text
observed_result
reread_trigger
next_recommended_state
```

Full validation return would be needed if:

- the explanation starts looking like final definition
- it risks being reused as baseline wording
- R loss / flattening is severe and ambiguous
- it becomes unclear whether the failure is L, T, X, or R
- user-surface wording conflicts with engine/VectorFL explanation
- the draft is likely to be inserted into package documents
- the explanation is strong enough to alter how the space / integrated engine relation is understood

Dry-run judgment:

`PASS_WITH_NOTE`

Short return is enough now because the explanation remains a draft and does not change package state. If explanation C were about to be reused as canonical wording, full validation return would be required.

## 9. transition check

| transition | verdict | reason |
| --- | --- | --- |
| unclassified seed -> formed sidecar | PASS | Seed used only operational minimum; VectorFL attached provisional identity. |
| formed sidecar -> reread_priority / framing_candidate / bounded_action_candidate | PASS_WITH_NOTE | `bounded_action_candidate` works because a bounded explanation draft is possible, but T/L/X ambiguity remains relevant. |
| explanation candidate -> user surface draft | PASS | Explanation C can move as a user-surface draft. |
| user surface draft -> validation_return | PASS | Draft can return as validation material without execution. |
| validation_return -> refine / hold / downgrade / archive_as_residue / promote 금지 | PASS_WITH_NOTE | `refine` is the right branch; promotion remains forbidden. |

## 10. operator cost check

Required questions:

- User-filled fields: 3 fields at seed stage: `current_purpose`, `source_trace`, and `initial_boundary` / `why_now`.
- Did the user choose `object_type`? No.
- Was Core 7 required from the user? No.
- Did User Surface show only a 3-4 line judgment card? Yes.
- Was explanation candidate comparison handled as VectorFL reading rather than user burden? Yes.
- Was the explanation over-promoted to final definition? No.

Cost verdict:

`PASS`

Reason:

The package keeps the evaluation burden in VectorFL. The user sees only the judgment card and the resulting explanation draft, not the classification machinery.

## 11. verdict

`PASS_WITH_NOTE`

Reason:

The package can handle user-surface explanation as a provisional object without turning the explanation into a final definition. It successfully separates internal-language failure, flattening failure, and balanced-draft success, but the exact boundary between R loss and acceptable simplification still needs more repetition.

## 12. findings

### What worked

- Seed stage stayed lightweight.
- `object_type` assignment stayed on VectorFL surface.
- Explanation A/B/C comparison made L and R failure visible.
- Explanation C preserved some structural residue without losing user readability.
- User Surface remained compact.
- Short validation return was sufficient for a no-execution draft case.

### What was too heavy

- Full L/R/T/X assessment is too heavy for User Surface, but it stayed where it belongs.
- Explanation C still carries enough structure that some users may need a second follow-up simplification.

### What remained ambiguous

- The line between acceptable simplification and R loss is still judgment-heavy.
- T and X may still blur together when a concept is both immature and hard to express.
- It is not fully clear when a strong explanation draft becomes risky enough to require full validation return.

### What should not be changed yet

- Do not change Core 7.
- Do not turn explanation draft into baseline wording.
- Do not add a new explanation-specific object family.
- Do not modify the package from this single dry-run.

### What may need a later package patch

- Add a small note for when user-surface explanation should default to full validation return.
- Add one or two more explanation examples showing acceptable simplification vs flattening.
- Add a short heuristic for when R loss should force `hold` rather than `refine`.

## 13. no-change rule

This report does not modify the package document.

Recommended future patches are listed only as future candidates. They are not applied here.

## 14. intentionally not changed

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- No baseline lock
- No schema enforcement
- No implementation
- No runtime manifest
- No validator or script
- No final definition promotion

## 15. unresolved questions

- Where exactly is the line between acceptable simplification and R loss?
- When should explanation draft ambiguity between L/T/X require full validation return?
- Should user-surface explanation default to `bounded_action_candidate`, or should immature cases stay `reread_priority` longer?
- When does a strong explanation draft become risky enough that it must not remain short-return only?
- What is the smallest user-language trace of intermediate layer / reread / provisionality that still prevents flattening?
