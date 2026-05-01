# Pre-1.12B Bridge Surface Identification Report v0

## Verdict

`PASS_WITH_NOTE`

The lower and upper systems already touch through file paths, evidence pointers, and human-readable generated reports. They do not yet touch through a stable admission rule. The bridge is dependency-heavy because an operator must still decide whether a lower artifact is only residue, usable evidence, engine-ingest-ready material, or a true upper packet candidate.

## Execution

### Lower Readiness Examples

| readiness | real artifact example | current lower meaning | upper surface candidate |
| --- | --- | --- | --- |
| residue-only | `runtime/events/engine_event_ledger.jsonl` | operational trace and run residue | reject for direct upper use; cite only as trace context when needed |
| residue-only | `runtime/receipts/*` | operation receipt or provenance residue | reject for packet use; possible supporting trace |
| evidence-ready | `app/work/observer_ingest_min/generated/source_manifest_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260328_071128.json` | source identity, profile, split mode, run id | upper evidence source or selected asset reason |
| evidence-ready | `app/work/observer_ingest_min/generated/split_units_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json` | segmented source units with excerpt pointers | upper evidence units, excerpt pointers, selected asset reasons |
| evidence-ready | `app/work/observer_ingest_min/generated/operator_summary_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.md` | human-readable lower interpretation | evidence-only support unless paired with readiness and route note |
| engine-ingest-ready | `app/work/observer_ingest_min/examples/sample_input_registry.json` | registry-shaped lower input | lower engine input; upper reference only unless interpretation frame exists |
| engine-ingest-ready | `app/work/external_input_preprocess/generated/builder_choi_interview_transcript_regroup_compare_20260405T074527Z.txt` | preprocessed transcript-like material | ingest-ready material, not automatically packet-candidate |
| packet-candidate | `app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json` | before/after gate, readiness signals, checkpoints | packet candidate or evidence bundle seed after admission checklist |
| packet-candidate | `app/work/observer_ingest_min/generated/gmd_native_read_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json` | native read with lower interpretation surface | packet candidate when scope, provenance, and route are clear |

### Upper Currently Consumable Artifact Kinds

| upper surface | currently accepted shape | lower source that can feed it | current gap |
| --- | --- | --- | --- |
| question packet `search_targets` | path refs, asset refs, target reasons | source manifests, split units, preprocess comparisons | no rule for when lower path becomes a search target |
| question packet `constraints` | scope limits, hold notes, ambiguity notes | readiness read, gate decision, trace notes | no direct lower-to-constraint mapping |
| exploration `selected_assets` | asset refs with selection reasons | source manifests, operator summaries, split units | selection still depends on operator interpretation |
| exploration `evidence_units` | source refs, pointers, excerpt, why it matters | split units, readable boards, comparison JSON | readiness does not automatically produce why-it-matters |
| merge/diff/hold `final_reasoning_basis` | comparison of space position and Codex position | preprocess comparison, lower readiness notes | lower quality and upper packet-worthiness are not separated |
| reingress `future_probe_note` | next probe hints and unresolved notes | lower action maps, probe reports, comparison checkpoints | bridge hints are not consistently carried forward |

### Direct Contact Points

1. A lower artifact path can already be carried into an upper `search_targets` list.
2. A split unit can already become an upper evidence pointer or excerpt.
3. A source manifest can already support provenance and selected asset reasons.
4. A preprocess comparison can already seed an upper comparison or verification packet.
5. A lower action or readiness report can already become a constraint or ambiguity note.

### Break Points

| break point | what currently happens | bridge implication |
| --- | --- | --- |
| readiness not encoded as upper admission | Codex reads several lower artifacts and infers status manually | bridge must separate lower readiness from upper admission |
| evidence-ready overclaim risk | complete-looking summaries may be treated as packet candidates | default should be `evidence_only` |
| engine-ingest-ready ambiguity | lower engine can read a material, but upper goal may still be missing | `ingest_ready` is not `packet_candidate` |
| packet-candidate dependency | candidate quality depends on provenance, route, and bounded scope | admission checklist must be explicit |
| line/axis temptation | lower reports may imply future line use | promotion remains blocked in this package |

## Interpretation

The lower and upper systems are not disconnected. They are connected through paths, evidence references, generated summaries, and comparison artifacts. The problem is that the contact surface lacks admission discipline.

`dependency-heavy` means Codex must currently do too many unstated bridge tasks in its head:

- classify lower readiness;
- decide whether the artifact is evidence or packet material;
- map lower fields into upper packet or evidence fields;
- detect over-promotion risk;
- decide what ambiguity must stay lower.

This is not primarily a lower implementation failure or an upper CLI spine failure. It is a handoff-rule failure.

## Validation

- Real lower artifact examples are identified: `PASS`.
- Upper surfaces are reference-only and not redefined: `PASS`.
- Lower material intake is kept separate from upper request intake: `PASS`.
- The main gap is specified as admission and mapping discipline, not new structure: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created: `docs/reports/pre12_bridge_surface_identification_report_v0.md`
3. What was fixed at the bridge level: the active lower-upper contact surfaces were named.
4. What remains unresolved: exact admission and field mapping rules.
5. Whether user decision is required: no.
6. Can Phase 1.12 start after this? not yet; minimum bridge spec should be written first.
7. Recommended next move: create the lower-to-upper bridge minimum spec.
