# Lower Split Unit Reframe v0

## Verdict

`PASS_WITH_NOTE`

Current split units should be re-read as future line-seed carriers, not just segmentation leftovers. This is a reframe, not a split engine rewrite.

## Current Split Strengths

- Observer split preserves profile, split mode, unit refs, and ordering.
- Timestamp, heading, and paragraph splits are easy to inspect and trace.
- `source_manifest_*`, `split_units_*`, and `processing_trace_*` give bounded lower evidence.
- Existing split is stable enough to remain inside the lower readiness ladder.

## Current Failure Modes

| failure mode | example shape | problem for line seed |
| --- | --- | --- |
| `title_only` | heading block with almost no payload | no thematic pressure survives |
| `title_plus_bulk` | one heading block absorbs too much section text | role and support blur together |
| `transcript_too_fine` | dust-like short transcript segments | correction, pull, and tension fragment across units |
| `flow_without_role` | readable front/middle/end block | movement is visible, but function is not |
| `safe_excerpt_only` | excerpt is bounded but too thin | evidence-ready exists without line-seed fertility |

## Line-Seed-Friendly Split Criteria

A split unit is line-seed-friendly when it can support at least one of:

- a bounded content role;
- a repeated pressure that can be cited again nearby;
- a correction or objection move that changes reading direction;
- a connective move between adjacent units;
- a tension marker that can later justify hold/support note.

Useful signs:

- not only a title;
- not an unbounded section dump;
- adjacent references are easy to recover;
- excerpt preserves the unit's function, not only its topic.

## Over-Thin vs Over-Thick

| case | honest reading | action |
| --- | --- | --- |
| over-thin | too little pressure survives the cut | keep split, add post-split grouping or line-seed bundling |
| over-thick | multiple roles collapse into one block | keep split, annotate role mix or candidate sub-splits later |
| balanced | one dominant role plus bounded context | good seed input candidate |

## Do-Not-Change Boundary

This reframe does not:

- rewrite `inputter.py`;
- rewrite `run_observer_ingest_min.py`;
- change readiness labels;
- change bridge minimum;
- promote split units into packet-candidates;
- touch line/axis/camera promotion logic.

## Future Patch Candidates

- add adjacent support recovery for heading-only units;
- add post-split grouping for transcript-like material;
- add content-role tagging over current split outputs;
- add line-seed bundle assembly over multiple nearby split units.

## Interpretation

Split units should not be treated as final meaning atoms. They are seeds or raw pieces from which later meaning-support can be assembled.

Reframing first is safer than rewriting the split engine because the current split system already supports traceability. The missing work is what happens after split, not whether split exists.

## Validation

- Readiness ladder remains unchanged: `PASS`.
- Existing observer artifacts still fit this reframe: `PASS`.
- The proposal stays additive and lower-side: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created: `docs/specs/lower_split_unit_reframe_v0.md`
3. What was clarified: split units as line-seed-friendly raw carriers.
4. What remains unresolved: exact grouping heuristics for transcript-heavy material.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended first implementation axis: post-split role and seed annotation before any splitter rewrite.
