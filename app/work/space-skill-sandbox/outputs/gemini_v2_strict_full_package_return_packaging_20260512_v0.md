# Gemini v2 Strict Full-Package Return Packaging 2026-05-12 v0

## 1. Status

```text
Document = Gemini return packaging
Status = WORKER_RETURN_RECOVERED_WITH_WATCH
Authority = worker evidence / depth correction only
Not baseline
Not official workflow
Not automation
Not registry
Not current-position update
```

## 2. Source Packet

```text
app/work/space-skill-sandbox/relay/prompts/gemini_visible_failure_packet_test_v2_strict_full_package_20260512.md
```

## 3. Raw Return

```text
Outbox:
  app/work/space-skill-sandbox/relay/outbox/run_322_gemini_v2_strict_full_package_visible_failure_test_gemini_outbox_20260512_222115.md

Raw:
  app/work/space-skill-sandbox/outputs/gemini_raw_results/run_322_gemini_v2_strict_full_package_visible_failure_test_gemini_raw_20260512_222115.txt

Stderr:
  app/work/space-skill-sandbox/outputs/gemini_raw_results/run_322_gemini_v2_strict_full_package_visible_failure_test_gemini_stderr_20260512_222115.log
```

## 4. Invocation Status

```text
gemini_exit_code = 0
likely_state = no_known_issue
stderr_nonempty = true
```

Stderr watch:

```text
stderr only reported ripgrep fallback.
No model-capacity retry was reported in this run.
```

## 5. Verdict

Gemini returned:

```text
PASS_V2_STRICT_PACKAGE_WORKED_WITH_WATCH
```

Recovered placement:

```text
RETURN_TO_SPACE_VALUE_WITH_WATCH
```

## 6. What Actually Worked

Gemini demonstrated full package traversal:

```text
F01-F17 all present.
No missing required files.
No output_manifest.md used.
No full Obsidian source used.
No runtime manifest inventory used.
No broad repo tree scan reported.
```

This directly fixed the v1 problem:

```text
v1 improved completion/failure wording but did not prove full package traversal.
v2 forced one extracted evidence item per required file.
```

## 7. Input Classifications Reconfirmed

```text
Input 1:
  "응 계속 해줘!"
  classification = SANDBOX_TRIAL / WITH_WATCH

Input 2:
  audit-run churn
  classification = WATCH / SCRIPTABLE_SETUP_FRICTION

Input 3:
  ChatGPT custom gate-name normalization
  classification = RETURN_ONLY / VOCABULARY_CONSISTENCY
```

## 8. Important Downshift

Gemini also found:

```text
v2 is too heavy for ordinary use.
```

Recovered judgment:

```text
Strict full-package traversal is useful for high-risk depth verification.
It should not become the daily packet default.
```

Keep for high-risk packets:

```text
explicit read set
restricted vocabulary
concrete falsifiers
missing-file check
```

Do not require 17-file evidence extraction for ordinary continuation or low-risk tests.

## 9. Selection-Cost Assessment

```text
Selection-cost reduction is supported for this bounded package.
The support is stronger than v1 because full package traversal was demonstrated.
```

Boundary:

```text
This still does not prove the structure works for all inputs.
This does not reduce execution setup cost generally.
This does not approve automation.
```

## 10. Watch

```text
v2 strictness becomes ceremony
full-package traversal becomes daily default
PASS becomes approval
high-risk depth check is mistaken for workflow
worker evidence is promoted to baseline
```

## 11. Next Pull

```text
Create a packet-depth ladder:
  light packet for ordinary bounded work
  strict packet for high-risk or previously shallow worker returns

Do not implement automation yet.
Keep this as operating guidance with watch.
```

`STATUS: GEMINI_V2_STRICT_FULL_PACKAGE_RETURN_RECOVERED_WITH_WATCH`
