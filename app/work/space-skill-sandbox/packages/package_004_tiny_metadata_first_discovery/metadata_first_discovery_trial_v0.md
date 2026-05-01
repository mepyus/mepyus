# Metadata-First Discovery Trial v0

## 0. Status

- status: sandbox candidate
- target: app/work/space-skill-sandbox/packages/package_003_graphify_compact_feedback
- source_space_rule: false
- baseline: false
- automation: false
- graph: false
- ontology: false
- whole_md_scan: false

## 1. Purpose

This trial checks whether a bounded package can be understood first through metadata:

- file names
- paths
- short headers
- explicit status
- closeout
- validation
- compact signals

The goal is to reduce unnecessary deep reading.

## 2. Target Selection

Selected target:

```text
app/work/space-skill-sandbox/packages/package_003_graphify_compact_feedback
```

Reason:

- Package 003 is the source of the metadata-first discovery signal.
- It is bounded and small.
- It includes package brief, Gemini packet, outbox/raw, review bundle, analysis result, user summary, and closeout.
- It is safer than Package 001 for a first metadata trial because Package 001 has three session subpackages.

## 3. Metadata Inventory

Files observed:

```text
analysis_result.md
codex_review_bundle.md
gemini_packet.md
handoff_log.md
outbox/package_003_graphify_compact_feedback_handoff_gemini_outbox_20260430_180646.md
package_brief.md
package_closeout.md
raw/package_003_graphify_compact_feedback_handoff_gemini_raw_20260430_180646.json
raw/package_003_graphify_compact_feedback_handoff_gemini_stderr_20260430_180646.log
user_summary.md
```

## 4. Found / Guessed / Reviewed

### Found

Directly visible from paths, headers, closeout, and validation:

- Package 003 target was Graphify.
- Package 003 verdict was PASS_WITH_WARNING.
- handoff_success_count was 1.
- collect_success was true.
- compact_signal_format_used was true.
- Graphify was not installed.
- graph/ontology/automation/source-space modification/baseline were not created.
- ripgrep fallback appeared in stderr.

### Guessed

Inferred from file structure and package flow:

- `analysis_result.md`, `user_summary.md`, and `package_closeout.md` are sufficient for normal package-level review.
- raw JSON and full outbox are only needed when validating output fidelity or debugging transport.
- the package is a good candidate for bounded metadata-first discovery because it has one session and compact closeout signals.

### Reviewed

Checked by reading short headers and closeout/status sections:

- package_closeout contains compact signal format.
- user_summary contains required package-level report fields.
- codex_review_bundle confirms one outbox and two raw files were collected.
- handoff_log confirms runner_exit_code 0.

## 5. Deep Read Candidates

Deep read if needed:

- `package_closeout.md`: compact signal source
- `analysis_result.md`: source of Graphify lens interpretation
- `user_summary.md`: user-facing package summary
- `codex_review_bundle.md`: transport collection evidence

Deep read only for debugging:

- `outbox/...md`: if analysis_result seems inconsistent
- `raw/...json`: if parsing or model response fidelity is questioned
- `raw/...stderr.log`: if warning classification is needed

Usually skip:

- full `gemini_packet.md` after brief is known
- full raw JSON when closeout and user summary already agree

## 6. Did Metadata-First Reduce Reading?

Yes, for this bounded package.

A useful package-level understanding was obtained from:

- file inventory
- first 60-90 lines of brief/closeout/summary/review bundle
- short stderr check

This avoided reading:

- full raw JSON
- full outbox
- whole md space
- unrelated packages

## 7. Small Script Candidate

Candidate only:

```text
package_metadata_scan.sh
```

Possible bounded behavior:

- input: one package directory
- read: file paths, first N lines of selected `.md`, byte counts for raw/stderr
- output: package-local metadata report
- must not: scan whole md space, infer truth, create graph, modify existing package results

Do not implement yet.

## 8. Risk

Metadata-first can become a new document layer that grows too large.

Guardrail:

- one bounded package only
- compact report
- no graph/ontology language unless explicitly framed as reading aid
- Found / Guessed / Reviewed labels required

## 9. Closeout

This is a sandbox metadata-first discovery trial only.
No graph, ontology, source-space modification, baseline, automation, hook, MCP, watch mode, router, controller, schema, script implementation, Gemini result auto-application, or production workflow was created.
