# VectorFL Card Role Clarification Pass
# 2026-05-13 Candidate v0

## 1. Status

Document:
  candidate card role clarification pass

Authority:
  orientation-only role map with watch

Not:
  card registry
  card workflow
  card schema
  card ontology
  baseline
  automation plan
  current-position
  output_manifest

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH

---

## 2. Why This Exists

VectorFL already contains many card-like assets.

The risk is not that cards exist.
The risk is that all cards are treated as the same kind of object.

This pass applies the Vessel / Contents Separation Spec to cards.

Core rule:
  Cards are not automatically vessels.
  Most cards are handling parts, contents, labels, or re-entry surfaces.

---

## 3. Card Role Types

Card as Vessel / container:
  Rare. A card should almost never become the large frame itself.

Card as Content:
  A recovered judgment, trace, comparison, or candidate material held inside the existing vessel.

Card as Inlet / intake:
  A shape for receiving new material, prompt, external source, or user purpose.

Card as Processing mechanism:
  A bounded handling aid used to move material through reading, dispatch, sandboxing, or review.

Card as Recovery outlet:
  A shape for returning processed material as recovered judgment, WATCH/HOLD, placement, and next owner.

Card as Re-entry surface:
  A thin orientation surface for coming back later without rereading everything.

Card as Safety lid / guardrail:
  A boundary shape that prevents overpromotion, scope drift, approval drift, or automation drift.

Card as Label / status marker:
  A compact marker for status, placement, readiness, closed state, blocked state, or candidate state.

Card as Autonomy support:
  A bounded execution support surface for external tools, workers, or CLI agents.

Card as Mixed / WATCH:
  A card whose name or usage crosses roles and must be downshifted before use.

Important:
  Card as Vessel should be rare.
  If many cards become vessels, the space fragments.

---

## 4. Card / Card-like Asset Map

