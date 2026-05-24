# Gemini Work Order Template
# Candidate v0

cycle_id:
  ...

status:
  NOT_READY / READY_FOR_GEMINI / GEMINI_RUNNING_MANUAL / GEMINI_RETURNED / HOLD

target Gemini role:
  execution / observation / broad reading / evidence return

authority:
  work order only

not:
  repo modification
  structure implementation
  final authority
  workflow
  baseline
  automation

## 1. Task Bundle

Tasks:

1. ...
2. ...
3. ...

## 2. Read Scope

Read:
  - ...

Optional if needed:
  - ...

## 3. Do Not Read

- entire repo
- all runs
- raw logs
- broad Obsidian vault
- implementation files unless explicitly included
- current-position unless explicitly included
- output_manifest unless explicitly included
- credential / token material

## 4. Execution / Observation Tasks

Gemini should:
  - ...

Gemini should not:
  - modify repo files
  - implement structure
  - create workflow / registry / schema
  - promote candidate to baseline
  - request user confirmation after every small observation

## 5. Structural Gap Rule

If a structural gap appears:
  do not solve it directly.

Instead:
  add a request to the cycle codex_request_queue.md format, or return a Gemini-to-Codex request suitable for that queue.

## 6. Codex Request Creation Rule

Each Codex request should include:

- request_id
- source Gemini task
- structural gap
- requested Codex work
- expected output
- forbidden actions
- priority

## 7. Return Format

Verdict:
  GEMINI_CYCLE_RETURNED_WITH_WATCH / CODEX_REQUESTS_READY / WATCH_ONLY / HOLD

Directly inspected:
  - ...

Not inspected:
  - ...

Observations:
  - ...

Codex requests:
  - ...

WATCH:
  - ...

HOLD:
  - ...

Placement suggestion:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD

## 8. Hard Boundaries

- no repo modification
- no automation
- no current-position update
- no output_manifest update
- no baseline / workflow / registry / schema promotion
- no broad raw log expansion

