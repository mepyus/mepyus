# VECTORFL_CODEX_GEMINI_SPACE_MATURATION_HANDOFF_SPEC_20260524_V0

verdict: PASS_CODEX_GEMINI_SPACE_MATURATION_HANDOFF_SPEC_WITH_HOLD

run dir:
/Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_codex_gemini_space_maturation_handoff_spec_v0

## purpose
Make Hermes execution outputs re-enter space in a form that Codex can steward and Gemini can re-read as layers, enabling repeated spatial maturation without relying on long conversation context.

## budget
- mode: FAST_NO_CALL_SCRIPT_ONLY_SPEC_DRAFT
- VectorFL internal execution: script-only
- Codex live call: NO
- Gemini live call: NO
- API/direct/server/replay: NO
- provider note: Hermes conversation uses provider API separately; VectorFL-internal execution here is script-only.

## core loop
- Hermes preserves raw original and reads bounded space refs
- Hermes creates execution output + receipt + minimal_space_delta
- Codex Space Steward reads referenced_material + reinserted_material + lacl/layer resources
- Codex produces spatial recovery/index/cross-link findings, not authority changes
- Gemini Layer Reader re-reads Codex findings for layer pressure, semantic flattening, and programization candidates
- Hermes merges returned packets into next safe lane as HOLD evidence

## roles
### CODEX_SPACE_STEWARD
responsibility:
- read handoff first
- map referenced_material vs reinserted_material
- classify assets primary_layer plus secondary_links
- detect duplicate/archaeology pressure
- prepare Gemini layer questions
- return spatial packet only
must_not:
- move folders
- promote authority
- mutate current-position
- call API/server/replay
- treat proposal as source of truth
### GEMINI_LAYER_READER
responsibility:
- read Codex spatial packet
- detect layer flattening and over-internalization
- judge whether space design reflects Phase1 whole-flow
- identify function strengthening opportunities
- return layer packet only
must_not:
- override authority
- turn watch-only issues into fixes
- replace Codex file-grounded findings with abstract opinion
### HERMES_EXECUTION_WORKBENCH
responsibility:
- preserve original
- select bounded refs
- execute local scripts or bounded approved commands
- write receipts/reports
- avoid authority mutation unless separately approved
must_output:
- raw_original_handle
- used_space_refs
- space_reference_delta
- receipt
- next_safe_lane

## created draft files
- /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_codex_gemini_space_maturation_handoff_spec_v0/03_VECTORFL_CURRENT_SPACE_HANDOFF_DRAFT.md
- /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_codex_gemini_space_maturation_handoff_spec_v0/04_VECTORFL_SPACE_LAYER_MAP_DRAFT.json
- /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_codex_gemini_space_maturation_handoff_spec_v0/05_VECTORFL_ASSET_INDEX_DRAFT.json
- /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_codex_gemini_space_maturation_handoff_spec_v0/06_VECTORFL_CODEX_SPACE_STEWARD_GUIDE_DRAFT.md
- /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_codex_gemini_space_maturation_handoff_spec_v0/07_VECTORFL_GEMINI_LAYER_READER_GUIDE_DRAFT.md
- /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_codex_gemini_space_maturation_handoff_spec_v0/08_VECTORFL_SPACE_MATURATION_PACKET_SCHEMA_DRAFT.json
- /Users/sungsookim/universe/vectorfl_replica/app/work/space-skill-sandbox/relay/runs/hermes_centered/run_20260524_codex_gemini_space_maturation_handoff_spec_v0/09_VECTORFL_NO_MUTATION_BOUNDARY_DRAFT.md

## success criteria
- Codex can read <=7 files and understand current position
- Codex returns primary_layer plus secondary_links without moving files
- Gemini can judge layer pressure from Codex packet without reading whole history
- Hermes can merge both packets into next safe lane with minimal provider context
- Each loop creates fewer-but-denser handoff assets, not artifact sprawl

## validation
- checks: 17
- active_hits: 0
- asset_index_items: 12
- early_attach_points: 3
- elapsed_seconds: 0.0025257320000000028

## HOLD
- folder_tree_mutation: NO
- source_code_mutation: NO
- authority_mutation: NO
- registry_mutation: NO
- current_position_apply: NO
- promotion: HOLD

NEXT_SAFE_LANE:
SPACE_MATURATION_HANDOFF_FILES_DRAFT_VALIDATION_NO_FOLDER_MOVE_V0
