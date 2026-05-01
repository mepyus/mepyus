# Space Boundary Camera-Lens Operationalization Package v0

## 0. status

```yaml
package_status: package_candidate
verdict: PASS_WITH_NOTE-ready
purpose: operationalize the space-boundary camera and source-surface lens order across the whole space
baseline_lock: false
schema_enforcement: false
implementation_lock: false
runtime_manifest_creation: false
validator_creation: false
automatic_microspace_update: false
```

## 1. package purpose

The current goal is not to add more theory.

The current goal is to make this practical:

```text
any boundary material enters
-> source surface is detected
-> the right camera/lens order is activated
-> only the relevant space slice is read first
-> Codex judges state, relation, and next move
-> the result returns to space
```

This package exists because the OpenMythos case proved one path, but the user's target is broader:

```text
the whole space should behave like a device/camera with replaceable lenses,
not like separate manual workflows for external links, Codex output, runtime logs, and conversation material.
```

## 2. current problem statement

Current friction:

```text
The space has enough assets, but using them still depends too much on manual instruction.
Codex can read and analyze, but it may over-read the whole space or follow noisy keyword matches.
```

The correction is:

```text
source-surface-first reading
```

Not:

```text
load every package
run every process
create another heavy schema
```

## 3. assets to reuse

| Asset | Role |
| --- | --- |
| `scripts/cli/space_boundary_lookup_packet.py` | first-pass read-only source/candidate packet |
| `docs/indexes/space_boundary_material_flow_map_v0.md` | space-wide material flow map |
| `docs/indexes/space_translation_language_base_v0.md` | camera/lens and translation language base |
| `docs/indexes/external_material_microspace_index_v0.md` | external material re-emergence space |
| `docs/reports/space_feedback_loop_multi_surface_case_collection_v0.md` | cross-surface examples |
| `docs/reports/space_boundary_source_surface_lens_order_note_v0.md` | source-surface lens order draft |
| `docs/reports/space_feedback_loop_return_to_space_record_minimum_v0.md` | minimal internal return record |
| `docs/reports/space_feedback_loop_microspace_update_gate_v0.md` | update gate / no auto-index mutation |

## 4. operating principle

Every session must include:

```text
1. goal check
2. execution
3. validation
4. return-to-space judgment
```

Every session must answer:

- Did source-surface-first reading reduce space reread?
- Did Codex select lenses instead of following all script hints?
- Did the output stay as a 4-line user card when possible?
- Did the result return to space with a state?
- Did we avoid implementation, schema lock, and index mutation?

## 5. package boundaries

Allowed:

- run lookup packet on real cases
- read local docs/reports/runtime artifacts
- write bounded validation reports
- collect cases
- identify helper patch candidates
- prepare patch readiness notes

Not allowed:

- baseline lock
- schema enforcement
- runtime manifest creation
- validator creation
- automatic microspace/index mutation
- return-record writer implementation
- dashboard work
- broad workflow redesign

## 6. target operating loop

```text
input
-> source surface guess
-> source-surface lens order
-> relevant asset slice
-> Codex judgment
-> user-facing 4-line card
-> internal return record candidate
-> update gate
```

The main question is:

```text
Can this loop handle several input surfaces without becoming heavy?
```

## 7. source surfaces to test

Minimum surfaces:

| Surface | Example source | First lens order |
| --- | --- | --- |
| external material URL/file | `inputs/external_cases/*.md`, GeekNews URL | technical -> maker-intent -> user-intent -> line/axis -> risk -> residue |
| generated report / Codex output | `docs/reports/*_trial_v0.md` | user-intent -> line/axis -> risk -> residue -> return-state |
| runtime artifact / event log | `runtime/events/*.jsonl`, manifests, receipts | evidence/event -> technical -> risk -> residue -> line/axis |
| conversation material | user direction/friction statement | user-intent -> feature-direction -> line/axis -> residue -> risk |
| worker return / execution result | structured return, bounded comparison output | expected-vs-observed -> risk -> residue -> next-move -> line/axis |
| program artifact / generated index | generated bundles, label packets, origin maps | artifact-role -> evidence/event -> technical -> residue -> risk |

## 8. session list

## Session 0. orientation and purpose check

### Goal check

Confirm the package target:

```text
Make Codex read boundary material through a source-surface camera and lens order before loading broad space context.
```

Non-goals:

- write a new theory
- make a dashboard
- implement helper patch immediately
- create a mandatory user form

### Execution

Read:

- `space_feedback_loop_multi_surface_case_collection_v0.md`
- `space_boundary_source_surface_lens_order_note_v0.md`
- `space_feedback_loop_operationalization_closeout_v0.md`

### Validation

PASS if the next session can test real inputs without rereading the whole formation-movement stack.

### Return-to-space judgment

Expected output:

```text
short orientation note, or no new file if existing package is enough
```

## Session 1. source-surface lens order live validation

### Goal check

Validate whether the lens order note helps Codex filter noisy lookup results.

### Execution

Run the lookup packet on at least six cases:

1. external material file
2. generated report
3. Codex output report
4. runtime event/log artifact
5. conversation excerpt
6. program artifact or worker-return-like material

For each case:

```text
lookup packet result
-> source-surface lens order
-> Codex-selected lenses
-> noisy lenses rejected
-> 4-line card
-> return state
```

