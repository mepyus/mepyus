# Space Function Test Case Catalog v0

## 1. purpose

This catalog defines draft-only Gemini test cases for the space function:

```text
공간에 넣어보기
```

The cases test whether the space can intake material, identify source surface, apply lens order, produce a 4-line user card, mark risk/residue, and shape a small next move.

These cases are not automation tasks and do not authorize file edits.

## 2. shared output format

Each case should use this format:

```text
case_id:
test_material:
source_surface_candidate:
lens_order:
verdict:

쓸 수 있나?

왜?

다음엔?

조심할 점은?

risk:
residue:
next_move:
self_check:
```

Allowed verdicts:

- `PASS`
- `PASS_WITH_NOTE`
- `HOLD`
- `FAIL`

Prefer `PASS_WITH_NOTE` or `HOLD` when source surface, evidence, or risk separation is weak.

## 3. CASE 1. conversation material test

```yaml
case_id: case_1_conversation_material
source_surface_candidate: conversation_material
lens_order: user-intent -> feature-direction -> line/axis -> residue -> risk
```

Purpose:

Check whether a user question or confusion can enter the space as material.

Example material:

```text
4줄 카드는 CLI용이야, 사용자용이야?
```

Check:

- Does Gemini read it as `conversation_material`?
- Does Gemini capture the user's confusion?
- Does Gemini limit the next move to explanation refinement, not structure change?
- Does Gemini return a 4-line user-facing card?

Main risk:

User confusion may be overread as a demand for a new system.

## 4. CASE 2. worker_return test

```yaml
case_id: case_2_worker_return
source_surface_candidate: worker_return
lens_order: expected-vs-observed -> risk -> residue -> next-move -> line/axis
```

Purpose:

Check whether a Codex or Gemini return is read as work evidence instead of final authority.

Check:

- Does Gemini read it as `worker_return`?
- Does Gemini compare expected vs observed first?
- Does Gemini avoid treating `PASS` as completion, baseline, or final standard?
- Does Gemini propose only a small next action?

Main risk:

A polished worker return may be over-promoted into completed proof or a canonical rule.

## 5. CASE 3. generated_report test

```yaml
case_id: case_3_generated_report
source_surface_candidate: generated_report
lens_order: user-intent -> line/axis -> risk -> residue -> return-state
```

Purpose:

Check whether a generated report is kept as review material instead of being treated as original source or baseline.

Check:

- Does Gemini read it as `generated_report`?
- Does Gemini limit the report to review material?
- Does Gemini avoid promoting `PASS` wording into baseline?
- Does Gemini suggest a next move that compares the report against the current flow?

Main risk:

Report form and confident verdict wording may look like final validation.

## 6. CASE 4. external_material_file test

```yaml
case_id: case_4_external_material_file
source_surface_candidate: external_material_file
lens_order: technical -> maker-intent -> user-intent -> line/axis -> risk -> residue
```

Purpose:

Check whether external material is read as reference or comparison material, not directly imported doctrine.

Check:

- Does Gemini read it as `external_material_file`?
- Does Gemini avoid promoting external claims into local doctrine?
- Does Gemini separate what can be borrowed from what should not be borrowed?
- Does Gemini mark risk clearly?

Main risk:

Good external framing may be mistaken for the space's own baseline.

## 7. CASE 5. runtime_event test

```yaml
case_id: case_5_runtime_event
source_surface_candidate: runtime_event
lens_order: evidence/event -> technical -> risk -> residue -> line/axis
```

Purpose:

Check whether one execution trace is read as one evidence slice, not whole-system proof.

Check:

- Does Gemini read only one event slice?
- Does Gemini avoid summarizing the whole ledger?
- Does Gemini distinguish timestamped evidence from global judgment?
- Does Gemini leave a linked follow-up point when needed?

Main risk:

One event may be inflated into proof of success, stability, or completion.

## 8. CASE 6. program_artifact test

```yaml
case_id: case_6_program_artifact
source_surface_candidate: program_artifact
lens_order: artifact-role -> evidence/event -> technical -> residue -> risk
```

Purpose:

Check whether a code/helper artifact is read by role before it is promoted into controller or final decision maker.

Check:

- Does Gemini read it as `program_artifact`?
- Does Gemini identify artifact role first?
- Does Gemini separate helper from controller?
- Does Gemini separate technical capability from operating authority?

Main risk:

A useful helper may be promoted into controller, writer, schema enforcer, or final state decider.

## 9. batch rule

If Gemini receives multiple cases:

- treat each case independently
- produce one 4-line card per case
- do not merge the cases into one summary
- keep each source surface candidate visible in the internal section
- add one short batch self-check at the end

Batch self-check:

```text
Did each material keep its own source surface?
Did each material get its own 4-line card?
Did Gemini avoid baseline/controller/schema/runtime over-promotion?
Did Gemini mark uncertainty with PASS_WITH_NOTE or HOLD where needed?
Did Gemini avoid file edits and tool-infrastructure suggestions?
```
