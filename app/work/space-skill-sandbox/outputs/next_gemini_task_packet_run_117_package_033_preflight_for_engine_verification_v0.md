# Next Gemini Task Packet - Run 117 Package 033 Preflight For Engine Verification

## Mode

SANDBOX RETURN ONLY / BOUNDED SIMULATION / NO PACKAGE PROMOTION / NO IMPLEMENTATION / NO AUTOMATION

## Gemini Case

- case_id: `run_117_package_033_preflight_for_engine_verification`
- instruction_path: `runtime/gemini_sandbox/run_117_package_033_preflight_for_engine_verification/instruction.md`
- output_path: `runtime/gemini_sandbox/run_117_package_033_preflight_for_engine_verification/`

## Current State

- baseline: Package 011 / Run 060, Trusted
- accepted_sequence_records: Package 012 through Package 029
- hold_closeout: Package 030 through Package 032
- package_033_status: HOLD / pending user review
- current_candidate: `engine_verification_brief_candidate_v0`

## Task

Run a bounded simulation using only summary records and the candidate brief.

Answer whether `engine_verification_brief_candidate_v0` can help read sandbox records as engine-layer verification evidence while preserving:

- candidate status
- 3-surface separation
- user decision authority
- VectorFL mediation
- non-automated engine-side verification
- process-position memory

## Required Return

Gemini must write:

- `result.md`
- `self_audit.md`

The return must include a position addendum:

```text
Position:
Direction:
Preserve:
Hold:
Next allowed step:
Next disallowed step:
```

## Guard

Do not analyze Package 032 artifacts. Do not approve Package 033. Do not create or propose implementation, automation, service, controller, schema, ledger, graph, or ontology.
