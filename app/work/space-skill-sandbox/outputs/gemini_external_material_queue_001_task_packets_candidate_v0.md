# Gemini External Material Queue 001 Task Packets Candidate v0

## 1. Status

```text
Status: task packet candidates
Authority: candidate packet design / not executable automation
Queue execution: not started
Gemini run: not run
External source read: not started
Result files: not created
```

This packet set is a non-executable candidate. It defines how Gemini could process one User-provided external material if execution is separately approved.

It does not run Gemini, read the source, adopt the material, create automation, create a router, create a workflow, update current-position, or create a result inbox/log.

## 2. Queue Context

```text
queue_id = gemini_external_material_queue_001
source_material = https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/
source_type = external URL / blog post
user_provided_source = yes
queue_instance = app/work/space-skill-sandbox/outputs/gemini_external_material_queue_instance_001_candidate.md
roles_reference = app/work/space-skill-sandbox/outputs/space_roles_reference_candidate_v0.md
current_anchor = app/work/space-skill-sandbox/outputs/current_position_entry_after_external_material_gate_v0.md
result_template = app/work/space-skill-sandbox/outputs/gemini_external_material_result_template_v0.md
```

## 3. Global Forbidden Actions

```text
no source invention
no broad browsing
no external material adoption
no baseline promotion
no official workflow creation
no automation/router/controller
no registry/index/ledger creation
no package movement
no Run 117 approval
no Gemini verified-truth claim
no current-position update
no hidden background execution
```

## 4. Global Stop Conditions

Gemini must stop and return to Codex/User review if any of these appear:

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

Auto-continue is allowed only when the task result is `CLEAR` or `CLEAR_WITH_WATCH`, the next task is explicitly listed, and no stop condition is triggered.

## 5. Packet Candidate 001

```text
task_id = gemini_external_material_queue_001_task_001
queue_id = gemini_external_material_queue_001
task_type = MATERIAL_GATE_CHECK
source_material = https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/
user_provided_source = yes
purpose = confirm that one explicit User-provided external source exists for this queue
read_scope = queue metadata only; do not open or summarize source content
execution_steps = check source field; confirm source count is one; confirm user_provided_source is yes; check whether scope is clear
expected_output = source gate result
evidence_required = source URL present; source type recorded; user-provided status recorded; one-source scope recorded
uncertainty_required = source accessibility is not tested in this packet
forbidden_actions = do not browse; do not summarize source; do not adopt material; do not infer execution approval
stop_conditions = SOURCE_MISSING; SCOPE_AMBIGUOUS; USER_DECISION_REQUIRED
return_format = app/work/space-skill-sandbox/outputs/gemini_external_material_result_template_v0.md
recovery_target = RUN_NOTE_ONLY
next_safe_action = continue to Task 002 only if source gate is CLEAR or CLEAR_WITH_WATCH
auto_continue_allowed = yes only on CLEAR or CLEAR_WITH_WATCH
```

## 6. Packet Candidate 002

```text
task_id = gemini_external_material_queue_001_task_002
queue_id = gemini_external_material_queue_001
task_type = SOURCE_SUMMARY
source_material = https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/
user_provided_source = yes
purpose = read only the provided source and summarize its factual claims
read_scope = provided URL only; no broad browsing; no linked-page expansion unless source access requires basic page context
execution_steps = open the source; identify title/author/date if visible; summarize core claims; record source refs; record uncertainty
expected_output = bounded source summary with evidence and uncertainty
evidence_required = factual source summary; source refs; visible title/date/author if available; no unsupported claims
uncertainty_required = missing metadata; inaccessible sections; ambiguous claims; translation uncertainty if any
forbidden_actions = do not browse broadly; do not adopt material; do not create comparison yet; do not infer policy/workflow
stop_conditions = SOURCE_MISSING; SCOPE_AMBIGUOUS; AUTHORITY_RISK; PROMOTION_RISK
return_format = app/work/space-skill-sandbox/outputs/gemini_external_material_result_template_v0.md
recovery_target = RUN_NOTE_ONLY
next_safe_action = continue to Task 003 if summary is bounded and no stop condition appears
auto_continue_allowed = yes only on CLEAR or CLEAR_WITH_WATCH
```

## 7. Packet Candidate 003

