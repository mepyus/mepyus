# Gemini External Material Queue Instance 001 Candidate

## 1. Status

```text
Status: queue instance candidate
Authority: candidate queue instance / not workflow / not automation / not router
Purpose: define the first non-executable continue-until-blocked Gemini queue for one User-provided external material
Queue execution: not started
Gemini run: not run
```

This queue instance is a candidate design artifact only.

It does not adopt the external material.
It does not execute Gemini.
It does not create automation, routing, registry, index, ledger, schema, or permission system.

## 2. Queue Metadata

```text
queue_id = gemini_external_material_queue_001
user_purpose = put one explicit external material into the space through the continue-until-blocked evidence pipeline
source_material = https://evan-moon.github.io/2026/04/28/tools-leave-their-maker/
source_type = external URL / blog post
user_provided = yes
created_by = Codex
authority_status = candidate queue instance / not workflow / not automation
roles_reference = app/work/space-skill-sandbox/outputs/space_roles_reference_candidate_v0.md
current_anchor = app/work/space-skill-sandbox/outputs/current_position_entry_after_external_material_gate_v0.md
template_refs = app/work/space-skill-sandbox/outputs/gemini_external_material_queue_template_v0.md; app/work/space-skill-sandbox/outputs/gemini_external_material_task_packet_template_v0.md; app/work/space-skill-sandbox/outputs/gemini_external_material_result_template_v0.md; app/work/space-skill-sandbox/outputs/gemini_external_material_continue_until_blocked_rules_v0.md
current_task = Task 001: MATERIAL_GATE_CHECK
result_location = not created / candidate result location only
recovery_target = RUN_NOTE_ONLY by default; PROCESS_MEMORY_LIGHT if comparison yields useful inspiration; CURRENT_POSITION_UPDATE only by explicit User/Codex review decision
```

## 3. Allowed Auto-Continue States

Gemini may continue only if the previous task result status is:

```text
CLEAR
CLEAR_WITH_WATCH
```

and all are true:

```text
next task is explicitly listed
source exists
read scope is clear
task remains read / observe / compare / evidence-return only
no User decision is needed
no authority or promotion risk is raised
no package movement is implied
no implementation is required
no current-position update is required
```

## 4. Blocking States

Gemini must stop if any result status is:

```text
NEEDS_USER_MATERIAL
SOURCE_MISSING
SCOPE_AMBIGUOUS
USER_DECISION_REQUIRED
AUTHORITY_RISK
PROMOTION_RISK
PACKAGE_MOVEMENT_RISK
IMPLEMENTATION_REQUIRED
NEXT_PURPOSE_REQUIRED
CURRENT_POSITION_UPDATE_REQUIRED
```

## 5. Task List

| Task | Type | Purpose | Input | Expected output | Continue condition | Stop condition |
|---|---|---|---|---|---|---|
| Task 001 | `MATERIAL_GATE_CHECK` | Confirm the User-provided URL is the single source for this queue | source URL + queue metadata | source gate result | source is explicit and scope is clear | `SOURCE_MISSING`, `SCOPE_AMBIGUOUS`, multiple sources |
| Task 002 | `SOURCE_SUMMARY` | Read only the provided source and summarize factual claims | provided URL | short source summary with source refs and uncertainty | summary is bounded and no adoption implied | source inaccessible, broad browsing needed |
| Task 003 | `FOUR_LINE_CARD` | Translate the material into user-facing orientation | source summary | four-line card in Korean | card stays usage aid | card becomes workflow/protocol |
| Task 004 | `ROLE_CLASSIFICATION` | Classify material role in our space | source summary + Roles reference | external reference / candidate / watch / reject classification | role is candidate/reference/watch only | adoption or authority implied |
| Task 005 | `COMPARISON_WITH_SPACE` | Compare material with current-position, process-memory, worker handoff, role boundaries | source summary + current anchor + Roles reference | fit / not-fit map | comparison remains evidence | policy/schema/workflow implication |
| Task 006 | `WATCH_ITEM_EXTRACTION` | Extract drift risks | comparison result | watch item list | risks are watch-only | hard law / prohibition implied |
| Task 007 | `INSPIRATION_EXTRACTION` | Extract inspiration-only lessons if useful | comparison + watch list | inspiration-only list | inspiration remains candidate | adoption plan implied |
| Task 008 | `DO_NOT_ADOPT_CHECK` | Confirm what must not be adopted | source + comparison | do-not-adopt boundaries | boundaries are clear | promotion / implementation needed |
| Task 009 | `RECOVERY_PATH_DECISION` | Recommend lightest recovery path | all prior results | `RUN_NOTE_ONLY`, `PROCESS_MEMORY_LIGHT`, `WATCH_ITEM_ONLY`, or current-position recommendation | no current-position update required, or recommended but not applied | `CURRENT_POSITION_UPDATE_REQUIRED`, `USER_DECISION_REQUIRED` |
| Task 010 | `CLOSEOUT_SUMMARY` | Consolidate evidence for Codex / ChatGPT / User | tasks 001-009 | closeout summary | final stop after summary | do not run if Task 009 requires current-position update or User decision |

## 6. Watch Items

```text
external material becoming adoption plan
queue becoming router
packet list becoming workflow
result log becoming ledger
Gemini evidence becoming verified truth
Gemini continuing past User decision gate
Codex packaging becoming implementation
watch item becoming hard law
current-position update happening automatically
```

## 7. What Must Not Be Inferred

```text
no external material adoption
no baseline promotion
no official workflow
no automation/router/controller
no registry/index/ledger
no formal permission system
no Gemini approval authority
no Gemini verified-truth authority
no Codex-to-Gemini autonomous routing without User-selected purpose
no package movement
no Run 117 approval
no hidden background execution
no current-position update
```

## 8. Next Safe Action

```text
User/ChatGPT review this queue instance candidate.
If approved, Codex may create non-executable task packet candidates for Task 001-010 or prepare a Gemini execution packet.
Do not run Gemini until execution is explicitly approved.
```

`STATUS: FIRST_EXTERNAL_MATERIAL_QUEUE_INSTANCE_001_CANDIDATE_PREPARED`
