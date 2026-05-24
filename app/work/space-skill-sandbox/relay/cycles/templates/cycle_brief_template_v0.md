# Cycle Brief Template
# Candidate v0

cycle_id:
  ...

status:
  CYCLE_DRAFT / CYCLE_READY_FOR_GEMINI / CYCLE_HOLD / CYCLE_CLOSED

authority:
  cycle planning support only

not:
  workflow
  automation
  registry
  baseline
  current-position
  execution approval

## 1. Purpose

Purpose:
  ...

Large-frame layer:
  ...

Why this should be a cycle instead of a packet:
  ...

## 2. This Cycle Will Do

- ...

## 3. This Cycle Will Not Do

- create automation
- create scripts
- update current-position
- update output_manifest
- promote workflow / registry / schema / baseline
- execute unapproved map / artifact / product work

## 4. Lanes

Gemini lane:
  ...

Codex lane:
  ...

ChatGPT / Supervisor lane:
  ...

User gate:
  ...

## 5. Approval Scope

user_instruction_raw:
  ...

interpreted_approval_scope:
  ...

not_approved_items:
  ...

stop_condition:
  ...

approval_recorded_by:
  ChatGPT / Supervisor / Codex / Gemini / User

approval_scope_watch:
  compressed approval must not become blanket approval

## 6. Hard Stops

- ...

## 7. Expected Cycle Return

Expected return:
  ...

Placement options:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD
