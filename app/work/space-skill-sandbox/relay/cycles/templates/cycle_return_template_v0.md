# Cycle Return Template
# Candidate v0

cycle_id:
  ...

cycle verdict:
  CYCLE_RETURNED_WITH_WATCH / CYCLE_PLACED_WITH_WATCH / WATCH_ONLY / HOLD / CYCLE_CLOSED

authority:
  return record only

not:
  baseline
  approval
  memory
  current-position
  workflow
  automation

## 1. Files

Files created:
  - ...

Files modified:
  - ...

Files inspected:
  - ...

## 2. Recovered Judgment

Recovered judgment:
  - ...

## 3. Usability

What is usable:
  - ...

What remains WATCH:
  - ...

What remains HOLD:
  - ...

## 4. Placement

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD

Reason:
  ...

## 5. Next Cycle / Next Action

Next cycle / next action:
  - ...

Manual gate:
  ...

## 6. Approval Scope

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

## 7. Hard Stop Confirmation

- no automation
- no scripts
- no current-position update
- no output_manifest update
- no baseline / workflow / registry / schema promotion
- no Big Frame Candidate Map creation unless explicitly approved
- no broad repo read
- no raw log expansion
