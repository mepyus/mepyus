# Line Thickening Resistance Semantics Hardening Note v0

## Purpose

This note records the second-stage hardening of `line_thickening`: split resistance semantics so that "not enough yet" evidence no longer inflates contradiction pressure.

## What changed

- `contradiction_points` now carries actual counterevidence.
- `weakness_points` carries "line is still thin" explanations.
- `caution_points` carries "do not promote yet" signals.
- legacy `resistance_or_counterexample` is treated as caution unless it clearly looks like counterevidence.
- registry contradiction counts are no longer inherited from legacy resistance counts.

## Why this matters

If insufficient recurrence is counted as contradiction, a line can stay stuck at `thin` even when direct-span recurrence is accumulating. This hardening keeps the registry honest:

- weakness is not contradiction
- caution is not contradiction
- only actual counterevidence should push contradiction pressure

## Promotion discipline

- `summary_echo` stays weak.
- `source_linked` can support a bounded `medium` path.
- `direct_span` plus recurrence can open `medium` and, if strong enough, `thick`.
- caution and weakness slow promotion without being treated as contradiction.

## Verification takeaway

The grounded recurrence cohort now distinguishes:

- exact replay suppression
- distinct pointer recurrence
- caution accumulation
- contradiction pressure

The result is that `input_to_reading_organ` can grow past thin without fake contradiction inflation, while the overall gate remains conservative.
