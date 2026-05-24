# Gemini Space Intake Worklist - Tools Leave Their Maker v0

## 1. Status

```text
Document = Gemini Space Intake Worklist
Status = EXECUTION_WORKLIST_CANDIDATE
Authority = bounded Gemini execution instruction / not approval
Source material = https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/
Codex role = structure / packetization / result packaging
Gemini role = execution / reading / observation / evidence return
Current-position update = not allowed by Gemini
```

This worklist is designed for Gemini to execute bounded reading, checking, and evidence extraction.

It is not a workflow promotion, not automation, not a router, not a registry, not a ledger, and not a permission system.

## 2. Why This Worklist Exists

Queue 001 proved that Gemini can process one external material through a continue-until-blocked sequence.

But Queue 001 mostly stayed at:

```text
external source -> Gemini summary -> process-memory-light
```

This worklist pushes the same source through the missing internal space process:

```text
source evidence
-> space intake
-> lens pass
-> camera/capture pass
-> line-axis pass
-> role classification
-> watch / mistake extraction
-> recovery recommendation
```

Gemini may make mistakes.

That is acceptable if Gemini:

```text
records the mistake
marks uncertainty
does not silently correct history
does not promote its own output into truth
returns a prevention note so the space can reduce repeat mistakes
```

## 3. Core Execution Rule

Gemini should continue through the listed tasks only when the current task result is:

```text
CLEAR
CLEAR_WITH_WATCH
MISTAKE_RECORDED_CONTINUE
```

Gemini must stop when the current task result is:

```text
SOURCE_MISSING
SCOPE_AMBIGUOUS
USER_DECISION_REQUIRED
AUTHORITY_RISK
PROMOTION_RISK
PACKAGE_MOVEMENT_RISK
IMPLEMENTATION_REQUIRED
CURRENT_POSITION_UPDATE_REQUIRED
NEXT_PURPOSE_REQUIRED
```

Minor mistakes do not require stopping if they are recorded and bounded.

Major mistakes require stopping if they affect source truth, authority, promotion, package movement, current-position, or scope.

## 4. Mistake Handling Contract

Gemini must assume it can misread, over-summarize, over-classify, hallucinate internal fit, or infer authority by accident.

When a possible mistake is found, record it as:

```text
mistake_id:
task_id:
mistake_type:
suspected_mistake:
evidence_or_trigger:
impact:
correction_or_uncertainty:
can_continue:
prevention_note:
repeat_risk:
```

Allowed `mistake_type` values:

```text
SOURCE_MISREAD
UNSUPPORTED_CLAIM
OVERGENERALIZATION
ROLE_DRIFT
AUTHORITY_OVERREAD
MISSING_UNCERTAINTY
BOUNDARY_WEAKENING
INTERNAL_REFERENCE_CONFUSION
LINE_AXIS_OVERFIT
WATCH_ITEM_OVERHARDENING
```

Mistake policy:

```text
do not hide mistakes
do not rewrite earlier task results silently
do not convert mistake notes into blame
do not treat mistake as failure if bounded and recorded
do use mistake notes to improve future packet design
```

## 5. Inputs Gemini Should Use

Primary source:

```text
https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/
```

Internal context to use conceptually:

```text
Space Roles Reference Candidate
Codex Structure Design / Gemini Execution Setup
Queue 001 Process Memory Light
```

Gemini does not need to read every internal file in full unless available in the prompt.

If internal context is missing or unclear, Gemini must say so and continue with uncertainty if safe.

## 6. Forbidden Actions

```text
do not adopt MCP or external protocols
do not create baseline
do not create official workflow
do not create source-space policy
do not create schema
do not create automation/router/controller
do not create registry/index/ledger
do not approve packages
do not approve Run 117
do not update current-position
do not treat Gemini observations as verified truth
do not treat description as permission
do not infer hidden authority from useful fit
```

## 7. Worklist Overview

```text
Task 00 = ROLE_AND_BOUNDARY_PRECHECK
Task 01 = MATERIAL_GATE_AND_SOURCE_IDENTITY
Task 02 = SOURCE_EVIDENCE_EXTRACTION
Task 03 = SOURCE_SELF_CHECK_AND_MISTAKE_SCAN
Task 04 = SPACE_INTAKE_RECORD_DRAFT
Task 05 = LENS_PASS
Task 06 = CAMERA_CAPTURE_PASS
Task 07 = LINE_AXIS_PLACEMENT_PASS
Task 08 = ROLE_CLASSIFICATION_AND_AUTHORITY_CHECK
Task 09 = WATCH_ITEM_AND_MISTAKE_MEMORY_EXTRACTION
Task 10 = RECOVERY_PATH_RECOMMENDATION
Task 11 = RESULT_BUNDLE_CLOSEOUT
```

## 8. Task 00 - ROLE_AND_BOUNDARY_PRECHECK

Purpose:

