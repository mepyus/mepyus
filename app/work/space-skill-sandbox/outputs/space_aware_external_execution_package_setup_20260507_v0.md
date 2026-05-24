# Space-Aware External Execution Package Setup v0

## Status

```yaml
status: package_setup_candidate
date: 2026-05-07
baseline_lock: false
automation: false
schema: false
registry: false
current_position_update: false
purpose: operating_principle_package_setup
```

## Basis

Activated anchors:

```text
app/work/space-skill-sandbox/outputs/space_aware_external_execution_intake_card_compact_20260507_v0.md
app/work/space-skill-sandbox/outputs/qmd_carrier_candidate_operating_setting_compact_v0.md
app/work/space-skill-sandbox/outputs/worker_return_packaging_candidate_setting_three_modes_v0.md
```

Operating rule:

```text
Plan from Space, not from Model Default.
```

Package rule:

```text
Do not create micro-runs by default.
Each package is a broad-but-bounded 10-12 session unit.
Each session must include execution, verification, test, and re-input.
Gemini or another external carrier can execute the sessions.
Codex prepares anchors/instructions and recovers package-level results.
```

## Global Session Contract

Every session in every package must return:

```yaml
session_id:
session_purpose:
active_anchors:
execution:
verification:
test:
reinput:
worker_return_shape:
  worker_role:
  input_purpose:
  anchors_used:
  how_anchors_changed_behavior:
  tool_output_summary:
  evidence_pointers:
  not_inspected_scope:
  issues_or_watch_items:
  return_to_space_value_candidate:
  do_not_promote:
hold_or_watch:
next_session_input:
```

Execution:

```text
Do the bounded work for the session.
```

Verification:

```text
Check whether the output used the provided anchors and respected HOLD/WATCH boundaries.
```

Test:

```text
Apply the output to one concrete target, sample, or edge case.
```

Re-input:

```text
State what the next session should receive as input.
```

## Global Stop Conditions

Stop package execution and return HOLD if:

```text
authority claim cannot be downshifted
baseline/schema/automation implementation claim appears
Return-to-Space Value is absent
full corpus indexing is requested
MCP/embed/query/rerank is promoted as default
user is forced into repeated copy-paste relay
package starts splitting into unmanaged micro-runs
```

## Package A - Worker Return Intake Hardening

Purpose:

```text
Harden the 10-field worker-return intake shape so external carriers can return recoverable package-level results.
```

Material family:

```text
Worker Return / Packaging Records
Task-Mode Gate Specs
Maturation / Residue Policy
```

Sessions:

```text
A01 - Intake Shape Regrounding
  execution: restate the 10-field shape from space anchors.
  verification: check no schema/baseline wording.
  test: map shape to one known success return.
  reinput: fields that were clear vs weak.

A02 - Success Case Mapping
  execution: apply shape to a successful external return.
  verification: confirm anchors_used and Return-to-Space candidate are present.
  test: classify recover with watch.
  reinput: success-mode rule.

A03 - Empty Failure HOLD
  execution: apply shape to an empty/silent return.
  verification: confirm missing anchors_used and missing Return-to-Space.
  test: classify HOLD without inferring meaning.
  reinput: empty-failure rule.

A04 - Partial Non-Empty WATCH
  execution: apply shape to a partial but usable return.
  verification: identify thin anchor trace and missing not-inspected scope.
  test: classify WATCH with downshift.
  reinput: partial-WATCH rule.

A05 - Mixed Claim Priority
  execution: evaluate a return with useful content plus overclaim wording.
  verification: decide downshift-to-WATCH vs HOLD.
  test: apply authority/baseline priority rule.
  reinput: HOLD/WATCH priority table.

A06 - Not-Inspected Disclosure Drill
  execution: inspect how missing/partial not-inspected scope should be added during recovery.
  verification: separate disclosed gap vs hidden critical gap.
  test: classify examples as WATCH or HOLD.
  reinput: disclosure rule.

A07 - Anchor Usage Trace Drill
  execution: evaluate thin vs behavioral anchor usage.
  verification: require how_anchors_changed_behavior.
  test: compare mention-only anchor vs behavior-changing anchor.
  reinput: anchor trace rule.

A08 - Return-to-Space Extraction
  execution: extract reusable judgment from three return types.
  verification: reject raw prose/logs as memory.
  test: produce 3-7 reusable judgment bullets.
  reinput: return extraction rule.

A09 - Micro-Run Prevention Gate
  execution: check whether recovery is creating tiny internal sessions.
  verification: enforce one package-level record.
  test: convert micro-run sequence into one package return.
  reinput: convergence gate.

A10 - Package Closeout
  execution: synthesize A01-A09.
  verification: confirm candidate-only status.
  test: produce one compact intake card update candidate.
  reinput: package-level Movement Record candidate.
```

