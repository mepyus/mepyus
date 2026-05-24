# Gemini Work Order
# cycle_001_big_frame_candidate_map_orientation

cycle_id:
  cycle_001_big_frame_candidate_map_orientation

status:
  READY_TO_SEND_TO_GEMINI

target:
  Gemini

role:
  execution / observation lane inside Manual Cycle Relay

authority:
  cycle work order only

not:
  Big Frame Candidate Map
  map draft
  workflow
  registry
  schema
  baseline
  product architecture
  dashboard
  routing authority
  current-position update
  output_manifest update
  automation
  final authority

## 1. Task

Inspect whether a future Big Frame Candidate Map can be safely oriented as an orientation-only map without becoming workflow, registry, baseline, product architecture, dashboard, routing authority, or current-position.

This cycle does not create the map.
This cycle does not draft the map.
This cycle does not approve map creation.

## 2. Questions To Answer

Gemini must answer:

1. Is the map-orientation cycle safe to continue?
2. What is the smallest orientation-only map shape?
3. What must be visible?
4. What must remain linked/outside?
5. What must remain WATCH?
6. What must remain HOLD?
7. Where must user judgment appear?
8. What would make the map draft fail?
9. Is there any structural gap requiring Codex?
10. Should the next owner be ChatGPT, Codex, User, or HOLD?

## 3. Read Scope

Prefer:

- app/work/space-skill-sandbox/outputs/big_frame_candidate_map_preparation_recovery_20260512_candidate_v0.md
- app/work/space-skill-sandbox/outputs/big_frame_consolidation_readiness_recovery_20260512_candidate_v0.md
- app/work/space-skill-sandbox/outputs/active_reentry_surface_genealogy_recovery_20260512_candidate_v0.md
- app/work/space-skill-sandbox/relay/cycles/README_manual_cycle_relay_20260513_candidate_v0.md

Optional if needed:

- app/work/space-skill-sandbox/outputs/thought_genealogy_processing_flow_recovery_20260512_candidate_v0.md
- app/work/space-skill-sandbox/outputs/sandbox_separation_genealogy_recovery_20260512_candidate_v0.md
- app/work/space-skill-sandbox/outputs/promotion_caution_genealogy_recovery_20260512_candidate_v0.md
- app/work/space-skill-sandbox/outputs/chatgpt_processing_mode_evolution_recovery_20260512_candidate_v0.md
- app/work/space-skill-sandbox/outputs/return_to_space_recovery_genealogy_recovery_20260512_candidate_v0.md

## 4. Do Not Read

- entire repo
- all runs
- raw logs
- broad Obsidian vault
- implementation files
- output_manifest unless explicitly necessary
- current-position unless explicitly necessary
- credential / token material

## 5. Structural Gap Rule

If Gemini finds a structure gap:

Do not solve it directly.

Add a Codex request entry suitable for:

app/work/space-skill-sandbox/relay/cycles/cycle_001_big_frame_candidate_map_orientation/codex_request_queue.md

Each request should include:

- request_id
- structural_gap
- requested_codex_work
- expected_output
- priority
- forbidden_actions

Codex should not act until user transfers this queue or ChatGPT / Supervisor approves.

## 6. Return Format

Verdict:
  GEMINI_CYCLE_OBSERVATION_RETURNED_WITH_WATCH / STRUCTURAL_GAP_FOUND / WATCH_ONLY / HOLD

Cycle:
  cycle_001_big_frame_candidate_map_orientation

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
  structural_gap:
  requested_codex_work:
  expected_output:
  priority:
  forbidden_actions:

Suggested next owner:
  ChatGPT / Codex / User / HOLD

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD

Do Not Promote:
  - ...

Next action:
  ...

## 7. Hard Boundaries

- no Big Frame Candidate Map creation
- no map draft
- no workflow
- no registry
- no schema
- no baseline
- no product architecture
- no current-position update
- no output_manifest update
- no automation
- no final authority claim
- no repo modification

