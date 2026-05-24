# Diff Audit Candidate-to-Component Readiness Packet v0

## 1. Verdict

```text
DIFF_AUDIT_READY_FOR_COMPONENT_REVIEW_NOT_COMPONENT_PROMOTION
```

## 2. Current Status

The Stage 1 diff-audit rule set is a strong candidate.

It is not yet:

```text
component
workflow
skill
baseline
schema
registry
ontology
automation
VectorFL authority
```

## 3. Purpose

This packet defines what must be true before the refined diff-audit rule set can be considered a component.

It does not promote the rule set.

It creates a review gate:

```text
strong candidate
  -> readiness review
  -> possible component proposal
  -> explicit user/Codex approval
  -> component packaging
```

## 4. Evidence Chain

Current evidence:

```text
1. Synthetic fixture audit
2. Rule-quality audit
3. Historical code-diff sample audit
4. Secret/token rule refinement
5. Refined rule historical replay
6. Seeded true-positive pressure
7. Hermes independent rerun
8. Hermes review-note threshold tightening
9. Current tracked worktree diff audit
```

Recovered current state:

```text
candidate strength:
  strong

hard finding behavior:
  stable across Codex and Hermes reruns

review-note behavior:
  tightened after Hermes over-counting

current tracked diff result:
  hard_findings: 0
  review_notes: 7
```

## 5. Proposed Component Purpose

Possible component name:

```text
Stage 1 Local Diff Audit Candidate
```

Purpose:

```text
Read a bounded git diff or patch fixture and classify obvious code-risk patterns
without modifying source, git state, external systems, memory, skill, cron, or VectorFL authority files.
```

Primary use:

```text
pre-review signal generation
receipt creation
candidate risk triage
Hermes/Codex local execution boundary test
```

Not its purpose:

```text
prove code safety
replace security scanning
auto-fix code
block commits automatically
create workflow/skill/baseline authority
```

## 6. Input Contract

Allowed inputs:

```text
unified diff text
*.patch files
git diff --no-ext-diff output
git diff --cached --no-ext-diff output
declared fixture directory
declared historical patch directory
```

Required input constraints:

```text
bounded paths must be declared
source of diff must be recorded
staged vs unstaged must be separated when applicable
untracked files must be either excluded explicitly or read through a separate approved path
```

Not allowed inputs:

```text
live source mutation
repo-wide unbounded scan
network source
external app source
MCP source
Hermes memory source
secret manager source
```

## 7. Output Contract

Required outputs:

```text
report.md
receipt.json
```

Report must include:

```text
verdict
commands run
files read
files created
scope
hard findings
review notes
suppressed notes if threshold tightening is used
known limitations
VectorFL recovery suggestion
WATCH
HOLD
```

Receipt must include:

```text
verdict
timestamp
command list
input files / paths
output files
exit code
hard finding count
review note count
network_used
packages_installed
git_mutation_used
source_files_modified
memory_modified
skill_modified
cron_modified
config_modified
vectorfl_authority_files_modified
baseline_workflow_schema_registry_ontology_promoted
```

## 8. Rule Boundary

### Hard Finding

Hard finding classes:

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

### Review Note

Review note classes:

```text
semantic token normalization:
  token = _normalize_token(value)
  token = _normalize_token(str(value).strip())

env/reference boundary:
  os.environ["TOKEN"]
  getenv("TOKEN")
  read_from_env("TOKEN")

placeholder/env secret assignment:
  TOKEN="${SERVICE_TOKEN}"
  TOKEN="<set-in-env>"
  CREDENTIAL=""

docs/tests/fixtures explicit examples:
  secret-looking examples
  dangerous command examples

script CLI output:
  print("usage: ...")
  print(json.dumps(...))
```

### Suppressed Noise

Suppressed by default:

```text
PATH_TOKEN_RE
for token in tokens
_tokenize(...)
overlap_tokens
canonicalizable_token_pair_count
sentence_tokens
ordinary tokenizer/parser/path-token naming
string-only print/eval noise
```

## 9. Known False Positives

Possible false positives:

```text
placeholder values that look realistic
docs/test examples outside obvious docs/tests paths
script CLI output counted as review notes
semantic token variables with secret-like names
```

Mitigation:

```text
keep context classification visible
do not treat review notes as findings
do not treat hard findings as proof of exploitability
require human/Codex review before action
```

## 10. Known False Negatives

Known blind spots:

```text
encoded secrets
concatenated secrets
multi-line secret construction
data-flow-based secret leakage
dangerous command built through variables
runtime reachability
dependency vulnerabilities
browser/MCP/external app side effects
untracked file contents unless explicitly read
```

Mitigation:

```text
call this Stage 1 only
keep output as triage signal
do not claim security coverage
use dedicated scanners if security assurance is required
```

## 11. Allowed Execution Mode

Allowed:

```text
local stdlib-only script
read-only git diff/git show if explicitly declared
read declared patch files
write report/receipt only under declared output directory
exit 0 on completed audit
```

Allowed git commands:

```text
git diff --no-ext-diff
git diff --cached --no-ext-diff
git show --no-ext-diff
git diff-tree --no-commit-id --name-only -r
git status --short
git ls-files --others --exclude-standard
```

## 12. Forbidden Execution Mode

Forbidden:

```text
git add
git commit
git reset
git checkout
source patching
auto-fix
package install
network
browser
MCP
external app connection
Hermes memory edit
Hermes skill edit
Hermes cron edit
Hermes config edit
AGENTS.md update
SKILL.md creation
VectorFL authority update
current-position update
output_manifest update
baseline/workflow/schema/registry/ontology promotion
```

## 13. Component Readiness Checklist

A component proposal may be considered only if all are true:

```text
[ ] Input contract is stable.
[ ] Output report format is stable.
[ ] Receipt JSON format is stable.
[ ] Rule boundary is documented.
[ ] False positives are documented.
[ ] False negatives are documented.
[ ] Read-only execution is preserved.
[ ] No git mutation is used.
[ ] No network/MCP/browser/external app is used.
[ ] No Hermes memory/skill/cron/config is modified.
[ ] No VectorFL authority file is modified.
[ ] At least one Codex run and one Hermes run agree on hard-finding behavior.
[ ] Current tracked diff audit has passed.
[ ] User explicitly asks for component proposal or packaging.
```

Current checklist status:

```text
most technical checks:
  passed or mostly passed

stable maintained implementation:
  missing

explicit component proposal request:
  missing

promotion approval:
  missing
```

## 14. Recovery Classification

```text
receipt:
  readiness packet created from evidence chain.

residue:
  readiness gaps and threshold caveats remain.

candidate:
  rule set remains strong candidate.

component:
  not yet.

space_update_proposal:
  only if user asks to package or promote.

STOP:
  direct component/workflow/skill/baseline/schema/registry/ontology/current-position/output_manifest update.
```

## 15. Next Smallest Action

Next action depends on user intent:

```text
Option A:
  Stop here and use this as strong candidate evidence.

Option B:
  Ask Gemini to review the readiness packet as an independent maturity lens.

Option C:
  Ask Hermes to package a no-promotion component proposal draft only.
```

Recommended:

```text
Option B first.
```

Reason:

```text
Before packaging, use Gemini to check whether the candidate-to-component boundary is too loose,
too strict, or missing a major risk class.
```

## 16. WATCH

```text
1. Strong candidate being treated as component.
2. Component packet becoming workflow by accident.
3. Hard findings being treated as proof of exploitability.
4. Review notes being treated as automatic action items.
5. Read-only git permissions drifting into mutation.
6. Hermes execution success being mistaken for VectorFL approval.
```

## 17. HOLD

```text
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
