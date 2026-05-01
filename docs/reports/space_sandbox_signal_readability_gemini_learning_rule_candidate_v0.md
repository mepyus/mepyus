# Space-Sandbox Signal Readability and Gemini Learning Rule Candidate v0

## 1. Status

- status: candidate only
- use: current-use learning and signal-readability rule candidate
- paired_with: `docs/reports/space_sandbox_lens_camera_rereading_rule_candidate_v0.md`
- baseline: false
- official_workflow: false
- implementation_instruction: false
- automation_instruction: false
- policy_or_template: false

This file is not a baseline, official workflow, policy, template, automation plan, ledger specification, or source-space law. It records a current operating rule candidate for reading Gemini/Codex/sandbox mistakes as signals that the future space can reread.

## 2. Why this rule exists

The recent sandbox loop repeatedly showed that a session can produce useful content while still failing at operating metadata:

- state tracking
- package numbering
- section completeness
- table or block integrity
- reuse detection
- wording discipline
- role boundary control
- implementation overreach

Earlier external-material work already taught the same principle. Graphify, harness engineering, mini-swe-agent, tool affordance, and external lens rereads were not treated as direct adoption instructions. They were read as lenses, thought assets, caution assets, and bounded signals.

Therefore Gemini mistakes should not be treated only as local errors to correct. They should be read as signals about how the model reads, overreads, forgets, generalizes, or drifts.

## 3. Core rule: failure is a signal, not just a defect

When Gemini makes a mistake, do not immediately collapse the event into:

```text
Gemini wrong -> fix this run -> continue
```

Instead read it as:

```text
Gemini output / stderr / omission / overreach
-> observed signal
-> signal class
-> likely reading failure
-> package-level feedback
-> next brief / watch / not_actionable
-> future-readable memory
```

The goal is not to make one session perfect. The goal is to build a small sensory network that lets future Codex, Gemini, ChatGPT, and the eventual program/space understand why a reading failed and what structure may reduce recurrence.

## 4. External-material precedent

The external-material phase already used this discipline:

- Graphify was treated as a graph-layer candidate and caution asset, not a graph adoption mandate.
- Harness engineering was treated as a provenance and boundary lens, not an agent-controller implementation.
- Tools-live-beyond-maker material became an affordance/caller-shift lens, not a skillification order.
- mini-swe-agent became a small bounded execution lens, not a framework adoption mandate.
- External lens synthesis produced thought assets and dangerous assumptions, not source-space law.

The recurring pattern was:

```text
external material
-> lens fragment
-> internal fit check
-> borrow / hold / reject
-> no direct promotion
```

The same pattern should apply to Gemini behavior:

```text
Gemini behavior
-> reading-failure signal
-> internal fit check
-> next_brief / watch / not_actionable
-> no direct automation or policy
```

## 5. Signal classes for Gemini and sandbox runs

Use these signal classes as reading aids, not rigid schema:

### state_tracking_signal

Gemini loses or over-advances accepted/hold/current package state.

Examples:

- treating a Hold package as accepted
- omitting recently accepted packages
- regressing the next package number

Reading:

- this is a memory/state tracking failure
- it suggests Gemini needs explicit state context or an externalized memory aid
- it does not prove the package content is invalid

### section_completeness_signal

Gemini omits a required section, changes section names, or folds a required section into another section.

Reading:

- this is output-contract drift
- it may be handled by required-section plans and final section checks
- if the missing section affects judgment, Hold may be appropriate

### format_integrity_signal

Gemini produces table misalignment, field shifting, or self-check mismatch.

Reading:

- Markdown tables are risky for long structured outputs
- block format may reduce alignment risk in some cases
- block format is a working preference, not a policy or proof

### reuse_memory_signal

Gemini mislabels a previously analyzed file as unused, forgets a prior artifact, or fails candidate-level reuse checks.

Reading:

- conversation-memory-only tracking is insufficient for reliable reuse prevention
- a ledger candidate may be designed, but not implemented without approval
- reuse failure is a process-memory signal, not merely a bad candidate choice

### role_boundary_signal

Gemini or Codex drifts from its role:

- Gemini proposes user interviews instead of preparing a user decision aid
- Gemini turns design notes into implementation suggestions
- Codex directly executes tasks assigned to Gemini/User control

Reading:

- role confusion must be recorded as a boundary signal
- the correction should preserve User as final controller
- do not solve role drift by adding automation too early

### implementation_drift_signal

The output moves from reading/design into creating files, automation, workflow, policy, template, graph, ontology, router, controller, hook, MCP, watch mode, or baseline.

Reading:

- this is overreach
- the safer move is a design candidate or risk note
- implementation requires explicit user approval

### tone_confidence_signal