| Card / Card-like Asset | File or Mention | Role | Layer | What it does | What it must not become | WATCH |
|---|---|---|---|---|---|---|
| Prompt Intake Card | Mention / concept only; closest file: `space_aware_external_execution_intake_card_compact_20260507_v0.md` | Inlet / intake | Intake Layer | Receives user purpose, material, boundary, and context before execution | workflow, schema, mandatory prompt form | Can become rigid prompt protocol |
| Space-Aware External Execution Intake Card Compact | File: `space_aware_external_execution_intake_card_compact_20260507_v0.md` | Inlet / intake + Autonomy support | Intake / Execution Layer | Keeps external execution grounded in Plan from Space and broad-but-bounded pass | automation, current-position, registry | Compact operating card may be treated as execution workflow |
| New Input Reading Card | Mention / concept in Obsidian `05-12/3.md`, `05-12/4.md`; also referenced in `obsidian_05_12_growth_frame_intake_20260512_candidate_v0.md` | Inlet / intake | Intake / Growth Layer | Reads how a new input contacts existing space | schema, required card for every input | Can slow operation if mandatory |
| Pull Decision Card | Mention / concept in Obsidian `05-12/1-4`; referenced in `obsidian_05_12_growth_frame_intake_20260512_candidate_v0.md` | Inlet / intake + Safety lid / guardrail | Intake / Boundary Layer | Decides what asset family to pull and what not to pull | approval form, workflow, registry | Pull decision may become automatic next task |
| Sandbox Derivation Card | Mention / concept; referenced in `obsidian_05_11_pump_ready_space_application_candidate_v0.md`, `obsidian_05_11_3_reservoir_pipeline_attachment_structure_candidate_v0.md` | Processing mechanism | Sandbox / Processing Layer | Keeps derivative work connected to origin, boundary, test, and return | product pipeline, workflow, schema | Sandbox card may become product architecture |
| Return-to-Space Card | Mention / concept in Obsidian `05-12/1-4`; named in Vessel / Contents Spec | Recovery outlet | Recovery Layer | Returns derivative or processed material as recovered judgment, placement, watch, next pull | current-position update, baseline, truth validation | Return can be mistaken for approval |
| Active Re-entry Card | Mention / role; closest files: `active_reentry_surface_candidate_20260512_v0.md`, `active_reentry_surface_genealogy_recovery_20260512_candidate_v0.md` | Re-entry surface | Re-entry Layer | Gives a thin way back into the space | registry, manifest, current-position | Active surface can get too large |
| Progress / Movement Card | File family: `movement_record_*.md`; ledger entries in `manual_cycle_relay_progress_ledger_20260513_candidate_v0.md` | Label / status marker + Re-entry surface | Recovery / Re-entry Layer | Records movement, proof, recovered judgment, next trigger | official history, current-position, registry | Movement records can become bookkeeping pile |
| Approval Scope Card | Mention / role embedded in cycle files and ledger guidance | Safety lid / guardrail | Approval / Boundary Layer | Records raw instruction, interpreted scope, not-approved items, stop condition | approval registry, standing permission | Compressed approval may become blanket approval |
| Judgment Capsule | File: `judgment_capsule_reentry_surface_candidate_20260509_v0.md` | Contents + Recovery outlet + Re-entry surface | Recovery / Re-entry Layer | Compresses recovered judgment into reusable low-token surface | final memory, baseline, wiki authority, schema | Capsule fields can harden into mandatory schema |
| Thin Operating Card | Mention / role; closest files: `user_language_trace_to_memory_operating_card_20260511_v0.md`, `vectorfl_live_task_operation_index_20260509_v0.md` Short Operating Card | Label / status marker + Recovery outlet + Re-entry surface | Recovery / Re-entry Layer | Folds a result into a thin usable operating surface | new card family, workflow, official state machine | Name may invite new card system |
| User-Language Trace-to-Memory Operating Card | File: `user_language_trace_to_memory_operating_card_20260511_v0.md` | Re-entry surface + Safety lid / guardrail | Recovery / User-facing Layer | Explains trace -> recovery -> candidate memory in user language | baseline, official workflow, current-position | User-facing clarity may be overpromoted |
| Four-Line Card | Mention / usage aid in several files, including `current_position_entry_after_user_facing_usage_flow_dry_run_v0.md` and `gemini_external_material_queue_001_task_packets_candidate_v0.md` | Re-entry surface + Label / status marker | User-facing Layer | Gives simple user orientation | protocol, routing surface, workflow | Repeated use may become mandatory workflow |
| Manual Recovery Rehearsal Card | File: `manual_recovery_rehearsal_card_20260511_candidate_v0.md` | Recovery outlet + Processing mechanism | Recovery Layer | Rehearses how a return should be manually recovered | helper automation, workflow, script request | Recovery steps may become automation plan |
| QMD Retrieval Return Card | Mentioned inside file: `qmd_vectorfl_retrieval_output_contract_candidate_v0.md` | Recovery outlet + Inlet / intake | Retrieval / Recovery Layer | Wraps retrieval results before entering VectorFL | parser schema, ingestion automation, truth | Contract language may be mistaken for schema |
| Big Frame Candidate Map | File: `big_frame_candidate_map_20260513_candidate_v0.md` | Re-entry surface / Orientation surface | Big Frame / Re-entry Layer | Orients the large frame and field map | vessel itself, final framework, workflow, registry | Candidate map can be mistaken for final framework |
| Mission Packet | Files: `mission_packet_result_contract_v0_candidate_20260508.md`, packet files in `relay/prompts` and `relay/packets` | Processing mechanism + Autonomy support | Execution Layer | Defines bounded task, useful result, boundaries, and return shape | automation queue, workflow, task registry | Packets can become automatic execution |
| Worker Dispatch / Work Order | Files: `relay/cycles/**/gemini_work_order.md`, template `gemini_work_order_template_v0.md` | Processing mechanism + Autonomy support | Execution Layer | Tells Gemini/worker what to observe or execute manually | final authority, workflow, automation | Work order can be treated as execution approval |
| Cycle Return | Files: `relay/cycles/**/cycle_return.md`, template `cycle_return_template_v0.md` | Recovery outlet + Label / status marker | Recovery / Closeout Layer | Records recovered judgment, usable value, WATCH/HOLD, placement | current-position, approval, memory injection | Closeout can be mistaken for next task approval |
| Supervisor Checkpoint | Files: `relay/cycles/**/supervisor_checkpoint.md`, template `supervisor_checkpoint_template_v0.md` | Safety lid / guardrail + Label / status marker | Supervisor / Boundary Layer | Reviews placement, gate, return status, and user decision need | approval, execution trigger, baseline | Checkpoint can become hidden authority |
| Codex Request Queue | Files: `relay/cycles/**/codex_request_queue.md`, template `codex_request_queue_template_v0.md` | Processing support | Structure Gap Layer | Holds Gemini-created structural requests for Codex | backlog, registry, automation queue | Queue priority can become execution authority |
| Progress Ledger entry | File: `manual_cycle_relay_progress_ledger_20260513_candidate_v0.md` | Label / status marker + Re-entry surface | Re-entry / Progress Layer | Gives thin progress/proof view | current-position, official history, backlog | Ledger can become authority map |

---

## 5. Current Structural Reading

Prompt Intake Card:
  likely Inlet / Intake

Pull Decision Card:
  likely Inlet / Intake + Safety lid

Sandbox Derivation Card:
  likely Processing mechanism

Return-to-Space Card:
  likely Recovery outlet

Active Re-entry Card:
  likely Re-entry surface

Progress / Movement Card:
  likely Label + Re-entry surface

Approval Scope Card:
  likely Safety lid / Guardrail

Judgment Capsule:
  likely Content + Recovery outlet

Thin Operating Card:
  likely Label + Recovery outlet + Re-entry surface

Big Frame Candidate Map:
  likely Re-entry surface / Orientation surface, not vessel itself

Mission Packet / Work Order:
  likely Processing mechanism / Autonomy support

Cycle Return:
  likely Recovery outlet + Label

Supervisor Checkpoint:
  likely Safety lid + Label

Codex Request Queue:
  likely Processing support, not automation queue

Progress Ledger entry:
  likely Label / re-entry marker, not current-position

