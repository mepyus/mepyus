# Judgment Provenance Record Template and Trial — 2026-05-09

## 0. Status

- candidate only
- live-use with watch
- not baseline
- not schema
- not registry
- not automation
- not truth engine
- not replacement for user judgment

## 1. Purpose

This document exists to help future workers distinguish where a judgment came from before that judgment enters a record, capsule, profile, policy mutation, watch item, or Return-to-Space note.

It is meant to prevent silent blending of:

- user-stated judgment
- ChatGPT / Supervisor inference
- Codex file observation
- Gemini synthesis
- external-source claims
- experiment results
- RUNLOG / process trace
- model-general reasoning

The practical goal is to separate observed evidence from inference, preserve source-of-judgment, and stop candidate/watch/raw trace confusion. It should make ChatGPT / Supervisor reasoning auditable without turning provenance into a schema or truth engine.

## 2. Minimal Provenance Labels

| Label | Meaning | Example | Common Misuse | Allowed Return Placement |
|---|---|---|---|---|
| `USER_CURRENT_INPUT` | Judgment or direction stated in the current user message. | User says the current anchor map is accepted as a first observation spine. | Treating the user's current judgment as file evidence. | `USER_JUDGED`, `WATCH`, `RETURN_TO_SPACE_VALUE_WITH_WATCH` |
| `USER_LONG_TERM_CONTEXT` | Durable user preference or repeated direction from prior conversation/project context. | User repeatedly wants candidate-with-watch and no baseline promotion. | Treating remembered context as a repo-observed fact. | `WATCH`, `ROUTING_HINT`, `CANDIDATE_CONTEXT` |
| `OBSERVED_FILE_EVIDENCE` | Directly read local file evidence. | A file states "candidate only" and "not baseline." | Extending the file's claim beyond the read scope. | `RETURN_TO_SPACE_VALUE_WITH_WATCH`, `WATCH`, `RAW_TRACE_ONLY` |
| `PROCESS_TRACE` | RUNLOG or process-log evidence that an action occurred. | `RUNLOG.jsonl` records Package Q patch action. | Treating process trace as semantic validation. | `RAW_TRACE_ONLY`, `WATCH`, `PROCESS_CONTEXT` |
| `CODEX_OBSERVATION` | Codex read-only observation or file existence check. | Codex reports a file was found or not found during a pass. | Treating Codex observation as final user judgment. | `WATCH`, `RETURN_TO_SPACE_VALUE_WITH_WATCH`, `MISSING_EVIDENCE` |
| `GEMINI_SYNTHESIS` | Gemini-produced synthesis, audit, test result, or package-level return. | Gemini reports a carrier trial passed with watch. | Treating synthesis as structural proof or baseline. | `RAW_TRACE_ONLY`, `WATCH`, `RETURN_TO_SPACE_VALUE_WITH_WATCH` after recovery |
| `CHATGPT_SUPERVISOR_INFERENCE` | Supervisor interpretation, routing judgment, or overclaim correction. | Supervisor infers that "정리해줘" is overloaded and needs routing clarification. | Hiding inference as observed file evidence. | `WATCH`, `ROUTING_HINT`, `CANDIDATE_CONTEXT` |
| `MODEL_GENERAL_REASONING` | General reasoning not grounded in current user input or observed files. | "This structure may reduce future rediscovery cost." | Presenting model judgment as project evidence. | `WATCH`, `HOLD_FOR_EVIDENCE`, `MODEL_SUGGESTED_CANDIDATE` |
| `EXTERNAL_SOURCE` | Claim or pattern from non-project source material. | External article suggests a tool or workflow pattern. | Importing external source as direct VectorFL rule. | `RAW_TRACE_ONLY`, `WATCH`, `EXTERNAL_REFERENCE_CANDIDATE` |
| `EXPERIMENT_RESULT` | Result from a bounded trial, test, carrier run, or package execution. | Hermes returned 10 Worker Return Intake fields in one test. | Generalizing one test into reliability or standard status. | `WATCH`, `RETURN_TO_SPACE_VALUE_WITH_WATCH` |
| `MISSING_EVIDENCE` | A required or expected source was not found or not inspected in the current pass. | Package S standalone note not found in the anchor pass. | Overstating absence as proof that no file exists anywhere. | `WATCH`, `HOLD_FOR_EVIDENCE` |

