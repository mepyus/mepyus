# External Tool Plan Prompt Wrapper v0

## Status

```yaml
status: prompt_wrapper_candidate
baseline_lock: false
automation: false
```

Use this wrapper when asking an external tool to draft a package or session plan.

Replace bracketed fields only. Do not expand into full space onboarding.

```markdown
# External Tool Plan Request - Space Anchored

## Current User Purpose

[one to three sentences]

## Required Space Anchors

Read or use these references first:

- `docs/specs/stable_space_operating_anchor_v0.md`
- `docs/indexes/plan_from_space_line_asset_map_v0.md`
- `app/work/SESSION_SPACE_ANCHOR_20260506_PLAN_FROM_SPACE_V0.md`
- `docs/specs/plan_basis_template_v0.md`
- `docs/specs/external_tool_plan_mode_reference_pack_v0.md`

## Current Line / Axis / Camera / Lens

Line:

- Plan from Space / Session Convergence Prevention

Axis:

- model-default planning vs space-grounded planning
- small session split vs broad-but-bounded package

Camera:

- user relay burden
- program continuity
- space recovery

Lens:

- Plan Basis present / absent
- package sizing
- hard boundary / watch / continue
- Return-to-Space Value
- non-inspected evidence disclosure

## Route / Position Gate

Use route:

```text
ROUTE_EXTERNAL_TOOL_PLANNING
```

Use canonical Position IDs:

```text
PV_PLAN_BASIS_GATE
PV_BROAD_BOUNDED_PACKAGE
PV_NON_INSPECTED_DISCLOSURE
PV_RETURN_TO_SPACE_CLOSEOUT
```

Consult:

- `docs/indexes/anchor_map_position_route_seed_v0.md`
- `docs/specs/anchor_stack_plan_mode_gate_sequence_v0.md`

Do not use shortened PV aliases in final output.

## Instructions

Do not start with a plan.

Return `PLAN_BASIS` first. Then return the plan.

Default to a broad-but-bounded package. Do not split into separate analysis / design / execution / verification / review sessions unless you state a blocking reason.

Do not create automation, writer, runner, controller, registry, baseline, or readiness declarations.

Treat your logs, memory, and session state as raw trace only.

## Required Output

```text
PLAN_BASIS
PLAN
SELF_CHECK
RETURN_TO_SPACE
```

`PLAN_BASIS` must include:

- route
- canonical position IDs
- package sizing judgment
- non-inspected scope
- Return-to-Space requirement

## Stop Conditions

Return HOLD if:

- broad scan is required
- unapproved file modification is required
- current line cannot be selected
- user decision is required
- Return-to-Space Value cannot be stated
- the request would make you final authority

## Return-to-Space Must Include

- read trace / evidence pointers
- non-inspected scope if applicable
- issue or watch item
- reusable judgment
- future reuse note
```

## Review

After receiving the worker output, review it with:

- `docs/specs/anchor_stack_gate_checklist_v0.md`
- `docs/specs/external_tool_plan_return_review_template_v0.md`
