# VectorFL Space Asset Access Map v0

Date: 2026-04-12

## purpose

This is a quick access map for the materials that make up the VectorFL space.

It is not a full inventory and it does not move files.

Use this when the supervisor, Codex, Gemini CLI, or another future tool needs to answer:

- where are the scripts?
- where are the raw inputs?
- where are the declarations/baselines/directives?
- where are the reports and locked reasoning assets?
- where are the runtime manifests and generated views?
- which existing index should I read before searching blindly?

## first rule

Do not start with repo-wide search unless you need unknown material.

Start from these maps:

- `vectorfl_status.md`
- `docs/reports/vectorfl_integrated_engine_asset_index_v0.md`
- `docs/notes/executable_runner_index_v0.md`
- `docs/guides/source_assets_creation_map_v1.md`
- `inputs/README.md`
- `source_assets/README.md`

## 1. current integrated engine assets

Use these when working on the integrated engine program and surfaces.

### code

- `app/runtime/vectorfl_integrated_engine_api.py`
  - Operating dialogue, work packet, assignment, worker launch/execution, internal read, synthesis, supervisor state.
- `app/runtime/vectorfl_integrated_engine_shell.py`
  - Python-rendered engine surface.
- `app/core/runtime/viewer_server.py`
  - HTTP route wiring.

### surface app

- `runtime/views/vectorfl_dual_surface.tsx`
  - User surface and VectorFL surface source.
- `runtime/views/vectorfl_dual_surface_app/`
  - React/Vite app wrapper for the TSX surface.
- `runtime/views/vectorfl_dual_surface_app/README.md`
  - Current program boundary, commands, design/dependency rules.

### runtime records

- `runtime/manifests/vectorfl_integrated_engine_operating_dialogue_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_work_packet_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_assignment_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_worker_launch_draft_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_worker_execution_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_worker_session_latest_v0.json`

Reading rule:

- These are latest records.
- They tell you what the engine most recently did.
- They are not permanent source documents.

## 2. scripts by operating intent

Use `docs/notes/executable_runner_index_v0.md` for detailed commands.

### viewer / surface

- `scripts/run_viewer_server.py`
  - Starts local viewer server.
- `scripts/run_vectorfl_operable_surface_set.py`
  - Builds operable surface set.
- `scripts/run_vectorfl_page_app_shell.py`
  - Earlier page shell runner.
- `scripts/run_vectorfl_paper_proper_mock.py`
  - Paper proper mock/supervisor surface generator.
- `scripts/run_vectorfl_paper_weekend_pilot_mock.py`
  - Weekend pilot legacy surface generator.

### Paper bridge / validator

- `scripts/run_vectorfl_paper_codex_bridge.py`
  - Codex bridge adapter for Paper proper lineage.
- `scripts/run_vectorfl_paper_gemini_crosscheck_bridge.py`
  - Gemini cross-check bridge for Paper proper lineage.
- `scripts/run_vectorfl_paper_actual_export_gate_validator.py`
  - actual_export_only gate validator and dry-run override validator.
- `scripts/run_vectorfl_paper_actual_export_swap_stub.py`
  - Swap/readiness stub lineage. Do not treat as slot replacement.
- `scripts/run_vectorfl_paper_promotion_stub.py`
  - Promotion stub lineage. Do not treat as promotion authority.

### input / external material

- `scripts/process_structured_doc_with_routing.py`
  - Structured markdown front door.
- `scripts/run_external_input_gate.py`
  - Decides whether input can be directly ingested or needs preprocessing.
- `scripts/run_external_case_raw_intake_probe.py`
  - Quick raw external input texture check.
- `scripts/run_transcript_aware_regroup.py`
  - Regroups transcript-like inputs.
- `scripts/run_transcript_preprocess_comparison.py`
  - Before/after preprocessing comparison.
- `scripts/run_post_preprocess_first_pass_probe.py`
  - First pass on preprocessed sidecar.
- `scripts/run_external_case_folder_sweep_loop.py`
  - Plan-first folder sweep.
- `scripts/run_external_case_flowline_sweep.py`
  - External case flowline sweep.

### line thickening / observation

- `scripts/apply_internal_observer.py`
  - Applies internal observer and can record line-thickening.
- `scripts/build_source_view.py`
  - Builds source view; can record line-thickening.
- `scripts/run_line_thickening_sample.py`
  - Small line-thickening sample.
