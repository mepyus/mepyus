# Bridge Admission Classifier Examples v0

## Basic Commands

Residue-only trace:

```bash
python3 scripts/cli/lower_upper_admission_classifier.py runtime/events/engine_event_ledger.jsonl
```

Expected admission:

```text
reject_for_upper
```

Evidence-ready source manifest:

```bash
python3 scripts/cli/lower_upper_admission_classifier.py app/work/observer_ingest_min/generated/source_manifest_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json --readiness-hint evidence-ready
```

Expected admission:

```text
evidence_only
```

Packet-candidate preprocess comparison:

```bash
python3 scripts/cli/lower_upper_admission_classifier.py app/work/external_input_preprocess/generated/builder_choi_interview_transcript_preprocess_comparison.json --readiness-hint packet-candidate
```

Expected admission:

```text
packet_candidate
```

## Operator Note

The classifier output should be read as admission guidance. It does not mean a lower artifact is semantically correct, baseline-ready, or promotion-ready.

## Validation

- Examples cover residue, evidence, and packet-candidate cases: `PASS`.
- Over-promotion is blocked by default: `PASS`.
