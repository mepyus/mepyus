# Space Boundary Camera-Lens Session 4 Helper Patch Readiness v0

## 1. status

```yaml
report_status: session_validation_report
package: docs/reports/space_boundary_camera_lens_operationalization_package_v0.md
session: Session 4. helper patch readiness check
verdict: PASS_WITH_NOTE
patch_readiness: PATCH_CANDIDATE_AFTER_LENS_BASE_AND_SUBTYPE_NOTE
baseline_lock: false
schema_enforcement: false
implementation: false
runtime_manifest_created: false
helper_patch_applied: false
```

## 2. goal check

Question:

```text
Should scripts/cli/space_boundary_lookup_packet.py be patched now to weight lenses by source surface?
```

This session compares:

```text
raw helper lens ranking
vs source-surface lens order
vs Codex final lens selection
```

## 3. current helper behavior

Current helper does:

- source surface guess
- candidate asset ranking
- microspace match
- keyword / microspace-based lens suggestion
- guardrail extraction
- user card template

Current helper does not do:

- source-surface-weighted lens ranking
- runtime artifact subtype split
- generated report section-aware matching
- final state decision
- file writes

## 4. repeated correction pattern

| Surface | Raw helper issue | Codex correction |
| --- | --- | --- |
| external material | multiple workflow clusters may appear | use technical/maker/user/risk/residue first |
| generated report | external clusters can over-match full report body | read as validation_return / residue first |
| Codex output | all lenses can fire from report vocabulary | source surface overrides keyword similarity |
| runtime event log | OpenMythos / process lenses can appear from generic terms | use evidence/event first |
| structured return | treated as generic runtime artifact | use expected-vs-observed first |
| program artifact | treated as generic runtime artifact | use artifact-role first |
| conversation | technical/process hints can dominate | use user-intent / feature-direction first |

Repeated conclusion:

```text
Source surface must dominate lens ranking before keyword matching.
```

## 5. patch-readiness criteria

| Criterion | Result | Note |
| --- | --- | --- |
| Same correction repeats across cases | PASS | All non-external cases needed source-surface override. |
| Source-surface weighting would reduce noise | PASS | Especially generated reports and runtime artifacts. |
| Codex judgment remains final | PASS | Patch can remain suggestion-only. |
| Implementation can be small/read-only | PASS | Add lens weighting and maybe subtype hints only. |
| No schema/runtime/index mutation needed | PASS | Helper stdout JSON only. |
| Lens vocabulary is complete enough | PASS_WITH_NOTE | `evidence/event`, `expected-vs-observed`, `artifact-role`, `return-state` are not in current `LENS_HINTS`. |
| Source subtype detection is complete enough | PASS_WITH_NOTE | Worker return and program artifact are collapsed under `runtime_artifact`. |

## 6. recommended patch scope

Patch candidate should be narrow:

```text
source-surface-weighted lens ranking only
```

Allowed changes:

- add surface default lens order map
- add new lens hint labels:
  - `evidence/event`
  - `expected-vs-observed`
  - `artifact-role`
  - `return-state`
- add source subtype hints:
  - `worker_return`
  - `program_artifact`
  - possibly `runtime_event`
- sort candidate lenses with source-surface weighting before raw score
- keep raw keyword/microspace reasons visible

Not allowed:

- deciding final state
- deciding promotion
- writing return records
- updating microspace index
- fetching web
- loading broad report stacks

## 7. why not patch immediately in this session

Reason:

```text
The patch is justified, but the lens vocabulary and runtime subtype labels should be documented first so the helper does not silently introduce new operating language.
```

This avoids turning a script patch into an implicit theory change.

The right sequence is:

```text
1. write small lens/subtype clarification note
2. patch helper with source-surface weighting
3. rerun Session 1 cases
4. validate noise reduction
```

## 8. patch readiness verdict

```yaml
verdict: PASS_WITH_NOTE
patch_readiness: PATCH_CANDIDATE_AFTER_LENS_BASE_AND_SUBTYPE_NOTE
why:
  - repeated evidence supports source-surface-weighted lens ranking
  - patch can remain read-only and suggestion-only
  - helper currently over-selects external/material lenses for runtime and generated report surfaces
hold_reason:
  - new lens labels should be documented before code patch
  - runtime subtypes should be named before code patch
```

## 9. next allowed move

Proceed to:

```text
bounded lens/subtype clarification note
```

Then, if accepted:

```text
Session 5. bounded helper patch
```

## 10. return-to-space judgment

```yaml
return_state: helper_patch_candidate_with_precondition
helper_patch_now: false
microspace_update_needed: false
next_allowed_move: create_lens_subtype_clarification_note_then_patch
```

## 11. unresolved questions

- Should `worker_return` be a source surface subtype or a separate source surface?
- Should `program_artifact` be split from `runtime_artifact` in helper output?
- Should `generated_report` be split into `codex_output_report`, `validation_report`, and `closeout_report`?
- Should the helper output both raw lens ranking and source-weighted lens ranking?
