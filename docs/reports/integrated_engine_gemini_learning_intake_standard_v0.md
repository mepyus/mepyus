# Integrated Engine Gemini Learning Intake Standard v0

Date: 2026-04-15

## 0. purpose

This document defines how Gemini should learn the current integrated-engine material before being used for analysis, review, design translation, or implementation support.

This is not model fine-tuning.

Read "learning" here as:

- session intake
- rereading the current space material
- summarizing the current baseline before acting
- respecting source priority and hold boundaries

Do not read this as:

- permanent Gemini training
- new schema
- new runtime binding
- new authority layer
- automatic worker launch rule
- permission to promote extensions

## 1. one-line rule

Before Gemini is used, it must first read the current baseline bundle, state what it learned, identify the active task boundary, and confirm what it will not promote or change.

## 2. authority order

Gemini must read documents with this precedence:

| priority | source class | how to treat it |
|---|---|---|
| 0 | the user's current task instruction | active task boundary |
| 1 | current working baseline docs | highest project reference for integrated-engine structure |
| 2 | latest closeout / use-observation docs | current state of what has passed, what is thin, and what is held |
| 3 | current scaffold / manifest samples | evidence for what is actually referenced |
| 4 | visual briefs / patch notes / audit notes | support context for why the current surface looks this way |
| 5 | older lineage / mock / external comparison docs | derivation material only, never current authority by default |

If sources disagree:

- current user task wins for scope
- v1 candidate baseline wins for structure
- latest closeout wins for current status
- older lineage stays as background unless explicitly relocked

## 3. baseline intake minimum

For any integrated-engine task, Gemini should first read:

1. `vectorfl_status.md`
2. `docs/reports/vectorfl_integrated_engine_asset_index_v0.md`
3. `docs/reports/integrated_engine_working_lexicon_v1_candidate.md`
4. `docs/reports/integrated_engine_working_protocol_v1_candidate.md`
5. `docs/reports/integrated_engine_working_interface_v1_candidate.md`

If the task concerns current scaffold use, Gemini should also read:

6. `docs/reports/integrated_engine_visual_patch_round3_closeout_note_v0.md`
7. `docs/reports/integrated_engine_render_contract_round4_closeout_note_v0.md`
8. `docs/reports/integrated_engine_render_field_round5_closeout_note_v0.md`
9. `docs/reports/integrated_engine_round6_boundary_closeout_note_v0.md`
10. `docs/reports/integrated_engine_manual_use_round_closeout_note_v0.md`

If the task concerns future expansion, Gemini should also read:

11. `docs/reports/integrated_engine_expansion_carry_forward_map_v0.md`
12. `docs/reports/integrated_engine_expansion_carry_forward_delta_round2_v0.md`
13. `docs/reports/integrated_engine_promotion_gate_criteria_v0.md`

## 4. task-specific intake sets

### documentation / baseline reading task

Read:

- baseline intake minimum
- latest relevant closeout note
- current task instruction

Gemini output before acting:

- current baseline summary
- relevant hold boundaries
- likely safe output type

### scaffold / visual review task

Read:

- baseline intake minimum
- three current scaffold files:
  - `runtime/views/user_surface_scaffold_v0.tsx`
  - `runtime/views/vectorfl_surface_scaffold_v0.tsx`
  - `runtime/views/engine_surface_scaffold_v0.tsx`
- visual translation or patch notes relevant to the surface
- Round 3 / 4 / 5 / 6 closeouts

Gemini output before acting:

- central panel gravity check
- read-map preservation check
- support-layer risk check
- visual-only vs semantic-change distinction

### mock / design asset translation task

Read:

- baseline intake minimum
- `docs/reports/gemini_mock_test_structural_analysis_v0.md`
- relevant visual translation brief
- consolidation note
- promotion gate criteria

Gemini output before acting:

- what can be translated
- what must stay discarded or held
- which surface is affected
- why the mock must not be adopted as-is

### implementation-support task

Read:

- baseline intake minimum
- task-specific scaffold files
- latest closeout notes
- promotion gate criteria

Gemini output before acting:

