# Diff Audit Maintained Implementation Boundary Review v0

## 1. Verdict

```text
DIFF_AUDIT_MAINTAINED_IMPLEMENTATION_BOUNDARY_REVIEWED_WITH_COMPONENT_HOLD
```

## 2. Status

This is review only.

No implementation is created.
No component is promoted.
No workflow/skill/baseline/schema/registry/ontology is created.

Current position:

```text
diff-audit rule set:
  strong candidate

component:
  HOLD
```

## 3. Purpose

This review answers:

```text
If diff-audit later becomes a component candidate,
where could a maintained implementation live?
What would its stable boundary be?
What must remain forbidden?
What would count as component readiness?
What would still block promotion?
```

This review is downstream of the flow-network model:

```text
large flow-network first
small execution lanes as pressure tests
selective recovery before promotion
component only after maintained implementation boundary
```

## 4. Possible Maintained Location

Future candidate path:

```text
app/work/space-skill-sandbox/outputs/05_15_sequential_execution_cards/component_candidates/stage1_diff_audit/
```

Reason:

```text
This keeps the implementation below official component authority
while making it easier to test a stable candidate shape.
```

Do not create this directory or implementation unless explicitly approved later.

Possible later official location, only after promotion:

```text
app/work/space-skill-sandbox/components/stage1_diff_audit/
```

This later location is not approved now.

## 5. Allowed Future Component Shape

Possible shape:

```text
stage1_diff_audit.py
README.md
rules_v0.py
reporting.py
fixtures/
tests/
examples/
```

Minimum candidate shape:

```text
stage1_diff_audit.py
README.md
```

Allowed nature:

```text
bounded local diff-audit utility
declared input diff files only
stdlib-only unless separately approved
report + receipt output
deterministic rule behavior
clear hard finding / review note separation
```

## 6. Input Contract

Allowed inputs:

```text
one or more declared .patch files
one declared directory containing .patch files
one declared diff text file
stdin only if explicitly selected by caller
```

Possible later inputs:

```text
git diff --no-ext-diff output captured by caller
git diff --cached --no-ext-diff output captured by caller
```

Preferred boundary:

```text
source collection is outside the component
audit execution is inside the component
```

Reason:

```text
This prevents a simple audit utility from quietly becoming a repo scanner or git workflow.
```

Required input metadata:

```text
input path
input kind
scope label
source command or source description
bounded path list if git diff was used upstream
```

Not allowed by default:

```text
repo-wide search
implicit git diff
implicit git status
implicit source-tree walking
untracked file reading
network input
browser input
MCP input
external app input
Hermes memory input
secret manager input
```

## 7. Output Contract

Required outputs:

```text
stage1_diff_audit_report.md
stage1_diff_audit_receipt.json
```

Report contract:

```text
verdict
rule_version
scope label
input paths
output paths
aggregate hard finding count
aggregate review note count
per-input summaries
hard finding examples
review note examples
suppressed noise examples
known false positives
known false negatives
WATCH
HOLD
```

Receipt contract:

```text
verdict
timestamp
rule_version
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
input_files_modified
memory_modified
skill_modified
cron_modified
config_modified
vectorfl_authority_files_modified
baseline_workflow_schema_registry_ontology_promoted
```

## 8. Rule Boundary

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
dangerous patterns in docs/tests/fixtures
```

Suppressed by default:

```text
ordinary tokenizer/parser/path-token naming
string-only print/eval noise
PATH_TOKEN_RE
for token in tokens
_tokenize(...)
overlap_tokens
canonicalizable_token_pair_count
sentence_tokens
```

## 9. Allowed Persistence

Allowed persistence:

```text
declared output report
declared output receipt
optional findings JSON if explicitly defined in the output contract
```

Not allowed persistence:

```text
source patches
modified input files
git state
Hermes memory
Hermes skill
Hermes cron
Hermes config
MCP config
AGENTS.md
SKILL.md
current-position
output_manifest
baseline/workflow/schema/registry/ontology files
```

## 10. Permissions Required

Allowed execution permission:

```text
local file read of declared inputs
local file write to declared output directory
Python stdlib execution
```

If upstream caller needs git diff, it must be explicitly separated:

```text
collector:
  read-only git diff/git show/git status if approved

auditor:
  reads produced patch/diff files only
```

This split should remain visible in receipts.

## 11. Forbidden Behavior

Not allowed:

```text
patch source files
git add
git commit
git reset
git checkout
auto-fix
package install
network
browser
MCP
Hermes memory write
Hermes skill creation/edit
cron
config edit
VectorFL authority update
baseline/workflow/schema/registry/ontology promotion
AGENTS.md update
SKILL.md creation
current-position update
output_manifest update
```

Also not allowed:

```text
auto-block commits
install pre-commit hooks
register as workflow
run on schedule
claim security assurance
```

## 12. Component Readiness Requirements

Component readiness requires:

```text
maintained implementation location
stable input contract
stable output contract
stable receipt/report contract
repeatable rule behavior
test fixtures
historical patch replay
current diff replay
false-positive handling
false-negative documentation
clear permission boundary
no authority mutation
Codex review
Hermes rerun
Gemini/check lens if boundary changes
separate user approval for promotion
```

Current status:

```text
rule behavior:
  strong candidate

maintained implementation:
  missing

component packaging:
  not approved

promotion:
  not approved
```

## 13. Promotion Blockers

Still blocks promotion:

```text
no maintained implementation exists
no stable component directory exists
no versioned reusable rule module exists
no formal component proposal has been approved
multi-line / concatenated secret blind spot remains
runtime reachability remains out of scope
untracked-file reading is not part of default contract
```

These blockers do not weaken strong candidate status.

They do block component promotion.

## 14. Recovery Classification

```text
receipt:
  implementation boundary review created.

residue:
  open design questions and promotion blockers remain.

candidate:
  diff-audit remains strong candidate.

component:
  HOLD.

space_update_proposal:
  not yet.

STOP:
  direct implementation/promotion/workflow/skill/baseline/schema/registry/ontology/current-position/output_manifest update.
```

## 15. Open Questions

```text
1. Should git diff collection remain permanently outside the component?
2. Should untracked files ever be supported?
3. Should script CLI print(...) remain review note or be suppressible by mode?
4. Should docs/tests dangerous command examples always stay review notes?
5. Should generated files be ignored by default?
6. Should output include JSON findings in addition to report/receipt?
7. Should multiline secret detection be out of scope or v1 requirement?
```

## 16. WATCH

```text
1. Boundary review becoming implementation approval.
2. Candidate implementation becoming component by accident.
3. Read-only utility becoming git workflow.
4. Review notes becoming auto-fix tasks.
5. Stage 1 audit being mistaken for security assurance.
6. Hermes rerun success becoming VectorFL approval.
```

## 17. HOLD

```text
no implementation created
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
