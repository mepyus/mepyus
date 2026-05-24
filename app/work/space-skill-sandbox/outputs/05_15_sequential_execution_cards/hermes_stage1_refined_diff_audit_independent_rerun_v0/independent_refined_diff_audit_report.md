# Hermes Stage 1 Refined Diff Audit Independent Rerun Report v0

## Verdict

[HERMES_STAGE1_REFINED_DIFF_AUDIT_INDEPENDENT_RERUN_EXECUTED_WITH_WATCH]

## Command Run

`python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_diff_audit_independent_rerun_v0/independent_refined_diff_audit.py`

## Files Read

- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/patches/
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_seeded_true_positive_pressure_v0/fixtures/
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_secret_rule_refinement_audit_v0/secret_rule_refinement_report.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_rule_historical_replay_v0/refined_rule_historical_replay_report.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_seeded_true_positive_pressure_v0/seeded_true_positive_pressure_report.md
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

- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_diff_audit_independent_rerun_v0/independent_refined_diff_audit.py
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_diff_audit_independent_rerun_v0/independent_refined_diff_audit_report.md
- app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_diff_audit_independent_rerun_v0/independent_refined_diff_audit_receipt.json

## Historical Patch Results

### 4601f7c18.patch
- files_touched_count: 2
- added_lines_seen: 138
- deleted_lines_seen: 25
- hard_findings: 0
- review_notes: 0
- contexts: `{"app_source": 2}`
- hard finding examples:
- none
- review note examples:
- none

### 4e0389a4d.patch
- files_touched_count: 5
- added_lines_seen: 3714
- deleted_lines_seen: 0
- hard_findings: 1
- review_notes: 5
- contexts: `{"app_source": 4, "config_or_env_like": 1}`
- hard finding examples:
- hard_finding | debug_print_js | app_source_non_secret_rule | app/ui/integrated_engine/main.tsx:3686 | context=app_source | `console.log("VectorFL Sandbox: Starting Boot Sequence...");`
- review note examples:
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/runtime/vectorfl_integrated_engine_api.py:160 | context=app_source | `PATH_TOKEN_RE = re.compile(r"(?:(?:runtime|docs|app|scripts|references|gemini)/[A-Za-z0-9._@%+=:,/\\-]+)")`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/runtime/vectorfl_integrated_engine_api.py:186 | context=app_source | `for match in PATH_TOKEN_RE.findall(text):`
- review_note | unresolved_todo | unresolved_marker | app/runtime/vectorfl_integrated_engine_api.py:651 | context=app_source | `"current_signal": "extract repeated pressure before TODO language",`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/runtime/vectorfl_integrated_engine_api.py:1763 | context=app_source | `for candidate, tokens in (`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/runtime/vectorfl_integrated_engine_api.py:1769 | context=app_source | `if any(token in explicit_tail for token in tokens):`

### a542716f3.patch
- files_touched_count: 7
- added_lines_seen: 1333
- deleted_lines_seen: 8
- hard_findings: 0
- review_notes: 11
- contexts: `{"app_source": 7}`
- hard finding examples:
- none
- review note examples:
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/lower_support_layers.py:223 | context=app_source | `def _tokenize(text: str) -> list[str]:`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/lower_support_layers.py:224 | context=app_source | `tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_-]{2,}|[가-힣]{2,}", text.lower())`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/lower_support_layers.py:226 | context=app_source | `token`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/lower_support_layers.py:227 | context=app_source | `for token in tokens`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/lower_support_layers.py:228 | context=app_source | `if token`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/lower_support_layers.py:347 | context=app_source | `def _dominant_tokens(texts: list[str]) -> list[str]:`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/lower_support_layers.py:350 | context=app_source | `counter.update(_tokenize(text))`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/lower_support_layers.py:351 | context=app_source | `repeated = [token for token, count in counter.most_common(5) if count >= 2]`