## 3. Minimal Record Fields

Use this compact shape when a judgment needs provenance. It is a candidate template, not a schema.

```text
judgment_id:
judgment:
source_type:
source_ref:
observer:
evidence_level:
inference_level:
layer:
status:
return_placement:
use_when:
do_not_use_when:
linked_parent:
linked_neighbors:
watch:
```

Field notes:

- `source_type` should name the provenance label, not just the tool name.
- `source_ref` should point to a file, RUNLOG entry, user input, or explicit missing source.
- `observer` should name who made the observation or interpretation.
- `evidence_level` should use the lightweight evidence levels below.
- `inference_level` should state whether the judgment is direct, interpreted, inferred, or missing-evidence-based.
- `return_placement` should keep candidate/watch/raw trace/hold distinctions visible.

## 4. Evidence Level Guidance

| Evidence Level | Use For | Do Not Use For |
|---|---|---|
| `EXTRACTED` | Directly quoted or directly observed file/process content. | Interpretation, synthesis, or future implications. |
| `INTERPRETED` | Meaning read from observed content with a stated source. | Unstated assumptions or proof claims. |
| `INFERRED` | Contextual conclusion from multiple signals. | Verified fact. |
| `AMBIGUOUS` | Conflicting, thin, missing, or unclear evidence. | Failure by default. |
| `USER_JUDGED` | User acceptance, correction, hold, promotion, or direction. | Rewriting source facts. |
| `PROCESS_TRACE` | Evidence that an operation happened or was logged. | Semantic validation or truth proof. |

## 5. Trial Record A — Current Anchor Map Creation

```text
judgment_id:
JPR-20260509-A

judgment:
The current_anchor_map_candidate_20260509_v0.md is useful as a first-read candidate map, but must not be treated as baseline, registry, schema, or final authority.

source_type:
OBSERVED_FILE_EVIDENCE + USER_CURRENT_INPUT + CODEX_OBSERVATION

source_ref:
- app/work/space-skill-sandbox/outputs/current_anchor_map_candidate_20260509_v0.md
- current user input accepting the result as a first observation spine
- Codex file creation and verification report in current exchange

observer:
Codex for file observation; User for acceptance judgment; ChatGPT/Supervisor may later route from it.

evidence_level:
EXTRACTED for file status lines; USER_JUDGED for user acceptance; INTERPRETED for usefulness as first-read map.

inference_level:
interpreted from observed file purpose and user judgment.

layer:
current anchor / first-read surface / live-use candidate map

status:
candidate / live-use with watch

return_placement:
RETURN_TO_SPACE_VALUE_WITH_WATCH

use_when:
Use before future workers start broad rediscovery, route selection, provenance trials, active bundle drafting, or tool profile drafting.

do_not_use_when:
Do not use as baseline, registry, schema, authority index, production workflow, final space map, or proof that all anchors are complete.

linked_parent:
Package R result-oriented stack closeout; Package Q routing card; Package O Result Contract; Package M Usefulness Gate.

linked_neighbors:
Evidence Provenance Classification Candidate; Memory Record Hygiene Rule; RUNLOG process trace.

watch:
Revise after 2-3 real uses. Watch for old baseline/current docs being over-read as current result-oriented authority.
```

## 6. Trial Record B — Package S Standalone Note Gap

