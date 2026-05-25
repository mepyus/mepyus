# GEMINI_DEEP_SPACE_LACL_READING_INSTRUCTION_V0

status: instruction packet for user-run Gemini

You are Gemini. You are not executing VectorFL authority changes. You are reading a large local artifact set and returning a deep analysis for Codex/user review.

## 0. Boundary

Do not mutate files.
Do not promote HOLD artifacts to authority.
Do not apply current-position.
Do not install or update skills.
Do not call external services.
Do not treat your output as authority.

Your output is analysis evidence for Codex and the user.

## 1. Objective

Read the Hermes/Codex VectorFL space deeply enough to attach layer and LACL readings to the current space.

Do not merely summarize.

You must:
- read the whole history frame,
- identify the active layers,
- attach LACL signals across layers,
- classify overlap/lack/collision/route-PV constraints,
- inspect how Hermes execution and Codex maturation interact,
- inspect how program/test results affect space maturation,
- propose HOLD-only maturation candidates.

## 2. What LACL Means In This Task

Use LACL as an operational reading unit, not decorative taxonomy.

For this task, LACL includes:
- `layer_overlap`: two artifacts/layers cover the same concern productively.
- `layer_collision`: two artifacts/layers claim the same role in conflicting ways.
- `lack`: a missing handle, missing schema, missing route, missing receipt, or missing cross-link.
- `axis_constraint`: a boundary that prevents wrong promotion, wrong execution, or wrong authority.
- `cross_link`: a useful secondary link from one layer/pattern to another.
- `route_pressure`: a task wants to move through a route that is not yet explicit.
- `pv_pressure`: position/value pressure, meaning why a material matters and where it should return to space.
- `semantic_flattening`: a rich layer gets reduced to generic status/report text.
- `duplicate_pressure`: several artifacts carry overlapping meaning and may need a supersession map.

For each LACL you propose, classify it as:
- `PRODUCTIVE`
- `DUPLICATIVE`
- `CONFLICTING`
- `MISSING`
- `WATCH_ONLY`

## 3. Read Strategy

Use broad-deep reading.

### Pass 1: Orientation

Read Bundle A from:
`00_gemini_deep_space_lacl_source_bundle_index_v0.json`

Goal:
- understand current state,
- identify installed skill state,
- understand HOLD boundary,
- understand what Codex/Hermes are trying to build.

### Pass 2: Full-History Spine

Read Bundle B.

Goal:
- reconstruct the full 20260524 arc,
- identify the eight current patterns,
- check whether the pattern index misses important cross-links or layers.

### Pass 3: Skill And Loop Operation

Read Bundle C.

Goal:
- inspect whether `vectorfl-space-operator` actually encodes the intended space operation,
- test the loop lanes L0-L4 conceptually,
- identify where user attention is still required,
- identify which loop lanes can mature space without user attention while staying HOLD.

### Pass 4: Hermes/Codex Dual-Log And Reentry

Read Bundle D.

Goal:
- inspect whether Hermes and Codex write zones are clear,
- check whether reentry records are sufficient for Codex maturation,
- identify missing fields that would make Codex guess,
- classify space effect from real-shaped reentry fixtures.

### Pass 5: Phase2/Phase3 Function And Structure Arcs

Read Bundle E.

Goal:
- identify tested function layers,
- find where role handoff, unique delta, overlap classification, and budget gate already exist,
- attach these to the current skill/loop structure,
- identify stale or underused function tests.

### Pass 6: AI Frontier / LACL / External Lens Arcs

Read Bundle F.

Goal:
- inspect EP96/EP97 overlap/lacl work,
- inspect infra-cost/context-economics lens,
- identify whether these should remain external lenses, become pattern-index candidates, or become cross-links under existing patterns,
- classify LACLs created by external material.

### Optional Pass 7: Older LACL Method Memory

Read Bundle G only if useful.

Goal:
- recover older LACL method definitions,
- avoid decorative LACL,
- use older method only as reading support, not authority.

## 4. Required Deep Analysis Tasks

### Task A: Layer Map