```text
Confirm Gemini is acting as bounded executor / observer / evidence return worker.
```

Steps:

```text
state Gemini role
state what Gemini may do
state what Gemini must not do
confirm output is worker evidence, not verified truth
```

Expected output:

```text
role boundary confirmation
```

Likely mistake:

```text
Gemini overstates its authority or says it will decide adoption.
```

Mistake handling:

```text
record AUTHORITY_OVERREAD and correct before continuing
```

Stop if:

```text
Gemini cannot preserve worker-evidence-only role
```

## 9. Task 01 - MATERIAL_GATE_AND_SOURCE_IDENTITY

Purpose:

```text
Confirm source is explicit, singular, and user-provided.
```

Steps:

```text
confirm URL
confirm one-source scope
identify source type
do not broaden beyond source
```

Expected output:

```text
source identity record
```

Likely mistakes:

```text
browsing beyond the source
treating linked context as part of the source without saying so
```

Mistake handling:

```text
record SOURCE_MISREAD or SCOPE_AMBIGUOUS if source scope expands
```

Stop if:

```text
source cannot be accessed
source identity is unclear
```

## 10. Task 02 - SOURCE_EVIDENCE_EXTRACTION

Purpose:

```text
Extract what the source says, not what we want it to mean.
```

Steps:

```text
identify main thesis
extract key terms
extract claims about tools, descriptions, affordance, MCP-style interface, and caller context
separate source claim from Gemini interpretation
record uncertainty
```

Expected output:

```text
source evidence table
```

Required format:

```text
claim:
source basis:
Gemini interpretation:
uncertainty:
```

Likely mistakes:

```text
unsupported claim
overgeneralization
missing uncertainty
```

Mistake handling:

```text
record mistake event and continue if source evidence remains usable
```

Stop if:

```text
summary depends on unsupported claims
```

## 11. Task 03 - SOURCE_SELF_CHECK_AND_MISTAKE_SCAN

Purpose:

```text
Check Gemini's own source extraction before using it in the space.
```

Steps:

```text
review Task 02 claims
mark any claim that lacks source support
mark any term that was translated too freely
mark any missing uncertainty
produce corrected evidence notes if needed
```

Expected output:

```text
self-check report
mistake events if any
corrected evidence notes
```

Likely mistakes:

```text
Gemini rubber-stamps its own summary
Gemini hides uncertainty
```

Mistake handling:

```text
record MISSING_UNCERTAINTY or UNSUPPORTED_CLAIM
```

Continue if:

```text
mistakes are bounded and corrected in the report
```

## 12. Task 04 - SPACE_INTAKE_RECORD_DRAFT

Purpose:

```text
Draft how this source would enter the space without adoption.
```

Steps:

```text
classify material as external reference / inspiration-only / candidate reference / watch item / reject / needs User decision
state what role it can safely play
state what it must not become
state whether current-position update is needed
```

Expected output:

```text
space intake draft
```

Likely mistakes:

```text
candidate reference becomes approval
useful material becomes adoption
watch item becomes law
```

Mistake handling:

```text
record ROLE_DRIFT or AUTHORITY_OVERREAD
```

Stop if:

```text
classification requires User adoption/promotion decision
```

## 13. Task 05 - LENS_PASS

Purpose:

```text
Read the source through existing space lenses without turning lenses into law.
```

Use these lenses:

```text
Harness over Model
Function over Affordance
Metadata before Full Context
Agent-readable Context
Program as Material
Definition before Prompt
Tool capability is not permission
```

For each lens:

```text
fit:
source evidence:
what this helps us see:
drift risk:
uncertainty:
```

Expected output:

```text
lens pass table
```

Likely mistakes:

```text
forcing a source into every lens
turning lens fit into policy
overfitting tool language into our system
```

Mistake handling:

```text
record LINE_AXIS_OVERFIT or ROLE_DRIFT
```

Continue if:

```text
lens pass remains audit support only
```

## 14. Task 06 - CAMERA_CAPTURE_PASS

Purpose:

```text
Capture what was seen through the lenses in a reusable record form.
```

Camera means:

```text
how we capture and record what was seen
not truth
not reality
not authority
```

Steps:

```text
produce compact capture notes
separate source observation from space interpretation
record where evidence is strong or weak
record what should be rechecked later
```

Expected output:

```text
camera capture notes
```

Likely mistakes:

```text
camera capture becomes verified truth
source note becomes official memory
```

Mistake handling:

```text
record AUTHORITY_OVERREAD or MISSING_UNCERTAINTY
```

## 15. Task 07 - LINE_AXIS_PLACEMENT_PASS

Purpose:

```text
Place source evidence against current line/axis candidates without promoting axes.
```

Use these axes:

```text
Harness-Orientation
Affordance-Program
Signal-Memory
Provenance-Integrity
```

For each axis:

```text
placement:
source evidence:
why it fits or does not fit:
watch risk:
uncertainty:
```

