# PLAN_MODE_REFERENCE_PACK_20260506_PLAN_FROM_SPACE_V0

## Status

```yaml
status: active_reference_pack
date: 2026-05-06
baseline_lock: false
automation: false
```

## Current User Purpose

Set up external-tool planning so package/session plans start from VectorFL space records and Anchor Stack checks rather than model-default decomposition.

## Read First

- `docs/specs/stable_space_operating_anchor_v0.md`
- `docs/indexes/plan_from_space_line_asset_map_v0.md`
- `app/work/SESSION_SPACE_ANCHOR_20260506_PLAN_FROM_SPACE_V0.md`
- `docs/specs/plan_basis_template_v0.md`
- `docs/specs/anchor_stack_gate_checklist_v0.md`

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

## Package Sizing Instruction

Default to one broad-but-bounded package.

Do not split into separate analysis / design / execution / verification / review sessions unless a blocking reason is stated.

## Worker Required Output

```text
PLAN_BASIS
PLAN
SELF_CHECK
RETURN_TO_SPACE
```

## Stop Conditions

- broad scan required
- unapproved file modification required
- baseline/readiness declaration pressure
- automation/writer/runner/controller creation pressure
- external tool memory/log treated as VectorFL memory
- no Return-to-Space Value can be stated

