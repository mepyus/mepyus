# MOVEMENT_RECORD_20260506_PLAN_FROM_SPACE_SETUP_V0

## Status

```yaml
status: movement_record_candidate
date: 2026-05-06
baseline_lock: false
automation: false
gemini_exploration_status: timeout_raw_trace_only
```

## Input Purpose

Use the user's May 6 materials to set up the VectorFL Anchor Stack so external tools plan from space records rather than model-default task decomposition.

The user specifically asked Codex to delegate token-heavy space exploration to Gemini and handle the remaining setup locally.

## Activated Space Memory

- Line: Plan from Space / Session Convergence Prevention
- Axis: model-default planning vs space-grounded planning; small session split vs broad-but-bounded package
- Camera: user relay burden; program continuity; space recovery; external tool plan mode
- Lens: Plan Basis; package sizing; hard boundary / watch / continue; Return-to-Space Value
- Stable anchor: `docs/specs/stable_space_operating_anchor_v0.md`
- Session anchor: `app/work/SESSION_SPACE_ANCHOR_20260506_PLAN_FROM_SPACE_V0.md`

## Space Assets Consulted

- `app/work/PROGRAM_FRAME_EXTERNAL_PATTERN_MAP_V0.md`: external tool roles and VectorFL space as source of truth.
- `app/work/CONTEXT_BUNDLE_TEMPLATE_V0.md`: existing line / axis / camera / lens, stop condition, and recovery route fields.
- `app/work/PACKAGE_END_FIX_REVIEW_V0.md`: tool drift and evidence gap classification.
- `app/work/REVIEW_RECOVERY_GATE_V0.md`: recover / candidate / watch / hold / reject / needs-user classification.
- `app/work/SESSION_43_RESULTS_V0.md`: Package 5 closeout and issue classification.
- `app/work/SESSION_44_RESULTS_V0.md`: user relay prevention and evidence / not-inspected disclosure.
- `app/work/SESSION_45_RESULTS_V0.md`: external material intake with evidence used, not inspected, user card, and Issue Log.
- `app/work/SESSION_46_RESULTS_V0.md`: candidate closeout with watch/backlog and closed implementation/automation boundary.
- `app/work/SESSION_47_RESULTS_V0.md`: space meaning re-attachment, Return-to-Space Value, and Movement Record candidate.
- `docs/specs/space_exploration_contract_v0.md`: bounded exploration result shape.
- `docs/reports/space_cli_token_budget_and_memory_weight_policy_v0.md`: small relevant memory first.
- `docs/reports/space_feedback_loop_return_to_space_record_minimum_v0.md`: lightweight return record minimum and writer HOLD.
- `docs/specs/line_maturity_and_operating_anchor_direction_lock_v0.md`: caution against premature line promotion.

## External Tool Role

Gemini was assigned bounded space exploration only.

Codex handled setup files, synthesis, and local evidence checks.

## Gemini Raw Trace

- packet: `app/work/space-skill-sandbox/relay/prompts/gemini_plan_from_space_exploration_packet_20260506_v0.md`
- outbox: `app/work/space-skill-sandbox/relay/outbox/plan_from_space_exploration_20260506_v0_gemini_outbox_20260506_185315.md`
- raw: `app/work/space-skill-sandbox/outputs/gemini_raw_results/plan_from_space_exploration_20260506_v0_gemini_raw_20260506_185315.txt`
- stderr: `app/work/space-skill-sandbox/outputs/gemini_raw_results/plan_from_space_exploration_20260506_v0_gemini_stderr_20260506_185315.log`

Result:

```text
Gemini CLI timed out after 240 seconds.
likely_state: auth_or_network_or_interactive_wait
stderr included quota/capacity retry messages.
raw output was empty.
```

Judgment:

Gemini output remains raw trace and does not become VectorFL memory. The failed exploration is a watch item, not a blocker for the local anchor setup, because Codex completed a bounded local source check against the primary assets.

