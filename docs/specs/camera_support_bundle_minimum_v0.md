# Camera Support Bundle Minimum v0

## Verdict

`PASS_WITH_NOTE`

Lower-side can prepare camera-readable support without performing camera promotion or final lens selection.

## Purpose

Camera support bundle says:

- which reading frame seems compatible;
- what context span is required;
- which weak frames should be avoided;
- when rollback is safer than over-reading.

It does not say:

- final camera chosen;
- camera taxonomy locked;
- promotion allowed.

## Minimum Candidate Fields

- `source_ref`
- `compatible_camera_hint`
- `required_context_span`
- `weak_frames`
- `rollback_condition`
- `reading_risk_note`
- `why_camera_supported`

## Field Meaning

| field | meaning |
| --- | --- |
| `source_ref` | source or source family behind the note |
| `compatible_camera_hint` | a provisional reading frame that seems to fit |
| `required_context_span` | how much adjacent material is needed |
| `weak_frames` | frames likely to distort the read |
| `rollback_condition` | when to back off from the hinted camera |
| `reading_risk_note` | ambiguity or overfit risk |
| `why_camera_supported` | bounded reason this frame is at least provisionally workable |

## Why Lower Should Prepare This

Lower-side already knows:

- split order;
- source family;
- local correction/tension;
- preprocess and route signals.

That is enough to prepare support notes for later camera reading, even if final camera/lens judgment remains upper-side and promotion-sensitive.

## Boundary

Do not use this bundle to:

- choose a final camera;
- override hold discipline;
- promote line or axis;
- imply packet-worthiness.

## Interpretation

Camera support is preparation, not decision. It gives the future camera/lens reader a better footing by naming context span and rollback conditions before the reading becomes overconfident.

## Validation

- Current camera sensitivity is respected: `PASS`.
- Promotion logic is untouched: `PASS`.
- The bundle remains support-only: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created: `docs/specs/camera_support_bundle_minimum_v0.md`
3. What was clarified: lower-side camera support as a bounded support layer.
4. What remains unresolved: provisional camera hint vocabulary.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended first implementation axis: add support notes only after role/seed layer exists.
