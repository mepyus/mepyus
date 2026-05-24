# Sandbox Trial Criteria 2026-05-12 Candidate v0

## 1. Status

```text
Document = sandbox trial criteria
Status = CANDIDATE_CRITERIA
Authority = pre-trial structure only
Not baseline
Not official workflow
Not automation
Not schema
Not current-position update
```

## 2. Purpose

Define when a candidate should go to sandbox instead of staying in thought, WATCH, HOLD, or worker dispatch.

This does not launch a sandbox trial.

## 3. Sandbox Trial Is Allowed When

All must be true:

```text
1. The trial target is bounded.
2. The original space will not be modified.
3. The expected output is small.
4. The failure condition is visible.
5. The return path is known.
6. The trial can reduce a real cost.
7. The result can be placed as candidate / watch / hold without promotion.
```

## 4. Sandbox Trial Is Not Allowed When

Any one is true:

```text
the goal is to make the structure feel more complete
the failure condition is missing
the result cannot return to space
the output would be confused with product/original
the trial needs user-sensitive real-world commitment
the task requires baseline/current-position decision
the trial is actually worker execution with unclear packet boundaries
```

## 5. WATCH Instead Of Sandbox

Use WATCH when:

```text
the idea is useful
the risk is visible
evidence is thin
the next strengthening evidence is known
```

WATCH must name:

```text
what to watch
what would strengthen it
what would weaken it
```

## 6. HOLD Instead Of Sandbox

Use HOLD when:

```text
source is missing
trigger is unclear
failure condition is absent
return path is absent
user judgment is needed before action
```

HOLD must name:

```text
what is missing
who/what can supply it
```

## 7. Worker Packet Instead Of Sandbox

Use WORKER_PACKET when:

```text
there is a bounded task for Codex/Gemini/worker
read/do-not-read scope is clear
forbidden actions are clear
success criteria are clear
return format is clear
no hidden whole-space inference is needed
```

Worker packet must include:

```text
purpose
required reading
do-not-read / do-not-do
output shape
failure / uncertainty return
hard stops
```

## 8. User Judgment Instead Of Sandbox

Stop for user when:

```text
choosing the practical input has real-world consequence
promotion to baseline/workflow is implied
current-position update is implied
script/helper implementation is implied
source-space modification is implied
```

## 9. Apply To Current 05-12 Candidate

Candidate:

```text
Common Growth Frame
```

Current decision:

```text
Do not sandbox the whole frame.
Sandbox only a small use case after a target is selected.
```

Possible sandbox targets:

```text
one external reference intake
one worker return recovery
one repo-seed derivation
one small practical artifact
```

Current placement:

```text
WATCH_FOR_SANDBOX_TARGET
```

Reason:

```text
The criteria exist, but the actual sandbox target should be selected deliberately.
If the target has user-real-world consequence, ask the user.
If the target is just another internal document, Codex can choose a low-risk one-input test.
```

## 10. Recommended Low-Risk Next Test

```text
Use one already-created internal output as a sandbox target.
Do not use a real workplace or personal high-stakes input yet.
```

Candidate low-risk target:

```text
app/work/space-skill-sandbox/outputs/chatgpt_asset_utilization_discussion_brief_20260512_v0.md
```

Why:

```text
It is internal.
It already has a clear purpose.
It can test whether the Common Growth Frame helps turn an asset inventory into a better ChatGPT discussion packet.
Failure is low-cost and returnable.
```

## 11. Watch

```text
sandbox target too large
sandbox used to avoid choosing
internal artifact testing replaces real-use forever
criteria becomes workflow
```

`STATUS: SANDBOX_TRIAL_CRITERIA_PREPARED`
