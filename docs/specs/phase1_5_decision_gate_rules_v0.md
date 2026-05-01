# Phase 1.5 Decision Gate Rules v0

## Status

- phase: `phase1_5_usage_loop_binding`
- authority: `working_spec`
- baseline_promotion: none

## Execution

The CLI loop proceeds automatically unless one of these stop conditions is detected:

1. `authority_conflict`
   - Existing baseline, constitution, SSOT, or authority meaning would be changed.
2. `destructive_move_required`
   - Existing canonical path must be deleted, renamed, or moved.
3. `final_naming_lock_required`
   - User-only official naming or final label must be chosen.
4. `structurally_meaningful_options_gt_1`
   - Two or more viable options would create materially different future structures.

Automatic proceed cases:

- weak ambiguity that can be marked `PROVISIONAL`;
- missing evidence that can be recorded as a gap;
- pointer-level exploration;
- draft artifact generation;
- runtime draft instance creation;
- usage guide or validation report creation;
- merge/diff where no authority replacement is implied.

Decision request format, when needed:

- What changed:
- Why user decision is required:
- Option A:
- Option B:
- Recommendation:
- Safe default if no reply:

## Code Binding

`scripts/cli/build_question_packet.py` records stop candidates in:

- `constraints.stop_conditions`
- `hold_reason_if_any`
- `merge_mode_candidate`
- `ambiguity_notes`

`scripts/cli/merge_or_diff.py` turns those stop candidates into:

- `chosen_mode: hold`
- `user_decision_required: true`
- `user_decision_reason_if_any`
- `unresolved_tensions`

`scripts/cli/write_reingress_record.py` preserves the unresolved stop reasons in the reingress record.

## Interpretation

Reducing user intervention is central because the usage loop should mature through repeated runs. If Codex asks for a decision on every ambiguity, the loop becomes conversational blocking rather than operational binding. The right boundary is narrow: ask only when continuing would silently change authority, canonical paths, final names, or future structure.

## Validation

The stop gate is not expected to be perfect semantic understanding. It is a conservative operating gate:

- it catches obvious high-risk terms;
- it records reasons rather than deleting tension;
- it still permits ordinary exploration, diff, and provisional work;
- it keeps baseline promotion outside automatic execution.

Expected result: most usage-loop questions proceed; authority/naming/destructive requests become `hold`.
