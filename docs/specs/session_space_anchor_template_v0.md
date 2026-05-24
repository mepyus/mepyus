# Session Space Anchor Template v0

## Status

```yaml
status: template_candidate
baseline_lock: false
automation: false
purpose: current_task_reentry_anchor
```

Use this template before external-tool planning or any long Codex/Gemini/Hermes/OmX run.

This is not a full context bundle and not a space summary. It is a compact re-entry card.

```markdown
# SESSION_SPACE_ANCHOR

## Status

status:
current_date:
baseline_lock: false
automation: false

## Current Purpose

[What the user is trying to do now.]

## Current Work Type

[package setup / external tool run / reference program reuse / review recovery / implementation planning / return-to-space / space exploration]

## Current Line

[Long-flow line inherited by this work.]

## Current Axis

- [main tension 1]
- [main tension 2]

## Current Camera

- [viewpoint 1]
- [viewpoint 2]

## Current Lens

- [judgment criterion 1]
- [judgment criterion 2]
- [judgment criterion 3]

## Space Assets To Re-Enter

- `[path]`: [why this is useful now]
- `[path]`: [why this is useful now]
- `[path]`: [why this is useful now]

## Package Sizing Rule

Default to broad-but-bounded package when purpose, boundary, and return shape are clear.

Split into smaller sessions only if a blocking reason exists:

- user decision changes direction
- unapproved implementation or file modification would be needed
- broad scan is required
- evidence gap is blocking
- tool role is unclear
- current line cannot be selected
- return shape is unclear

## Stop / Continue

Stop for:

- [hard boundary]

Continue with Issue Log for:

- [watch item]

## Runtime Re-Entry Prompts

- Am I still on the current line?
- Did I split into small sessions by model default?
- Is this a hard boundary or watch item?
- Am I asking the user to relay tool output?
- Does the output include Return-to-Space Value?

## Return-to-Space Requirement

The result must include:

- Plan Basis or activated anchor
- read trace / evidence pointers
- issue or watch item
- Return-to-Space Value
- future reuse note
```

