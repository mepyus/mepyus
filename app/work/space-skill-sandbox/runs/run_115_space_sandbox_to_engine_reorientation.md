# Run 115 - Space Sandbox To Engine Reorientation

## Mode

CODEX / SANDBOX INSTRUCTION AUTHORING / OUTWARD REORIENTATION / NO PACKAGE 032 ARTIFACT ANALYSIS / NO PROMOTION / NO AUTOMATION

## Purpose

Correct the Run 114 over-narrowing tendency.

Run 113 and Run 114 established an important brake: when candidate selection reaches `needs_user_confirmation`, analysis must halt. That brake remains valid. The correction is that the sandbox must not become the whole operating center. Sandbox proof should return to the integrated engine as current-work-package evidence, surface movement, line/axis signal, CLI attachment guidance, or reflux material.

## Re-read Summary

- `vectorfl_status.md`: current priority is the three-surface integrated engine body; CLI/agents are optional tool layers.
- `vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md`: user surface sets goal/scope/material context, VectorFL reads intermediate formations, engine processes/validates/records/returns.
- `integrated_engine_gemini_cli_orientation_v1.md`: Gemini/CLI can assist, but must not replace the body or promote language into final schema.
- `integrated_engine_working_protocol_v1_candidate.md`: user request must pass VectorFL review before engine processing; engine result returns to VectorFL validation before user decision/reflux.
- `integrated_engine_process_first_work_package_next_checklist_v0.md`: next useful work starts from one current work package moving through the 3-surface body, not more panels or inward documentation loops.
- `gemini_cli_operating_role_contract_v0.md`: Gemini is a bounded worker for fast reading, material separation, fixed trials, validation notes, and self-checks.
- `gemini_cli_sandbox_execution_protocol_v0.md`: Gemini may execute only read-only/sandbox-output tasks and must not modify existing repo files.

## Decision

Do not continue inward Package 032 artifact analysis yet.

Create a Gemini sandbox instruction that asks for an outward reorientation return:

- what the sandbox proved outside itself
- how the signal maps to the three surfaces
- what current work package candidate can move through the integrated engine body
- what remains brake/watch/hold
- what the next Gemini-sized support task should be

## Created

- `runtime/gemini_sandbox/run_115_space_sandbox_to_engine_reorientation/instruction.md`
- `runtime/gemini_sandbox/run_115_space_sandbox_to_engine_reorientation/next_packet.md`
- `app/work/space-skill-sandbox/outputs/next_gemini_task_packet_run_115_space_sandbox_to_engine_reorientation_v0.md`

## Boundary

- package_032_artifact_analysis: false
- user_confirmation_rule_removed: false
- implementation_change: false
- automation_created: false
- baseline_promotion: false
- schema_created: false
- controller_created: false
- index_updated: false

## Next

Run Gemini with:

```text
runtime/gemini_sandbox/run_115_space_sandbox_to_engine_reorientation/instruction.md
```

Then Codex should review `result.md` and `self_audit.md` before translating any useful signal into canonical docs or implementation work.
