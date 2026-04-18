# VectorFL Integrated Engine Asset Index v0

Date: 2026-04-12

## verdict

- This is an index and operating map, not a restructure.
- Do not move files based on this note alone.
- The current integrated-engine work is split across code, runtime views, manifests, reports, and reference readings.
- The immediate cleanup rule is: keep the assets in place, make their roles legible, and avoid mistaking generated/test surfaces for canonical surfaces.

## current posture

The integrated engine is now organized around three surface roles:

- User surface: goal, scope, and material-context start surface.
- VectorFL surface: intermediate-formation reading and translation surface for line/relation/gap/pending/reflux before execution.
- Engine surface: ingest, process, validate, trace/memory, and return surface.

Current interpretation lock:

- `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md` is the current CLI-facing reading lock for the three-surface body.
- `docs/reports/integrated_engine_common_language_extraction_v1.md` is the current extraction dataset for setup language and assistant interpretation grammar; use it as language material, not as final schema.
- `docs/reports/integrated_engine_vectorfl_surface_elevated_direction_note_v1.md` is the current provisional direction note for the VectorFL surface rising as an operating waist; use it as direction material, not as a final workflow-hub lock.
- `docs/reports/integrated_engine_exploration_question_set_v1.md` is the repeatable question set for future language-harvest runs.
- `docs/reports/integrated_engine_exploration_question_set_v1_1.md` is the current repeatable language-harvest protocol with source priority, freshness notes, previous-run overlap, and stable-candidate judgment rules.
- `docs/reports/integrated_engine_language_harvest_run_20260414_v1_1.md` is the first v1.1 execution report; it compares against `integrated_engine_common_language_extraction_v1.md` as harvest_round_1 and adds current priority 1/2 surface/code evidence.
- `docs/reports/integrated_engine_common_language_extraction_v2.md` is harvest_round_2; use it to compare repeated expressions, stronger rewrites, new candidate grammar, and stable candidates against harvest_round_1.
- `docs/reports/integrated_engine_common_language_extraction_v3.md` and `docs/reports/integrated_engine_common_language_round3_boundary_report_v1.md` are narrow boundary clarifications; they add no new body-language lock and separate extension/future/unresolved language.
- `docs/reports/integrated_engine_setup_working_lexicon_v0.md` is the current setup handoff lexicon for using stable body language while keeping extension/future/unresolved language separate.
- `docs/reports/integrated_engine_transfer_packet_minimum_slots_v0.md` is the current transfer-packet working draft for reducing communication friction between user surface, VectorFL surface, and engine surface; use it as v0 operating language, not as final schema.
- `docs/reports/integrated_engine_operating_object_slot_movement_rules_v0.md` is the current operating-object slot movement working draft; use it to test explicit movement through inbox, VectorFL review, engine processing, external support, validation, return-ready, and closed slots without treating it as a final state machine.
- `docs/reports/integrated_engine_anchor_object_minimum_fields_v0.md` is the current anchor-object minimum-field working draft; use it as comparison/boundary/position-judgment language, not as final anchor schema.
- `docs/reports/integrated_engine_maturation_object_minimum_fields_v0.md` is the current maturation-object minimum-field working draft; use it to preserve origin, position, maturity, linkage, and open edges for line/axis/note/harvest/comparison material without treating it as final maturity schema.
- `docs/reports/integrated_engine_screen_panel_classification_criteria_v0.md` is the current screen-panel classification working draft; use it to classify panels as anchor expression, maturation expression, or operating expression before detailed UI layout or runtime implementation.
- `docs/reports/integrated_engine_three_surface_representative_panel_layout_v0.md` is the current representative panel-layout working draft; use it to keep user surface operating-centered, VectorFL surface maturation-centered, and engine surface execution-centered without treating it as final UI design.
- `docs/reports/integrated_engine_three_surface_panel_connection_flow_v0.md` is the current representative panel-connection working draft; use it to describe which panel action emits which packet/log and wakes which target panel without treating it as final interaction automation.
- `docs/reports/integrated_engine_panel_render_contract_v0.md` is the current panel render-contract working draft; use it to limit each panel to the manifest fields needed for its question without treating it as final props or runtime binding.
- `docs/reports/integrated_engine_current_reading_order_note_v1.md` records the current reading order: v1.1 protocol, harvest_round_1, harvest_round_2, harvest_round_3/boundary, then the working lexicon.
- `docs/reports/integrated_engine_gemini_cli_orientation_v1.md` is the short orientation for Gemini CLI or other external CLI workers editing the integrated-engine surface.
- Team relay, handoff/waiting/report, external research, CLI calls, automatic routing, and standing worker assignment are operating extensions, not the body skeleton.
- Earlier assignment-desk or workflow-board wording should be read as lineage/extension material unless explicitly relocked.

