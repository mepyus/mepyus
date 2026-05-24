# Gemini Work Order
# cycle_003_operating_contract_usability_check

cycle_id:
  cycle_003_operating_contract_usability_check

status:
  READY_TO_SEND_TO_GEMINI

target:
  Gemini

role:
  execution / observation / verification lane inside Manual Cycle Relay

authority:
  cycle work order only

not:
  workflow
  registry
  schema
  baseline
  automation
  current-position update
  output_manifest update
  final operating model
  final authority

## 1. Task

Read the Operating Principle Layer Separation Pack and verify whether it is usable for real execution / observation without role or term confusion.

You are not asked to rewrite the contracts.
You are not asked to implement structure.
You are not asked to approve the contracts as baseline.

## 2. Required Read Scope

Read these files:

- app/work/space-skill-sandbox/outputs/operating_principle_layer_separation_map_20260513_candidate_v0.md
- app/work/space-skill-sandbox/outputs/operating_term_disambiguation_table_20260513_candidate_v0.md
- app/work/space-skill-sandbox/outputs/codex_gemini_chatgpt_lane_contract_20260513_candidate_v0.md
- app/work/space-skill-sandbox/outputs/manual_cycle_relay_operating_contract_20260513_candidate_v0.md
- app/work/space-skill-sandbox/outputs/operating_principle_task_inventory_20260513_candidate_v0.md

Optional only if needed:

- app/work/space-skill-sandbox/relay/README_multi_cli_operating_principles_20260513_candidate_v0.md
- app/work/space-skill-sandbox/relay/README_codex_delegated_return_handling_20260513_candidate_v0.md
- app/work/space-skill-sandbox/relay/cycles/README_manual_cycle_relay_20260513_candidate_v0.md

## 3. Do Not Read

- entire repo
- all runs
- raw logs
- broad Obsidian vault
- implementation files
- output_manifest unless explicitly necessary
- current-position unless explicitly necessary
- credential / token material

## 4. Questions To Answer

Answer:

1. Are the layer, term, lane, and cycle contracts clear enough for Gemini execution / observation?
2. Which contract is most usable immediately?
3. Which contract is most ambiguous for Gemini?
4. Are any terms still likely to collapse across layers?
5. Are lane boundaries clear enough to prevent Gemini from implementing structure directly?
6. Are Codex responsibilities clear enough to prevent broad Gemini-style analysis by Codex?
7. Are User and ChatGPT approval / design gates clear enough?
8. What remains WATCH?
9. What remains HOLD?
10. Are there structural gaps requiring Codex?

## 5. Structural Gap Rule

If you find a structure gap:

Do not solve it directly.

Return a Codex request entry suitable for:

app/work/space-skill-sandbox/relay/cycles/cycle_003_operating_contract_usability_check/codex_request_queue.md

Each request should include:

- request_id
- structural_gap
- requested_codex_work
- expected_output
- priority
- forbidden_actions

Codex should not act until user transfers this queue or a bounded Codex recovery step is approved.

## 6. Required Return Format

Verdict:
  GEMINI_CYCLE_003_CONTRACT_USABILITY_RETURNED_WITH_WATCH / STRUCTURAL_GAP_FOUND / WATCH_ONLY / HOLD

Cycle:
  cycle_003_operating_contract_usability_check

Directly inspected:
  - ...

Not inspected:
  - ...

Contract usability:
  ...

Most usable contract:
  ...

Most ambiguous contract:
  ...

Term collision risks:
  - ...

Lane clarity:
  ...

Cycle clarity:
  ...

User / ChatGPT gate clarity:
  ...

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

## 7. Hard Boundaries

- no repo modification
- no structure implementation
- no baseline / workflow / registry / schema promotion
- no current-position update
- no output_manifest update
- no automation or script recommendation as immediate next action
- no final authority claim

