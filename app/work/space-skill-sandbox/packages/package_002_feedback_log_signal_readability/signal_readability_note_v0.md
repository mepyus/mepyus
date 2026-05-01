# Signal Readability Note v0

## 0. Status

- status: sandbox candidate
- source_space_rule: false
- baseline: false
- automation: false
- log_parser: false

## 1. Purpose

This note defines how Codex should make package signals readable enough for the next package brief and user review.

The goal is compact interpretation, not full log reproduction.

## 2. Reading Rule

Do not read every stderr line as a failure.

First ask:

- Did the session exit successfully?
- Did the output answer the brief?
- Did the signal indicate environment, tool use, prompt clarity, quota/cost, output quality, boundary risk, or next-package adjustment?
- Does this require action now, watch, or no action?

## 3. Action Buckets

### next_brief

Use when the signal should change the next package brief.

Package 001 examples:

- ask for success-with-warning classification
- keep packages small and timeout-aware
- clarify when tool use is unnecessary

### watch

Use when the signal is real but not yet actionable.

Package 001 examples:

- quota retry
- Node deprecation warning
- ripgrep fallback

### not_actionable

Use when the signal confirms boundaries or has no current design implication.

Package 001 examples:

- no source-space modification
- no automation
- no baseline

## 4. Next Brief Compact Principle

The next package brief should include only:

- purpose
- references
- boundary
- signal focus
- expected package-level output
- review questions

Do not list every log line.
Do not require a rigid document template.
Do not convert warnings into rules.

## 5. Success-With-Warning

Package validation should distinguish:

```text
PASS
PASS_WITH_WARNING
PASS_WITH_NOTE
FAIL
```

Candidate meaning:

- PASS: output usable, no notable warning
- PASS_WITH_WARNING: output usable, execution warning should be watched
- PASS_WITH_NOTE: output usable, design note or missing context exists
- FAIL: output missing, boundary violated, or transport failed

This is a candidate vocabulary only. It is not a source-space rule.

## 6. Scriptable Handoff Implication

Do not modify scripts yet.

The next script-layer candidate, if repeated evidence accumulates, may be:

- classify exit code 0 plus stderr patterns as success-with-warning
- include warning summary in `codex_review_bundle.md`
- keep raw logs intact

This remains a later candidate, not Package 002 implementation.

## 7. Closeout

This is a sandbox signal readability note only.
No automatic log parser was created.
No script was modified.
No source-space promotion was performed.
No baseline was created.
No automation, hook, MCP, watch mode, router, controller, schema, agent implementation, Gemini result auto-application, or production workflow was created.
