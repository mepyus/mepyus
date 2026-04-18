# line thickening first grounded feed v0

## Verdict

`direct_span` grounded feed established through an existing observer read path.

## What was connected

`scripts/apply_internal_observer.py` now has an opt-in `line_thickening` sink.

The hook runs only when explicitly enabled and only on the fragments that the script already reads.

## Why this path

This path was chosen because it is already an actual reread-like path:

- it reads `FragmentStore`
- it runs the internal observer over fragment text
- it preserves fragment metadata and provenance
- it already owns a concrete fragment pointer surface

The fragment `frag_ytex_003` was the verification target because it carries a real source span:

- `source_range.start = 366`
- `source_range.end = 679`
- `paragraph_index = 5`

## Behavior

The new adapter emits a `RereadObservation` with:

- `source_kind = raw_surface`
- `source_path_or_ref = youtube_exam_excerpt.md`
- `source_run_id_or_event_id = batch_6a088be5400f`
- `source_pointer = runtime/fragments/frag_ytex_003.json#source_range=366-679;paragraph_index=5`
- `evidence_mode = direct_span`

The line chosen for the first grounded feed is `input_to_reading_organ`.

## Verification result

The grounded run produced:

- one new observation packet
- one registry update
- one promotion log entry

The resulting state stayed conservative:

- `status = candidate`
- `thickness_level = thin`

That is the desired behavior for a first grounded feed.

## What remains unchanged

- preflight still emits summary-echo observations
- preflight does not widen into this path
- no new entrypoints were added
- no fuzzy dedupe was introduced

## One-line summary

> The first grounded feed now exists: a real fragment reread path with a direct span pointer can sink into line thickening without changing the default preflight path.
