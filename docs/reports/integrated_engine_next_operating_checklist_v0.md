# Integrated Engine Next Operating Checklist v0

## Verdict

READY

## Current Goal

Move from "CLI can run from the integrated-engine UI" to "the user can converse with CLI inside VectorFL and route each turn into User assignment, VectorFL reread, Engine request, or space-deposit candidate."

## Checklist

### Step 1. Current State And Folder Status Lock

- owner: User surface / documentation support
- goal: lock today's folder and operating state before new implementation.
- actions:
  - create `gemini/folder_status.md`
  - create `app/ui/integrated_engine/folder_status.md`
  - record today closeout and next checklist
- verification:
  - files exist
  - current UI folder and Gemini proposal folder are no longer confused
- record:
  - `integrated_engine_20260416_operating_closeout_v0.md`
- status: completed in this package

### Step 2. VectorFL CLI Conversational Turn Layer

- owner: VectorFL surface
- goal: let the user type a CLI conversation turn in VectorFL, not only fire a one-shot run.
- actions:
  - add a compact conversation input area to VectorFL CLI panel
  - preserve existing one-shot run path
  - show recent turns as readable cards
  - store turn artifacts in existing `runtime/cli_sessions`
- verification:
  - one read-only conversational turn runs
  - latest turn is visible without opening raw files
  - no new surface is added
- record:
  - `integrated_engine_vectorfl_cli_conversation_turn_patch_note_v0.md`
- status: completed
- verification result:
  - build passed from `app/ui/integrated_engine`
  - real read-only Codex turn passed: `cli_20260416T123507Z_64047d89`
  - mark action passed with `implementation_return`

### Step 3. Turn Route Classification

- owner: VectorFL surface
- goal: classify each CLI turn as one of a small route set.
- route set:
  - `vectorfl_reread`
  - `user_assignment_candidate`
  - `engine_request_candidate`
  - `deposit_candidate`
  - `hold`
- actions:
  - derive route from marks / suggested_next_use / user-selected route
  - show route label on the turn card
  - do not auto-promote route into action
- verification:
  - one turn can be marked as user assignment candidate
  - one turn can be marked as engine request candidate
  - route labels do not imply completion
- record:
  - `integrated_engine_cli_turn_route_classification_note_v0.md`
- status: completed
- verification result:
  - build passed from `app/ui/integrated_engine`
  - `cli_20260416T123507Z_64047d89` marked as `user_assignment_candidate`
  - `cli_20260416T123852Z_1ad257c6` marked as `engine_request_candidate`
  - route labels appear in `build_cli_host_control_state`

### Step 4. User Assignment Handoff

- owner: User surface
- goal: let a routed CLI turn become a candidate assignment to a selected team/role.
- actions:
  - select team/role from current internal team framework
  - attach CLI turn summary as assignment candidate
  - show it in User surface operation log
  - keep persistence closed unless separately opened
- verification:
  - a VectorFL turn can be sent to `내부 언어팀 / 언어담당`
  - User surface shows assignment candidate
  - detailed reread remains in VectorFL
- record:
  - `integrated_engine_user_assignment_handoff_note_v0.md`
- status: completed
- verification result:
  - build passed from `app/ui/integrated_engine`
  - `user_assignment_candidate` turn count visible from CLI host state: 1
  - User surface filters assignment candidates instead of showing every CLI turn as work
  - Internal Team Assignment Desk can attach a candidate to the selected role as local UI state

### Step 5. Engine Request Candidate Handoff

- owner: VectorFL -> Engine
- goal: let VectorFL-shaped turns become Engine request candidates without auto-execution.
- actions:
  - expose a candidate engine request card on Engine surface
  - show source turn, purpose, bounded context, and validation need
  - preserve "candidate" boundary
- verification:
  - engine request candidate appears
  - no automatic processing or deposit occurs
- record:
  - `integrated_engine_engine_request_candidate_handoff_note_v0.md`
- status: completed
- verification result:
  - build passed from `app/ui/integrated_engine`
  - engine request candidate count visible from CLI host state: 7
  - `cli_20260416T123852Z_1ad257c6` appears as `engine_request_candidate`
  - candidate cards remain non-executing and can only be sent back to VectorFL for reread

### Step 6. Engine Return To VectorFL Validation Loop

- owner: Engine -> VectorFL
- goal: make engine return material visible for VectorFL validation before user decision.
- actions:
  - connect latest engine return material to VectorFL reread queue
  - show return summary, uncertainty, and next route
  - keep user decision separate
- verification:
  - return material can be sent to VectorFL
  - VectorFL can mark validation/reread/deposit candidate
- record:
  - `integrated_engine_engine_return_vectorfl_validation_note_v0.md`
- status: completed
- verification result:
  - build passed from `app/ui/integrated_engine`
  - VectorFL Validation / Reread Queue added
  - Engine/User handoffs can be loaded back into CLI reread context
  - current engine/validation candidate source count: 7

### Step 7. Space Deposition Candidate

- owner: Engine / VectorFL
- goal: prepare deposition candidate material without automatic ingestion.
- actions:
  - collect source turn, route, result, validation note, and user decision state
  - write candidate artifact
  - show it as deposit candidate only
- verification:
  - artifact exists
  - UI says candidate, not canonical memory
- record:
  - `integrated_engine_space_deposition_candidate_note_v0.md`
- status: completed
- verification result:
  - `cli_20260416T123852Z_1ad257c6` marked as `deposit_candidate`
  - deposit candidate artifact includes `route_label`, `current_marks`, `user_decision_state`, and `canonical_deposition_state`
  - artifact explicitly says candidate only, not canonical memory

## Next Step To Start

All current checklist steps 1-7 are completed.

Next recommended mode: real UI use validation of the complete first path.

Do not jump to Gemini adapter, automatic canonical deposition, Engine auto-execution, or package 2 before the user validates the actual operating feel.