- `scripts/run_transition_over_surface_targeted_breadth_validation.py`
- `scripts/run_primary_material_breadth_validation.py`
- `scripts/run_transition_over_surface_forward_persistence_confirmation.py`
- `scripts/run_transition_over_surface_residue_robustness_probe.py`
- `scripts/run_transition_over_surface_sandbox_recovery_check.py`
- `scripts/run_transition_over_surface_sandbox_reintroduction_trip.py`

### multi-lens / interpretation

- `scripts/run_multi_lens_document_reading_probe.py`
- `scripts/run_multi_lens_document_reading_strength_validation.py`
- `scripts/run_multi_pass_interpretation_training.py`
- `scripts/run_paragraph_role_interpretation_training.py`
- `scripts/run_question_inducing_block_review.py`
- `scripts/run_dialogue_asset_probe.py`
- `scripts/run_dialogue_asset_purpose_synthesis.py`

### state / runtime safety

- `scripts/run_runtime_preflight.py`
- `scripts/run_state_validation_fixture_v1.py`
- `scripts/backfill_engine_state_v1.py`
- `scripts/record_operation_event.py`
- `scripts/sync_folder_status.py`
- `scripts/folder_status_sync.py`

## 3. raw input zones

Use `inputs/README.md`.

- `inputs/external_cases/`
  - Raw external cases, transcripts, copied source material, outside technical/business references.
- `inputs/internal_notes/`
  - Internal notes, quick memos, draft working input.
- `inputs/reference_docs/`
  - Reference documents and organized reference input candidates.

Rule:

- Raw input starts in `inputs/`.
- Do not mix interpreted output into `inputs/`.

## 4. source asset zones

Use `source_assets/README.md` and `docs/guides/source_assets_creation_map_v1.md`.

- `source_assets/declarations/`
  - Declarations and philosophy-level source assets.
- `source_assets/baselines/`
  - Baseline and lock documents.
- `source_assets/directives/`
  - Codex/Gemini/operator directives.
- `source_assets/handoffs/`
  - Handoff notes.
- `source_assets/external_case_inputs/`
  - External case input source assets.
- `source_assets/session_notes/`
  - Session close notes and working summaries.
- `source_assets/legacy_misc/`
  - Legacy root-md candidates not yet moved.

Rule:

- New source-md assets should usually start under `source_assets/`, not repo root.
- Old root md may remain in place for provenance stability.

## 5. docs zones

### guides

- `docs/guides/`
  - Human-facing how-to and access maps.
  - Put navigational guidance here.

Useful current guides:

- `docs/guides/source_assets_creation_map_v1.md`
- `docs/guides/input_dropzones.md`
- `docs/guides/engine_overview.md`

### reports

- `docs/reports/`
  - Result notes, readouts, closeouts, inspection reports.
  - Use for “what happened / what was learned / why this is the current state.”

Useful current reports:

- `docs/reports/vectorfl_integrated_engine_asset_index_v0.md`
- `docs/reports/vectorfl_integrated_engine_current_position_checkpoint_v0.md`
- `docs/reports/vectorfl_integrated_engine_internal_inspection_v0.md`
- `docs/reports/vectorfl_integrated_engine_worker_execution_loop_log_v0.md`
- `docs/reports/vectorfl_integrated_engine_three_surface_reframe_v0.md`

### specs / contracts / policies

- `docs/specs/`
  - Structural plans and expected shape.
- `docs/contracts/`
  - Stronger expected data/behavior contracts.
- `docs/policies/`
  - Operating rules and guardrails.

Rule:

- If it tells what to do repeatedly, consider `policies`.
- If it defines shape, consider `contracts` or `specs`.
- If it records what happened, use `reports`.

## 6. runtime zones

### manifests

- `runtime/manifests/`
  - Latest records, registries, label packets, bridge records, validation results.

Important subareas:

- `runtime/manifests/vectorfl_integrated_engine_*`
- `runtime/manifests/vectorfl_paper_*`
- `runtime/manifests/folder_inventory/`
- `runtime/manifests/folder_changes/`
- `runtime/manifests/bridges/`
- `runtime/manifests/label_packets/`
- `runtime/manifests/origin_maps/`

Rule:

- Runtime manifests are evidence/state, not source prose.
- Treat `latest` as current pointer, not as historical archive.

### contracts

- `runtime/contracts/`
  - Runtime-side JSON contracts, examples, and checklist-like artifacts.

### views

- `runtime/views/`
  - Generated or served views, current React surface source, and older view lineages.

Current high-value view areas:

