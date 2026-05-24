# Gemini External Material Task Packet Template v0

## 1. Status

Status: task packet template candidate
Authority: candidate reference / not executable automation
Purpose: define a bounded Gemini task packet for external-material handling

## 2. Required Fields

- task_id
- queue_id
- task_type
- source_material
- user_provided_source
- purpose
- read_scope
- execution_steps
- expected_output
- evidence_required
- uncertainty_required
- forbidden_actions
- stop_conditions
- return_format
- recovery_target
- next_safe_action
- auto_continue_allowed

## 3. Task Types

- MATERIAL_GATE_CHECK
- SOURCE_SUMMARY
- FOUR_LINE_CARD
- ROLE_CLASSIFICATION
- COMPARISON_WITH_SPACE
- WATCH_ITEM_EXTRACTION
- INSPIRATION_EXTRACTION
- DO_NOT_ADOPT_CHECK
- RECOVERY_PATH_DECISION
- CLOSEOUT_SUMMARY

## 4. Standard Forbidden Actions

- no source invention
- no broad browsing
- no external material adoption
- no baseline promotion
- no official workflow creation
- no automation/router/controller
- no registry/index/ledger creation
- no package movement
- no Run 117 approval
- no Gemini verified-truth claim
- no current-position update

## 5. Standard Stop Conditions

- source missing
- scope ambiguous
- User decision needed
- authority risk
- promotion risk
- implementation required
- package movement implied
- current-position update required
