# Space-CLI Pipeline Script Candidate Map v0

## 1. purpose

This document separates future script candidates from non-scriptable judgment areas.

No script is created by this document.

The manual pipeline must run on actual material two or three times before script extraction.

Scripts, when introduced later, should inspect mechanics and format.

Scripts must not decide.

## 2. scriptable candidates

## packet_skeleton_generator

Role:

Generate an empty markdown skeleton for a manual pipeline run.

Allowed:

- create blank markdown
- insert field list
- preserve `auto_execute: no`

Forbidden:

- finalize source surface
- assign worker automatically
- finalize reflux memory
- execute next step

## required_field_checker

Role:

Check whether required fields are missing.

Allowed checks:

- missing `request_summary`
- missing `source_surface`
- missing `guardrails`
- missing `expected_output`
- missing `stop_conditions`

Forbidden:

- judge whether content is correct
- decide PASS / HOLD
- edit fields automatically

## memory_card_count_checker

Role:

Check whether memory card count exceeds the manual limit.

Allowed:

- count memory cards
- warn when over three to five cards

Forbidden:

- decide which memory card is appropriate
- classify memory weight
- delete cards automatically

## forbidden_expression_scanner

Role:

Detect over-promotion risk expressions.

Candidate expressions:

- baseline lock
- controller 구현
- schema 생성
- Gemini upgraded
- Eyes and Hands
- active partner
- code editing permission
- final judge
- automatic execution

Allowed:

- report expression hits
- report file and line candidate

Forbidden:

- auto-rewrite
- auto-revert
- decide final verdict

## worker_return_field_checker

Role:

Check whether a worker return contains basic review fields.

Allowed checks:

- expected-vs-observed exists
- files_modified exists
- files_created exists
- declared_verdict exists
- issue_list or detected_issues exists

Forbidden:

- automate PASS / HOLD
- accept worker output
- promote worker output into baseline

## user_card_presence_checker

Role:

Check whether the 4-line user-facing card exists.

Allowed checks:

- `쓸 수 있나?`
- `왜?`
- `다음엔?`
- `조심할 점은?`

Forbidden:

- judge card quality
- replace user-facing wording automatically

## 3. non-scriptable judgment areas

Scripts must not decide:

- final source surface
- final worker assignment
- baseline promotion
- final reflux memory classification
- next_move execution
- final user intent
- structure design direction
- file edit / revert decision

## 4. script adoption principles

- Confirm the repeated bottleneck two or three times first.
- Start with read-only checks or skeleton generation.
- A script is a checker, not a judge.
- Script output must be reread as `worker_return`.
- Script failure must not trigger automatic correction.
- Script success must not mean pipeline success.

## 5. current verdict

```yaml
verdict: PASS_WITH_NOTE
script_created: false
script_candidates_mapped: true
judgment_areas_protected: true
next_allowed_move: run_manual_pipeline_before_script_extraction
```
