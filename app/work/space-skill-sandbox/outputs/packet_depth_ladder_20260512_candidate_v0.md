# Packet Depth Ladder 2026-05-12 Candidate v0

## 1. Status

```text
Document = packet depth ladder
Status = CANDIDATE_OPERATING_GUIDE
Authority = packet preparation support only
Not baseline
Not official workflow
Not automation
Not schema
Not registry
Not current-position update
```

## 2. Why This Exists

The Gemini v2 strict full-package run proved two things at once:

```text
strict traversal can fix shallow worker returns
strict traversal is too heavy for ordinary use
```

So packet depth needs levels.

The goal is not to create a router.

The goal is to choose packet depth deliberately before asking a worker to read.

## 3. Levels

### Level 1. Light Packet

Use when:

```text
task is narrow
stakes are low
no source-space modification
no promotion decision
no previous shallow worker failure
```

Requires:

```text
role
read set
do-not-do list
return shape
one failure condition
```

Do not require:

```text
per-file evidence table
full package traversal
strict missing-file audit
```

Expected use:

```text
simple classification
small external reference intake
single-note orientation
quick WATCH / HOLD check
```

### Level 2. Normal Packet

Use when:

```text
worker must compare multiple local files
result will be recovered into process memory
selection-cost or boundary claim is being tested
```

Requires:

```text
role
source refs
ordered read set
do-not-read set
local vocabulary
completion condition
visible proof
failure condition
return format
placement options
```

Expected use:

```text
Gemini structure review
multi-file package check
return recovery review
bounded packet-quality test
```

### Level 3. Strict Packet

Use when:

```text
previous worker return was shallow
worker claimed PASS without enough evidence
high-risk boundary is being tested
source list completeness matters
auditability is more important than speed
```

Requires:

```text
explicit file list with IDs
one extracted evidence item per file
missing-file check
do-not-read violation check
local vocabulary enforcement
concrete falsifier
evaluator limits
daily-use downshift check
```

Expected use:

```text
rerun after shallow Gemini return
high-risk packet verification
worker-depth validation
evidence completeness check
```

## 4. Choosing Depth

```text
If the task can be answered from one active surface:
  Level 1

If the worker must compare a bounded package:
  Level 2

If a previous result looked fluent but under-evidenced:
  Level 3

If user judgment, baseline, current-position, or source-space modification is involved:
  stop and request explicit user decision
```

## 5. What To Preserve Across All Levels

```text
receipt is not approval
worker return is evidence first
PASS is not promotion
source refs are not authority
output_manifest is navigation only
visible proof must be present
failure condition must be concrete
```

## 6. Gemini Model Note

Current observed smoke results:

```text
gemini-2.5-flash:
  duration_seconds = 21
  likely_state = model_capacity_or_quota
  stderr showed MODEL_CAPACITY_EXHAUSTED retry traces

gemini-3-flash-preview:
  duration_seconds = 10
  likely_state = no_known_issue
  stderr only reported ripgrep fallback
```

Candidate recommendation:

```text
Use gemini-3-flash-preview as the preferred explicit model for the next Gemini packet tests.
```

Watch:

```text
Model choice is not quality proof.
Still inspect completion condition, required evidence, stderr, and result depth.
```

## 7. Watch

```text
ladder becomes workflow
strict becomes ceremony
light becomes excuse for shallow evidence
model preference becomes quality guarantee
runner metadata becomes approval
```

## 8. Next Pull

```text
Use Level 2 for the next ordinary Gemini packet.
Use Level 3 only if the result is shallow or high-risk.
```

`STATUS: PACKET_DEPTH_LADDER_PREPARED_WITH_WATCH`
