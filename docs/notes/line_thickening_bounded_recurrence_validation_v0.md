# line thickening bounded recurrence validation note v0

## Purpose

This note records the bounded recurrence check on the already-connected grounded path only:
`scripts/apply_internal_observer.py`.

The goal is not expansion. The goal is to verify that:

- exact same fragment replay does not over-promote
- distinct fragments in the same source family are treated as recurrence, not as replay
- a grounded feed from another family can still stay conservative
- the registry remains a derived current-state surface while logs remain the truth archive

## Cohort

The bounded cohort was processed in this order:

1. `frag_ytex_001`
2. `frag_ytex_001` again
3. `frag_ytex_002`
4. `frag_ytex_003`
5. `frag_basic_003`

This cohort stays within the same grounded path and uses only concrete fragment pointers already present in runtime.

## Replay vs recurrence

- Exact same fragment replay:
  - the second `frag_ytex_001` append was detected as an exact duplicate
  - no new observation row was appended
  - no promotion was triggered

- Distinct fragment recurrence:
  - `frag_ytex_002`, `frag_ytex_003`, and `frag_basic_003` all appended as distinct direct-span observations
  - the promotion log now carries `distinct_source_pointer_repeat`
  - the line registry accumulates the new support while remaining conservative

## Grounding discipline

The new recurrence guard stays thin:

- `summary_echo` remains a non-thickening path
- `direct_span` observations can contribute to recurrence
- repeated source pointers are not treated as new evidence
- exact duplicate replay is still suppressed at append time

## One-line lock

> The same grounded path can validate recurrence only if replay and distinct pointer recurrence remain visibly different, and neither is allowed to force thickening by itself.