## integrated-engine current baseline

The integrated-engine v1 candidate set is the current upper bundle for the PASS-level v0 operating grammar and the current PASS baseline for low-intensity operation.

Use it as a current working baseline for the next chat or next implementation pass, not as a final lock. It has passed both:

- user-origin loop: user request -> VectorFL review -> engine return -> VectorFL validation / reflux
- VectorFL-origin restart loop: maturation signal -> user follow-up organization -> engine follow-up return -> user decision / VectorFL recheck

- `docs/reports/integrated_engine_working_lexicon_v1_candidate.md`
  - Working lexicon for three surfaces, three object classes, packet kinds, panel expression classes, and shared panel language.
- `docs/reports/integrated_engine_working_protocol_v1_candidate.md`
  - Working protocol for slot movement, transfer packets, anti-bypass, return validation, reflux principles, panel connection flow, and current loop state.
- `docs/reports/integrated_engine_working_interface_v1_candidate.md`
  - Working interface for panel classification, panel layout, read mapping, render contract, and the maturation-canvas PASS basis.

Position:

- These are top-level `docs/reports` bundle documents.
- They reorganize the current PASSed v0 result into lexicon / protocol / interface candidate layers.
- They do not replace the detailed v0 source reports, manifests, or scaffolds.
- The detailed v0 reports remain the derivation/support set underneath this current working baseline.

The current implementation is transitional:

- The Python viewer route still carries `/vectorfl-engine/operate` as an engine-facing operating shell.
- Do not read `/vectorfl-engine/operate` as a direct user-surface-to-engine-surface bypass; the current body interpretation still requires the VectorFL intermediate reading surface.
- The user and VectorFL surfaces are being carried by the React/Vite surface app based on `runtime/views/vectorfl_dual_surface.tsx`.
- Tailwind is now wired into the React surface app; the prior hand-written Tailwind-like CSS should not be expanded further.
- The older integrated engine manifests and worker execution loop still matter as runtime evidence, but they are not the UI structure itself.

## canonical current assets

These are the first files to inspect for the current integrated-engine work.

### engine runtime code

- `app/runtime/vectorfl_integrated_engine_api.py`
  - Runtime API for operating dialogue, work packet, assignment, worker draft/execution, internal read, synthesis, and supervisor state.
- `app/runtime/vectorfl_integrated_engine_shell.py`
  - Python-rendered integrated-engine shell. Current `/vectorfl-engine/operate` uses this as engine-facing surface.
- `app/core/runtime/viewer_server.py`
  - Viewer server routing. Current routes connect Python engine surface and React user/VectorFL surface.

### React user / VectorFL surface

- `runtime/views/vectorfl_dual_surface.tsx`
  - Current TSX source for user surface and VectorFL surface mock/app surface.
  - Holds teams, roles, lines, selected team/line, modal draft state, and tab switching.
  - Treat as the current user/VectorFL surface source, not as a generated disposable HTML artifact.
- `runtime/views/vectorfl_dual_surface_app/`
  - Vite/React wrapper app for the TSX surface.
  - Current dev URL: `http://127.0.0.1:5174/`.
- `runtime/views/vectorfl_dual_surface_app/README.md`
  - Program boundary note for the React/Vite app: entrypoints, commands, dependency boundary, design boundary, and generated output boundary.
- `runtime/views/vectorfl_dual_surface_app/vite.config.ts`
  - Vite config with React, Tailwind v4, and local aliases.
- `runtime/views/vectorfl_dual_surface_app/src/styles.css`
  - Tailwind import and VectorFL/Paperclip color token layer.
  - Keep this as token/base/dialog/select support; do not rebuild a hand-written Tailwind clone here.
- `runtime/views/vectorfl_dual_surface_app/src/components/ui/`
  - Minimal local shadcn-style wrappers used so the imported TSX surface can run.

### current generated React build

- `runtime/views/vectorfl_dual_surface_app/dist/`
  - Generated Vite build output.
  - Useful for preview/build verification, but not the canonical source.
  - Do not edit directly.

## latest integrated-engine runtime records

These latest manifests represent the current operating object / execution loop state.

- `runtime/manifests/vectorfl_integrated_engine_operating_dialogue_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_work_packet_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_assignment_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_worker_launch_draft_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_worker_execution_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_worker_session_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_codex_run_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_internal_read_run_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_internal_read_report_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_synthesis_run_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_synthesis_report_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_supervisor_route_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_supervisor_gate_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_implementation_brief_latest_v0.json`
- `runtime/manifests/vectorfl_integrated_engine_implementation_launch_gate_latest_v0.json`

Reading rule:

