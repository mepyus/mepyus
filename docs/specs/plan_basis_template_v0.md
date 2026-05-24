# Plan Basis Template v0

## Status

```yaml
status: template_candidate
baseline_lock: false
automation: false
purpose: pre_plan_space_grounding
```

External tools should not return a plan first. They should return a Plan Basis, then a plan.

Plan Basis is the minimum evidence that a plan came from VectorFL space rather than model-default decomposition.

```markdown
# PLAN_BASIS

## Work Type

[package setup / external tool run / reference program reuse / review recovery / implementation planning / return-to-space / space exploration]

## Current Line

[Long-flow line used for this work.]

## Axis

- [main tension that changes plan shape]

## Camera

- [viewpoint used to judge usefulness and risk]

## Lens

- [criteria used to judge plan sizing, stop/continue, and return]

## Space Assets Consulted

- `[path]`: [why this asset matters]
- `[path]`: [why this asset matters]

## Package Sizing Judgment

Decision:

- [broad-but-bounded package / smaller session split required]

Reason:

- [space-grounded reason]

If smaller session split is required, cite the blocking reason:

- [user decision / unapproved implementation / broad scan / blocking evidence gap / unclear role / no current line / unclear return shape]

## Stop / Continue Rule

Stop for:

- [hard boundary]

Continue with Issue Log for:

- [watch item]

## Return-to-Space Requirement

The result must return:

- [read trace / evidence pointers]
- [issue or watch item]
- [Return-to-Space Value]
- [future reuse note]
```

## Acceptance Check

A plan without Plan Basis should be treated as model-default until checked.

A Plan Basis is valid only if the chosen line / axis / camera / lens changes at least one of:

- package sizing
- stop / continue criteria
- evidence requirement
- user relay burden handling
- return-to-space shape

