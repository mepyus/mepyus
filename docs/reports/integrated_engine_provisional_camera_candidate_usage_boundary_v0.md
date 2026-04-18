# Integrated Engine Provisional Camera Candidate Usage Boundary v0

## Status

PASS_WITH_NOTE

Current status:

```text
eligible for provisional camera candidate, not promoted
```

This document defines where the C0-C6 provisional camera candidate may be used during review-stage work.
It does not promote the camera.

## Boundary Principle

Run target-shape gate before using C0-C6.
C0-C6 may be used only when the target is content-bearing enough to test the slots without invention.

## Allowed Target Shapes

| shape | why allowed | typical failure risk | immediate rollback destination |
|---|---|---|---|
| content-bearing report | Has sections, argument, correction, classification, or review body. | Treating report conclusions as canonical. | status distinction; verification/rollback discipline. |
| content-bearing transcript | Has enough body text to test scope, tension, mechanism, output, support. | Overfitting transcript content to camera slot names. | frame/content separation. |
| content-bearing design note | Has design body, conflict, salvage/hold, or projection material. | Design clay mistaken as baseline. | target-shape gate; support placement check. |
| content-bearing structural analysis | Has mapping, conflict, hold, and recommendation sections. | Support/conflict list becomes the center. | C6 support placement check. |

## Disallowed Target Shapes

| shape | why disallowed | typical failure risk | immediate rollback destination |
|---|---|---|---|
| intake-note-only | Has source pointer/topic hint but cannot test C1-C6. | Frame forcing from topic hint. | asset-specific metadata / support object only. |
| metadata-only | Has id, tags, or paths but no content flow. | Scope anchor mistaken for full probe. | target-shape gate. |
| pointer-only | References another object but does not contain body evidence. | Linked target treated as already read. | support object only. |
| index-only | Lists assets without processing or argument body. | Navigation list treated as reading structure. | navigation support only. |
| scaffold-only shell | Provides UI shell without content-bearing reading material. | Visual layout mistaken for process evidence. | screen-specific support review, not camera probe. |

## Probe-Valid vs Rollback-Only

Probe-valid:

- content-bearing target
- C1-C6 can be tested by evidence, with at least four slots meaningfully judged
- C0 scope anchor can be split into frame-role and content-role
- C6 support/guard can be attached to core segments
- mismatch can be marked partial/missing without forcing

Rollback-only:

- only C0 is visible
- source/topic metadata exists but no body
- support exists without core body
- applying C0-C6 would require invented segment content

## Content-Bearing Minimum Requirement

A target is content-bearing for C0-C6 review only if it contains:

- a readable object scope
- at least one tension, correction, or processing need
- some preparation/source/state/evidence setup
- a mechanism, mediation, selection, or projection rule
- a result, return, classification, or candidate output
- at least one support, limitation, contrast, guard, or rollback note

Partial slots are allowed.
Invented slots are not allowed.

## Allowed Returns In Candidate State

- slot match table
- content variation note
- scope anchor split
- support placement note
- rollback signal table
- candidate / hold / partial / missing verdict
- next action recommendation

## Forbidden Returns

- promoted camera
- axis
- glossary
- canonical record
- UI implementation instruction
- automation plan
- ingestion rule

## Self-Check

- target-shape gate conflict? no
- content-bearing rule conflicts with lens draft? no
- any "review eligible" wording used as "promoted"? no
- rollback destination present for allowed/disallowed shapes? yes

## Pointers

- Procedure: `docs/reports/integrated_engine_provisional_camera_usage_procedure_v0.md`
- Lens-slot matrix: `docs/reports/integrated_engine_lens_slot_compatibility_matrix_v0.md`
- Verification integration: `docs/reports/integrated_engine_camera_verification_rollback_integration_v0.md`
