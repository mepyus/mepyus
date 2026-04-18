# implementation placement baseline v0

## 0. One-line definition

This baseline defines where each implementation artifact should live in the system:
baseline, log, runtime summary, or evaluator.

It prevents concept translation from becoming a placement drift.

## 1. Purpose

This baseline exists so implementation artifacts are placed in the correct surface:

1. Keep definitions in baselines, not runtime mutation paths.
2. Keep events and judgments in append-only logs.
3. Keep current state in runtime summary surfaces, not as truth archives.
4. Keep calculations in evaluators, not in storage files.
5. Prevent Claude Code from mixing lifecycle layers for convenience.

Core sentence:

**A concept may descend into code, but its placement must still respect whether it is a definition, event, summary, or evaluator artifact.**

## 2. Placement layers

### 2.1 Baseline surface

Use this surface for:

- definitions
- locked rules
- forbidden mappings
- evaluator boundaries
- placement rules themselves

Examples:

- `concept_to_implementation_map_baseline_v0.md`
- `build_drift_anchor_baseline_v0.md`
- `implementation_eval_criteria_baseline_v0.md`
- `rejection_log_baseline_v0.md`

### 2.2 Append-only log surface

Use this surface for:

- decisions
- rejections
- holds
- reviews
- watch evaluations

Examples:

- `runtime/logs/phase_decision_log.jsonl`
- `runtime/logs/hold_log.jsonl`
- `runtime/logs/rejection_log.jsonl`
- `runtime/logs/breadcrumbs.jsonl`

### 2.3 Runtime summary surface

Use this surface for:

- current phase
- latest active line snapshot
- candidate scope summary
- active hold summary
- watch status summary

Examples:

- `runtime/current_phase.json`
- `runtime/manifests/pipeline_candidate_scope_summary.json`
- `runtime/manifests/latent_line_registry_v1.json`

### 2.4 Evaluator surface

Use this surface for:

- phase evaluation
- line scoring
- candidate watch evaluation
- trace completeness checks
- placement checks

Examples:

- `evaluate_phase_transition()`
- `line_score_evaluator()`
- `evaluate_candidate_watch()`
- `verify_required_fields()`

## 3. Placement rules

### 3.1 Definitions do not live in runtime mutation paths

If a file is defining what something means, it belongs in a baseline or note surface, not in a mutable runtime artifact.

### 3.2 Events do not become summaries

Append-only logs capture what happened.
They do not replace current-state summary artifacts.

### 3.3 Summaries do not replace logs

Runtime summary surfaces are derived.
The append-only log remains the truth source for reread.

### 3.4 Evaluators do not own storage truth

Evaluators compute decisions.
They do not become the archive itself.

### 3.5 Placement must match lifecycle

Do not place a concept where it cannot be reread correctly later.

## 4. Concept-to-placement examples

### 4.1 latent line

Preferred placement:

- baseline definition
- evaluator output
- runtime snapshot

Do not place as:

- direct mutable entity that is treated as source truth

### 4.2 breadcrumb

Preferred placement:

- append-only log
- summary surface

Do not place as:

- console-only output
- transient debug print

### 4.3 phase decision

Preferred placement:

- evaluator output
- append-only decision log
- runtime current phase summary

Do not place as:

- manual enum overwrite as sole source of truth

### 4.4 hold

Preferred placement:

- append-only hold log
- runtime hold summary

Do not place as:

- fallback branch
- TODO placeholder

### 4.5 rejection

Preferred placement:

- append-only rejection log
- review summary surface

Do not place as:

- error log
- ad hoc note

### 4.6 candidate

Preferred placement:

- candidate registry
- scope summary
- watch linkage records

Do not place as:

- immediate hard-coded implementation rule

## 5. Placement smell checklist

Watch for these smells:

- a definition baseline starts storing live runtime truth
- a log file starts acting as the canonical current state
- a summary file becomes the only archive
- evaluator logic is embedded directly in storage files
- a concept is placed into a surface that cannot reread it later

## 6. Relationship to other baselines

This baseline works with:

- `concept_to_implementation_map_baseline_v0`
- `build_drift_anchor_baseline_v0`
- `implementation_eval_criteria_baseline_v0`

The sequence is:

1. Map the concept to an implementation unit.
2. Anchor the build intent.
3. Place the artifact in the correct lifecycle surface.
4. Evaluate whether the implementation preserved the structure and intent.

## 7. One-line conclusion

> implementation placement is the rule that keeps definitions, logs, summaries, and evaluators in the surfaces where they can be reread and judged correctly later.
