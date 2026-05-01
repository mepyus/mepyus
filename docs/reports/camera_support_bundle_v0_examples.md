# Camera Support Bundle v0 Examples

## Verdict

`PASS_WITH_NOTE`

These examples illustrate how lower-side camera support should look without carrying lens conclusions.

## Example 1 — Change-Centered

### Source Fragment

`preprocess reduced transcript noise, but intake should still be checked before mutation`

### Expected Content-Role

- `transition`
- secondary possibility: `objection`

### Expected Line Seed Character

- correction-pressure seed;
- regroup changed the material shape, but readiness is still not fully stable;
- local question: what exactly improved, and what still resists direct intake?

### Expected Camera Support Signal

- `camera_signal_summary`: change-like observation is supportable
- `change_signal_strength`: `medium`
- `change_support_note`: before/after regroup changed the material state enough to justify reread
- `boundary_signal_strength`: `thin`
- `flow_signal_strength`: `thin`

### Insufficiency / Gap

- still no upper interpretation of what the change means;
- missing cross-source confirmation;
- cannot conclude operational maturity from this fragment alone.

### Upper Lens Reference Note

Could later feed:

- structural lens as a reread candidate of state change;
- validation lens as a caution on “changed but not yet safe.”

This is only a reference memo, not lower artifact content.

## Example 2 — Boundary-Centered

### Source Fragment

`keep evidence-only as the default landing zone`

### Expected Content-Role

- `main_claim`
- secondary possibility: `connective`

### Expected Line Seed Character

- boundary-pressure seed;
- repeated non-promotion and admission-discipline reminder;
- local question: what must stay support-only even if it looks richer?

### Expected Camera Support Signal

- `camera_signal_summary`: boundary-like observation is supportable
- `boundary_signal_strength`: `medium`
- `boundary_support_note`: the fragment clearly supports hold/not-yet/evidence-only observation
- `change_signal_strength`: `thin`
- `flow_signal_strength`: `thin`

### Insufficiency / Gap

- does not say what upper interpretation should do with the boundary;
- does not name an axis;
- does not conclude whether this boundary survives other sources.

### Upper Lens Reference Note

Could later feed:

- operational lens for admission discipline;
- validation lens for anti-inflation brake.

Reference only.

## Example 3 — Flow-Centered

### Source Fragment

`content-role -> line seed -> camera support -> upper lens reading`

### Expected Content-Role

- `connective`
- secondary possibility: `transition`

### Expected Line Seed Character

- flow/linkage seed;
- the fragment organizes layer order and carry-forward direction;
- local question: where exactly does lower stop and upper begin?

### Expected Camera Support Signal

- `camera_signal_summary`: flow-like observation is supportable
- `flow_signal_strength`: `medium`
- `flow_support_note`: sequence and between-layer insertion are explicitly visible
- `change_signal_strength`: `thin`
- `boundary_signal_strength`: `thin`

### Insufficiency / Gap

- sequence visibility is present, but no structural interpretation should be stored lower-side;
- no judgment yet about whether this order is optimal or mature;
- still no axis naming.

### Upper Lens Reference Note

Could later feed:

- structural lens for layer-position reading;
- maturity lens for “support-bearing lower organ” development.

Reference only.

## Compatibility With Current Working Core

These examples remain compatible because:

- they stop at support;
- they preserve `evidence_only`;
- they avoid lens results in the lower artifact body;
- they avoid axis naming and promotion hints.

## Thin Points In The Current Examples

1. The examples show slot meaning clearly, but not yet a canonical serialization shape.
2. Boundary and flow examples can still drift into interpretive wording if generated carelessly.
3. Change examples are clearer on preprocess artifacts than on compact note fragments.

## Next Implementation Candidates

1. Prototype observer/preprocess family camera-support companions using these three example patterns.
2. Add a wording guard so emitted notes stay at “supportable observation” level only.

## Risk If Implemented Too Early

1. Example phrasing may be copied too literally into generators and become pseudo-lens output.
2. Change-centered cases may accidentally inherit before/after semantics as if they were verdicts.
