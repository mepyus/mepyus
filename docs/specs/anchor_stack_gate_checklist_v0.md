# Anchor Stack Gate Checklist v0

## Status

```yaml
status: checklist_candidate
baseline_lock: false
automation: false
```

This is a manual checklist for reviewing whether a worker plan passed through the Anchor Stack.

## 1. Pre-Plan Gate

Pass only if the worker states:

- current user purpose
- current work type
- selected route
- canonical Position IDs
- current line
- at least one axis
- at least one camera
- at least one lens
- space assets consulted

Fail / hold if:

- plan appears before Plan Basis
- worker says only "VectorFL 기준 반영" without concrete assets
- worker uses shortened PV aliases without canonical normalization
- worker asks to read the whole space

## 2. Plan Sizing Gate

Pass only if the worker states:

- broad-but-bounded package or smaller split
- reason for the sizing
- blocking reason if smaller split is chosen
- route/PV selection changed or justified the sizing

Fail / hold if:

- analysis / design / execution / verification / review sessions appear by default
- validation is separated into a new session without justification
- closeout is proposed as a separate session without Return-to-Space reason

## 3. Boundary Gate

Pass only if the worker separates:

- hard boundary
- watch item
- continue-with-issue-log item
- user decision point

Hard stop examples:

- broad scan
- unapproved implementation
- baseline/readiness declaration
- automation/writer/runner/controller creation
- external memory/log treated as VectorFL memory

Continue-with-issue-log examples:

- weak evidence pointer
- wording drift
- candidate-level instability
- non-blocking structure gap

## 4. Runtime Re-Entry Gate

Pass only if the worker promises to re-check the active Session Space Anchor before:

- splitting tasks
- final/ready language
- closeout
- user relay request

Hold if the plan would make the user copy/paste between tools without a space packet.

Pass with watch if manual relay is temporary and the worker names `PV_MANUAL_RELAY_BRIDGE` or an equivalent packaged-return route.

## 5. Return-to-Space Gate

Pass only if closeout includes:

- read trace / evidence pointer
- issue or watch item
- Return-to-Space Value
- future reuse note
- recommended next route or PV set

Fail / hold if:

- closeout says only "done"
- no reusable judgment remains
- the worker's raw trace is treated as memory
- worker claims authority, baseline, registry, schema, or final map status

## 6. Review Result Labels

Use these labels:

- `PASS_AS_SPACE_GROUNDED_PLAN`
- `PASS_WITH_WATCH`
- `HOLD_FOR_PLAN_BASIS`
- `HOLD_FOR_BOUNDARY`
- `HOLD_FOR_USER_DECISION`
- `REJECT_MODEL_DEFAULT_PLAN`
