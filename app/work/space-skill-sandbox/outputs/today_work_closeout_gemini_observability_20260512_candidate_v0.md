# Today Work Closeout - Gemini Observability 2026-05-12 Candidate v0

## 1. Status

```text
Document = closeout / setup check
Status = CANDIDATE_CLOSEOUT_WITH_WATCH
Authority = process memory and setup support only
Not baseline
Not official workflow
Not automation
Not current-position update
```

## 2. What Was Built Before Closeout

```text
Obsidian 05-12 was recovered as a common growth frame.
ChatGPT return was recovered with watch.
Active surface reduced selection cost in Codex tests.
Gemini first pass confirmed selection-cost reduction with watch.
Gemini v1 visible-failure packet was downshifted for insufficient depth.
Gemini v2 strict full-package packet fixed the depth issue but was too heavy for ordinary use.
External references formed a Closed Packet / Visible Failure Lens.
```

## 3. Current Operating Judgment

```text
Use packet depth deliberately:
  light for ordinary bounded work
  normal for worker packets
  strict after shallow worker returns or high-risk verification
```

This is a candidate operating judgment only.

## 4. Gemini Runner Problem Found

The user flagged that Gemini calls were hard to understand:

```text
model selection unclear
speed unclear
stderr / quota signals hidden
which result path to inspect unclear
```

Code inspection confirmed:

```text
scripts/sandbox/run_gemini_packet.sh did not expose --model.
Outbox did not record requested model.
Outbox did not record duration, prompt bytes, raw bytes, stderr bytes, or command summary.
Stderr tail was only appended on non-zero exit, hiding important retry/capacity signals on successful runs.
```

## 5. Runner Patch Applied

File changed:

```text
scripts/sandbox/run_gemini_packet.sh
```

Added:

```text
--model MODEL
output-format stream-json support
requested_model in outbox header
duration_seconds
prompt_bytes
raw_bytes
stderr_bytes
command_summary
stderr tail even on successful exit
timeout record includes requested model and prompt bytes
```

## 6. Smoke Test

Command:

```text
bash scripts/sandbox/run_gemini_packet.sh --smoke-text --model gemini-2.5-flash --output-format text --timeout-seconds 60 smoke_model_observability_20260512
```

Result:

```text
gemini_exit_code = 0
requested_model = gemini-2.5-flash
duration_seconds = 21
prompt_bytes = 35
raw_bytes = 16
stderr_bytes = 4937
response = GEMINI_SMOKE_OK
likely_state = model_capacity_or_quota
```

Important:

```text
The command succeeded, but stderr showed 429 / MODEL_CAPACITY_EXHAUSTED retry traces.
This explains why a successful Gemini call can still feel slow or unstable.
```

## 7. Watch

```text
runner observability becomes automation confidence
model selection becomes assumed quality guarantee
successful exit hides retry/capacity issues
strict packet depth becomes daily default
Gemini output becomes approval
```

## 8. Next Pull

```text
Create a small Gemini runner observability note:
  how to choose model
  how to read duration / likely_state / stderr tail
  when to use strict packet depth
  when to downshift a successful result
```

`STATUS: TODAY_WORK_CLOSEOUT_GEMINI_OBSERVABILITY_PREPARED`
