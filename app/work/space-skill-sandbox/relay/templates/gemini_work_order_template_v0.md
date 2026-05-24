# Gemini Work Order Template
# Candidate v0

## 1. Work Order Status

cycle_id:
  ...

work_order_id:
  ...

status:
  NOT_READY / READY_TO_SEND_TO_GEMINI / GEMINI_RUNNING_MANUAL / GEMINI_RETURNED / HOLD

target:
  Gemini

role:
  execution / observation / verification lane inside Manual Cycle Relay

authority:
  work order only

not:
  repo modification
  structure implementation
  workflow
  registry
  schema
  baseline
  automation
  current-position update
  output_manifest update
  final authority

## 2. Purpose

Purpose:
  ...

Why Gemini:
  execution / observation / broad bounded reading / evidence return / structural gap detection

What this work order should not become:
  - automation
  - broad repo search permission
  - final authority
  - structure implementation instruction

## 3. Task Bundle

Gemini should answer:

1. ...
2. ...
3. ...

## 4. Required Read Scope

Read:
  - ...

Optional only if needed:
  - ...

## 5. Do Not Read

- entire repo
- all runs
- raw logs
- broad Obsidian vault
- implementation files unless explicitly included
- output_manifest unless explicitly necessary
- current-position unless explicitly necessary
- credential / token material

## 6. Structural Gap Rule

If Gemini finds a structural gap:

Do not solve it directly.
Do not implement repo structure.

Return a Codex request entry suitable for the cycle codex_request_queue.md.

Each request should include:

- request_id
- source Gemini task
- structural_gap
- requested_codex_work
- expected_output
- priority
- forbidden_actions

## 7. Return Format

Verdict:
  GEMINI_CYCLE_RETURNED_WITH_WATCH / STRUCTURAL_GAP_FOUND / WATCH_ONLY / HOLD

Cycle:
  ...

Directly inspected:
  - ...

Not inspected:
  - ...

Main finding:
  ...

Recovered judgment candidates:
  - ...

What is usable:
  - ...

What remains WATCH:
  - ...

What remains HOLD:
  - ...

Structural gaps found:
  none / list

Codex requests needed:
  none / list

If Codex request needed:
  request_id:
  source Gemini task:
  structural_gap:
  requested_codex_work:
  expected_output:
  priority:
  forbidden_actions:

Suggested next owner:
  Codex / ChatGPT / User / HOLD

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD

Do Not Promote:
  - ...

Next action:
  ...

## 8. Hard Boundaries

- no repo modification
- no structure implementation
- no automation
- no scripts
- no current-position update
- no output_manifest update
- no baseline / workflow / registry / schema promotion
- no final authority claim

