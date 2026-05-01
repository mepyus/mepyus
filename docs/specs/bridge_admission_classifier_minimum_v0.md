# Bridge Admission Classifier Minimum v0

## Verdict

`PASS_WITH_NOTE`

`scripts/cli/lower_upper_admission_classifier.py` operationalizes the Pre-1.12B bridge minimum as a conservative admission helper.

## Purpose

Classify a lower artifact into one upper admission level:

- `reject_for_upper`
- `evidence_only`
- `ingest_ready`
- `packet_candidate`

The classifier does not change lower readiness. It only reports the safest upper admission.

## Inputs

Minimum inputs:

- `artifact_path`
- optional `--readiness-hint`
- optional `--artifact-kind`
- optional checklist signals:
  - `--provenance-present`
  - `--trace-present`
  - `--routing-present`
  - `--packet-worthiness-present`

## Output Fields

The classifier emits JSON with:

- `artifact_path`
- `artifact_exists`
- `artifact_kind`
- `readiness_hint`
- `upper_admission`
- `classifier_confidence`
- `reasons`
- `blocked_higher_admission`
- `checklist_signals`
- `manual_note`
- `guardrail`

## Conservative Rules

| observed/hinted readiness | admission |
| --- | --- |
| `residue-only` | `reject_for_upper` |
| `evidence-ready` | `evidence_only` |
| `engine-ingest-ready` | `ingest_ready` |
| `packet-candidate` | `packet_candidate` |

Additional rules:

- missing artifact path -> `reject_for_upper`;
- runtime residue -> `reject_for_upper`;
- source manifests/split units/operator summaries -> `evidence_only`;
- preprocessed material -> `ingest_ready`;
- preprocess comparison artifacts -> `packet_candidate`;
- GMD/native read -> cautious `packet_candidate` with support note;
- unknown or ambiguous hints never raise admission.

## Interpretation

The classifier is a judgment aid, not a promotion engine. It makes the existing bridge minimum executable, but it does not decide source meaning, baseline status, or line/axis readiness.

`evidence_only` is a normal result. Many lower artifacts are useful evidence but should not become request frames.

Ambiguous cases stay lower because readiness inflation is more damaging than a conservative admission note.

## Validation

- Matches Pre-1.12B transition table: `PASS`.
- Keeps blocked higher admission visible: `PASS`.
- Does not change schemas or artifact paths: `PASS`.
- Does not patch lower input organ: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created/updated:
   - `scripts/cli/lower_upper_admission_classifier.py`
   - `docs/specs/bridge_admission_classifier_minimum_v0.md`
3. What was operationalized: bridge admission classification.
4. What remains unresolved: classifier is heuristic and conservative.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended closeout move: add examples and wrapper usage.
