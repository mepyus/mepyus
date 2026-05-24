# Stable Space Operating Anchor v0

## Status

```yaml
status: stable_anchor_candidate
baseline_lock: false
automation: false
read_before: external_tool_plan
```

## Anchor

VectorFL space is not a file store and not an external-tool memory bank.

VectorFL space is a memory-judgment-recovery loop. External tools are movement organs inside that loop.

Planning starts from a space anchor, not from model-default task decomposition.

Sessions are work units, not the authority layer. The authority layer is the current space purpose, activated memory, boundary judgment, and return route.

## Operating Rules

1. Read small relevant memory first.
2. Use pointer-based source checks before full-source rereads.
3. Treat broad scans as hard boundary unless explicitly approved.
4. Treat external tool logs, memory, and session state as raw trace.
5. Promote only interpreted Return-to-Space Value into VectorFL memory.
6. Distinguish hard boundary from watch item.
7. Use broad-but-bounded packages by default when the line, boundary, and return shape are clear.
8. Split into smaller sessions only when a blocking reason exists.

## Hard Boundary Candidates

- unapproved implementation or file modification
- broad scan without bounded activation route
- readiness / baseline declaration
- external runtime state treated as VectorFL memory
- user decision required but skipped
- automation, writer, runner, controller, or registry creation without explicit approval

## Watch / Continue Candidates

These should usually go to Issue Log while work continues:

- wording drift
- weak evidence pointer
- candidate-level instability
- non-blocking structure gap
- minor return-format mismatch
- uncertainty that can be preserved as future reuse note

## Required Return Shape

Every external-tool run or planning package should return:

- Plan Basis or activated anchor
- read trace / evidence pointers
- issue or watch item
- user-facing card when useful
- Return-to-Space Value
- future reuse note

## Runtime Re-Entry Questions

- Am I still on the current line?
- Did I split into small sessions by default?
- Is this a hard boundary or a watch item?
- Am I making the user a relay?
- Does this output include reusable judgment?
- Can this closeout become a Movement Record?

