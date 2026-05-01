# Phase 1.15 Lower Input Softening Gap Audit Report v0

## Verdict

`PASS_WITH_NOTE`

The lower input organ is safe but still too hard at the point where split output is asked to serve upper evidence or packet admission. The gap is not provenance, trace, or source identity. The gap is the missing soft middle layer that can carry content-role, line seed pressure, and camera/axis support notes without triggering promotion.

## Gap Categories

| gap type | where it appears now | why it matters | dominant layer |
| --- | --- | --- | --- |
| `over-thin split` | raw dust split and some heading-only observer units | a unit can be readable but too narrow to carry line pressure or correction flow | lower |
| `over-hard evidence promotion` | split units and summaries move quickly into `evidence-ready` use | readability gets mistaken for interpretive readiness | bridge |
| `role missing` | source manifest and split units preserve identity but not function | upper must infer whether a block is definition, claim, correction, or connective work | lower |
| `line seed missing` | split -> evidence path has no middle carrier for repeated pressure or linkage hints | line-reading starts from brittle excerpts instead of seeded bundles | lower + bridge |
| `camera support missing` | lower artifacts rarely say which reading frame needs which context span | camera/lens work starts from raw material instead of prepared support | lower |
| `axis support missing` | lower outputs can hint at direction but cannot honestly hold an axis without promotion | upper either over-reads or has to rebuild support from scratch | lower + upper boundary |
| `provenance strong / argument weak` | source manifest, origin map, trace, routing artifacts | the organ knows where material came from, but not yet what argument-role the material performs | lower |
| `trace strong / interpretive support weak` | processing trace, receipts, operator summaries | process visibility is high, but line/axis/camera support is still sparse | lower + bridge |

## 4-Axis Reading

### A. Split Unit

Current split is strong for visibility and replay. It is weak when a unit becomes:

- heading-only;
- title-plus-bulk;
- transcript dust too small for thematic pull;
- block-shaped but not role-shaped.

The result is safe segmentation with low line-seed fertility.

### B. Content-Role

Current lower artifacts preserve:

- source identity;
- profile;
- split mode;
- ordering;
- run trace.

What they do not preserve well is the function of a chunk inside the source. `gmd_native_read` already emits `role_type`, but that layer is still a derived bridge artifact, not a narrow lower-organ minimum.

### C. Line Seed

Right now the common path is:

```text
split unit
-> evidence-ready
-> upper interpretation
```

That jump is too hard. A line seed layer is missing between split and evidence use:

- repeated pressure,
- linkage hint,
- question inducement,
- misunderstanding correction,
- tension marker.

### D. Camera Support / Axis Hold

Lower-side can already expose ordering and source-family echoes, but it does not yet leave a bounded note saying:

- which camera might read this material well;
- what context span is required;
- where rollback is needed;
- why axis promotion is not yet allowed.

## Interpretation

The lower organ is safe because it preserves source, trace, and route discipline. It is hard because it treats “made visible” as the last lower-side job.

Line/axis/camera reading needs one more layer before upper admission:

- content-role to say what a block is doing;
- line seed bundle to say what pressure is accumulating;
- camera support note to say what frame needs what span;
- axis hold support note to say what direction is visible but not promotable.

Without that layer, the bridge remains dependency-heavy. Codex must keep reconstructing meaning-bearing middle structure manually.

## Validation

- Lower problem vs bridge problem vs upper problem is separated: `PASS`.
- The 4-axis bottlenecks are explicit: `PASS`.
- No readiness or promotion rule was changed: `PASS`.
- The diagnosis stays inside Phase 1.13/1.14 guardrails: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created: `docs/reports/phase1_15_lower_input_softening_gap_audit_report_v0.md`
3. What was clarified: lower softness gap across split, role, seed, camera/axis support.
4. What remains unresolved: exact patch order and narrow role/seed field shapes.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended first implementation axis: content-role plus line-seed middle layer on top of current split outputs.
