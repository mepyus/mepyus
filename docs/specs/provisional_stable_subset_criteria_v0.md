# Provisional Stable Subset Criteria v0

## Verdict

`PASS_WITH_NOTE`

This criteria document defines when a Phase 1.x artifact, rule, or flow can enter the provisional stable subset. It is a working stability rule, not a baseline promotion rule.

## Inclusion Criteria

An item may enter the provisional stable subset only when all are true:

1. Repeated run stability: validated across multiple bounded runs or successive phases.
2. Schema/runtime consistency: current scripts and runtime contracts can produce or consume it.
3. Guardrail compliance: it preserves hold discipline, bridge admission, and non-promotion rules.
4. Additive compatibility: it does not require removing older fields or rewriting canonical paths.
5. No destructive rewrite dependency: it can work without repository-wide migration.
6. No pending naming conflict: it does not require final taxonomy or official naming lock.
7. No baseline-authority conflict: it does not alter existing baseline or source authority meaning.
8. Operational value: future work would break real usage if it silently changed the item.

## Exclusion Criteria

An item must stay outside the provisional stable subset when any are true:

1. Heuristic-heavy and unbounded.
2. Promotion-sensitive, especially line/axis/camera material.
3. Dependent on broad archive treatment.
4. Dependent on full provenance graph or content-signature matching.
5. Operator-only and not yet reusable.
6. Requires final naming/taxonomy lock.
7. Requires lower input organ patch or schema rewrite.
8. Has not passed repeated run validation.

## Required Validation Evidence

Minimum evidence should include:

- a validation report with `PASS` or `PASS_WITH_NOTE`;
- runtime artifacts that parse as JSON when applicable;
- no baseline promotion or canonical path migration;
- hold/guardrail behavior tested by at least one bounded run;
- an explicit note for what remains heuristic.

## Guardrail Dependency

The subset depends on these guardrails:

- `evidence_only` is a valid stable landing zone.
- lower readiness and upper admission are separate.
- identity confidence does not imply readiness admission.
- pair confidence does not imply diff salience.
- diff salience does not imply authority promotion.
- hold is reserved for stop conditions, severe uncertainty, or user-owned decisions.

## Change Tolerance

Allowed changes:

- additive fields;
- helper improvements that preserve output lanes;
- more bounded examples;
- stricter validation that does not rewrite the spine.

Disallowed changes without a new review:

- removing the four-artifact chain;
- changing canonical runtime artifact directories;
- promoting evidence-only artifacts to packet candidates by default;
- final-locking taxonomy names;
- changing baseline meaning;
- moving line/axis/camera assets into stable core.

## Lock Boundary

The provisional stable subset may lock:

- flow shape;
- guardrails;
- minimal field families;
- compatibility requirements;
- do-not-change zones.

It may not lock:

- final taxonomy names;
- semantic scoring weights;
- broad archive policy;
- UI surfaces;
- provenance graph design;
- baseline promotion.

## Unlock Conditions

The subset must be reopened if:

- current runtime scripts can no longer produce four artifacts;
- bridge guardrail is violated;
- old/new comparison cannot distinguish legacy plausible identity from emitted strong identity;
- hold triggers become overbroad or silently bypassed;
- future lower-side patch requires changing admission semantics.

## Interpretation

Provisional stable means repeated operational stability, not "looks good." A feature can be useful but still excluded when it is too heuristic, too broad, or too promotion-sensitive.

Heuristic-heavy areas must stay outside because locking them would freeze provisional scoring or naming before enough diverse runs prove them.

## Validation

- Criteria can be applied to Stage 3 subset selection: `PASS`.
- Criteria are stricter than "useful" but looser than baseline promotion: `PASS`.
- Guardrail dependency is explicit: `PASS`.

## Stage Closeout

1. Verdict: `PASS_WITH_NOTE`
2. Files created: `docs/specs/provisional_stable_subset_criteria_v0.md`
3. What is now inside the subset: criteria only.
4. What remains outside: actual selection and lock.
5. Whether user decision is required: no.
6. Guardrail status: preserved.
7. Recommended next move: select the subset.