- whether implementation is allowed by the current task
- which files are in scope
- which files are explicitly out of scope
- whether the task is core refinement, wording-only, documentation-only, or extension-gated

## 5. required Gemini pre-action digest

Before giving advice or writing a patch, Gemini should produce a short digest with this shape:

```text
Gemini intake digest:

1. Current baseline:
   - user surface =
   - VectorFL surface =
   - engine surface =
   - central panels =

2. Documents read:
   - ...

3. Active task boundary:
   - documentation-only / read-only / wording-only / visual patch / implementation

4. Must not cross:
   - read-map change?
   - manifest shape change?
   - runtime binding?
   - selected-object behavior?
   - trace UI?
   - extension promotion?

5. Likely safe action:
   - ...

6. Uncertainty or missing source:
   - ...
```

If Gemini cannot produce this digest, it should not proceed.

## 6. what Gemini should learn from the material

Gemini should extract:

- three-surface roles
- central panel gravity
- request / return / reflux separation
- anchor / maturation / operating object separation
- current loop state as current-position state, not full history
- panel connection records as support trace, not live event feed
- current PASS / PASS_WITH_NOTE status
- which items are core now
- which items are extension later
- which items need promotion gate
- wording confusion candidates vs structural gaps

Gemini should not convert these into:

- final enum set
- DB schema
- automatic router
- component props
- runtime data model
- live manifest truth
- team assignment authority
- governance console

## 7. hard guardrails

Gemini must not:

- treat old mock design as current UI authority
- replace current working baseline with older lineage language
- make user surface a team board
- make VectorFL surface a line browser or workflow hub
- make engine surface a control room or final judgment surface
- promote selected-object behavior without a display-state contract
- add trace UI without trace inclusion and density rules
- treat connection records as live event feed
- treat empty state as runtime failure
- introduce watcher / supervisor / bridge authority
- use external search unless explicitly requested
- propose implementation when the task is documentation-only or read-only

## 8. source freshness rule

Gemini should treat the current integrated-engine baseline as:

- current working baseline
- current PASS / PASS_WITH_NOTE baseline
- not final lock

Freshness reading:

- v1 candidate docs establish current language and protocol
- closeout notes establish current use status
- scaffold files establish current visible panel/read-map evidence
- sample manifests establish low-intensity scenario evidence
- older v0 / lineage reports explain derivation only

When unsure, Gemini should say:

- "This looks like lineage/support material, not current baseline authority."

## 9. output discipline

Gemini output should be structured as one of:

- reading digest
- use observation
- drift/confusion list
- visual translation note
- bounded patch review
- promotion-gate evaluation
- implementation support note

Gemini should avoid:

- broad redesign
- "new architecture" proposals
- changing multiple surfaces when one is requested
- mixing current baseline with future extension
- hiding uncertainty

## 10. reusable Gemini prompt

Use this prompt before giving Gemini a task:

```text
Before answering, read this as an integrated-engine Gemini intake task.

First learn the current baseline from:
1. vectorfl_status.md
2. docs/reports/vectorfl_integrated_engine_asset_index_v0.md
3. docs/reports/integrated_engine_working_lexicon_v1_candidate.md
4. docs/reports/integrated_engine_working_protocol_v1_candidate.md
5. docs/reports/integrated_engine_working_interface_v1_candidate.md

Then read any task-specific docs I provide.

Produce a Gemini intake digest before doing the task:
- current baseline
- documents read
- active task boundary
- must-not-cross boundaries
- likely safe action
- uncertainty or missing source

Do not promote extensions.
Do not add runtime binding.
Do not change read maps unless explicitly asked.
Do not treat mock or lineage docs as current authority.
Do not implement if the task is documentation-only or read-only.
```

## 11. current recommended use

For the next Gemini use, the safest mode is:

- baseline intake first
- then task-specific read
- then digest
- then bounded output

Default mode:

- read / summarize / compare / observe

Escalate to implementation only when:

- the user explicitly asks for implementation
- target files are named
- current baseline documents do not forbid the change
- promotion gate is not required, or has already passed

## 12. closeout sentence

Gemini should enter the project through the space, not through a fresh design impulse: read the current baseline, learn the held boundaries, state the safe task mode, and only then assist.
