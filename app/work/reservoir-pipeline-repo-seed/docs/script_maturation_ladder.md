# Script Maturation Ladder

## Status

```text
Status = candidate operating frame
Authority = script-growth boundary only
Not baseline
Not official workflow
Not automation
Not schema
```

## Purpose

Prevent script sprawl.

The goal is not to create many scripts early. The goal is to let repeated, working, low-risk parts of the repo process mature until scripting is the conservative next step.

## Core Rule

```text
Do not script a desire.
Script only a repeated operation whose inputs, outputs, boundaries, and failure modes have already appeared in records.
```

## Maturity Levels

| Level | Name | Meaning | Allowed action |
|---|---|---|---|
| 0 | Thought / friction | A user or worker feels repeated CLI cost | record the friction |
| 1 | Repeated manual move | The same read/check/setup move appears across runs | record examples |
| 2 | Stable packet shape | Inputs, outputs, and watch boundaries are visible | draft a script candidate card |
| 3 | Dry-run candidate | Script can report without mutating judgment | build dry-run/probe only |
| 4 | Setup-support script | Script reduces setup/checking cost | allow generated reports |
| 5 | Trusted helper | Script has survived repeated use without boundary drift | consider stronger integration |

## Promotion Conditions

A script candidate needs:

```text
at least two recorded manual examples
clear source refs
clear output refs
known not-read / not-touched boundary
known failure or WATCH behavior
human decision point preserved
dry-run mode if possible
no authority or baseline claim
```

## Scriptable Only After Evidence

Examples that may mature:

```text
minimum trace packet field audit
boundary label lint
manifest coverage surfacing
next run/output filename drafting
scaffold presence check
```

These are scriptable because they check structure. They do not choose meaning.

## Not Scriptable Yet

```text
source material selection
camera / lens choice
recovered judgment wording
reuse / HOLD / WATCH placement
promotion decision
whole-space interpretation
claim that a worker understands the user
```

## Existing Script Placement

```text
scripts/run_reservoir_pipeline_repo_seed_audit.py
```

Current placement:

```text
Level 3 -> Level 4 candidate
```

Reason:

It was created to test whether already repeated structural checks can be reported by script. It must not become a pattern for adding scripts whenever a new friction appears.

## Watch

```text
script count grows faster than recorded repeated operations
script output becomes authority
dry-run disappears too early
setup helper becomes judgment automation
scripts hide what the user needs to decide
```

`STATUS: SCRIPT_MATURATION_LADDER_PREPARED`
