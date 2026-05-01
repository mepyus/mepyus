# Space Skill Sandbox Review v0

## Scope

Review the first sandbox loop:

```text
source refs
-> lens
-> skill
-> worker guide
-> test material
-> run
-> validation
```

## Verdict

```yaml
verdict: OK
status: sandbox_loop_validated
baseline: false
implementation: false
automation: false
source_space_modified: false
```

## What worked

- The sandbox stayed separate from the source space.
- One external material was used.
- Internal references were limited to two.
- The first run exposed that the skill was too long and that a lens/worker guide layer was missing.
- The retry added only the missing sandbox layers.
- The v0.1 skill is short enough for worker use.
- The final run returned a clear 4-line footer.
- Graphify remained a candidate lens, not an adoption mandate.

## What changed through the loop

```text
Round 1:
  skill + material + run existed
  but lens and worker guide were missing
  verdict: NEEDS_RETRY

Round 2:
  lens + short worker guide + short skill v0.1 + rerun existed
  user decision became clearer
  verdict: OK
```

## User burden check

The loop partially reduces user burden now.

It reduces:

- repeated explanation of external intake rules
- repeated warning against implementation drift
- repeated need to say "do not adopt this as baseline"
- repeated need to ask for a 4-line footer

It does not yet prove:

- real-world time savings
- behavior across multiple external materials
- whether Graphify itself should be tested as a tool

## Keep

- `external-material-intake-lens.md`
- `external-material-intake.v0_1.skill.md`
- `worker_guide_v0.md`
- `run_002_external_material_intake_graphify_v0_1.md`

## Hold

- Graphify installation
- Graphify hooks/watch mode
- MCP integration
- whole Deep Space graphification
- graph output reingestion
- skill baseline promotion

## Next bounded test

Run one real external material through `external-material-intake.v0_1.skill.md`.

Recommended candidate:

```text
Graphify small-folder read-only orientation question
```

Allowed:

- prepare a small test folder
- ask one graph-orientation question manually
- compare whether output helps the 4-line footer

Forbidden:

- whole-space graphification
- sensitive/private material
- always-on hook
- MCP integration
- baseline/schema/search adoption
