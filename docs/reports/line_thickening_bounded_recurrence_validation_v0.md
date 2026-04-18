# line thickening bounded recurrence validation v0

## Verdict

PASS

## Cohort

The same grounded path was used only once, with a small ordered fragment cohort:

- `frag_ytex_001`
- `frag_ytex_001` again
- `frag_ytex_002`
- `frag_ytex_003`
- `frag_basic_003`

This stayed inside `scripts/apply_internal_observer.py` and used the existing grounded fragment reread path only.

## What changed

The script now supports a bounded recurrence mode:

- `--bounded-recurrence-validation`

That mode preserves fragment order and duplicate IDs, so replay can be tested without creating a new entrypoint.

The `line_thickening` evaluator also now exposes recurrence-sensitive signals:

- `same_source_pointer_replay`
- `distinct_source_pointer_repeat`

These signals are carried in promotion decisions, but they do not override conservative gating.

## Verification

The actual run was:

```bash
python3 scripts/apply_internal_observer.py runtime frag_ytex_001 frag_ytex_001 frag_ytex_002 frag_ytex_003 frag_basic_003 --record-line-thickening --bounded-recurrence-validation
```

Observed behavior:

- the second `frag_ytex_001` replay was suppressed as an exact duplicate
- `frag_ytex_002`, `frag_ytex_003`, and `frag_basic_003` each appended grounded observation packets
- the packets carried `evidence_mode=direct_span`
- the promotion log recorded `distinct_source_pointer_repeat` for the recurrence path
- the registry updated only as a derived current-state surface

## Why it stays conservative

The new recurrence signal is intentionally weak:

- it separates replay from recurrence
- it does not auto-promote on same-pointer repetition
- it does not force thickening on a single family or a single run
- it keeps `input_to_reading_organ` at `candidate / thin`

## What remains thin

- exact same fragment replay still contributes nothing new
- distinct fragments in the same family are recognized as recurrence, but not as thickening fuel by themselves
- cross-family recurrence is still not enough for medium or thick without stronger support balance

## Next boundary

The next safe expansion would require a separate grounded path only if it already exists and already carries concrete pointers. No new path should be created just to increase recurrence counts.