## Gemini Compact Crosscheck

- packet: `app/work/space-skill-sandbox/relay/prompts/gemini_plan_from_space_compact_crosscheck_packet_20260506_v0.md`
- outbox: `app/work/space-skill-sandbox/relay/outbox/plan_from_space_compact_crosscheck_20260506_v0_gemini_outbox_20260506_190215.md`
- packaged return: `docs/reports/plan_from_space_anchor_stack_gemini_compact_crosscheck_return_v0.md`

Result:

```text
Gemini compact crosscheck completed.
It supported Plan Basis as the grounding gate and identified boundary integrity / non-inspected evidence disclosure as the strongest watch item.
```

## Gemini Manual Bounded Exploration Return

- original packet: `app/work/space-skill-sandbox/relay/prompts/gemini_plan_from_space_exploration_packet_20260506_v0.md`
- delivery route: user manual relay
- packaged return: `docs/reports/plan_from_space_bounded_exploration_gemini_manual_return_v0.md`
- relay bridge note: `docs/specs/manual_external_tool_relay_bridge_note_v0.md`

Result:

```text
Manual Gemini result supplied the bounded exploration report that the scripted run could not complete.
It supports the same Anchor Stack direction and adds a temporary manual-relay watch.
```

## Gemini Persisted LACL Assets Return

- delivery route: user manual relay
- guide candidate: `GEMINI.md`
- LACL result candidate: `docs/reports/lacl_regrounding_deep_exploration_result_20260506_v0.md`
- PV setup touched: `docs/specs/anchor_position_value_layer_setup_v0.md`
- packaged return: `docs/reports/lacl_regrounding_gemini_persisted_assets_packaging_20260506_v0.md`
- correction record: `docs/reports/lacl_regrounding_persistence_downshift_correction_20260506_v0.md`

Result:

```text
Gemini supplied useful LACL and PV candidate values, but also wrote authority-like language.
Codex kept the useful findings and downshifted authority / registry / permanent-memory claims.
```

## Map-Position Route Buildout

- compact anchor: `app/work/COMPACT_POSITION_ANCHOR_20260506_MAP_POSITION_ROUTE_BUILDOUT_V0.md`
- Plan Basis: `app/work/PLAN_BASIS_20260506_MAP_POSITION_ROUTE_BUILDOUT_V0.md`
- route seed: `docs/indexes/anchor_map_position_route_seed_v0.md`
- Gemini packet: `app/work/space-skill-sandbox/relay/prompts/gemini_anchor_map_position_discovery_packet_20260506_v0.md`

Result:

```text
Codex created a first route seed for choosing which PV IDs future small anchors should carry.
The route seed is intentionally candidate-only and now has a Gemini packet for deeper evidence validation.
```

## Route Input Evidence Buildout

- compact anchor: `app/work/COMPACT_POSITION_ANCHOR_20260506_ROUTE_INPUT_EVIDENCE_BUILDOUT_V0.md`
- Plan Basis: `app/work/PLAN_BASIS_20260506_ROUTE_INPUT_EVIDENCE_BUILDOUT_V0.md`
- evidence matrix: `docs/indexes/anchor_route_input_evidence_matrix_v0.md`
- gate sequence: `docs/specs/anchor_stack_plan_mode_gate_sequence_v0.md`
- self-application trial: `docs/reports/anchor_gate_sequence_self_application_trial_20260506_v0.md`
- route seed updated: `docs/indexes/anchor_map_position_route_seed_v0.md`

Result:

```text
Codex sampled the May 6 nine input documents and linked route rows to evidence pointers.
The pass added ROUTE_INPUT_CLASSIFICATION as a candidate and extracted the four plan-mode gates.
Codex also recorded a self-application trial so the gate sequence is tested during setup, not only documented.
```

## Gemini Anchor Map Position Discovery Return

