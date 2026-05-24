# External Reference Intake - Claude Code Goal 2026-05-12 Candidate v0

## 1. Status

```text
Document = external reference intake
Status = CANDIDATE_EXTERNAL_REFERENCE_INTAKE
Authority = source interpretation only
Not baseline
Not official workflow
Not automation
Not registry
Not current-position update
```

## 2. Source

```text
Source title = Claude를 목표를 향해 계속 작동하게 하기
Source URL = https://code.claude.com/docs/ko/goal
Source owner = Anthropic / Claude Code Docs
Read date = 2026-05-12
```

## 3. Why Read

```text
User asked whether this source should be run through our original-interpretation criteria.
```

The source is relevant because it describes:

```text
goal condition
multi-turn continuation
post-turn evaluator
visible proof requirement
clear / resume / non-interactive execution
requirements and limits
```

## 4. What The Source Says In Its Own Frame

The page explains Claude Code `/goal` as a session-scoped way to set a completion condition.

Key source claims, paraphrased:

```text
1. A goal defines a condition and Claude continues across turns until that condition is judged satisfied.
2. A separate smaller evaluator checks after each turn whether the condition is met.
3. Effective conditions need a measurable final state, explicit verification, and constraints.
4. The evaluator judges only what Claude has shown in the conversation; it does not independently inspect files or run commands.
5. The goal is session-scoped, can be checked or cleared, and can resume with a continued session.
6. It is different from timed loops, Stop hooks, and auto mode.
```

## 5. Original-Interpretation Pull

The most relevant judgment for our space is not:

```text
use Claude /goal
copy the feature
automate our loop
replace current-position
make an evaluator decide authority
```

The relevant judgment is:

```text
A continuation loop is only safe when the stop condition, visible proof, constraints, and evaluator limits are explicit.
```

## 6. Fit With Our Current Structure

This source aligns with our existing watch discipline:

```text
Receipt is not approval.
Return is trace first.
Evaluator can only judge visible evidence.
Goal/condition must not become authority by itself.
Automation-like continuation needs explicit stop boundaries.
```

It also strengthens one missing lens:

```text
completion-condition visibility
```

For our packets, that means:

```text
If a worker is asked to continue until done,
the packet must say what visible evidence proves done.
```

## 7. Local Gate Classification

```text
Classification = RETURN_ONLY
Modifier = EXTERNAL_REFERENCE_WITH_WATCH
```

Reason:

```text
The source is useful as a reference lens.
It does not require immediate sandbox execution.
It should not trigger automation or workflow creation.
It can return to space as a candidate condition-writing lens.
```

## 8. Candidate Reusable Lens

```text
Goal Condition Lens:
  final state:
  visible proof:
  constraints:
  evaluator limits:
  stop / clear condition:
  what must not be inferred:
```

Authority:

```text
candidate lens only
not schema
not workflow
not automation
```

## 9. Watch

```text
/goal becomes imported automation fantasy
evaluator becomes authority
visible proof is forgotten
condition becomes broad and unverifiable
session-scoped goal is mistaken for persistent current-position
stop condition is omitted
```

## 10. Placement

```text
Placement = RETURN_TO_SPACE_VALUE_WITH_WATCH
```

## 11. Next Pull

```text
Use the Goal Condition Lens on one future worker/Gemini packet.
Check whether it reduces execution-boundary ambiguity without creating automation.
```

`STATUS: EXTERNAL_REFERENCE_INTAKE_CLAUDE_GOAL_PREPARED_WITH_WATCH`
