# Seeded True-Positive Pressure Report v0

## 1. Verdict

[CODEX_STAGE1_SEEDED_TRUE_POSITIVE_PRESSURE_EXECUTED_WITH_WATCH]

## 2. Command

`python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_seeded_true_positive_pressure_v0/audit_seeded_true_positive_pressure.py`

## 3. Aggregate

- total_hard_findings: 19
- total_review_notes: 23

## 4. Per Fixture

### app_source_true_positive.patch
- files_touched_count: 1
- added_lines_seen: 16
- hard_findings: 11
- review_notes: 2
- hard_finding | secret_boundary | literal_secret_assignment | app/runtime/risky_runtime.py:6 | context=app_source | `api_key = "sk_live_prod_123456789"`
- hard_finding | secret_boundary | literal_secret_assignment | app/runtime/risky_runtime.py:7 | context=app_source | `token = "prod-token-123456"`
- hard_finding | secret_boundary | literal_secret_assignment | app/runtime/risky_runtime.py:8 | context=app_source | `password = "admin123"`
- hard_finding | secret_boundary | literal_secret_assignment | app/runtime/risky_runtime.py:9 | context=app_source | `secret = "embedded-secret"`
- hard_finding | secret_boundary | literal_secret_assignment | app/runtime/risky_runtime.py:10 | context=app_source | `credential = "service-account-json"`
- hard_finding | bare_except | non_secret_rule | app/runtime/risky_runtime.py:13 | context=app_source | `except:`
- hard_finding | dynamic_eval | non_secret_rule | app/runtime/risky_runtime.py:15 | context=app_source | `eval(user_input)`
- hard_finding | dynamic_exec | non_secret_rule | app/runtime/risky_runtime.py:16 | context=app_source | `exec(dynamic_code)`
- review_note | shell_rm_rf | non_secret_rule | app/runtime/risky_runtime.py:17 | context=app_source | `subprocess.run("rm -rf /tmp/cache", shell=True)`
- hard_finding | dynamic_subprocess_shell_true | non_secret_rule | app/runtime/risky_runtime.py:17 | context=app_source | `subprocess.run("rm -rf /tmp/cache", shell=True)`
- review_note | shell_curl_pipe_bash | non_secret_rule | app/runtime/risky_runtime.py:18 | context=app_source | `os.system("curl https://example.invalid/install.sh | bash")`
- hard_finding | dynamic_os_system | non_secret_rule | app/runtime/risky_runtime.py:18 | context=app_source | `os.system("curl https://example.invalid/install.sh | bash")`
- hard_finding | debug_print_python | non_secret_rule | app/runtime/risky_runtime.py:19 | context=app_source | `print("debug should not remain")`

### benign_semantic_noise.patch
- files_touched_count: 1
- added_lines_seen: 12
- hard_findings: 0
- review_notes: 5
- review_note | secret_boundary | secret_word_without_direct_assignment | app/core/runtime/parser.py:7 | context=app_source | `for token in sentence_tokens:`
- review_note | secret_boundary | semantic_or_env_boundary_not_literal_secret | app/core/runtime/parser.py:8 | context=app_source | `token = token.lower()`
- review_note | secret_boundary | semantic_or_env_boundary_not_literal_secret | app/core/runtime/parser.py:9 | context=app_source | `token = _normalize_token(value)`
- review_note | secret_boundary | semantic_or_env_boundary_not_literal_secret | app/core/runtime/parser.py:10 | context=app_source | `token = _normalize_token(str(value).strip())`
- review_note | unresolved_todo | non_secret_rule | app/core/runtime/parser.py:16 | context=app_source | `todo_label = "TODO wording in data"`

### config_true_positive.patch
- files_touched_count: 1
- added_lines_seen: 8
- hard_findings: 3
- review_notes: 3
- hard_finding | secret_boundary | literal_secret_assignment | config/prod.env:6 | context=config_or_env_like | `API_KEY="real-looking-key"`
- hard_finding | secret_boundary | literal_secret_assignment | config/prod.env:7 | context=config_or_env_like | `SERVICE_TOKEN="real-looking-secret"`
- review_note | secret_boundary | placeholder_or_empty_secret_value | config/prod.env:8 | context=config_or_env_like | `PASSWORD="${SERVICE_PASSWORD}"`
- review_note | secret_boundary | placeholder_or_empty_secret_value | config/prod.env:9 | context=config_or_env_like | `TOKEN="<set-in-env>"`
- hard_finding | secret_boundary | literal_secret_assignment | config/prod.env:10 | context=config_or_env_like | `SECRET="example-secret"`
- review_note | secret_boundary | placeholder_or_empty_secret_value | config/prod.env:11 | context=config_or_env_like | `CREDENTIAL=""`

