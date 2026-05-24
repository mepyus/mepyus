# Movement Record - Gemini Active Surface Selection-Cost Test 2026-05-12 v0

## 1. Status

```text
Document = movement record
Status = PROCESS_MEMORY_WITH_WATCH
Authority = worker-return movement trace only
Not baseline
Not official workflow
Not automation
Not current-position update
```

## 2. Movement

```text
Codex built package manifest
-> Codex built Gemini packet
-> Gemini CLI executed the packet
-> Gemini read the package in the requested order
-> Gemini tested two Codex classifications
-> Gemini chose one additional input
-> Gemini returned PASS_SELECTION_COST_REDUCED_WITH_WATCH
-> Codex recovered return as worker evidence with watch
```

## 3. What Was Learned

```text
Package listing helped Gemini avoid shallow scanning.
Gemini completed the test using the bounded required package.
Gemini did not need broad repo scanning according to its report.
Gemini agreed with Codex on:
  SANDBOX_TRIAL_WITH_WATCH for continuation trigger
  WATCH / SCRIPTABLE_SETUP_FRICTION for audit-run churn
Gemini added:
  RETURN_ONLY for ChatGPT custom gate-name normalization
```

## 4. Execution Watch

```text
Gemini stderr contained temporary model-capacity retry messages.
The command completed with exit code 0.
Keep this as reliability watch, not judgment watch.
```

## 5. What Was Not Learned

```text
This does not prove the structure works for all inputs.
This does not approve automation.
This does not make the package manifest a registry.
This does not make the active surface baseline.
This does not reduce execution setup cost.
```

## 6. Next Pull

```text
Use a new substantive input and run the same bounded package approach.
If repeated tests show stable friction in setup or return recovery,
then record a script candidate rather than implementing immediately.
```

`STATUS: MOVEMENT_RECORD_GEMINI_ACTIVE_SURFACE_SELECTION_COST_TEST_PREPARED`
