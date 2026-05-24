# CODEX_SPACE_OPERATION_ROUTER_20260524_V0

status: HOLD / operational guide

purpose:
Map short user instructions into Codex space duties inside the Hermes-centered VectorFL loop. This file does not authorize authority, registry, current-position, source, folder-tree, API, server, replay, Codex direct API, or Gemini direct API mutation.

## Core Role Split

Hermes remains the original interpretation, model merge, execution, and trace center.

Codex owns:
- first-pass space retrieval for Hermes
- selected/rejected reference judgment
- later analysis of Hermes reentry records
- HOLD-only space maturation proposals

Gemini may appear only as optional analysis inside a Codex script-chain. Hermes does not directly invoke Gemini.

## Instruction Routing

### User says: "공간을 확인해"

Route to: `CODEX_SPACE_CHECK`

Goal:
Read the compact space controls and latest Hermes-centered status handles, then return a bounded space snapshot.

Read first:
1. `12_LIGHT_REPORT_FOR_CODEX_HERMES_CENTERED_LOOP.md`
2. `02_hermes_centered_loop_contract_v0.json`
3. `03_codex_reference_path_index_v0.json`
4. `06_VECTORFL_SPACE_LAYER_MAP_COMPACT.json`
5. `07_VECTORFL_ASSET_INDEX_COMPACT.json`
6. `09_VECTORFL_NO_MUTATION_BOUNDARY_DRAFT.md`

Return should answer:
- what space controls are active
- which assets are relevant now
- which files are HOLD/proposal only
- whether there is a Hermes reentry record waiting for Codex
- what the next safe lane is

### User says: "헤르메스 작업 내용을 분석해"

Route to: `CODEX_HERMES_WORK_ANALYSIS`

Goal:
Read Hermes execution/merge/reentry artifacts and explain what Hermes took from space, how Hermes merged it with model reasoning, what was executed, and what should re-enter space.

Read first:
1. `15_hermes_model_merge_from_codex_retrieval_v0.json`
2. `16_hermes_execution_trace_and_codex_reentry_record_v0.json`
3. `17_validation_hermes_merge_from_codex_retrieval_v0.json`
4. `19_CODEX_SPACE_MATURATION_RETURN_PACKET.json`
5. `20_hermes_merge_from_codex_maturation_v0.json`
6. `21_codex_readable_maturation_merge_status_v0.json`
7. `22_validation_codex_maturation_merge_v0.json`

Return should answer:
- what Hermes read from Codex/space
- what Hermes selected as merge input
- what Hermes changed in judgment
- what Hermes executed or intentionally did not execute
- what reentry record exists for Codex
- what assets are only proposed for future indexing
- whether promotion is still HOLD

### User says: "공간자료를 찾아줘" or Hermes asks Codex for retrieval

Route to: `CODEX_SPACE_RETRIEVAL_BY_ORIGINAL`

Goal:
Use a user original or Hermes task packet to retrieve bounded space material for Hermes to merge and execute.

Read first:
1. user original or Hermes task packet
2. compact layer map
3. compact asset index
4. no-mutation boundary
5. reference path index
6. retrieval return schema

Return path pattern:
`07_CODEX_SPACE_RETRIEVAL_RETURN_PACKET_*.json`

Required return fields:
- `packet_id`
- `role`
- `read_files`
- `selected_space_material`
- `rejected_space_material`
- `original_to_space_fit`
- `changed_judgment_for_hermes`
- `risks`
- `recommended_hermes_merge_inputs`
- `next_for_hermes`
- `promotion_status`

### User says: "공간 숙성 판단해" or Hermes provides reentry

Route to: `CODEX_SPACE_MATURATION_BY_REENTRY_RECORD`

Goal:
Read Hermes reentry records and decide whether the result should become a HOLD-only space maturation proposal.

Read first:
1. Hermes execution trace and Codex reentry record
2. Hermes merge packet
3. Codex retrieval return packet
4. reference path index
5. no-mutation boundary
6. reentry instruction

Return path pattern:
`19_CODEX_SPACE_MATURATION_RETURN_PACKET*.json`

Required return fields:
- `packet_id`
- `role`
- `read_files`
- `maturation_decision`
- `space_assets_to_reindex`
- `gemini_via_codex_script_used`
- `gemini_findings_ref_or_inline`
- `changed_judgment`
- `next_safe_lane`
- `promotion_status`

## Non-Negotiable Boundary

Default status is `HOLD`.

Never do these from this router:
- mutate source code
- mutate authority
- apply current-position
- mutate registry
- move folders
- promote proposal to authority
- call Codex/Gemini through direct API
- ask Hermes to call Gemini directly
- run external API/direct/server/replay lanes

## Output Discipline

Every Codex return should separate:
- `read_files`
- `selected_material`
- `rejected_material`
- `changed_judgment`
- `risks`
- `next_safe_lane`
- `promotion_status`

Every Hermes analysis should separate:
- space refs Hermes used
- model reasoning Hermes added
- execution decision
- execution trace
- Codex-readable reentry handle
- HOLD or approval boundary

