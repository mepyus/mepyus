# Gemini External Material Result Template v0

## 1. Status

Status: result template candidate
Authority: worker evidence / not verified truth / not approval
Purpose: define how Gemini returns task results

## 2. Required Fields

- queue_id
- task_id
- task_type
- status
- source_refs
- evidence_summary
- uncertainty
- space_use_judgment
- watch_items
- what_must_not_be_inferred
- recovery_path
- next_safe_action
- auto_continue_decision
- stop_reason

## 3. Allowed Statuses

- CLEAR
- CLEAR_WITH_WATCH
- NEEDS_USER_MATERIAL
- SOURCE_MISSING
- SCOPE_AMBIGUOUS
- USER_DECISION_REQUIRED
- AUTHORITY_RISK
- PROMOTION_RISK
- PACKAGE_MOVEMENT_RISK
- IMPLEMENTATION_REQUIRED
- CURRENT_POSITION_UPDATE_REQUIRED

## 4. Auto-Continue Decisions

- CONTINUE_TO_NEXT_PACKET
- STOP_AND_RETURN_TO_CODEX
- STOP_FOR_USER_DECISION

## 5. Recovery Paths

- RUN_NOTE_ONLY
- PROCESS_MEMORY_LIGHT
- WATCH_ITEM_ONLY
- CURRENT_POSITION_UPDATE_RECOMMENDED_BUT_NOT_APPLIED
- CURRENT_POSITION_UPDATE_REQUIRED

## 6. Evidence Rule

Gemini returns evidence and uncertainty.
Gemini does not return approval, truth, adoption, promotion, implementation, or package movement.
