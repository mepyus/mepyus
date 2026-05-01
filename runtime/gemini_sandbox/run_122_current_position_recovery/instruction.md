# Gemini Instruction - Run 122 Current Position Recovery

## Mode

GEMINI / BOUNDED OBSERVATION WORKER / CURRENT POSITION RECOVERY / PACKAGE-LEVEL READ ONLY / NO IMPLEMENTATION / NO AUTOMATION / NO PROMOTION

## Case

- case_id: `run_122_current_position_recovery`
- output_path: `runtime/gemini_sandbox/run_122_current_position_recovery/`
- allowed_write_paths:
  - `runtime/gemini_sandbox/run_122_current_position_recovery/result.md`
  - `runtime/gemini_sandbox/run_122_current_position_recovery/self_audit.md`
- forbidden_write_paths: every path outside `runtime/gemini_sandbox/run_122_current_position_recovery/`

## Your Role

You are Gemini, a bounded execution / observation worker.

You do not decide direction. You do not approve packages. You do not promote baselines. You do not design new systems. Your job in this run is to read the bounded records listed below and return a structured observation report that helps Codex and the User recover the current working position.

## Why This Run Exists

Run 121 halted at a Package 033 pilot approval gate. That was compliant with its narrow instruction, but it is not enough for the next session because it does not recover the broader current position.

The project now needs durable current-position recovery before any further Package 033 pilot, Package 032 artifact read, or engine-facing promotion step.

There is also a larger memory problem. The recent restart / session-loss event showed that a lot of work can exist in the space while the next session still cannot re-enter from the right position unless there is a durable current-position surface.

Treat this as process-memory work, not a one-session fix. If a worker, CLI, or model loses context, times out, or lacks a tool capability, the useful result is not only the immediate failure. The useful result is:

```text
failure observed
-> cause analyzed
-> authority separated
-> next packet corrected
-> re-entry signal preserved
```

The ongoing work is:

```text
space rereading
-> lens / camera testing
-> sandbox experiments
-> Gemini / Codex role validation
-> failure and interruption recovery
-> return signals to integrated engine / line-axis / CLI attachment / process memory
```

The sandbox is a proving ground. It is not the destination.

## Read Scope

Read these files only:

1. `app/work/space-skill-sandbox/runs/run_113_selection_protocol_signal_closeout.md`
2. `app/work/space-skill-sandbox/runs/run_114_package_032_user_confirmation_preflight.md`
3. `app/work/space-skill-sandbox/runs/run_115_space_sandbox_to_engine_reorientation.md`
4. `app/work/space-skill-sandbox/runs/run_116_engine_verification_brief_candidate_packet.md`
5. `app/work/space-skill-sandbox/runs/run_117_package_033_preflight_for_engine_verification_packet.md`
6. `app/work/space-skill-sandbox/runs/run_118_continuous_process_position_memory_rule.md`
7. `app/work/space-skill-sandbox/runs/run_119_run_117_execution_packet_ready.md`
8. `app/work/space-skill-sandbox/runs/run_120_package_033_engine_verification_pilot_packet.md`
9. `runtime/gemini_sandbox/run_121_package_033_pilot_approval_gate/result.md`
10. `runtime/gemini_sandbox/run_121_package_033_pilot_approval_gate/self_audit.md`
11. `runtime/gemini_sandbox/run_117_package_033_preflight_for_engine_verification/result.md`
12. `runtime/gemini_sandbox/run_117_package_033_preflight_for_engine_verification/codex_review.md`
13. `app/work/space-skill-sandbox/outputs/continuous_process_position_memory_rule_v0.md`
14. `docs/reports/process_memory_operating_layer_candidate_v0.md`

Do not read Package 032 artifact contents.
Do not read `app/work/space-skill-sandbox/packages/package_032_boundary_trial/session_02_refinement/codex_review_bundle.md`.
Do not scan the whole repository.

## Task

Return an OBSERVATION_REPORT that answers:

1. What is the current position?
2. What is the last trusted baseline?
3. Which package range is accepted?
4. Which package range is hold / pending / not accepted?
5. What was the latest completed Gemini execution?
6. What did Run 117 prove, and what did it not prove?
7. What did Run 120 prepare?
8. What did Run 121 do, and why is it not enough as the next-session memory?
9. What is the next allowed step?
10. What must not happen next?
11. What should Codex preserve when preparing the next packet?
12. What memory / pipeline signal does this recovery step expose?
13. What should future sessions read first so they do not depend on chat memory?

## Required Output: result.md

Write `result.md` using exactly these sections:

```markdown
# Run 122 Result - Current Position Recovery

## Status

## Current Position

## Last Trusted Baseline

## Accepted / Hold / Invalid State

## Latest Completed Gemini Execution

## Run 117 Signal

## Run 120 Meaning

## Run 121 Meaning

## Next Allowed Step

## Next Disallowed Steps

## Process Memory Note

## Memory Failure / Pipeline Signal

## OBSERVATION_REPORT
```

The `OBSERVATION_REPORT` section must use this block:

```text
OBSERVATION_REPORT
from: Gemini
to: Codex / ChatGPT / User
type: current_position_recovery
status:
current_position:
last_trusted_point:
accepted_state:
hold_state:
invalid_or_orphaned_state:
latest_completed_execution:
next_allowed_action:
forbidden_moves:
memory_pipeline_signal:
next_session_entry_signal:
uncertainty:
```

## Required Output: self_audit.md

Write `self_audit.md` using exactly this structure:

```markdown
# Run 122 Self Audit

Did I stay within the listed read scope?

Did I avoid reading Package 032 artifact contents?

Did I avoid approving or promoting Package 033?

Did I avoid implementation, automation, schema, ledger, graph, ontology, service, router, hook, or controller creation?

Did I return observation rather than design authority?

Did I preserve user approval authority?
```

## Hard Boundaries

- No implementation.
- No automation.
- No package approval.
- No Package 032 artifact analysis.
- No Package 033 acceptance.
- No schema, ledger, graph, ontology, service, router, hook, controller, or baseline creation.
- No new operating law.
- No whole-repository scan.
- No source-space promotion.

## Expected Status

The expected status is:

```text
CURRENT_POSITION_RECOVERED
```

If you cannot answer from the read scope, return:

```text
BLOCKER_RAISED
reason:
needed_context:
```
