# Diff Audit Rule Candidate State After Hermes Threshold Tightening v0

## 1. Verdict

```text
DIFF_AUDIT_RULE_SET_STRENGTHENED_AS_CANDIDATE_WITH_COMPONENT_HOLD
```

## 2. Current Position

The Stage 1 diff-audit rule set is now a stronger candidate.

It is still not:

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

## 3. Evidence Chain

```text
synthetic fixture audit
  -> rule-quality audit
  -> historical code-diff sample audit
  -> secret/token rule refinement
  -> refined rule historical replay
  -> seeded true-positive pressure
  -> Hermes independent rerun
  -> Hermes review-note threshold tightening
```

## 4. Hermes Threshold Tightening Result

Report/receipt counts:

```text
before:
  historical_hard_findings: 1
  historical_review_notes: 118
  seeded_hard_findings: 19
  seeded_review_notes: 31

after:
  historical_hard_findings: 1
  historical_review_notes: 7
  seeded_hard_findings: 19
  seeded_review_notes: 27
```

Note:

```text
The terminal summary supplied by the user reported historical_review_notes 2 and seeded_review_notes 20.
The persisted report/receipt show 7 and 27.
Use persisted report/receipt as the recoverable evidence.
```

## 5. What Stabilized

Hard findings stayed stable:

```text
historical_hard_findings:
  1 -> 1

seeded_hard_findings:
  19 -> 19
```

The retained historical hard finding is:

```text
console.log(...) in app source
```

Seeded hard findings retained:

```text
literal secret assignments
bare except
eval(...)
exec(...)
subprocess.run(... shell=True)
os.system(...)
curl ... | bash in script/deploy context
rm -rf in script/deploy context
chmod 777 in script/deploy context
```

## 6. What Improved

Review-note noise decreased sharply.

Suppressed token-noise class:

```text
PATH_TOKEN_RE
for token in tokens
_tokenize(...)
overlap_tokens
canonicalizable_token_pair_count
sentence_tokens
ordinary tokenizer/parser/path-token naming
```

Retained review-note class:

```text
semantic token assignment:
  token = _normalize_token(value)
  token = _normalize_token(str(value).strip())

env/reference boundary:
  os.environ["SERVICE_TOKEN"]

placeholder/env secret assignment:
  TOKEN="${SERVICE_TOKEN}"
  TOKEN="<set-in-env>"
  CREDENTIAL=""

docs/tests explicit examples:
  secret-like assignment examples
  dangerous command examples

script print usage:
  print("usage: ...")
  print(json.dumps(...))
```

## 7. Current Recovery Classification

```text
receipt:
  Hermes independently executed threshold tightening with report/receipt evidence.

residue:
  review-note threshold difference remains observable.

candidate:
  refined diff-audit rule set is now stronger.

component:
  HOLD.

STOP:
  any direct conversion to workflow/skill/baseline/schema/registry/ontology/current-position/output_manifest.
```

## 8. Remaining Gaps

The rule set is not component-ready because:

```text
1. The real historical sample is small.
2. Review-note threshold is now much tighter and may under-report some weak signals.
3. No broad real working-tree sample has been tested.
4. No independent Gemini/code-review lens has compared the final rule boundary.
5. The rule exists as test artifacts, not a maintained reusable component.
```

## 9. Next Smallest Action

Do not promote.

Run one bounded broader-real-sample test:

```text
Hermes Stage 1 current working-tree diff read-only audit
```

Conditions:

```text
read-only git diff only
no source modification
no git add/commit/reset/checkout
no package install
no network/browser/MCP
no Hermes memory/skill/cron/config edit
write only declared output directory
recovery as receipt/residue/candidate only
component remains HOLD
```

Purpose:

```text
Test whether the tightened rule boundary works on a larger, current, messy real diff surface.
```

## 10. WATCH

```text
1. Review-note threshold becoming too tight.
2. Hard findings being treated as proof of exploitability.
3. Candidate rule set being promoted into component/workflow/skill too early.
4. Current working-tree diff containing unrelated user work.
5. Hermes execution success being mistaken for VectorFL authority.
```

## 11. HOLD

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
