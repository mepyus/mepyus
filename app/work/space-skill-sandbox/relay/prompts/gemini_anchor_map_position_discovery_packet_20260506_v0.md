# Gemini Anchor Map Position Discovery Packet 20260506 v0

## Role

You are doing bounded space exploration for VectorFL.

Your task is to discover where the anchor map should attach position values for future small anchors.

Do not summarize the whole space. Do not promote anything to baseline, registry, ontology, schema, workflow, or automation.

## Core Question

When a future session needs a small anchor, what route should determine the 2-4 Position Values it carries?

We need evidence-backed route positions, not more general principles.

## Required First Step

Return a short `PLAN_BASIS` before the report:

```yaml
line:
axis:
camera:
lens:
space_assets_you_will_read:
bounded_scope:
do_not_infer:
```

## Read Bundle A - Current Route And Position Setup

Read these first:

- `docs/indexes/anchor_map_position_route_seed_v0.md`
- `docs/indexes/anchor_route_input_evidence_matrix_v0.md`
- `docs/specs/anchor_stack_plan_mode_gate_sequence_v0.md`
- `docs/indexes/plan_from_space_position_map_seed_v0.md`
- `docs/specs/anchor_position_value_layer_setup_v0.md`
- `docs/specs/small_anchor_generation_rule_v0.md`
- `docs/indexes/lacl_candidate_synthesis_matrix_seed_v0.md`
- `GEMINI.md`

## Read Bundle B - LACL And Gemini Packaging

Read these:

- `docs/reports/lacl_regrounding_deep_exploration_result_20260506_v0.md`
- `docs/reports/lacl_regrounding_gemini_persisted_assets_packaging_20260506_v0.md`
- `docs/reports/lacl_regrounding_persistence_downshift_correction_20260506_v0.md`
- `docs/reports/position_value_discovery_gemini_return_packaging_v0.md`
- `docs/reports/may6_nine_doc_anchor_stack_alignment_review_v0.md`

## Read Bundle C - Evidence Records

Read enough of these to test whether the route rows are grounded:

- `app/work/SESSION_43_RESULTS_V0.md`
- `app/work/SESSION_44_RESULTS_V0.md`
- `app/work/SESSION_46_RESULTS_V0.md`
- `app/work/SESSION_47_RESULTS_V0.md`
- `app/work/PROGRAM_FRAME_EXTERNAL_PATTERN_MAP_V0.md`
- `docs/specs/line_maturity_and_operating_anchor_direction_lock_v0.md`
- `docs/reports/space_feedback_loop_return_to_space_record_minimum_v0.md`
- `docs/specs/manual_external_tool_relay_bridge_note_v0.md`

## Optional Bundle D - May 6 Nine Foundational Docs

If available, read the nine May 6 documents again and use them as source evidence:

- `05-06/1.md`
- `05-06/2.md`
- `05-06/3.md`
- `05-06/4.md`
- `05-06/5.md`
- `05-06/6.md`
- `05-06/7.md`
- `05-06/8.md`
- `05-06/9.md`

Local source paths if available:

- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/1.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/2.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/3.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/4.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/5.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/6.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/7.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/8.md`
- `/Users/sungsookim/Library/Mobile Documents/iCloud~md~obsidian/Documents/시냄스/codex_/05-06/9.md`

If unavailable, mark:

```text
SOURCE_MISSING: MAY6_NINE_DOCS
```

## Output Required

### 1. Read Trace

List files read, missing, not inspected, and lightly inspected.

### 2. Route Validation

For each current route in `anchor_map_position_route_seed_v0.md`, return:

```yaml
route_id:
keep_revise_hold:
evidence_pointers:
what_task_behavior_it_changes:
best_position_ids:
position_ids_to_remove:
missing_evidence:
watch:
do_not_infer:
```

Pay special attention to whether `ROUTE_INPUT_CLASSIFICATION` is a real route or should merge with `ROUTE_SESSION_REENTRY` / `ROUTE_EXTERNAL_TOOL_PLANNING`.

### 3. New Route Candidates

Propose a new route only if it changes task behavior beyond existing routes.

```yaml
route_id:
use_when:
position_ids:
map_slot:
evidence_pointers:
wrong_completion_prevented:
return_shape:
maturity_state: candidate | hold
watch:
do_not_infer:
```

### 4. Route Merge Candidates

Identify routes that should merge because they trigger the same PV set or prevent the same wrong completion.

### 5. Missing Map Slots

Identify map slots not covered by the current seed, but only when backed by evidence.

Examples:

- package source ambiguity
- older active/residue sampling
- current-position recovery
- external role boundary
- user decision boundary

### 5A. Gate Sequence Validation

Validate the four-gate sequence in `anchor_stack_plan_mode_gate_sequence_v0.md`:

```yaml
gate:
keep_revise_hold:
evidence_pointers:
best_route_links:
best_position_ids:
missing_evidence:
watch:
```

### 6. Small Anchor Recommendations

Return 3-5 recommended small anchor sets with 2-4 canonical PV IDs each.

Each set must state:

```yaml
anchor_use:
position_ids:
required_gate:
watch:
do_not_infer:
return_shape:
```

### 7. HOLD / Do Not Promote

List what must remain candidate or HOLD.

### 8. Return-to-Space Value

Return:

- reusable findings
- route rows Codex should revise
- route rows Codex should hold
- any canonical PV updates needed
- next bounded read candidate

## Constraints

- Use canonical PV IDs from `plan_from_space_position_map_seed_v0.md`.
- Treat aliases in worker files as aliases only.
- State non-inspected scope.
- Do not write files.
- Do not claim full-space coverage.
- Do not propose implementation or automation.
