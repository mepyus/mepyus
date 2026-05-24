# CLI Return Template
# Candidate v0

## 1. Return Status

return_id:
  ...

source_cli:
  Gemini / Codex / ChatGPT / worker

source_packet:
  ...

state:
  RETURNED_RAW / SUPERVISOR_REVIEWED / PACKAGED_WITH_WATCH / WATCH / HOLD / CLOSED

Authority:
  return only

Not:
  truth
  approval
  baseline
  workflow
  registry
  automation
  memory

## 2. Verdict

Verdict:
  ...

## 3. Files

Files created:
  - ...

Files modified:
  - ...

Files inspected:
  - ...

## 4. Recovered Judgment

Recovered judgment:
  - ...

## 5. Usability

What is usable:
  - ...

What remains WATCH:
  - ...

What remains HOLD:
  - ...

## 6. Placement

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD

Do not use as:
  - approval
  - baseline
  - current-position
  - automation trigger

## 7. Next Action

Next action:
  - ...

Manual transfer needed:
  YES / NO

Target CLI:
  Gemini / Codex / ChatGPT / none

## 8. Hard Stop Confirmation

Hard stop confirmation:
  - no automation
  - no current-position update
  - no output_manifest update
  - no baseline / workflow / registry / schema promotion
  - no broad repo read unless explicitly packeted
  - no raw log expansion unless explicitly packeted

