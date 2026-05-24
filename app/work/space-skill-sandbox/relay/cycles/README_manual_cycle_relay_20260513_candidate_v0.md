# Manual Cycle Relay
# 2026-05-13 Candidate v0

## 1. Status

Document:
  candidate cycle relay support

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

Reduce user relay fatigue by grouping multiple packet-level exchanges into one manual cycle.

The cycle is a larger manual relay unit. It is meant to reduce repeated handoffs, not to automate execution.

## 3. Relation to Manual CLI Relay Surface

Manual CLI Relay Surface:
  packet-level relay

Manual Cycle Relay:
  cycle-level relay that groups packets, returns, and requests

The existing relay board and packet folders remain valid. The cycle layer only groups related work so the user can transfer fewer, larger file paths.

## 4. Core Rule

ChatGPT designs the cycle and the large-frame direction.
Codex implements the cycle files and structure.
Gemini executes/observes/verifies inside the cycle.
Gemini creates Codex requests only when structural gaps appear.
Codex processes structure requests and packages results.
Codex directly handles bounded Gemini return recovery and cycle state updates when no large-frame redesign or authority decision is required.
User manually transfers paths and approves gates.
No CLI becomes authority.

## 5. Cycle Files

Each cycle may contain:

- cycle_brief.md
- gemini_work_order.md
- codex_request_queue.md
- supervisor_checkpoint.md
- cycle_return.md

## 6. State Labels

CYCLE_DRAFT:
  cycle exists but is not ready to run.

CYCLE_READY_FOR_GEMINI:
  user may manually transfer Gemini work order.

GEMINI_RUNNING_MANUAL:
  Gemini is manually executing or observing.

GEMINI_RETURNED:
  Gemini returned a cycle result.

CODEX_REQUESTS_READY:
  Gemini identified structure requests for Codex.

CODEX_STRUCTURING_MANUAL:
  Codex is manually processing cycle structure requests.

CODEX_RETURNED:
  Codex returned structure / packaging results.

SUPERVISOR_REVIEW_NEEDED:
  ChatGPT / Supervisor needs to place the cycle.

CYCLE_PLACED_WITH_WATCH:
  cycle has been placed with watch.

CYCLE_HOLD:
  cycle is blocked until an unblock condition is met.

CYCLE_CLOSED:
  cycle is complete for now.

## 7. Do Not Promote

- cycle != workflow
- work order != automation
- request queue != registry
- checkpoint != current-position
- cycle return != baseline
- next cycle != automatic task

## 8. Watch

- cycle becoming too big
- Gemini doing structure instead of request creation
- Codex doing broad analysis instead of structure
- user still forced to relay long text
- checkpoint becoming current-position
- cycle board becoming workflow
- unnecessary ChatGPT round trips returning as relay fatigue
- Codex direct handling drifting into hidden authority
- Codex doing execution / verification that should be delegated to Gemini
- Gemini verification being mistaken for approval
