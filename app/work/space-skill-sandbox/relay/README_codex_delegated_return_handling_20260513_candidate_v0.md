# Codex Delegated Return Handling
# 2026-05-13 Candidate v0

## 1. Status

Document:
  candidate operating delegation note

Authority:
  setup support / operating orientation only

Not:
  workflow
  registry
  schema
  baseline
  current-position
  output_manifest
  automation
  final authority

## 2. Purpose

Reduce unnecessary ChatGPT round trips while preserving the role split:

ChatGPT:
  large-frame structure design

Codex:
  design implementation

Gemini:
  related execution / observation / verification

User:
  approval / direction / HOLD release

Codex should directly handle Gemini return recovery and bounded structure implementation when the task does not require large-frame redesign, promotion, baseline movement, current-position update, automation, or user approval.

## 3. Delegation Rule

Codex handles directly:
  - Gemini return recovery
  - cycle_return updates
  - supervisor_checkpoint updates
  - codex_request_queue updates
  - run record creation
  - bounded structure files
  - template / packet / skeleton implementation
  - WATCH / HOLD preservation

Codex delegates to Gemini:
  - execution
  - broad bounded verification
  - repeated observation
  - dry-fill tests
  - evidence checks that would consume large context

ChatGPT / Supervisor is needed for:
  - large-frame redesign
  - promotion / baseline decision
  - workflow / registry / schema question
  - current-position update question
  - automation or script maturation decision
  - ambiguous user direction
  - user-facing conceptual reframing

User is needed for:
  - final approval
  - HOLD release
  - map draft execution approval
  - baseline / workflow / registry promotion
  - automation approval

## 4. Practical Rule

If the next step is recovery, packaging, cycle state update, or bounded repo structure:
  Codex proceeds.

If the next step is execution, verification, dry-fill, or broad bounded observation:
  Codex writes a Gemini work order and lets Gemini execute.

If the next step changes the big frame, promotes authority, or releases HOLD:
  stop for User / ChatGPT judgment.

## 5. Do Not Promote

- Codex handling != final authority
- return recovery != baseline
- cycle close != promotion
- WATCH placement != approval
- HOLD release requires explicit user judgment
- direct handling != automation
- Gemini execution != approval
- ChatGPT design != user approval

## 6. Watch

- Codex becoming hidden supervisor
- fewer handoffs becoming weaker judgment
- cycle close hiding unresolved HOLD
- structure implementation drifting into big-frame redesign
- Codex consuming verification tokens that should be delegated to Gemini
- Gemini verification being mistaken for approval
