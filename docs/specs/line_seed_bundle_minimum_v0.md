# Line Seed Bundle Minimum v0

## Verdict

`PASS_WITH_NOTE`

The lower organ needs a middle layer between split output and evidence-ready use. That layer is a line seed bundle: not a line, not a packet, and not a promotion step.

## Purpose

Line seed bundle exists to hold accumulating pressure before upper line interpretation hardens it.

It should answer:

- why these split units belong together;
- what pressure or correction repeats;
- what question is being induced;
- why the material is promising but still not axis-ready.

## Minimum Candidate Fields

- `source_ref`
- `split_unit_refs`
- `repeated_pressure_note`
- `linkage_hint`
- `question_inducement`
- `misunderstanding_correction`
- `tension_marker`
- `provisional_role_mix`
- `why_line_seed`
- `not_yet_axis_reason`

## Field Meaning

| field | meaning |
| --- | --- |
| `source_ref` | common source or bounded source family |
| `split_unit_refs` | the units being bundled |
| `repeated_pressure_note` | what keeps returning or pushing the same direction |
| `linkage_hint` | why these units are read together |
| `question_inducement` | what follow-up reading they provoke |
| `misunderstanding_correction` | whether the bundle carries a correction move |
| `tension_marker` | contradiction, drag, or unresolved stress |
| `provisional_role_mix` | rough role pattern across units |
| `why_line_seed` | why this is promising for future line reading |
| `not_yet_axis_reason` | why it must not be promoted yet |

## Boundaries

Line seed bundle is:

- below line;
- below axis;
- below upper packet;
- above raw split unit.

It is a support layer, not a readiness level.

## Why Split -> Evidence Makes Things Hard

When split output goes directly into evidence-ready use:

- repeated pressure is lost across adjacent units;
- correction flow is left implicit;
- tension stays scattered;
- upper must rebuild thematic pull manually.

A line seed bundle softens this jump by carrying a bounded, honest grouping before promotion-sensitive work begins.

## Relationship To Existing Lanes

- compatible with grounded evidence because it still points to split refs;
- compatible with bridge minimum because it does not change admission;
- compatible with hold discipline because `not_yet_axis_reason` stays explicit;
- compatible with content-role because role mix can be computed from tagged units.

## Interpretation

Line seed is a pre-line formation. It says “something directional is forming here” without pretending that the direction is final, general, or promotable.

That is exactly the missing middle layer between safe split output and brittle upper line reading.

## Validation

- Existing evidence lane is not replaced: `PASS`.
- Promotion boundary remains explicit: `PASS`.
- The object is narrow enough to prototype later: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created: `docs/specs/line_seed_bundle_minimum_v0.md`
3. What was clarified: line seed as a middle support layer.
4. What remains unresolved: exact bundle assembly heuristic.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended first implementation axis: generate line-seed bundles from adjacent split units plus role notes.
