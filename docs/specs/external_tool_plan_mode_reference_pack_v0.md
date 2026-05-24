# External Tool Plan Mode Reference Pack v0

## Status

```yaml
status: reference_pack_candidate
baseline_lock: false
automation: false
target: external_tool_plan_mode
```

Use this pack when asking Codex, Gemini, Hermes, OmX, or another worker to draft a package/session plan.

Do not send the whole space. Send this compact pack plus specific source pointers.

## Required Inputs

### 1. Current User Purpose

One to three sentences.

Do not paste the full conversation.

### 2. Stable Anchor

Reference:

- `docs/specs/stable_space_operating_anchor_v0.md`

Worker must preserve:

- external tools are movement organs, not source of truth
- external tool logs/memory are raw trace
- Return-to-Space Value is required for memory promotion
- broad scans are hard boundary unless explicitly approved

### 3. Current Line Asset Map

Default for this setup:

- `docs/indexes/plan_from_space_line_asset_map_v0.md`

Worker must state:

- current line
- why this line applies
- which related assets were used
- how the line changed package sizing or stop/continue judgment

### 4. Session Space Anchor

Reference template:

- `docs/specs/session_space_anchor_template_v0.md`

Current active anchor:

- `app/work/SESSION_SPACE_ANCHOR_20260506_PLAN_FROM_SPACE_V0.md`

Worker should re-read the active anchor before:

- plan generation
- session splitting
- final/ready language
- closeout

### 5. Plan Basis

Reference:

- `docs/specs/plan_basis_template_v0.md`

Worker must return Plan Basis before the plan.

A plan without Plan Basis is treated as model-default until checked.

Plan Basis should include:

- selected route
- canonical Position IDs
- package sizing judgment
- non-inspected scope

### 6. Return Contract

Reference:

- `docs/specs/movement_record_template_v0.md`

Worker result must include:

- read trace / evidence pointers
- issue or watch item
- Return-to-Space Value
- future reuse note

### 7. Route / Gate References

Use:

- `docs/indexes/anchor_map_position_route_seed_v0.md`
- `docs/specs/anchor_stack_plan_mode_gate_sequence_v0.md`
- `docs/indexes/plan_from_space_position_map_seed_v0.md`

Default route:

```text
ROUTE_EXTERNAL_TOOL_PLANNING
```

Default Position IDs:

```text
PV_PLAN_BASIS_GATE
PV_BROAD_BOUNDED_PACKAGE
PV_NON_INSPECTED_DISCLOSURE
PV_RETURN_TO_SPACE_CLOSEOUT
```

## Package Sizing Default

Default:

```text
broad-but-bounded package
```

Do not split into analysis / design / execution / verification / review sessions by default.

Small split requires a blocking reason:

- user decision changes direction
- unapproved implementation or file modification would be needed
- broad scan is required
- evidence gap is blocking
- tool role is unclear
- current line cannot be selected
- return shape is unclear

## Output Shape

```markdown
# PLAN_BASIS

[fill Plan Basis first]

# PLAN

[bounded package plan]

# SELF_CHECK

- Did the line change package sizing?
- Did route/PV selection appear before the plan?
- Did the result distinguish hard boundary from watch item?
- Did the result avoid user relay burden?
- Did the result include Return-to-Space Value?
- Did the result avoid baseline/automation claims?

# RETURN_TO_SPACE

- reusable judgment:
- issue/watch:
- future reuse note:
```

## Stop Conditions

Stop and return HOLD if:

- requested plan needs broad scan
- requested plan needs unapproved file modification
- worker cannot identify current line
- worker would need to declare readiness/baseline
- worker cannot produce Return-to-Space Value
- worker is being asked to become final authority
