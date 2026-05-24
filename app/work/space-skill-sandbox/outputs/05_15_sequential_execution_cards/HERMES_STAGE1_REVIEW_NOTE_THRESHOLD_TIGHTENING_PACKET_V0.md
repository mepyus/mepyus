# Hermes Stage 1 Review-Note Threshold Tightening Packet v0

Copy this whole prompt into the active Hermes terminal.

---

You are Hermes Agent acting as a native local execution workbench candidate for VectorFL.

This is a **Stage 1 review-note threshold tightening test**.

Use this packet in Hermes, not Gemini.

Core principle:

```text
Let Hermes act natively.
Let VectorFL recover selectively.
```

## 1. Purpose

Hermes independently reran the refined diff audit and matched the important hard-finding behavior:

```text
historical_hard_findings: 1
seeded_hard_findings: 19
```

This strengthens the candidate rule set.

But Hermes review-note counts were much higher than Codex replay:

```text
Codex replay:
  historical_review_notes: 30
  seeded_review_notes: 23

Hermes independent rerun:
  historical_review_notes: 118
  seeded_review_notes: 31
```

Likely cause:

```text
Hermes counted broad token/secret word occurrences as review_note,
including ordinary tokenizer/parser/path-token naming.
```

This test should tighten review-note threshold without weakening hard findings.

This is not a component.
This is not a workflow.
This is not a skill.
This is not VectorFL authority update.

## 2. Read-Only Inputs

Read only:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_diff_audit_independent_rerun_v0/independent_refined_diff_audit_report.md
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_refined_diff_audit_independent_rerun_v0/independent_refined_diff_audit_receipt.json
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_historical_code_diff_sample_audit_v0/patches/
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_seeded_true_positive_pressure_v0/fixtures/
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
write one Python stdlib-only threshold test script
run that script once
read only declared historical patches and seeded fixtures
write one markdown report
write one JSON receipt
print a concise terminal summary
```

## 4. Output Directory

Create and write only under:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_review_note_threshold_tightening_v0/
```

Allowed output files:

```text
review_note_threshold_tightening.py
review_note_threshold_tightening_report.md
review_note_threshold_tightening_receipt.json
```

## 5. Tightened Review-Note Rule

Keep hard-finding rules the same.

Tighten `secret_boundary` review notes:

### Count as Review Note

Only count secret/token review notes when one of these is true:

```text
1. direct assignment exists:
   token = ...
   API_TOKEN = ...
   password = ...
   credential = ...

2. env/reference boundary exists:
   os.environ["TOKEN"]
   getenv("TOKEN")
   read_from_env("TOKEN")

3. placeholder/env secret value exists:
   TOKEN="${SERVICE_TOKEN}"
   TOKEN="<set-in-env>"
   CREDENTIAL=""

4. docs/test/fixture contains explicit secret-like assignment or dangerous command example

5. function or variable name is explicitly about secret/credential/password/api_key,
   not ordinary tokenizer/parser token processing
```

### Do Not Count as Review Note

Do not count ordinary token-processing terms:

```text
PATH_TOKEN_RE
for token in tokens
tokens.add(token)
def _tokenize(...)
def _collect_anchor_tokens(...)
overlap_tokens = ...
canonicalizable_token_pair_count = ...
token_count = ...
sentence_tokens
parser token loop
```

These can be ignored unless there is direct assignment to a secret-like name, literal secret value, env reference, or dangerous command.

## 6. Expected Behavior

Hard findings should remain stable:

```text
historical_hard_findings:
  1

seeded_hard_findings:
  19
```

Review notes should decrease from Hermes independent rerun:

```text
historical_review_notes:
  should be much lower than 118

seeded_review_notes:
  should be closer to Codex 23 than Hermes 31
```

Do not force exact Codex counts.
Explain count differences.

## 7. Expected Report

Write:

```text
review_note_threshold_tightening_report.md
```

Include:

```text
verdict
command run
files read
files created
before counts from Hermes independent rerun
after counts from tightened threshold
historical patch results
seeded fixture results
review notes suppressed
review notes retained
hard-finding stability check
false-positive notes
false-negative notes
VectorFL recovery suggestion
WATCH
HOLD
```

## 8. Expected Receipt

Write:

```text
review_note_threshold_tightening_receipt.json
```

Include:

```text
verdict
timestamp
command
input files
output files
exit code
before_historical_hard_findings
before_historical_review_notes
before_seeded_hard_findings
before_seeded_review_notes
after_historical_hard_findings
after_historical_review_notes
after_seeded_hard_findings
after_seeded_review_notes
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
  Hermes tightened review-note threshold with command/output evidence

residue:
  suppressed-token-noise examples and retained-review examples

candidate:
  refined diff-audit rule set becomes stronger if hard findings remain stable and review noise decreases

component:
  HOLD until broader real sample and user/Codex explicit approval

STOP:
  patch/commit/skill/memory/cron/config/MCP/network/VectorFL authority mutation
```

## 10. Terminal Summary Format

Print:

```text
HERMES_STAGE1_REVIEW_NOTE_THRESHOLD_TIGHTENING_DONE
    output_dir: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_review_note_threshold_tightening_v0/
    report: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_review_note_threshold_tightening_v0/review_note_threshold_tightening_report.md
    receipt: app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/hermes_stage1_review_note_threshold_tightening_v0/review_note_threshold_tightening_receipt.json
    verdict: [HERMES_STAGE1_REVIEW_NOTE_THRESHOLD_TIGHTENING_EXECUTED_WITH_WATCH]
    watch: review-note tightening may strengthen candidate status but still does not authorize component/workflow/skill/baseline
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
