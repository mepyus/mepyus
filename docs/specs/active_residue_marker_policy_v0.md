# Active / Residue Marker Policy v0

## Status

```yaml
status: marker_policy_candidate
date: 2026-05-06
baseline_lock: false
automation: false
schema: false
registry: false
scope: bounded_space_asset_sampling
```

## Purpose

Give older reports and records a lightweight status marker when they are used for current Anchor Stack planning.

This policy prevents old records from being overread as current active anchors.

## Marker Set

```text
active
candidate_only
watch_only
residue
raw_trace
```

## Marker Meanings

### active

The asset currently changes route, PV, Plan Basis, gate, or Movement Record behavior.

Use only with a direct current-purpose pointer.

### candidate_only

The asset contains useful structure but has not changed current task behavior yet.

Use when it may support future route/PV updates.

### watch_only

The asset is mostly a risk signal or caution.

Use when it should prevent overpromotion or drift.

### residue

The asset is historical context that should not drive current planning unless reactivated by a bounded read.

Use when older records are useful for lineage but not current instruction.

### raw_trace

The asset is an external tool output, log, transcript, runner output, or unprocessed worker report.

It must be packaged before memory promotion.

## Sampling Rule

Apply markers only to bounded samples:

- files named by a route
- files named by a Plan Basis
- files named by a Gemini/Codex worker return
- files needed to decide active vs residue for one current route

Do not apply this to the whole docs tree.

## Route Link

Use `ROUTE_SPACE_RESIDUE_SAMPLING` when:

- older reports may be mistaken for current anchors
- route evidence depends on older packages/sessions
- the worker asks for active/residue distinction

Recommended PVs:

```text
PV_NON_INSPECTED_DISCLOSURE
PV_LINE_MATURITY_CAUTION
```

## Do Not

- Do not turn markers into archive taxonomy.
- Do not bulk-label all files.
- Do not infer active status from recency alone.
- Do not infer residue status from age alone.
- Do not let raw trace become memory without Return-to-Space packaging.
