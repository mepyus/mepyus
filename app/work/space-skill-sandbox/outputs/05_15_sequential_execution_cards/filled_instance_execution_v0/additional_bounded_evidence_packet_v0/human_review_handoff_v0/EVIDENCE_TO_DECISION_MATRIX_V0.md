# Evidence to Decision Matrix v0

verdict:
  EVIDENCE_TO_DECISION_MATRIX_PREPARED_WITH_PROMOTION_HOLD

current_decision:
  candidate remains candidate

why_not_component_yet:
  prior S8 found Gemini scope limitation over primary sibling inputs

if future scope-gap execution fails:
  decision: candidate remains candidate or STOP
  reason: added evidence did not resolve blocker

if future Gemini reads relay inputs but Codex finds overclaims:
  decision: candidate remains candidate
  reason: recovery still removes component-level claims

if future Gemini reads relay inputs and Codex confirms bounded evidence with no overclaims:
  decision: candidate-to-component review may be prepared
  reason: blocker may be reduced, but promotion still requires separate VectorFL/user approval

if any output claims promotion or authority mutation:
  decision: STOP
  reason: promotion/authority not approved

promotion_rule:
  No evidence packet self-promotes. Promotion requires separate explicit approval after recovery.

required_final_line:
  No promotion was performed. Recovery class remains candidate.
