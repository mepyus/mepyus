# line thickening grounding hardening v0

## Purpose

This note hardens the existing preflight-connected `line_thickening` slice so it does not turn summary echo into thickening fuel.

The preflight hook already emits line-centered observations.
This note adds grounding discipline so those observations carry explicit provenance-like anchors and conservative promotion gates.

## Grounding modes

The observation packet distinguishes three levels of grounding quality:

- `summary_echo`
  - the packet is derived from a preflight decision or phase summary rather than a source span
- `source_linked`
  - the packet has a concrete pointer into a trace/state/log source, even if it is still indirect
- `direct_span`
  - the packet points to a direct source span or row-like anchor that can be traced back without inference

## Anchor fields

The minimum anchor shape records:

- `source_kind`
- `source_path_or_ref`
- `source_run_id_or_event_id`
- `source_pointer`
- `evidence_mode`

These fields make it explicit whether an observation came from a summary echo or from a source-linked/direct trace.

## Promotion hardening

The promotion evaluator is conservative by design:

- `summary_echo` only observations stay at `candidate / thin`
- `medium` requires at least one `source_linked` or `direct_span` observation
- `thick` requires at least one `direct_span` plus recurrence across distinct runs or distinct asset/surface families

## Truth discipline

- `line_registry` remains a derived current-state surface
- `reread_observation_log.jsonl` and `line_promotion_log.jsonl` remain the truth archive

## One-line lock

> line thickening should remain grounded in source-linked or direct evidence; summary echo may be recorded, but it should not become thickening fuel by default.
