# Phase 1.7 Excerpt Failure Shape Audit Report v0

## Verdict

`PASS_WITH_NOTE`

Phase 1.6 excerpt extraction created grounded fields, but sample runs show several quality failures. The spine works; the weak point is excerpt selection quality.

## Execution

Audited:

- `docs/reports/phase1_6_evidence_grounding_validation_report_v0.md`
- `docs/specs/excerpt_extraction_rules_v0.md`
- `docs/specs/evidence_unit_grounding_contract_v0.md`
- `docs/specs/reingress_learning_fields_v0.md`
- `scripts/cli/excerpt_helpers.py`
- `scripts/cli/explore_space.py`
- `runtime/exploration_results/phase1_6_run_01_exploration_result.json` through `phase1_6_run_05_exploration_result.json`

## Failure Shapes

- `title_only`: excerpt contains only one heading line, for example `# Source Authority Ladder v0`.
- `metadata_only`: excerpt captures status metadata rather than the operative rule.
- `too_short_to_support`: excerpt exists but is too short to support `why_it_matters`.
- `context_cutoff`: excerpt starts correctly but stops before the operative bullets or rule.
- `wrong_block_boundary`: heading lookup chooses a top-level heading rather than the relevant lower section.
- `noisy_generated_block`: likely future risk for generated/runtime documents.
- `fallback_overused`: not observed in Phase 1.6 bounded runs, but likely for missing/generated/large files.

## Interpretation

Excerpt quality is the grounding bottleneck because merge/diff/hold can only be as honest as the evidence it sees. A path plus a title is better than no source, but it still does not show the operative rule. Treating title-only excerpts as `cross_supported` makes the artifact look stronger than it is.

This is not a pointer fallback problem. Pointer fallback is still a required safety path. The problem is when extraction claims to be grounded but the excerpt is not useful enough to justify the selected reason.

Markdown specs/guides show `title_only` and `context_cutoff` most often. Status/contract documents can show `metadata_only`. Large/generated assets still need explicit fallback stress testing.

## Validation

- Failure types are separated: PASS.
- Tuning targets are clear: avoid title-only, widen short heading blocks, detect metadata-only, attach quality labels.
- Spine can be preserved: PASS.
- Next stage target: define quality labels and implement bounded retry/widen.
