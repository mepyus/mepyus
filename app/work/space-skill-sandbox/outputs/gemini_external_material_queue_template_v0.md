# Gemini External Material Queue Template v0

## 1. Status

Status: queue template candidate
Authority: candidate reference / not workflow / not automation / not router
Purpose: define a durable task queue shape for one User-provided external material

## 2. Queue Metadata

Fields:

- queue_id
- user_purpose
- source_material
- source_type
- user_provided: yes/no
- created_by
- authority_status
- roles_reference
- current_anchor
- task_list
- current_task
- allowed_auto_continue_states
- blocking_states
- result_location
- recovery_target
- watch_items
- what_must_not_be_inferred

## 3. Default Task List

Task 001: MATERIAL_GATE_CHECK
Task 002: SOURCE_SUMMARY
Task 003: FOUR_LINE_CARD
Task 004: ROLE_CLASSIFICATION
Task 005: COMPARISON_WITH_SPACE
Task 006: WATCH_ITEM_EXTRACTION
Task 007: INSPIRATION_EXTRACTION
Task 008: DO_NOT_ADOPT_CHECK
Task 009: RECOVERY_PATH_DECISION
Task 010: CLOSEOUT_SUMMARY

## 4. Auto-Continue Rule

Continue only if previous result status is:

- CLEAR
- CLEAR_WITH_WATCH

and:

- next task is already listed
- source exists
- scope is clear
- no User decision is required
- no promotion / adoption / implementation / package movement is implied
- no current-position update is required

## 5. Blocking States

- NEEDS_USER_MATERIAL
- SOURCE_MISSING
- SCOPE_AMBIGUOUS
- USER_DECISION_REQUIRED
- AUTHORITY_RISK
- PROMOTION_RISK
- PACKAGE_MOVEMENT_RISK
- IMPLEMENTATION_REQUIRED
- NEXT_PURPOSE_REQUIRED
- CURRENT_POSITION_UPDATE_REQUIRED

## 6. What This Queue Is Not

- not router
- not workflow
- not automation approval
- not permission system
- not registry/index/ledger
- not package movement trigger