### a998543da.patch
- files_touched_count: 6
- added_lines_seen: 11322
- deleted_lines_seen: 0
- hard_findings: 0
- review_notes: 102
- contexts: `{"app_source": 3, "scripts_or_deploy": 1, "tests_or_fixtures": 2}`
- hard finding examples:
- none
- review note examples:
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/live_input_space.py:4310 | context=app_source | `canonicalizable_token_pair_count=int(promotion_review_data.get("canonicalizable_token_pair_count", 0) or 0),`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/live_input_space.py:5045 | context=app_source | `canonicalizable_token_pair_count=int(direct_overlap_review.get("canonicalizable_token_pair_count", 0) or 0),`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/live_input_space.py:5059 | context=app_source | `canonicalizable_token_pair_count=int(direct_overlap_review.get("canonicalizable_token_pair_count", 0) or 0),`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/live_input_space.py:5171 | context=app_source | `overlap_tokens = set(semantic_overlap + structural_overlap + process_overlap + object_overlap)`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/live_input_space.py:5172 | context=app_source | `translated_but_not_canonicalized_count = len([value for value in translated_hits if value not in overlap_tokens])`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/live_input_space.py:5232 | context=app_source | `_normalize_token(str(value).strip())`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/live_input_space.py:5282 | context=app_source | `def _collect_anchor_tokens(materials: Sequence[Dict[str, object]]) -> Set[str]:`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/live_input_space.py:5283 | context=app_source | `tokens: Set[str] = set()`

## Seeded Fixture Results

### app_source_true_positive.patch
- files_touched_count: 1
- added_lines_seen: 16
- deleted_lines_seen: 0
- hard_findings: 11
- review_notes: 4
- contexts: `{"app_source": 1}`
- hard finding examples:
- hard_finding | secret_boundary | literal_secret_assignment | app/runtime/risky_runtime.py:6 | context=app_source | `api_key = [REDACTED]`
- hard_finding | secret_boundary | literal_secret_assignment | app/runtime/risky_runtime.py:7 | context=app_source | `token = [REDACTED]`
- hard_finding | secret_boundary | literal_secret_assignment | app/runtime/risky_runtime.py:8 | context=app_source | `password = [REDACTED]`
- hard_finding | secret_boundary | literal_secret_assignment | app/runtime/risky_runtime.py:9 | context=app_source | `secret = [REDACTED]`
- hard_finding | secret_boundary | literal_secret_assignment | app/runtime/risky_runtime.py:10 | context=app_source | `credential = [REDACTED]`
- hard_finding | bare_except | app_source_non_secret_rule | app/runtime/risky_runtime.py:13 | context=app_source | `except:`
- hard_finding | dynamic_eval | app_source_non_secret_rule | app/runtime/risky_runtime.py:15 | context=app_source | `eval(user_input)`
- hard_finding | dynamic_exec | app_source_non_secret_rule | app/runtime/risky_runtime.py:16 | context=app_source | `exec(dynamic_code)`
- review note examples:
- review_note | shell_rm_rf | shell_pattern_outside_script_deploy | app/runtime/risky_runtime.py:17 | context=app_source | `subprocess.run("rm -rf /tmp/cache", shell=True)`
- review_note | shell_curl_pipe_bash | shell_pattern_outside_script_deploy | app/runtime/risky_runtime.py:18 | context=app_source | `os.system("curl https://example.invalid/install.sh | bash")`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/runtime/risky_runtime.py:20 | context=app_source | `safe_token = _normalize_token(value)`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/runtime/risky_runtime.py:21 | context=app_source | `safe_ref = os.environ["SERVICE_TOKEN"]`

