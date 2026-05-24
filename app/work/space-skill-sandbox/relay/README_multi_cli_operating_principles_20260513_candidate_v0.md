# Multi-CLI Operating Principles
# 2026-05-13 Candidate v0

## 1. Status

Document:
  candidate operating principles

Authority:
  operating orientation only

Not:
  workflow
  registry
  schema
  baseline
  current-position
  output_manifest
  automation
  final authority

## 2. Core Role Principle

ChatGPT:
  large-frame structure design / supervisor judgment / placement / WATCH-HOLD / user-facing reframing

Codex:
  design implementation / repo-side structure / packet and cycle files / recovery packaging / bounded state updates

Gemini:
  execution / observation / verification / broad bounded reading / evidence return / structural gap detection

User:
  final judgment / direction setting / manual transfer / approval / HOLD release / promotion approval

No CLI becomes authority.

## 3. Codex Judgment Standard

Codex must hold the operating boundary.

Codex should do directly:
  - implement structures designed by ChatGPT / User
  - create and update packet / cycle / skeleton / template files
  - recover Gemini returns
  - update bounded cycle state
  - package run records
  - preserve WATCH / HOLD

Codex should delegate to Gemini:
  - execution
  - verification
  - broad bounded reading
  - repeated observation
  - dry-fill tests
  - evidence checks that would consume large context

Codex should escalate to ChatGPT / User:
  - large-frame structure design
  - conceptual reframing
  - authority / promotion decision
  - baseline / workflow / registry / schema question
  - current-position or output_manifest question
  - automation / script maturation decision
  - HOLD release
  - ambiguous direction that changes the frame

## 4. Practical Routing Test

Ask:
  Is this design, implementation, execution, or approval?

If design:
  ChatGPT / User.

If implementation:
  Codex.

If execution / verification:
  Gemini.

If approval / promotion / HOLD release:
  User, with ChatGPT support when needed.

## 5. Token Discipline

Codex implementation can consume many tokens.

Therefore:
  - Codex should not perform broad verification when Gemini can do it from a work order.
  - Gemini should not implement repo structure.
  - ChatGPT should not be used for every small return recovery.
  - User should not be forced to relay small packet decisions repeatedly.

## 6. Failure Modes

The pipeline shakes if:
  - Codex tries to become large-frame designer.
  - Gemini starts implementing repo structure.
  - ChatGPT is used for every small operational state update.
  - User becomes the packet router for every minor step.
  - execution results become approval.
  - skeleton usability becomes final map approval.

## 7. Do Not Promote

- role split != workflow
- Codex implementation != approval
- Gemini verification != truth
- ChatGPT supervision != user judgment
- User transfer != promotion
- cycle success != automation approval

