# Gemini Worklist - External Reference Materials Deep Reread v0

## 0. Mode

This is a bounded Gemini reread worklist.

Gemini should read the reference materials created from the four-source external candidate round and return worker evidence.

Do not implement anything.
Do not adopt any source.
Do not recommend implementation.
Do not create automation.
Do not create runtime scripts.
Do not clone, install, run, or execute any repo.
Do not create registry, index, ledger, router, controller, formal schema, official workflow, or baseline.
Do not update current-position.
Do not attach any tool/API/function/repo.
Do not treat this reread as project truth.

Return evidence, uncertainty, watch items, and suggested next safe action only.

## 1. Purpose

The purpose is to reread the external reference materials more deeply as a reference set.

The goal is not:

```text
Which tool should we adopt?
```

The goal is:

```text
How can this reference set help the space recognize future tool/repo/API/function/agent candidates?
Which signals are reusable?
Which signals are only context?
Which signals should remain watch-only?
Which references should be retrieved under which natural trigger?
Where could the reference set be overread?
```

## 2. Source Materials to Read

Read in this order:

```text
1. docs/reports/external_candidate_reference_materials_list_v0.md
2. docs/reports/external_candidate_four_source_round_closeout_v0.md
3. docs/reports/external_candidate_four_source_cross_synthesis_v0.md
4. docs/reports/external_candidate_context_mode_reading_packaging_v0.md
5. docs/reports/external_candidate_ouroboros_reading_packaging_v0.md
6. docs/reports/external_candidate_gomodel_reading_packaging_v0.md
7. docs/reports/external_candidate_ai_frontier_ep94_reading_packaging_v0.md
```

Use only these documents unless the User explicitly provides more material.

Do not browse externally.

Do not reopen the original external sources unless explicitly asked.

## 3. Reading Frame

Treat all materials as:

```text
REFERENCE_MATERIAL_ONLY
worker evidence + Codex packaging
not project authority
not implementation target
not official workflow
not registry/index/ledger
```

Use the four-source conclusion as the main frame:

```text
Do not chase tools directly.
Strengthen the internal process grammar that separates:
- context from action
- plan from execution
- evidence from authority
- strategy from implementation
```

## 4. Task List

### Task 01 - Source Coverage Check

Confirm the seven documents were readable.

Return:

```text
read_status:
missing_sources:
blocked_sources:
uncertainty:
```

Stop with `STATUS: SOURCE_ACCESS_BLOCKED` if required local documents are missing.

### Task 02 - Reference Role Verification

Verify the intended role of each source:

```text
context-mode
ouroboros
GoModel
AI Frontier EP94
cross-source synthesis
round closeout
reference materials list
```

For each, return:

```text
material:
correct_role:
evidence:
must_not_become:
uncertainty:
```

### Task 03 - Reusable Signal Extraction

Extract reusable signals.

At minimum evaluate:

```text
Context / Resource containment
Execution boundary / Tool-side containment
Ambiguity / Plan-before-execution
Evidence packaging / evaluation
Model/tool volatility and model-agnosticism
Brain / Hand decoupling
User-as-Judge reinforcement
```

For each signal, return:

```text
signal:
supported_by:
what_it_helps_notice:
when_to_retrieve:
must_not_become:
confidence:
uncertainty:
```

Allowed confidence values:

```text
HIGH
MEDIUM
LOW
UNKNOWN
```

### Task 04 - Natural Trigger Map

Build a map of when each reference should be retrieved in future work.

Use these trigger categories:

```text
new external tool/repo/API/Skill candidate
context vs action boundary unclear
plan vs execution boundary unclear
worker evidence packaging problem
execution-side provider/tool boundary issue
model/tool volatility pressure
User asks whether to adopt/ignore/hold a tool
Codex/Gemini/worker role split unclear
```

For each trigger, return:

```text
trigger:
first_reference_to_read:
optional_second_reference:
why:
what_to_avoid:
```

### Task 05 - Overread / Drift Risk Scan

Scan for places where the reference set could be overread.

At minimum check:

