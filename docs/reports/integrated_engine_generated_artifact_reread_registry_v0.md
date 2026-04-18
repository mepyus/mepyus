# Integrated Engine Generated Artifact Reread Registry v0

## 1. Verdict

PASS_WITH_CORRECTION

Generated artifacts are not disposable just because a patch or interpretation missed the direction.

They are high-value engine data:

- intended direction
- actual implementation choice
- partial success
- wrong projection
- hidden assumption
- repeated drift
- future correction material

The current error was not that these artifacts exist. The error was that they were treated as finished reports or failed patches instead of being reread as evidence.

## 2. Why This Registry Exists

The integrated engine is supposed to metabolize its own products.

If a patch is wrong, it still contains:

- what the engine thought it was doing
- what the user objected to
- what surface/lens/frame was misapplied
- what part can be reused
- what pattern must not repeat

Therefore generated docs and UI patches must be reread before the next implementation.

## 3. Artifact Classes

### A. Intention Artifacts

These record what the work was trying to become.

Examples:

- `integrated_engine_body_packet_memory_lock_v0.md`
- `integrated_engine_body_process_packet_alignment_audit_v0.md`
- `integrated_engine_body_camera_lens_reread_correction_v0.md`
- `integrated_engine_surface_projection_composition_plan_v0.md`

Use:

```text
Recover the intended body / camera / lens logic.
```

### B. Misread Artifacts

These show where implementation turned structure into visible panels or labels.

Examples:

- `integrated_engine_panel_proliferation_course_correction_note_v0.md`
- `integrated_engine_single_work_package_walkthrough_validation_v0.md`
- `integrated_engine_single_work_package_orientation_patch_note_v0.md`

Use:

```text
Detect panel-first drift and overconfident summary.
```

### C. Partial Success Artifacts

These contain usable pieces even if the overall composition is not right yet.

Examples:

- `integrated_engine_shell_level_shared_operating_spine_patch_note_v0.md`
- `integrated_engine_surface_local_current_object_focus_layer_patch_note_v0.md`
- `integrated_engine_vectorfl_current_work_packet_formation_layer_patch_note_v0.md`
- `integrated_engine_internal_search_evidence_bundle_gate_patch_note_v0.md`
- `integrated_engine_vectorfl_density_hierarchy_patch_note_v0.md`

Use:

```text
Extract working subcomponents without promoting the whole layout.
```

### D. Panel Reuse Artifacts

These show which existing panels can survive if correctly projected.

Examples:

- `integrated_engine_existing_panel_reuse_process_mapping_v0.md`
- `integrated_engine_mock_panel_authority_tone_down_patch_note_v0.md`
- `integrated_engine_surface_exposure_budget_audit_v0.md`
- `integrated_engine_surface_exposure_hierarchy_round_closeout_v0.md`

Use:

```text
Reuse existing panels as local views, not as body structure.
```

### E. Live Code Artifacts

These are the current generated UI structures that must be reread as data:

- `SharedOperatingSpine`
- `SurfaceCurrentObjectFocus`
- `VectorFLMediationProcessMap`
- `CliHostControlPanel`
- `InternalTeamAssignmentPanel`
- `UserCliAssignmentPanel`
- `EngineCliReturnPanel`

Use:

```text
Identify what each component actually makes visible,
what it hides,
and which surface lens it accidentally absorbs.
```

## 4. Reread Findings From Current Generated Artifacts

### Finding 1. Shared spine was useful but easily overpromoted

Good data:

- active turn
- purpose
- route/state
- authority state
- evidence readiness

Wrong tendency:

- treating shared spine as common dashboard.

Correction:

```text
shared spine = orientation only
```

### Finding 2. Surface local focus found the right question but became another panel

Good data:

- User = assignment / decision candidate
- VectorFL = reread / mediation material
- Engine = request / validation / deposit material

Wrong tendency:

- adding another explanatory layer instead of making existing panels read through the local lens.

Correction:

```text
local focus should become projection logic, not a large visible card.
```

### Finding 3. VectorFL packet formation exposed real manual labor

Good data:

- purpose
- locks
- evidence refs
- task lens
- do / do-not
- expected return
- route candidate

Wrong tendency:

- treating visible packet fields as enough, even though evidence was still user-provided or inferred.

Correction:

```text
packet layer is valuable as evidence of what must become structured,
but it is not yet internal-search-backed packet formation.
```

### Finding 4. Internal team panel is not wrong; its placement is unfinished

Good data:

- internal team / role frame
- language 담당 as a real user-surface assignment
- modal execution pattern

Wrong tendency:

- treating language loop as a standalone card rather than a work package assigned to a role.

Correction:

```text
team/role UI must read "this work package is assigned here",
not "here is a team management panel."
```

### Finding 5. Engine return panel is useful but not enough as process surface

Good data:

- request candidate
- validation target
- extraction / deposit candidate
- latest return material

Wrong tendency:

- return/candidate feed can substitute for engine process.

Correction:

```text
Engine surface must foreground process stage and returned material,
not the full user/vectorfl reasoning chain.
```

### Finding 6. Existing mock panels are not trash

Good data:

- slot/card rhythm
- pipeline status rhythm
- event list patterns
- asset/inspection affordances
- team/role/routing visual ideas

Wrong tendency:

- either promote them as core or dismiss them as wrong.

Correction:

```text
mock panels are design clay and process-view candidates.
They must be projected through body/camera/lens before use.
```

## 5. Repeated Drift Pattern

The repeated drift is:

```text
source says body/camera/lens
-> implementation sees missing concept
-> implementation adds visible panel
-> screen becomes denser
-> user still has to mentally assemble process
```

The correction is:

```text
source says body/camera/lens
-> identify current lens
-> derive process stage
-> derive surface projection
-> reuse or collapse existing panels
-> screen becomes less mentally assembled
```

## 6. Generated Artifact Reread Rule

Before any next UI patch:

1. reread the relevant source lock
2. reread the generated patch note that created the current behavior
3. identify which parts are:
   - intention
   - partial success
   - misread
   - reusable data
   - hold
4. only then patch

No generated artifact should be dismissed just because it was "wrong."

## 7. What The Current Artifacts Already Teach

They teach that the first real screen refactor should not be:

```text
add more cards
```

It should be:

```text
take the existing cards and make them projections of the same current work package
```

This means:

- `SurfaceCurrentObjectFocus` should likely become a data derivation/helper, not a dominant card.
- `SharedOperatingSpine` should stay thin.
- `CliHostControlPanel` should stay VectorFL, but its packet output should feed surface projections.
- `InternalTeamAssignmentPanel` should show assignment of the current work package, not generic team management first.
- `EngineCliReturnPanel` should show process material for the current work package, not a broad return feed first.

## 8. What Must Not Be Done

- do not delete generated docs as stale
- do not ignore failed patches
- do not treat patch notes as bureaucratic leftovers
- do not implement from memory after one reread
- do not add a new panel before rereading the panel that already carries related data
- do not flatten generated mistakes into "bad work"

## 9. Next Use

Use this registry as the entry gate for the next implementation:

```text
surfaceProjection composition patch
```

That patch must start by rereading:

- this registry
- `integrated_engine_body_camera_lens_reread_correction_v0.md`
- `integrated_engine_surface_projection_composition_plan_v0.md`
- `integrated_engine_existing_panel_reuse_process_mapping_v0.md`
- the current components in `VectorFLIntegrationShell.tsx`

Then it should change composition, not add panels.
