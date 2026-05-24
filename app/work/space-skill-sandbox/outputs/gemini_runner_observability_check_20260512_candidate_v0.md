# Gemini Runner Observability Check 2026-05-12 Candidate v0

## 1. Status

```text
Document = runner observability check
Status = CANDIDATE_SETUP_SUPPORT
Authority = CLI transparency support only
Not baseline
Not official workflow
Not automation of judgment
Not current-position update
```

## 2. What The Runner Can Now Show

Outbox now exposes:

```text
requested_model
gemini_version
duration_seconds
prompt_bytes
raw_bytes
stderr_bytes
likely_state
command_summary
stderr tail
```

This makes it easier to answer:

```text
Which model did we request?
How long did it take?
Did stderr contain hidden retry/capacity issues?
Was the response tiny or substantial?
Which raw/outbox/stderr files should be inspected?
```

## 3. Model Selection

Runner now accepts:

```text
--model MODEL
```

Example:

```text
bash scripts/sandbox/run_gemini_packet.sh --model gemini-2.5-flash --output-format text --timeout-seconds 120 PACKET RUN_ID
```

If no model is passed:

```text
requested_model = default
```

Meaning:

```text
Gemini CLI chooses its configured default.
The runner records that no explicit model was requested.
```

## 4. Smoke Test Evidence

```text
Outbox:
  app/work/space-skill-sandbox/relay/outbox/smoke_model_observability_20260512_gemini_outbox_20260512_222811.md

requested_model:
  gemini-2.5-flash

duration_seconds:
  21

result:
  GEMINI_SMOKE_OK

likely_state:
  model_capacity_or_quota
```

Interpretation:

```text
The call succeeded, but stderr showed model-capacity retry traces.
So success does not mean the call was clean or fast.
```

## 5. Reading Result Quality

Do not judge only by:

```text
gemini_exit_code = 0
```

Also check:

```text
requested_model
duration_seconds
raw_bytes
stderr_bytes
likely_state
stderr tail
whether the result satisfied the packet completion condition
whether required files were actually evidenced
```

## 6. Watch

```text
model flag becomes quality guarantee
duration is mistaken for quality
stderr warnings are ignored because exit code is 0
likely_state overrules human review
runner metadata becomes approval
```

`STATUS: GEMINI_RUNNER_OBSERVABILITY_CHECK_PREPARED`
