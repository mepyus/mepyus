# Codex Space Execution Split Manual v0

## Purpose

This manual fixes the working split between:

- what Codex should do directly
- what the space should do through scripts
- what should be handled as a hybrid path

The goal is to reduce token-heavy full-manual handling as the space grows.

## Core Rule

Codex should not do everything itself.

Use space scripts first when the job is:

- probe
- validation
- sweep
- generated evidence collection
- bounded non-interpreting transformation

Use Codex first when the job is:

- interpretation
- cross-asset synthesis
- structural mapping
- boundary judgment
- report shaping
- reinjection judgment

Use hybrid when the job needs both:

- scripted evidence collection
- Codex-side interpretation and packaging

## Space-Script-First

Best for:

- direct probes
- direct gate checks
- validation chains
- sandbox or plan-first loops

Typical examples:

- `run_external_input_gate.py`
- `run_external_case_raw_intake_probe.py`
- `run_transcript_preprocess_comparison.py`
- `run_external_case_folder_sweep_loop.py`
- `run_transition_over_surface_*`

## Codex-First

Best for:

- what are we trying to do?
- how does this map into our space?
- what should be adopted, separated, or rejected?
- what should become a reusable answer?

These are interpretation-heavy and should not be offloaded to scripts alone.

## Hybrid

Best for:

- external repo/tool adaptation
- internal-plus-external comparison
- any task that says:
  - analyze
  - structure
  - compare
  - report
  - attach

Pattern:

1. use script surfaces to gather bounded evidence
2. let Codex synthesize and judge
3. keep final usable output and reinjection judgment on the Codex side

## Current Practical Rule

If a capability already exists in:

- [executable_capability_registry_v0.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/executable_capability_registry_v0.json)
- [executable_runner_index_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/notes/executable_runner_index_v0.md)
- [space_asset_execution_lane_map_v0.md](/Users/sungsookim/universe/vectorfl_replica/docs/guides/space_asset_execution_lane_map_v0.md)

then prefer:

- script for collection/probe/validation
- Codex for interpretation and final packaging

## Helper Entrypoint

Use:

- [run_execution_split_advisor.py](/Users/sungsookim/universe/vectorfl_replica/scripts/run_execution_split_advisor.py)

Example:

```bash
python3 scripts/run_execution_split_advisor.py "전처리 필요 여부 판정"
python3 scripts/run_execution_split_advisor.py "git_search 외부도구를 분석하고 우리 공간에 붙일 구조를 리포트해줘"
```

## One-Line Summary

Let scripts gather bounded evidence; let Codex decide what that evidence means and how it should be used.