```text
reference list becoming registry/index
operation reference becoming implementation plan
strategic context becoming project law
comparison lens becoming ontology
output containment becoming truth filter
observability becoming ledger/control layer
Plan-before-Execution becoming mandatory workflow
User-as-Judge becoming ceremonial checkbox
Gemini evidence becoming verified truth
Codex packaging becoming final authority
```

For each, return:

```text
risk:
status:
evidence:
guardrail:
```

Allowed status values:

```text
NO_RISK_FOUND
WATCH_ONLY
RISK_FOUND
UNKNOWN
```

### Task 06 - Reference Usefulness Ranking

Rank the references by usefulness for future project problems.

This is not adoption ranking.

Use these categories:

```text
most useful for context/output problems
most useful for ambiguity/planning problems
most useful for execution/provider boundary problems
most useful for model/tool volatility problems
most useful for User judgment / role-boundary problems
```

For each, return:

```text
category:
best_reference:
reason:
watch:
```

### Task 07 - Missing Link / Weak Spot Check

Identify whether the reference set has gaps.

Questions:

```text
Is any signal under-supported?
Is any reference too implementation-heavy to use safely?
Is any reference too strategic to help concrete work?
Is any trigger missing from the re-entry map?
Is the reference list too close to registry/index behavior?
Is the set lightweight enough for future reuse?
```

Return:

```text
gap_or_weak_spot:
evidence:
severity:
suggested_handling:
```

Allowed severity:

```text
LOW
MEDIUM
HIGH
UNKNOWN
```

### Task 08 - Mistake / Uncertainty Memory

Record any mistakes, possible overreads, or uncertain judgments from this reread.

Return:

```text
mistake_or_uncertainty_id:
type:
what_happened:
evidence_or_trigger:
correction_or_open_question:
can_continue:
prevention_note:
```

If none, return:

```text
No mistake-memory event found in this pass.
```

### Task 09 - User-facing Summary Card

Return a short Korean card:

```text
지금 이 레퍼런스 묶음은 무엇인가?
언제 꺼내 쓰면 좋은가?
무엇을 조심해야 하나?
다음 안전 행동은 무엇인가?
```

Keep it concise.

### Task 10 - Final Judgment

Give one final judgment:

```text
REFERENCE_SET_USEFUL_WITH_WATCH
REFERENCE_SET_TOO_HEAVY
REFERENCE_SET_NEEDS_PATCH
REFERENCE_SET_HOLD
```

Expected likely judgment:

```text
REFERENCE_SET_USEFUL_WITH_WATCH
```

Also recommend one next safe action:

```text
WAIT_FOR_NEXT_NATURAL_TRIGGER
PATCH_REFERENCE_LIST_LIGHTLY
RUN_ONE_SIGNAL_DRY_TEST
HOLD_FOR_USER_REVIEW
```

Do not recommend implementation.

## 5. Required Final Output Structure

Return exactly these sections:

```text
1. Status
2. Source coverage
3. Reference role verification
4. Reusable signals
5. Natural trigger map
6. Overread / drift risk scan
7. Reference usefulness ranking
8. Missing links / weak spots
9. Mistake / uncertainty memory
10. User-facing summary card
11. Final judgment
12. Next safe action
13. Boundary confirmation
14. Final status
```

## 6. Boundary Confirmation

Confirm explicitly:

```text
no implementation
no automation
no runtime script
no repo cloning/running
no SDK/API integration
no MCP attachment
no context-mode adoption
no ouroboros Agent OS adoption
no GoModel gateway adoption
no Managed Agent adoption
no registry/index/ledger
no formal schema
no official workflow
no current-position update
no baseline promotion
no tool/API/function attachment
no Plan Packet workflow
no Gemini autonomous authority
no Gemini verified-truth authority
no Codex final authority
```

## 7. Final Status

End with one of:

```text
STATUS: EXTERNAL_REFERENCE_MATERIALS_DEEP_REREAD_COMPLETE
STATUS: SOURCE_ACCESS_BLOCKED
STATUS: REFERENCE_SET_HOLD_RECOMMENDED
```
