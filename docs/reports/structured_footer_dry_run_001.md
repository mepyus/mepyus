# Observation Surface Dry-run 002: Structured Footer Validation

## 1. Case 1: Read-only report
--- STRUCTURED FOOTER v0 ---
status: OK
task_intent: Generate read-only report
packet_type: research
scope: read_only
summary: External lens synthesis report generated.
source_ref: user_instruction_01
risk_signal: low
validation_required: no
human_review_required: no
evidence_ref: docs/reports/ext_report.md
next_packet_candidate: none
note: Pass-through; no baseline impact.
--- END FOOTER ---

### Observation Surface Reading
- status: 완료
- user_facing_status: 완료
- visible_summary: Read-only report generated.
- risk_signal: 저위험
- needs_validation: 아니오
- needs_human_review: 아니오
- next_suggested_action: 완료

### Adequacy Check
- Footer provides all necessary signals for pass-through.
- Evidence reference is sufficient.

## 2. Case 2-A: Small text/code logic modification
--- STRUCTURED FOOTER v0 ---
status: VALIDATION_REQUIRED
task_intent: Update button label text
packet_type: implementation
scope: code_change
summary: Updated button_primary.css label.
source_ref: user_instruction_02
risk_signal: medium
validation_required: yes
human_review_required: no
evidence_ref: assets/css/button_primary.css (diff)
next_packet_candidate: validation
note: Logic unchanged; label update only.
--- END FOOTER ---

### Observation Surface Reading
- status: 검증 필요
- user_facing_status: 검증 필요
- visible_summary: Button label updated.
- risk_signal: 주의
- needs_validation: 예
- needs_human_review: 아니오
- next_suggested_action: 검증 단계 진행

### Adequacy Check
- `evidence_ref` (diff) is critical to prevent rubber-stamping.

## 3. Case 2-B: Structural cleanup
--- STRUCTURED FOOTER v0 ---
status: VALIDATION_REQUIRED
task_intent: Refactor CSS class names
packet_type: refactor
scope: structural_cleanup
summary: Renamed duplicate CSS classes.
source_ref: user_instruction_03
risk_signal: low
validation_required: yes
human_review_required: no
evidence_ref: assets/css/main.css (diff)
next_packet_candidate: validation
note: logic_changed=false confirmed.
--- END FOOTER ---

### Observation Surface Reading
- status: 검증 필요
- user_facing_status: 검증 필요
- visible_summary: CSS classes refactored.
- risk_signal: 저위험
- needs_validation: 예
- needs_human_review: 아니오
- next_suggested_action: 검증 단계 진행

### Adequacy Check
- Refactor packet properly separated from Implementation.

## 4. Case 3: Baseline promotion proposal
--- STRUCTURED FOOTER v0 ---
status: HUMAN_REVIEW_REQUIRED
task_intent: Propose new packet flow baseline
packet_type: validation
scope: baseline_proposal
summary: Proposal to baseline packet flow rules.
source_ref: codex_proposal_04
risk_signal: high
validation_required: yes
human_review_required: yes
evidence_ref: docs/reports/proposal_v0.md
next_packet_candidate: hold
note: AI cannot lock baseline.
--- END FOOTER ---

### Observation Surface Reading
- status: 사용자 판단 필요
- user_facing_status: 사용자 판단 필요
- visible_summary: Baseline proposal generated.
- risk_signal: 높음
- needs_validation: 예
- needs_human_review: 예
- next_suggested_action: 보류

### Adequacy Check
- `human_review_required` field correctly triggers the Sovereign Lock.

## 5. Case 4: File deletion
--- STRUCTURED FOOTER v0 ---
status: HUMAN_REVIEW_REQUIRED
task_intent: Delete outdated report files
packet_type: validation
scope: file_deletion
summary: Proposed deletion of report_v1, report_v2.
source_ref: user_instruction_05
risk_signal: high
validation_required: yes
human_review_required: yes
evidence_ref: list_of_files_to_delete
next_packet_candidate: hold
note: Deletion requires manual archival check.
--- END FOOTER ---

### Observation Surface Reading
- status: 사용자 판단 필요
- user_facing_status: 사용자 판단 필요
- visible_summary: Deletion proposed for 2 files.
- risk_signal: 높음
- needs_validation: 예
- needs_human_review: 예
- next_suggested_action: 보류

### Adequacy Check
- Prevents auto-deletion risk by forcing human review.

## 6. Case 5: External research result
--- STRUCTURED FOOTER v0 ---
status: VALIDATION_REQUIRED
task_intent: Synthesize external research
packet_type: research
scope: external_exploration
summary: Ambient status patterns researched.
source_ref: research_query_06
risk_signal: medium
validation_required: yes
human_review_required: no
evidence_ref: docs/reports/research_v06.md
next_packet_candidate: space_intake
note: Research != Implementation.
--- END FOOTER ---

### Observation Surface Reading
- status: 검증 필요
- user_facing_status: 검증 필요
- visible_summary: Research synthesized.
- risk_signal: 중위
- needs_validation: 예
- needs_human_review: 아니오
- next_suggested_action: 공간으로 흡수

### Adequacy Check
- Separates research from internal rule-making.

---

## Final evaluation
- **Did status vocabulary stay controlled?** Yes.
- **Did validation and human review remain distinct?** Yes, clearly separated by the review trigger.
- **Did deletion/baseline impact go to human review?** Yes, forced `HUMAN_REVIEW_REQUIRED`.
- **Did research avoid direct implementation transition?** Yes, routed to `space_intake`.
- **Did OK avoid lock/truth confusion?** Yes, marked as execution-only.
- **Is the structure too heavy?** The footer is manageable for the CLI/Codex worker to generate.

## Final report format
Verdict: PASS

Created report files:
- docs/reports/structured_footer_dry_run_001.md

Modified source-space files:
- None

Index updated:
- No

Internal design artifacts created:
- No

Corrected cases:
1. Read-only report (Success status)
2. Text update (Implementation path)
3. Refactor (Structural safety check)
4. Baseline proposal (Review lock)
5. Deletion proposal (Review lock)
6. Research exploration (Space intake path)

Remaining ambiguities:
- None

Recommended simplification:
- Move `source_ref` and `evidence_ref` to a secondary detail view (hover/click).

Do not proceed to implementation yet:
Yes
