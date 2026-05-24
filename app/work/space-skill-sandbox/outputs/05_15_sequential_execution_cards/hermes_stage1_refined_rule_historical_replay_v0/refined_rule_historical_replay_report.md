# Refined Rule Historical Replay Report v0

## 1. Verdict

[CODEX_STAGE1_REFINED_RULE_HISTORICAL_REPLAY_EXECUTED_WITH_WATCH]

## 2. Command

`python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_rule_historical_replay_v0/replay_refined_rules_on_historical_patches.py`

## 3. Files Read

- hermes_stage1_historical_code_diff_sample_audit_v0/patches/4601f7c18.patch
- hermes_stage1_historical_code_diff_sample_audit_v0/patches/4e0389a4d.patch
- hermes_stage1_historical_code_diff_sample_audit_v0/patches/a542716f3.patch
- hermes_stage1_historical_code_diff_sample_audit_v0/patches/a998543da.patch

## 4. Aggregate Replay

- old_hard_findings_estimate: 5
- old_review_notes_estimate: 29
- refined_hard_findings: 1
- refined_review_notes: 30
- hard_finding_delta: -4

## 5. Per Patch Results

### 4601f7c18.patch
- files_touched_count: 2
- old_hard_findings_estimate: 0
- refined_hard_findings: 0
- refined_review_notes: 0

### 4e0389a4d.patch
- files_touched_count: 5
- old_hard_findings_estimate: 1
- refined_hard_findings: 1
- refined_review_notes: 2
- review_note | old=review_note | rule=unresolved_todo | reason=non_secret_rule_unchanged | app/runtime/vectorfl_integrated_engine_api.py:651 | `"current_signal": "extract repeated pressure before TODO language",`
- review_note | old=review_note | rule=secret_boundary | reason=secret_word_without_direct_assignment | app/runtime/vectorfl_integrated_engine_api.py:1769 | `if any(token in explicit_tail for token in tokens):`
- hard_finding | old=hard_finding | rule=debug_print_js | reason=non_secret_rule_unchanged | app/ui/integrated_engine/main.tsx:3686 | `console.log("VectorFL Sandbox: Starting Boot Sequence...");`

### a542716f3.patch
- files_touched_count: 7
- old_hard_findings_estimate: 0
- refined_hard_findings: 0
- refined_review_notes: 3
- review_note | old=review_note | rule=secret_boundary | reason=secret_word_without_direct_assignment | app/core/runtime/lower_support_layers.py:226 | `token`
- review_note | old=review_note | rule=secret_boundary | reason=secret_word_without_direct_assignment | app/core/runtime/lower_support_layers.py:227 | `for token in tokens`
- review_note | old=review_note | rule=secret_boundary | reason=secret_word_without_direct_assignment | app/core/runtime/lower_support_layers.py:228 | `if token`
- none | old=review_note | rule=secret_boundary | reason=assignment_not_secret_named | app/core/runtime/lower_support_layers.py:351 | `repeated = [token for token, count in counter.most_common(5) if count >= 2]`

### a998543da.patch
- files_touched_count: 6
- old_hard_findings_estimate: 4
- refined_hard_findings: 0
- refined_review_notes: 25
- review_note | old=hard_finding | rule=secret_boundary | reason=semantic_or_env_boundary_not_literal_secret | app/core/runtime/live_input_space.py:5292 | `token = _normalize_token(value)`
- review_note | old=review_note | rule=secret_boundary | reason=secret_word_without_direct_assignment | app/core/runtime/live_input_space.py:5293 | `if token:`
- review_note | old=review_note | rule=secret_boundary | reason=secret_word_without_direct_assignment | app/core/runtime/live_input_space.py:5294 | `tokens.add(token)`
- review_note | old=hard_finding | rule=secret_boundary | reason=semantic_or_env_boundary_not_literal_secret | app/core/runtime/live_input_space.py:5296 | `token = _normalize_token(str(value).strip())`
- review_note | old=review_note | rule=secret_boundary | reason=secret_word_without_direct_assignment | app/core/runtime/live_input_space.py:5297 | `if token:`
- review_note | old=review_note | rule=secret_boundary | reason=secret_word_without_direct_assignment | app/core/runtime/live_input_space.py:5298 | `tokens.add(token)`
- review_note | old=review_note | rule=secret_boundary | reason=secret_word_without_direct_assignment | app/core/runtime/live_input_space.py:5309 | `for token in _collect_anchor_tokens(materials):`
- none | old=review_note | rule=secret_boundary | reason=assignment_not_secret_named | app/core/runtime/live_input_space.py:5310 | `kinds = _anchor_token_kinds(token)`
- review_note | old=review_note | rule=secret_boundary | reason=secret_word_without_direct_assignment | app/core/runtime/live_input_space.py:5312 | `profile["semantic"].add(token)`
- review_note | old=review_note | rule=secret_boundary | reason=secret_word_without_direct_assignment | app/core/runtime/live_input_space.py:5315 | `profile.setdefault(kind, set()).add(token)`
- review_note | old=review_note | rule=secret_boundary | reason=secret_word_without_direct_assignment | app/core/runtime/live_input_space.py:5319 | `def _anchor_token_kinds(token: str) -> Set[str]:`
- none | old=review_note | rule=secret_boundary | reason=assignment_not_secret_named | app/core/runtime/live_input_space.py:5320 | `lowered = _normalize_token(token)`

## 6. Recovered Judgment

- The refined secret/token rule lowers historical `_normalize_token(...)` examples from hard finding to review note.
- The `console.log(...)` app-source finding remains a hard finding.
- No component/workflow/skill/baseline authority is created by this replay.

## 7. VectorFL Recovery Suggestion

receipt:
  refined rule replay ran over the historical patch sample

residue:
  old-vs-refined delta and remaining false-positive/false-negative notes

candidate:
  refined diff-audit rule boundary is stronger

component:
  HOLD until the rule set is replayed against a broader real sample and a seeded true-positive set

STOP:
  patch/commit/skill/memory/cron/config/MCP/network/VectorFL authority mutation

## 8. HOLD

- no source files modified
- no prior audit files modified
- no patches applied
- no git used
- no package install
- no network / browser / MCP
- no Hermes memory / skill / cron / config edit
- no VectorFL authority update
- no baseline / workflow / schema / registry / ontology promotion
