# Run 324: Gemini Runner Observability Patch

## Status

```text
Run = 324
Status = runner observability patch
Authority = setup support only
Not baseline
Not official workflow
Not automation of judgment
Not current-position update
```

## Trigger

```text
User asked to close out the current work and inspect Gemini invocation wiring,
because model choice, speed, and result state were hard to see.
```

## Inputs

```text
scripts/sandbox/run_gemini_packet.sh
gemini --help
gemini --version
recent Gemini outbox/raw/stderr files
```

## Output / Files Changed

```text
scripts/sandbox/run_gemini_packet.sh
app/work/space-skill-sandbox/outputs/today_work_closeout_gemini_observability_20260512_candidate_v0.md
app/work/space-skill-sandbox/outputs/gemini_runner_observability_check_20260512_candidate_v0.md
```

## Result

```text
Runner now supports --model.
Runner records requested_model, duration_seconds, prompt_bytes, raw_bytes, stderr_bytes, command_summary, and stderr tail.
Smoke test confirmed metadata appears in outbox.
Smoke test also exposed hidden 429 / model-capacity retry traces despite exit code 0.
```

## Boundary

```text
No Gemini judgment automation.
No workflow creation.
No baseline promotion.
No current-position update.
```

`STATUS: RUN_324_GEMINI_RUNNER_OBSERVABILITY_PATCH_PREPARED`
