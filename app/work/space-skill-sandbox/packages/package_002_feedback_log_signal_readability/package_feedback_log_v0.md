# Package Feedback Log v0

## 0. Status

- status: sandbox candidate
- source_space_rule: false
- baseline: false
- automation: false
- log_parser: false
- script_modified: false

## 1. Purpose

This document defines a compact package-level feedback log for reading session signals without turning them into rules too early.

The goal is to convert:

```text
raw / stderr / outbox / validation
→ package-level signal
→ next package brief adjustment
```

The goal is not to automate log parsing or promote single-session warnings into permanent policy.

## 2. Signal Classes

### execution_environment_signal

Signals from the runtime environment rather than from the package intent.

Package 001 evidence:

- Gemini model capacity retry messages in Session 1, 2, and especially Session 3
- missing ripgrep fallback to GrepTool

Reading:

- repeated enough to watch
- not a package failure when exit code is 0 and usable output exists
- should inform timeout and retry expectations, not content rules

### tool_usage_signal

Signals from Gemini or CLI tool usage during execution.

Package 001 evidence:

- Session 3: `grep_search` invalid regular expression pattern `(?i)borrow`

Reading:

- likely tool syntax mismatch or model tool-use assumption
- should be captured as success-with-warning
- should not immediately trigger script changes

### prompt_brief_clarity_signal

Signals that the brief may have caused avoidable tool use or ambiguity.

Package 001 evidence:

- Session 3 tried grep-style search for `borrow`
- output remained usable and aligned with requested sections

Reading:

- next briefs can explicitly say "do not use tools unless needed" or "analysis from packet context is enough" when external file reads are not essential
- do not over-correct by banning tools globally

### quota_cost_signal

Signals about model capacity, latency, or token/cost pressure.

Package 001 evidence:

- repeated quota reset retries in stderr
- Session 3 took materially longer than Sessions 1 and 2

Reading:

- repeated and worth watching
- next packages should keep sessions small and timeout-aware
- not enough evidence for changing model or architecture

### output_quality_signal

Signals from whether the returned content answered the package need.

Package 001 evidence:

- all three sessions produced usable lens analysis
- Session 3 had noisy stderr but usable output

Reading:

- output quality passed
- stderr warnings should be classified separately from content failure

### boundary_risk_signal

Signals that a run crossed or approached forbidden boundaries.

Package 001 evidence:

- no source-space modification
- no baseline
- no automation
- no Gemini result auto-application
- no production workflow

Reading:

- no boundary violation
- external materials remained lenses, not authority

### next_package_adjustment_signal

Signals that should shape the next package brief.

Package 001 evidence:

- Session 1 requested signal readability
- Session 2 requested diagnostic capture and affordance mapping
- Session 3 requested linear trace and success-with-warning classification

Reading:

- promote to next brief candidate
- do not promote to source-space rule or baseline

## 3. Feedback Log Format

Use this compact format in future package closeouts:

```text
signal:
source:
class:
evidence:
impact:
action: next_brief | watch | not_actionable
why:
boundary:
```

## 4. Package 001 Signal Table

| signal | source | class | action | why |
|---|---|---|---|---|
| quota retry | stderr, sessions 1-3 | quota_cost_signal | watch | repeated, but runs completed |
| grep_search regex error | session 3 stderr | tool_usage_signal | next_brief | avoid unnecessary tool search or specify simple text reading |
| Node deprecation warning | session 3 stderr | execution_environment_signal | watch | environment/tooling warning, not content failure |
| usable output despite stderr | outbox, session 3 | output_quality_signal | next_brief | classify success-with-warning |
| no boundary violation | validation | boundary_risk_signal | not_actionable | confirms boundary held |
| signal readability need | package closeout | next_package_adjustment_signal | next_brief | package feedback should shape future briefs |

## 5. Promotion Discipline

Signals can become:

- next brief adjustment
- watch item
- candidate for later guide
- non-actionable note

Signals do not become:

- source-space rule
- baseline
- automation
- router/controller behavior
- permanent policy from one run

## 6. Closeout

This is a sandbox feedback log candidate only.
No automatic log parser was created.
No script was modified.
No source-space promotion was performed.
No baseline was created.
No automation, hook, MCP, watch mode, router, controller, schema, agent implementation, Gemini result auto-application, or production workflow was created.
