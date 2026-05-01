# Phase 1.13 Subset Selection Report v0

## Verdict

`PASS_WITH_NOTE`

The selected subset is the current working core: four-artifact spine, v5 runtime artifact lane, bridge minimum, evidence-only landing zone, hold discipline, additive evidence lanes, identity anchoring for new artifacts, and companion-map legacy identity backfill. The lock intentionally excludes final taxonomies, content-signature matching, lower organ patching, and line/axis/camera promotion.

## Selected Subset Items

| selected item | why selected | dependency notes | future impact if changed |
| --- | --- | --- | --- |
| `run_phase1_space_query.py` four-artifact flow | repeated Phase 1.5-1.12 runs produced all four artifacts | depends on build/explore/merge/reingress scripts | changing sequence breaks current usage loop |
| runtime lanes `runtime/query_packets`, `runtime/exploration_results`, `runtime/merge_diff_reports`, `runtime/reingress_records` | stable artifact locations across repeated runs | not a canonical path migration; working lane lock only | moving lanes breaks old/new run comparison |
| v5 artifact identity emission | Phase 1.11/1.12 generated artifacts emit inline identity | depends on identity helpers and v5 templates | future scripts must keep artifact identity or provide compatibility |
| lower->upper bridge minimum | Pre-1.12B and Phase 1.12 guardrail passed | depends on readiness/admission separation | lower-side patch must not bypass admission |
| evidence-only landing zone | prevents lower evidence over-promotion | depends on bridge checklist | future bridge work must preserve this default |
| hold discipline | stop conditions remain narrow and tested | depends on decision gate behavior | final naming/baseline/path decisions must still hold |
| grounded evidence lane | repeated runs preserve pointer/excerpt/depth/fallback | depends on excerpt helpers | future evidence work must keep pointer fallback |
| excerpt quality fields | useful for review and merge risk | heuristic labels remain outside final lock | future tuning can change thresholds but not hide quality |
| structured evidence lane | JSON/path evidence works across v2-v5 | depends on structured helper | future structured work must preserve path/salience visibility |
| diff evidence lane | before/after changed path evidence works | depends on diff helper and pairing input | future diff work must keep bounded before/after units |
| pairing lane | pair-before-diff discipline works | depends on family/path/version heuristics | future pairing must keep rejected candidates and risk notes |
| identity lane | new artifacts self-describe and old artifacts can be risk-noted | depends on identity helper | future identity work must keep confidence visible |
| legacy companion-map backfill mode | Phase 1.12 validates bounded old/new comparison | depends on `docs/indexes/legacy_artifact_family_identity_map_v0.json` | future backfill must not rewrite old archive blindly |

## Excluded Items

| excluded item | why excluded |
| --- | --- |
| final taxonomy naming | repeatedly marked not ready to lock |
| confidence/quality/salience scoring thresholds | useful but heuristic |
| content-signature identity | not implemented and still future work |
| full provenance graph | explicitly non-goal |
| broad observer archive backfill | too wide and uneven |
| lower input organ patch | not part of subset lock and still needs design |
| invocation grammar beyond current CLI options | not validated as a grammar system |
| line/axis/camera promotion-sensitive assets | high over-promotion risk |
| baseline promotion | out of scope and not justified by current runs |

## Interpretation

This subset is the current working core because it is the part future work depends on and repeated runs already exercised. It protects the operational spine without pretending the heuristics are final.

The excluded items remain useful, but not stable. Locking them now would either freeze provisional labels or blur the line between evidence handling and semantic promotion.

## Validation

- Selected items map to existing scripts/contracts/runtime lanes: `PASS`.
- Excluded items match repeated "not ready to lock" notes: `PASS`.
- Scope is working core, not full baseline: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created: `docs/reports/phase1_13_subset_selection_report_v0.md`
3. What is now inside the subset: selected working core items listed above.
4. What remains outside: heuristics, final naming, promotion-sensitive assets, broad archive.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended next move: write lock documentation.