Expected output:

```text
line-axis placement candidate
```

Likely mistakes:

```text
axis becomes ontology
axis placement becomes final classification
overfitting source to existing axes
```

Mistake handling:

```text
record LINE_AXIS_OVERFIT
```

Continue only if:

```text
placement remains candidate / audit support
```

## 16. Task 08 - ROLE_CLASSIFICATION_AND_AUTHORITY_CHECK

Purpose:

```text
Check whether the source, its lessons, and Gemini's own output are still role-bounded.
```

Check:

```text
external reference != adoption
inspiration-only != implementation plan
watch item != prohibition
description != permission
Gemini evidence != verified truth
Codex packaging != implementation authority
current-position != registry/index
```

Expected output:

```text
role / authority check table
```

Likely mistakes:

```text
useful source becomes authority
description language becomes permission
Gemini output overstates certainty
```

Mistake handling:

```text
record AUTHORITY_OVERREAD or BOUNDARY_WEAKENING
```

Stop if:

```text
authority risk cannot be bounded
```

## 17. Task 09 - WATCH_ITEM_AND_MISTAKE_MEMORY_EXTRACTION

Purpose:

```text
Extract watch items and mistake-memory candidates so future runs get better.
```

Required outputs:

```text
watch_items:
mistake_events:
prevention_notes:
packet_design_improvements:
```

Watch examples to check:

```text
intentional description becoming implicit permission
worker packet description becoming workflow
tool affordance becoming automation claim
MCP source becoming adoption plan
Gemini evidence becoming verified truth
line-axis placement becoming ontology
camera capture becoming official truth
```

Mistake-memory goal:

```text
We do not punish Gemini for mistakes.
We preserve mistakes so Codex can improve packet design and reduce repeat errors.
```

Expected output:

```text
watch and mistake memory section
```

## 18. Task 10 - RECOVERY_PATH_RECOMMENDATION

Purpose:

```text
Recommend where the result should return in the space.
```

Choose one:

```text
RUN_NOTE_ONLY
PROCESS_MEMORY_LIGHT
WATCH_ITEM_ONLY
CANDIDATE_REFERENCE_ONLY
REUSABLE_SETTING_RECOMMENDED_BUT_NOT_CREATED
CURRENT_POSITION_UPDATE_RECOMMENDED_BUT_NOT_APPLIED
CURRENT_POSITION_UPDATE_REQUIRED
USER_DECISION_REQUIRED
```

Expected recommendation for this source:

```text
PROCESS_MEMORY_LIGHT or CANDIDATE_REFERENCE_ONLY
```

Stop if:

```text
CURRENT_POSITION_UPDATE_REQUIRED
USER_DECISION_REQUIRED
```

Gemini must not create the recovery artifact.

Gemini only recommends it.

## 19. Task 11 - RESULT_BUNDLE_CLOSEOUT

Purpose:

```text
Return one structured result bundle to Codex / ChatGPT / User.
```

Required output:

```markdown
# Gemini Result - Space Intake Worklist: Tools Leave Their Maker

## 1. Final Status

Use one:
CLEAR
CLEAR_WITH_WATCH
MISTAKE_RECORDED_CONTINUE
BLOCKED_NEEDS_USER
BLOCKED_SOURCE_ACCESS
BLOCKED_AUTHORITY_RISK
BLOCKED_PROMOTION_RISK

## 2. Completed Tasks

## 3. Source Evidence Table

## 4. Source Self-Check

## 5. Space Intake Draft

## 6. Lens Pass

## 7. Camera Capture Pass

## 8. Line-Axis Placement Pass

## 9. Role / Authority Check

## 10. Watch Items

## 11. Mistake Events

## 12. Prevention Notes

## 13. Recovery Path Recommendation

## 14. What Must Not Be Inferred

## 15. Next Safe Action

STATUS: GEMINI_SPACE_INTAKE_WORKLIST_TOOLS_LEAVE_THEIR_MAKER_COMPLETE
```

## 20. Codex Packaging Plan After Gemini Returns

Codex should not re-read the full source unless necessary.

Codex should use Gemini's result bundle to create:

```text
run record
process-memory-light or candidate-reference note
watch item carry-forward note if needed
mistake-memory note if mistakes were found
pipeline design improvement note if packet wording needs adjustment
```

Codex should then decide whether:

```text
current-position update is still not required
User/ChatGPT review is needed
packet design should be refined
another source can use the same pipeline shape
```

## 21. Boundary Confirmation

```text
no baseline promotion
no official workflow creation
no source-space policy creation
no schema creation
no automation/router/controller
no registry/index/ledger
no package movement
no Run 117 approval
no current-position update by Gemini
no Gemini verified-truth authority
no Gemini autonomous authority
no Codex implementation authority
```

`STATUS: GEMINI_SPACE_INTAKE_WORKLIST_TOOLS_LEAVE_THEIR_MAKER_PREPARED`
