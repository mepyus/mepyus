# Hermes Stage 1 Refined Diff Audit Independent Rerun Packet v0

Copy this whole prompt into the active Hermes terminal.

---

You are Hermes Agent acting as a native local execution workbench candidate for VectorFL.

This is a **Stage 1 independent rerun test**.

Use this packet in Hermes, not Gemini.

Core principle:

```text
Let Hermes act natively.
Let VectorFL recover selectively.
```

## 1. Purpose

Codex refined the Stage 1 diff-audit rule boundary after historical and seeded fixture tests.

Current recovered judgment:

```text
literal secrets in app/config/script:
  hard_finding

semantic token normalization:
  review_note

docs/tests examples:
  review_note

dangerous shell / eval / exec / bare except:
  hard_finding in app/script contexts

string-only print/eval noise:
  not hard_finding
```

Codex replay results:

```text
historical replay:
  old_hard_findings_estimate: 5
  refined_hard_findings: 1

seeded true-positive pressure:
  total_hard_findings: 19
  total_review_notes: 23
```

This Hermes task should independently rerun the refined audit over the already-created fixtures and historical patches, then produce report/receipt.

This test checks:

```text
Can Hermes reproduce the refined candidate rule behavior?
Can Hermes keep execution local and bounded?
Can Hermes return evidence without promoting the rule set?
```

This is not a component.
This is not a workflow.
This is not a skill.
This is not VectorFL authority update.

## 2. Read-Only Inputs

Read only these existing directories/files:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/patches/
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_seeded_true_positive_pressure_v0/fixtures/
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_secret_rule_refinement_audit_v0/secret_rule_refinement_report.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_rule_historical_replay_v0/refined_rule_historical_replay_report.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_seeded_true_positive_pressure_v0/seeded_true_positive_pressure_report.md
```

Do not modify these files.
Do not inspect live source files.
Do not perform broad repo search.
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
write one Python stdlib-only independent rerun script
run that script once
read only declared historical patches and seeded fixtures
write one markdown report
write one JSON receipt
print a concise terminal summary
```

## 4. Output Directory

Create and write only under:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_diff_audit_independent_rerun_v0/
```

Allowed output files:

```text
independent_refined_diff_audit.py
independent_refined_diff_audit_report.md
independent_refined_diff_audit_receipt.json
```

Do not copy input patch files unless necessary. Prefer reading them in place.

## 5. Refined Rule Boundary to Implement

Implement a Python stdlib-only diff audit with path-context classification.

### Contexts

```text
docs:
  docs/** or *.md

tests_or_fixtures:
  tests/** or path containing fixture/fixtures

config_or_env_like:
  config/** or *.env/*.json/*.toml/*.yaml/*.yml or filename containing env

scripts_or_deploy:
  scripts/**, deploy*, or shell script extensions

app_source/source_code:
  app/**/*.py, app/**/*.ts, app/**/*.tsx, app/**/*.js, app/**/*.jsx
```

### Secret Boundary

Hard finding:

```text
quoted literal secret-like assignment in app_source/source_code
quoted literal secret-like assignment in config_or_env_like
quoted literal secret-like assignment in scripts_or_deploy
```

Examples:

```text
api_key = "sk_live_prod_123456789"
token = "prod-token-123456"
password = "admin123"
SERVICE_TOKEN="real-looking-secret"
API_KEY="real-looking-key"
```

Review note:

```text
token = _normalize_token(value)
token = _normalize_token(str(value).strip())
token = token.lower()
API_TOKEN = os.environ["API_TOKEN"]
TOKEN="${SERVICE_TOKEN}"
TOKEN="<set-in-env>"
CREDENTIAL=""
docs/test/fixture examples
secret words without direct assignment
```

### Non-Secret Rules

Hard finding in app/source contexts:

```text
actual print(...) call at line start
actual console.log(...) call at line start
bare except:
eval(...)
exec(...)
subprocess.run(... shell=True)
os.system(...)
```

Hard finding in scripts/deploy context:

```text
curl ... | bash
rm -rf
chmod 777
dynamic execution
```

Review note:

```text
same patterns in docs/tests/fixtures
string-only noise such as:
  print_usage = "print( is just text"
  todo_label = "TODO wording in data"
```

## 6. Expected Replay Targets

Run the independent script over both sets:

```text
historical patches:
  app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/patches/*.patch

seeded fixtures:
  app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_seeded_true_positive_pressure_v0/fixtures/*.patch
```

Expected rough behavior:

```text
historical refined hard findings:
  about 1
  expected retained hard hit: console.log in app source

seeded refined hard findings:
  about 19
  expected: literal secrets / shell / dynamic execution caught

semantic token normalization:
  review note, not hard finding
```

If your counts differ, explain why in the report. Do not force-match Codex counts.

## 7. Expected Report

Write:

```text
independent_refined_diff_audit_report.md
```

Include:

```text
verdict
command run
files read
files created
historical patch results
seeded fixture results
aggregate counts
differences from Codex replay
false-positive notes
false-negative notes
VectorFL recovery suggestion
WATCH
HOLD
```

## 8. Expected Receipt

Write:

```text
independent_refined_diff_audit_receipt.json
```

Include:

```text
verdict
timestamp
command
input files
output files
exit code
historical_hard_findings
historical_review_notes
seeded_hard_findings
seeded_review_notes
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
  Hermes independently reran refined diff audit with command/output evidence

residue:
  count differences, false-positive notes, false-negative notes

candidate:
  refined diff-audit rule set becomes stronger if behavior matches Codex replay

component:
  HOLD until broader real sample and user/Codex explicit approval

STOP:
  patch/commit/skill/memory/cron/config/MCP/network/VectorFL authority mutation
```

## 10. Terminal Summary Format

Print:

```text
HERMES_STAGE1_REFINED_DIFF_AUDIT_INDEPENDENT_RERUN_DONE
    output_dir: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_diff_audit_independent_rerun_v0/
    report: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_diff_audit_independent_rerun_v0/independent_refined_diff_audit_report.md
    receipt: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_diff_audit_independent_rerun_v0/independent_refined_diff_audit_receipt.json
    verdict: [HERMES_STAGE1_REFINED_DIFF_AUDIT_INDEPENDENT_RERUN_EXECUTED_WITH_WATCH]
    watch: independent rerun may strengthen candidate status but still does not authorize component/workflow/skill/baseline
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