```text
judgment_id:
JPR-20260509-B

judgment:
Package S standalone note was not found in this anchor pass; Package S is currently supported only by RUNLOG and Package Q patch context unless a real Package S output file is later found.

source_type:
CODEX_OBSERVATION + MISSING_EVIDENCE + PROCESS_TRACE

source_ref:
- app/work/space-skill-sandbox/outputs/current_anchor_map_candidate_20260509_v0.md
- RUNLOG.jsonl, Package Q overloaded-term patch entry referencing PACKAGE_S_RESULT_ORIENTED_OPERATING_STACK_REAL_USE_TRIAL_20260508
- search/anchor pass reported no Package S standalone note

observer:
Codex observation from current anchor-map pass.

evidence_level:
AMBIGUOUS for missing standalone source; PROCESS_TRACE for RUNLOG reference; INTERPRETED for current support status.

inference_level:
missing-evidence-based; bounded to this anchor pass.

layer:
gap / watch / process-trace-supported context

status:
watch

return_placement:
WATCH

use_when:
Use when Package S is cited as live-use candidate evidence or when explaining why Package Q contains overloaded-term resolution for "정리해줘".

do_not_use_when:
Do not claim Package S does not exist anywhere. Do not treat RUNLOG reference as a full semantic recovery note. Do not promote Package S result beyond live candidate with watch.

linked_parent:
Package Q routing card; Package R closeout; RUNLOG process trace.

linked_neighbors:
current_anchor_map known gaps; user-facing routing card section 6.1.

watch:
If a Package S standalone output is later found, update this judgment and attach the file path.
```

## 7. Trial Record C — ChatGPT Explaining Instead of Observing

```text
judgment_id:
JPR-20260509-C

judgment:
ChatGPT/Supervisor has a recurring risk of explaining the space conceptually instead of observing current space anchors before answering.

source_type:
USER_CURRENT_INPUT + USER_LONG_TERM_CONTEXT + CHATGPT_SUPERVISOR_INFERENCE

source_ref:
- current user instruction requiring future space-related reasoning to show whether a judgment came from current user input, project context, observed files, external source, model inference, experiment result, or process trace
- current_anchor_map_candidate_20260509_v0.md watch item: "ChatGPT explaining instead of observing"
- Package R role boundary for ChatGPT / Supervisor as ambiguous routing, principle alignment, user-language explanation, next package framing, and overclaim detection

observer:
User for risk direction; ChatGPT/Supervisor inference for recurring risk framing; Codex for file-supported watch reference.

evidence_level:
USER_JUDGED for current user concern; EXTRACTED for anchor-map watch item; INFERRED for recurrence risk.

inference_level:
partly file-supported watch; partly supervisor inference; not a quantified behavioral telemetry finding.

layer:
watch / response behavior / supervisor routing discipline

status:
watch

return_placement:
WATCH

use_when:
Use before answering broad space questions, making routing decisions, or explaining current state without reading current anchors.

do_not_use_when:
Do not treat as proof of every ChatGPT answer pattern. Do not use to prohibit explanation when explanation is requested. Do not treat as file evidence beyond the cited watch item and role boundary.

linked_parent:
Result-Oriented Operating Stack Closeout; Current Anchor Map Candidate.

linked_neighbors:
User-Facing Routing Card; Memory Record Hygiene Rule; future tool profile record.

watch:
Next-use correction: read current anchors first, label source type, separate observed file evidence from supervisor inference, and keep user-facing answer concise.
```

## 8. Usage Note for Future Workers

Use this document when converting a judgment into a record, capsule, tool profile, policy mutation, watch item, or Return-to-Space value.

Future workers should:

- cite or name the source type explicitly.
- separate current user input from observed file evidence.
- avoid treating inference as observed file evidence.
- avoid treating user philosophy as repo evidence.
- avoid treating Gemini synthesis as structural proof.
- avoid treating Codex file observation as final user judgment.
- mark missing evidence as missing-evidence-based, not as proof of absence.
- keep return placement visible: Return-to-Space, Watch, Routing Hint, Raw Trace, Hold, or Discard.

## 9. Known Limits

- This is only a first provenance trial.
- It is not a full provenance system.
- It has not been tested across many records.
- Field names may change after 2-3 real uses.
- It may create ceremony bloat if used on every small answer.
- It may create false precision if labels are applied mechanically.
- It does not replace the Result Usefulness Gate or user judgment.

## 10. Watch Items

- provenance template becoming schema.
- provenance labels becoming truth engine.
- too many fields increasing friction.
- source labels used mechanically.
- model inference hidden inside `INTERPRETED`.
- user judgment flattened into model status.
- Codex over-structuring.
- Gemini over-abstracting.
- ChatGPT explaining instead of observing.
- process trace treated as semantic proof.
- missing evidence overstated as global absence.

## 11. Final Note

This document is a provenance trial only.

It should be revised after 2-3 real uses.

It should not be treated as final schema or registry.