- delivery route: user manual relay
- packaged return: `docs/reports/gemini_anchor_map_position_discovery_return_packaging_20260506_v0.md`
- route seed updated: `docs/indexes/anchor_map_position_route_seed_v0.md`

Result:

```text
Gemini validated the current route seeds as mostly keep, flagged ROUTE_INPUT_CLASSIFICATION as merge-watch,
and proposed ROUTE_SPACE_RESIDUE_SAMPLING as a new candidate.
Codex downshifted Gemini's AUTHORITY / RETURN_READY language and kept the report as worker evidence.
```

## External Plan Trial Set A Setup

- compact anchor: `app/work/COMPACT_POSITION_ANCHOR_20260506_EXTERNAL_PLAN_TRIAL_SETUP_V0.md`
- Plan Basis: `app/work/PLAN_BASIS_20260506_EXTERNAL_PLAN_TRIAL_SETUP_V0.md`
- Gemini packet: `app/work/space-skill-sandbox/relay/prompts/gemini_external_tool_planning_trial_set_a_20260506_v0.md`
- review template: `docs/specs/external_tool_plan_return_review_template_v0.md`

Result:

```text
Codex prepared the first practical external-tool planning trial.
The trial tests PLAN_BASIS -> bounded plan with route/PV gates before accepting worker output.
Codex also updated the older plan wrapper, reference pack, and gate checklist so they require route/PV fields.
```

## Gemini External Planning Trial Set A Return

- delivery route: user manual relay
- review: `docs/reports/gemini_external_tool_planning_trial_set_a_return_review_20260506_v0.md`
- created spec: `docs/specs/useful_shape_maturation_boundary_v0.md`
- created spec: `docs/specs/active_residue_marker_policy_v0.md`
- created spec: `docs/specs/external_tool_runner_reliability_watch_v0.md`

Result:

```text
Gemini returned Plan Basis before plan and avoided default multi-session decomposition.
Codex reviewed it as PASS_WITH_WATCH because AUTHORITY / TRIAL_PLAN_READY language required downshift.
The accepted plan produced three candidate setup specs: maturation boundary, active/residue marker policy, and runner reliability watch.
```

## Current Position Check After Set A

- report: `docs/reports/current_position_check_20260506_anchor_stack_after_set_a_v0.md`
- entry: `app/work/CURRENT_POSITION_20260506_ANCHOR_STACK_AFTER_SET_A_V0.md`

Result:

```text
Codex checked the current position against the space records and May 6 nine-doc principles.
The setup is no longer in basic anchor creation; it is in route/PV/gate trial and maturation.
Current review label remains PASS_WITH_WATCH because external worker authority/status drift and manual relay remain active watches.
```

## Big-Frame Operating Structure Setup

- compact anchor: `app/work/COMPACT_POSITION_ANCHOR_20260506_BIG_FRAME_SETUP_V0.md`
- Plan Basis: `app/work/PLAN_BASIS_20260506_BIG_FRAME_SETUP_V0.md`
- big frame: `docs/specs/anchor_stack_big_frame_operating_structure_v0.md`
- surface tiers: `docs/indexes/anchor_stack_operating_surface_tiers_v0.md`
- role boundary: `docs/specs/codex_gemini_user_role_boundary_v0.md`
- closeout: `docs/reports/anchor_stack_big_frame_setup_closeout_20260506_v0.md`

Result:

```text
Codex set the big-frame operating structure directly, per user instruction.
The setup now starts from Current Position + Big Frame + Surface Tiers, not manifest replay.
Gemini's role is bounded exploration/crosscheck; Codex owns setup, synthesis, packaging, and stabilization.
```

## Validation Lens Alignment Review

- report: `docs/reports/anchor_stack_validation_lens_alignment_review_20260506_v0.md`
- corrected file: `docs/indexes/anchor_stack_operating_surface_tiers_v0.md`
- corrected file: `docs/specs/anchor_stack_big_frame_operating_structure_v0.md`
- corrected file: `app/work/CURRENT_POSITION_20260506_ANCHOR_STACK_AFTER_SET_A_V0.md`

