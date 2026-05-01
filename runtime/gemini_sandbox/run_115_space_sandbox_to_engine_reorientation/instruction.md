# Gemini Instruction - Run 115 Space Sandbox To Engine Reorientation

## Case

- case_id: `run_115_space_sandbox_to_engine_reorientation`
- task_type: Material Sorting + 4-line Card Drafting + Self-Check
- scope_level: bounded read / sandbox return only
- output_mode: write sandbox result files only
- output_path: `runtime/gemini_sandbox/run_115_space_sandbox_to_engine_reorientation/`
- forbidden_write_paths: every path outside `runtime/gemini_sandbox/run_115_space_sandbox_to_engine_reorientation/`

## Why This Run Exists

Run 113 and Run 114 correctly discovered a selection-protocol brake:

```text
needs_user_confirmation -> halt before artifact analysis
```

But the larger operation must not keep folding inward around sandbox procedure. The sandbox exists to test small operating moves, validate them, and then turn useful signals back toward the integrated engine, line/axis reading, CLI attachment, and reusable space material.

This run asks Gemini to help reorient outward.

## Primary Reading Rule

Use this as the default interpretation:

```text
The integrated engine keeps a three-surface body: user surface sets goal/scope/material context, VectorFL surface reads line/relation/gap/pending/reflux as a line-first middle layer, and engine surface processes/validates/records trace-memory/returns; team, handoff, worker, CLI, routing, and automation are operating extensions unless explicitly relocked.
```

Do not treat the sandbox as the final body. Do not treat Package 032 as the main goal. Treat Package 032 / Run 113 / Run 114 as evidence about operating brakes, authority boundaries, and worker behavior that may inform a current work package.

## Required Source Refs

Read only these docs:

1. `vectorfl_status.md`
2. `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md`
3. `docs/reports/integrated_engine_gemini_cli_orientation_v1.md`
4. `docs/reports/integrated_engine_working_protocol_v1_candidate.md`
5. `docs/reports/integrated_engine_process_first_work_package_next_checklist_v0.md`
6. `docs/reports/gemini_cli_operating_role_contract_v0.md`
7. `docs/reports/gemini_cli_sandbox_execution_protocol_v0.md`
8. `app/work/space-skill-sandbox/runs/run_113_selection_protocol_signal_closeout.md`
9. `app/work/space-skill-sandbox/runs/run_114_package_032_user_confirmation_preflight.md`
10. `app/work/space-skill-sandbox/outputs/package_032_user_confirmation_pending_v0.md`

Do not deep-read Package 032 candidate artifact contents.

## Task

Produce a short outward-facing reorientation return.

Answer these five questions:

1. What did the sandbox prove that is useful outside the sandbox?
2. Which part belongs to `user_surface`, `vectorfl_surface`, and `engine_surface`?
3. What is the current work package candidate that can move through the 3-surface engine body?
4. What should remain a brake / watch / hold rather than become structure?
5. What is the next Gemini-sized task that supports engine use without promoting Gemini into authority?

## Required Output Files

Write:

- `runtime/gemini_sandbox/run_115_space_sandbox_to_engine_reorientation/result.md`
- `runtime/gemini_sandbox/run_115_space_sandbox_to_engine_reorientation/self_audit.md`

Do not write any other file.

## Result Format

Use this exact structure in `result.md`:

```text
# Run 115 Result - Space Sandbox To Engine Reorientation

Verdict:

Material:

Source surface separation:

Useful sandbox proof:

3-surface mapping:

Current work package candidate:

Brake / watch / hold:

Next Gemini-sized task:

4-line card:
1.
2.
3.
4.

Risk:

Next:
```

## Self-Audit Format

Use this exact structure in `self_audit.md`:

```text
# Run 115 Self Audit

Did I avoid Package 032 artifact analysis?

Did I keep Gemini as support worker, not final judge?

Did I preserve the 3-surface body?

Did I turn sandbox signal outward toward engine / line / axis / CLI attachment?

Did I avoid schema, controller, index, automation, or baseline promotion?

Verdict:
```

## Constraints

- Do not modify repo files outside the sandbox output path.
- Do not create scripts.
- Do not update indexes.
- Do not create runtime manifests.
- Do not propose a new schema, controller, router, or automation loop.
- Do not convert `needs_user_confirmation` into a permanent classification system.
- Do not continue Package 032 artifact analysis.
- Do not flatten the work into "Package 032 is blocked"; the point is to extract an operating proof and aim it back at the integrated engine.

## Preferred Verdict

Use `PASS_WITH_NOTE` if the reorientation is useful but still needs Codex/User translation before it can become a canonical document or implementation target.
