# Evaluation - Source 16
# Maturation Queue Item Generator

## 1. Verdict

Verdict:
  GOOD_LANE_DIFFERENTIATION_NEEDS_DECISION_THRESHOLDS_WITH_WATCH

## 2. What Works

- It distinguishes Codex, Gemini, and user correction lanes well.
- It catches the main risk per lane:
  Codex -> execution success as approval
  Gemini -> synthesis as truth
  User -> correction as permanent baseline
- It produces a usable minimal field set.

## 3. Deficiencies

- It does not define threshold rules for mini vs full item.
- It does not say when a placement candidate becomes review-required.
- It has no confidence or uncertainty field.
- It may over-produce candidate outputs.

## 4. Direction Adjustment

Add threshold rules:

Full item required when:
  file write, command execution, API/credential/account, user correction, repeated WATCH, or promotion risk appears.

Mini item enough when:
  reference-only or simple compression with no boundary risk.

Review required when:
  conflict_signal is strong, promotion_risk is high, or boundary is unclear.

## 5. Supplement Needed

Add `uncertainty` and `why_full_item` fields to future generator drafts.

## 6. HOLD

- no automatic final placement
- no automatic surface update
- no memory/baseline write

`STATUS: EVAL_16_COMPLETED_WITH_WATCH`
