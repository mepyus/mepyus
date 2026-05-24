# Secret/Token Rule Refinement Audit Report v0

## 1. Verdict

[CODEX_STAGE1_SECRET_RULE_REFINEMENT_AUDIT_EXECUTED_WITH_WATCH]

## 2. Command

`python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_secret_rule_refinement_audit_v0/audit_secret_rule_refinement.py`

## 3. Files Read

- fixtures/actual_credential_literal.patch
- fixtures/config_env_boundary.patch
- fixtures/docs_and_tests_examples.patch
- fixtures/historical_token_examples.patch
- fixtures/semantic_token_normalization.patch

## 4. Files Created

- fixtures/actual_credential_literal.patch
- fixtures/semantic_token_normalization.patch
- fixtures/config_env_boundary.patch
- fixtures/docs_and_tests_examples.patch
- fixtures/historical_token_examples.patch
- audit_secret_rule_refinement.py
- secret_rule_refinement_report.md
- secret_rule_refinement_receipt.json

## 5. Aggregate Behavior

- old_hard_findings: 18
- old_review_notes: 8
- refined_hard_findings: 9
- refined_review_notes: 20
- false_positive_reduction_against_old_hard_count: 9

## 6. Fixture Results

### actual_credential_literal.patch
- files_touched_count: 1
- added_lines_seen: 6
- old_hard_findings: 5
- refined_hard_findings: 5
- refined_review_notes: 0
- hard_finding | old=hard_finding | reason=literal_secret_assignment | app/runtime/secrets.py:6 | `api_key = "sk_live_example_123456"`
- hard_finding | old=hard_finding | reason=literal_secret_assignment | app/runtime/secrets.py:7 | `token = "secret-token-value"`
- hard_finding | old=hard_finding | reason=literal_secret_assignment | app/runtime/secrets.py:8 | `password = "plain-text"`
- hard_finding | old=hard_finding | reason=literal_secret_assignment | app/runtime/secrets.py:9 | `secret = "local-dev-secret"`
- hard_finding | old=hard_finding | reason=literal_secret_assignment | app/runtime/secrets.py:10 | `credential = "embedded-credential"`
- none | old=none | reason=assignment_not_secret_named | app/runtime/secrets.py:11 | `safe_value = read_from_env("SERVICE_TOKEN")`

### config_env_boundary.patch
- files_touched_count: 1
- added_lines_seen: 6
- old_hard_findings: 5
- refined_hard_findings: 3
- refined_review_notes: 3
- hard_finding | old=none | reason=literal_secret_assignment | config/service.env:6 | `SERVICE_TOKEN = "real-looking-secret"`
- hard_finding | old=hard_finding | reason=literal_secret_assignment | config/service.env:7 | `API_KEY = "real-looking-key"`
- review_note | old=hard_finding | reason=placeholder_or_empty_secret_value | config/service.env:8 | `PASSWORD = "${SERVICE_PASSWORD}"`
- review_note | old=hard_finding | reason=placeholder_or_empty_secret_value | config/service.env:9 | `TOKEN = "<set-in-env>"`
- hard_finding | old=hard_finding | reason=literal_secret_assignment | config/service.env:10 | `SECRET = "example-secret"`
- review_note | old=hard_finding | reason=placeholder_or_empty_secret_value | config/service.env:11 | `CREDENTIAL = ""`

### docs_and_tests_examples.patch
- files_touched_count: 2
- added_lines_seen: 8
- old_hard_findings: 0
- refined_hard_findings: 0
- refined_review_notes: 8
- review_note | old=review_note | reason=secret_word_without_direct_assignment | docs/secret_examples.md:6 | `Use API_KEY = "example-key" only as documentation.`
- review_note | old=review_note | reason=secret_word_without_direct_assignment | docs/secret_examples.md:7 | `Do not set token = "secret-token-value" in source.`
- review_note | old=review_note | reason=docs_example | docs/secret_examples.md:8 | `password = "placeholder"`
- review_note | old=review_note | reason=tests_or_fixtures_example | tests/fixtures/test_secret_fixture.py:14 | `api_key = "sk_live_test_fixture"`
- review_note | old=review_note | reason=tests_or_fixtures_example | tests/fixtures/test_secret_fixture.py:15 | `token = "fixture-token"`
- review_note | old=review_note | reason=tests_or_fixtures_example | tests/fixtures/test_secret_fixture.py:16 | `password = "fixture-password"`
- review_note | old=review_note | reason=tests_or_fixtures_example | tests/fixtures/test_secret_fixture.py:17 | `secret = "fixture-secret"`
- review_note | old=review_note | reason=tests_or_fixtures_example | tests/fixtures/test_secret_fixture.py:18 | `credential = "fixture-credential"`

