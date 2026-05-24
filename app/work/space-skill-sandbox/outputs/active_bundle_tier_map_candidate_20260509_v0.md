# Active Bundle Tier Map Candidate — 2026-05-09

## 0. Status

- candidate only
- bundle tier map candidate only
- live-use with watch
- not baseline
- not schema
- not registry
- not routing authority
- not automation
- not production workflow
- not replacement for user judgment

## 1. Purpose

This document preserves the Package V / Trials 004-008 active-bundle tier finding as a practical bundle selection aid.

It exists to reduce rediscovery cost, choose the smallest sufficient bundle, prevent broad repo reading, preserve layer-specific neighbor logic, and avoid fixed route authority.

The core candidate principle:

```text
Start with the smallest bundle that can answer the task.
Add one neighbor only when the task requires a missing layer.
```

## 2. Bundle Tier Map

| Tier | Name | Bundle Contents | Confirmed Use | Not Enough For | Add Neighbor When | Status |
|---|---|---|---|---|---|---|
| Tier 1 | Core | 3 files: `result_oriented_operating_stack_closeout`; `result_usefulness_gate`; `mission_packet_result_contract` | core result-oriented judgment recovery | maturation-ready asset | judgment provenance is needed | candidate with watch |
| Tier 2 | Asset | Tier 1 + `judgment_provenance_record` | judgment capsule production; policy mutation detection; operating requirement judgment | tool calibration | tool behavior, strength/drift, or safe scope must be judged | candidate with watch |
| Tier 3 | Calibration | Tier 2 + `tool_profile_record` | tool calibration; strength/drift/safe scope/next-use correction | user intent / routing drift | user trigger or Supervisor routing needs interpretation | candidate with watch |
| Tier 4 | Routing | Tier 3 + `user_facing_routing_card` | routing drift detection; user trigger / tool capability / Supervisor drift | event-level root cause analysis | actual sequence, timestamps, or process causality are needed | candidate with watch |
| Future Tier 5 | Causality | Tier 4, or relevant smaller tier, + bounded RUNLOG slice | event-level causality; why a policy changed; actual drift sequence | full repo causality or unrestricted trace reading | only when causal maturation is the task | not tested |

## 3. Neighbor Selection Rule Candidate

Start with the smallest bundle that can answer the task.

Add exactly one neighbor only when the task requires a missing layer.

```text
Need core operating judgment -> Tier 1
Need recoverable asset / provenance -> Tier 2
Need tool calibration -> Tier 3
Need routing/user trigger interpretation -> Tier 4
Need event-level causality -> Future Tier 5 with bounded RUNLOG slice
```

This rule is candidate with watch.

It is not routing authority, automatic file selection, or permission to ignore user judgment.

## 4. Trial Evidence Summary

### Trial 004

evidence_type:
GEMINI_TRIAL_EVIDENCE / USER_PROVIDED_SUMMARY; Package T setup file observed.

confirmed:
3-file bundle recovered core result-oriented judgment.

missing:
provenance maturity and capsule readiness were limited without a provenance neighbor.

### Trial 005

evidence_type:
GEMINI_TRIAL_EVIDENCE / USER_PROVIDED_SUMMARY.

confirmed:
Adding judgment provenance improved capsule maturity and made source-of-judgment handling more usable.

missing:
Tool calibration remained under-supported without tool profile context.

### Package U

evidence_type:
GEMINI_TRIAL_EVIDENCE / USER_PROVIDED_SUMMARY.

confirmed:
4-file bundle could detect policy mutation needs and operating requirement changes.

missing:
Not enough for deeper route/tool calibration by itself.

### Trial 006

evidence_type:
GEMINI_TRIAL_EVIDENCE / USER_PROVIDED_SUMMARY.

confirmed:
4-file bundle detected requirements but did not support true calibration.

missing:
tool_profile_record neighbor was needed.

### Trial 007

evidence_type:
GEMINI_TRIAL_EVIDENCE / USER_PROVIDED_SUMMARY; tool_profile_record file observed.

confirmed:
Tool profile neighbor enabled tool calibration: strength, drift, safe scope, and next-use correction.

missing:
User intent and routing drift needed routing card context.

### Trial 008

evidence_type:
GEMINI_TRIAL_EVIDENCE / USER_PROVIDED_SUMMARY.

confirmed:
Routing card neighbor enabled routing drift detection across user trigger, tool capability, and Supervisor behavior.

missing:
Event-level root cause analysis still required RUNLOG / raw trace.

### Package V

evidence_type:
GEMINI_TRIAL_EVIDENCE / USER_PROVIDED_SUMMARY. Package V standalone file was not found in the narrow saved-file check for this task.

confirmed:
Synthesized Tier 1-4 bundle map and identified RUNLOG / raw trace as the remaining gap for event-level causality.

missing:
RUNLOG-based causal maturation was not yet tested.

## 5. What This Map Must Not Become

- not fixed routing authority
- not command registry
- not schema
- not baseline
- not automatic file selector
- not proof of global token efficiency
- not permission to ignore user judgment
- not replacement for observation

