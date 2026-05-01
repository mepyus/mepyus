# First Tiny Script Decision v0

## 0. Status

- status: sandbox decision candidate
- selected_candidate: package_metadata_scan.sh
- implementation_created: false
- prototype_approved: false
- source_space_rule: false
- baseline: false
- automation: false

## 1. Decision

Recommend `package_metadata_scan.sh` as the first tiny script prototype candidate.

Do not implement it yet.

Implementation requires explicit user approval after reviewing this decision package.

## 2. Why This Candidate

`package_metadata_scan.sh` is the safest first prototype because it has:

- a bounded input: one package directory
- a package-local output
- a repeated manual bottleneck observed in Package 004
- a clear non-judgment role
- a direct usefulness path for Codex validation
- lower risk than stderr classification, result compression, global locating, or status approval scripts

## 3. What It Should Do

If approved later, the script should:

- accept one package directory
- confirm it is under `app/work/space-skill-sandbox/packages/`
- list package-local files
- read only short headers from selected package-level markdown files
- record raw/outbox/stderr filenames and byte counts
- produce a compact metadata report
- mark `reviewed_by: pending`

## 4. What It Must Not Do

The script must not:

- scan the whole md space
- read outside the input package
- follow arbitrary links
- parse all raw JSON by default
- read full outbox by default
- overwrite existing package artifacts by default
- create graph, ontology, schema, router, or controller
- decide whether a package passed
- decide next package
- mark guesses as reviewed
- modify source-space

## 5. Input / Output Boundary

Input:

```text
PACKAGE_DIR
```

Allowed root:

```text
app/work/space-skill-sandbox/packages/
```

Candidate output:

```text
<PACKAGE_DIR>/metadata_scan_report.md
```

Initial overwrite policy:

```text
refuse if metadata_scan_report.md already exists
```

## 6. Failure Safety

A safe prototype should:

- fail before writing when input is invalid
- write to a temporary file first
- move into place only after complete generation
- refuse overwrite by default
- exit non-zero on invalid scope
- leave existing package files unchanged

## 7. Smoke Test Requirements

Minimum smoke tests before calling the prototype usable:

1. `bash -n scripts/sandbox/package_metadata_scan.sh`
2. run on `app/work/space-skill-sandbox/packages/package_003_graphify_compact_feedback`
3. confirm output is created inside that package only
4. confirm no source-space files changed
5. confirm whole md space was not scanned
6. rerun and confirm overwrite refusal
7. run with invalid path outside packages and confirm non-zero exit
8. inspect report for compactness and `reviewed_by: pending`

## 8. Approval Conditions

User must approve:

- script name: `package_metadata_scan.sh`
- script path: `scripts/sandbox/package_metadata_scan.sh`
- allowed input root
- output filename
- overwrite refusal behavior
- max header lines
- raw/outbox/stderr handling
- smoke package target

## 9. Why Other Candidates Are Not First

`stderr_signal_classifier.sh`:

- higher false-classification risk
- needs more warning samples

`package_result_compressor.sh`:

- may hide nuance and boundary issues

`run_review_locator.sh`:

- can drift into global index/controller behavior

`package_collect_verifier.sh`:

- useful later, but less directly tied to metadata-first bottleneck

## 10. Stop Point

Stop here.

This package recommends the prototype candidate but does not authorize implementation.

Implementation must wait for explicit user approval.

## 11. Closeout

This is a sandbox prototype decision document only.
No script was implemented.
No source-space promotion was performed.
No baseline was created.
No automation, hook, MCP, watch mode, graph, ontology, router, controller, schema, Gemini result auto-application, or production workflow was created.
