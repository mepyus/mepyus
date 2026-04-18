# Integrated Engine Reusable Reading-Frame Probe Result Template v0

## Verdict
PASS_WITH_NOTE

This document is a repeatable result template for future reusable reading-frame probes.
It does not promote the frame to a camera, axis, glossary, or canonical record.

## Use Boundary

- Use only when checking whether a held reading-frame transfers to a new target.
- Do not use this template to create a new camera.
- Do not use this template to promote an axis.
- Do not use this template as a glossary or canonical ingestion form.
- Probe output must end with one of:
  - reusable
  - partially reusable
  - asset-specific

## Probe Result Template

### 1. Probe Target

- target asset:
- target asset role:
- why this target was selected:
- asset count used:
- broad scan avoided? yes / no

### 2. Probe Type

- probe type:
  - sibling
  - cross-shape
- probe intent:
  - frame transferability check
  - rollback check
  - support placement check
  - scope anchor split check
- not in scope:
  - new line extraction
  - axis promotion
  - glossary
  - canonical ingestion
  - new camera

### 3. Applied Hold Frame

- hold frame id:
- current status:
  - hold
  - camera candidate pending
  - asset-specific rollback candidate
- frame segments applied:
  - F0. Scope Anchor
  - F1. Processing Tension / Problem Shift
  - F2. Input / State Preparation
  - F3. Attention / Selection Mechanism
  - F4. Output / Representation Result
  - F5. Block Support / Stability
  - F6. Support / Contrast / Limitation

### 4. Frame-Level Match Check

| frame segment | match status | evidence summary | note |
|---|---|---|---|
| F0. Scope Anchor | match / partial / missing |  |  |
| F1. Processing Tension / Problem Shift | match / partial / missing |  |  |
| F2. Input / State Preparation | match / partial / missing |  |  |
| F3. Attention / Selection Mechanism | match / partial / missing |  |  |
| F4. Output / Representation Result | match / partial / missing |  |  |
| F5. Block Support / Stability | match / partial / missing |  |  |
| F6. Support / Contrast / Limitation | match / partial / missing |  |  |

Frame-level match rule:
- Match the role, not the exact content.
- If exact content differs but segment role remains stable, mark partial rather than missing.
- If the frame must be forced to fit, mark missing and note rollback risk.

### 5. Content-Variation Check

| frame segment | content in base asset | content in probe target | variation type | acceptable? |
|---|---|---|---|---|
| F0 |  |  | none / light / strong / breaks frame | yes / no |
| F1 |  |  | none / light / strong / breaks frame | yes / no |
| F2 |  |  | none / light / strong / breaks frame | yes / no |
| F3 |  |  | none / light / strong / breaks frame | yes / no |
| F4 |  |  | none / light / strong / breaks frame | yes / no |
| F5 |  |  | none / light / strong / breaks frame | yes / no |
| F6 |  |  | none / light / strong / breaks frame | yes / no |

Content-variation rule:
- Encoder-side vs decoder-side difference can be acceptable if frame role remains stable.
- If content variation changes the segment role itself, do not promote.

### 6. Scope Anchor Split Check

- scope anchor frame-role present? yes / no
- scope anchor content-role identified? yes / no
- frame-role:
- content-role:
- does content-role overtake frame-role? yes / no
- pass / note / fail:

Scope anchor split rule:
- Scope anchor must lock the reading range.
- The content of the anchor may change per input.
- If scope anchor content is treated as universal frame content, rollback risk is present.

### 7. Support Placement Rule Check

- support lines present? yes / no
- support is attached to core segment? yes / no
- support became standalone center? yes / no
- support role type:
  - contrast
  - limitation
  - decision support
  - termination support
  - implementation note
- pass / note / fail:

Support placement rule:
- Support must attach to a core segment.
- Support must not become the primary reading object.
- If support inflation appears, do not promote.

### 8. Reuse Verdict

Choose one:

- reusable
- partially reusable
- asset-specific

Verdict reason:

### 9. Promotion Gate Status Update

| gate | required threshold | current evidence | status |
|---|---|---|---|
| evidence count | minimum 3 inputs |  | open / partial / pass |
| cross-shape input | minimum 1 cross-shape probe |  | open / partial / pass |
| frame-level match | most frame roles remain stable |  | open / partial / pass |
| content variation tolerance | content varies without breaking role |  | open / partial / pass |
| scope anchor split | frame-role and content-role separated |  | open / partial / pass |
| support placement | support stays attached and subordinate |  | open / partial / pass |
| non-forcing check | mismatch can be named without forcing |  | open / partial / pass |
| boundary safety | no axis/glossary/canonical drift |  | open / partial / pass |

Promotion status:
- hold
- one more probe needed
- eligible for camera-candidate review
- rollback to asset-specific

### 10. Rollback Signal Observed?

| signal | observed? | note |
|---|---|---|
| frame forcing | yes / no |  |
| scope collapse | yes / no |  |
| support inflation | yes / no |  |
| content overgeneralization | yes / no |  |
| axis drift | yes / no |  |
| glossary drift | yes / no |  |
| canonical drift | yes / no |  |
| low reuse value | yes / no |  |
| mismatch opacity | yes / no |  |