## 6. RUNLOG Gap

RUNLOG / raw trace is still needed for:

- event-level causality
- why a policy changed
- actual user-Supervisor misrouting
- actual tool drift over time
- token usage history
- success/fail sequence

Do not read full RUNLOG by default.

Future Trial 009 should use a bounded RUNLOG slice only.

The current gap:

```text
semantic maturation is candidate-supported;
causal maturation still needs bounded process-trace evidence.
```

## 7. Watch Items

- tier map becoming routing authority
- active bundle success overgeneralized
- RUNLOG ignored when causality is needed
- adding too many neighbors by habit
- ceremony replacing judgment
- token-saving reducing judgment quality
- routing card becoming command registry
- tool profile freezing model identity
- candidate becoming baseline
- Package V summary treated as observed file evidence without saved report

## Lens Language Addendum — Candidate

Trial 010 / Tolaria contributed one useful external-reference phrase: types can be treated as lenses, not schemas.

evidence_type:
USER_PROVIDED_SUMMARY / GEMINI_TRIAL_EVIDENCE. A saved Trial 010 / Tolaria file was not found in the narrow check for this patch.

This is a language refinement only. Tolaria is not authority, not a product template, and not a direction toward a note app, GUI, or Git-first replacement for RUNLOG.

### Tiers as Lenses, Not Schemas

- Tier 1 is a Core Judgment Lens.
- Tier 2 is an Asset / Provenance Lens.
- Tier 3 is a Tool Calibration Lens.
- Tier 4 is a Routing / User Trigger Lens.
- Tier 5 is a Causal Maturation Lens.

These are not mandatory schemas.

They are not routing authority.

They are not automatic read rules.

They are candidate lenses for selecting the smallest sufficient context.

A tier helps the worker see a missing layer. It does not command the worker, validate the file, or replace user judgment.

### Missing Field / Missing Context Rule

If a field or neighbor is missing, the result is not automatically invalid.

Instead, mark:

- MISSING_EVIDENCE
- missing neighbor
- blurry lens
- watch

Then decide whether to add exactly one neighbor or stop.

### Lens Failure Watch

- lens becoming schema
- tier map becoming routing authority
- worker filling fields mechanically
- structure replacing judgment
- adding neighbors by habit
- "lens" language becoming vague permission to ignore evidence

This addendum is candidate with watch. It should be revised after 1-2 real uses.

## Progressive Lens Loading Addendum — Candidate

Trial 012 contributed a useful external-reference lens: context engineering is not loading more context, but selecting enough high-signal context for the task.

evidence_type:
USER_PROVIDED_SUMMARY / GEMINI_TRIAL_EVIDENCE. A saved Trial 012 file was not found in the narrow check for this patch.

This is a loading discipline only. It does not create a skills system, memory system, AGENTS.md, MCP integration, or automation.

### Progressive Lens Loading Rule

Start with the smallest sufficient lens.

Default:

- begin with Tier 1 / Core Judgment Lens or the smallest task-relevant bundle
- do not load Tier 3/4/5 by habit
- do not load all tool profiles, routing cards, provenance records, and RUNLOG slices at once
- add one neighbor only when the task shows a missing layer

### Neighbor Request Conditions

```text
Need recoverable asset / provenance -> add Provenance neighbor
Need tool calibration -> add Tool Profile neighbor
Need user trigger / routing -> add Routing Card neighbor
Need event-level causality -> add bounded RUNLOG slice
Need memory hygiene -> add memory/provenance surface only if memory placement is being decided
```

### Missing Layer Handling

If the worker cannot answer confidently with the current lens, it should not silently broaden context.

It should state:

- missing layer
- why current lens is insufficient
- exactly one requested neighbor
- expected useful result from adding that neighbor

### Relation to Trial 012

Trial 012 showed that external materials on context engineering, skills, agent-facing instructions, MCP, and memory hygiene all support the same candidate principle:

```text
More context is not better context. Load the next lens only when it improves the task.
```

Do not treat those external materials as VectorFL authority.

### Progressive Loading Watch

- under-context from refusing needed neighbor
- over-context from loading all lenses
- progressive loading becoming hidden routing authority
- agent-facing docs becoming command registry
- skills/MCP/memory systems being adopted prematurely
- context engineering misunderstood as "more context"
- user judgment bypassed

This addendum is a loading discipline only.

It should be tested in real tasks before becoming a recurring operating habit.

## 8. Recommended Next Trial

Trial 009 — RUNLOG Neighbor / Causal Maturation Trial

Goal:

Test whether adding one bounded RUNLOG slice can recover event-level causality without exploding token cost.

Candidate question:

```text
Can a bounded RUNLOG neighbor explain why a policy mutation happened, without requiring broad raw trace reading?
```

Do not execute Trial 009 from this document.

## 9. Final Note

This document is a bundle tier map candidate only.

It should be revised after Trial 009.

It should not be treated as final routing policy.
