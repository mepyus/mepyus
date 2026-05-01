# Small Execution Unit Registry Candidate v0

## 0. Status

- status: sandbox candidate
- implementation_created: false
- source_space_rule: false
- baseline: false
- automation: false
- controller: false
- whole_md_scan: false

## 1. Purpose

This registry compares small execution unit candidates that could reduce repeated package-loop bottlenecks.

The registry is not an implementation plan by itself. It is a decision aid.

## 2. Candidate Comparison

### 1. package_metadata_scan.sh

- purpose: produce compact metadata-first discovery for one bounded package
- input: one package directory
- output: package-local `metadata_scan_report.md`
- read scope: paths, file sizes, first N lines of selected package files, raw/outbox/stderr filenames
- write scope: one new package-local report, no overwrite by default
- risk: output bloat, guessed/reviewed over-automation, scope drift
- route/session fit: Codex package orchestration, pre-validation discovery
- implement now: no
- candidate strength: high
- user judgment required: yes, before implementation

### 2. package_status_summary.sh

- purpose: summarize package state from package-local files
- input: one package directory
- output: package-local status summary or stdout
- read scope: package brief, closeout, validation, handoff log
- write scope: candidate package-local summary only
- risk: may imply completion or approval if wording is too strong
- route/session fit: Codex validation support, user handoff summary
- implement now: no
- candidate strength: medium-high
- user judgment required: yes

### 3. package_collect_verifier.sh

- purpose: verify that handoff/collect produced expected outbox/raw/stderr bundle
- input: one package directory
- output: package-local verification note or stdout
- read scope: codex_review_bundle, outbox/raw/stderr file presence, handoff log
- write scope: candidate package-local verification note only
- risk: may be mistaken as content validation
- route/session fit: scriptable handoff transport validation
- implement now: no
- candidate strength: medium
- user judgment required: yes

### 4. stderr_signal_classifier.sh

- purpose: classify stderr signals into success-with-warning / auth / quota / tool-use candidates
- input: package-local stderr file or package directory
- output: package-local warning classification
- read scope: stderr only, maybe outbox invocation status
- write scope: candidate package-local warning report
- risk: false classification, security term overreach, treating warning as rule
- route/session fit: Codex validation support
- implement now: no
- candidate strength: medium
- user judgment required: yes

### 5. package_result_compressor.sh

- purpose: compress package closeout/user summary into ChatGPT-facing report
- input: package directory
- output: compact user summary or stdout
- read scope: package closeout, user summary, validation
- write scope: package-local compressed summary candidate
- risk: loses nuance, hides boundary issues
- route/session fit: User to ChatGPT handoff
- implement now: no
- candidate strength: medium
- user judgment required: yes

### 6. evidence_path_checker.sh

- purpose: check whether referenced evidence paths exist inside a bounded package
- input: package directory and package-local markdown file
- output: missing/present path report
- read scope: package-local paths only
- write scope: optional package-local report
- risk: can drift into global link checker or source-space scanner
- route/session fit: Codex validation support
- implement now: no
- candidate strength: medium-low
- user judgment required: yes

### 7. run_review_locator.sh

- purpose: locate run/review files for a package or run id
- input: run id or package id
- output: matching package-local or sandbox run/review paths
- read scope: bounded sandbox run/review directories, not full md space
- write scope: none or package-local locator note
- risk: could drift toward global index/controller
- route/session fit: Codex navigation support
- implement now: no
- candidate strength: low-medium
- user judgment required: yes

## 3. Candidate Ranking

1. `package_metadata_scan.sh`
2. `package_status_summary.sh`
3. `package_collect_verifier.sh`
4. `stderr_signal_classifier.sh`
5. `package_result_compressor.sh`
6. `evidence_path_checker.sh`
7. `run_review_locator.sh`

## 4. First Prototype Candidate

Best first prototype candidate:

```text
package_metadata_scan.sh
```

Reason:

- most directly tied to the current bottleneck
- bounded to one package directory
- can avoid judging content
- can reduce repeated Codex metadata-reading work
- has a clear stop point before implementation

This is not implementation approval.

## 5. Candidates To Hold

Hold for later:

- `stderr_signal_classifier.sh`: needs more warning samples before classification is safe
- `package_result_compressor.sh`: risk of hiding nuance
- `run_review_locator.sh`: can drift toward global index/controller

## 6. Role Boundaries

Codex:

- validates candidate output
- decides what to deep-read
- writes user summary

Gemini:

- may consume compact metadata when asked
- does not own script execution or validation

ChatGPT:

- reviews direction and boundary drift from package-level summary

User:

- approves or rejects prototype implementation
- remains final judge

## 7. Closeout

This is a sandbox registry candidate only.
No script was implemented.
No source-space promotion was performed.
No baseline was created.
No automation, hook, MCP, watch mode, graph, ontology, router, controller, schema, Gemini result auto-application, or production workflow was created.