Adjustment from direct inspection:
  Several cards explicitly say they are not workflow, schema, registry, baseline, automation, or current-position. The issue is not missing guardrails; the issue is repeated card language spreading across many roles.

---

## 6. Misread Risk Table

| Card | Misread Risk | Why dangerous | Correct reading | Guardrail |
|---|---|---|---|---|
| Any card | card becomes workflow | Turns observation aids into mandatory process | Situation-specific handling part | Use one card only when it fits the current blurry field |
| Card list in Obsidian 05-12 | card becomes registry | Makes concept list into official catalog | Candidate card concepts | Mark mention / concept only |
| QMD Retrieval Return Card | card becomes schema | Contract fields may be implemented as parser schema | Recovery wrapper for retrieval evidence | Keep candidate contract note, no ingestion automation |
| Big Frame Candidate Map | card/map becomes final framework | Freezes orientation surface into vessel authority | Re-entry / orientation surface | Keep candidate map status |
| Cycle Return | card becomes current-position | Closeout becomes official present state | Recovery outlet and status label | Separate current-position approval required |
| Supervisor Checkpoint | card becomes approval | Supervisor review becomes hidden authority | Gate review and role watch | User remains promotion authority |
| Codex Request Queue | card becomes automation queue | Structural requests turn into automatic tasks | Processing support only | Require user/ChatGPT transfer or approval |
| Progress Ledger entry | card becomes official memory/history | Progress view becomes authority ledger | Thin re-entry marker | Keep not current-position / not output_manifest |
| Judgment Capsule | card becomes baseline | Recovered judgment becomes permanent rule | Compact reusable candidate judgment | Keep provenance, use_when, do_not_use_when, watch |
| Mission Packet / Work Order | card becomes execution permission | Packet existence triggers execution | Bounded manual instruction surface | Manual transfer and approval scope required |
| Four-Line Card | card becomes protocol | User-facing aid becomes mandatory UI/workflow | Optional usage aid | Keep no protocolization watch |
| Thin Operating Card | card becomes new file family | Adds clutter while trying to reduce it | Role applied to existing returns | Use as folding role, not new system |

---

## 7. Thin Operating Card Decision

Decision:
  C. needed only as a role, not a new file family

Reason:
  Thin Operating Card should be the way results are folded, not another card system. Existing `cycle_return`, `movement_record`, `progress ledger entry`, and user-language operating cards already cover the needed surface when kept thin. Creating a new file family would add the clutter this pass is meant to prevent.

Use:
  Treat Thin Operating Card as a role marker for compact recovery/re-entry surfaces.

Do not:
  Create a new mandatory card template or official card lane.

---

## 8. What Is Structurally Stable

- Card-as-observation-tool language is already present in Obsidian 05-12.
- Many files already include explicit not-baseline / not-workflow / not-schema / not-registry warnings.
- Cycle files have separable roles: work_order, request_queue, checkpoint, return.
- Existing Vessel / Contents Separation Spec is sufficient to classify cards without creating a new card system.
- Big Frame Candidate Map and Progress Ledger already declare orientation-only status.

## 9. What Is Structurally Unstable Or Mixed

- The word card covers intake, processing, recovery, re-entry, guardrail, label, content, and autonomy support.
- Concept cards in Obsidian 05-12 can be mistaken for actual files or a complete card catalog.
- Contract and template language can drift toward schema/workflow.
- Work orders, packets, and queues can be misread as automation.
- Ledger and movement records can drift toward current-position or official history.
- Thin Operating Card is useful as a role but risky as a new file family.

---

## 10. Recommendation

Recommendation:
  A. Use Card Role Map as orientation-only and do not create new card system.

Why:
  The existing vessel can hold the current card variety if roles are separated. The immediate need is less card creation and more role clarity. Gemini can later review naming/meaning drift, but no new card framework is needed now.

---

## 11. Do Not Promote

- card role map != card registry
- card role map != workflow
- card role map != schema
- card role map != ontology
- card role map != baseline
- Thin Operating Card != new vessel
- cycle_return != current-position
- request_queue != automation queue
- checkpoint != approval
- progress ledger != official history

---

## 12. Final Return Card

Material:
  existing VectorFL card-like assets

Classification:
  re-entry / inlet / process / recovery / guardrail / label / content roles

Recovered Judgment:
  Card is not one object type in VectorFL. Card is a surface word used across multiple handling roles. The safe move is to classify each card by vessel/contents role before use, not to create a card registry or card workflow.

WATCH:
  - card list becoming registry
  - card template becoming schema
  - cycle_return becoming current-position
  - request_queue becoming automation queue
  - checkpoint becoming approval
  - Thin Operating Card becoming new file family

HOLD:
  - card registry
  - card schema
  - card workflow
  - card ontology
  - baseline promotion
  - current-position update
  - output_manifest update
  - automation

Placement:
  RETURN_TO_SPACE_VALUE_WITH_WATCH

Next Owner:
  Gemini

Do Not Promote:
  card role clarification is an orientation-only sorting pass, not a card system.

