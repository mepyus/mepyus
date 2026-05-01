# Pre-1.12 Lower Output Readiness Recheck v0

## Verdict

`PASS_WITH_NOTE`

The readiness ladder remains useful, but most lower outputs stop at residue-only or evidence-ready. Only a smaller subset is engine-ingest-ready, and packet-candidate remains provisional because lower outputs do not yet carry a stable admission rule into the upper CLI packet/evidence spine.

## Readiness Ladder

| readiness | meaning | current examples | why not higher |
| --- | --- | --- | --- |
| `residue-only` | Useful trace/residue, not enough for direct reasoning or packet admission | `runtime/events/*`, `runtime/receipts/*`, repeated generated boards, `runtime/views/*` derived views | Records activity and history but often lacks compact claim/evidence/readiness shape |
| `evidence-ready` | Human/Codex can cite or read it as evidence with source context | `source_manifest_*.json`, `split_units_*.json`, `processing_trace_*.json`, `readable_input_board_*.md`, `operator_summary_*.md`, `raw_intake_gap_analysis_before_middle_layer_fix_v1.md` | Evidence is readable, but does not always state admission decision or next upper packet shape |
| `engine-ingest-ready` | Shape is stable enough for a lower route or runtime helper | `input_registry_contract_v1.md`, observer ingest direct/registry inputs, structured-doc routing label packets, transcript preprocess sidecars after probe | Still lower-engine ready, not automatically upper question-packet ready |
| `packet-candidate` | Could become an upper CLI packet/evidence target with minimal interpretation | preprocess comparison JSON with readiness read, GMD/native read payload, middle-layer compare-ready examples, selected operator summaries with clear source/trace | Needs stable lower->upper bridge rule: what fields become search targets, evidence units, constraints, ambiguity notes |

## Example Reclassification

- `app/work/observer_ingest_min/generated/source_manifest_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260328_071128.json`: evidence-ready. It identifies source path, profile, split mode, unit count, and run id.
- `app/work/observer_ingest_min/generated/split_units_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json`: evidence-ready. It contains unit refs and excerpts, but not a line/axis decision.
- `app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json`: packet-candidate. It has before/after gates, readiness read, and next checkpoint, but still needs bridge mapping into upper packet fields.
- `app/work/external_input_preprocess/generated/*regroup*.txt`: engine-ingest-ready or evidence-ready depending on whether probe has passed. Alone it is not packet-candidate.
- `docs/reports/raw_intake_gap_analysis_before_middle_layer_fix_v1.md`: evidence-ready and action-informing, but not packet-candidate because it intentionally says patch later and does not encode a runtime admission object.

## Why Some Outputs Are Not Packet-Candidate

Many lower outputs are intentionally about preservation, visibility, or diagnosis:

- split units say what was cut, not what should be asked;
- operator summaries say what is readable, not what is claim-ready;
- preprocess sidecars improve shape but need a post-preprocess probe;
- raw input probes expose flattening, but do not package topic-bearing frame blocks.

The upper CLI packet requires a request-like structure: interpreted goal, constraints, search targets, expected output shape, ambiguity handling, and merge mode candidate. Lower outputs do not yet consistently provide that.

## Interpretation

The readiness criteria still hold:

- `residue-only` is not a failure.
- `evidence-ready` is the common healthy lower output.
- `engine-ingest-ready` means lower machinery can read it, not that upper can answer with it.
- `packet-candidate` should be reserved for lower outputs with source, reason, readiness, candidate frame, and next route/axis hints.

## Validation

- Readiness categories are non-identical: PASS.
- Each category has actual examples: PASS.
- The distinction between lower engine readiness and upper packet readiness is preserved: PASS.
- Packet-candidate remains intentionally narrow: PASS.

## Next Stage Entry

Proceed to lower -> upper bridge diagnosis.
