# Pre-1.12 Lower -> Upper Bridge Diagnosis v0

## Verdict

`PASS_WITH_NOTE`

The lower input organ is not missing basic ingestion. The upper CLI spine is also not the primary weakness. The dependency-heavy bridge comes from the missing translation/handoff rule between lower output readiness and upper packet/evidence shape.

## What Bridges Well

| lower output | upper use that works | why |
| --- | --- | --- |
| source manifest | search target / source identity evidence | source path, detected profile, split mode, run id are explicit |
| split units | evidence pointer / excerpt target | unit refs and excerpts are available |
| processing trace | confidence / fallback note | split mode and engine stage are explicit |
| readable input board | human-readable evidence summary | front/middle/end and flow are visible |
| operator summary | quick exploration context | input recognition and decomposition are concise |
| preprocess comparison JSON | packet-candidate | before/after gates, readiness read, and next checkpoint exist |
| raw intake gap report | bridge diagnosis evidence | explicitly compares structured/external/raw paths |

## What Needs Heavy Human Interpretation

- converting split units into line/axis candidates;
- distinguishing generic discourse anchors from topic-bearing anchors;
- deciding when a preprocess sidecar is enough for direct ingest;
- deciding which lower residue should become upper search targets;
- converting readiness read into `task_mode`, `constraints`, `merge_mode_candidate`, and `ambiguity_notes`;
- selecting whether lower output is evidence, candidate packet, or just residue.

## Dependency-Heavy Points

| point | cause | lower 부족 | upper 부족 | bridge 부족 |
| --- | --- | --- | --- | --- |
| raw transcript -> upper evidence | dust units too fine; discourse anchors dominate | yes | no | yes |
| preprocess comparison -> upper packet | readiness exists but no direct packet mapping | partial | partial | yes |
| split unit -> line/axis | unit has excerpt but not semantic frame | yes | no | yes |
| operator summary -> evidence bundle | summary readable but source excerpts may be thin | partial | no | yes |
| route/projection docs -> CLI run | conceptual loop not wired to upper packet fields | no | partial | yes |

## Diagnosis

### Is lower itself insufficient?

Partly. Raw transcript intake is still weak without middle-layer aggregation. The raw intake report already identified missing functions: transcript normalization, discourse noise suppression, case block aggregation, provisional frame sketching, and compare-ready signal packaging.

### Is upper itself insufficient?

Not primarily. Phase 1.5~1.11 can interpret questions, explore space, produce evidence, merge/diff/hold, reingress, and handle grounded/structured/diff/pairing/identity artifacts. Its weakness is that it does not know which lower outputs deserve packet admission.

### Is the bridge rule insufficient?

Yes. This is the dominant gap. Lower outputs carry source/split/trace/readiness, but there is no stable mapping like:

```text
lower readiness + signal kind + route residue
-> upper packet search targets / constraints / evidence candidates / ambiguity handling
```

## Interpretation

The bridge is dependency-heavy because lower outputs are rich but not normalized into upper-handoff packets. Codex must read multiple lower artifacts, infer readiness, infer line/axis relevance, and then manually decide how to encode the upper run.

This is exactly a translation/handoff gap, not a retrieval gap.

## Validation

- Lower and upper are not conflated: PASS.
- Diagnosis is based on actual lower artifacts and Phase 1.x upper spine behavior: PASS.
- The root cause is separated into lower / upper / bridge: PASS.
- The dominant gap is bridge rule plus middle-layer packaging: PASS.

## Next Stage Entry

Proceed to middle-layer and efficiency judgment.