Codex rechecked the current setup against the May 6 nine source inputs using a validation lens.
The setup passes with correction: the main structure matches the new principles, but Surface Tiers needed downshift from read-all list to route-selected active pool.

Current safe re-entry meaning:

```text
Current Position -> Big Frame -> route/PV selection -> 3-7 route-specific surfaces
```

not:

```text
read all anchor-related files
```

## Operational Validation Package Setup

- package basis: `app/work/PACKAGE_BASIS_20260506_ANCHOR_STACK_OPERATIONAL_VALIDATION_V0.md`
- package spec: `docs/specs/anchor_stack_operational_validation_package_v0.md`
- execution-list trial: `docs/reports/anchor_stack_session_execution_list_trial_20260506_v0.md`
- recognition probe: `docs/specs/anchor_stack_recognition_probe_v0.md`
- recognition result: `docs/reports/anchor_stack_recognition_probe_result_20260506_v0.md`

Codex set up the next package as a broad-but-bounded operational validation package, not another conceptual setup pass.

The package carries the whole structure:

```text
May 6 principles
-> Current Position
-> Big Frame
-> route/PV selection
-> 3-7 active surfaces
-> package execution list
-> internal validation units
-> Movement Record return
-> recognition probe
```

Bounded execution-list trial result:

```text
Session 43, 44, 46, 47 and current Anchor Stack setup were listed through route/PV/package-sizing/return fields.
The Anchor Stack changed the list from chronological summary into operating judgment.
Review label: PASS_AS_BOUNDED_TRIAL_WITH_WATCH.
```

Recognition probe result:

```text
PASS_LOCAL_RECOGNITION.
The package is now discoverable by package id, execution-list marker, and core PV markers from Current Position, Movement Record, manifest, package spec, trial report, and probe files.
```

## Gemini New LACL Operational Application Trial Packet

- packet: `app/work/space-skill-sandbox/relay/prompts/gemini_new_lacl_operational_application_trial_20260506_v0.md`

Codex prepared a Gemini instruction packet for bounded exploration of how the new Line / Axis / Camera / Lens operating principles apply to actual internal space process records.

The packet asks Gemini to compare old process readings with new LACL readings, return candidate conversion rows, identify application slots, test session/package listing rules, and report recognition / re-discovery markers.

This is a worker exploration packet only.
Codex remains responsible for packaging, downshift, Movement Record updates, and any future map changes.

## Gemini Broad-Deep LACL Material Topology Survey Packet

- packet: `app/work/space-skill-sandbox/relay/prompts/gemini_broad_deep_lacl_material_topology_survey_20260506_v0.md`

Codex prepared a wider and deeper Gemini instruction packet after the user judged the previous LACL trial too narrow.

The new packet asks Gemini to inspect internal material families across maps, indexes, run records, package folders, specs, reports, external material records, and May 6 source inputs if available.

The goal is to identify where LACL signals are distributed and which material families future small anchors should activate.

This packet remains bounded by sampling limits and cannot produce final taxonomy, baseline, registry, schema, workflow, or automation.

## Small Anchor Generation Rule v1 Setup Instruction

- instruction: `app/work/INSTRUCTION_20260506_SMALL_ANCHOR_GENERATION_RULE_V1_SETUP.md`

Codex prepared a setup instruction for the next candidate layer: material-family-aware small anchor generation.

The instruction directs the next worker to create v1 candidate files only, adding:

```text
material_family
signal_zone
recognition_markers
read_depth_default
when_to_deepen
when_to_stop
return_to_space_shape
```

It explicitly forbids treating Gemini's broad-deep topology survey as authority or turning material families into taxonomy, registry, schema, baseline, or automation.

## Created Outputs

