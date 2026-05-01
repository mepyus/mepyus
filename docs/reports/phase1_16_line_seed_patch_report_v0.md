# Phase 1.16 Line Seed Patch Report v0

## Verdict

`PASS_WITH_NOTE`

Lower-side now emits line seed bundles as a support layer between split output and later upper evidence use.

## Files Created or Updated

- `app/core/runtime/lower_support_layers.py`
- `app/work/observer_ingest_min/run_observer_ingest_min.py`
- `app/core/runtime/external_input_comparison.py`
- `scripts/run_transcript_preprocess_comparison.py`
- `scripts/build_lower_support_layers.py`
- `docs/reports/phase1_16_line_seed_patch_report_v0.md`

## What Was Actually Patched

### Observer Ingest Path

Each observer run now writes:

- `line_seed_bundles_<run_id>.json`

Bundles are assembled from adjacent split units plus role notes. Each bundle leaves:

- `repeated_pressure_note`
- `linkage_hint`
- `question_inducement`
- `misunderstanding_correction`
- `tension_marker`
- `provisional_role_mix`
- `why_line_seed`
- `not_yet_axis_reason`

### Transcript Preprocess Path

Each preprocess comparison now carries:

- `support_layers.line_seed_bundles`

and the comparison runner writes a companion seed file.

## Why This Is Not A Line

The bundle is still:

- source-local;
- support-only;
- non-promotable;
- explicitly blocked by `not_yet_axis_reason`.

It is designed to preserve repeated pressure and correction flow before upper reading hardens the material into evidence or line reasoning.

## What Qualified As Seed Pressure

Current heuristics accept:

- adjacent units with a seed-driver role (`main_claim`, `correction`, `objection`, `connective`, `axis_support_candidate`);
- repeated local tokens across nearby units;
- preprocess comparison chains that repeat regroup/correction/readiness pressure.

## Validation

- Seed bundle is not treated as line promotion: `PASS`.
- `not_yet_axis_reason` remains explicit: `PASS`.
- Seed bundle does not raise readiness automatically: `PASS`.
- Some compact directive material still yields zero seed bundles honestly: `PASS_WITH_NOTE`.

## Thin Areas

- short directive material can stay too sparse for a seed;
- some bundles are token-driven and still shallow;
- transcript bundles are useful but still coarse because they use comparison components rather than deeper regroup blocks.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created/updated: listed above.
3. What was actually patched: lower line-seed support emission.
4. What remains unresolved: richer bundle heuristics for compact or title-heavy sources.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended next move: validate ladder safety and then decide whether camera support is the next bounded patch.
