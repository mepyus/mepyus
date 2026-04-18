# Capability-Aware Internal Search Minimum Slice v0

## What Changed

A minimum internal search slice was added for the operating screen.

It now returns two result types in one query flow:

- `reading_result`
- `capability_result`

The slice is read-only over existing runtime assets and capability registry state.

## Bounded Validation

Validation used three bounded queries:

- `input observer`
- `sandbox trip`
- `validation`

### Reading side

`input observer` returns pointer-bearing `input_to_reading_organ` reading candidates with:

- direct-span evidence
- source pointer
- surrounding context
- current validation profile / primary-only profile / ecology bias / next missing axis

The result set also exposes that current official reading still says:

- `next_missing_axis=path`
- `distinct_path_count=1`

So the panel is useful for path-diversity inspection, but it does not prove that path diversity has materially opened.

### Capability side

Alias-based lookup works against the capability registry:

- `sandbox trip` -> sandbox probe capability
- `validation` -> validation chain capability
- `input observer` -> grounded feed capability also appears with reading candidates

Capability results show:

- `capability_type`
- `entrypoint`
- `runtime_scope`
- `output_surfaces`
- `linked_scripts`
- `safety_note`

## Operating Panel Read

The panel now lets the operator see:

1. whether the match is a reading target or a capability
2. why it was selected
3. where the reading points, or what the capability calls
4. which safety range applies
5. what next entry is available

## Current Limits

- Reading search is still a bounded log/registry scan.
- Capability lookup is still registry read, not capability execution planning.
- `input_to_reading_organ` results expose multiple primary anchors, but current registry state still reads as path-narrow.
- The panel helps inspect the bottleneck; it does not remove it.

## Next Step

If this slice is reopened, the next bounded step should be to normalize observation-level `path_origin` labels for `input_to_reading_organ` so the panel can separate true path diversity from legacy `raw_surface` carryover more cleanly.
