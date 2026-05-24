# Gemini External Material Continue-Until-Blocked Rules v0

## 1. Status

Status: rules candidate
Authority: candidate operating guardrail / not workflow / not automation
Purpose: define when Gemini may continue and when it must stop

## 2. Continue Conditions

Gemini may continue only when all are true:

- result status is CLEAR or CLEAR_WITH_WATCH
- next task is explicitly listed in the queue
- source exists
- read scope is clear
- task remains read / observe / compare / evidence-return only
- no User decision is needed
- no authority or promotion risk is raised
- no package movement is implied
- no implementation is required
- no current-position update is required

## 3. Stop Conditions

Gemini must stop on:

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

## 4. Special Rules

- If Task 009 recommends CURRENT_POSITION_UPDATE_REQUIRED, stop before Task 010.
- If Task 009 recommends CURRENT_POSITION_UPDATE_RECOMMENDED_BUT_NOT_APPLIED, Task 010 may run.
- If a blocked state appears, Gemini returns the result and stops.
- Blocked Gemini task must not block the whole project.
- Codex packages blocked result for User / ChatGPT review.

## 5. What Must Not Be Inferred

- queue is not router
- packet list is not workflow
- result log is not ledger
- Gemini evidence is not verified truth
- auto-continue is not approval
- recovery recommendation is not current-position update
