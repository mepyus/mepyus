# line thickening first grounded feed note v0

## Purpose

This note records the first bounded grounded feed into `line_thickening` from an existing read path that already carries a concrete pointer.

The goal is not to widen the surface. The goal is to keep preflight as the summary-echo path while adding one grounded path that can emit `source_linked` or `direct_span` observations honestly.

## Chosen path

The hook is attached to `scripts/apply_internal_observer.py`.

Why this path:

- it already reads real fragments from `FragmentStore`
- it already produces an observer-layer reread of the fragment text
- the fragment records preserve source pointer metadata
- one fragment in the current runtime (`frag_ytex_003`) already has a concrete `source_range`

## Grounding classification

The adapter classifies grounding by the fragment metadata it can actually inspect:

- `summary_echo`
  - reserved for preflight summary-derived observations
- `source_linked`
  - used when the fragment has a source path or page-level reference but no concrete span
- `direct_span`
  - used when the fragment has a concrete source range or paragraph pointer that can be traced back directly

## Grounded feed choice

The verification target was `frag_ytex_003`, because it already carries:

- `source_range.start = 366`
- `source_range.end = 679`
- `paragraph_index = 5`

That makes it a safe first `direct_span` feed without inventing a new pointer system.

## Promotion discipline

The feed is still conservative:

- the registry remains derived state
- the observation log remains the truth archive
- a single direct span does not automatically thicken the line
- recurrence still matters before any medium/thick outcome

## One-line lock

> The first grounded feed should come from an existing read path with a real pointer, and it should stay a bounded sink rather than a new entrypoint.
