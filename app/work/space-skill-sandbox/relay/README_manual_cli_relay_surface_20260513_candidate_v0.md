# Manual CLI Relay Surface
# 2026-05-13 Candidate v0

## 1. Status

Document:
  candidate manual relay surface

Authority:
  setup support only

Not:
  automation
  workflow
  registry
  schema
  baseline
  current-position
  output_manifest
  routing authority

## 2. Purpose

Reduce manual relay fatigue while preserving user judgment and tool role separation.

This surface lets the user pass file paths and packet ids instead of repeatedly copying long prompt context.

## 3. Role Split

Gemini:
  execution / observation / verification / broad bounded reading / evidence return

Codex:
  design implementation / structure / packaging / recovery / packet setup

ChatGPT:
  large-frame structure design / supervisor / placement / packet authoring for authority decisions

User:
  final judgment / manual transfer / promotion approval

Codex delegated handling:
  Codex may directly recover Gemini returns and update bounded relay/cycle files when no large-frame redesign, promotion, automation, current-position update, or HOLD release is involved.

Routing standard:
  ChatGPT designs the big frame.
  Codex implements the design.
  Gemini executes and verifies.
  User approves direction and releases HOLD.

## 4. Core Relay Rule

Gemini executes and observes.
Codex structures and packages.
ChatGPT supervises and places.
User approves and transfers.
Files carry context.
No CLI becomes authority.

## 5. Standard Flow

1. ChatGPT creates packet.
2. User transfers packet/path to target CLI.
3. Target CLI returns result.
4. Codex directly packages bounded returns when no large-frame or authority decision is required.
5. ChatGPT reviews results only when placement changes authority, releases HOLD, changes the big frame, or requires user-facing judgment.
6. Gemini creates Codex request only when structural gap appears.

## 6. State Labels

DRAFT:
  packet is being prepared.

READY_TO_SEND:
  user can transfer the packet/path to the target CLI.

SENT_BY_USER:
  user has manually relayed the packet/path.

RETURNED_RAW:
  CLI result has returned but has not been supervisor-reviewed.

SUPERVISOR_REVIEWED:
  ChatGPT has reviewed the result for placement.

READY_FOR_CODEX_RECOVERY:
  reviewed return can be packaged by Codex.

READY_FOR_GEMINI_EXECUTION:
  packet is ready for Gemini execution or observation.

PACKAGED_WITH_WATCH:
  Codex packaged the result as candidate material with watch.

PLACED_WITH_WATCH:
  supervisor placed the material with watch.

WATCH:
  useful or relevant, but should not advance without explicit care.

HOLD:
  do not proceed until an unblock condition is met.

CLOSED:
  relay item is complete for now.

## 7. Do Not Promote

- relay board != workflow
- packet template != automation
- Gemini return != truth
- Codex return != approval
- ChatGPT placement != baseline
- user transfer != promotion
- next action != automatic task

## 8. Watch

- relay structure becoming another document pile
- user still forced to copy long prompts
- Gemini producing structure instead of request packet
- Codex doing broad analysis instead of structure
- board becoming current-position
- packets becoming hidden workflow
