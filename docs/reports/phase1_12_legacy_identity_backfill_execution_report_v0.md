# Phase 1.12 Legacy Identity Backfill Execution Report v0

## Verdict

`PASS_WITH_NOTE`

Bounded identity backfill was executed through a companion mapping table and helper binding. No legacy artifact was destructively rewritten.

## Execution

Created:

- `docs/indexes/legacy_artifact_family_identity_map_v0.json`
- `docs/indexes/legacy_artifact_family_identity_map_v0.md`

Updated:

- `scripts/cli/identity_helpers.py`
- `scripts/cli/build_question_packet.py`

The helper now checks the legacy identity map before falling back to path/stem inference when a JSON artifact lacks inline `artifact_identity`.

## Backfilled Families

| family | mode applied | confidence | why this mode is safest |
| --- | --- | --- | --- |
| runtime contract v-series | `mapping_table_family_backfill` | `plausible_identity` | avoids rewriting templates while giving v0-v5 contracts comparable family keys |
| Phase 1.8/1.9/1.10 run-03 merge reports | `mapping_table_family_backfill` | `plausible_identity` | supports old/old and old/new mixed comparison without pretending old files emitted identity |
| external preprocess comparison artifacts | `sidecar_identity_note` + map | `plausible_identity` | preserves bridge guardrail for lower packet-candidates |
| observer raw-intake generated bundle | `mapping_table_family_backfill` | `plausible_identity` | clarifies source/split/GMD roles while preserving evidence-only admission |

## Do Not Backfill Yet

| family | reason |
| --- | --- |
| line/axis/camera reports | promotion-sensitive; identity may be misread as line/axis readiness |
| broad observer archive | too large and uneven for bounded Phase 1.12 |
| receipts and event ledgers | residue-only and rejected for upper by bridge guardrail |

## Interpretation

The map approach is safest because it is reversible, bounded, and explicit. It gives pairing/diff/merge enough identity to reduce path-only inference, but it leaves old artifact contents intact.

The selected legacy artifacts receive `plausible_identity`, not `strong_identity`. That ceiling is deliberate: they did not originally emit inline identity, so backfill should improve honesty without pretending the self-description was native.

## Validation

- Old artifacts were not rewritten: `PASS`.
- Canonical paths were not moved: `PASS`.
- Identity confidence and basis are explicit: `PASS`.
- Readiness guardrail is included in each map entry: `PASS`.
- No baseline or final naming lock was made: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created/updated:
   - `docs/indexes/legacy_artifact_family_identity_map_v0.json`
   - `docs/indexes/legacy_artifact_family_identity_map_v0.md`
   - `scripts/cli/identity_helpers.py`
   - `scripts/cli/build_question_packet.py`
3. What was backfilled: selected legacy families via companion map.
4. What remains unresolved: broader archive backfill and automated bridge admission.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended next move: verify pairing/diff/merge binding.
