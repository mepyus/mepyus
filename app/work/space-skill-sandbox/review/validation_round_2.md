# Validation Round 2

## Target

Validate the retry loop:

```text
validation_round_1
-> add lens
-> add worker guide
-> add shorter skill v0.1
-> run_002_external_material_intake_graphify_v0_1
```

## Criteria

```text
1. Lens exists.
2. Worker guide exists and stays short.
3. Skill v0.1 stays short.
4. Run uses one external material.
5. Run references at most two internal criteria.
6. Run returns a clear 4-line footer.
7. Run avoids implementation/adoption drift.
8. Run gives user a concrete next judgment.
9. Sandbox remains separate from source space.
```

## Evidence

```yaml
lens_file: lenses/external-material-intake-lens.md
worker_guide_file: worker_guides/worker_guide_v0.md
skill_file: skills/external-material-intake.v0_1.skill.md
run_file: runs/run_002_external_material_intake_graphify_v0_1.md
worker_guide_lines: 50
skill_v0_1_lines: 50
internal_reference_count: 2
footer_exists: true
implementation_jump: false
automation_created: false
baseline_created: false
```

## Analysis

The first run proved the intake shape but was still too report-like.

The retry improved the loop by separating:

- lens: how to read external material
- skill: how a worker should execute the intake
- guide: what a worker reads first
- run: one concrete application
- review: whether the sandbox loop worked

The v0.1 skill is short enough for a worker to use. The run keeps Graphify in `borrow_later / graph_layer_candidate / caution_asset` instead of promoting it to adoption.

The next step is concrete and bounded:

```text
small test folder
read-only graph orientation question
no hook / MCP / whole-space graphification
```

## Verdict

```yaml
verdict: OK
reason: sandbox loop now satisfies the minimum success criteria without implementation or source-space modification
remaining_note: actual user burden reduction still needs one real user-facing run beyond Graphify-note simulation
```
