# Scriptable Setup Map

## Status

```text
Status = candidate setup-support map
Authority = cost-reduction support only
Not baseline
Not official workflow
Not automation of judgment
Not schema
```

## Purpose

Reduce repeated CLI cost for the user by identifying which parts of the reservoir-pipeline repo seed can be checked or prepared by script.

The scriptable layer should help with setup and reading friction. It must not replace the user's promotion judgment or the space's return discipline.

This document is subordinate to:

```text
docs/script_maturation_ladder.md
```

That means no new script should be added only because a task feels repetitive. The repeated operation must first mature through records.

## Growth Boundary

```text
Do not grow scripts horizontally.
Grow script candidates vertically through evidence.
```

Flow:

```text
manual friction
-> repeated recorded move
-> script candidate card
-> dry-run/probe
-> setup-support script
-> trusted helper only after repeated use
```

## Scriptable

| Area | Script can do | Why safe | Output |
|---|---|---|---|
| Scaffold check | verify expected directories and required files exist | structural, not interpretive | OK/MISSING report |
| Trace packet audit | detect missing minimum packet sections | checks presence only | packet completeness report |
| Boundary label lint | flag missing `Not automation` / `Not schema` labels | prevents drift | boundary watch |
| Run/output naming | draft next run and output filenames | bookkeeping only | candidate paths |
| Manifest coverage | surface files absent from `output_manifest.md` | candidate sync only | WATCH list |
| JSON payload | emit machine-readable audit result | repeatable reading support | runtime payload |

## Must Stay Human

```text
selecting source material
deciding recovered_judgment wording
choosing reuse / HOLD / WATCH placement
promoting anything to baseline
declaring an official workflow
deciding to automate beyond setup/linting
```

## Existing Probe

```text
scripts/run_reservoir_pipeline_repo_seed_audit.py
```

Placement:

```text
Level 3 -> Level 4 candidate
```

It is a probe for the maturation ladder, not permission to create many scripts.

Use:

```text
python3 scripts/run_reservoir_pipeline_repo_seed_audit.py --tag current
```

Dry read:

```text
python3 scripts/run_reservoir_pipeline_repo_seed_audit.py --tag current --no-write
```

## Interpretation

```text
READY_FOR_SCRIPTABLE_SETUP_SUPPORT:
  current scaffold and packet checks passed.

READY_WITH_WATCH:
  usable, but one or more candidate sync or boundary watches exist.

BLOCKED:
  required scaffold or trace packet material is missing.
```

## Watch

```text
script output becomes authority
manifest becomes registry
trace packet becomes fixed schema
setup support becomes automation of judgment
user stops seeing the final placement choice
```

`STATUS: SCRIPTABLE_SETUP_MAP_PREPARED`
