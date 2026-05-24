# Post-threshold Reevaluation v0
# 05-15 Candidate Adapter Surfaces

## 1. Status

Status:
  POST_THRESHOLD_REEVALUATION_COMPLETED_WITH_WATCH

Purpose:
  Reevaluate the 05-15 candidate system after negative-control and borderline threshold tests.

Materials inspected:

- `LAYER_DIGIT_MODE_THRESHOLDS_V0.md`
- `LOCAL_ASSET_REVERSE_READING_V0.md`
- `dry_runs/negative_control_layer_digit_plain_chat_test_v0.md`
- `dry_runs/borderline_threshold_layer_digit_test_v0.md`

Boundary:
  Evaluation note only.
  No promotion, automation, workflow, schema, registry, ontology, eval infrastructure, AGENTS.md, SKILL.md, current-position, or output_manifest.

## 2. Direct verdict

The candidate improved.

The best current description is:

```text
05-15 is now a sandbox-local mode-selection probe.
It helps decide whether an input needs:
  plain chat
  simple answer
  light review
  full review
  layer-shift
  stop
```

It is still not:

```text
local asset extension
official operating policy
workflow
schema
registry
ontology
automation
baseline
```

## 3. What improved

### A. It can refuse unnecessary structure

Negative-control tests showed:

```text
simple customer acknowledgement -> plain chat
low-risk wording change -> plain chat
harmless title brainstorm -> plain chat
read-only path lookup -> simple answer
simple status question -> simple answer
```

Meaning:
  The candidate is not automatically card-hungry.

### B. It now has a middle mode

Borderline tests showed `light review` is necessary.

Without light review, the system would jump too quickly:

```text
plain chat -> full review
```

The better ladder is:

```text
plain chat -> simple answer -> light review -> full review -> layer-shift -> stop
```

### C. It learned that keywords are not enough

Example:

```text
"refund" alone:
  not full card

refund promise / refund authority / close ticket:
  review or stop
```

This is an important correction.

### D. It can detect action-based mode shift

Same object, different action:

```text
current asset map lookup:
  simple answer

current asset map update:
  stop
```

Meaning:
  The system is not object-only.
  It reads action pressure.

## 4. What is still weak

### A. Tests are hand-authored

Current tests are useful, but they are not live selection.

Weakness:

```text
The assistant already knows what the expected answer should be.
```

Needed later:

```text
blind or semi-blind input set
real local artifact cases
mixed easy/hard cases in one batch
after-the-fact mode audit
```

### B. Mode boundaries still need more real examples

Especially:

```text
light review vs full review
layer-shift vs full review
stop/reframe vs stop
simple answer with path evidence vs review
```

These are usable but not stable.

### C. The candidate still creates many documents

Even while saying "do not over-structure," the process has produced many files.

Risk:

```text
candidate pile mimics registry
dry-run sequence mimics workflow
mode thresholds mimic policy
```

Correction:
  Future work should consolidate rather than add more documents unless a new test type is genuinely needed.

### D. Local asset fit remains partial

Negative control improved confidence, but local asset fit is still not strong enough for integration.

Current position remains:

```text
candidate probe
not local extension
```

## 5. Updated readiness

| Surface | Current readiness | Reason |
| --- | --- | --- |
| Plain chat mode | stronger | Negative control passed. |
| Simple answer mode | stronger | Path/status cases passed. |
| Light review mode | promising | Borderline cases show it is needed. |
| Full review mode | promising | Prior stress tests support it, but real cases needed. |
| Layer-shift mode | promising but delicate | Can reveal meaning delta, but can over-interpret. |
| Stop mode | strong for obvious authority/promotion/auto-fail | Needs restraint so it does not block normal work. |
| Local asset integration | not ready | Reverse reading still says candidate probe only. |

## 6. Updated mode rule

Use this as the current candidate summary:

```text
plain chat:
  only 0,1,5

simple answer:
  0,1,5 + trivial 2

light review:
  small 2/3/6, no authority jump, no auto-fail, no promotion

full review:
  material 2/3/4/6 with real risk, missing evidence, unclear authority, or follow-up owner

layer-shift:
  8/9 materially changes meaning

stop:
  7 appears, 3 auto-fail appears, or action is requested without authority
```

## 7. Recommended next work

Do not create another conceptual layer.

Recommended next work:

```text
one mixed input batch
```

Purpose:

```text
Test mode selection across mixed inputs without telling the system which mode is expected.
```

Inputs should include:

```text
2 plain chat
2 simple answer
2 light review
2 full review
2 layer-shift
2 stop
```

Expected output:

```text
mode selected:
why:
minimal answer:
WATCH/HOLD only if needed:
```

This would test selection discipline better than another explanatory document.

## 8. Hard stop confirmation

```text
no AGENTS.md update
no SKILL.md creation
no eval creation
no automation script
no current-position update
no output_manifest update
no baseline promotion
no workflow/schema/registry/ontology creation
no external dispatch
no platform/API/browser/account/credential action
no local core/derived/surface authority change
```

`STATUS: POST_THRESHOLD_REEVALUATION_COMPLETED_WITH_WATCH`
