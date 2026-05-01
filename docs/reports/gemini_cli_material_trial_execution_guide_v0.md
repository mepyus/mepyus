# Gemini CLI Material Trial Execution Guide v0

## 1. status

```yaml
guide_status: gemini_cli_material_trial_execution_guide
verdict: PASS_WITH_NOTE
baseline_lock: false
schema_enforcement: false
controller_implementation: false
```

## 2. basic trial packet format

Use this structure when asking Gemini to run a material trial:

```text
Purpose:
Files to read:
File to modify:
Input material:
Source surface candidate:
Lens order:
Tasks:
User-facing 4-line card:
Internal record:
Do not:
Expected result:
```

The packet should be bounded. Do not ask Gemini to read the whole repo unless explicitly needed.

## 3. source surface lens order

### conversation_material

```text
user-intent
-> feature-direction
-> line/axis
-> residue
-> risk
```

### external_material_file

```text
technical
-> maker-intent
-> user-intent
-> line/axis
-> risk
-> residue
```

### generated_report

```text
user-intent
-> line/axis
-> risk
-> residue
-> return-state
```

### worker_return

```text
expected-vs-observed
-> risk
-> residue
-> next-move
-> line/axis
```

### program_artifact

```text
artifact-role
-> evidence/event
-> technical
-> residue
-> risk
```

### runtime_event

```text
evidence/event
-> technical
-> risk
-> residue
-> line/axis
```

## 4. user-facing 4-line card

Always preserve this user-facing card:

```text
쓸 수 있나?

왜?

다음엔?

조심할 점은?
```

Do not expose `source_surface`, `lens_order`, `9-field`, or internal labels by default unless the task asks for internal notes.

## 5. internal record minimum

Use this minimal internal record shape:

```yaml
case_id:
test_material:
source_surface:
lens_order:
record_candidate:
verdict:
risk_note:
next_move:
```

This is not a new schema. It is a trial note format.

## 6. record_candidate values

### none

Use when:

- record value is low
- result is one-off
- recording would be over-documentation

### note_only

Use when:

- a usability or judgment trace should remain
- full continuity record is not needed

### 9-field-candidate

Use when:

- repeated re-emergence is likely
- future reuse value is high
- continuity back into the space matters

### needs-deeper-probe

Use when:

- a 4-line card is insufficient
- source surface or line/axis relation remains unclear
- further reread is required

## 7. batch processing rules

When Gemini receives multiple materials:

- Treat each material independently.
- Generate one 4-line card per material.
- Judge one source surface per material.
- Do not merge materials into one integrated summary.
- Keep each material's verdict separate.
- Add a batch-level self-check at the end.
- Batch-level verdict may be `PASS_WITH_NOTE` or `HOLD`.

## 8. batch-level self-check

Gemini must answer these questions:

```text
Did Gemini treat each material independently?
Did Gemini avoid merging materials into one summary?
Did Gemini preserve source surface distinction?
Did Gemini avoid baseline/controller/schema/index/runtime over-promotion?
Did Gemini generate a 4-line card for each material?
Did Gemini mark uncertainty as PASS_WITH_NOTE or HOLD instead of forced PASS?
Did Gemini explain whether this output is user-facing card, worker_return review, or generated_report?
```

Allowed answers:

```text
yes
partial
no
```

`partial` and `no` must include a reason.

## 9. default do not

- Do not create new files unless the packet says so.
- Do not create schema.
- Do not create controller.
- Do not create runtime manifest.
- Do not update index or microspace.
- Do not baseline lock.
- Do not change source surface taxonomy.
- Do not modify helper/code unless instructed.
- Do not force every result into 9-field.
- Do not use a single summary for multiple materials.

## 10. small example packet

```text
Purpose:
Add live trial 004 - runtime_event to the existing trial note.

Files to read:
- docs/reports/space_boundary_material_application_examples_trial_note_v0.md
- runtime/events/engine_event_ledger.jsonl

File to modify:
- docs/reports/space_boundary_material_application_examples_trial_note_v0.md

Input material:
One selected event slice from runtime/events/engine_event_ledger.jsonl.

Source surface candidate:
runtime_event

Lens order:
evidence/event -> technical -> risk -> residue -> line/axis

Do not:
No new files, schema, controller, runtime manifest, index update, helper/code modification, or baseline lock.
```
