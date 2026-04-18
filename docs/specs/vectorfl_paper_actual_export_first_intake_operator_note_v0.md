# VectorFL Paper Actual Export First Intake Operator Note v0

## purpose
This note is for the first true host/export candidate intake only.

It does not create `inbox_latest`, does not replace the current slot, does not modify the proper surface, and does not close `actual_export_only`.

## template asset
- `runtime/manifests/vectorfl_paper_actual_export_candidate_intake_template_v0.json`

Use the template only when a real host/export candidate exists. Do not use it to create a synthetic candidate for more testing.

## when inbox_latest may be created
Create `runtime/manifests/vectorfl_paper_actual_export_candidate_inbox_latest_v0.json` only when all of the following are available:
- a raw export reference from the host/runtime
- a concrete export origin
- a capture timestamp or local receipt timestamp
- a capture context explaining why this candidate is relevant to VectorFL Paper
- a host/runtime relation note
- a transformation history from raw export into the four-surface shape
- an honesty declaration that it is not reference-derived and not a local fixture
- the four required surfaces: `issues_row`, `heartbeat_runs_row`, `issue_comments_rows`, `approvals_row`

## minimum raw export evidence
Minimum evidence means the operator can point to the raw captured export before VectorFL normalization.

It should include:
- `raw_export_ref`
- host system or product
- export origin such as workspace, project, repository, run, or issue source
- export method such as API export, CLI export, downloaded JSON, or host-generated archive
- capture timestamp and captured-by actor or adapter
- transformation history that explains every normalization step

If this evidence is missing, do not create `inbox_latest`.

## how to populate the template
1. Copy the template structure into `runtime/manifests/vectorfl_paper_actual_export_candidate_inbox_latest_v0.json` only after a real candidate exists.
2. Replace every placeholder with host-derived or operator-declared evidence.
3. Keep the raw export reference separate from the normalized four-surface record.
4. Preserve host field grammar where possible.
5. Put any synthetic or inferred fields in `honesty_declaration.synthetic_fields`.
6. Leave `runtime/manifests/vectorfl_paper_actual_export_host_record_slot_v0.json` unchanged.
7. Validate with:
   `python3 scripts/run_vectorfl_paper_actual_export_gate_validator.py --override-record runtime/manifests/vectorfl_paper_actual_export_candidate_inbox_latest_v0.json`

## provenance failure
Treat the intake as provenance failure if any of the following is true:
- raw export reference is absent
- export origin is vague or reconstructed from memory
- capture timestamp is absent and no local receipt timestamp exists
- host/runtime relation is not explained
- transformation history is missing
- record is copied from a reference candidate
- record is a local fixture with host-like fields
- redaction prevents shape or mapping judgment
- synthetic fields are present but not declared

## when to output request_candidate_provenance_fix
Use `request_candidate_provenance_fix` when the four-surface shape looks usable but evidence is not strong enough for supervisor review.

Typical cases:
- required surfaces exist but raw export provenance is incomplete
- candidate is likely actual but export origin is underspecified
- normalization history is missing or too broad
- redaction affects `resultJson`, comments, or governance payload judgment
- honesty declaration is incomplete

## why this is not gate close
The intake template and future inbox path are only preparation for validation.

None of the following counts as gate close:
- template creation
- `inbox_latest` creation
- successful shape validation
- `candidate_for_reopen_validation`
- comparison stability
- legacy surface merge-test readability

Gate close remains forbidden until a separate supervisor decision authorizes slot replacement review after a true host/export candidate passes override-record validation with sufficient provenance and reopen/gate evidence.