### Validation

Check:

- source surface detected correctly
- lens order improves over raw lens ranking
- Codex can reject irrelevant cluster hints
- output stays compact
- return state is explicit

Expected output:

```text
source-surface lens order validation report
```

## Session 2. asset-slice minimum check

### Goal check

Determine what minimal docs need to be read per source surface.

Question:

```text
Can Codex avoid loading the whole space by using a smaller source-surface asset slice?
```

### Execution

For each source surface, identify:

- required index/docs
- optional docs
- docs to avoid unless needed
- microspace check necessity

Candidate output shape:

```yaml
source_surface:
required_first_slice:
optional_second_slice:
avoid_by_default:
escalate_when:
```

### Validation

PASS if each source surface has a small first slice.

HOLD if the slice still requires broad package reread.

Expected output:

```text
source-surface asset slice minimum note
```

## Session 3. return-record fit across surfaces

### Goal check

Test whether the current nine-field return record minimum works outside OpenMythos.

Fields:

```yaml
source_ref:
input_summary:
selected_lenses:
space_relation:
codex_judgment:
return_state:
reemergence_trigger:
created_outputs:
do_not:
```

### Execution

Create return record candidates for at least four surfaces:

- external material
- generated report / Codex output
- runtime artifact
- conversation material

### Validation

Check:

- record is not too heavy
- user does not fill it
- re-emergence trigger is concrete
- `do_not` prevents over-promotion
- `space_relation` prevents detached summary

Expected output:

```text
cross-surface return record fit validation report
```

## Session 4. helper patch readiness check

### Goal check

Decide whether `space_boundary_lookup_packet.py` should be patched to weight lenses by source surface.

### Execution

Compare:

```text
raw helper lens ranking
vs
source-surface lens order
vs
Codex final lens selection
```

Across the validation cases.

### Validation

Patch is allowed only if:

- the same correction repeats across cases
- source-surface weighting reduces noise
- Codex judgment remains final
- implementation is small and read-only
- no schema/runtime/index mutation is introduced

Expected output:

```text
helper patch readiness report
```

Possible results:

- `NO_PATCH_collect_more_cases`
- `PATCH_CANDIDATE_lens_weighting_only`
- `HOLD_more_runtime_cases_needed`

## Session 5. bounded helper patch, only if ready

### Goal check

Only run this if Session 4 says:

```text
PATCH_CANDIDATE_lens_weighting_only
```

### Execution

Patch only:

```text
source-surface-weighted lens ranking
```

Do not change:

- final state decision
- object family
- schema
- index updates
- runtime writes

### Validation

Run the same cases from Session 1 again.

PASS if:

- noisy lenses decrease
- expected source-surface lenses rise
- top asset suggestions remain useful
- script stays read-only suggestion

Expected output:

```text
helper patch validation report
```

## Session 6. normal-use mini trial

### Goal check

Test the default user experience on one new user-provided or existing material.

### Execution

Run:

```text
lookup packet
-> source-surface lens order
-> minimal asset slice
-> Codex judgment
-> 4-line card
-> return record candidate
-> update gate
```

### Validation

Check:

- user only provides material
- Codex does not ask for process details
- output is not just summary
- space relation is visible
- next move is clear

Expected output:

```text
normal-use mini trial report
```

## Session 7. package closeout

### Goal check

Decide whether source-surface camera/lens operation is stable enough for normal use.

### Execution

Review Sessions 1-6.

### Validation

Decide:

- keep collecting cases
- patch helper
- create asset-slice index
- hold structure expansion
- open writer implementation package later

Expected output:

```text
camera-lens operationalization closeout report
```

## 9. execution checklist

Use at the start of every session:

```text
1. What input surface is being tested?
2. What is the correct first lens order?
3. What does the lookup packet suggest?
4. What should Codex accept or reject?
5. What minimal asset slice is needed?
6. What user-facing card is enough?
7. What return state should be recorded?
8. What must not be promoted or automated?
```

Use at the end:

```text
1. Did source-surface-first reading reduce noise?
2. Did user/operator burden go down?
3. Did Codex preserve judgment authority?
4. Did the material become easier to re-find?
5. Did we avoid schema/runtime/index overreach?
6. Is the next session clear?
```

## 10. recommended execution order

```text
Session 0
-> Session 1
-> Session 2
-> Session 3
-> Session 4
-> Session 5 only if patch-ready
-> Session 6
-> Session 7
```

Do not run Session 5 unless Session 4 explicitly justifies it.

## 11. current first action

Start with:

```text
Session 1. source-surface lens order live validation
```

Reason:

```text
The lens order note exists, but it needs real validation across surfaces before any helper patch.
```

## 12. guardrails

- Do not baseline lock.
- Do not enforce schema.
- Do not create runtime manifest.
- Do not create validator.
- Do not implement return-record writer.
- Do not auto-update microspace/index.
- Do not add object families.
- Do not let scripts choose final state.
- Do not turn this into a user form.
- Do not make dashboard work part of this package.

## 13. verdict

```yaml
verdict: PASS_WITH_NOTE-ready
next_allowed_move: execute_session_1_source_surface_lens_order_live_validation
main_risk: patching helper before source-surface lens order is sufficiently validated
preferred_mode: small cross-surface sessions, explicit validation, no automation until repeated evidence
```