### benign_semantic_noise.patch
- files_touched_count: 1
- added_lines_seen: 12
- deleted_lines_seen: 0
- hard_findings: 0
- review_notes: 11
- contexts: `{"app_source": 1}`
- hard finding examples:
- none
- review note examples:
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/parser.py:6 | context=app_source | `def parse(sentence_tokens, values):`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/parser.py:7 | context=app_source | `for token in sentence_tokens:`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/parser.py:8 | context=app_source | `token = token.lower()`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/parser.py:9 | context=app_source | `token = _normalize_token(value)`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/parser.py:10 | context=app_source | `token = _normalize_token(str(value).strip())`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/parser.py:11 | context=app_source | `tokens = {_normalize_token(v) for v in values}`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/parser.py:12 | context=app_source | `api_key_name = "field name, not credential"`
- review_note | secret_boundary | semantic_or_env_or_secret_word_without_literal_assignment | app/core/runtime/parser.py:13 | context=app_source | `password_label = "label only"`

### config_true_positive.patch
- files_touched_count: 1
- added_lines_seen: 8
- deleted_lines_seen: 0
- hard_findings: 3
- review_notes: 3
- contexts: `{"config_or_env_like": 1}`
- hard finding examples:
- hard_finding | secret_boundary | literal_secret_assignment | config/prod.env:6 | context=config_or_env_like | `API_KEY = [REDACTED]`
- hard_finding | secret_boundary | literal_secret_assignment | config/prod.env:7 | context=config_or_env_like | `SERVICE_TOKEN = [REDACTED]`
- hard_finding | secret_boundary | literal_secret_assignment | config/prod.env:10 | context=config_or_env_like | `SECRET = [REDACTED]`
- review note examples:
- review_note | secret_boundary | placeholder_or_env_secret_value | config/prod.env:8 | context=config_or_env_like | `PASSWORD = [REDACTED]`
- review_note | secret_boundary | placeholder_or_env_secret_value | config/prod.env:9 | context=config_or_env_like | `TOKEN = [REDACTED]`
- review_note | secret_boundary | placeholder_or_env_secret_value | config/prod.env:11 | context=config_or_env_like | `CREDENTIAL = [REDACTED]`

### docs_tests_noise.patch
- files_touched_count: 2
- added_lines_seen: 12
- deleted_lines_seen: 0
- hard_findings: 0
- review_notes: 11
- contexts: `{"docs": 1, "tests_or_fixtures": 1}`
- hard finding examples:
- none
- review note examples:
- review_note | secret_boundary | docs_tests_fixtures_secret_example | docs/security_examples.md:6 | context=docs | `Do not write API_KEY = [REDACTED].`
- review_note | shell_curl_pipe_bash | docs_tests_fixtures_non_secret_pattern | docs/security_examples.md:7 | context=docs | `Do not run curl https://example.invalid/install.sh | bash.`
- review_note | shell_rm_rf | docs_tests_fixtures_non_secret_pattern | docs/security_examples.md:8 | context=docs | `Avoid rm -rf in examples.`
- review_note | secret_boundary | docs_tests_fixtures_secret_example | docs/security_examples.md:9 | context=docs | `password = [REDACTED]`
- review_note | secret_boundary | docs_tests_fixtures_secret_example | tests/fixtures/test_security_examples.py:15 | context=tests_or_fixtures | `api_key = [REDACTED]`
- review_note | secret_boundary | docs_tests_fixtures_secret_example | tests/fixtures/test_security_examples.py:16 | context=tests_or_fixtures | `token = [REDACTED]`
- review_note | secret_boundary | docs_tests_fixtures_secret_example | tests/fixtures/test_security_examples.py:17 | context=tests_or_fixtures | `password = [REDACTED]`
- review_note | dynamic_eval | docs_tests_fixtures_non_secret_pattern | tests/fixtures/test_security_examples.py:18 | context=tests_or_fixtures | `eval("1 + 1")`

