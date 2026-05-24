# Codex Structure Packet Template
# Candidate v0

## 1. Packet Status

packet_id:
  ...

status:
  DRAFT / READY_FOR_CODEX_RECOVERY / READY_TO_SEND / PACKAGED_WITH_WATCH / WATCH / HOLD

authority:
  structure / packaging request only

not:
  approval
  workflow
  registry
  schema
  baseline
  automation
  current-position update

## 2. Source Request

source request:
  ...

source return:
  ...

review status:
  SUPERVISOR_REVIEWED / NOT_REVIEWED / UNKNOWN

## 3. Structure Task

Codex should:
  - ...

Codex should not:
  - perform broad Gemini-style analysis
  - expand raw logs
  - read the whole repo
  - treat worker / Gemini / ChatGPT return as truth
  - promote candidate to baseline
  - create workflow / registry / schema / automation

## 4. Allowed Files

allowed create / modify paths:
  - ...

allowed inspect paths:
  - ...

## 5. Forbidden Actions

- no current-position update
- no output_manifest update unless explicitly approved
- no baseline / workflow / registry / schema promotion
- no automation / script / watcher creation
- no Big Frame Candidate Map creation unless explicitly packeted
- no credential or token handling

## 6. Expected Output

expected output file:
  ...

optional run record:
  app/work/space-skill-sandbox/runs/run_XXX_...

placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH / HOLD

## 7. Run Record Rule

Create a run record only when it follows existing repo convention and stays short.

Run record is not memory.
Run record is not approval.

## 8. Hard Stop Confirmation

Confirm:
  - no automation
  - no current-position update
  - no output_manifest update
  - no baseline / workflow / registry / schema promotion
  - no broad repo read
  - no raw log expansion

## 9. Return Format

Verdict:
  ...

Files created:
  - ...

Files modified:
  - ...

Files inspected:
  - ...

Recovered / structured judgment:
  - ...

What is usable:
  - ...

What remains WATCH:
  - ...

What remains HOLD:
  - ...

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH / HOLD

Next action:
  - ...

Hard stop confirmation:
  - ...

