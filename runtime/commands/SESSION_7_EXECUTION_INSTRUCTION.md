# SESSION_7_EXECUTION_INSTRUCTION.md

## 1. Goal
Create `REVIEW_RECOVERY_GATE_V0`, `CLASSIFICATION_RULES_V0`, `REVIEW_CHECKLIST_V0`, `DIGEST_EVIDENCE_RULES_V0`, and `USER_JUDGMENT_GATE_V0` to formalize the output validation, classification, and handoff process.

## 2. Search First
- Existing review/gate structures in VectorFL space.
- Recovery classifications (Recover, Candidate, Watch, etc.).
- Digest-first evidence requirements.
- User judgment escalation logic.
- Drift detection records.

## 3. Required Outputs (Artifacts)
- **Review & Recovery Gate**: Judgment fields (input source, classification, recoverable material, etc.).
- **Classification Rules**: Logic for Recover, Candidate, Watch, Hold, Reject, Needs Codex, Needs User, Boundary Risk.
- **Review Checklist**: Mandatory 15-point review for every tool output.
- **Digest Evidence Rules**: Minimum evidence requirements (material family, pointer, use case).
- **User Judgment Gate**: Explicit boundaries for when User judgment is mandatory.

## 4. Constraints
- **Preserve User Judgment**, don't overload it.
- **Recovery over Authority**: Treat output as recoverable material, not as final truth.
- No implementation, No automation.
- Log non-blocking issues.
- **Do not modify files or execute commands without user approval.**

## 5. Next Handoff
Prepare `SESSION_8_HANDOFF.md` for First Full Pass Plan session.
