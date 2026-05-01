# Legacy Artifact Identity Backfill Contract v0

## Verdict

`PASS_WITH_NOTE`

Legacy identity backfill is a bounded companion layer. It improves artifact self-description for comparison, but it does not rewrite old artifacts, does not change readiness, and does not promote lower outputs to upper packet status.

## Scope

This contract applies only to selected legacy artifact families that are repeatedly used by the Phase 1.5 through Phase 1.11 CLI spine.

## Backfill Modes

| mode | when to use | when not to use | required evidence | readiness risk | confidence ceiling |
| --- | --- | --- | --- | --- | --- |
| `inline_minimum_backfill` | artifact is still actively generated, safely editable, and already has a JSON object shape | old artifact would need destructive rewrite or bulk churn | stable role, family, run stem, phase label, generated chain | medium; inline fields may be mistaken as native identity | `strong_identity` only for newly emitted or safely regenerated artifacts |
| `sidecar_identity_note` | artifact should not be modified but needs human-readable identity explanation | large archive where per-artifact notes would sprawl | path, role, family key, lineage hint, reason | low-medium; note must state no readiness promotion | `plausible_identity` |
| `mapping_table_family_backfill` | many artifacts share a family pattern and scripts need machine-readable identity | family is ambiguous or usage is rare | exact path entries or bounded family group with explicit basis | low when exact path based | `plausible_identity` for legacy, unless embedded marker exists |
| `do_not_backfill_yet` | family is promotion-sensitive, rare, broad, or poorly bounded | artifact is in active old/new comparison path | reason for holding and future probe | safest | `weak_identity` or no assignment |

## Recommended Identity Fields

```json
{
  "artifact_identity": {
    "artifact_role": "",
    "family_key": "",
    "lineage_hint": "",
    "run_stem": "",
    "phase_label": "",
    "artifact_slot": "",
    "generated_from_ref": "",
    "prior_artifact_ref": "",
    "identity_confidence": "weak_identity",
    "identity_basis": []
  }
}
```

Additional fields may be present when using the Phase 1.11 identity anchor shape, including `artifact_id`, `comparison_ready`, and `identity_anchor_source`.

## Confidence Ceiling Rules

| source of identity | maximum confidence |
| --- | --- |
| embedded identity emitted by current scripts | `strong_identity` |
| exact sidecar or mapping entry for a legacy artifact | `plausible_identity` |
| path/stem inference without mapping entry | `plausible_identity` only when role is clear, otherwise `weak_identity` |
| broad family inference without exact path | `weak_identity` |
| promotion-sensitive report title only | `weak_identity` or `do_not_backfill_yet` |

## Readiness Guardrail

Identity confidence is not readiness admission.

| identity result | forbidden implication |
| --- | --- |
| `plausible_identity` | does not turn evidence-ready into packet-candidate |
| `strong_identity` | does not promote baseline, naming, line, or axis status |
| sidecar/mapping identity | does not prove source meaning |
| same-family identity | does not prove diff salience |

Pre-1.12B transitions remain locked:

- `residue-only -> reject_for_upper`
- `evidence-ready -> evidence_only`
- `engine-ingest-ready -> ingest_ready`
- `packet-candidate -> packet_candidate`

## Interpretation

Legacy backfill must be bounded because old artifacts were generated before the current identity discipline existed. Forcing every old artifact to look like a new artifact would create false confidence.

Inline is not the only correct answer. Sidecar notes and mapping tables are safer when old artifacts should remain unchanged or when the only goal is to help pairing/diff read family and role more honestly.

Identity backfill does not mean readiness promotion. It answers "what artifact is this?" not "how far may this artifact travel into the upper loop?"

## Validation

- Contract is additive and bounded: `PASS`.
- Confidence ceilings prevent false strong identity: `PASS`.
- Bridge minimum guardrail is repeated and preserved: `PASS`.
- Old/new mixed comparison receives a machine-readable path: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created/updated: `docs/specs/legacy_artifact_identity_backfill_contract_v0.md`
3. What was backfilled: nothing yet; mode rules were fixed.
4. What remains unresolved: concrete targets and companion map.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended next move: select bounded backfill targets.