Rollback decision:
- no rollback
- keep hold
- rollback to asset-specific structure

### 11. Next Action

Choose one:

- hold
- one more probe
- rollback

Next action reason:

## Sample: Transformer1 -> Transformer2 Probe

### 1. Probe Target

- target asset: `inputs/external_cases/choi_ai_classroom_transformer2.txt`
- target asset role: sibling input
- why this target was selected: closest same-series transformer classroom input
- asset count used: 1 additional sibling txt
- broad scan avoided? yes

### 2. Probe Type

- probe type: sibling
- probe intent:
  - frame transferability check
  - scope anchor split check
  - support placement check
- not in scope:
  - new camera
  - axis promotion
  - glossary
  - canonical ingestion

### 3. Applied Hold Frame

- hold frame id: `provisional_reusable_reading_frame_hold`
- current status: hold
- frame segments applied: F0-F6

### 4. Frame-Level Match Check

| frame segment | match status | evidence summary | note |
|---|---|---|---|
| F0. Scope Anchor | partial | transformer2 centers decoder structure and autoregressive generation | anchor role transfers, content changes |
| F1. Processing Tension / Problem Shift | partial | training/inference tension replaces RNN-to-parallel shift | role transfers with decoder-side content |
| F2. Input / State Preparation | partial | shifted decoder input and masked attention setup | not the same as encoder Q/K/V setup |
| F3. Attention / Selection Mechanism | match | causal masked attention and cross-attention appear | attention role remains central |
| F4. Output / Representation Result | partial | next-token probability / generation output | result shape changes |
| F5. Block Support / Stability | match | residual, layer norm, feed-forward, block stacking remain present | stable support role |
| F6. Support / Contrast / Limitation | match | beam search, sampling, temperature, EOS/max length attach as support | support placement rule transfers |

### 5. Content-Variation Check

| frame segment | content in base asset | content in probe target | variation type | acceptable? |
|---|---|---|---|---|
| F0 | encoder-side self-attention + positional encoding | decoder structure + autoregressive generation | strong | yes |
| F1 | RNN sequence limit -> parallel processing -> order loss | autoregressive inference vs parallel training | strong | yes |
| F2 | token embedding -> Q/K/V projection | shifted decoder input / mask preparation | strong | yes |
| F3 | self-attention score/weight/value aggregation | causal mask + cross-attention | strong | yes |
| F4 | context-bearing representation | next-token probability / generation output | strong | yes |
| F5 | residual / norm / feed-forward support | decoder residual / norm / feed-forward support | light | yes |
| F6 | position contrast / rare-position limitation | generation decision / termination support | strong | yes |

### 6. Scope Anchor Split Check

- scope anchor frame-role present? yes
- scope anchor content-role identified? yes
- frame-role: lock the input reading range before segment interpretation
- content-role: decoder structure + autoregressive generation
- does content-role overtake frame-role? no
- pass / note / fail: note

### 7. Support Placement Rule Check

- support lines present? yes
- support is attached to core segment? yes
- support became standalone center? no
- support role type:
  - decision support
  - termination support
  - implementation note
- pass / note / fail: pass

### 8. Reuse Verdict

- partially reusable

Verdict reason:
The frame roles transfer, but the content changes from encoder-side reading to decoder-side generation reading.

### 9. Promotion Gate Status Update

| gate | required threshold | current evidence | status |
|---|---|---|---|
| evidence count | minimum 3 inputs | 2 inputs | open |
| cross-shape input | minimum 1 cross-shape probe | none | open |
| frame-level match | most frame roles remain stable | partially stable | partial |
| content variation tolerance | content varies without breaking role | observed | partial |
| scope anchor split | frame-role and content-role separated | observed | partial |
| support placement | support stays attached and subordinate | observed | partial |
| non-forcing check | mismatch can be named without forcing | observed | partial |
| boundary safety | no axis/glossary/canonical drift | maintained | pass |

Promotion status: hold

### 10. Rollback Signal Observed?

| signal | observed? | note |
|---|---|---|
| frame forcing | no | mismatches were named as variation |
| scope collapse | no | anchor role and content role were separated |
| support inflation | no | support stayed attached |
| content overgeneralization | no | encoder/decoder distinction preserved |
| axis drift | no | no promotion made |
| glossary drift | no | no glossary made |
| canonical drift | no | no canonical ingestion made |
| low reuse value | no | frame helped expose variation |
| mismatch opacity | no | partial matches were visible |

Rollback decision: keep hold

### 11. Next Action

- hold

Next action reason:
The frame is promising but needs at least one more probe, preferably one cross-shape input, before camera-candidate review.

## Closeout

- current lock: probe result template v0
- current reusable frame status: hold
- promotion blocked until: minimum evidence threshold and cross-shape probe are satisfied
- forbidden next drift:
  - axis promotion
  - glossary
  - canonical ingestion
  - new camera creation