- These are latest runtime records, not permanent design specs.
- Use them to understand what actually ran and what the shell currently displays.
- Do not treat an old latest execution as current truth unless the freshness gate confirms it belongs to the current operating object/draft chain.

## current checkpoint / explanation reports

These reports explain why the current shape exists.

- `docs/reports/vectorfl_integrated_engine_current_position_checkpoint_v0.md`
  - Best prior checkpoint for how Paper/proper/operable work evolved into integrated-engine work.
- `docs/reports/vectorfl_integrated_engine_three_surface_reframe_v0.md`
  - Earlier three-surface framing when `/operate`, `/vectorfl`, `/engine` were still described as separate Python viewer modes.
  - Important: this is partly superseded by the current decision that `/vectorfl-engine/operate` is now the engine surface and the React app carries user/VectorFL surfaces.
- `docs/reports/vectorfl_integrated_engine_worker_execution_loop_log_v0.md`
  - Worker execution loop record.
- `docs/reports/vectorfl_integrated_engine_internal_inspection_v0.md`
  - Internal inspection record for engine hardening.
- `docs/reports/vectorfl_page_shell_codex_gemini_operating_subject_merge_plan_v0.md`
  - Earlier merge/translation plan about page shell, operable surface, and Codex/Gemini operating subject behavior.
  - Keep as lineage context, not as the current implementation target.

## Paper / proper / bridge lineage

These are not the active user/VectorFL surface, but they explain the supervisor bridge lineage.

### Paper proper / bridge scripts

- `scripts/run_vectorfl_paper_proper_mock.py`
- `scripts/run_vectorfl_paper_codex_bridge.py`
- `scripts/run_vectorfl_paper_gemini_crosscheck_bridge.py`
- `scripts/run_vectorfl_paper_actual_export_gate_validator.py`
- `scripts/run_vectorfl_paper_weekend_pilot_mock.py`

### Paper views

- `runtime/views/vectorfl_paper_proper/index.html`
  - Paper proper supervisor bridge surface.
  - Do not confuse with the current integrated-engine user/VectorFL surface.
- `runtime/views/vectorfl_paper_weekend_pilot/index.html`
  - Weekend pilot / legacy-pilot surface.
  - Archive/reference role only unless explicitly reopened.

### Paper manifests

Representative active/latest Paper bridge records:

- `runtime/manifests/vectorfl_paper_codex_handoff_latest_v0.json`
- `runtime/manifests/vectorfl_paper_codex_return_latest_v0.json`
- `runtime/manifests/vectorfl_paper_gemini_review_latest_v0.json`
- `runtime/manifests/vectorfl_paper_supervisor_decision_latest_v0.json`
- `runtime/manifests/vectorfl_paper_actual_export_host_record_slot_v0.json`
- `runtime/manifests/vectorfl_paper_actual_export_gate_validation_latest_v0.json`
- `runtime/manifests/vectorfl_paper_actual_export_gate_validation_dry_run_v0.json`
- `runtime/manifests/vectorfl_paper_reference_candidate_validation_comparison_v0.json`

Reading rule:

- These explain the validator, handoff, return, cross-check, and supervisor decision loop.
- They should not be promoted into current slot, gate close, or actual-export truth without explicit supervisor action.

## Operable surface lineage

The operable surface remains a useful reference for tested control-surface ideas and Codex/Gemini lane behavior.

- `app/runtime/vectorfl_operable_surface_set.py`
- `scripts/run_vectorfl_operable_surface_set.py`
- `runtime/views/vectorfl_operable_surface/index.html`

Useful generated groups under `runtime/views/vectorfl_operable_surface/`:

- `engine-overview.*`
- `agent-mcp-control.*`
- `worker-inbox.*`
- `lane-detail-chatgpt.*`
- `lane-detail-gemini.*`
- `lane-detail-claude.*`
- `lane-editor-chatgpt.*`
- `lane-editor-gemini.*`
- `lane-editor-claude.*`
- `line-review.*`
- `trace-audit.*`
- `external-resources.*`

Reading rule:

- Use this as prior operable-surface evidence.
- Do not treat it as the current integrated-engine surface unless a specific unit is intentionally translated.

## historical page shell / older generated views

These are important lineage assets but should not drive the current screen by default.

- `runtime/views/vectorfl_page_shell/`
- `runtime/views/vectorfl_page_mock/`
- `runtime/views/vectorfl_page/`

Reading rule:

- These explain earlier graph/page shell attempts.
- Current user/VectorFL direction should not collapse back into this layer unless the supervisor explicitly reopens page shell integration.

## reference readings and design lineage

Paperclip-related readings are relevant because they shaped the current user/VectorFL surface direction.

