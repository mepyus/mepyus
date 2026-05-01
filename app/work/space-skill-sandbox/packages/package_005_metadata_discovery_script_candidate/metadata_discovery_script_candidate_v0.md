# Metadata Discovery Script Candidate v0

## 0. Status

- status: sandbox candidate
- implementation_created: false
- source_space_rule: false
- baseline: false
- automation: false
- whole_md_scan: false
- graph: false
- ontology: false

## 1. Candidate

Candidate script name:

```text
package_metadata_scan.sh
```

Candidate role:

```text
bounded package metadata discovery helper
```

## 2. Why It May Be Useful

Package 004 showed that Codex could understand Package 003 without reading the full raw JSON, full outbox, or unrelated package files.

The repeated manual steps were:

- list package files
- identify package-level records
- read short headers/status/closeout sections
- identify raw/outbox/stderr artifacts
- separate normal review files from debugging files
- mark which observations are direct evidence vs Codex inference

These steps are repetitive and bounded enough to be a small execution unit candidate.

## 3. What The Script May Read

Allowed input:

```text
one package directory path
```

Allowed reads:

- file paths under that package directory
- file sizes
- first N lines of selected markdown files
- closeout/status headings when present
- raw/outbox/stderr filenames
- byte counts for raw/stderr files

Default bounded files to inspect:

- `package_brief.md`
- `user_summary.md`
- `package_closeout.md`
- `codex_review_bundle.md`
- `codex_validation.md`
- `analysis_result.md`
- `handoff_log.md`
- `review` or `validation` file if package-local

## 4. What The Script Must Not Read

The script must not:

- scan the whole md space
- read outside the provided package directory
- follow arbitrary links
- recursively inspect unrelated packages
- parse all raw JSON by default
- read entire outbox files by default
- treat inferred links as truth

## 5. What The Script May Write

Allowed output:

```text
<package_dir>/metadata_scan_report.md
```

The output must be compact and package-local.

The script should not overwrite existing package artifacts unless explicitly passed a force flag. First candidate behavior should refuse to overwrite.

## 6. What The Script Must Not Write

The script must not write:

- source-space files
- baseline files
- global index files
- graph outputs
- ontology/schema outputs
- files outside the package directory
- modified existing package results

## 7. Found / Guessed / Reviewed Boundary

The script can help with:

### Found

Mechanically list evidence directly visible from filenames and short headers:

- file exists
- status line exists
- closeout exists
- runner exit code line exists
- raw/stderr/outbox files exist

### Guessed

The script may only label these as `candidate_guess`, not fact:

- likely deep-read candidates
- likely skip candidates
- likely package type
- possible warning class

### Reviewed

The script must not assign `reviewed` by itself.

`Reviewed` requires Codex or user validation.

The script may reserve a field:

```text
reviewed_by: pending
```

## 8. Candidate Output Shape

Compact output should include:

```text
package:
scan_scope:
files_seen:
found:
candidate_guess:
review_needed:
deep_read_candidates:
usually_skip:
warnings:
boundary_check:
reviewed_by: pending
```

## 9. Use In Codex / Gemini / ChatGPT / User Loop

Codex:

- uses report to decide what to deep-read
- validates guessed fields
- writes package-level summary

Gemini:

- may receive compact metadata instead of entire package contents
- should not treat metadata as complete truth

ChatGPT:

- receives user summary and package-level signals
- reviews direction and boundary drift

User:

- decides whether script implementation proceeds
- judges whether metadata output is actually readable

## 10. Usefulness Judgment

Candidate suitability:

```text
high as candidate
not approved for implementation yet
```

Reason:

- repeated manual steps are clear
- bounded input is possible
- output can remain package-local
- script can avoid judgment if Found/Guessed/Reviewed boundary is explicit

Why not implement immediately:

- only one successful metadata-first trial exists
- output bloat risk remains
- first implementation needs user approval
- overwrite and scope behavior need preflight decisions

## 11. Stop Point

Before implementation, user must approve:

- script name
- input scope
- output path
- overwrite behavior
- max header lines
- whether raw/outbox are summarized by size only or shallow header

## 12. Closeout

This is a sandbox script candidate document only.
No script was implemented.
No source-space promotion was performed.
No baseline was created.
No automation, hook, MCP, watch mode, graph, ontology, router, controller, schema, Gemini result auto-application, or production workflow was created.
