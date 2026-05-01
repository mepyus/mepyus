# Lower Content Role Tagging Minimum v0

## Verdict

`PASS_WITH_NOTE`

Lower-side needs a narrow content-role layer so provenance-bearing units can carry function before they meet upper interpretation.

## Purpose

Content-role tagging answers:

```text
what is this chunk doing in the source?
```

It does not answer:

```text
what axis should be promoted?
what camera is final?
what upper packet should be emitted?
```

## Minimum Role Set

- `definition`
- `background`
- `main_claim`
- `transition`
- `correction`
- `objection`
- `example`
- `exception`
- `connective`
- `axis_support_candidate`

## Why These Roles

This set is deliberately narrow:

- enough to separate explanatory vs directional work;
- enough to surface correction/objection pressure;
- enough to mark a chunk that looks axis-relevant without promoting it.

## Tagging Rules

- assign one primary role when possible;
- allow provisional mix when two functions coexist;
- keep role honest and local to the chunk;
- if role is unclear, leave a note rather than over-claim.

Suggested fields for a future additive layer:

- `source_ref`
- `split_unit_ref`
- `content_role`
- `secondary_role`
- `role_confidence`
- `role_basis_note`
- `why_this_role`

## Why Provenance Is Not Enough

Provenance tells us where the material came from. It does not tell us whether a chunk defines, objects, corrects, or bridges two pressure points.

Upper line/axis/camera reading is forced to do too much if every lower chunk arrives only with origin and excerpt.

## Why Lower-Side Role Helps Upper

If lower chunks carry role early:

- upper can distinguish connective material from claim material faster;
- correction and objection signals can seed hold/support earlier;
- camera support can later ask for the right context span instead of generic expansion;
- line seed bundle assembly becomes less arbitrary.

## Boundaries

This is not:

- a final taxonomy lock;
- a promotion taxonomy;
- a replacement for grounded evidence relation types;
- a reason to change readiness.

## Interpretation

The lower organ already knows source identity well. It now needs a minimal sense of function. That function should remain revisable and narrow, but it should exist before the upper side has to infer it from scratch every time.

## Validation

- The taxonomy is narrow and usable: `PASS`.
- It is additive and revisable: `PASS`.
- It does not change readiness or promotion: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created: `docs/specs/lower_content_role_tagging_minimum_v0.md`
3. What was clarified: narrow lower-side content-role layer.
4. What remains unresolved: exact confidence labels and mixed-role handling.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended first implementation axis: role tagging over current observer/preprocess outputs.
