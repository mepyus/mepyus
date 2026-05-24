# Gemini Execution Packet Template
# Candidate v0

## 1. Packet Status

packet_id:
  ...

status:
  DRAFT / READY_TO_SEND / SENT_BY_USER / RETURNED_RAW / WATCH / HOLD

authority:
  execution / observation request only

not:
  approval
  workflow
  registry
  baseline
  automation
  current-position update

## 2. Purpose

purpose:
  ...

why Gemini:
  execution / observation / broad reading / evidence return

## 3. Read Scope

read:
  - ...

do_not_read:
  - broad raw logs
  - full repo
  - private notes outside explicit scope
  - linked-note context packs unless explicitly approved
  - credential / token material

smallest sufficient context rule:
  read only what is needed to answer this packet.

## 4. Task

Gemini should:
  - ...

Gemini should not:
  - modify repo files
  - create structure files
  - promote candidate to baseline
  - update current-position
  - create workflow / registry / schema / automation

## 5. Expected Return

expected return:
  observation / evidence / comparison / bounded analysis

landing zone:
  app/work/space-skill-sandbox/relay/returns/from_gemini/

## 6. Failure Condition

failure condition:
  - read scope expands beyond packet
  - result is framed as final authority
  - structure gap is solved directly instead of requested from Codex
  - output implies baseline / workflow / automation approval

## 7. Structural Gap Rule

If structural gap appears:
  create a Gemini-to-Codex Structure Request using:
  app/work/space-skill-sandbox/relay/templates/gemini_to_codex_structure_request_template_v0.md

Gemini should request structure work instead of performing it directly.

## 8. Hard Boundaries

- no repo modification
- no baseline / workflow / registry / schema promotion
- no current-position update
- no output_manifest update
- no automation proposal as next action unless explicitly asked
- no credential or token handling

## 9. Return Format

Verdict:
  ...

Files inspected:
  - ...

Observation:
  - ...

Evidence:
  - ...

Structural gaps:
  - ...

Codex request needed:
  YES / NO

Placement suggestion:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH / HOLD

Hard stop confirmation:
  - no repo modification
  - no promotion
  - no automation

