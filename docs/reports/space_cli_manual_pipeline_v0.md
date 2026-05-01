# Space-CLI Manual Pipeline v0

## 1. pipeline purpose

This pipeline is not CLI automation.

It is not a bridge, dispatcher, JSON execution system, runtime structure, schema, or script plan.

The purpose is to make the space-CLI lightweight attachment / comparison / reflux structure repeatable by hand.

The manual pipeline lets the space do these jobs around CLI workers:

- read input material
- judge source surface
- retrieve only necessary memory
- compose a minimum task packet for a worker
- recover worker output
- read native vs space-referenced difference
- classify reflux memory candidates
- return a user-facing 4-line card

The space remains the body.

Codex and Gemini are workers.

## 2. pipeline stages

```text
1. Trigger / Input
2. Intake Routing
3. Lightweight Memory Retrieval
4. Minimum Task Packet
5. Worker Assignment
6. Worker Execution or Draft
7. Return Intake
8. Native vs Space-Referenced Diff
9. Reflux Memory Classification
10. User-Facing Return
11. Next Loop Candidate
```

## 3. stage questions

## 1. Trigger / Input

- What did the user put into the space?
- Is it material, a request, a worker result, an external source, or a pressure signal?
- Does the user ask for judgment, execution, explanation, or continuation?

## 2. Intake Routing

- What is the source surface?
- Is it `conversation_material`, `external_material_file`, `generated_report`, `worker_return`, `runtime_event`, or `program_artifact`?
- If uncertain, should it remain `candidate` or `uncertain`?
- Is there an embedded secondary surface inside the material?

## 3. Lightweight Memory Retrieval

- What memory cards are needed now?
- Can this be handled with three to five cards?
- Which source pointers are needed only if the cards are insufficient?
- What should not be read in full?

## 4. Minimum Task Packet

- What is the request summary?
- What is the source surface?
- What is the user goal?
- What guardrails must be included?
- What role should the worker take?
- What output is expected?
- What stop conditions must be explicit?

## 5. Worker Assignment

- Is this space internal only?
- Is this Codex structure / documentation / patch work?
- Is this Gemini execution / verification / first-draft work?
- Is user decision required before proceeding?
- Which route is not recommended?

## 6. Worker Execution or Draft

- Is the worker doing draft-only, verification, implementation, review, or formatting?
- Is the worker modifying files?
- Does the worker need to stop because the task asks for authority it should not have?

## 7. Return Intake

- Should the result be reread as `worker_return`?
- What was expected?
- What was observed?
- Are PASS, PASS_WITH_NOTE, or created-file lists being over-promoted?
- Are there missing files, overreach phrases, or wrong Next pointers?

## 8. Native vs Space-Referenced Diff

- What would a native CLI likely do?
- What changed when space context was attached?
- What is missing, overreaching, aligned, contradictory, or residual?

## 9. Reflux Memory Classification

- Is this `note_only`?
- Is this `reuse_hint`?
- Is this `risk_memory`?
- Is this `pattern_candidate`?
- Is this `hold_signal`?
- Is this `next_move_candidate`?
- Is this `deeper_probe_needed`?

## 10. User-Facing Return

Return the default user-facing card:

```text
쓸 수 있나?
왜?
다음엔?
조심할 점은?
```

Do not expose internal labels by default unless needed for user judgment.

## 11. Next Loop Candidate

- What is the next candidate?
- Is it only a candidate?
- Does it require user decision?
- Is `auto_execute` explicitly `no`?

## 4. guardrails

- Do not turn this pipeline into an automatic executor.
- Do not auto-execute `next_move_candidate`.
- Do not make Gemini the final judge.
- Reread Codex results as `worker_return`.
- Reread Gemini results as `worker_return`.
- Do not promote external material into baseline.
- Do not harden the minimum packet into a schema.
- Do not promote reflux memory directly into baseline.
- Do not let scripts decide source surface, worker assignment, reflux state, or next action.

## 5. current verdict

```yaml
verdict: PASS_WITH_NOTE
manual_pipeline: true
automation_pipeline: false
script_created: false
runtime_structure_created: false
schema_created: false
baseline_lock: false
next_allowed_move: apply_manual_pipeline_to_one_real_material
```
