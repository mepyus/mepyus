# Lower Upper Admission Checklist v0

## Verdict

`PASS_WITH_NOTE`

This checklist fixes the minimum operator discipline for deciding whether a lower artifact can enter upper evidence, ingest, or packet use.

## Admission Checklist

Use `pass`, `weak`, or `fail` for each item. A `weak` result can still admit an artifact, but only with an ambiguity note or lower admission level.

| check | question | pass signal | weak/fail signal | operator action |
| --- | --- | --- | --- | --- |
| provenance clarity | Do we know where this material came from? | source path, input path, origin map, generated-from ref | missing source, only runtime residue | downgrade or reject |
| segmentation sufficiency | Is the material unit usable? | bounded unit with meaningful excerpt or clear object node | title-only, too fine, too large, metadata-only | evidence downgrade or next probe |
| routing clarity | Is its lower route/gate readable? | split mode, preprocess gate, decision reason, route marker | route not stated or mixed | add ambiguity note |
| trace presence | Can generation be traced? | run id, processing trace, receipt, generated timestamp | orphaned artifact | avoid packet-candidate |
| scope boundedness | Is the target bounded enough for upper use? | one source, one comparison, one question surface, one case block | broad dump or unbounded folder | keep as search target only |
| signal usefulness | Does it contain useful material signal? | source content, evidence cue, readiness signal, checkpoint | process noise only | reject for upper |
| packet-worthiness | Can it seed an upper packet? | interpretable goal, search target, constraint, expected next output | only evidence or raw material | keep evidence-only or ingest-ready |
| ambiguity note | Are limits named? | uncertainty, missing gap, weak route, weak readiness stated | uncertainty hidden | add note before admission |

## Admission Result Rules

| result | required minimum |
| --- | --- |
| `reject_for_upper` | fails signal usefulness or provenance clarity |
| `evidence_only` | passes provenance and signal usefulness; segmentation is at least weak |
| `ingest_ready` | passes provenance, routing clarity, trace presence, and scope boundedness |
| `packet_candidate` | passes all checks, especially packet-worthiness |

## Failure Modes

| failure mode | symptom | admission response |
| --- | --- | --- |
| `provenance_weak` | source is inferred from filename only | downgrade to lower trace or weak evidence |
| `split_too_thin` | unit is title-only, subtitle shard, or filler | evidence downgrade; request adjacent grouping |
| `split_too_thick` | unit is a large dump without local pointer | search target only, not evidence unit |
| `trace_missing` | no run id, processing trace, or generated-from context | block packet-candidate |
| `route_ambiguous` | lower says mixed/unclear or uncertain_needs_probe | keep as ingest-ready/evidence-only with ambiguity note |
| `residue_over_promoted` | receipt/event/log treated as source evidence | reject for upper |
| `packet_candidate_over_claimed` | evidence-ready artifact used as request frame | downgrade to evidence-only |
| `quality_vs_packet_confusion` | high-quality lower artifact lacks upper goal | do not promote beyond evidence or ingest-ready |
| `line_axis_overreach` | lower evidence used as line/axis promotion proof | block; leave future probe note |

## Interpretation

The bridge problem is more about admission discipline than schema. Existing upper contracts already have packet fields, evidence fields, and reingress notes. Existing lower organs already produce manifests, split units, traces, summaries, and comparisons. The missing layer is the disciplined answer to: "how far may this lower artifact travel upward?"

Lower artifact quality and packet-worthiness are different. A strong split unit may be excellent evidence, but it still should not define the upper request. A preprocess comparison may be packet-candidate because it contains readiness, gate decisions, and next-checkpoint structure.

## Validation

- The checklist can be applied by an operator without code changes: `PASS`.
- Failure modes are concrete and tied to lower artifacts: `PASS`.
- The checklist prevents residue and evidence over-promotion: `PASS`.
- The checklist does not redefine lower or upper contracts: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created: `docs/specs/lower_upper_admission_checklist_v0.md`
3. What was fixed at the bridge level: admission checks and failure modes.
4. What remains unresolved: real artifact example application.
5. Whether user decision is required: no.
6. Can Phase 1.12 start after this? not yet; example application should confirm usability.
7. Recommended next move: apply the rules to real artifacts.
