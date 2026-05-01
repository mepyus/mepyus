# Phase 1.15 Lower Input Softening Patch Priority Map v0

## Verdict

`PASS_WITH_NOTE`

The first practical patch axis should be content-role plus line-seed support over existing split outputs. Camera support and axis hold support should stay spec-first until the seed layer exists.

## Priority Table

| axis | judgment | reason | expected operator benefit | expected risk |
| --- | --- | --- | --- | --- |
| split unit | `spec-first` | current split is stable; first clarify line-seed-friendly criteria before patching | better split evaluation without destabilizing lower traces | premature splitter patch could disturb readiness and trace |
| content-role | `light patch` | narrow, local, and directly reduces upper interpretation burden | faster distinction between claim/background/correction/connective work | role over-claim if taxonomy grows too fast |
| line seed bundle | `light patch` | this is the missing middle layer between split and evidence use | repeated pressure and correction flow become reusable | mistaken as line promotion if boundary is unclear |
| camera support | `spec-first` | useful, but should build on role/seed outputs first | later camera reading gets safer context span notes | premature hint vocabulary may drift into pseudo-taxonomy |
| axis hold support | `spec-first` | should only exist after seed-level grouping exists | keeps non-promotable direction visible without upper rediscovery | risk of pseudo-axis promotion if emitted too early |
| lower→upper bridge interaction | `keep` | bridge minimum already works; new layers should travel underneath it | preserves admission discipline while lower gets softer | inflation risk if new layers are mistaken for packet-worthiness |

## Why This Order

### 1. Content-Role First

Content-role is the cheapest useful softening layer:

- small taxonomy;
- local to split units;
- immediately useful for later grouping.

### 2. Line Seed Next

Once role is available, line seed bundling becomes more honest:

- repeated pressure can be named;
- correction can be grouped;
- tension can be kept visible without promotion.

### 3. Camera Support After Seed

Camera support is meaningful only when the material already has some grouped pressure and role pattern. Otherwise the hint is too speculative.

### 4. Axis Hold After Seed

Axis hold support should be even more conservative. It is helpful only when multiple seed refs already suggest a direction but still fail promotion criteria.

## Keep / Hold Notes

- keep bridge minimum unchanged;
- keep evidence-only as the default landing zone;
- hold any attempt to reclassify readiness;
- hold any attempt to patch promotion logic.

## Interpretation

The path with the best efficiency gain is not split rewrite. It is adding one narrow layer that says what chunks are doing, then one narrow layer that says what pressure is forming.

That order thickens the lower organ while keeping the current core stable.

## Validation

- The priority order is narrow and realistic: `PASS`.
- The order does not break current lock or bridge minimum: `PASS`.
- The next implementation package can start from this map: `PASS_WITH_NOTE`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created: `docs/reports/phase1_15_lower_input_softening_patch_priority_map_v0.md`
3. What was clarified: patch order across split, role, seed, camera support, axis hold support.
4. What remains unresolved: exact light-patch surface for role and seed emission.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended first implementation axis: content-role tagging plus line-seed bundling over current observer/preprocess outputs.