- `docs/specs/space_anchor_stack_operating_setup_v0.md`
- `docs/specs/stable_space_operating_anchor_v0.md`
- `docs/indexes/plan_from_space_line_asset_map_v0.md`
- `docs/specs/session_space_anchor_template_v0.md`
- `docs/specs/plan_basis_template_v0.md`
- `docs/specs/external_tool_plan_mode_reference_pack_v0.md`
- `docs/specs/external_tool_plan_prompt_wrapper_v0.md`
- `docs/specs/anchor_stack_gate_checklist_v0.md`
- `docs/specs/movement_record_template_v0.md`
- `docs/indexes/anchor_stack_manifest_v0.md`
- `docs/reports/plan_from_space_anchor_stack_gemini_compact_crosscheck_return_v0.md`
- `docs/reports/plan_from_space_bounded_exploration_gemini_manual_return_v0.md`
- `docs/specs/manual_external_tool_relay_bridge_note_v0.md`
- `docs/specs/anchor_position_value_layer_setup_v0.md`
- `docs/indexes/plan_from_space_position_map_seed_v0.md`
- `docs/specs/compact_position_anchor_template_v0.md`
- `app/work/POSITION_VALUE_LAYER_SESSION_ANCHOR_20260506_V0.md`
- `app/work/space-skill-sandbox/relay/prompts/gemini_position_value_discovery_packet_20260506_v0.md`
- `docs/reports/position_value_discovery_gemini_return_packaging_v0.md`
- `docs/reports/may6_nine_doc_anchor_stack_alignment_review_v0.md`
- `docs/specs/position_value_application_trial_packet_v0.md`
- `app/work/COMPACT_POSITION_ANCHOR_20260506_LACL_REGROUNDING_V0.md`
- `app/work/PLAN_BASIS_20260506_LACL_REGROUNDING_SETUP_V0.md`
- `docs/reports/position_anchor_self_application_trial_20260506_v0.md`
- `app/work/space-skill-sandbox/relay/prompts/gemini_lacl_regrounding_deep_exploration_packet_20260506_v0.md`
- `docs/specs/gemini_lacl_manual_return_intake_contract_v0.md`
- `docs/specs/lacl_regrounding_result_packaging_template_v0.md`
- `docs/indexes/lacl_candidate_synthesis_matrix_seed_v0.md`
- `docs/specs/small_anchor_generation_rule_v0.md`
- `GEMINI.md`
- `docs/reports/lacl_regrounding_deep_exploration_result_20260506_v0.md`
- `docs/reports/lacl_regrounding_gemini_persisted_assets_packaging_20260506_v0.md`
- `docs/reports/lacl_regrounding_persistence_downshift_correction_20260506_v0.md`
- `app/work/COMPACT_POSITION_ANCHOR_20260506_MAP_POSITION_ROUTE_BUILDOUT_V0.md`
- `app/work/PLAN_BASIS_20260506_MAP_POSITION_ROUTE_BUILDOUT_V0.md`
- `docs/indexes/anchor_map_position_route_seed_v0.md`
- `app/work/space-skill-sandbox/relay/prompts/gemini_anchor_map_position_discovery_packet_20260506_v0.md`
- `app/work/COMPACT_POSITION_ANCHOR_20260506_ROUTE_INPUT_EVIDENCE_BUILDOUT_V0.md`
- `app/work/PLAN_BASIS_20260506_ROUTE_INPUT_EVIDENCE_BUILDOUT_V0.md`
- `docs/indexes/anchor_route_input_evidence_matrix_v0.md`
- `docs/specs/anchor_stack_plan_mode_gate_sequence_v0.md`
- `docs/reports/anchor_gate_sequence_self_application_trial_20260506_v0.md`
- `docs/reports/gemini_anchor_map_position_discovery_return_packaging_20260506_v0.md`
- `app/work/COMPACT_POSITION_ANCHOR_20260506_EXTERNAL_PLAN_TRIAL_SETUP_V0.md`
- `app/work/PLAN_BASIS_20260506_EXTERNAL_PLAN_TRIAL_SETUP_V0.md`
- `app/work/space-skill-sandbox/relay/prompts/gemini_external_tool_planning_trial_set_a_20260506_v0.md`
- `docs/specs/external_tool_plan_return_review_template_v0.md`
- `docs/reports/gemini_external_tool_planning_trial_set_a_return_review_20260506_v0.md`
- `docs/specs/useful_shape_maturation_boundary_v0.md`
- `docs/specs/active_residue_marker_policy_v0.md`
- `docs/specs/external_tool_runner_reliability_watch_v0.md`
- `docs/reports/current_position_check_20260506_anchor_stack_after_set_a_v0.md`
- `app/work/CURRENT_POSITION_20260506_ANCHOR_STACK_AFTER_SET_A_V0.md`
- `app/work/COMPACT_POSITION_ANCHOR_20260506_BIG_FRAME_SETUP_V0.md`
- `app/work/PLAN_BASIS_20260506_BIG_FRAME_SETUP_V0.md`
- `docs/specs/anchor_stack_big_frame_operating_structure_v0.md`
- `docs/indexes/anchor_stack_operating_surface_tiers_v0.md`
- `docs/specs/codex_gemini_user_role_boundary_v0.md`
- `docs/reports/anchor_stack_big_frame_setup_closeout_20260506_v0.md`
- `docs/reports/anchor_stack_validation_lens_alignment_review_20260506_v0.md`
- `app/work/PACKAGE_BASIS_20260506_ANCHOR_STACK_OPERATIONAL_VALIDATION_V0.md`
- `docs/specs/anchor_stack_operational_validation_package_v0.md`
- `docs/reports/anchor_stack_session_execution_list_trial_20260506_v0.md`
- `docs/specs/anchor_stack_recognition_probe_v0.md`
- `docs/reports/anchor_stack_recognition_probe_result_20260506_v0.md`
- `app/work/space-skill-sandbox/relay/prompts/gemini_new_lacl_operational_application_trial_20260506_v0.md`
- `app/work/space-skill-sandbox/relay/prompts/gemini_broad_deep_lacl_material_topology_survey_20260506_v0.md`
- `app/work/INSTRUCTION_20260506_SMALL_ANCHOR_GENERATION_RULE_V1_SETUP.md`
- `app/work/SESSION_SPACE_ANCHOR_20260506_PLAN_FROM_SPACE_V0.md`
- `app/work/PLAN_MODE_REFERENCE_PACK_20260506_PLAN_FROM_SPACE_V0.md`
- `app/work/MOVEMENT_RECORD_20260506_PLAN_FROM_SPACE_SETUP_V0.md`
- `app/work/space-skill-sandbox/relay/prompts/gemini_plan_from_space_exploration_packet_20260506_v0.md`
- `app/work/space-skill-sandbox/relay/prompts/gemini_plan_from_space_compact_crosscheck_packet_20260506_v0.md`