- `docs/reports/paperclip_native_product_reading_v0.md`
- `docs/reports/paperclip_native_page_taxonomy_and_operable_flow_v0.md`
- `docs/reports/paperclip_git_search_surface_translation_v0.md`
- `docs/reports/paperclip_rereading_for_vectorfl_operating_flow_v0.md`
- `docs/reports/paperclip_vs_vectorfl_operating_screen_gap_review_v0.md`
- `docs/reports/vectorfl_paperclip_tab_flow_merge_plan_v0.md`
- `docs/specs/paperclip_agent_configuration_and_instruction_surface_reading_v0.md`
- `docs/specs/paperclip_frame_component_extraction_reading_v0.md`
- `docs/specs/paperclip_instruction_and_handoff_structure_v0.md`
- `docs/specs/paperclip_internal_work_assignment_reading_v0.md`
- `docs/specs/paperclip_shell_extraction_boundary_v0.md`

Reading rule:

- Do not copy Paperclip as a visual skin only.
- The useful lesson is object-preserving navigation, setup-inside-tabs, role-aware pages, and a surface that supports operation rather than tab-only listing.

## Gemini / Codex assistant context

Gemini is currently a rear-side helper, not the primary operating authority.

Use Gemini for:

- internal flow reading
- line-script candidate inspection
- translation material discovery
- rear-side summary and omission/risk check

Use Codex for:

- program structure
- code changes
- runtime integration
- bridge/validator implementation and verification

Do not treat either tool as permanently fixed:

- the operating engine should allow Codex, Gemini, Claude Code, or later worker tools to be swapped by registry/config over time.
- current UI should not hard-code worker identity as the main conceptual axis.

## active dev URLs and commands

Typical current URLs:

- Python engine surface: `http://127.0.0.1:8421/vectorfl-engine/operate`
- React user/VectorFL surface: `http://127.0.0.1:5174/`

Typical verification:

- `python3 -m py_compile app/runtime/vectorfl_integrated_engine_shell.py app/core/runtime/viewer_server.py`
- `npm run build` from `runtime/views/vectorfl_dual_surface_app`
- `curl -s -o /tmp/vectorfl_dual_surface_check.html -w '%{http_code}' http://127.0.0.1:5174/`
- `curl -s -o /tmp/vectorfl_engine_check.html -w '%{http_code}' http://127.0.0.1:8421/vectorfl-engine/operate`

## what should not be reorganized yet

Do not move these yet:

- `runtime/manifests/vectorfl_integrated_engine_*`
- `runtime/manifests/vectorfl_paper_*`
- `runtime/views/vectorfl_paper_proper/`
- `runtime/views/vectorfl_operable_surface/`
- `runtime/views/vectorfl_page_shell/`
- `runtime/views/vectorfl_dual_surface.tsx`
- `runtime/views/vectorfl_dual_surface_app/`

Reason:

- many of these are referenced by scripts, reports, or viewer routes.
- physical reorganization should wait until the logical map is stable.

## next cleanup candidates

Recommended next cleanup sequence:

1. Decide whether `runtime/views/vectorfl_dual_surface_app/dist/` should be tracked, ignored, or treated as runtime build output.
   - Current decision: ignored as generated output in `runtime/views/vectorfl_dual_surface_app/.gitignore`.
2. Decide whether `runtime/views/vectorfl_dual_surface.tsx` should move into the app `src/` after the surface stabilizes.
3. Add a small `runtime/views/folder_status.md` update through the normal inventory/status route, not by hand-editing the rendered status file.
4. Add a future `runtime/manifests/vectorfl_integrated_engine_asset_registry_v0.json` only if code wants a machine-readable index later.
5. Defer physical folder moves until the user/VectorFL/engine surface split is stable in daily use.

## compact reading order for another CLI

If another CLI must learn the current integrated engine quickly, read in this order:

1. `vectorfl_status.md`
2. `docs/reports/vectorfl_integrated_engine_current_position_checkpoint_v0.md`
3. `docs/reports/vectorfl_integrated_engine_asset_index_v0.md`
4. `app/runtime/vectorfl_integrated_engine_api.py`
5. `app/runtime/vectorfl_integrated_engine_shell.py`
6. `app/core/runtime/viewer_server.py`
7. `runtime/views/vectorfl_dual_surface.tsx`
8. `runtime/views/vectorfl_dual_surface_app/src/styles.css`
9. `runtime/manifests/vectorfl_integrated_engine_operating_dialogue_latest_v0.json`
10. `runtime/manifests/vectorfl_integrated_engine_worker_execution_latest_v0.json`

## final operating rule

For now, treat the integrated-engine assets as a mapped working set:

- keep physical files in place
- keep source vs generated distinction visible
- keep Paper/proper/operable/page-shell lineage available but subordinate
- keep current user/VectorFL work in the React surface app
- keep engine inventory and maintenance in the Python engine surface until a later program-grade frontend split is explicit
