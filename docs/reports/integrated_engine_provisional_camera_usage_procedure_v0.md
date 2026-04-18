# Integrated Engine Provisional Camera Usage Procedure v0

## Status

PASS_WITH_NOTE

Current status:

```text
eligible for provisional camera candidate, not promoted
```

This is a review-stage procedure for using the C0-C6 provisional camera candidate.
It is not a promoted camera procedure.

## Procedure

| step | input | action | expected output | failure signal | rollback destination | advance condition |
|---|---|---|---|---|---|---|
| 1. baseline status check | current status note | Confirm `eligible for provisional camera candidate, not promoted`. | status line | promoted assumed | status distinction / review entry summary | status is explicit |
| 2. target-shape gate check | candidate target | Decide probe-valid vs rollback-only. | target-shape verdict | intake-note-only treated as full probe | usage boundary / asset-specific metadata | content-bearing target confirmed |
| 3. choose object | one valid target | Select one bounded object. | object scope | broad scan or many targets | process recovery checklist | one object selected |
| 4. choose lens or lens set | object scope + work purpose | Pick primary lens; optional secondary lens only if needed. | lens route | lens chosen for name appeal | lens-slot matrix | lens answers verification question |
| 5. apply C0-C6 with partial allowed | object + lens | Fill slots as match / partial / missing. | slot table | forcing all slots full | frame/content separation | missing/partial allowed |
| 6. mark missing / partial / match | slot table | Name why each slot fits or does not. | match status | vague "mostly fits" | fixed template | mismatch is visible |
| 7. detect rollback signals | match table + target shape | Check frame forcing, support inflation, drift, opacity. | rollback signal table | unhandled signal | rollback integration | signals absent or handled |
| 8. decide current result type | slot + rollback result | Pick candidate / hold / rollback / one-more-probe. | result type | canonical result implied | status distinction | result remains review-stage |
| 9. decide next action | result type | Choose hold / optional probe / review update / rollback. | next action | implementation or promotion opens | process recovery checklist | next action does not exceed status |
| 10. save report / note / runlog | final result | Save bounded note with evidence and rollback. | recoverable record | only chat memory | report/note storage | next reader can restart |

## Partial Rule

C0-C6 do not need to all be full matches.
Allowed values:

- match
- partial
- missing
- not applicable due target-shape

Missing is safer than invented content.

## C3 Mechanism Forcing Guard

C3 is the highest-risk slot.
Do not force a mechanism when the target only has topic, result, or support language.
If selection/foregrounding/route/attention/validation mechanism is not visible, mark C3 `missing` or `partial`.

## Candidate vs Canonical Rule

All outputs from this procedure are review-stage candidates.
Do not treat:

- slot match as promotion
- output/result as canonical
- support guard as camera rule
- repeated fit as axis

## Self-Check

- conflicts with process recovery checklist? no
- rollback discipline connected at steps 7-9? yes
- usage boundary enforced before applying C0-C6? yes
- C3 forcing guard explicit? yes
- canonical/candidate distinction explicit? yes

## Pointers

- Usage boundary: `docs/reports/integrated_engine_provisional_camera_candidate_usage_boundary_v0.md`
- Rollback integration: `docs/reports/integrated_engine_camera_verification_rollback_integration_v0.md`
- Review summary: `docs/reports/integrated_engine_provisional_camera_review_bundle_summary_v0.md`
