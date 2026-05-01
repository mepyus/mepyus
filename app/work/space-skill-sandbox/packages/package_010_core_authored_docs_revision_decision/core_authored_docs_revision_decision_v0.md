# Core Authored Docs Revision Decision v0

## 0. Status

- status: sandbox decision candidate
- script_modified: false
- source_space_rule: false
- baseline: false
- automation: false
- graph_index: false
- ontology: false

## 1. Decision

Recommendation: prepare a small Package 011 revision proposal for `package_metadata_scan.sh`.

The revision should add a metadata-level label for package-specific authored docs, but it should not rank, review, or interpret their meaning.

## 2. Problem Observed

Package 009 showed that the current report is useful for package-local orientation, but its deep-read candidate heuristic favors standard records:

- `user_summary.md`
- `package_closeout.md`

In Package 006, the package-specific authored docs were visible in `Files Seen` and header excerpts, but not clearly separated as a first review surface:

- `small_execution_unit_registry_candidate_v0.md`
- `priority_note_v0.md`

This can leave Codex or ChatGPT reading the summary before the actual authored substance of the package.

## 3. Why the Distinction Helps

Standard package records answer:

- What was the package?
- What was the verdict?
- What boundary was claimed?
- What did the user need to know?

Core authored docs usually answer:

- What new candidate, lens, registry, decision, checklist, or methodology was produced?
- What should a later package actually inspect?
- What repeated package-loop signal was captured?

Separating the two would reduce repeated manual scanning because Codex can quickly see:

- standard records for validation and boundary review
- core authored docs for substance review
- raw/outbox/stderr for debugging only

## 4. Safe Metadata-Level Criteria

The script may safely label files as candidate core authored docs when a package-local file is:

- a markdown file at package root
- not one of the standard package records
- not `metadata_scan_report.md`
- not under `raw/` or `outbox/`
- not a handoff or transcript artifact

Standard package records may include:

- `package_brief.md`
- `user_summary.md`
- `package_closeout.md`
- `codex_review_bundle.md`
- `codex_validation.md`
- `handoff_log.md`
- `gemini_packet.md`
- `metadata_scan_report.md`

## 5. What Must Remain Human Judgment

The script must not decide:

- whether a core authored doc is correct
- whether it should become a rule
- whether it is more important than another doc
- whether a package passed
- whether a signal should be promoted
- whether source-space should change

The script may only say:

- this looks like a package-local authored doc candidate
- review is pending
- user/Codex judgment is required

## 6. Proposed Revision Shape

If approved in Package 011, add one small section:

```text
## Core Authored Doc Candidates

- <root-level non-standard markdown files>

reviewed_by: pending
```

Optionally adjust `Deep-Read Candidates` to include:

1. core authored doc candidates
2. `package_closeout.md`
3. `user_summary.md`
4. `codex_review_bundle.md` or `analysis_result.md` when present

This remains a metadata aid, not a ranking engine.

## 7. Revision Boundary

Allowed:

- small shell-only revision
- bounded package input unchanged
- package-local output unchanged
- overwrite refusal unchanged
- `reviewed_by: pending` unchanged
- no new dependencies

Forbidden:

- graph/index creation
- ontology creation
- router/controller behavior
- whole md space scan
- interpretation of document correctness
- automatic promotion of signals
- output outside the target package

## 8. Verdict

The revision is useful and small enough to consider next, but it requires explicit user approval before implementation.

Verdict: PASS_WITH_STOP_POINT

