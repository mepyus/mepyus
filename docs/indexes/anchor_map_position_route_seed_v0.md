# Anchor Map Position Route Seed v0

## Status

```yaml
status: route_seed_candidate
date: 2026-05-06
baseline_lock: false
automation: false
registry: false
schema: false
scope: plan_from_space_anchor_map_positioning
```

## Purpose

This seed starts the "our map" layer: where small anchors should attach when a future session or external tool needs compact position values.

It is a route seed, not a completed map. It uses canonical PV IDs from `docs/indexes/plan_from_space_position_map_seed_v0.md`.

## Route Row Fields

```text
route_id:
use_when:
position_ids:
map_slot:
line_axis_camera_lens_basis:
wrong_completion_prevented:
return_shape:
watch:
do_not_infer:
next_evidence_needed:
```

## Current Route Seeds

### ROUTE-01 External Tool Planning

```yaml
route_id: ROUTE_EXTERNAL_TOOL_PLANNING
use_when: Gemini/Codex/Hermes/OmX proposes a plan or package structure.
position_ids:
  - PV_PLAN_BASIS_GATE
  - PV_BROAD_BOUNDED_PACKAGE
  - PV_NON_INSPECTED_DISCLOSURE
  - PV_RETURN_TO_SPACE_CLOSEOUT
map_slot: entry_gate / sizing_axis / evidence_boundary / closeout_gate
line_axis_camera_lens_basis: Plan from Space line; small split vs broad package axis; external tool plan-mode camera; Plan Basis and Return-to-Space lenses.
wrong_completion_prevented: model-default multi-session planning and output-only closeout.
return_shape: Plan Basis, bounded plan, evidence scope, issue/watch, reusable judgment.
watch: session_convergence_watch; evidence_overclaim_watch.
do_not_infer: no universal workflow; no full-space coverage claim.
next_evidence_needed: examples where external tool planning succeeded or failed with this route.
```

### ROUTE-02 Bounded Gemini Reread

```yaml
route_id: ROUTE_BOUNDED_GEMINI_REREAD
use_when: Gemini should read more space to answer a specific map/line/axis question.
position_ids:
  - PV_BOUNDED_REREAD_UNIT
  - PV_NON_INSPECTED_DISCLOSURE
  - PV_RAW_TRACE_BOUNDARY
map_slot: retrieval_route / evidence_boundary / raw_trace_boundary
line_axis_camera_lens_basis: bounded reread axis; provenance camera; non-inspected disclosure lens.
wrong_completion_prevented: broad scan, decorative summary, and raw trace promotion.
return_shape: read trace, missing/not-inspected scope, evidence-backed candidates, Return-to-Space findings.
watch: broad_scan_watch; raw_trace_promotion_watch.
do_not_infer: no direct map update; no Gemini authority.
next_evidence_needed: active/residue sampling from older docs and reports.
```

### ROUTE-03 Manual Worker Return Intake

```yaml
route_id: ROUTE_MANUAL_WORKER_RETURN_INTAKE
use_when: the user manually relays Gemini or another worker result.
position_ids:
  - PV_MANUAL_RELAY_BRIDGE
  - PV_RAW_TRACE_BOUNDARY
  - PV_RETURN_TO_SPACE_CLOSEOUT
map_slot: relay_boundary / raw_trace_boundary / closeout_gate
line_axis_camera_lens_basis: User Relay Burden Reduction line; raw trace vs memory axis; user burden and provenance cameras.
wrong_completion_prevented: user becoming dispatcher and worker report becoming memory by polish.
return_shape: packaged worker return, accepted candidate values, corrections, watch items.
watch: normalized_relay_watch; worker_authority_drift.
do_not_infer: no permanent relay workflow; no final truth from worker output.
next_evidence_needed: stable non-manual runner path after quota/auth issues are solved.
```

### ROUTE-04 Authority Downshift

