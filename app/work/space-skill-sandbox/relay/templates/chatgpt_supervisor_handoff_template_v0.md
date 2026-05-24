# ChatGPT Supervisor Handoff Template
# Candidate v0

## 1. Handoff Status

handoff_id:
  ...

status:
  READY_TO_SEND / SENT_BY_USER / SUPERVISOR_REVIEWED / WATCH / HOLD / CLOSED

target:
  ChatGPT / Supervisor

authority:
  review request only

not:
  approval
  baseline
  workflow
  registry
  schema
  current-position update
  automation
  execution trigger

## 2. Why This Handoff Exists

Reason:
  ...

Decision needed:
  ...

What should not happen yet:
  - ...

## 3. Current Relay State

Relevant packets:
  - ...

Current board state:
  - ...

HOLD items:
  - ...

## 4. Evidence / Returns To Review

User-provided return:
  ...

Files / packet paths:
  - ...

What was not done:
  - ...

## 5. Supervisor Questions

Ask ChatGPT to decide:

1. Is this return usable?
2. What is the placement?
3. Should the next packet remain DRAFT, move to READY_TO_SEND, or stay HOLD?
4. What remains WATCH?
5. What remains HOLD?
6. Is explicit user approval required before execution?
7. What should Codex do next, if anything?

## 6. Required ChatGPT Return Format

Verdict:
  USE_WITH_WATCH / READY_TO_SEND_WITH_WATCH / KEEP_HOLD / WATCH_ONLY / HOLD

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD

Relay board update:
  ...

Packet state recommendation:
  DRAFT / READY_TO_SEND / HOLD / CLOSED

What is usable:
  - ...

What remains WATCH:
  - ...

What remains HOLD:
  - ...

User judgment needed:
  - ...

Codex next action:
  - ...

Do Not Promote:
  - ...

Hard stop:
  - no automation
  - no current-position update
  - no output_manifest update
  - no baseline / workflow / registry / schema promotion

