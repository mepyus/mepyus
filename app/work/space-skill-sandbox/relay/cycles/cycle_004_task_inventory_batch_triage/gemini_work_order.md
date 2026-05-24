# Gemini Work Order
# cycle_004_task_inventory_batch_triage

cycle_id:
  cycle_004_task_inventory_batch_triage

status:
  READY_TO_SEND_TO_GEMINI

target:
  Gemini

role:
  execution / observation / batch triage lane inside Manual Cycle Relay

authority:
  cycle work order only

not:
  workflow
  backlog
  registry
  automation
  baseline
  current-position update
  output_manifest update
  final authority

## 1. Task

Read the full operating task inventory and routing contracts.

Then perform one batch triage:

1. For each task group A-F, decide whether it is:
   - executable by Gemini now
   - needs Codex setup
   - needs ChatGPT / User design judgment
   - must remain HOLD
   - should be WATCH only

2. Execute only bounded verification tasks that can be done from the provided documents without new Codex setup.

3. If a task needs Codex setup, do not solve it directly. Return a Codex request entry suitable for codex_request_queue.md.

4. Preserve all HOLD gates.

5. Return one consolidated cycle-level result.

This cycle exists to reduce small relay loops.

## 2. Required Read Scope

Read:

- app/work/space-skill-sandbox/outputs/operating_principle_task_inventory_20260513_candidate_v0.md
- app/work/space-skill-sandbox/outputs/operating_principle_layer_separation_map_20260513_candidate_v0.md
- app/work/space-skill-sandbox/outputs/operating_term_disambiguation_table_20260513_candidate_v0.md
- app/work/space-skill-sandbox/outputs/codex_gemini_chatgpt_lane_contract_20260513_candidate_v0.md
- app/work/space-skill-sandbox/outputs/manual_cycle_relay_operating_contract_20260513_candidate_v0.md
- app/work/space-skill-sandbox/relay/templates/gemini_work_order_template_v0.md

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

## 4. Batch Triage Rules

For each group:

Group A - Contract Usability Verification:
  Already largely executed in Cycle 003.
  Verify whether any residual action remains.

Group B - Term Collision Test:
  If possible from current term table, perform a small bounded dry classification using 5-7 terms.
  If a separate test sheet is necessary, create a Codex request instead.

Group C - Lane Contract Stress Test:
  If test scenarios are not present, create a Codex request for scenario sheet setup.
  Do not invent broad history.

Group D - Manual Cycle Contract Trial:
  Determine whether this needs Codex setup before Gemini can execute.

Group E - Big Frame Map Gate:
  Keep HOLD unless explicit user approval exists.

Group F - Automation Maturity Watch:
  Keep WATCH/HOLD.
  Do not recommend scripts as immediate next action.

## 5. Structural Gap Rule

If you find a structure gap:

Do not solve it directly.
Do not implement repo structure.

Return a Codex request entry suitable for:

app/work/space-skill-sandbox/relay/cycles/cycle_004_task_inventory_batch_triage/codex_request_queue.md

Each request should include:

- request_id
- source task group
- structural_gap
- requested_codex_work
- expected_output
- priority
- forbidden_actions

## 6. Required Return Format

Verdict:
  GEMINI_CYCLE_004_BATCH_TRIAGE_RETURNED_WITH_WATCH / STRUCTURAL_GAPS_FOUND / WATCH_ONLY / HOLD

Cycle:
  cycle_004_task_inventory_batch_triage

Directly inspected:
  - ...

Not inspected:
  - ...

Batch triage summary:
  - ...

Per-group decision:

| group | decision | reason | next owner | WATCH | HOLD |
|---|---|---|---|---|---|

Bounded verification executed:
  yes / no

If yes:
  verification target:
  finding:

Codex requests needed:
  none / list

If Codex request needed:
  request_id:
  source task group:
  structural_gap:
  requested_codex_work:
  expected_output:
  priority:
  forbidden_actions:

What is usable:
  - ...

What remains WATCH:
  - ...

What remains HOLD:
  - ...

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
- no automation
- no scripts
- no current-position update
- no output_manifest update
- no baseline / workflow / registry / schema promotion
- no final Big Frame Candidate Map creation
- no HOLD release
- no final authority claim

