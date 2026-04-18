# Integrated Engine Lower To Upper Bridge Blockers And Stop Rules v0

## 1. Verdict

PASS_WITH_NOTE

Bridge attempts must stop when the lower bundle cannot support evidence/trace/route without forcing upper packet meaning into it.

## 2. Stop Rule Table

| blocker | type | what it means | required action |
| --- | --- | --- | --- |
| provenance too thin | hard stop | source relation is absent or guessed | stop; keep as residue-only |
| trace too incomplete | hard stop or caution | no run/receipt/trace relation for intended use | stop if no trace; caution if trace is partial |
| route too unclear | hard stop for routing bridge | runmode/authority/ticket relation missing | stop routing bridge |
| bundle too residue-heavy | hard stop | bundle is mostly logs/commands without evidence body | keep as audit residue |
| line-overread pressure too high | hard stop | translation depends on treating splits/GMD as lines | stop; require separate line/reread validation |
| upper-added context would dominate too much | caution stop | lower bundle supplies little beyond existence | keep as evidence-only or choose another bundle |
| missing purpose anchoring | hard stop for packet instance | no bounded reason for upper packet exists | stop before packet |
| authority boundary too unclear | hard stop | forbidden actions cannot be stated | stop before packet |
| expected output shape missing | caution stop | bridge can be discussed but packet instance would be vague | write evaluation only, no packet |
| lower/upper object collapse | hard stop | lower bundle is described as the packet itself | stop and rewrite as evidence bundle |

## 3. Hard Stop Conditions

Stop immediately if:

- the source cannot be identified
- artifact paths are not inspectable
- lower artifacts are called line artifacts
- a receipt is treated as semantic correctness
- `execution_linkable` is treated as execution complete
- the packet cannot state forbidden actions
- the bridge claim becomes canonical or automatic

## 4. Caution Stop Conditions

Pause or downgrade to evidence-only if:

- lower bundle is real but too summary-heavy
- trace exists but is minimal
- expected output shape is vague
- route is visible but not relevant to the requested bridge purpose
- too many fields must be upper-added

## 5. Stop Outputs

If a bridge attempt stops, produce one of:

- evidence-only note
- blocker note
- residue classification
- request for a better lower bundle

Do not produce:

- upper packet instance
- canonical bridge claim
- line extraction
- automation instruction

## 6. Phase 1 Validation

- Stop clarity check: passed. Hard stops and caution stops are separated.
- Bad bridge block check: passed. Overread, line inflation, and lower/upper collapse are hard stops.
- Reusable but bounded check: passed. Stop outputs are supervisory notes, not runtime implementation.

