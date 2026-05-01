# Lower To Upper Bridge Minimum v0

## Verdict

`PASS_WITH_NOTE`

This spec fixes the minimum admission rule between lower material intake outputs and the upper Codex CLI spine. It does not promote any lower artifact to baseline, does not change upper packet schemas, and does not patch lower input scripts.

## Scope

This document governs how lower-side outputs are admitted into the upper request-side loop:

```text
lower artifact
-> lower readiness classification
-> upper admission level
-> upper packet/evidence/reingress use
```

It applies to lower outputs such as:

- source manifests;
- split units;
- processing traces;
- label packets;
- routing basis records;
- observer summaries;
- preprocess comparison artifacts;
- generated lower residue.

## Non-Goals

- No lower input organ rewrite.
- No `inputter.py` or `labeler.py` patch.
- No segmentation rule change.
- No line/axis promotion logic change.
- No upper packet schema overhaul.
- No runtime artifact naming change.
- No baseline promotion.
- No final naming lock.
- No old artifact backfill.
- No UI or vector retrieval.

## Lower Readiness Definitions

| lower readiness | definition | typical artifacts | upper default |
| --- | --- | --- | --- |
| `residue-only` | useful operational trace, but not enough to support upper evidence or packet use | event ledgers, receipts, repeated runtime views, loose residues | `reject_for_upper` |
| `evidence-ready` | has provenance, source pointer, excerpt, trace, or readable support that can ground an upper claim | source manifest, split units, operator summary, raw intake report | `evidence_only` |
| `engine-ingest-ready` | lower engine or route can read it, but upper interpretation goal is not necessarily formed | input registry, preprocessed transcript text, structured lower input | `ingest_ready` |
| `packet-candidate` | includes enough provenance, bounded scope, route/readiness signal, and next-use hint to seed an upper packet | preprocess comparison JSON, selected GMD/native read, compare-ready lower package | `packet_candidate` |

## Upper Admission Levels

| admission level | meaning | allowed upper use |
| --- | --- | --- |
| `reject_for_upper` | do not lift into upper packet or evidence | may be mentioned only as lower trace context in a report |
| `evidence_only` | can support an upper exploration result but should not become the request frame | selected asset, evidence unit, supporting link, tension note |
| `ingest_ready` | can be pointed to as material the lower engine can process or has processed | search target, preprocessing constraint, next probe candidate |
| `packet_candidate` | can seed upper packet fields after checklist pass | interpreted goal seed, search targets, constraints, expected output shape, evidence candidates |

## Allowed Transitions

| lower readiness | allowed upper admission | allowed transition |
| --- | --- | --- |
| `residue-only` | `reject_for_upper` | keep lower; cite only as trace if necessary |
| `evidence-ready` | `evidence_only` | map to selected asset or evidence unit |
| `engine-ingest-ready` | `ingest_ready` | map to search target, constraint, or next probe candidate |
| `packet-candidate` | `packet_candidate` | map to upper packet seed and evidence candidate set |

## Blocked Transitions

| blocked transition | reason |
| --- | --- |
| `residue-only -> evidence_only` | trace existence is not source support |
| `residue-only -> packet_candidate` | residue does not contain bounded request intent or evidence frame |
| `evidence-ready -> packet_candidate` | evidence can support a question but does not define the question by itself |
| `engine-ingest-ready -> packet_candidate` | lower readability is not upper packet-worthiness |
| `packet_candidate -> baseline` | baseline promotion is out of scope |
| any lower readiness -> line/axis promotion | promotion logic is out of scope |

Exception: an artifact may move one level higher only when an accompanying report supplies the missing checklist items. The admission note must name the supporting artifact.

## Minimal Admission Checklist

Before a lower artifact enters upper use, check:

| check | admission meaning |
| --- | --- |
| provenance clarity | source path, origin, or generated-from context is visible |
| segmentation sufficiency | unit size is neither title-only nor unbounded bulk |
| routing clarity | route, gate, split mode, or readiness signal is stated |
| trace presence | run id, processing trace, or generation basis exists |
| scope boundedness | artifact points to a bounded material, problem, or comparison |
| signal usefulness | artifact contains source signal, not only process noise |
| packet-worthiness | artifact can seed a goal, search target, constraint, or expected output |
| ambiguity note | unresolved ambiguity is named instead of hidden |

Minimum required checks by admission:

| admission | required checks |
| --- | --- |
| `evidence_only` | provenance clarity, segmentation or pointer sufficiency, signal usefulness |
| `ingest_ready` | provenance clarity, routing clarity, trace presence, scope boundedness |
| `packet_candidate` | all checks, with packet-worthiness explicitly satisfied |

## Bridge Failure Modes

| failure mode | bridge response |
| --- | --- |
| provenance weak | keep lower or use only as weak context |
| split too thin | do not promote; require aggregation or adjacent support |
| split too thick | use as search target, not evidence unit |
| trace missing | avoid packet candidate; add ambiguity note |
| route ambiguous | keep at `ingest_ready` or `evidence_only` |
| residue over-promoted | reject for upper and record failure |
| packet candidate over-claimed | downgrade to evidence or ingest-ready |
| evidence treated as line/axis proof | block promotion; record as future probe |

## Operator Note

Default to the lowest honest upper admission. In this bridge, `evidence_only` is not a weak result. It is the normal safe landing zone for lower outputs that can ground upper reasoning but should not define the upper question.

`packet_candidate` must be earned by provenance, route clarity, bounded scope, and a usable next-use frame. A complete-looking lower generated file is not automatically a packet candidate.

## Interpretation

Lower readiness and upper admission must be separated because they answer different questions. Lower readiness asks whether the material has been made usable inside the lower input organ. Upper admission asks how much authority that material should have in the request-side CLI loop.

Not every lower output is packet-candidate because many outputs are evidence, traces, or processing aids. Promoting them directly would make the upper packet inherit lower process noise as if it were user intent.

The `evidence_only` level is important because it preserves valuable lower output without overclaiming it. It lets upper exploration cite and compare lower artifacts while keeping packet formation disciplined.

## Validation

- The rule is narrow and does not change upper schema: `PASS`.
- The rule applies to real lower artifacts from Pre-1.12: `PASS`.
- The rule blocks residue and evidence over-promotion: `PASS`.
- The rule keeps baseline promotion and final naming lock out of scope: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created: `docs/specs/lower_to_upper_bridge_minimum_v0.md`
3. What was fixed at the bridge level: readiness-to-admission transitions and blocks.
4. What remains unresolved: field-level mapping examples and operator checklist.
5. Whether user decision is required: no.
6. Can Phase 1.12 start after this? not yet; field mapping and examples should be written first.
7. Recommended next move: create field mapping guide.
