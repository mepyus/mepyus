# Next Gemini Task Packet - Run 122 Current Position Recovery

## Mode

CODEX -> GEMINI / STRUCTURE_PACKET / CURRENT POSITION RECOVERY / PACKAGE-LEVEL READ ONLY / NO IMPLEMENTATION / NO AUTOMATION / NO PROMOTION

## Case

- case_id: `run_122_current_position_recovery`
- instruction_path: `runtime/gemini_sandbox/run_122_current_position_recovery/instruction.md`
- output_path: `runtime/gemini_sandbox/run_122_current_position_recovery/`

## Purpose

Gemini should recover the current working position from bounded package/run records and return an `OBSERVATION_REPORT`.

This is not a Package 033 pilot. This is not artifact analysis. This is a recovery step so the next session can continue from the right position.

## Why Run 122

Run 121 already produced a narrow approval-gate halt for a proposed Package 033 pilot. It should be preserved as a bounded halted result, but it is not sufficient as current-position memory.

Run 122 asks Gemini to recover the broader current position.

## Read Scope

Use only the files listed in:

```text
runtime/gemini_sandbox/run_122_current_position_recovery/instruction.md
```

## Required Return

- `runtime/gemini_sandbox/run_122_current_position_recovery/result.md`
- `runtime/gemini_sandbox/run_122_current_position_recovery/self_audit.md`

## Expected Status

```text
CURRENT_POSITION_RECOVERED
```

## Boundary

- package_032_artifact_analysis: false
- package_033_accepted: false
- target_artifact_read: false
- implementation_change: false
- automation_created: false
- baseline_promotion: false
- whole_repo_scan: false

## Next

After Gemini returns, Codex reviews `result.md` and `self_audit.md`, then prepares the next structure packet or user decision request.
