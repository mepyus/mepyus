# Operating Principle Task Inventory
# 2026-05-13 Candidate v0

## 1. Status

Document:
  candidate task inventory

Source:
  Operating Principle Layer Separation Pack v0

Authority:
  planning / orientation only

Not:
  workflow
  automation
  registry
  backlog
  baseline
  current-position
  output_manifest

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH

## 2. Purpose

Turn the operating contracts into an actionable but non-automatic task inventory.

This inventory helps decide:

- what Codex should implement directly
- what Gemini should execute / verify
- what ChatGPT / User must decide
- what remains WATCH
- what remains HOLD

## 3. Routing Rule

Design:
  ChatGPT / User

Implementation:
  Codex

Execution / verification:
  Gemini

Approval / HOLD release / promotion:
  User, with ChatGPT support when needed

## 4. Task Groups

### Group A. Contract Usability Verification

Goal:
  Verify whether the new layer / term / lane / cycle contracts are usable for real execution.

Primary owner:
  Gemini

Codex role:
  create a Gemini work order and recover the return

Suggested cycle:
  cycle_003_operating_contract_usability_check

Tasks:

| task_id | task | owner | status | output | watch |
|---|---|---|---|---|---|
| A1 | Create Cycle 003 folder and work order for Gemini contract usability check | Codex | READY_CANDIDATE | cycle files | do not turn into workflow |
| A2 | Gemini reads the four operating contract files and checks execution clarity | Gemini | WAITING_FOR_WORK_ORDER | Gemini cycle return | Gemini verification is not approval |
| A3 | Recover Gemini return into cycle_return and checkpoint | Codex | WAITING_FOR_RETURN | recovered cycle result | Codex recovery is not final authority |

HOLD:
  none, unless user wants to pause contract testing.

### Group B. Term Collision Test

Goal:
  Test whether ambiguous terms can be interpreted by layer without collapsing into schema or workflow.

Primary owner:
  Gemini

Codex role:
  provide a bounded dry-fill skeleton

Suggested cycle:
  cycle_004_term_collision_dry_run

Tasks:

| task_id | task | owner | status | output | watch |
|---|---|---|---|---|---|
| B1 | Create a small term-collision test sheet using 5-7 terms | Codex | CANDIDATE | dry test file | term table must not become ontology |
| B2 | Gemini classifies each term by layer and flags ambiguity | Gemini | WAITING_FOR_WORK_ORDER | evidence return | Gemini result is not final vocabulary |
| B3 | Codex recovers ambiguity list into WATCH / usable distinctions | Codex | WAITING_FOR_RETURN | recovered judgment | no baseline vocabulary |

HOLD:
  final vocabulary approval.

### Group C. Lane Contract Stress Test

Goal:
  Test if a realistic mixed request can be routed to ChatGPT / Codex / Gemini / User without role confusion.

Primary owner:
  Gemini for verification, Codex for structure

Codex role:
  create test cases and a Gemini work order

Suggested cycle:
  cycle_005_lane_contract_stress_test

Tasks:

| task_id | task | owner | status | output | watch |
|---|---|---|---|---|---|
| C1 | Create 6 mixed-task scenarios from recent relay work | Codex | CANDIDATE | scenario sheet | do not invent broad history |
| C2 | Gemini routes each scenario to owner lane and flags uncertainty | Gemini | WAITING_FOR_WORK_ORDER | lane test return | routing is not authority |
| C3 | Codex updates lane contract only if ambiguity is structural and bounded | Codex | WAITING_FOR_RETURN | patch or WATCH note | no hidden supervisor |

HOLD:
  any role change requiring ChatGPT / User judgment.

### Group D. Manual Cycle Contract Trial

Goal:
  Use the Manual Cycle Relay Operating Contract to run a larger practical cycle without many small handoffs.

Primary owner:
  Codex for setup, Gemini for execution

Suggested cycle:
  cycle_006_cycle_contract_practical_trial

Tasks:

| task_id | task | owner | status | output | watch |
|---|---|---|---|---|---|
| D1 | Create a cycle using the operating contract exactly | Codex | CANDIDATE | cycle files | cycle must not become workflow |
| D2 | Gemini executes one bundled observation from the cycle work order | Gemini | WAITING_FOR_WORK_ORDER | cycle-level return | no task splitting into many relays |
| D3 | Codex recovers result and measures relay reduction qualitatively | Codex | WAITING_FOR_RETURN | cycle_return | do not claim automation |

HOLD:
  automation / scripts.

### Group E. Big Frame Map Gate

Goal:
  Decide whether existing evidence is enough to release HOLD for a Big Frame Candidate Map draft.

Primary owner:
  User + ChatGPT

Codex role:
  preserve evidence and prepare decision packet only if asked

Tasks:

| task_id | task | owner | status | output | watch |
|---|---|---|---|---|---|
| E1 | Prepare concise evidence packet for map draft HOLD release decision | Codex | HOLD_UNTIL_REQUESTED | decision packet | packet is not approval |
| E2 | Decide whether to release HOLD for map draft execution | User + ChatGPT | HOLD | explicit decision | HOLD release must be recorded |
| E3 | If approved, execute existing map draft packet or create revised cycle | Codex / Gemini as assigned | HOLD | map draft or cycle | no final framework |

HOLD:
  final Big Frame Candidate Map creation and map draft execution until explicit user approval.

### Group F. Automation Maturity Watch

Goal:
  Track scriptability without creating scripts prematurely.

Primary owner:
  User + ChatGPT for maturity decision, Codex for notes

Tasks:

| task_id | task | owner | status | output | watch |
|---|---|---|---|---|---|
| F1 | Note repeated manual steps from cycles 003-006 | Codex | WATCH | scriptability notes | observation only |
| F2 | Identify which steps are stable enough to consider helper scripts | Gemini / Codex | WATCH | evidence summary | no script yet |
| F3 | User decides whether any helper script is allowed | User | HOLD | approval or hold | automation requires explicit approval |

HOLD:
  all automation / scripts.

## 5. Recommended Next Task

Recommended next task:
  A1 - Create Cycle 003 folder and work order for Gemini contract usability check.

Reason:
  The operating contracts were just created.
  Before using them as an operating surface, Gemini should verify whether they are clear enough for execution / observation and where role confusion remains.

Next owner:
  Codex

Suggested cycle:
  cycle_003_operating_contract_usability_check

Do not do yet:
  - Big Frame Candidate Map creation
  - map draft execution
  - automation
  - current-position update
  - output_manifest update

## 6. Do Not Promote

- task inventory != backlog
- recommended task != automatic next task
- Gemini verification != approval
- Codex implementation != authority
- User approval remains required for HOLD release

## 7. Watch

- inventory becoming backlog / registry
- task groups becoming workflow
- recommended next task becoming automatic
- Codex doing Gemini verification directly
- User being pulled back into relay-worker role

