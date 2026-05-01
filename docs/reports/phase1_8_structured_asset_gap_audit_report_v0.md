# Phase 1.8 Structured Asset Gap Audit Report v0

## Verdict

`PASS_WITH_NOTE`

Phase 1.7 improved prose-like excerpt quality, but runtime/generated/JSON assets are still often read at identity or top-level shape level. The next gap is structured salience: which field/path matters for the question, and what implication that field has.

## Execution

Audited:

- `docs/reports/phase1_6_evidence_grounding_validation_report_v0.md`
- `docs/reports/phase1_7_excerpt_quality_validation_report_v0.md`
- `docs/specs/evidence_unit_grounding_contract_v0.md`
- `docs/specs/excerpt_quality_contract_v0.md`
- `scripts/cli/explore_space.py`
- `scripts/cli/excerpt_helpers.py`
- Phase 1.6 and 1.7 run artifacts
- `runtime/contracts/*.json`

## Gap Types

- `identity_only`: JSON excerpt captures `contract_id`, `contract_status`, and `extends` only.
- `shape_only`: excerpt shows object shape but not the path relevant to the question.
- `field_without_implication`: a key/value is visible but no `why_it_matters` or salience is attached.
- `diff_without_salience`: structured difference is possible but no changed path is prioritized.
- `noisy_large_object`: likely risk when generated artifacts grow beyond contract templates.
- `nested_path_blindness`: nested fields such as `evidence_units[].grounding_status` or `validation.learning_fields_present` are not selected.
- `fallback_overuse_on_json`: not dominant yet, but fallback could hide structured fields in large/unreadable JSON.

## Interpretation

After prose excerpt tuning, the next bottleneck is structured asset reading because runtime contracts and generated records are operationally important. They are not prose sources. Reading them as line windows around the top of the file proves identity, but it does not explain whether the artifact has evidence depth, learning fields, stop flags, or path-level compatibility.

JSON should be read as an evidence source where paths carry meaning. For contract questions, required fields and validation flags matter. For diff-heavy questions, changed or salient paths matter. For generated artifact questions, status, chosen mode, evidence depth, and reusable paths matter.

This is different from prose reading. Prose evidence needs coherent excerpt windows. Structured evidence needs path, node kind, shape summary, value excerpt, and salience reason.

## Validation

- Structured gaps are distinct from prose excerpt gaps: PASS.
- Next contract target is clear: field/path evidence units.
- Spine can be preserved with additive fields and helper logic.
- No baseline or path migration is needed.

## Entry Condition For Next Stage

Create a structured evidence contract and bounded JSON/path extraction helper.
