# Movement Record - Gemini v2 Strict Full-Package Test 2026-05-12 v0

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
Gemini v1 returned PASS but did not demonstrate full package traversal
-> user flagged insufficient operation
-> Codex downshifted v1 to WATCH_INSUFFICIENT_DEPTH
-> Codex created v2 strict full-package packet
-> Gemini read F01-F17 and extracted evidence for every file
-> Gemini returned PASS_V2_STRICT_PACKAGE_WORKED_WITH_WATCH
-> Codex recovered result with daily-use downshift
```

## 3. What Was Learned

```text
The user's objection was correct.
v1 was structurally improved but operationally too shallow.
v2 fixed the shallow-read problem.
v2 is effective for depth verification but too heavy for ordinary use.
```

## 4. What Was Recovered

```text
Strict package traversal can verify worker depth.
Audit-run churn remains WATCH / SCRIPTABLE_SETUP_FRICTION.
Gate-name normalization remains RETURN_ONLY.
Continuation trigger remains SANDBOX_TRIAL / WITH_WATCH.
```

## 5. Watch

```text
Do not let strict packet become default ceremony.
Do not treat v2 PASS as approval.
Do not promote packet-depth ladder to workflow without more evidence.
```

## 6. Next Pull

```text
Draft a lightweight packet-depth ladder:
  light
  normal
  strict
with clear conditions for when strict mode is justified.
```

`STATUS: MOVEMENT_RECORD_GEMINI_V2_STRICT_FULL_PACKAGE_PREPARED`
