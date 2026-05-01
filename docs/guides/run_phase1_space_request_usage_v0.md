# Run Phase 1 Space Request Usage v0

## Purpose

`scripts/cli/run_phase1_space_request.py` is a thin wrapper over `scripts/cli/run_phase1_space_query.py`.

It helps users add lower artifact admission context before invoking the locked four-artifact spine.

## What It Does

- accepts a plain question or input file;
- accepts optional `--mode`;
- optionally classifies `--artifact-path`;
- supports `--admission-only`;
- appends bridge admission context to the request;
- calls `run_phase1_space_query.py`;
- preserves the four output artifacts.

## What It Does Not Do

- It does not replace `run_phase1_space_query.py`.
- It does not create a new runtime spine.
- It does not patch the lower input organ.
- It does not define line/axis/camera grammar.
- It does not promote lower evidence into packet candidates.

## Examples

Plain question:

```bash
python3 scripts/cli/run_phase1_space_request.py "Check the current bridge guardrail status" --stem phase1_14_example_plain
```

Explicit mode:

```bash
python3 scripts/cli/run_phase1_space_request.py "Compare old and new identity artifacts" --mode comparison --stem phase1_14_example_compare
```

Lower artifact context:

```bash
python3 scripts/cli/run_phase1_space_request.py "Use this lower artifact as evidence only" --artifact-path app/work/observer_ingest_min/generated/source_manifest_raw_intake_gap_analysis_before_middle_layer_fix_v1_20260409_184529.json --readiness-hint evidence-ready --evidence-only --stem phase1_14_example_lower
```

Admission-only:

```bash
python3 scripts/cli/run_phase1_space_request.py --admission-only --artifact-path runtime/events/engine_event_ledger.jsonl
```

Hold on risk:

```bash
python3 scripts/cli/run_phase1_space_request.py "Check risky final naming request" --hold-on-risk --stem phase1_14_example_hold
```

## Interpretation

The wrapper clarifies invocation. It is not the full invocation grammar design. It stays deliberately small so the stable subset remains intact.

Line/axis/camera grammar remains future work because it is promotion-sensitive and outside the Phase 1.13 lock.

## Validation

- Existing four-artifact spine remains the execution path: `PASS`.
- Classifier can be used without running the full spine: `PASS`.
- Wrapper does not replace the core entrypoint: `PASS`.