## Issue / Watch Item

- Watch: Gemini exploration timed out before producing a usable report.
- Watch: compact crosscheck did not inspect files and must not be treated as full space exploration.
- Watch: user manual relay is currently acceptable as a bridge, but should not become steady-state tool operation.
- Watch: Position Value Layer should remain a small-anchor coordinate layer, not ontology/schema.
- Watch: Gemini position discovery is worker evidence; final map selection remains Codex/User judgment.
- Watch: Position Value Layer is an extension from the nine-document requirements, not an original named layer in the source set.
- Watch: compact anchor self-application has begun, but should be repeated in future turns to find friction.
- Watch: future Gemini LACL result should not update maps directly; it must be packaged and synthesized.
- Watch: Gemini-persisted files may contain overpromotion language; downshift before use.
- Watch: short PV aliases must be normalized to canonical PV IDs before small-anchor reuse.
- Watch: map-position route seed should not become a completed map without Gemini/Codex evidence validation.
- Watch: route rows should be added only if they change actual task behavior.
- Watch: `ROUTE_INPUT_CLASSIFICATION` is candidate-only and may merge with session re-entry or external tool planning.
- Watch: gate sequence is an operating sequence, not a workflow/runner.
- Watch: gate sequence has only a setup-turn self-application trial; it needs a real external-planning trial.
- Watch: Gemini route validation did not inspect May 6 nine documents directly; use it as route crosscheck, not primary input evidence.
- Watch: `ROUTE_SPACE_RESIDUE_SAMPLING` is candidate-only and could become archive taxonomy if overexpanded.
- Watch: Set A trial must be reviewed before accepting worker output into route/PV maps.
- Watch: old plan prompts may still exist elsewhere; use the route/PV-aware wrapper for future planning requests.
- Watch: Set A passed with watch, not full pass, because worker authority/status language still drifted.
- Watch: active/residue markers should be sampled only; do not bulk-label the docs tree.
- Watch: runner reliability watch should not create automation by itself.
- Watch: current setup has moved from anchor creation to trial/maturation; more abstract setup should be resisted unless tied to a bounded trial.
- Watch: big-frame structure is candidate operating frame, not baseline.
- Watch: do not let surface tiers become a registry or whole-space reading order.
- Watch: Gemini should not own operating decisions; use it for bounded exploration/crosscheck.
- Watch: `Plan from Space` line is an operating-anchor candidate for this bounded purpose, but should not be promoted as a general line registry baseline.
- Watch: Anchor Stack should remain a compact re-entry layer, not a new document bureaucracy.
- Watch: Surface Tiers is an active pool. If future sessions bulk-read it as a checklist, the setup will drift away from the May 6 principles.
- Watch: operational validation currently proves bounded local recognition, not yet external worker cognition.
- Watch: package-internal execution units must not be mistaken for separate default sessions.
- Watch: recognition probe passing does not prove that Gemini/Codex/Hermes will apply the package without prompt-level enforcement.
- Watch: new LACL application trial must remain bounded; do not let it become full-space taxonomy or ontology.
- Watch: broad-deep material topology survey can still drift into whole-space inventory; enforce sampling limits and candidate-only return.
- Watch: material-family-aware small anchors must not become a global taxonomy or heavy checklist.

