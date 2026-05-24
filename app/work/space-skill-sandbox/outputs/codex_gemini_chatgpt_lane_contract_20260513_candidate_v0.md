# Codex / Gemini / ChatGPT Lane Contract
# 2026-05-13 Candidate v0

## 1. Status

Document:
  candidate lane contract

Authority:
  operating guide with watch

Not:
  workflow
  automation
  hierarchy
  final authority model
  role registry
  baseline

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH

## 2. Purpose

Prevent role confusion between:

- ChatGPT / Supervisor
- Codex
- Gemini
- User

## 3. Lane Summary

ChatGPT / Supervisor:
  large-frame design
  placement
  WATCH / HOLD
  packet authoring
  cycle design
  return judgment

Codex:
  repo-side structure implementation
  file creation
  packet / cycle / board setup
  recovery packaging
  request queue processing

Gemini:
  execution
  observation
  broad reading
  evidence return
  structural gap detection

User:
  final judgment
  explicit approval
  manual transfer
  promotion authority

## 4. Allowed / Forbidden Table

| Lane | Allowed | Forbidden | Return Format | Failure Condition |
|---|---|---|---|---|
| ChatGPT / Supervisor | large-frame design; placement; WATCH/HOLD; packet and cycle design; return judgment | must not get pulled into endless local correction before large-frame placement; must not replace user approval | supervisor verdict; placement; WATCH/HOLD; next owner | ChatGPT becomes hidden final authority or local editor for every small update |
| Codex | repo-side structure implementation; file creation; packet/cycle/board setup; recovery packaging; request queue processing | must not do broad Gemini-style analysis; must not promote candidate to baseline; must not update current-position unless explicitly approved | files created/modified; recovered judgment; placement with watch; hard stops | Codex becomes large-frame designer or treats structure as approval |
| Gemini | execution; observation; broad bounded reading; evidence return; structural gap detection | must not implement structure directly; must not create baseline/workflow/schema; must not treat observation as final authority | observation verdict; inspected files; evidence; structural gaps; Codex requests if needed | Gemini output becomes truth or Gemini edits structure directly |
| User | final judgment; explicit approval; manual transfer; promotion authority; HOLD release | should not be forced back into long-prompt relay worker role | approval / direction / HOLD release / promotion decision | user becomes packet router instead of direction holder |

## 5. Structural Gap Rule

If Gemini finds structure gap:
  Gemini creates Codex request entry.
  Gemini does not solve directly.

If Codex finds meaning ambiguity:
  Codex reports ambiguity.
  Codex does not decide meaning.

If ChatGPT sees over-promotion:
  ChatGPT marks WATCH / HOLD.

If User approves promotion:
  explicit approval must be recorded.

## 6. Do Not Promote

- lane contract != hierarchy
- lane contract != automation
- lane contract != rigid workflow
- ChatGPT supervisor != final authority
- Gemini observation != truth
- Codex structure != approval
- User transfer != promotion

