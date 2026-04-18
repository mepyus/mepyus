# Integrated Engine Next Step Checklist Protocol v0

## Purpose

Future work should not be run as tiny scattered edits or as a giant architecture jump. Each next step should be a bounded checklist unit large enough to be meaningful, but small enough to verify and record.

## Checklist Unit Shape

Each checklist unit must include:

1. goal
2. current surface owner
3. files likely touched
4. exact non-goals
5. implementation actions
6. verification actions
7. record file to write
8. pass / pass_with_note / hold verdict

## Required Per-Step Loop

For every checklist item:

```text
read current context
-> implement bounded change
-> verify
-> write short record
-> decide next smallest step
```

## Surface Routing Rule

Every checklist item must say which surface owns the step:

| owner | use when |
| --- | --- |
| User surface | purpose, assignment, team/role setup, user decision, work organization. |
| VectorFL surface | CLI conversation, route sorting, mediation, validation, reread, drift detection. |
| Engine surface | processing request, execution return, extraction/validation/deposit candidate material. |

## Do Not Mix

- Do not put team/role assignment directly into VectorFL just because CLI is involved.
- Do not put detailed reread/validation into User surface.
- Do not let Engine surface decide meaning or promote material.
- Do not create a new route for every internal role.
- Do not build persistence before the operating shape is proven.

## Verification Minimum

Each checklist unit must verify at least one of:

- TypeScript build.
- Python compile.
- API state response.
- UI visible placement.
- runtime artifact creation.
- route/mark/deposit candidate visibility.

## Record Minimum

Each checklist unit must write a short note under `docs/reports` with:

- what changed
- why it changed
- what passed
- what remains held
- next smallest step

