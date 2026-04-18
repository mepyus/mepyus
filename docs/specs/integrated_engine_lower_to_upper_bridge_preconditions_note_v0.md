# Integrated Engine Lower To Upper Bridge Preconditions Note v0

## 1. Verdict

PASS_WITH_NOTE

This note defines conservative preconditions for attempting a lower-to-upper input bridge. It does not declare a canonical bridge and does not automate packetization.

## 2. Eligibility Levels

| level | meaning | allowed next step |
| --- | --- | --- |
| not eligible | lower bundle is too thin, untraceable, or overread-prone | stop; keep as residue or evidence-only |
| evidence-only support | lower bundle can support a bounded claim but cannot form packet input | cite as evidence; do not translate to packet |
| eligible for bounded bridge attempt | lower bundle can supply evidence/trace/route support and upper-added fields are explicit | create one draft upper packet input |

## 3. Minimum Preconditions

### 3.1 Provenance Sufficiency

Eligible when:

- source path, source doc id, run id, or provenance link is visible
- artifact paths are inspectable
- source relation does not need guessing

Not eligible when:

- generated object has no source relation
- source can only be inferred from filename
- source relation conflicts across bundle members

### 3.2 Segmentation Legibility Threshold

Required only for content/source/reread bundles.

Eligible when:

- split mode or segmentation basis is visible
- unit ids or excerpts are inspectable
- the bridge explicitly blocks line-overread

Evidence-only when:

- segmentation exists but lacks source/run context

Not eligible when:

- units cannot be connected to source or run

### 3.3 Trace Sufficiency

Eligible when:

- receipt, processing trace, event id, or generated-output list shows how the object was formed

Evidence-only when:

- trace is partial but sufficient for a bounded citation

Not eligible when:

- no run, receipt, event, or trace relation can be found

### 3.4 Bundling Sufficiency

Eligible when:

- the bundle includes at least two complementary lower objects
- one object carries evidence/source/route
- another object carries trace/provenance/authority support

Not eligible when:

- a single lower artifact is asked to carry packet meaning

### 3.5 Route Legibility

Required for routing/authority bridge attempts.

Eligible when:

- routing labels, runmode, ticket relation, or receipt status are visible
- execution-linkable is not confused with executed or approved

Not eligible when:

- route state is absent or would need invention

### 3.6 Non-Line-Overread Condition

Eligible when:

- split units, GMD native read, or multi-lens surfaces are explicitly guarded as evidence/support, not line artifacts

Hard stop when:

- packet translation depends on treating lower units as lines

### 3.7 Packetization Support Threshold

Eligible only if upper-added fields can be made explicit:

- purpose
- scope boundary
- authority boundary
- selected lens
- allowed actions
- forbidden actions
- expected output shape
- next route candidate
- why this path was chosen

If these cannot be stated, the bundle may remain evidence-only but not bridge-eligible.

## 4. Bundle-Type Guidance

| bundle type | default eligibility |
| --- | --- |
| source manifest + split units + processing trace | eligible for bounded bridge attempt when line guard is explicit |
| label packet + routing basis + receipt | eligible for bounded bridge attempt when route purpose is explicit |
| origin map + provenance link + source manifest | evidence-only or eligible if purpose is source-return/reread grounding |
| GMD native read + split units + uncertainty | caution; eligible only with strong line/promotion guard |
| event ledger + command trace only | usually evidence-only or residue-only |

## 5. Phase 1 Validation

- Conservatism check: passed. Eligibility requires provenance, trace, bundle sufficiency, and upper-added fields.
- Bad-example block check: passed. Single artifacts and line-dependent translations are blocked.
- Lower/upper distinction check: passed. Upper-added packet fields remain mandatory.

