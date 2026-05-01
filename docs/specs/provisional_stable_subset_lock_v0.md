# Provisional Stable Subset Lock v0

## Purpose

This document locks the Phase 1.5 through Phase 1.12 working core as a provisional stable subset. It is not a full baseline promotion, not a final naming lock, and not a canonical path migration.

The lock protects the currently repeatable operating spine so future lower-side patching, invocation grammar work, and expansion do not break it accidentally.

## Locked Subset List

### 1. Four-Artifact Spine

The stable runtime flow is:

```text
question packet
-> exploration result
-> merge/diff/hold report
-> reingress record
```

The current entrypoint is:

- `scripts/cli/run_phase1_space_query.py`

The current runtime lanes are:

- `runtime/query_packets/`
- `runtime/exploration_results/`
- `runtime/merge_diff_reports/`
- `runtime/reingress_records/`

### 2. Current v5 Working Artifact Shape

The current working templates are:

- `runtime/contracts/space_exploration_result_v5.json`
- `runtime/contracts/merge_diff_report_v5.json`
- `runtime/contracts/space_reingress_record_v5.json`

This locks compatibility with the v5 additive shape, not final schema names.

### 3. Guardrail Core

Locked guardrails:

- lower readiness and upper admission are separate;
- `evidence_only` is a stable safe landing zone;
- hold remains narrow;
- identity backfill does not change readiness;
- pair confidence, identity confidence, diff salience, and authority are separate layers.

### 4. Additive Evidence Lanes

Locked as additive lanes:

- grounded evidence with pointer/excerpt/fallback;
- excerpt quality visibility;
- structured path-aware evidence;
- before/after diff evidence;
- pairing evidence before diff claims;
- artifact identity evidence;
- legacy companion-map identity evidence.

### 5. Legacy Companion Map Mode

The approved Phase 1.12 legacy approach is companion-map/sidecar identity, not destructive rewrite:

- `docs/indexes/legacy_artifact_family_identity_map_v0.json`

Legacy mapped identity remains capped at `plausible_identity` unless the artifact itself emits inline identity.

## Explicit Non-Goals

- No baseline promotion.
- No final taxonomy naming lock.
- No canonical path movement.
- No schema rewrite.
- No UI work.
- No vector retrieval.
- No full provenance graph.
- No line/axis/camera promotion.
- No lower input organ patch in this lock.
- No broad legacy archive rewrite.

## Lock Boundary

Inside the lock:

- artifact chain order;
- runtime lane compatibility;
- v5 additive artifact shape;
- guardrail semantics;
- evidence-only default;
- hold discipline;
- identity confidence visibility;
- legacy companion-map method.

Outside the lock:

- exact scoring weights;
- final confidence labels;
- final family taxonomy;
- content-signature matching;
- invocation grammar design;
- lower organ implementation;
- broad archive policy;
- baseline status.

## Do-Not-Change Zones

Future work must not:

1. remove any of the four artifact stages;
2. collapse evidence-only into packet-candidate;
3. make identity confidence imply readiness;
4. compare diff evidence before checking pair confidence;
5. hide weak identity, weak pair, or comparison risk notes;
6. rewrite legacy artifacts broadly to simulate native identity;
7. treat line/axis/camera evidence as stable core;
8. convert this lock into baseline without a separate decision.

## Allowed Future Work Around The Lock

Allowed:

- additive helper improvements;
- stricter validation reports;
- more bounded runs;
- lower-side bridge classifier that preserves admission rules;
- invocation grammar wrapper that still emits the four artifacts;
- second bounded legacy backfill for a proven high-use family;
- content-signature experiment outside the locked core.

## Unlock Conditions

Reopen this lock if:

- four-artifact flow stops working;
- v5 artifacts no longer parse or no longer include identity where expected;
- bridge admission changes are required;
- lower-side patch needs new readiness semantics;
- final naming or baseline decision is requested;
- a future phase proves a better core with repeated runs.

## Relation To Future Lower-Side Work

Lower-side patch work may proceed only around this lock. It may improve compare-ready packaging or bridge classification, but it must not promote lower evidence directly into upper packet status.

## Relation To Future Invocation Grammar Work

Invocation grammar work may wrap or enrich the input surface, but it must still emit the same four artifact classes and preserve stop/hold behavior.

## Relation To Baseline Promotion Later

This lock may become evidence for a future baseline promotion discussion. It is not itself that promotion. A future promotion would require user decision, broader run evidence, and explicit authority review.

## Interpretation

This lock is not a full baseline because it protects only the operational core. It deliberately leaves naming, scoring, broad archives, and promotion-sensitive semantic layers outside.

Its value is practical: future work can move faster because it knows what not to break.

## Validation

- Lock is concrete enough to guide future edits: `PASS`.
- Lock does not conflict with current runtime reality: pending Stage 5 compatibility check.
- No final naming or baseline decision is made: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created: `docs/specs/provisional_stable_subset_lock_v0.md`
3. What is now inside the subset: working core listed above.
4. What remains outside: final taxonomy, broad archive, lower patch, invocation grammar, line/axis/camera.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended next move: run lock compatibility check.