Package return:

```text
WORKER_RETURN_INTAKE_PACKAGE_RETURN
candidate setting update
HOLD/WATCH priority table
one Movement Record candidate
do-not-promote list
```

## Package B - QMD Evidence Carrier Operationalization

Purpose:

```text
Make QMD usable as a bounded evidence access carrier without turning it into memory, authority, or automation.
```

Material family:

```text
External Material Intake Records
Task-Mode Gate Specs
Run Records
```

Sessions:

```text
B01 - QMD Candidate Setting Regrounding
  execution: restate QMD bounded pattern.
  verification: confirm candidate-only status.
  test: identify stop conditions.
  reinput: QMD safe-use rule.

B02 - Material Family Selection
  execution: select a 3-7 file active surface set by material family.
  verification: reject whole-corpus scope.
  test: explain why each file is active.
  reinput: active surface packet.

B03 - Pointer Discovery Shape
  execution: define search --json expected return.
  verification: hold QMD score as metadata.
  test: classify score/docid/snippet/URI as raw trace.
  reinput: pointer card.

B04 - Body Bundle Shape
  execution: define exact qmd URI multi-get --json follow-up.
  verification: avoid comma-separated glob groups.
  test: compare exact URI vs comma-glob behavior.
  reinput: body bundle card.

B05 - Evidence-to-Recovery Boundary
  execution: separate evidence pointer from interpreted memory.
  verification: enforce Codex recovery requirement.
  test: classify body bundle as raw/candidate material.
  reinput: recovery boundary.

B06 - Gate Anchor Retrieval Use
  execution: retrieve or simulate gate-spec pointers.
  verification: QMD is not anchor authority.
  test: apply retrieved pointers to one worker plan review.
  reinput: gate anchor application notes.

B07 - Failure / No Result Handling
  execution: handle empty QMD or no-match result.
  verification: classify HOLD vs WATCH.
  test: no recoverable pointer -> HOLD or alternate bounded query.
  reinput: failure handling rule.

B08 - Gemini Carrier Integration
  execution: have Gemini synthesize QMD evidence into one packaged return.
  verification: ensure Gemini output is candidate material.
  test: apply worker-return 10-field shape.
  reinput: Gemini packaged return.

B09 - Stop Condition Review
  execution: check full corpus/MCP/embed/automation pressure.
  verification: classify each as HOLD.
  test: produce hold list.
  reinput: stop-condition card.

B10 - Package Closeout
  execution: synthesize B01-B09.
  verification: confirm no baseline/schema/automation.
  test: produce one QMD carrier card update candidate.
  reinput: package-level Movement Record candidate.
```

Package return:

```text
QMD_CARRIER_PACKAGE_RETURN
active surface rule
pointer/body bundle rule
stop-condition table
one Movement Record candidate
```

## Package C - Gemini Broad-Bounded Carrier Protocol

Purpose:

```text
Set up Gemini so it can execute internal small work in one broad-bounded pass and return a recoverable package.
```

Material family:

```text
Task-Mode Gate Specs
Worker Return / Packaging Records
Current Position / Re-Entry Notes
```

Sessions:

```text
C01 - Instruction Shape Regrounding
  execution: restate Gemini default return shape.
  verification: no invented PVs or baseline language.
  test: apply to one sample task.
  reinput: instruction template.

C02 - Anchor Packet Intake
  execution: define what Gemini receives from Codex.
  verification: route/PV/LACL/material family present.
  test: detect missing anchors.
  reinput: anchor packet requirements.

C03 - Broad-Bounded Execution Discipline
  execution: define how Gemini bundles internal small steps.
  verification: no micro-run splitting.
  test: convert 3 small steps into one return.
  reinput: bundling rule.

C04 - PLAN_BASIS Gate
  execution: require PLAN_BASIS before synthesis.
  verification: check route and canonical PVs.
  test: reject model-default plan.
  reinput: plan basis check.

C05 - Evidence / Not-Inspected Discipline
  execution: require evidence pointers and not-inspected scope.
  verification: classify missing disclosure.
  test: WATCH vs HOLD.
  reinput: disclosure package.

C06 - HOLD/WATCH Classification
  execution: apply worker-return three modes.
  verification: prioritize HOLD over recoverable content when needed.
  test: success / empty / partial examples.
  reinput: classification table.

C07 - Return-to-Space Extraction
  execution: extract 3-7 reusable judgments.
  verification: remove raw trace.
  test: produce candidate Movement Record.
  reinput: return value set.

C08 - Do-Not-Promote Discipline
  execution: list non-promotions.
  verification: baseline/schema/automation/current-position absent.
  test: downshift overclaim wording.
  reinput: do-not-promote list.

C09 - User Relay Burden Check
  execution: detect repeated copy-paste relay burden.
  verification: package result into one pasteable return.
  test: compress multi-output into one package.
  reinput: relay bridge note.

C10 - Package Closeout
  execution: synthesize C01-C09.
  verification: one package-level return only.
  test: produce reusable Gemini instruction template candidate.
  reinput: Movement Record candidate.
```

