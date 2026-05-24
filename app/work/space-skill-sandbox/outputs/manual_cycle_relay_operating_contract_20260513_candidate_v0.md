# Manual Cycle Relay Operating Contract
# 2026-05-13 Candidate v0

## 1. Status

Document:
  candidate manual cycle relay operating contract

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

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH

## 2. Purpose

Define how a manual cycle should operate so the user can transfer paths instead of long prompts.

## 3. Cycle Files

Each cycle may contain:

- cycle_brief.md
- gemini_work_order.md
- codex_request_queue.md
- supervisor_checkpoint.md
- cycle_return.md

## 4. File Contracts

### cycle_brief.md

Owner:
  ChatGPT / Codex setup

Reader:
  User / Codex / Gemini when orienting cycle purpose

Writer:
  Codex implements from ChatGPT / User design

State labels:
  CYCLE_DRAFT / CYCLE_READY_FOR_GEMINI / CYCLE_HOLD / CYCLE_CLOSED

Purpose:
  define cycle goal, boundaries, lanes, user gate

Must not become:
  final operating model
  current-position
  automatic task plan

### gemini_work_order.md

Owner:
  Codex setup from ChatGPT design

Reader:
  Gemini

Writer:
  Codex

State labels:
  NOT_READY / READY_TO_SEND_TO_GEMINI / GEMINI_RUNNING_MANUAL / GEMINI_RETURNED / HOLD

Purpose:
  tell Gemini what to execute / observe

Must not become:
  automation
  final authority
  broad repo search permission

### codex_request_queue.md

Owner:
  Gemini may add requests; Codex processes after approval

Reader:
  Codex / ChatGPT / User

Writer:
  Gemini proposes entries; Codex may update status after approved processing

State labels:
  EMPTY / CODEX_REQUESTS_READY / CODEX_STRUCTURING_MANUAL / CODEX_RETURNED / HOLD

Purpose:
  collect structure gaps

Must not become:
  registry
  backlog
  automatic task queue

### supervisor_checkpoint.md

Owner:
  ChatGPT / Supervisor

Reader:
  ChatGPT / User / Codex

Writer:
  ChatGPT or Codex for bounded placement when no authority change is involved

State labels:
  NOT_STARTED / SUPERVISOR_REVIEW_NEEDED / CYCLE_PLACED_WITH_WATCH / CYCLE_HOLD / CYCLE_CLOSED

Purpose:
  review cycle return and decide placement

Must not become:
  current-position
  baseline approval
  hidden authority

### cycle_return.md

Owner:
  ChatGPT / Codex after review

Reader:
  User / ChatGPT / Codex / Gemini when next cycle needs context

Writer:
  Codex for bounded recovery; ChatGPT for large-frame placement

State labels:
  NOT_STARTED / GEMINI_RETURNED / CYCLE_RETURNED_WITH_WATCH / CYCLE_CLOSED_WITH_WATCH / HOLD

Purpose:
  record cycle-level recovered judgment

Must not become:
  automatic memory
  official history
  baseline

## 5. Cycle State Labels

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
  Codex is manually processing approved cycle structure requests.

CODEX_RETURNED:
  Codex returned structure / packaging results.

SUPERVISOR_REVIEW_NEEDED:
  ChatGPT / Supervisor needs to place the cycle, or Codex needs explicit boundary to handle a bounded placement.

CYCLE_PLACED_WITH_WATCH:
  cycle has been placed with watch.

CYCLE_HOLD:
  cycle is blocked until an unblock condition is met.

CYCLE_CLOSED:
  cycle is complete for now.

## 6. Standard Manual Cycle Flow

1. ChatGPT designs cycle.
2. Codex creates cycle files.
3. User gives gemini_work_order path to Gemini.
4. Gemini returns one cycle-level result.
5. If structural gap exists, Gemini provides Codex request entries.
6. ChatGPT reviews return, or Codex handles bounded recovery when no authority change is involved.
7. User approves next gate if needed.
8. Codex processes approved structure requests.
9. Cycle closes with WATCH / HOLD / placement.

Important:
  This is a guide, not a mandatory workflow.

## 7. Compressed Approval Rule

Compressed user commands such as "실행해," "계속," or "진행해" must be interpreted only inside the current cycle context.

They do not automatically approve:

- baseline promotion
- workflow creation
- registry creation
- automation
- current-position update
- output_manifest update
- next cycle execution
- product architecture
- broad repo read

Each compressed approval must record:

- user_instruction_raw
- interpreted_approval_scope
- not_approved_items
- stop_condition
- approval_recorded_by
- approval_scope_watch

Meaning:
  The exact user phrase should be preserved, and the allowed scope should be stated narrowly.

Watch:
  compressed approval must not become blanket approval.

## 8. Failure Conditions

Cycle fails if:

- user must still copy long prompts repeatedly
- Gemini splits the task into many small relays
- Codex performs broad analysis instead of structure
- checkpoint becomes current-position
- request queue becomes backlog/registry
- cycle return becomes baseline
- next cycle becomes automatic

## 9. Do Not Promote

- cycle != workflow
- work order != automation
- request queue != registry
- checkpoint != current-position
- cycle return != baseline
- next cycle != automatic task
