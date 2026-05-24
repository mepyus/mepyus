# Cost Metric and Worker Landing Watch Patch 2026-05-12 Candidate v0

## 1. Status

```text
Document = watch patch
Status = CANDIDATE_WATCH_PATCH
Authority = boundary clarification only
Not baseline
Not official workflow
Not automation
Not schema
Not current-position update
```

## 2. Why This Exists

Gemini's structure-before-ChatGPT review returned:

```text
PASS_SEND_TO_CHATGPT_WITH_WATCH
```

Two useful gaps were identified:

```text
Cost Reduction Metric is underdefined.
Worker return landing zone could be more explicit.
```

This patch records those gaps before sending the ChatGPT packet.

## 3. Cost Reduction Metric Candidate

When a flow or packet claims to reduce cost, specify which cost:

```text
Explanation cost:
  fewer user turns needed to restate direction

Selection cost:
  easier to choose WATCH / HOLD / sandbox / worker packet

Recovery cost:
  easier to recover a return without rereading everything

Boundary cost:
  fewer chances of baseline/workflow/automation confusion

Execution setup cost:
  less manual setup for a bounded worker packet
```

Minimum rule:

```text
Do not say "reduces cost" alone.
Name the cost type.
```

## 4. Worker Return Landing Zone Candidate

Raw worker/Gemini returns should land as trace before memory:

```text
runtime/gemini_sandbox/ or outputs/gemini_raw_results/
relay/outbox/
```

Then Codex packages them into:

```text
return packaging
movement record
minimum trace packet
candidate output if useful
```

Rule:

```text
Worker return lands as trace first.
It does not land directly as memory, approval, current-position, or baseline.
```

## 5. Patch To Future ChatGPT Recovery

When recovering the future ChatGPT return, check:

```text
Did ChatGPT name which cost would be reduced?
Did ChatGPT distinguish raw return from recovered memory?
Did ChatGPT propose a landing zone for any worker packet result?
```

## 6. Watch

```text
cost metric becomes KPI
landing zone becomes registry
worker trace becomes approval
```

`STATUS: COST_METRIC_AND_WORKER_LANDING_WATCH_PATCH_PREPARED`
