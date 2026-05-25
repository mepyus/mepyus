# SPACE_MATURATION_LOOP_SCALING_PRINCIPLE_V0

status: installed skill support / HOLD maturation policy

purpose:
Increase skill and loop execution so the user does not have to manually focus on every space maturation decision. The loop should run more often, but remain bounded, traceable, and HOLD by default.

## 1. Goal

The goal is not full automation.

The goal is assisted space maturation:
- Codex checks the space more often.
- Hermes execution records become Codex-readable reentry more consistently.
- Program/test results are inspected for space effect.
- Missing handles, stale handles, duplicate pressure, and boundary risk are surfaced early.
- User attention is reserved for approval, promotion, install, authority, or ambiguous high-impact decisions.

## 2. Loop Lanes

### L0: On-Demand Space Check

Trigger:
- user says "공간을 확인해"
- user asks status after a Hermes run
- quick board points to a new latest artifact

Codex action:
- read quick board and latest pointers
- produce a bounded space snapshot
- no Gemini by default

Output:
- `CODEX_SPACE_CHECK_RETURN`

### L1: Post-Hermes Reentry Maturation

Trigger:
- Hermes writes a Codex-readable reentry record
- Hermes merge trace includes `space_reference_delta`
- shared handoff board says Codex is waiting

Codex action:
- run the eight-step maturation loop
- classify space delta
- write HOLD-only maturation proposal

Output:
- `CODEX_SPACE_MATURATION_RETURN`

### L2: Program Result Space-Effect Inspection

Trigger:
- local fixture/test/program result passes or fails
- Hermes or Codex writes validation output
- user says "계속" after test output

Codex action:
- do not stop at pass/fail
- inspect program behavior, execution trace, space contact, space effect, and maturation decision

Output:
- `PROGRAM_RESULT_SPACE_EFFECT_RETURN`

### L3: Batch Pattern Maintenance

Trigger:
- several HOLD proposals accumulate
- duplicate artifacts appear
- stale/superseded pressure grows
- full-history arc index becomes stale

Codex action:
- batch related results into pattern maintenance
- propose index/status/supersession updates
- keep authority unchanged

Output:
- `PATTERN_MAINTENANCE_PROPOSAL`

### L4: Gemini Ambiguity Exploration

Trigger:
- bounded files cannot resolve layer ambiguity
- space effect may affect multiple arcs
- stale/current separation is unclear
- semantic flattening is suspected

Codex action:
- use Gemini only through Codex-side script-chain
- treat Gemini output as evidence
- Codex remains responsible for judgment

Output:
- `GEMINI_ASSISTED_SPACE_REVIEW`

## 3. User Attention Policy

Codex should not ask the user to decide every maturation detail.

Codex may proceed without extra user attention when:
- output remains HOLD
- no authority/current-position/registry/source/folder mutation occurs
- no provider-backed Gemini call is needed
- no installation/promotion/apply lane is being executed
- namespace separation is preserved

Codex must ask or require explicit approval when:
- installing or changing a skill
- applying authority/current-position/registry/source/folder changes
- promoting HOLD proposal to operational authority
- running provider-backed Gemini for wide exploration if not already approved
- executing external API/server/replay lanes

## 4. Default Return Discipline

Every scaled loop run should return:
- what triggered the loop
- which lane ran
- what files were read
- what changed in space
- whether the result touched existing patterns
- whether missing/stale/duplicate/boundary pressure exists
- whether Gemini was used or skipped
- what HOLD proposal was written
- what requires user attention

## 5. Safety Invariant

More loop execution must not mean more authority mutation.

Default:
`more observation + more HOLD proposals + better receipts`

Not default:
`automatic apply + hidden promotion + direct provider calls`

promotion_status: INSTALLED_SKILL_OPERATION_HOLD_BY_DEFAULT
