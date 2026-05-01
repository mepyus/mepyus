# Excerpt Extraction Rules v0

## Status

- phase: `phase1_6_evidence_grounding_hardening`
- authority: `working_spec`

## Execution

Extraction modes:

- `line_window`: take a small window around a matched line or the first meaningful line.
- `paragraph_block`: take the paragraph around the matched line, using blank lines as boundaries.
- `heading_plus_block`: take the nearest heading and the immediately following non-empty block.
- `bullet_cluster`: take adjacent bullet lines in the same local cluster.
- `pointer_only`: fallback when no useful excerpt can be extracted.

Default bounded limits:

- max excerpt lines: 12
- max excerpt characters: 1600
- preferred markdown mode: `heading_plus_block`
- preferred json mode: `line_window`

Extraction inputs:

- `path`
- `reason`
- optional terms derived from path/reason/request

Extraction output:

- `pointer`
- `excerpt_window`
- `excerpt_mode`
- `grounding_status`
- `local_confidence`

## Interpretation

Excerpt extraction here is not a full parser problem. Phase 1.6 only needs bounded grounding: enough local text to make the evidence unit inspectable and to prevent merge/diff/hold from being based on a path alone.

The safe fallback is `pointer_only`. If extraction fails, the run should continue and record that the evidence remains thin. This protects the Phase 1.5 spine from being blocked by parser edge cases.

Markdown specs and guides usually benefit from `heading_plus_block` because headings carry local meaning. JSON artifacts usually benefit from `line_window` or compact pretty excerpts because object structure matters more than prose paragraphs. Bullet-heavy guides can use `bullet_cluster`.

## Validation

- Excerpts must be short enough for runtime artifacts.
- Excerpts must not claim more than their local text supports.
- Extraction failure must not crash the usage loop.
- Pointer-only fallback must remain explicit.

## Stage Closeout

- Verdict: `PASS`
- Files created: this spec, fallback guide, and `scripts/cli/excerpt_helpers.py`.
- Extraction modes implemented: `heading_plus_block`, `paragraph_block`, `bullet_cluster`, `line_window`, `pointer_only`.
- Known weak document shapes: huge generated JSON, binary files, very long unbroken paragraphs.
- Entry condition for next stage: merge logic can read `grounding_status` and depth summary.
