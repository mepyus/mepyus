# Phase 1.17 Flow Validation Reread Trial Report v0

## Verdict

PASS_WITH_NOTE

## Scope

This was a bounded upper reread trial only.

- no schema change
- no lower emitter change
- no classifier change
- no lens naming
- no axis/precursor naming
- no promotion/action layer

The only question was whether `flow support` already works as a real reread cue.

## Trial Set

Base set:

1. observer/review: `route_selection_policy_v0` default
2. observer/report: `raw_intake_gap_analysis_before_middle_layer_fix_v1`
3. preprocess comparison: `builder_choi_interview`
4. preprocess comparison: `codex_ambassader_jung`
5. compact/title-only: `middle_layer_thickening_program_instruction_v1`

Deliberately added flow-rich cases:

6. flow-rich local case: `route_selection_policy_v0` / `line_seed_004`
7. flow-rich local case: `route_selection_policy_v0` / `line_seed_024`

Generated outputs:

- [observer_review_route_selection_policy_v0_default.json](/Users/sungsookim/universe/vectorfl_replica/runtime/reread_trials/phase1_17_flow_validation/observer_review_route_selection_policy_v0_default.json)
- [observer_report_raw_intake_gap_analysis.json](/Users/sungsookim/universe/vectorfl_replica/runtime/reread_trials/phase1_17_flow_validation/observer_report_raw_intake_gap_analysis.json)
- [preprocess_builder_choi_interview.json](/Users/sungsookim/universe/vectorfl_replica/runtime/reread_trials/phase1_17_flow_validation/preprocess_builder_choi_interview.json)
- [preprocess_codex_ambassader_jung.json](/Users/sungsookim/universe/vectorfl_replica/runtime/reread_trials/phase1_17_flow_validation/preprocess_codex_ambassader_jung.json)
- [observer_compact_middle_layer_instruction.json](/Users/sungsookim/universe/vectorfl_replica/runtime/reread_trials/phase1_17_flow_validation/observer_compact_middle_layer_instruction.json)
- [flow_rich_route_selection_seed_004.json](/Users/sungsookim/universe/vectorfl_replica/runtime/reread_trials/phase1_17_flow_validation/flow_rich_route_selection_seed_004.json)
- [flow_rich_route_selection_seed_024.json](/Users/sungsookim/universe/vectorfl_replica/runtime/reread_trials/phase1_17_flow_validation/flow_rich_route_selection_seed_024.json)

## Trial Modes

- A: `role + seed`
- B: `role + seed + full camera support`
- C: `role + seed + flow support emphasis`

Mode C did not add a new schema. It only consumed the existing `flow_support` slot while leaving change/boundary out of reread narrowing.

## A/B/C Comparison Table

| Artifact | A -> B | A -> C | Flow judgment |
| --- | --- | --- | --- |
| route_selection default | boundary narrowed reread | no change | no clear added value |
| raw intake gap report | boundary narrowed reread | no change | no clear added value |
| builder preprocess | change+boundary narrowed reread | no change | no clear added value |
| codex preprocess | change+boundary narrowed reread | no change | no clear added value |
| compact/title-only | no meaningful gain | no meaningful gain | no clear added value |
| flow-rich seed_004 | flow narrowed reread | flow narrowed reread | independent value |
| flow-rich seed_024 | change+flow narrowed reread | flow narrowed reread | independent value |

## Artifact-by-Artifact Judgment

### 1. route_selection_policy_v0 default

- A: local risk/resistance pressure
- B: local limit / not-yet wording
- C: same practical reread as A
- verdict:
  - `flow no clear added value`

Read:
default local selection in this artifact is not flow-led. The real gain came from boundary.

### 2. raw_intake_gap_analysis_before_middle_layer_fix_v1

- A: local risk/resistance pressure
- B: local limit / not-yet wording
- C: same practical reread as A
- verdict:
  - `flow no clear added value`

Read:
again, boundary did the real narrowing.

### 3. builder_choi_interview preprocess comparison

- A: local correction pressure
- B: local shift + local limit wording
- C: no narrower than A
- verdict:
  - `flow no clear added value`

Read:
preprocess comparison is useful, but currently through change/boundary, not through flow.

### 4. codex_ambassader_jung preprocess comparison

- A: local correction pressure
- B: local shift + local limit wording
- C: no narrower than A
- verdict:
  - `flow no clear added value`

### 5. middle_layer_thickening_program_instruction_v1

- A/B/C: practically the same
- verdict:
  - `flow no clear added value`

Read:
this stayed traceable emptiness, which is the correct bounded outcome.

### 6. flow-rich route_selection local case: line_seed_004

- A: adjacent units with local handoff pressure
- B: local sequence / handoff wording
- C: local sequence / handoff wording
- verdict:
  - `flow independent value`

Read:
this is the clearest positive flow case in the trial. `flow_support = has_signal` was enough to narrow reread by itself.

### 7. flow-rich route_selection local case: line_seed_024

- A: adjacent units with local handoff pressure
- B: local shift + nearby sequence wording
- C: local sequence / handoff wording
- verdict:
  - `flow independent value`

Read:
flow still had standalone reread value even when change was also alive in the full read.

## Compact / Title-Only Observation

Compact/title-only stayed near traceable emptiness.

- camera support did not add bounded reread value
- flow did not wake up
- C did not outperform A

This is the right result. The trial should not force useful flow where the lower artifact does not carry it.

## Carry-Forward Handle Check

### In flow-rich cases

Useful.

Why:

- it kept reread inside the same local unit refs
- it did not widen scope
- it worked as a real bounded pointer for the narrowed flow reread

### In non-flow cases

Mostly formal.

Why:

- the refs were still stable
- but the handle did not add much beyond what A already had

## Why We Are Not Modifying the Emitter Yet

This trial separated two different questions.

1. Is the emitter always bad?
2. Or does flow only matter in narrower local cases?

The result supports the second reading.

Flow is not globally useless. It becomes useful when the local source actually contains sequence / handoff wording. That means a direct emitter change now would be premature. The current uncertainty is not “flow never works,” but “flow works only in narrower source slices than the default selection usually surfaces.”

## Provisional Reading of Flow at This Stage

Current honest reading:

- flow is **not** a broadly reliable reread cue across all lower artifacts
- flow **can** be an independent reread cue in locally flow-rich slices
- outside those slices, flow is currently weak or absent

So the honest temporary position is:

**flow is mixed, with independent value in selected local cases and no clear added value in the broader default set**

