# Script Candidate Card - Recovery Helper Boundary 2026-05-11

## Status

```text
Status = script candidate card
Authority = proposal / maturation record only
Not implementation request
Not automation approval
Not baseline
Not schema
Not current-position update
```

## Candidate Name

```text
recovery_helper_boundary
```

## Friction Observed

```text
Gemini and runtime returns repeatedly require the same recovery pass:
  identify worker role
  identify source refs
  identify not-inspected scope
  downshift over-strong claims
  preserve WATCH/HOLD/RETURN placement
  record do-not-promote boundaries
  create movement/minimum-trace records
```

This is real CLI/reading cost, but the judgment inside the recovery is not scriptable yet.

## Recorded Examples

```text
example_1:
  app/work/space-skill-sandbox/outputs/gemini_whole_space_structure_map_exploration_return_packaging_20260511_v0.md
  app/work/reservoir-pipeline-repo-seed/records/run_271_gemini_return_minimum_trace_packet.md

example_2:
  app/work/space-skill-sandbox/outputs/gemini_runtime_to_current_position_connection_map_return_packaging_20260511_v0.md
  app/work/reservoir-pipeline-repo-seed/records/run_273_gemini_return_minimum_trace_packet.md

supporting earlier examples:
  app/work/reservoir-pipeline-repo-seed/records/run_256_minimum_trace_packet.md
  app/work/reservoir-pipeline-repo-seed/records/run_257_minimum_trace_packet.md
  app/work/reservoir-pipeline-repo-seed/records/run_266_minimum_trace_packet.md
```

## Inputs

Potential helper may read:

```text
one user-pasted worker return saved or provided as input
one packet/run record
worker_return_packaging_candidate_setting_three_modes_v0.md
script_maturation_ladder.md
existing minimum trace packet records
```

## Outputs

Potential helper may produce only draft scaffolding:

```text
missing-field checklist
candidate source refs list
not-inspected-scope reminder
do-not-promote checklist
draft output filenames
draft packet sections with blanks
```

## What It Must Not Decide

```text
whether the return is true
recovered judgment wording
reuse / HOLD / WATCH / RETURN placement
current-position update
baseline promotion
official workflow status
whether a script should run again
```

## Failure / WATCH Behavior

If material is missing:

```text
mark NEEDS_HUMAN_RECOVERY
do not infer missing source refs
do not infer not-inspected scope
do not classify placement
```

If material is partial:

```text
surface WATCH_REQUIRED
show which fields are thin
leave recovered judgment blank
```

If material contains authority claims:

```text
surface AUTHORITY_DOWNSHIFT_REQUIRED
do not auto-rewrite as accepted judgment
```

## Maturity Level

```text
Level 2 = stable packet shape visible / candidate card only
```

Reason:

```text
Repeated recovery shape exists, but no dry-run helper should be built until at least one more manual recovery confirms the same field pressure without new judgment needs.
```

## Promotion Condition

Move to Level 3 dry-run candidate only if:

```text
at least one additional worker/runtime return is manually recovered using this same shape
the helper scope remains field/checklist/stub only
all examples preserve human placement judgment
failure behavior is tested on a missing or partial return
the user explicitly wants a dry-run helper
```

## Watch

```text
helper becomes recovery judge
helper fills recovered judgment
helper decides current-position update
helper turns WATCH into pass
helper creates records without human review
script-first drift
```

`STATUS: SCRIPT_CANDIDATE_RECOVERY_HELPER_BOUNDARY_PREPARED`
