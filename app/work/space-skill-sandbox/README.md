# Space Skill Sandbox

## Purpose

This folder is a small sandbox for testing whether existing deep-space assets can be lowered into short, usable worker skills.

It does not modify the source space.

It is not:

- baseline
- schema
- automation
- controller
- router
- reingestion system
- Graphify adoption
- official skill registry

## Current test

First test:

```text
external-material-intake.skill.md
-> Graphify note as test material
-> run_001_external_material_intake_graphify.md
```

The goal is to check whether a worker can:

1. read one external material
2. reference only 1-2 internal criteria
3. compare structure
4. make one small dry-run
5. self-check for drift
6. return a 4-line footer

## Success criteria

- The sandbox stays small.
- Existing source-space documents are not rewritten.
- The skill is short enough for CLI/Gemini/Codex to use.
- The run does more than summarize external material.
- The run does not jump to implementation.
- The user can judge proceed / hold / user-review-needed from the footer.

## Current status

```yaml
state: sandbox_candidate
baseline: false
automation: false
implementation: false
first_skill: external-material-intake
first_test_material: graphify_note
```