## Return-to-Space Value

- Recoverable material: Anchor Stack file set for plan-before-space correction.
- Reusable judgment: Plan Basis is the acceptance check that distinguishes space-grounded planning from model-default planning.
- Reusable judgment: Broad-but-bounded package is the default when purpose, boundary, and return shape are clear; small session split requires a blocking reason.
- Reusable judgment: boundary integrity should explicitly include non-inspected evidence disclosure.
- Issue / watch: Gemini can be delegated token-heavy exploration, but its logs/results remain raw trace until interpreted.
- Issue / watch: manual user relay should be recorded as temporary bridge, not normalized as operating design.
- Future reuse note: small anchors should pass 1-3 position IDs from the position map seed instead of replaying broad setup text.
- Future reuse note: for external tool planning, start with `PV_PLAN_BASIS_GATE`, `PV_BROAD_BOUNDED_PACKAGE`, `PV_NON_INSPECTED_DISCLOSURE`, and `PV_RETURN_TO_SPACE_CLOSEOUT`.
- Future reuse note: the next useful setup is a position-value application trial, not another abstract layer.
- Future reuse note: Gemini should now be asked for LACL re-grounding evidence, not another general space summary.
- Future reuse note: after Gemini returns, use `lacl_regrounding_result_packaging_template_v0` and then update `lacl_candidate_synthesis_matrix_seed_v0` only as candidate.
- Future reuse note: root tool guides such as `GEMINI.md` need explicit status fields because future tools may overread them as authority.
- Future reuse note: for small anchor creation, choose a route first, then transmit the route's 2-4 canonical PV IDs.
- Future reuse note: give Gemini `gemini_anchor_map_position_discovery_packet_20260506_v0.md` next if more map-position evidence is needed.
- Future reuse note: every future plan-mode run should pass four checks: Pre-Plan, Plan Sizing, Runtime Re-Entry, Closeout/Return-to-Space.
- Future reuse note: next real trial should ask an external tool for `PLAN_BASIS -> bounded plan`, then package its result through the manual worker return route if needed.
- Future reuse note: use `gemini_external_tool_planning_trial_set_a_20260506_v0.md` as the next manual Gemini prompt.
- Future reuse note: review Set A output with `external_tool_plan_return_review_template_v0.md`.
- Future reuse note: external plan requests should include `ROUTE_EXTERNAL_TOOL_PLANNING` and the four canonical PVs before the worker plan.
- Future reuse note: use `useful_shape_maturation_boundary_v0.md` before promoting any new route/PV/gate artifact.
- Future reuse note: use `active_residue_marker_policy_v0.md` only for bounded samples named by current route evidence.
- Future reuse note: repeated manual Gemini relay should trigger runner reliability package planning, not ad hoc normalization.
- Future reuse note: use `CURRENT_POSITION_20260506_ANCHOR_STACK_AFTER_SET_A_V0.md` for next-session re-entry.
- Future reuse note: for future setup work, read `CURRENT_POSITION_20260506_ANCHOR_STACK_AFTER_SET_A_V0.md` then `anchor_stack_big_frame_operating_structure_v0.md` before opening the manifest.
- Future reuse note: Gemini packets should be generated from Codex-owned route/PV/gate decisions, not the other way around.
- Future reuse note: Before external tool planning, use `stable_space_operating_anchor_v0` + relevant line map + session anchor + Plan Basis requirement.
- Future reuse note: when validating the Anchor Stack, use `anchor_stack_validation_lens_alignment_review_20260506_v0.md` and recheck whether the setup changed task behavior.
- Future reuse note: use `PKG_20260506_ANCHOR_STACK_OPERATIONAL_VALIDATION_V0` when testing whether a returned package becomes searchable/re-enterable.
- Future reuse note: future session lists should include route, PV, package sizing, stop/continue, and Return-to-Space fields.
- Future reuse note: package closeout should include a recognition marker set so future route/PV discovery can find it without user relay.
- Future reuse note: package Gemini's new LACL application return as worker evidence before adding any conversion row to a map.
- Future reuse note: use Gemini broad-deep material topology survey results to design more concrete small anchors by material family, not to create a global taxonomy.
- Future reuse note: run `INSTRUCTION_20260506_SMALL_ANCHOR_GENERATION_RULE_V1_SETUP.md` before creating new small anchors for external planning or Gemini exploration.

