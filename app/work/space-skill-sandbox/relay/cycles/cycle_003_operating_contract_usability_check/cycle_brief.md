# Cycle Brief
# cycle_003_operating_contract_usability_check

cycle_id:
  cycle_003_operating_contract_usability_check

status:
  CYCLE_READY_FOR_GEMINI

authority:
  manual cycle setup only

not:
  workflow
  registry
  schema
  baseline
  automation
  current-position update
  output_manifest update
  final operating model

## 1. Purpose

Ask Gemini to verify whether the Operating Principle Layer Separation Pack is usable for real execution / observation without role or term confusion.

This cycle tests contract usability.
It does not promote the contracts to baseline.

## 2. This Cycle Will Do

- provide Gemini a bounded work order
- ask Gemini to inspect four operating contract files
- ask Gemini to identify unclear terms, lane confusion, or execution-blocking gaps
- ask Gemini to return one cycle-level observation
- ask Gemini to provide Codex request entries only if structure work is needed

## 3. This Cycle Will Not Do

- rewrite the operating principles
- promote any contract to baseline
- create workflow / registry / schema
- create automation or scripts
- update current-position
- update output_manifest
- create or approve Big Frame Candidate Map

## 4. Lanes

Gemini lane:
  execution / observation / verification of contract usability

Codex lane:
  cycle setup and later return recovery; process request queue only if Gemini creates requests and user / supervisor approves

ChatGPT / Supervisor lane:
  large-frame redesign only if Gemini finds conceptual ambiguity requiring design judgment

User gate:
  manual transfer of gemini_work_order path to Gemini
  explicit approval required for any HOLD release or promotion

## 5. Hard Stops

- no automation
- no scripts
- no current-position update
- no output_manifest update
- no baseline / workflow / registry / schema promotion
- no final Big Frame Candidate Map creation

## 6. Expected Cycle Return

Expected cycle return:
  Gemini contract usability observation with WATCH / HOLD and structural-gap status

Placement options:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD

