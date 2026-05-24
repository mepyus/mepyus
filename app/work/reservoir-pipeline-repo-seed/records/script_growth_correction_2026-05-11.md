# Script Growth Correction - 2026-05-11

## Status

```text
Status = correction record
Authority = candidate operating correction
Not baseline
Not official workflow
Not automation
Not schema
```

## User Correction

```text
The goal is not to randomly increase scripts now.
The goal is to first set a large frame where scriptable parts mature through repeated operation, then gradually become scripts.
```

## Corrected Judgment

```text
Scripts should be downstream of accumulated working evidence.
They are not the starting point of the pipeline.
```

## Correction Applied

Created:

```text
app/work/reservoir-pipeline-repo-seed/docs/script_maturation_ladder.md
app/work/reservoir-pipeline-repo-seed/templates/script_candidate_card.md
```

Repositioned:

```text
scripts/run_reservoir_pipeline_repo_seed_audit.py
```

as:

```text
Level 3 -> Level 4 candidate
```

not:

```text
permission to add more scripts by default
```

## Operating Rule

```text
First accumulate repeated manual moves.
Then record a script candidate card.
Then dry-run.
Then allow setup-support scripting.
Only later consider stronger integration.
```

## Watch

```text
script-first drift
CLI-cost reduction becoming premature automation
candidate script becoming official workflow
more scripts appearing without repeated examples
```

## Return Placement

```text
RETURN_TO_SPACE_VALUE_WITH_WATCH
```

`STATUS: SCRIPT_GROWTH_CORRECTION_PREPARED`