Return a layer map with:
- layer_id
- layer_name
- primary artifacts
- owning actor if any: Hermes / Codex / Gemini / User / Shared
- current status: authority / installed skill / HOLD evidence / fixture / proposal / stale
- related patterns from the eight-pattern index
- risk if misread

### Task B: LACL Attachment Table

Return at least 20 LACL candidates.

Each LACL must include:
- lacl_id
- type: layer_overlap / layer_collision / lack / axis_constraint / cross_link / route_pressure / pv_pressure / semantic_flattening / duplicate_pressure
- source artifacts
- connected layers
- connected patterns
- classification: PRODUCTIVE / DUPLICATIVE / CONFLICTING / MISSING / WATCH_ONLY
- why it matters
- proposed HOLD action

### Task C: Route / PV / LACL Matrix

For the following routes, attach PV and LACL signals:
- `CODEX_SPACE_CHECK`
- `CODEX_HERMES_WORK_ANALYSIS`
- `CODEX_SPACE_RETRIEVAL_BY_ORIGINAL`
- `CODEX_SPACE_MATURATION_BY_REENTRY_RECORD`
- `PROGRAM_RESULT_SPACE_EFFECT_INSPECTION`
- `L3_BATCH_PATTERN_MAINTENANCE`
- `L4_GEMINI_AMBIGUITY_EXPLORATION`

For each route:
- what triggers it
- what position/value it protects
- what LACLs it tends to expose
- what output it should write
- when it must stop for user attention

### Task D: Hermes Execution vs Codex Space Operation

Return a clear assessment of whether current artifacts preserve:
- Hermes as execution workbench,
- Codex as space operator,
- Gemini as Codex-side wide lens,
- shared handoff as cross-inspection surface.

Identify any artifacts that blur these roles.

### Task E: Program Result Space-Effect Reading

Inspect the program-result space-effect principle and fixtures.

Return:
- whether this is sufficient to stop local tests from ending at pass/fail,
- where it should attach to Phase2/S1-S7 history,
- whether it creates duplicate artifact pressure,
- what schema or handle is still missing.

### Task F: LACL-Based Maturation Proposal

Produce HOLD-only proposals:
- new cross-links,
- missing handles,
- stale/superseded maps,
- pattern-index refinements,
- loop ledger improvements,
- reentry record field repairs.

Do not propose authority apply.
Do not propose folder moves.
Do not propose current-position apply.

## 5. Return Format

Return Markdown first, then a compact JSON block.

Markdown sections:

1. `Executive Judgment`
2. `Layer Map`
3. `LACL Attachment Table`
4. `Route / PV / LACL Matrix`
5. `Hermes-Codex-Gemini Role Integrity`
6. `Program Result Space-Effect Findings`
7. `HOLD Maturation Proposals`
8. `Stale / Duplicate / Boundary Risks`
9. `What Gemini Could Not Determine`
10. `Next Safe Lane`

Then include this JSON shape:

```json
{
  "packet_id": "GEMINI_DEEP_SPACE_LACL_READING_RETURN_V0",
  "role": "GEMINI_CODEX_SIDE_WIDE_LENS",
  "read_bundles": [],
  "layer_map_count": 0,
  "lacl_candidates_count": 0,
  "strongest_lacl_candidates": [],
  "route_pv_lacl_matrix": [],
  "role_integrity_judgment": "",
  "program_result_space_effect_judgment": "",
  "hold_maturation_proposals": [],
  "missing_handles": [],
  "stale_or_duplicate_pressure": [],
  "boundary_risks": [],
  "codex_should_accept": [],
  "codex_should_reject_or_hold": [],
  "next_safe_lane": "",
  "promotion_status": "HOLD"
}
```

## 6. Quality Bar

Do not be shallow.

Prefer fewer but stronger claims over broad vague summary.

Every major claim should point to one or more artifact paths.

If you infer something, mark it as inference.

If a document bundle is too large to fully read, say exactly which files you read deeply and which files you skimmed.

## 7. Final Boundary Reminder

Your return is not authority.

It should help Codex mature the space by HOLD proposals only.

promotion_status: HOLD
