# Deficiency And Direction Adjustment Summary
# 05-15 Execution Evaluation

## 1. Status

Status:
  DEFICIENCY_SUMMARY_PREPARED_WITH_WATCH

Purpose:
  Consolidate evaluation results into explicit supplementation directions.

Not:
  promotion
  automation
  rewrite instruction
  baseline

## 2. Overall Evaluation

The 05-15 execution artifacts are now traceable and usable as candidate material, but they need a thinner practical layer before repeated use.

Core issue:
  The structure is rich, but the operating forms can still feel heavier than the work they are meant to support.

Primary correction:
  Keep the full forms as reference, but add small practical thresholds and short modes.

## 3. Main Deficiencies

### A. Queue Item Too Heavy

Problem:
  Full Queue Item reads like a schema.

Adjustment:
  Add Mini Queue Item for daily use.

Mini fields:
  source
  recovered
  WATCH
  HOLD
  boundary
  next

Use full item only when:
  command/file/API/credential/account risk, user correction, repeated WATCH, conflict, or promotion risk appears.

### B. Generator Needs Thresholds

Problem:
  Generator can over-produce candidates.

Adjustment:
  Add thresholds:
  full item required, review required, uncertainty.

Add fields:
  uncertainty
  why_full_item
  review_trigger

### C. Daily Loop Needs Load Control

Problem:
  Daily Loop can become ceremony.

Adjustment:
  Run only when triggered.

Triggers:
  three or more meaningful inputs
  user correction changes frame
  external tool result returns
  HOLD recheck appears
  next packet is being prepared

### D. Packet Builder v0 Too Generic

Problem:
  v0 does not account for tool-specific drift.

Adjustment:
  Use Packet Builder v0.1 minimal form by default.

Required:
  target_tool
  tool_mode
  risk_focus
  allowed
  forbidden
  hard_stop

### E. Codex Return Needs Short Mode

Problem:
  Full Return Packet is too heavy for no-write inspection.

Adjustment:
  Add Short Return:
  verdict
  direct answer
  WATCH
  HOLD
  next

Use Full Return only when:
  files read/written, commands run, patch/result evidence, or boundary-sensitive action occurred.

### F. Gemini Return Needs Evidence Strength

Problem:
  broad synthesis may sound stronger than source support.

Adjustment:
  Add fields:
  evidence_strength
  observation_type
  source_coverage

### G. Packet Builder Needs Unknown/Mixed Fallback

Problem:
  tool_mode may become taxonomy, and mixed tools may be under-scoped.

Adjustment:
  If mode is unknown:
    default to REFERENCE_ONLY or HOLD.

  If mixed high-risk:
    split packets by action.

Add field:
  mode_conflict

## 4. Direction For Next Iteration

Do not add new conceptual surfaces.

Instead, add a practical supplement layer:

1. Queue Item Mini Form
2. Generator Threshold Rules
3. Daily Loop Trigger Rules
4. Short Return Packet
5. Gemini Evidence Strength Add-on
6. Packet Builder Unknown/Mixed Fallback

These are supplements to make the existing structure usable, not new architecture.

## 5. Current HOLD

Still HOLD:
  promotion
  automation
  external dispatch
  current-position update
  output_manifest update
  product/UI integration
  AGENTS.md / SKILL.md changes
  eval file creation

## 6. Recommended Next Non-gated Work

Create one supplement file:
  `PRACTICAL_SUPPLEMENTS_V0.md`

It should contain only:
  mini forms
  thresholds
  short return
  evidence strength
  mixed-mode fallback

No new operating theory.

`STATUS: DEFICIENCY_AND_DIRECTION_SUMMARY_PREPARED_WITH_WATCH`
