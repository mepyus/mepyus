# Hermes Stage 1 Secret Rule Refinement Audit Packet v0

Copy this whole prompt into the active Hermes terminal.

---

You are Hermes Agent acting as a native local execution workbench candidate for VectorFL.

This is a **Stage 1 local secret-rule refinement audit**.

Use this packet in Hermes, not Gemini.

Core principle:

```text
Let Hermes act natively.
Let VectorFL recover selectively.
```

## 1. Purpose

The previous historical code-diff sample audit found:

```text
total_hard_findings: 5
debug_print_js: 1
secret_token_assignment: 4
```

The key uncertainty is this:

```text
token = _normalize_token(value)
token = _normalize_token(str(value).strip())
```

These lines were classified as hard findings because they match `token =`.
But they may be semantic token normalization variables, not credential leakage.

This test should refine the rule boundary between:

```text
credential literal assignment
semantic token variable / parser normalization
test fixture credential example
docs/example credential text
config/env credential-like field
```

This is not a component.
This is not a workflow.
This is not a skill.
This is not VectorFL authority update.

## 2. Source Materials to Read

Read only these existing files first:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/historical_code_diff_audit_report.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/historical_code_diff_audit_receipt.json
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/audit_historical_code_diffs.py
```

You may also read only these patch files:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/patches/a998543da.patch
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/patches/4e0389a4d.patch
```

Do not perform broad repo search.
Do not inspect live source files.
Do not use git.

## 3. Hard Boundary

Do not:

```text
modify source files
modify prior audit files
modify prior patch files
apply patches
run git
run git add
run git commit
run git reset
run git checkout
move existing files
install packages
use network
call browser
call MCP
connect to external apps
send messages
create cron
edit ~/.hermes/cron/jobs.json
write Hermes memory
create or edit Hermes skill
change Hermes config
update AGENTS.md
create SKILL.md
update VectorFL files outside the declared output directory
update current-position
update output_manifest
promote anything to baseline/workflow/schema/registry/ontology
write outside the declared output directory
```

Allowed:

```text
create one declared sandbox output directory
copy or synthesize small fixture patches under that output directory
write one Python stdlib-only refinement audit script
run that script once
write one markdown report
write one JSON receipt
print a concise terminal summary
```

## 4. Output Directory

Create and write only under:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_secret_rule_refinement_audit_v0/
```

Allowed output files/directories:

```text
fixtures/
audit_secret_rule_refinement.py
secret_rule_refinement_report.md
secret_rule_refinement_receipt.json
```

Inside `fixtures/`, write only small `.patch` fixtures for this test.

## 5. Fixture Design

Create small diff fixtures that pressure the boundary:

### A. Actual Credential Literal

Should be hard finding:

```text
api_key = "sk_live_example"
token = "secret-token-value"
password = "plain-text"
```

### B. Semantic Token Normalization

Should be review note or no finding, not hard finding:

```text
token = _normalize_token(value)
token = _normalize_token(str(value).strip())
normalized_tokens = [_normalize_token(v) for v in values]
```

### C. Parser / NLP Token Variable

Should be review note or no finding, not hard finding:

```text
for token in sentence_tokens:
    token = token.lower()
```

### D. Config / Env-Like Credential Field

Should be hard finding if literal value is assigned:

```text
SERVICE_TOKEN = "real-looking-secret"
API_KEY = "real-looking-key"
```

Should be review note if placeholder:

```text
SERVICE_TOKEN = "${SERVICE_TOKEN}"
API_KEY = "<set-in-env>"
```

### E. Test / Fixture Credential Example

Should be review note unless it looks like a real secret and is outside test/docs context.

### F. Docs Example

Should be review note, not hard finding.

## 6. Rule Refinement Expectation

Implement a refined stdlib-only classifier that separates:

```text
literal_secret_assignment:
  hard_finding in app/source/config/script contexts when RHS is quoted literal and not placeholder

semantic_token_assignment:
  review_note or no finding when RHS calls normalize/parse/tokenize/lower/strip over existing values

placeholder_secret_assignment:
  review_note when RHS is placeholder/env reference/example marker

docs_or_test_secret_example:
  review_note

config_literal_secret:
  hard_finding
```

The report must explicitly compare old behavior vs refined behavior for the historical examples:

```text
token = _normalize_token(value)
token = _normalize_token(str(value).strip())
```

## 7. Expected Report

Write:

```text
secret_rule_refinement_report.md
```

Include:

```text
verdict
command run
files read
files created
fixture results
old rule behavior
refined rule behavior
hard findings
review notes
false-positive reduction
false-negative watch
VectorFL recovery suggestion
WATCH
HOLD
```

## 8. Expected Receipt

Write:

```text
secret_rule_refinement_receipt.json
```

Include:

```text
verdict
timestamp
command
input files
output files
exit code
network_used
packages_installed
git_used
source_files_modified
prior_files_modified
memory_modified
skill_modified
cron_modified
config_modified
vectorfl_authority_files_modified
current_position_updated
output_manifest_updated
baseline_workflow_schema_registry_ontology_promoted
```

## 9. VectorFL Recovery Suggestion

Use this recovery frame:

```text
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
```

## 10. Terminal Summary Format

Print:

```text
HERMES_STAGE1_SECRET_RULE_REFINEMENT_AUDIT_DONE
    output_dir: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_secret_rule_refinement_audit_v0/
    report: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_secret_rule_refinement_audit_v0/secret_rule_refinement_report.md
    receipt: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_secret_rule_refinement_audit_v0/secret_rule_refinement_receipt.json
    verdict: [HERMES_STAGE1_SECRET_RULE_REFINEMENT_AUDIT_EXECUTED_WITH_WATCH]
    watch: refined secret/token rules may reduce false positives but still do not authorize component/workflow/skill/baseline
```

## 11. Hard Stop Confirmation

Confirm:

```text
no source files modified
no prior audit files modified
no patches applied
no git used
no git add / commit / reset / checkout
no package install
no network / browser / MCP
no Hermes memory / skill / cron / config edit
no AGENTS.md / SKILL.md update
no VectorFL authority update
no current-position / output_manifest update
no baseline / workflow / schema / registry / ontology promotion
no declared output directory outside write
```
