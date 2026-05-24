# Pipeline Candidate List v0

## 1. Document Status

```text
Document = Pipeline Candidate List
Status = CANDIDATE_LIST_ONLY
Authority = orientation / re-entry support
Not registry
Not index
Not ledger
Not official workflow
Not automation
Not baseline
Not current-position update
```

Purpose:

```text
Remember processes that have enough repeated shape to be treated as pipeline candidates, while keeping immature flows as watch/hold.
```

Boundary:

```text
This list does not implement pipelines.
This list does not make any pipeline official.
This list does not trigger execution automatically.
This list does not replace User decision.
```

## 2. Listing Criteria

List a process as `PIPELINE_CANDIDATE` only when:

```text
the repeated flow is visible
inputs are identifiable
outputs are identifiable
stop conditions are identifiable
User gate and forbidden actions are preserved
the process can be reused across more than one case
at least one bounded dry run or equivalent evidence exists
```

If not enough evidence exists, keep it as:

```text
MATERIAL
CONNECTION_SEED
LINE_CANDIDATE
PROCESS_ASSET
WATCH
HOLD
```

## 3. Current Pipeline Candidates

### 3.1 Line-to-Axis Formation Reading Pipeline Candidate

```text
name: Line-to-Axis Formation Reading Pipeline Candidate
status: PIPELINE_CANDIDATE_WITH_WATCH
source_packaging: docs/reports/line_to_axis_formation_process_asset_dry_run_packaging_v0.md
supporting_rule_candidate: docs/reports/axis_formation_rule_candidate_v0.md
execution_packet: docs/reports/gemini_line_to_axis_formation_execution_packet_v0.md
first_dry_run_status: LINE_TO_AXIS_FORMATION_PROCESS_ASSET_DRY_RUN_COMPLETE
recommended_state: WAIT_FOR_NEXT_NATURAL_TRIGGER
```

Why listed:

```text
The dry run produced connection seeds, line candidates, an axis candidate, camera/lens assignment, overhardening checks, and a user-facing card.
The flow has clear steps and can be reused when natural triggers appear.
```

Core flow:

```text
source coverage
material grouping
connection extraction
line candidate naming
line test
axis candidate test
camera/lens assignment
overhardening check
User-facing card
final judgment
```

Use when:

```text
repeated process asset signals appear
line/axis naming is needed
new external candidate connects to several prior records
space feels scattered and lower-level materials need grouping
```

Do not use when:

```text
the task is one-off
the User only wants a quick answer
there is not enough evidence bundle
using it would create ceremony
```

Watch:

```text
candidate card becoming registry
line candidate becoming official axis too early
axis candidate becoming ontology
process asset becoming ledger
pipeline candidate becoming official workflow
Gemini evidence becoming verified truth
Codex packaging becoming final authority
```

## 4. Candidates Not Yet Listed

The following may have useful process shapes, but are not listed here unless separately reviewed against the listing criteria:

```text
Formation Prework
Worker Evidence Packaging
Bounded Deep Reread
Continue-Until-Blocked
Reference Materials Deep Reread
Four-Axis Whole-Space Reading Pass
```

Reason:

```text
Some of these are already process assets or worklists, but this list should only add them when their pipeline-candidate status is explicitly reviewed.
```

## 5. Watch Items

```text
pipeline candidate list becoming registry/index
pipeline candidate becoming official workflow
candidate status implying implementation readiness
watch/hold items being promoted by presence in this list
User gate becoming ceremonial
Gemini evidence becoming verified truth
Codex packaging becoming final authority
```

## 6. Do Not Do Yet

```text
no implementation
no automation
no runtime script
no registry/index/ledger
no formal schema
no official workflow
no current-position update
no baseline promotion
no ontology creation
no official axis registry
no tool/API/function attachment
no Plan Packet workflow
no pipeline execution from this list alone
no Gemini verified-truth authority
no Codex final authority
```

## 7. Final Status

```text
STATUS: PIPELINE_CANDIDATE_LIST_PREPARED
```
