# Phase 1.12 Pairing Diff Merge Binding Check Report v0

## Verdict

`PASS_WITH_NOTE`

Legacy backfill is now read by the CLI helper layer. It affects identity anchors, pair confidence context, merge identity risk notes, and reingress identity learning without changing the four-artifact spine.

## Execution

Checked:

- `scripts/cli/identity_helpers.py`
- `scripts/cli/pairing_helpers.py`
- `scripts/cli/diff_helpers.py`
- `scripts/cli/explore_space.py`
- `scripts/cli/merge_or_diff.py`
- `scripts/cli/write_reingress_record.py`

Minimal binding added:

- `identity_helpers.read_identity_anchor()` reads `docs/indexes/legacy_artifact_family_identity_map_v0.json` when a JSON artifact lacks inline `artifact_identity`.
- `build_question_packet.py` adds Phase 1.12 legacy/backfill search targets when the request names legacy/backfill/old-new comparison.

## Binding Results

| layer | legacy identity effect | status |
| --- | --- | --- |
| identity helper | mapped legacy artifacts return `plausible_identity` with `legacy_backfill_map` source | `PASS` |
| pairing helper | old/new pairs carry legacy identity confidence and identity support refs | `PASS` |
| diff helper | diff units inherit pair confidence and identity confidence through exploration | `PASS` |
| exploration | `identity_anchors`, `identity_anchor_summary`, `pairing_units`, and `diff_evidence_units` receive legacy identity context | `PASS` |
| merge/diff/hold | `identity_risk_note`, `pairing_risk_note`, and identity confidence arrays reflect legacy anchors | `PASS` |
| reingress | `useful_identity_modes`, `weak_identity_areas`, `reusable_identity_groups`, and `identity_risk_summary` preserve learning | `PASS` |

## Check Output

Manual helper checks showed:

- `runtime/merge_diff_reports/phase1_8_run_03_merge_diff_report.json` now reads as `plausible_identity` from `legacy_backfill_map`.
- `app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json` now reads as `plausible_identity` with lower bridge guardrail note.
- `runtime/contracts/merge_diff_report_v0.json` now reads as `plausible_identity` in the runtime contract family.
- A mixed pair between `phase1_9_run_03_merge_diff_report.json` and `phase1_11_run_03_merge_diff_report.json` carries `plausible_identity -> strong_identity` rather than path-only inference.

## Interpretation

Backfill is not just documentation. It changes the comparison layer from "infer old artifact identity from path only" to "read a bounded companion identity anchor first, then fall back to path inference only when unmapped."

The effect appears at three layers:

1. pairing is more honest about old/new identity confidence;
2. merge/diff can write identity risk notes based on mapped legacy confidence;
3. reingress preserves which identity modes worked.

What remains heuristic:

- legacy map entries are still companion assertions, not embedded self-description;
- broad legacy archive still falls back to path/stem inference;
- same-family matching remains stem/version based, not content-signature based.

## Validation

- Python compile passed for relevant CLI helpers: `PASS`.
- Legacy identity map parses as JSON: `PASS`.
- Helper reads mapped identity entries: `PASS`.
- New spine remains v5 four-artifact flow: `PASS`.
- Bridge guardrail remains unchanged: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created/updated: `docs/reports/phase1_12_binding_check_report_v0.md`
3. What was backfilled: binding from companion map into helper/pairing/diff/merge/reingress path.
4. What remains unresolved: broad unmapped legacy families remain heuristic.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended next move: run bounded old/new mixed scenarios.