## Next Re-Entry Trigger

Use this record when:

- an external tool proposes a multi-session plan by default
- Gemini/Codex/Hermes/OmX is asked to draft package/session structure
- a closeout lacks Return-to-Space Value
- the user starts relaying output between tools manually

## Do Not

- Do not declare the Anchor Stack as baseline.
- Do not create an automatic writer or runner from these templates.
- Do not treat the Gemini timeout output as space exploration findings.
- Do not expand this into a broad whole-space inventory.
- Do not treat `GEMINI.md` as primary authority.
- Do not write shortened PV aliases into future anchors when canonical PV IDs exist.
- Do not treat `anchor_map_position_route_seed_v0.md` as a completed map.
- Do not treat `anchor_stack_plan_mode_gate_sequence_v0.md` as automation or as separate-session workflow.
- Do not treat Gemini's `AUTHORITY` or `RETURN_READY` wording as actual authority or memory promotion.
- Do not stabilize `ROUTE_SPACE_RESIDUE_SAMPLING` without a bounded residue sampling trial.
- Do not treat `TRIAL_PLAN_READY` wording as authority or memory promotion.
- Do not convert the useful-shape maturation boundary into a schema.
- Do not use the manifest as the primary reading order.
- Do not let Gemini set or revise the big frame without Codex packaging.