```yaml
route_id: ROUTE_AUTHORITY_DOWNSHIFT
use_when: a tool-created file claims mandate, authority, registry, constitution, permanent memory, or baseline.
position_ids:
  - PV_LINE_MATURITY_CAUTION
  - PV_RAW_TRACE_BOUNDARY
  - PV_NON_INSPECTED_DISCLOSURE
map_slot: maturity_guard / authority_boundary / evidence_boundary
line_axis_camera_lens_basis: line maturity caution; raw trace vs interpreted memory axis; provenance camera.
wrong_completion_prevented: candidate setup becoming space law.
return_shape: downshift correction record and alias/canonical normalization if needed.
watch: axis_ontology_watch; registry_drift_watch.
do_not_infer: no baseline; no ontology; no registry; no schema.
next_evidence_needed: recurring overpromotion examples across tools.
```

### ROUTE-05 Session Re-Entry

```yaml
route_id: ROUTE_SESSION_REENTRY
use_when: a future session needs compact recovery without replaying all setup records.
position_ids:
  - PV_CURRENT_POSITION_ENTRY
  - PV_PLAN_BASIS_GATE
  - PV_RETURN_TO_SPACE_CLOSEOUT
map_slot: current_position / entry_gate / closeout_gate
line_axis_camera_lens_basis: program continuity camera; Plan Basis and Return-to-Space lenses.
wrong_completion_prevented: session-loss drift and context replay overload.
return_shape: compact position anchor plus next Plan Basis.
watch: session_loss_watch; done_without_memory_watch.
do_not_infer: no auto-continue; no current-position authority unless user/Codex writes it explicitly.
next_evidence_needed: real next-session recovery trial.
```

### ROUTE-06 Input Classification

```yaml
route_id: ROUTE_INPUT_CLASSIFICATION
use_when: new user input arrives and the current line / axis / camera / lens is not yet fixed.
position_ids:
  - PV_CURRENT_POSITION_ENTRY
  - PV_PLAN_BASIS_GATE
  - PV_LINE_MATURITY_CAUTION
map_slot: input_gate / current_position / maturity_guard
line_axis_camera_lens_basis: user input first activates a line; Plan Basis then fixes axis, camera, and lens before plan.
wrong_completion_prevented: immediate model-default planning from user input.
return_shape: compact line/axis/camera/lens classification plus Plan Basis or small anchor.
watch: decorative_lacl_watch; route_overlap_watch.
do_not_infer: no taxonomy; no global classifier; no automatic routing.
validation_state: merge_watch
next_evidence_needed: trial whether this is only the Pre-Plan phase of external tool planning or a distinct route.
```

### ROUTE-07 Space Residue Sampling

```yaml
route_id: ROUTE_SPACE_RESIDUE_SAMPLING
use_when: older reports or records may be residue rather than active route evidence.
position_ids:
  - PV_NON_INSPECTED_DISCLOSURE
  - PV_LINE_MATURITY_CAUTION
map_slot: evidence_boundary / maturity_guard
line_axis_camera_lens_basis: active evidence vs residue axis; line maturity caution lens; provenance camera.
wrong_completion_prevented: treating old residue as current anchor, source of truth, or baseline.
return_shape: active / candidate_only / watch_only / residue sampling note.
watch: residue_overread_watch; full_space_audit_watch.
do_not_infer: no whole-space audit; no archive taxonomy; no automatic active/residue classifier.
validation_state: new_candidate_from_gemini
next_evidence_needed: bounded sample of older reports named by Gemini or Codex using `docs/specs/active_residue_marker_policy_v0.md`.
```

## Map Gaps For Gemini

- Which older space records are active route evidence vs residue?
- Are there additional route slots beyond entry, sizing, evidence, relay, maturity, and closeout?
- Which LACL items should be merged because they produce the same route behavior?
- Which candidate routes actually change task shape in past sessions?
- Which route needs a new PV rather than a combination of existing PVs?
- Does `ROUTE_INPUT_CLASSIFICATION` remain distinct from `ROUTE_SESSION_REENTRY`, or should it merge?
- Does `ROUTE_SPACE_RESIDUE_SAMPLING` change task behavior enough to remain a route?

## Do Not

- Do not treat this route seed as a line registry.
- Do not add route rows without evidence pointers.
- Do not create automation from this seed.
- Do not let route count grow unless the route changes actual task behavior.
