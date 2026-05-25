# CODEX_SPACE_MATURATION_OPERATING_PRINCIPLE_HOLD_V0

status: HOLD / space operating principle

purpose:
Define how Codex matures the VectorFL space while Hermes owns execution. This is not an execution policy. It is the operating principle for how the space is observed, judged, verified, and proposed for maturation after new inputs and Hermes execution traces.

## 1. Separation From Execution

Hermes owns execution operation.

Hermes decides:
- how the user original is preserved
- what space reference is needed before execution
- how original + space + model reasoning are merged
- whether to execute or hold
- what trace, receipt, and reentry record are written

Codex owns space operation.

Codex decides:
- what the current space says before execution
- what space material should be retrieved for Hermes
- what Hermes actually used from the space
- what changed after Hermes execution
- whether the change creates a reusable pattern, stale handle, missing handle, or risk
- whether Gemini is needed as a Codex-side wide lens
- what HOLD-only maturation proposal should be written

The key boundary:
Execution produces results. Space operation decides how results should be remembered.

## 2. Space Maturation Loop

Every Codex space maturation pass follows this loop:

1. Observe
   Read only the relevant quick board, summary card, sync packet, trace, receipt, reentry record, pattern index, and compact controls.

2. Classify
   Classify the input as one of:
   - fresh space check
   - Hermes work analysis
   - pre-execution space retrieval
   - post-execution reentry maturation
   - full-history pattern maintenance
   - stale/superseded-handle review
   - Gemini ambiguity exploration

3. Compare
   Compare new material against:
   - current full-history pattern index
   - accepted structure layers
   - existing selected/rejected refs
   - known stale/superseded handles
   - HOLD/authority boundary

4. Judge Space Delta
   Decide whether the input:
   - creates a new reusable pattern
   - strengthens an existing pattern
   - changes the meaning of an existing pattern
   - exposes missing handles
   - makes older artifacts stale or superseded
   - creates duplicate pressure
   - risks treating HOLD as authority
   - does not change the space

5. Decide Gemini
   Use Gemini only when bounded files are insufficient and layer ambiguity remains.

6. Propose Maturation
   Write HOLD-only proposals such as:
   - pattern index addition
   - layer assignment
   - stale/superseded map update
   - missing handle creation
   - reentry schema repair
   - quick-board rule clarification
   - validation packet

7. Verify
   Validate JSON shape, sha256 references, namespace separation, no-mutation boundary, and promotion status.

8. Return
   Return a compact artifact that Hermes and the user can read quickly.

## 3. Maturation Judgment Types

Codex must choose one primary maturation judgment:

- `NO_SPACE_DELTA`
  The input does not change reusable space memory.

- `REFERENCE_ONLY`
  The input is useful evidence but should not become a pattern or handle.

- `STRENGTHEN_EXISTING_PATTERN`
  The input supports an already indexed pattern.

- `NEW_PATTERN_CANDIDATE`
  The input introduces a repeated or reusable operating structure.

- `LAYER_REASSIGNMENT_CANDIDATE`
  The input shows that an artifact belongs under a clearer layer.

- `STALE_OR_SUPERSEDED_HANDLE`
  The input makes prior language, handles, or files historically valid but no longer current.

- `MISSING_HANDLE`
  The input reveals that future readers need a named index, schema, route, or pointer.

- `BOUNDARY_RISK`
  The input risks confusing HOLD proposals with authority or execution permissions.

## 4. Gemini Use Principle

Gemini is not a default step.

Use Gemini when:
- multiple layers could claim the same artifact
- stale and current handles cannot be separated from bounded files
- a pattern may affect several arcs at once
- Codex needs wide cluster exploration before making a HOLD proposal
- Hermes trace conflicts with existing space index or reentry records

Do not use Gemini when:
- the answer is available from six or fewer bounded files
- the task is only status checking
- the result would merely summarize Codex's own file-grounded conclusion
- the call would make provider-backed exploration feel like normal execution

Gemini output is never authority. It is evidence for Codex judgment.

## 5. Required Output Shape

Every Codex space maturation artifact should include:

- `packet_id`
- `role`
- `read_files`
- `input_classification`
- `space_state_before`
- `comparison_basis`
- `space_delta_judgment`
- `maturation_decision`
- `gemini_exploration_decision`
- `proposed_space_changes_hold_only`
- `stale_or_superseded_handles_hold_only`
- `missing_handles`
- `boundary`
- `validation`
- `next_safe_lane`
- `promotion_status`

## 6. Space Health Invariants

Codex protects these invariants:

- original user input remains distinct from space memory
- Hermes execution trace remains distinct from Codex maturation proposal
- selected refs remain distinct from rejected refs
- model reasoning remains distinct from retrieved space
- HOLD proposal remains distinct from authority
- quick boards are cross-inspection surfaces, not authority
- immutable artifacts are not rewritten
- latest pointers point to immutable artifacts with sha256
- Gemini findings never replace Codex judgment
- missing handles are proposed before broad restructuring

## 7. Current Full-History Baseline

The current baseline is the eight-pattern HOLD index:

1. no-call recovery and current-position surface
2. prototype behavior loop
3. Phase2 function position stack
4. Phase3 structure relayering
5. Hermes-centered Codex space loop
6. provider-call budget governance
7. external space lens stack
8. space-operator governance and channel

Future space maturation should reference this baseline first, then decide whether the new input changes it.

## 8. Non-Negotiable Boundary

This principle does not authorize:
- source mutation
- authority mutation
- current-position apply
- registry mutation
- folder move
- promotion
- direct Codex API invocation
- direct Gemini API invocation
- Hermes direct Gemini invocation
- external API/server/replay execution

promotion_status: HOLD
