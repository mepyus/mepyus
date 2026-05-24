# Cycle Brief
# cycle_004_task_inventory_batch_triage

cycle_id:
  cycle_004_task_inventory_batch_triage

status:
  CYCLE_READY_FOR_GEMINI

authority:
  manual cycle setup only

not:
  workflow
  backlog
  registry
  automation
  baseline
  current-position update
  output_manifest update

## 1. Purpose

Give Gemini the full operating task inventory plus routing criteria so Gemini can batch-triage the next work instead of receiving many small packets.

This cycle tests whether Gemini can:

- read the whole task inventory
- separate Gemini execution tasks from Codex structure tasks
- preserve User / ChatGPT gates
- identify Codex setup requests
- avoid treating the inventory as an automatic backlog

## 2. This Cycle Will Do

- provide Gemini one work order path
- ask Gemini to triage Groups A-F from the task inventory
- ask Gemini to execute only bounded verification that is possible from available files
- ask Gemini to return Codex request entries for missing structure
- ask Gemini to keep HOLD items held
- ask Gemini to recommend a next owner per task group

## 3. This Cycle Will Not Do

- execute automation
- create scripts
- release HOLD
- create final Big Frame Candidate Map
- promote task inventory to backlog
- update current-position
- update output_manifest
- create workflow / registry / schema / baseline

## 4. Lanes

Gemini lane:
  batch triage / execution-readiness verification / evidence return / Codex request detection

Codex lane:
  recover Gemini return and process bounded structure requests later

ChatGPT / Supervisor lane:
  needed only if Gemini finds large-frame design ambiguity or over-promotion risk requiring conceptual judgment

User gate:
  required for HOLD release, automation, map draft execution, promotion, or direction change

## 5. Hard Stops

- no automation
- no scripts
- no current-position update
- no output_manifest update
- no baseline / workflow / registry / schema promotion
- no final Big Frame Candidate Map creation
- no HOLD release

## 6. Expected Cycle Return

Expected cycle return:
  Gemini batch triage return with per-group action, Codex request entries, WATCH / HOLD, and next owner.

Placement options:
  RETURN_TO_SPACE_VALUE_WITH_WATCH / WATCH_ONLY / HOLD

