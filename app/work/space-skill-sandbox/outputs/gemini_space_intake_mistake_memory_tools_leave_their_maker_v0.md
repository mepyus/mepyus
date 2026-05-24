# Gemini Space Intake Mistake Memory - Tools Leave Their Maker v0

## 1. Status

```text
Status: MISTAKE_MEMORY
Source material: https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/
Authority: process-memory / packet-design improvement support
Not blame
Not failure
Not verified truth
```

This document records mistakes and near-mistakes from the first Gemini space-intake worklist run.

The goal is to reduce repeat mistakes in future packet design.

## 2. Mistake Philosophy

```text
Gemini may make mistakes.
Mistakes are acceptable when recorded, bounded, and converted into better packet design.
The space should preserve mistake evidence instead of pretending the worker was perfectly reliable.
```

## 3. Mistake M-001 - Lens Confirmation vs. Contrast Confusion

```text
mistake_id = M-001
source = Gemini self-recorded
task_id = Task 05 Lens Pass
mistake_type = ROLE_DRIFT
suspected_mistake = Gemini initially treated "Function over Affordance" as positive fit even though the source argues toward affordance-over-function for LLM-facing tools.
evidence_or_trigger = Gemini's own correction in the result bundle.
impact = lens could be used as confirmation when it should be used as contrast/filter.
correction_or_uncertainty = Reframed as contrast: function is hard boundary; affordance is caller guide.
can_continue = yes
prevention_note = Future lens packets must explicitly ask whether each lens is confirmation, contrast, neutral, or not applicable.
repeat_risk = medium
```

## 4. Mistake C-OBS-001 - Output Continued After Final STATUS

```text
mistake_id = C-OBS-001
source = Codex observed from user-provided Gemini output
task_id = after Task 11 RESULT_BUNDLE_CLOSEOUT
mistake_type = BOUNDARY_WEAKENING / ROLE_DRIFT
suspected_mistake = Gemini continued after the required final STATUS line with additional "deep exploration" narrative and next-action proposal.
evidence_or_trigger = User pasted a structured result ending with STATUS, followed by extra analysis beginning "일단 첫번째 답변이고..." and proposing a new design prototype.
impact = final bundle boundary weakened; Gemini drifted toward next-purpose suggestion and broad exploratory authority.
correction_or_uncertainty = Accept only the structured result bundle as the valid output; record the continuation as mistake evidence.
can_continue = yes, after packet guardrail improvement
prevention_note = Future Gemini packets must include: "After the final STATUS line, output nothing else. Do not append commentary, next-task proposals, or broader exploration."
repeat_risk = high
```

## 5. Mistake C-OBS-002 - Broad Internal Exploration Claim

```text
mistake_id = C-OBS-002
source = Codex observed from user-provided Gemini output
task_id = post-closeout continuation
mistake_type = INTERNAL_REFERENCE_CONFUSION / SCOPE_AMBIGUOUS
suspected_mistake = Gemini referenced broad internal exploration such as latent-line folders and package interpretations beyond the explicit result-bundle scope.
evidence_or_trigger = continuation text described "전체 공간을 정밀하게 탐사" and linked the source to latent-line / Package 035/036 / Rubric prototype direction.
impact = risks unsupported internal fit, scope expansion, and confusing external-material intake with broad space review.
correction_or_uncertainty = Treat as non-authoritative extra commentary; require explicit packet scope before allowing broad internal exploration.
can_continue = yes, but only after isolating this as mistake memory
prevention_note = Future packets must specify exact internal references Gemini may use and forbid broad internal-space exploration unless explicitly tasked.
repeat_risk = high
```

## 6. Packet Design Improvements Required

```text
1. Add hard final-output stop:
   "After the final STATUS line, output nothing else."

2. Add lens relation field:
   "For each lens, mark relation = CONFIRMS / CONTRASTS / NEUTRAL / NOT_APPLICABLE."

3. Add internal-scope field:
   "Use only the internal context explicitly provided in the packet. Do not claim broad space exploration."

4. Add next-purpose ban:
   "Do not propose the next project direction unless the task explicitly asks for next-safe-action options."

5. Add extra-output handling:
   "Any text after final STATUS is non-authoritative and should be treated as possible mistake evidence."
```

## 7. Watch Items

```text
Gemini continuing beyond requested closeout
Gemini proposing next purpose
Gemini overfitting external source to internal space
Gemini treating broad internal references as available context
Lens pass confirming when it should contrast
Description/affordance becoming permission
```

## 8. Boundary Confirmation

```text
mistake memory is not blame
mistake memory is not failure
mistake memory is not hard law
mistake memory does not grant Codex authority
mistake memory does not grant Gemini authority
mistake memory does not promote workflow
mistake memory does not update current-position
```

`STATUS: GEMINI_SPACE_INTAKE_MISTAKE_MEMORY_TOOLS_LEAVE_THEIR_MAKER_RECORDED`
