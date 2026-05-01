# Camera Support Bundle v0 Boundary Note

## Verdict

`PASS`

## Layer Comparison

| layer | what it does | what it does not do |
| --- | --- | --- |
| `content-role` | says what a chunk is doing locally | does not group pressure; does not choose observation mode; does not interpret |
| `line seed` | says what pressure/linkage is forming across units | does not pick a camera; does not interpret with a lens; does not name an axis |
| `camera support` | says what observation mode may later read the material meaningfully | does not interpret the scene; does not judge precursor/axis; does not promote |

## Why They Must Not Replace Each Other

### Content-Role Is Not Line Seed

Role tagging is local function.

It answers:

- definition?
- background?
- correction?
- connective?

It does not answer:

- what pressure repeats across adjacent units;
- what should be reread together.

### Line Seed Is Not Camera Support

Line seed groups local pressure:

- repeated pull;
- correction;
- tension;
- linkage.

It still does not answer:

- whether the next useful observation is change, boundary, or flow.

### Camera Support Is Not Lens Reading

Camera support only says:

- this material looks observable through change/boundary/flow.

It does not say:

- what that observation means structurally;
- whether it matures operationally;
- whether it survives validation;
- whether it forms an axis precursor.

Those are upper-side lens tasks.

## Why Camera Support Stops At Observation Possibility

The lower organ already carries:

- provenance;
- split trace;
- local roles;
- line seed pressure.

That is enough to say:

- “change-like support exists,”
- “boundary-like support exists,”
- “flow-like support exists.”

It is not enough to say:

- “this is structurally a reorganization,”
- “this is operationally the center,”
- “this matures the engine,”
- “this should become an axis.”

Those require upper lens reading and later precursor/held-axis judgment.

## Why Classification Must Stay `evidence_only`

`camera_support_bundle_v0` is still a support artifact:

- it carries hints and insufficiency;
- it is not an upper request frame;
- it does not establish packet-worthiness;
- it should travel as evidence support, not admission escalation.

If it moved beyond `evidence_only`, the system would confuse:

- observation possibility
with
- upper request intent.

That would violate the bridge minimum.

## Handoff Discipline

Correct chain:

```text
content-role
-> line seed
-> camera support
-> upper lens reading
-> precursor / held-axis judgment
```

Incorrect chain:

```text
content-role
-> camera support
-> axis naming
```

or

```text
line seed
-> camera support
-> packet candidate
```

## Why This Boundary Matters

Without this boundary:

- lower-side becomes an accidental interpretation engine;
- upper-side loses its lens function;
- support artifacts start pretending to be decisions;
- evidence-only discipline becomes porous.

The boundary protects honesty more than elegance.

## Compatibility With Current Working Core

This note stays compatible with the current core because it does not request:

- schema rewrite;
- classifier rewrite;
- bridge redefinition;
- promotion change.

It only clarifies division of labor.

## Thin Points In The Current Boundary

1. Some future camera-support emitters may be tempted to embed lens-like prose.
2. The distinction between strong line seed and weak camera support may blur in dense cases.
3. Flow camera can drift into structural interpretation unless wording stays narrow.

## Next Implementation Candidates

1. Emit `camera_support_bundle` companions from existing role+seed outputs.
2. Add wording guards so generated notes stay observation-possibility only.

## Risk If Implemented Too Early

1. Dense support notes may collapse line seed and camera support into one layer.
2. Flow support may be over-read as structural lens output before upper processing.
