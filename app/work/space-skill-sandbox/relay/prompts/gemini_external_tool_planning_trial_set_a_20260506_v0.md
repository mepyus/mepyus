# Gemini External Tool Planning Trial Set A 20260506 v0

## Role

You are testing VectorFL external-tool plan mode.

Your task is to draft a bounded plan for the requested setup continuation, but only after returning `PLAN_BASIS`.

Do not modify files. Do not create automation, runner, writer, registry, schema, baseline, or authority claims.

## Current User Purpose

Continue building the Anchor Stack so future small anchors can transmit effective position values to external tools.

Focus this trial on validating whether `ROUTE_EXTERNAL_TOOL_PLANNING` and the four plan-mode gates produce a space-grounded plan rather than model-default session splitting.

## Required Position IDs

Use these canonical PVs:

```text
PV_PLAN_BASIS_GATE
PV_BROAD_BOUNDED_PACKAGE
PV_NON_INSPECTED_DISCLOSURE
PV_RETURN_TO_SPACE_CLOSEOUT
```

## Required Route

Use:

```text
ROUTE_EXTERNAL_TOOL_PLANNING
```

Do not use `ROUTE_INPUT_CLASSIFICATION` as a separate route unless you explain why it should not merge into this route.

## Read These Assets

- `docs/indexes/anchor_map_position_route_seed_v0.md`
- `docs/indexes/anchor_route_input_evidence_matrix_v0.md`
- `docs/specs/anchor_stack_plan_mode_gate_sequence_v0.md`
- `docs/specs/external_tool_plan_mode_reference_pack_v0.md`
- `docs/specs/anchor_stack_gate_checklist_v0.md`
- `docs/reports/gemini_anchor_map_position_discovery_return_packaging_20260506_v0.md`
- `docs/indexes/plan_from_space_position_map_seed_v0.md`
- `docs/specs/anchor_position_value_layer_setup_v0.md`

If any file is missing, list it under `MISSING`.

## Output Required

### 1. PLAN_BASIS

Return this before any plan:

```yaml
work_type:
current_line:
route:
position_ids:
axis:
camera:
lens:
space_assets_consulted:
package_sizing_judgment:
stop_conditions:
continue_with_issue_log:
return_to_space_requirement:
non_inspected_scope:
```

### 2. BOUNDED PLAN

Return one broad-but-bounded plan.

Do not split into analysis / design / implementation / validation / review sessions by default.

The plan should include internal checks inside one package.

### 3. SELF_CHECK

Answer:

- Did you return Plan Basis before plan?
- Did route/PV selection change package sizing?
- Did you avoid default multi-session decomposition?
- Did you state non-inspected scope?
- Did you avoid authority/baseline/registry claims?
- Does the plan leave Return-to-Space Value?

### 4. RETURN_TO_SPACE

Return:

```yaml
reusable_judgment:
issue_watch:
future_reuse_note:
recommended_review_label:
```

Use one recommended review label:

- `PASS_AS_SPACE_GROUNDED_PLAN`
- `PASS_WITH_WATCH`
- `HOLD_FOR_PLAN_BASIS`
- `HOLD_FOR_BOUNDARY`
- `HOLD_FOR_USER_DECISION`
- `REJECT_MODEL_DEFAULT_PLAN`

## HOLD Conditions

Return `HOLD` instead of plan if:

- you cannot return Plan Basis first
- you need a broad scan
- you need to modify files
- user decision is required
- Return-to-Space Value cannot be stated
- you would need to claim authority or baseline status
