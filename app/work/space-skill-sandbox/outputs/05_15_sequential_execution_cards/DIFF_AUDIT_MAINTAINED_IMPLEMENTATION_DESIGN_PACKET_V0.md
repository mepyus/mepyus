# Diff Audit Maintained Implementation Design Packet v0

## 1. Verdict

```text
DIFF_AUDIT_MAINTAINED_IMPLEMENTATION_DESIGN_ONLY_COMPONENT_HOLD
```

## 2. Purpose

This packet designs what a maintained implementation could look like.

It does not implement it.
It does not promote the rule set.
It does not create a component.

Current status:

```text
diff-audit rule set:
  strong candidate

component:
  HOLD
```

## 3. Why This Packet Exists

Gemini reviewed the candidate-to-component readiness packet and confirmed:

```text
strong candidate:
  yes

component:
  HOLD

main blocker:
  no stable maintained implementation
```

Therefore the next smallest action is:

```text
define implementation boundary before implementation
```

## 4. Proposed Location

Possible maintained implementation location:

```text
app/work/space-skill-sandbox/components/stage1_diff_audit/
```

Alternative lower-authority location:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/component_candidates/stage1_diff_audit/
```

Recommended for now:

```text
component_candidates/stage1_diff_audit/
```

Reason:

```text
Keeps the implementation below official component authority
while allowing a stable candidate implementation to be tested.
```

## 5. Proposed File Shape

Candidate implementation could contain:

```text
README.md
stage1_diff_audit.py
rules_v0.py
reporting.py
fixtures/
tests/
examples/
```

Minimum viable candidate implementation:

```text
stage1_diff_audit.py
README.md
```

Not allowed in this stage:

```text
package install
daemon
cron
git hook
pre-commit hook
CI integration
Hermes skill
Codex skill
AGENTS.md update
SKILL.md creation
workflow registration
```

## 6. Stable CLI Shape

Proposed CLI:

```text
python3 stage1_diff_audit.py \
  --input <diff-or-patch-path> \
  --input-kind patch \
  --scope-label <label> \
  --output-dir <declared-output-dir>
```

Optional later:

```text
--input-kind stdin
--input-kind git-diff
--input-kind git-diff-cached
--bounded-path <path>
```

For candidate implementation, avoid direct git calls if possible.

Preferred mode:

```text
Caller provides diff text or patch files.
Audit script reads only declared files.
```

Reason:

```text
This keeps source selection and audit execution separated.
```

## 7. Stable Input Contract

Allowed:

```text
one or more declared .patch files
one declared directory containing .patch files
one diff text file
```

Required:

```text
input path exists
input path is inside allowed workspace/output scope
output dir is declared
scope label is recorded
```

Not allowed:

```text
unbounded repo scan
implicit git diff
implicit reading of source tree
network input
MCP input
external app input
secret manager input
```

## 8. Stable Output Contract

Required outputs:

```text
stage1_diff_audit_report.md
stage1_diff_audit_receipt.json
```

Required report sections:

```text
verdict
scope
inputs
outputs
aggregate counts
per-input findings
hard finding examples
review note examples
suppressed examples
known limits
WATCH
HOLD
```

Required receipt fields:

```text
verdict
timestamp
command
input_paths
output_paths
exit_code
hard_findings
review_notes
suppressed_notes
network_used
packages_installed
git_used
git_mutation_used
source_files_modified
memory_modified
skill_modified
cron_modified
config_modified
vectorfl_authority_files_modified
baseline_workflow_schema_registry_ontology_promoted
```

## 9. Rule Versioning

Rule version:

```text
stage1_diff_audit_rules_v0
```

Rule version must be written to:

```text
report.md
receipt.json
```

Changing any of these requires new version:

```text
hard finding boundary
review note boundary
suppressed noise boundary
path context classifier
receipt contract
```

## 10. Known Rule Boundary

Hard finding:

```text
literal secret assignment in app/source/config/script context
bare except in app/source context
eval(...) in app/source context
exec(...) in app/source context
subprocess.run(... shell=True) in app/source context
os.system(...) in app/source context
console.log(...) in app source
print(...) in app source
curl ... | bash in script/deploy context
rm -rf in script/deploy context
chmod 777 in script/deploy context
```

Review note:

```text
semantic token normalization
env/reference boundary
placeholder/env secret assignment
docs/tests/fixtures explicit examples
script CLI output
```

Suppressed:

```text
ordinary tokenizer/parser/path-token naming
string-only print/eval noise
```

## 11. Safety Boundary

Candidate implementation must be:

```text
stdlib-only
read-only over inputs
write-only to declared output dir
no source mutation
no git mutation
no network
no browser
no MCP
no external app
no memory/skill/cron/config mutation
no VectorFL authority update
```

## 12. Test Requirement Before Component Proposal

Before component proposal, candidate implementation must pass:

```text
1. seeded true-positive fixture test
2. semantic-token noise fixture test
3. historical patch replay
4. current tracked diff replay
5. Hermes independent rerun using candidate implementation
6. Codex receipt review
```

Passing these allows:

```text
component proposal draft
```

Still does not allow:

```text
component promotion
workflow creation
skill creation
baseline update
```

## 13. Open Design Questions

```text
1. Should git diff collection stay outside the component?
2. Should untracked file reading be supported at all?
3. Should script CLI print(...) remain review note or be suppressed?
4. Should docs/tests dangerous commands always be review notes?
5. Should generated files be ignored by default?
6. Should report format be Markdown-only or Markdown + JSON findings?
```

## 14. Recommended Next Action

Do not implement yet unless explicitly requested.

Recommended next gate:

```text
Hermes/Codex review this design packet for implementation boundary only.
```

If user asks to implement:

```text
create candidate implementation under:
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/component_candidates/stage1_diff_audit/
```

## 15. WATCH

```text
1. Design packet being mistaken for implementation approval.
2. Candidate implementation being mistaken for component.
3. Component proposal being mistaken for component promotion.
4. Direct git support expanding the execution boundary.
5. Audit becoming pre-commit automation.
```

## 16. HOLD

```text
no implementation unless explicitly requested
no component promotion
no workflow creation
no skill creation
no baseline promotion
no schema/registry/ontology creation
no current-position update
no output_manifest update
no AGENTS.md update
no SKILL.md creation
no automation
```