Gemini uses conclusion-heavy or authority-like language:

- confirmed
- proved
- stable inheritance
- fully secured
- fundamentally solved
- maturity/progress claims

Reading:

- the output may still be useful
- the conclusion needs bounded wording
- require evidence/interpretation separation and what-not-to-infer

### category_confusion_signal

Gemini misclassifies artifact type:

- metadata scan report as validation record
- package brief as worker guide
- closeout as official workflow

Reading:

- this is a lens/category failure
- it should trigger category fit checks
- it should not automatically invalidate the selected file if the selected file remains usable

## 6. Action buckets

Signals should be routed into action buckets:

### next_brief

Use when the signal should shape the next Gemini/Codex package brief.

Examples:

- require explicit state summary
- require candidate-level reuse check
- require section plan
- require block format for signal extraction
- require role-boundary restatement

### watch

Use when the signal is real but not enough to change the next brief by itself.

Examples:

- occasional overconfident wording
- one ambiguous category label
- one non-selected candidate mistake

### not_actionable

Use when the signal is already bounded or only confirms an existing boundary.

Examples:

- no source-space promotion
- no baseline change
- no automation created
- no forbidden tool path entered

## 7. Session judgment rule

Do not over-focus on whether one session is perfect.

Judge a session at two levels:

### local output value

Ask:

- Did the output answer the immediate task?
- Did it stay bounded enough?
- Is the selected evidence usable?
- Did the error affect the core judgment?

### learning signal value

Ask:

- What did Gemini misread?
- Why did it misread?
- Was the mistake caused by memory load, format pressure, role confusion, category ambiguity, or overconfidence?
- What future-readable structure would help?
- Should this become next_brief, watch, or not_actionable?

A session can be accepted with pattern notes even when it contains minor Gemini errors. A session should be held when the error changes the judgment, violates boundaries, or corrupts the intended evidence.

## 8. Whole-space orientation

Each session is a small observation inside the whole space/sandbox rereading process.

Do not let the session become the whole problem.

The intended frame is:

```text
whole space / sandbox memory
-> one bounded observation
-> signal extraction
-> failure-pattern memory
-> future-readable adjustment
-> return to whole-space direction
```

The purpose of package work is not to polish isolated outputs. The purpose is to make the space more readable by future agents and programs.

## 9. Future program / small sensory network rule

Treat the current records as early sensory wiring for a future program or space-reading organ.

Useful records should help future systems answer:

- What was observed?
- Through which lens?
- With which camera?
- What evidence supports it?
- What interpretation was added?
- What should not be inferred?
- What signal class appeared?
- What action bucket was chosen?
- What changed in the next brief?
- What remained watch-only?

The current task is not to build the program. It is to leave records that the future program can read.

## 10. Gemini learning instruction

Before the next read-heavy or synthesis run, Gemini should read:

1. `docs/reports/space_sandbox_lens_camera_rereading_rule_candidate_v0.md`
2. `docs/reports/space_sandbox_signal_readability_gemini_learning_rule_candidate_v0.md`

Gemini should then produce a short calibration note answering:

1. Why is a Gemini mistake a signal, not only a defect?
2. What is the difference between correcting a session and recording a reading-failure pattern?
3. Which signal classes are most relevant to Gemini's recent behavior?
4. What is the difference between `next_brief`, `watch`, and `not_actionable`?
5. Why should block format not become a policy just because it helped once?
6. Why should a ledger candidate not become an implementation without approval?
7. How should Gemini preserve evidence/interpretation separation?
8. What should Gemini avoid promoting?
9. How should Gemini keep the whole-space frame while executing one bounded session?

Gemini should not execute a new analysis until it has produced this calibration note.

## 11. Current forbidden moves

- no source-space promotion
- no baseline change
- no graph/ontology/router/controller creation
- no automation or automatic verification
- no policy/template/workflow creation
- no ledger file creation without explicit user approval
- no merge plan
- no structural redesign
- no cleanup/delete/move
- no treating signal classes as rigid schema
- no treating this rule candidate as law

## 12. Current recommended loop

1. Start from whole-space / sandbox orientation.
2. Run one bounded observation.
3. Separate evidence from interpretation.
4. Identify signal classes.
5. Route each signal to `next_brief`, `watch`, or `not_actionable`.
6. Record Gemini/Codex reading-failure patterns when present.
7. Avoid local correction loops unless the error changes judgment or violates boundaries.
8. Convert repeated patterns into candidate memory structures only after repeated evidence.
9. Return to User/ChatGPT for direction-level judgment.

## 13. Closing note

This file is a current-use learning rule candidate.
It exists to connect external-material lens discipline, sandbox signal readability, and Gemini performance calibration.
It must not be promoted without explicit user approval.
