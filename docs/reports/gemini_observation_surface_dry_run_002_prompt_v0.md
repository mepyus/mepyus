# Gemini Dry-run 002 Prompt
# Topic: Corrected Observation Surface Packet Classification
# Mode: DRY-RUN ONLY / NO IMPLEMENTATION / NO UI DESIGN

## Purpose
Run the 5 cases again using the correction rules from `docs/reports/observation_surface_dry_run_001_correction_note_v0.md`.

## Rules
- Use only allowed statuses:
  OK / RUNNING / FAILED / BLOCKED / VALIDATION_REQUIRED / HUMAN_REVIEW_REQUIRED / HOLD
- OK never means locked/promoted/baseline/truth.
- Worker result review defaults to Validation Packet.
- Research never transitions directly to Implementation.
- Refactor requires logic_changed=false.
- Baseline/schema/architecture impact requires human_review_required.
- File deletion requires Validation/Human Review.

## Cases to classify

### Case 1
Read-only report generated (No logic change).

### Case 2-A
Small text/code logic modification.

### Case 2-B
Structural cleanup (no logic change).

### Case 3
AI proposes baseline promotion for the packet flow.

### Case 4
AI proposes deleting outdated research reports.

### Case 5
Gemini returns external research result (Research Packet) with thought asset candidates.

## For each case, output:

case:
status:
packet_type:
scope:
risk_signal:
validation_required:
human_review_required:
next_packet_candidate:
recovery_candidate:
forbidden_next_step:
note:
why:

## Final evaluation

- Did status vocabulary stay controlled?
- Did validation and human review remain distinct?
- Did deletion/baseline impact go to human review?
- Did research avoid direct implementation transition?
- Did OK avoid lock/truth confusion?
- Is the structure too heavy?
- What should be simplified?

## Final report format

Verdict:
Created report files:
Modified source-space files:
Index updated:
Internal design artifacts created:

Corrected cases:
1.
2.
3.
4.
5.

Remaining ambiguities:
1.
2.
3.

Recommended simplification:
...

Do not proceed to implementation yet:
Yes