### historical_token_examples.patch
- files_touched_count: 1
- added_lines_seen: 8
- old_hard_findings: 5
- refined_hard_findings: 1
- refined_review_notes: 5
- review_note | old=hard_finding | reason=semantic_or_env_boundary_not_literal_secret | app/core/runtime/live_input_space.py:6 | `token = _normalize_token(value)`
- review_note | old=hard_finding | reason=semantic_or_env_boundary_not_literal_secret | app/core/runtime/live_input_space.py:7 | `token = _normalize_token(str(value).strip())`
- review_note | old=hard_finding | reason=semantic_or_env_boundary_not_literal_secret | app/core/runtime/live_input_space.py:8 | `token = _normalize_token(value)`
- review_note | old=hard_finding | reason=semantic_or_env_boundary_not_literal_secret | app/core/runtime/live_input_space.py:9 | `token = _normalize_token(str(value).strip())`
- hard_finding | old=hard_finding | reason=literal_secret_assignment | app/core/runtime/live_input_space.py:12 | `token = "not-a-normalizer-literal"`
- review_note | old=none | reason=semantic_or_env_boundary_not_literal_secret | app/core/runtime/live_input_space.py:13 | `API_TOKEN = os.environ["API_TOKEN"]`

### semantic_token_normalization.patch
- files_touched_count: 1
- added_lines_seen: 8
- old_hard_findings: 3
- refined_hard_findings: 0
- refined_review_notes: 4
- review_note | old=hard_finding | reason=semantic_or_env_boundary_not_literal_secret | app/core/runtime/tokenizer.py:7 | `token = _normalize_token(value)`
- review_note | old=hard_finding | reason=semantic_or_env_boundary_not_literal_secret | app/core/runtime/tokenizer.py:8 | `token = _normalize_token(str(value).strip())`
- review_note | old=none | reason=secret_word_without_direct_assignment | app/core/runtime/tokenizer.py:10 | `for token in sentence_tokens:`
- review_note | old=hard_finding | reason=semantic_or_env_boundary_not_literal_secret | app/core/runtime/tokenizer.py:11 | `token = token.lower()`

## 7. Historical Example Comparison

- old=hard_finding -> refined=review_note | reason=semantic_or_env_boundary_not_literal_secret | `token = _normalize_token(value)`
- old=hard_finding -> refined=review_note | reason=semantic_or_env_boundary_not_literal_secret | `token = _normalize_token(str(value).strip())`
- old=hard_finding -> refined=review_note | reason=semantic_or_env_boundary_not_literal_secret | `token = _normalize_token(value)`
- old=hard_finding -> refined=review_note | reason=semantic_or_env_boundary_not_literal_secret | `token = _normalize_token(str(value).strip())`
- old=hard_finding -> refined=hard_finding | reason=literal_secret_assignment | `token = "not-a-normalizer-literal"`
- old=none -> refined=review_note | reason=semantic_or_env_boundary_not_literal_secret | `API_TOKEN = os.environ["API_TOKEN"]`

## 8. Recovered Rule Boundary

- Quoted literal secret-like assignments in app/source/config remain hard findings.
- Placeholder/env/reference values are review notes, not hard findings.
- `_normalize_token(...)`, parser-token variables, and derived token lists are semantic token handling, not credential leakage by themselves.
- Docs and test fixtures stay as review notes unless a separate authority boundary says they are live secrets.
- Config/env-like literal secrets keep hard-finding pressure.

## 9. False Positive / False Negative Notes

- False-positive reduced: the historical `_normalize_token(...)` examples no longer become hard findings.
- False-negative watch: a real secret can still be hidden behind variable indirection, concatenation, decoding, or environment reads.
- This script does not perform data-flow analysis, entropy checks, git history secret scanning, or runtime reachability analysis.

## 10. VectorFL Recovery Suggestion

receipt:
  refinement audit ran with command/output evidence

residue:
  observed false-positive and false-negative boundaries

candidate:
  refined secret/token rule boundary

component:
  HOLD until tested against more real diffs and at least one deliberately seeded true-positive case

STOP:
  patch/commit/skill/memory/cron/config/MCP/network/VectorFL authority mutation

## 11. WATCH

refined secret/token rules may reduce false positives but still do not authorize component/workflow/skill/baseline

## 12. HOLD

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