- `runtime/views/vectorfl_dual_surface.tsx`
- `runtime/views/vectorfl_dual_surface_app/`
- `runtime/views/vectorfl_paper_proper/`
- `runtime/views/vectorfl_paper_weekend_pilot/`
- `runtime/views/vectorfl_operable_surface/`
- `runtime/views/vectorfl_page_shell/`

Rule:

- Do not assume every view folder is current.
- `vectorfl_dual_surface*` is current user/VectorFL surface.
- Python `/vectorfl-engine/operate` is current engine surface.
- Paper/proper, operable, and page_shell are lineage/reference unless reopened.

## 7. app code zones

### core

- `app/core/`
  - Core models, runtime primitives, state, viewer server, input/state operations.

High-value current files:

- `app/core/runtime/viewer_server.py`
- `app/core/runtime/live_input.py`
- `app/core/models/entities.py`
- `app/core/states.py`

### runtime

- `app/runtime/`
  - Runtime APIs, shells, reporting, process console, operable surfaces.

High-value current files:

- `app/runtime/vectorfl_integrated_engine_api.py`
- `app/runtime/vectorfl_integrated_engine_shell.py`
- `app/runtime/vectorfl_operable_surface_set.py`
- `app/runtime/vectorfl_paper_operable_api.py`
- `app/runtime/vectorfl_paper_operable_shell.py`
- `app/runtime/line_thickening.py`
- `app/runtime/internal_search_minimum.py`

### input layer

- `app/input_layer/`
  - Source locating, segmenting, labeling, anchorizing.

High-value files:

- `app/input_layer/source_locator/origin_map_minimum_v1.py`
- `app/input_layer/segmenter/experimental_segmenter.py`
- `app/input_layer/segmenter/experimental_segmenter_v2.py`
- `app/input_layer/labeler/labeler.py`
- `app/input_layer/anchorizer/anchorizer.py`

### work

- `app/work/`
  - Experiments, transition support, processor compare, generated operator summaries.

High-value current zones:

- `app/work/observer_ingest_min/`
- `app/work/external_input_preprocess/`
- `app/work/operating_ui/`
- `app/work/processor_compare/`
- `app/work/current_layer_baseline/`

Rule:

- Treat `app/work/` as experiment/workbench unless a specific artifact has been promoted by a report/spec.

## 8. quick reading paths

### To understand the integrated engine

1. `vectorfl_status.md`
2. `docs/reports/vectorfl_integrated_engine_asset_index_v0.md`
3. `runtime/views/vectorfl_dual_surface_app/README.md`
4. `app/runtime/vectorfl_integrated_engine_api.py`
5. `app/runtime/vectorfl_integrated_engine_shell.py`
6. `runtime/views/vectorfl_dual_surface.tsx`

### To find a script by intent

1. `docs/notes/executable_runner_index_v0.md`
2. `scripts/folder_status.md`
3. `scripts/`

### To add a new source material

1. `inputs/README.md`
2. `source_assets/README.md`
3. `docs/guides/source_assets_creation_map_v1.md`

### To understand Paper/proper lineage

1. `docs/reports/vectorfl_paper_supervisor_bridge_ready_surface_v1.md`
2. `docs/reports/vectorfl_paper_surface_identity_correction_and_merge_reanalysis_v0.md`
3. `docs/reports/vectorfl_operable_surface_proper_merge_correction_v0.md`
4. `runtime/views/vectorfl_paper_proper/index.html`
5. `runtime/views/vectorfl_operable_surface/index.html`

### To understand line thickening and translation material

1. `docs/notes/executable_runner_index_v0.md`
2. `docs/reports/line_thickening_runtime_insertion_report_v0.md`
3. `app/runtime/line_thickening.py`
4. `runtime/line_thickening_demo/`
5. `runtime/line_thickening_demo_v2/`

## 9. do not do yet

- Do not physically reorganize the repo tree just to make it look cleaner.
- Do not move root legacy md without provenance review.
- Do not treat generated runtime outputs as canonical source.
- Do not treat Paper/proper or weekend pilot as the current integrated engine surface.
- Do not expand the React surface app into a full frontend workspace before the user/VectorFL/engine split stabilizes.

## 10. next indexing step

The next useful step is a small machine-readable registry, but only after this guide is used once or twice.

Candidate future file:

- `runtime/manifests/vectorfl_space_asset_access_registry_v0.json`

Until then, this markdown guide is the safer supervisor-facing index.
