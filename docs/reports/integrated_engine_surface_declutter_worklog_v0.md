# Integrated Engine Surface Declutter Worklog v0

## 1. Mission

Set up a decluttered integrated-engine surface and a single-handler package pilot across User / VectorFL / Engine.

This package was not:

- full redesign
- multi-agent orchestration
- automatic bridge implementation
- upper/lower unification
- final UI polish

## 2. Phase 1 - Projection Policy And Panel Map

### Produced

- `docs/specs/integrated_engine_surface_projection_policy_v0.md`
- `docs/reports/integrated_engine_surface_active_support_hold_map_v0.md`

### What Became Clearer

- Each surface has a different first question.
- Active/support/hold content is now explicit.
- Bridge/team/trace detail should not be front-surface content.

### Validation

- Distinct first-question check: passed.
- Active/support/hold separation: passed.
- Bridge/team/trace demotion: passed.

## 3. Phase 2 - Decluttered Surface Implementation

### Modified

- `app/ui/integrated_engine/VectorFLIntegrationShell.tsx`

### What Changed

- Shared operating spine was reduced and details moved into support.
- `SingleHandlerPackagePanel` was added.
- User / VectorFL / Engine each project the same package differently.
- Line atlas, selected line inspection, route/log panels, team config, and legacy engine mock are moved or kept in support/detail layers.

### Validation

- Front-surface lightness: passed with note.
- Surface distinction: passed.
- Important structure reachable: passed.
- UI build: passed with `npm run build` in `app/ui/integrated_engine`.

### Remaining Risk

- VectorFL remains dense because CLI packet formation still lives there.

## 4. Phase 3 - Single Handler Package Flow

### Produced

- `docs/reports/integrated_engine_single_handler_package_flow_spec_v0.md`
- `runtime/contracts/integrated_engine_single_handler_package_instance_v0.json`
- `runtime/contracts/integrated_engine_single_handler_return_record_instance_v0.json`

### What Became Clearer

- One handler package can be displayed across all three surfaces.
- Each surface can expose only the fields it needs.
- Same process / different projection is now visible.

### Validation

- One-handler rule: passed.
- Flow coherence: passed.
- No multi-agent dashboard: passed.
- Package JSON parse: passed for `runtime/contracts/integrated_engine_single_handler_package_instance_v0.json`.
- Return-record JSON parse: passed for `runtime/contracts/integrated_engine_single_handler_return_record_instance_v0.json`.

## 5. Phase 4 - Screen Validation

### Produced

- `docs/reports/integrated_engine_surface_declutter_validation_note_v0.md`
- `docs/reports/integrated_engine_single_handler_package_run_note_v0.md`

### What Improved

- User surface is more purpose-first.
- VectorFL surface is more mediation-first.
- Engine surface is more process/return-first.
- End-to-end screen compile path passed through `tsc && vite build`.

### Still Noisy

- `CliHostControlPanel` still needs a later active/support split.
- Some internal authority language remains visible because it is needed for safety.

## 6. Phase 5 - Closeout

### Produced

- `docs/reports/integrated_engine_surface_declutter_worklog_v0.md`
- `docs/reports/integrated_engine_surface_declutter_closeout_note_v0.md`

### Intentionally Not Done

- no second handler
- no multi-team dashboard
- no automation
- no bridge implementation
- no upper/lower unification
- no final UI polish pass

## 7. Final Worklog Verdict

PASS_WITH_NOTE

The shell is now closer to operating mode. It still carries verification-mode residue, mainly in VectorFL packet controls, but the single-handler flow is visible and surface density is reduced.
