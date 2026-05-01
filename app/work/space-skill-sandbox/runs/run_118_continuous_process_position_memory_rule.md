# Run 118 - Continuous Process Position Memory Rule

## Mode

CODEX / OPERATING RULE CAPTURE / NO AUTOMATION / NO BASELINE PROMOTION / NO IMPLEMENTATION

## Purpose

Capture the user's correction that the important practice is not a single daily snapshot or one Gemini session fix.

The durable need is continuous process-position memory: every meaningful direction change, misread correction, halt, candidate decision, and reorientation should leave a written record that preserves where the work is and why it moved.

## Current State

- baseline: Package 011 / Run 060, Trusted
- accepted_sequence_records: Package 012 through Package 029
- hold_closeout: Package 030 through Package 032
- current_candidate: `engine_verification_brief_candidate_v0`
- package_033_status: HOLD / pending user review

## User Correction Captured

The user clarified:

- today is not the point
- the point is to record and save every process as it happens
- the collaboration is long-horizon, not single-session focused
- correcting Gemini's single output matters less than analyzing why it misread and recording that analysis
- the records should protect direction and goals across future sessions

## Created

- `app/work/space-skill-sandbox/outputs/continuous_process_position_memory_rule_v0.md`

## Operating Consequence

Future run records, Gemini packets, Codex reviews, and package closeouts should include a small position addendum when the work is meaningful:

```text
Position:
Direction:
Preserve:
Hold:
Next:
```

This is a memory discipline, not an automated ledger.

## Boundary

- formal_ledger_created: false
- automation_created: false
- baseline_promotion: false
- schema_created: false
- controller_created: false
- package_033_promoted: false

## Next

Use this rule as a standing reminder when preparing Run 117 or any later Gemini packet: record not only the task result, but why the task is positioned that way in the larger sandbox-to-engine process.
