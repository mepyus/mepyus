# Package-Based Agent Workflow Design v0

## 0. Status

- status: sandbox candidate
- source_space_rule: false
- baseline: false
- automation: false
- relay_v1: false
- production_workflow: false

## 1. Purpose

This document defines a sandbox candidate workflow for moving from session-level correction to package-level feedback.

The goal is not to make Codex, Gemini, ChatGPT, or the user do more work. The goal is to stop treating every session as a separate event and start collecting intent, execution, evidence, validation, and user judgment at package scale.

## 2. Core Shift

Current bottleneck:

- session-level copy/paste handoff
- fragmented waiting
- fragmented validation
- repeated output-format correction
- weak package-level learning

Target operating shape:

- package brief
- Codex package plan
- Gemini execution packet
- manual script handoff
- raw/outbox capture
- Codex validation bundle
- user summary
- ChatGPT direction review
- next package adjustment

## 3. Role Split

### User

- owns direction
- makes final judgment
- approves escalation, promotion, or closure
- is not reduced to a copy/paste relay

### ChatGPT

- reviews direction and structure
- checks boundary drift
- challenges premature promotion or automation
- should receive compressed package summaries, not every raw session trace

### Codex

- acts as package orchestrator and validator
- creates package structure
- separates Codex work from Gemini work
- validates Gemini results
- prepares user-facing summaries
- creates the next package candidate when appropriate

### Gemini

- acts as execution and analysis worker
- drafts or analyzes within a bounded package
- returns results into captureable outbox/raw evidence
- does not own source-space modification, baseline creation, or promotion

## 4. Package Folder Candidate

Package folders may use this structure:

```text
app/work/space-skill-sandbox/packages/
  package_001_example/
    package_brief.md
    codex_plan.md
    gemini_packet.md
    handoff_log.md
    raw/
    outbox/
    codex_review_bundle.md
    codex_validation.md
    user_summary.md
    package_closeout.md
```

Each folder is a bounded work unit. The folder is not a source-space interface by itself and does not imply promotion.

## 5. Package State Candidate

The candidate state sequence is:

```text
draft
→ planned
→ approved_for_handoff
→ sent_to_gemini
→ gemini_returned
→ collected
→ codex_validated
→ user_reviewed
→ closed
```

Scripts may record transport facts such as `sent_to_gemini`, `gemini_runner_returned`, and `collected`.

Scripts must not decide whether a package is valid, promoted, baseline-ready, or closed.

## 6. Minimal Brief Discipline

Package prompts should avoid excessive templates.

A useful brief usually needs only:

- purpose
- references
- forbidden boundaries
- expected outputs
- review questions

The package should leave enough room for tool judgment so that tool mistakes become observable signals instead of hidden compliance failures.

## 7. Feedback Loop

Package closeout should ask:

- What ran?
- What changed?
- What failed?
- What was learned?
- What should be adjusted in the next package?
- What requires user judgment?

The point is package-level feedback, not session-level micromanagement.

## 8. Guardrails

This workflow must not create:

- background automation
- watch mode
- hook
- MCP auto-connection
- source-space automatic modification
- baseline
- Relay v1.0 declaration
- router
- controller
- schema
- ontology
- Gemini result auto-application

## 9. Closeout

This is a sandbox package workflow candidate only.
No automation was created by this document.
No source-space promotion was performed.
No baseline was created.
No Relay v1.0 was declared.
No production workflow was created.