Package return:

```text
GEMINI_CARRIER_PROTOCOL_PACKAGE_RETURN
default instruction template
return shape
HOLD/WATCH table
one Movement Record candidate
```

## Package D - Integrated Operating Trial

Purpose:

```text
Run one end-to-end external execution loop using the candidate settings without expanding into micro-runs.
```

Material family:

```text
Integrated Engine / Operating Surface Records
Worker Return / Packaging Records
External Material Intake Records
```

Sessions:

```text
D01 - Trial Purpose Selection
  execution: choose one bounded real task.
  verification: active material family and route are explicit.
  test: reject overbroad task.
  reinput: trial purpose.

D02 - Anchor Packet Draft
  execution: create one anchor packet.
  verification: route/PV/LACL/material family present.
  test: active surfaces 3-7.
  reinput: anchor packet.

D03 - Gemini Instruction Draft
  execution: create one broad-bounded Gemini instruction.
  verification: required return shape present.
  test: no micro-run language.
  reinput: Gemini instruction.

D04 - External Carrier Execution
  execution: Gemini performs bounded execution.
  verification: user returns one packaged result.
  test: result has worker-return fields.
  reinput: packaged return.

D05 - Codex Recovery
  execution: downshift and classify result.
  verification: evidence/gap/watch separated.
  test: HOLD/WATCH/success mode selected.
  reinput: recovery notes.

D06 - QMD Evidence Use If Needed
  execution: use QMD only if bounded evidence pointer access is required.
  verification: 3-7 active surfaces and exact URI list.
  test: no full corpus/MCP/embed.
  reinput: evidence bundle.

D07 - Return-to-Space Extraction
  execution: extract reusable judgment.
  verification: raw trace not promoted.
  test: 3-7 return bullets.
  reinput: return value.

D08 - Movement Record Candidate
  execution: draft one package-level record.
  verification: no per-step micro-records.
  test: includes future reuse note.
  reinput: record candidate.

D09 - User Judgment Gate
  execution: present direction choices.
  verification: user not routine relay.
  test: approve / hold / revise.
  reinput: user decision.

D10 - Package Closeout
  execution: close trial.
  verification: candidate-only status.
  test: next package recommendation.
  reinput: next package seed.
```

Package return:

```text
INTEGRATED_OPERATING_TRIAL_PACKAGE_RETURN
one end-to-end trace
one recovery
one Movement Record candidate
next package seed
```

## Recommended Order

```text
1. Package A - Worker Return Intake Hardening
2. Package C - Gemini Broad-Bounded Carrier Protocol
3. Package B - QMD Evidence Carrier Operationalization
4. Package D - Integrated Operating Trial
```

Reason:

```text
First harden what a worker return must look like.
Then make Gemini executable by others.
Then attach QMD as bounded evidence access.
Then run one integrated trial.
```

## Gemini Handoff Rule

For each package, Codex should create one Gemini instruction packet with:

```text
package purpose
session list
active anchors
stop conditions
required return shape
one package-level Movement Record candidate
```

Gemini should return one package result, not one result per session.

## Codex Recovery Rule

Codex should:

```text
recover package result once
downshift claims
classify HOLD/WATCH
extract Return-to-Space Value
write one package-level Movement Record only if reusable judgment exists
avoid per-session records unless a hard boundary requires it
```

## Do Not Promote

```text
not baseline
not registry
not schema
not automation
not current-position update
not final workflow
not QMD/Gemini/Codex authority
```

`STATUS: SPACE_AWARE_EXTERNAL_EXECUTION_PACKAGE_SETUP_PREPARED`