```text
task_id = gemini_external_material_queue_001_task_003
queue_id = gemini_external_material_queue_001
task_type = FOUR_LINE_CARD
source_material = https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/
user_provided_source = yes
purpose = translate the source summary into a simple User-facing orientation card
read_scope = Task 002 result plus queue context; do not reread source unless summary is insufficient
execution_steps = answer four lines in Korean: 지금 어디까지 왔나? 무엇을 움직일 수 있나? 무엇을 조심해야 하나? 다음 판단은 무엇인가?
expected_output = four-line card that remains a usage aid
evidence_required = each line grounded in Task 002 summary; clear warning that material is not adopted
uncertainty_required = any unclear fit or source ambiguity
forbidden_actions = do not turn card into workflow; do not create protocol; do not infer next purpose
stop_conditions = SCOPE_AMBIGUOUS; USER_DECISION_REQUIRED; PROMOTION_RISK
return_format = app/work/space-skill-sandbox/outputs/gemini_external_material_result_template_v0.md
recovery_target = RUN_NOTE_ONLY
next_safe_action = continue to Task 004 if card stays user-facing and candidate-only
auto_continue_allowed = yes only on CLEAR or CLEAR_WITH_WATCH
```

## 8. Packet Candidate 004

```text
task_id = gemini_external_material_queue_001_task_004
queue_id = gemini_external_material_queue_001
task_type = ROLE_CLASSIFICATION
source_material = https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/
user_provided_source = yes
purpose = classify the role this external material can safely play in our space
read_scope = Task 002 and Task 003 results; Roles reference candidate; queue boundaries
execution_steps = classify as external reference, candidate reference, inspiration-only, watch item, reject, or needs user decision; explain why
expected_output = role classification with no adoption
evidence_required = role selected; basis from source summary; basis from Roles reference
uncertainty_required = unclear authority or role ambiguity
forbidden_actions = do not adopt; do not approve; do not promote; do not treat as source-space authority
stop_conditions = USER_DECISION_REQUIRED; AUTHORITY_RISK; PROMOTION_RISK
return_format = app/work/space-skill-sandbox/outputs/gemini_external_material_result_template_v0.md
recovery_target = RUN_NOTE_ONLY
next_safe_action = continue to Task 005 if role is candidate/reference/watch only
auto_continue_allowed = yes only on CLEAR or CLEAR_WITH_WATCH
```

## 9. Packet Candidate 005

```text
task_id = gemini_external_material_queue_001_task_005
queue_id = gemini_external_material_queue_001
task_type = COMPARISON_WITH_SPACE
source_material = https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/
user_provided_source = yes
purpose = compare the material against current space concepts without adoption
read_scope = Task 002-004 results; current anchor; Roles reference; package and agent-work-mem summaries only if already cited in queue context
execution_steps = compare source ideas with current-position, process-memory, worker handoff, role boundaries, evidence pipeline, and watch items
expected_output = fit / not-fit / watch map
evidence_required = comparison points; source-grounded evidence; internal reference basis
uncertainty_required = where internal fit is unclear or needs User/ChatGPT judgment
forbidden_actions = do not create policy; do not create schema; do not create workflow; do not implement
stop_conditions = AUTHORITY_RISK; PROMOTION_RISK; IMPLEMENTATION_REQUIRED; CURRENT_POSITION_UPDATE_REQUIRED
return_format = app/work/space-skill-sandbox/outputs/gemini_external_material_result_template_v0.md
recovery_target = PROCESS_MEMORY_LIGHT if useful; otherwise RUN_NOTE_ONLY
next_safe_action = continue to Task 006 if comparison remains evidence-only
auto_continue_allowed = yes only on CLEAR or CLEAR_WITH_WATCH
```

## 10. Packet Candidate 006

```text
task_id = gemini_external_material_queue_001_task_006
queue_id = gemini_external_material_queue_001
task_type = WATCH_ITEM_EXTRACTION
source_material = https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/
user_provided_source = yes
purpose = extract role drift and promotion risks as watch items
read_scope = Task 005 comparison result; Roles reference watch-item definition
execution_steps = identify drift risks; mark each as watch-only unless a stop condition appears; explain why each is not hard law
expected_output = watch item list with evidence and uncertainty
evidence_required = watch item; drift type; source or internal basis; why watch-only
uncertainty_required = risks that may require User judgment
forbidden_actions = do not turn watch item into prohibition; do not create rule; do not block automatically
stop_conditions = AUTHORITY_RISK; PROMOTION_RISK; USER_DECISION_REQUIRED
return_format = app/work/space-skill-sandbox/outputs/gemini_external_material_result_template_v0.md
recovery_target = WATCH_ITEM_ONLY or PROCESS_MEMORY_LIGHT
next_safe_action = continue to Task 007 if risks remain watch-only
auto_continue_allowed = yes only on CLEAR or CLEAR_WITH_WATCH
```

## 11. Packet Candidate 007

