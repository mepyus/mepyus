# Gemini Instruction - Run 117 Package 033 Preflight For Engine Verification

## Case

- case_id: `run_117_package_033_preflight_for_engine_verification`
- task_type: bounded simulation + 4-line card drafting + self-check
- scope_level: bounded read / sandbox return only
- output_mode: write sandbox result files only
- output_path: `runtime/gemini_sandbox/run_117_package_033_preflight_for_engine_verification/`
- forbidden_write_paths: every path outside `runtime/gemini_sandbox/run_117_package_033_preflight_for_engine_verification/`

## Current State

- baseline: Package 011 / Run 060, Trusted
- accepted_sequence_records: Package 012 through Package 029
- hold_closeout: Package 030 through Package 032
- package_033_status: HOLD / pending user review
- current_candidate: `engine_verification_brief_candidate_v0`

## Purpose

Run a bounded preflight simulation for `engine_verification_brief_candidate_v0`.

The simulation question is:

```text
Can the candidate brief help read sandbox records as engine-layer verification evidence while preserving candidate status, surface separation, user decision authority, and no implementation drift?
```

## Source Refs

Read only:

1. `app/work/space-skill-sandbox/outputs/engine_verification_brief_candidate_v0.md`
2. `runtime/gemini_sandbox/run_116_engine_verification_brief_candidate/result.md`
3. `runtime/gemini_sandbox/run_116_engine_verification_brief_candidate/codex_review.md`
4. `app/work/space-skill-sandbox/runs/run_113_selection_protocol_signal_closeout.md`
5. `app/work/space-skill-sandbox/runs/run_114_package_032_user_confirmation_preflight.md`
6. `app/work/space-skill-sandbox/runs/run_115_space_sandbox_to_engine_reorientation.md`
7. `app/work/space-skill-sandbox/runs/run_116_engine_verification_brief_candidate_packet.md`
8. `app/work/space-skill-sandbox/outputs/continuous_process_position_memory_rule_v0.md`

Do not read Package 032 candidate artifact contents.

## Task

Use the candidate brief against the summary records only.

Answer:

1. Does the brief remain candidate-only?
2. Does it preserve user / VectorFL / engine surface separation?
3. Does it help identify verification evidence without creating official logic?
4. What remains brake / watch / hold?
5. What process-position memory should be preserved for the next run?

## Required Output Files

Write exactly:

- `runtime/gemini_sandbox/run_117_package_033_preflight_for_engine_verification/result.md`
- `runtime/gemini_sandbox/run_117_package_033_preflight_for_engine_verification/self_audit.md`

Do not write any other file.

## Result Format

Use this exact structure:

```text
# Run 117 Result - Package 033 Preflight For Engine Verification

Verdict:

Simulation scope:

Candidate-only check:

Surface separation check:

Verification evidence check:

Brake / watch / hold:

Process-position memory:

4-line card:
1.
2.
3.
4.

Risk:

Next:

Position:
Direction:
Preserve:
Hold:
Next allowed step:
Next disallowed step:
```

## Self-Audit Format

Use this exact structure:

```text
# Run 117 Self Audit

Did I avoid Package 032 artifact analysis?

Did I avoid creating or approving Package 033?

Did I keep the candidate brief non-baseline and non-implementation?

Did I preserve the 3-surface body?

Did I avoid service, controller, schema, ledger, graph, ontology, and automation?

Did I include process-position memory?

Verdict:
```

## Guard

- Do not create Package 033 as accepted.
- Do not validate or close Package 032.
- Do not deep-read package artifacts.
- Do not implement a validator.
- Do not create service, controller, schema, ledger, graph, ontology, or automation.
- Do not promote sandbox rules into engine policy.
- Prefer `PASS_WITH_NOTE` or `HOLD` unless every boundary remains clear.
