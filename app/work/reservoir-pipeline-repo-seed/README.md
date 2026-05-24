# Reservoir Pipeline Repo Seed

## Status

```text
Status = repo-seed candidate
Authority = example / portable scaffold only
Not baseline
Not official workflow
Not automation
Not registry
Not permission system
```

## Purpose

This repo seed shows how to keep an original thinking space intact while attaching temporary pipelines for concrete purposes.

It must also keep the trace of how a pipeline was created. A future pipeline should be able to inspect:

```text
what source material was read
which space traces shaped the direction
which judgments were made during construction
which outputs were produced
what returned to the space
what remains watch-only
```

The seed does not copy the original space. It only carries a small operating shape:

```text
Original Space / Reservoir
-> Reservoir Access Gate
-> Asset Family Selector
-> Pump Attachment Frame
-> Temporary Pipeline
-> Sandbox Derivation
-> Return Channel
-> Reservoir Deepens
```

## How To Use

1. Start from a concrete user purpose.
2. Pass it through `templates/reservoir_access_gate.md`.
3. Select loose asset families from `docs/asset_families.md`.
4. Attach temporary ports from `docs/attachment_ports.md`.
5. Fill `templates/pipeline_connector.md`.
6. If the result is a derivative, fill `templates/sandbox_derivation_card.md`.
7. Return the result with `templates/return_record.md`.
8. Record the creation trace with `templates/process_trace_record.md`.
9. Update the source/reference map when new material shaped the pipeline.

## Script Maturation

Scripts are not added by default. A repeated operation must first mature through records:

```text
manual friction
-> repeated recorded move
-> script candidate card
-> dry-run/probe
-> setup-support script
```

See:

```text
docs/script_maturation_ladder.md
docs/scriptable_setup_map.md
```

Current probe:

```text
python3 scripts/run_reservoir_pipeline_repo_seed_audit.py --tag current
```

This checks scaffold shape, minimum trace packet sections, boundary labels, and manifest coverage. It does not decide recovered judgment, placement, or promotion.

## What This Protects

```text
the original space remains a reservoir
pipelines are temporary
ports are handles, not APIs
asset families are reading aids, not registries
derivatives are tested outside the reservoir
returns carry authority labels and watch items
the user remains the promotion gate
```

## First Example

See:

```text
examples/workplace_process_analysis_derivative_v0.md
```

This example uses a mock workplace process. It does not import real company data.

## Creation Trace

This seed was created from a real space-reading round. See:

```text
records/2026-05-11_pipeline_creation_trace.md
indexes/source_reference_map.md
records/decision_log.md
records/output_manifest.md
```

Those records are part of the seed. They are not administrative extras. They let another pipeline understand the intent, evidence, and direction behind this one.