```text
task_id = gemini_external_material_queue_001_task_007
queue_id = gemini_external_material_queue_001
task_type = INSPIRATION_EXTRACTION
source_material = https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/
user_provided_source = yes
purpose = extract candidate inspiration-only lessons if useful
read_scope = Task 002-006 results
execution_steps = list possible lessons; label every lesson INSPIRATION_ONLY; distinguish lesson from adoption
expected_output = inspiration-only list or no-useful-inspiration result
evidence_required = each lesson tied to source summary and space comparison
uncertainty_required = whether a lesson needs later User review
forbidden_actions = do not create adoption plan; do not create implementation plan; do not create package movement
stop_conditions = PROMOTION_RISK; IMPLEMENTATION_REQUIRED; USER_DECISION_REQUIRED
return_format = app/work/space-skill-sandbox/outputs/gemini_external_material_result_template_v0.md
recovery_target = PROCESS_MEMORY_LIGHT if lessons are useful; otherwise RUN_NOTE_ONLY
next_safe_action = continue to Task 008 if all lessons remain inspiration-only
auto_continue_allowed = yes only on CLEAR or CLEAR_WITH_WATCH
```

## 12. Packet Candidate 008

```text
task_id = gemini_external_material_queue_001_task_008
queue_id = gemini_external_material_queue_001
task_type = DO_NOT_ADOPT_CHECK
source_material = https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/
user_provided_source = yes
purpose = explicitly confirm what must not be adopted, promoted, or copied
read_scope = Task 002-007 results; global forbidden actions
execution_steps = list do-not-adopt items; check for baseline/workflow/schema/automation/package/current-position risks
expected_output = do-not-adopt boundary list
evidence_required = boundary; related risk; source or internal basis
uncertainty_required = unclear boundary cases
forbidden_actions = do not weaken boundaries; do not infer approval from useful fit
stop_conditions = AUTHORITY_RISK; PROMOTION_RISK; IMPLEMENTATION_REQUIRED; PACKAGE_MOVEMENT_RISK
return_format = app/work/space-skill-sandbox/outputs/gemini_external_material_result_template_v0.md
recovery_target = WATCH_ITEM_ONLY or PROCESS_MEMORY_LIGHT
next_safe_action = continue to Task 009 if boundaries are clear and no stop condition appears
auto_continue_allowed = yes only on CLEAR or CLEAR_WITH_WATCH
```

## 13. Packet Candidate 009

```text
task_id = gemini_external_material_queue_001_task_009
queue_id = gemini_external_material_queue_001
task_type = RECOVERY_PATH_DECISION
source_material = https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/
user_provided_source = yes
purpose = recommend the lightest recovery path for the completed evidence chain
read_scope = Task 001-008 results
execution_steps = choose one recovery path; explain why; flag if current-position update or User decision is required
expected_output = recovery path decision
evidence_required = chosen path; reason; what was learned; what remains watch-only
uncertainty_required = whether recovery requires User/ChatGPT review
forbidden_actions = do not update current-position; do not create run records; do not create closeout by execution
stop_conditions = CURRENT_POSITION_UPDATE_REQUIRED; USER_DECISION_REQUIRED; AUTHORITY_RISK
return_format = app/work/space-skill-sandbox/outputs/gemini_external_material_result_template_v0.md
recovery_target = RUN_NOTE_ONLY; PROCESS_MEMORY_LIGHT; WATCH_ITEM_ONLY; CURRENT_POSITION_UPDATE_RECOMMENDED_BUT_NOT_APPLIED; or CURRENT_POSITION_UPDATE_REQUIRED
next_safe_action = continue to Task 010 only if no current-position update is required and no User decision is required
auto_continue_allowed = yes only on CLEAR or CLEAR_WITH_WATCH and recovery does not require User decision
```

## 14. Packet Candidate 010

```text
task_id = gemini_external_material_queue_001_task_010
queue_id = gemini_external_material_queue_001
task_type = CLOSEOUT_SUMMARY
source_material = https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/
user_provided_source = yes
purpose = consolidate Task 001-009 evidence for Codex / ChatGPT / User review
read_scope = Task 001-009 results only
execution_steps = summarize source status, role classification, fit, watch items, inspiration-only lessons, do-not-adopt items, recovery recommendation, and next safe action
expected_output = closeout summary for review
evidence_required = compact summary of all task results; clear final status
uncertainty_required = open questions and User decision points
forbidden_actions = do not approve; do not adopt; do not create current-position update; do not continue to another task
stop_conditions = final stop after summary; USER_DECISION_REQUIRED if next action needs User judgment
return_format = app/work/space-skill-sandbox/outputs/gemini_external_material_result_template_v0.md
recovery_target = as decided in Task 009
next_safe_action = stop and return to Codex / ChatGPT / User review
auto_continue_allowed = no
```

## 15. What This Packet Set Is Not

```text
not Gemini execution
not queue activation
not workflow
not router
not automation
not result inbox
not execution log
not current-position update
not source summary
not external material adoption
```

## 16. Next Safe Action

```text
Review these task packet candidates before Gemini execution.
If approved later, execute only the explicitly approved queue/packet scope.
Do not auto-run Gemini from this document alone.
```

`STATUS: GEMINI_EXTERNAL_MATERIAL_QUEUE_001_TASK_PACKETS_CANDIDATE_PREPARED`