### script_deploy_true_positive.patch
- files_touched_count: 1
- added_lines_seen: 9
- deleted_lines_seen: 0
- hard_findings: 5
- review_notes: 2
- contexts: `{"scripts_or_deploy": 1}`
- hard finding examples:
- hard_finding | secret_boundary | literal_secret_assignment | scripts/deploy.sh:7 | context=scripts_or_deploy | `API_KEY = [REDACTED]`
- hard_finding | secret_boundary | literal_secret_assignment | scripts/deploy.sh:8 | context=scripts_or_deploy | `SERVICE_TOKEN = [REDACTED]`
- hard_finding | shell_curl_pipe_bash | script_shell_or_destructive_command | scripts/deploy.sh:9 | context=scripts_or_deploy | `curl https://example.invalid/install.sh | bash`
- hard_finding | shell_rm_rf | script_shell_or_destructive_command | scripts/deploy.sh:10 | context=scripts_or_deploy | `rm -rf "$DEPLOY_ROOT"`
- hard_finding | shell_chmod_777 | script_shell_or_destructive_command | scripts/deploy.sh:11 | context=scripts_or_deploy | `chmod 777 "$DEPLOY_ROOT"`
- review note examples:
- review_note | secret_boundary | placeholder_or_env_secret_value | scripts/deploy.sh:13 | context=scripts_or_deploy | `TOKEN = [REDACTED]`
- review_note | secret_boundary | placeholder_or_env_secret_value | scripts/deploy.sh:14 | context=scripts_or_deploy | `SECRET = [REDACTED]`

## Aggregate Counts

- historical_hard_findings: 1
- historical_review_notes: 118
- seeded_hard_findings: 19
- seeded_review_notes: 31
- aggregate_hard_findings: 20
- aggregate_review_notes: 149

## Rule Hits

- bare_except: hard_finding=1, review_note=1
- debug_print_js: hard_finding=1, review_note=0
- debug_print_python: hard_finding=1, review_note=3
- dynamic_eval: hard_finding=1, review_note=1
- dynamic_exec: hard_finding=1, review_note=0
- dynamic_os_system: hard_finding=1, review_note=1
- dynamic_subprocess_shell_true: hard_finding=1, review_note=0
- secret_boundary: hard_finding=10, review_note=137
- shell_chmod_777: hard_finding=1, review_note=0
- shell_curl_pipe_bash: hard_finding=1, review_note=2
- shell_rm_rf: hard_finding=1, review_note=2
- unresolved_todo: hard_finding=0, review_note=2

## Differences From Codex Replay

- historical_hard_findings matched Codex replay target: 1
- seeded aggregate differs from Codex replay target 19/23: observed 19/31
- historical_review_notes differs from prior replay 30: observed 118; likely independent rule implementation/counting boundary variation

## False-Positive Notes

- Semantic token normalization and token iteration are review notes, not hard findings.
- Docs/tests/fixtures examples stay review notes even when they contain secret-looking or dynamic-execution strings.
- String/path-context detection cannot prove whether a literal value is a real live credential; secret-like excerpts are redacted.

## False-Negative Notes

- This rerun does not perform entropy scanning, data-flow analysis, runtime reachability, dependency analysis, or git history secret scanning.
- Literal secret detection can miss concatenated, encoded, or indirectly loaded values.
- Anchored print/eval/exec detection intentionally avoids string-only noise and may miss obfuscated calls.

## VectorFL Recovery Suggestion

receipt:
  Hermes independently reran refined diff audit with command/output evidence

residue:
  count differences, false-positive notes, false-negative notes

candidate:
  refined diff-audit rule set becomes stronger if behavior matches Codex replay

component:
  HOLD until broader real sample and user/Codex explicit approval

STOP:
  patch/commit/skill/memory/cron/config/MCP/network/VectorFL authority mutation

## WATCH

independent rerun may strengthen candidate status but still does not authorize component/workflow/skill/baseline

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

## Hard Stop Confirmation

No mutation, promotion, persistence, git, network, browser, MCP, package install, cron, memory, skill, config, or VectorFL authority action was performed.
