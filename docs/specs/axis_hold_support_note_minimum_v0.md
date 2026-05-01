# Axis Hold Support Note Minimum v0

## Verdict

`PASS_WITH_NOTE`

Lower-side can prepare bounded axis hold notes without entering axis promotion.

## Purpose

Axis hold support note records:

- that a direction is visible;
- why it is not yet safe to promote;
- what support is missing;
- what conflict or tension is still active.

## Minimum Candidate Fields

- `related_seed_refs`
- `common_direction_hint`
- `hold_reason`
- `missing_support`
- `conflict_or_tension`
- `promotion_not_allowed_yet`

## Field Meaning

| field | meaning |
| --- | --- |
| `related_seed_refs` | line seed bundles or split refs behind the hold |
| `common_direction_hint` | bounded directional pull, not a promoted axis |
| `hold_reason` | the main reason promotion is blocked |
| `missing_support` | what must be added later |
| `conflict_or_tension` | active contradiction, blur, or counter-pull |
| `promotion_not_allowed_yet` | explicit boundary statement |

## Why Lower Should Leave Hold Notes

If lower-side says nothing, upper-side must repeatedly rediscover the same not-yet-ready directional pull.

If lower-side promotes too early, current camera/axis sensitivity is violated.

The honest middle position is a hold support note: visible direction, explicit non-promotion.

## Boundary

This note must not:

- become an axis;
- become packet-worthiness;
- override bridge minimum;
- imply stable corridor or camera judgment.

## Interpretation

Axis hold support notes let lower-side contribute to future axis reading without trespassing into promotion logic. They are a memory and caution layer, not a semantic upgrade.

## Validation

- Promotion logic remains untouched: `PASS`.
- Hold discipline remains narrow and explicit: `PASS`.
- The note is clearly support-only: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created: `docs/specs/axis_hold_support_note_minimum_v0.md`
3. What was clarified: axis-visible but non-promotable lower note.
4. What remains unresolved: how many seed refs should typically support one hold note.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended first implementation axis: axis hold notes only after line-seed bundling exists.
