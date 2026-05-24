# Evaluation - Source 25
# Packet Builder v0.1 Examples

## 1. Verdict

Verdict:
  USABLE_MINIMAL_PACKET_FORM_NEEDS_MODE_FALLBACKS_WITH_WATCH

## 2. What Works

- The three examples show why tool_mode matters.
- Codex, Gemini, and API/CLI packets correctly emphasize different risk focus.
- API/CLI packet properly treats auth status as execution-adjacent and HOLD.

## 3. Deficiencies

- It does not define what to do when tool_mode is uncertain or mixed.
- It does not include a "mode conflict" field.
- It risks making tool_mode look like an ontology.
- It does not tell when to split one mixed packet into multiple packets.

## 4. Direction Adjustment

Fallback rule:
  If tool_mode is unclear, use `unknown` and default to REFERENCE_ONLY or HOLD.

Mixed-mode rule:
  If a tool touches two high-risk modes, split packets by action:
  read packet first, execution/API packet only after explicit approval.

Mode conflict field:
  mode_conflict:
    [why one mode is insufficient]

## 5. Supplement Needed

Add unknown/mixed fallback lines to future Packet Builder guidance.

## 6. HOLD

- no tool_mode ontology
- no generic packet for mixed high-risk tool
- no dispatch from packet draft

`STATUS: EVAL_25_COMPLETED_WITH_WATCH`
