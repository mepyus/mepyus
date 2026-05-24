# Hermes Stage 1 Local Diff Audit Rule Quality Packet v0

Copy this whole prompt into the active Hermes terminal.

---

You are Hermes Agent acting as a native external execution workbench candidate for VectorFL.

This is a **Stage 1 local deterministic rule-quality test** for the diff-audit candidate.

The previous Stage 1 diff-audit run used intentionally obvious risk fixtures. This packet tests whether the audit rules can handle:

```text
clean diff
borderline diff
false-positive-looking diff
```

Purpose:

```text
Test candidate rule quality without promoting the audit into a component, workflow, skill, baseline, or authority.
```

Core principle:

```text
Let Hermes act natively.
Let VectorFL recover selectively.
```

## 1. What This Tests

This packet tests:

```text
1. Whether candidate audit rules over-trigger on benign content.
2. Whether warning language separates hard findings from review-only notes.
3. Whether clean/borderline examples remain receipts/residue/candidate evidence, not component validation.
4. Whether Hermes can run another local deterministic script while preserving persistence boundaries.
```

## 2. Hard Boundary

Do not:

```text
modify source files
patch existing files
run git add
run git commit
run repo-wide search
inspect sibling folders
read files outside the declared output directory and the explicit input file listed below
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
update VectorFL files
update current-position
update output_manifest
promote anything to baseline/workflow/schema/registry/ontology
write outside the declared output directory
```

Allowed:

```text
read the explicit input file listed below
create one declared sandbox output directory
write three declared fixture patch files
write one Python stdlib-only audit script
run that script once
write one declared markdown report
write one declared JSON receipt
print a concise terminal summary
```

## 3. Explicit Context Input

Read only this existing context file:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_local_diff_audit_with_persistence_boundary_v0/audit_report.md
```

If this file is missing, report it and continue with this prompt only.

Do not read anything else outside the output directory.

## 4. Output Directory

Create and write only under:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_local_diff_audit_rule_quality_v0/
```

Allowed output files:

```text
fixture_clean.patch
fixture_borderline.patch
fixture_false_positive.patch
audit_rule_quality.py
rule_quality_report.md
rule_quality_receipt.json
```

Do not write any other files.

## 5. Fixture Files To Create

Create `fixture_clean.patch` with exactly this content:

```diff
diff --git a/app/export_status.py b/app/export_status.py
index aaaaaaa..bbbbbbb 100644
--- a/app/export_status.py
+++ b/app/export_status.py
@@ -1,5 +1,8 @@
 def export_status(job):
-    return {"state": job.state}
+    return {
+        "state": job.state,
+        "completed_at": job.completed_at,
+        "row_count": job.row_count,
+    }
```

Create `fixture_borderline.patch` with exactly this content:

```diff
diff --git a/app/logging.py b/app/logging.py
index ccccccc..ddddddd 100644
--- a/app/logging.py
+++ b/app/logging.py
@@ -1,6 +1,9 @@
 def log_export_attempt(logger, export_id, user_id):
-    logger.info("export started")
+    logger.info("export started", extra={"export_id": export_id, "user_id": user_id})
+    # TODO: replace user_id with stable audit-safe identifier after privacy review
+    return True
```

Create `fixture_false_positive.patch` with exactly this content:

```diff
diff --git a/docs/security_examples.md b/docs/security_examples.md
index eeeeeee..fffffff 100644
--- a/docs/security_examples.md
+++ b/docs/security_examples.md
@@ -1,4 +1,10 @@
 # Security examples
 
-Document examples here.
+Do not hardcode values such as password = "example".
+Do not pipe curl to bash in production scripts.
+Example marker only: sk_live_example_should_not_be_used.
+Prefer documented secret storage and review suspicious shell commands.
+This document is explanatory and is not executable code.
```

## 6. Audit Script Requirements

Create:

```text
audit_rule_quality.py
```

The script must:

```text
use only Python standard library
read only fixture_clean.patch, fixture_borderline.patch, fixture_false_positive.patch
not modify input files
not inspect the repo
not call git
not use subprocess
not use network
not install packages
write rule_quality_report.md
write rule_quality_receipt.json
exit 0 if completed
```

The script should detect the same simple risk patterns as the previous audit, but add a simple context note:

```text
If the file path in the diff starts with docs/:
  mark hardcoded secret-looking string and curl pipe bash hits as documentation-context review notes, not hard findings.

If TODO/FIXME appears in added line:
  mark as review note unless paired with high-risk code or shell command.

If print( appears:
  hard finding only for non-docs files.
```

This is still a simple string-based audit. Do not claim semantic compliance.

## 7. Expected Markdown Report

The script must write:

```text
rule_quality_report.md
```

with sections:

```markdown
# Hermes Stage 1 Local Diff Audit Rule Quality Report v0

## 1. Verdict

[HERMES_STAGE1_LOCAL_DIFF_AUDIT_RULE_QUALITY_EXECUTED_WITH_WATCH]

## 2. Command

## 3. Files Read

## 4. Files Created

## 5. Findings Per Fixture

## 6. Hard Findings vs Review Notes

## 7. False-Positive / Borderline Notes

## 8. Limits

## 9. VectorFL Recovery Suggestion

## 10. WATCH

## 11. HOLD

## 12. Hard Stop Confirmation
```

VectorFL recovery suggestion must state:

```text
receipt:
  rule-quality audit ran, with command/output evidence

residue:
  false-positive and borderline behavior notes

candidate:
  refined diff-audit rule idea with docs-context and review-note distinction

component:
  still not yet; needs repeated validation on real diffs

STOP:
  any attempt to patch files, commit changes, create skill, write memory, schedule cron, change config, call MCP, use network, or promote audit rules to baseline/workflow/schema/registry/ontology
```

## 8. Expected JSON Receipt

The script must write:

```text
rule_quality_receipt.json
```

with fields:

```json
{
  "verdict": "[HERMES_STAGE1_LOCAL_DIFF_AUDIT_RULE_QUALITY_RECEIPT]",
  "command": "python3 audit_rule_quality.py",
  "input_files": [],
  "output_files": [],
  "exit_code": 0,
  "network_used": false,
  "packages_installed": false,
  "subprocess_used": false,
  "git_used": false,
  "input_files_modified": false,
  "memory_modified": false,
  "skill_modified": false,
  "cron_modified": false,
  "config_modified": false,
  "vectorfl_authority_files_modified": false,
  "notes": []
}
```

Add a timestamp field if available from Python standard library.

## 9. Execution Instruction

After creating the three fixture files and the script, run exactly:

```text
python3 app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_local_diff_audit_rule_quality_v0/audit_rule_quality.py
```

Do not run any other command except what is required to create files in the declared output directory.

## 10. Report-Level HOLD

The report must confirm:

```text
no source files modified
no patches applied
no git add
no git commit
no repo-wide search
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

## 11. Terminal Summary

When finished, print:

```text
HERMES_STAGE1_LOCAL_DIFF_AUDIT_RULE_QUALITY_DONE
    output_dir: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_local_diff_audit_rule_quality_v0/
    script: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_local_diff_audit_rule_quality_v0/audit_rule_quality.py
    report: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_local_diff_audit_rule_quality_v0/rule_quality_report.md
    receipt: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_local_diff_audit_rule_quality_v0/rule_quality_receipt.json
    verdict: [HERMES_STAGE1_LOCAL_DIFF_AUDIT_RULE_QUALITY_EXECUTED_WITH_WATCH]
    watch: refined audit rules may become candidate, but still not component/workflow/skill/baseline
```