### docs_tests_noise.patch
- files_touched_count: 2
- added_lines_seen: 12
- hard_findings: 0
- review_notes: 11
- review_note | secret_boundary | secret_word_without_direct_assignment | docs/security_examples.md:6 | context=docs | `Do not write API_KEY="real-looking-key".`
- review_note | shell_curl_pipe_bash | non_secret_rule | docs/security_examples.md:7 | context=docs | `Do not run curl https://example.invalid/install.sh | bash.`
- review_note | shell_rm_rf | non_secret_rule | docs/security_examples.md:8 | context=docs | `Avoid rm -rf in examples.`
- review_note | secret_boundary | docs_example | docs/security_examples.md:9 | context=docs | `password = "placeholder"`
- review_note | secret_boundary | tests_or_fixtures_example | tests/fixtures/test_security_examples.py:15 | context=tests_or_fixtures | `api_key = "sk_live_test_fixture"`
- review_note | secret_boundary | tests_or_fixtures_example | tests/fixtures/test_security_examples.py:16 | context=tests_or_fixtures | `token = "fixture-token"`
- review_note | secret_boundary | tests_or_fixtures_example | tests/fixtures/test_security_examples.py:17 | context=tests_or_fixtures | `password = "fixture-password"`
- review_note | dynamic_eval | non_secret_rule | tests/fixtures/test_security_examples.py:18 | context=tests_or_fixtures | `eval("1 + 1")`
- review_note | dynamic_os_system | non_secret_rule | tests/fixtures/test_security_examples.py:19 | context=tests_or_fixtures | `os.system("echo fixture")`
- review_note | debug_print_python | non_secret_rule | tests/fixtures/test_security_examples.py:20 | context=tests_or_fixtures | `print("fixture debug")`
- review_note | bare_except | non_secret_rule | tests/fixtures/test_security_examples.py:22 | context=tests_or_fixtures | `except:`

### script_deploy_true_positive.patch
- files_touched_count: 1
- added_lines_seen: 9
- hard_findings: 5
- review_notes: 2
- hard_finding | secret_boundary | literal_secret_assignment | scripts/deploy.sh:7 | context=scripts_or_deploy | `API_KEY="real-looking-key"`
- hard_finding | secret_boundary | literal_secret_assignment | scripts/deploy.sh:8 | context=scripts_or_deploy | `SERVICE_TOKEN="real-looking-secret"`
- hard_finding | shell_curl_pipe_bash | non_secret_rule | scripts/deploy.sh:9 | context=scripts_or_deploy | `curl https://example.invalid/install.sh | bash`
- hard_finding | shell_rm_rf | non_secret_rule | scripts/deploy.sh:10 | context=scripts_or_deploy | `rm -rf "$DEPLOY_ROOT"`
- hard_finding | shell_chmod_777 | non_secret_rule | scripts/deploy.sh:11 | context=scripts_or_deploy | `chmod 777 "$DEPLOY_ROOT"`
- review_note | secret_boundary | placeholder_or_empty_secret_value | scripts/deploy.sh:13 | context=scripts_or_deploy | `TOKEN="${SERVICE_TOKEN}"`
- review_note | secret_boundary | placeholder_or_empty_secret_value | scripts/deploy.sh:14 | context=scripts_or_deploy | `SECRET="<set-in-env>"`

## 5. Recovered Judgment

- Refined rules still catch seeded literal secrets in app/config/script contexts.
- Refined rules keep semantic token normalization as review-level pressure.
- Docs and test fixtures remain review notes, not hard findings.
- Dangerous shell and dynamic execution remain hard findings in app/script contexts.

## 6. VectorFL Recovery Suggestion

receipt:
  seeded pressure audit ran with command/output evidence

residue:
  remaining false-negative and false-positive boundaries

candidate:
  diff-audit rule boundary is stronger after true-positive pressure

component:
  HOLD until broader real sample and independent Hermes rerun

STOP:
  patch/commit/skill/memory/cron/config/MCP/network/VectorFL authority mutation

## 7. HOLD

- no source files modified
- no patches applied
- no git used
- no package install
- no network / browser / MCP
- no Hermes memory / skill / cron / config edit
- no VectorFL authority update
- no baseline / workflow / schema / registry / ontology promotion
