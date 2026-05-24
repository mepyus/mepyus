# Hermes Stage 1 Historical Code Diff Sample Audit Packet v0

Copy this whole prompt into the active Hermes terminal.

---

You are Hermes Agent acting as a native local execution workbench candidate for VectorFL.

This is a **Stage 1 local historical code-diff sample audit**.

Use this packet in Hermes, not Gemini.

Why Hermes:

```text
This task uses Hermes-native local file/terminal execution.
The goal is to test local historical diff extraction + deterministic audit + report/receipt recovery.
```

Core principle:

```text
Let Hermes act natively.
Let VectorFL recover selectively.
```

## 1. Purpose

The previous historical audit read 7 extracted patch files, but all were documentation/work-output files:

```text
app/work/SESSION_*_RESULTS_V0.md
```

That produced hard findings = 0, but the validation value was weak for code-risk auditing.

This packet asks Hermes to select a better bounded sample:

```text
5-10 historical commits or patches that touch code/script/config/build/deploy surfaces.
```

Then run a deterministic local diff audit over only those extracted patches.

## 2. Hard Boundary

Do not:

```text
modify source files
apply patches
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
run read-only git commands:
  git log
  git show
  git diff-tree

create one declared sandbox output directory
write selected patch files under that output directory
write one Python stdlib-only audit script
run that script once
write one markdown report
write one JSON receipt
print a concise terminal summary
```

## 3. Output Directory

Create and write only under:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/
```

Allowed output files/directories:

```text
patches/
audit_historical_code_diffs.py
historical_code_diff_audit_report.md
historical_code_diff_audit_receipt.json
```

Inside `patches/`, write only selected `.patch` files.

Do not write anything else.

## 4. Patch Selection Rule

Use read-only git commands to find a bounded sample of 5-10 commits touching at least some of:

```text
app/**/*.py
app/**/*.ts
app/**/*.tsx
scripts/**/*.py
scripts/**/*.sh
config/*
*.json
*.toml
*.yaml
*.yml
package.json
vite.config.*
deploy*
```

Avoid selecting only:

```text
*.md
app/work/*.md
runtime/commands/*
generated docs
pure output reports
```

Selection should prefer commits with code/script/config content.

If fewer than 5 such commits exist, report that and continue with whatever bounded sample exists.

For each selected commit, write:

```text
patches/<short_sha>.patch
```

using read-only `git show`.

## 5. Audit Script Requirements

Create:

```text
audit_historical_code_diffs.py
```

The script must:

```text
use only Python standard library
read only patches/*.patch under the declared output directory
not modify input patch files
not inspect the repo
not call git
not use subprocess
not use network
not install packages
write historical_code_diff_audit_report.md
write historical_code_diff_audit_receipt.json
exit 0 if completed
```

The script should detect added-line patterns:

```text
debug print:
  print(
  console.log(

hardcoded secret-looking string:
  sk_live
  api_key
  token =
  password =
  secret =
  credential

bare except:
  except:

unresolved TODO / FIXME:
  TODO
  FIXME

suspicious shell command:
  curl ... | bash
  rm -rf
  chmod 777

dangerous dynamic execution:
  eval(
  exec(
  subprocess.run(... shell=True)
  os.system(
```

Add path-context classification:

```text
docs/*.md:
  review_note unless it is a script block marked executable

tests/ or fixtures:
  review_note unless it mutates real external systems

generated/:
  review_note; fix upstream/generator

config/ or env-like files:
  hard_finding for secret-looking strings

scripts/ or deploy files:
  hard_finding for shell/network/destructive command patterns

app source:
  hard_finding for debug print, secret-looking string, bare except, dangerous dynamic execution
```

This remains a string/path-context audit. Do not claim semantic compliance.

## 6. Expected Report

Write:

```text
historical_code_diff_audit_report.md
```

with sections:

```markdown
# Hermes Stage 1 Historical Code Diff Sample Audit Report v0

## 1. Verdict

[HERMES_STAGE1_HISTORICAL_CODE_DIFF_SAMPLE_AUDIT_EXECUTED_WITH_WATCH]

## 2. Patch Selection

selected commits:
selection command summary:
selection limits:

## 3. Command

## 4. Files Read

## 5. Files Created

## 6. Findings Per Patch

## 7. Context Summary

## 8. Rule Hits

## 9. False Positive / False Negative Notes

## 10. Limits

## 11. VectorFL Recovery Suggestion

## 12. WATCH

## 13. HOLD

## 14. Hard Stop Confirmation
```

VectorFL recovery suggestion must state:

```text
receipt:
  historical code-diff audit ran with command/output evidence

residue:
  false-positive, false-negative, path-context, and sample-selection notes

candidate:
  refined code/script/config diff-audit rules if useful

component:
  still HOLD until repeated validation on real diffs with stable false-positive behavior

STOP:
  patch/commit/skill/memory/cron/config/MCP/network/VectorFL authority mutation
```

## 7. Expected JSON Receipt

Write:

```text
historical_code_diff_audit_receipt.json
```

with fields:

```json
{
  "verdict": "[HERMES_STAGE1_HISTORICAL_CODE_DIFF_SAMPLE_AUDIT_RECEIPT]",
  "timestamp": "",
  "selection_commands": [],
  "selected_commits": [],
  "input_patch_files": [],
  "output_files": [],
  "audit_command": "python3 audit_historical_code_diffs.py",
  "exit_code": 0,
  "network_used": false,
  "packages_installed": false,
  "subprocess_used_by_audit_script": false,
  "git_used_for_patch_selection_only": true,
  "git_mutation_used": false,
  "source_files_modified": false,
  "patches_applied": false,
  "input_files_modified": false,
  "memory_modified": false,
  "skill_modified": false,
  "cron_modified": false,
  "config_modified": false,
  "vectorfl_authority_files_modified": false,
  "current_position_updated": false,
  "output_manifest_updated": false,
  "baseline_workflow_schema_registry_ontology_promoted": false
}
```

## 8. Execution Instruction

After creating selected patch files and the script, run exactly one audit command:

```text
python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/audit_historical_code_diffs.py
```

Do not run any mutation command.

## 9. Report-Level HOLD

The report must confirm:

```text
no source files modified
no patches applied
no git add
no git commit
no git reset
no git checkout
no package install
no network
no browser
no MCP call
no cron
no Hermes memory edit
no Hermes skill edit
no Hermes config edit
no AGENTS.md update
no SKILL.md creation
no VectorFL authority update
no current-position update
no output_manifest update
no baseline/workflow/schema/registry/ontology promotion
```

## 10. Terminal Summary

When finished, print:

```text
HERMES_STAGE1_HISTORICAL_CODE_DIFF_SAMPLE_AUDIT_DONE
    output_dir: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/
    report: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/historical_code_diff_audit_report.md
    receipt: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/historical_code_diff_audit_receipt.json
    verdict: [HERMES_STAGE1_HISTORICAL_CODE_DIFF_SAMPLE_AUDIT_EXECUTED_WITH_WATCH]
    watch: historical code-diff results may refine candidate rules, but still do not authorize component/workflow/skill/baseline
```

