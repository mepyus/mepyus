# Formation-Movement Interface Agent Skills Bounded Comparison Note v0

## 1. status

```yaml
status: comparison_note
mode: bounded_reread_only
verdict: PASS_WITH_NOTE
package_candidate_support: true
comparison_scope: agent_skills_reference_vs_internal_package_scenes
no_package_modification: true
no_baseline_lock: true
no_schema_enforcement: true
no_implementation: true
no_runtime_manifest: true
no_validator_or_script: true
no_reference_promotion: true
```

## 2. source

External source:

- GeekNews summary:
  `https://news.hada.io/topic?id=28294`
- upstream repository:
  `https://github.com/addyosmani/agent-skills`

Internal comparison scenes:

- `docs/reports/formation_movement_interface_agent_skills_external_reference_validation_case_v0.md`
- `docs/reports/formation_movement_interface_codex_oneshot_validation_case_v0.md`
- `docs/reports/formation_movement_interface_external_reference_ingest_validation_case_v0.md`
- `docs/reports/formation_movement_interface_package_draft_v0.md`

## 3. purpose

This note does not test whether `agent-skills` is correct in itself.

It tests a narrower question:

> When reread through the formation-movement package, does this external source behave mainly as direct evidence, defensive logic, or comparison frame?

Boundaries:

- no doctrine adoption
- no package patch
- no B lock
- no workflow import
- no baseline wording reuse

## 4. working judgment card

```text
현재 판정: strong defensive_logic + comparison_frame candidate
이유: 단계/검증/역할/품질게이트를 강하게 말하지만, 우리 내부 후보의 본체를 직접 증명하지는 않습니다.
다음 이동: Codex prepare / external ingest / validation gate 장면과 bounded compare
금지선: direct evidence lock, B promotion, operating rule 채택 금지
```

## 5. external source signals

From the GeekNews summary and upstream repository, the strongest repeated signals are:

- stage ordering:
  `/spec`, `/plan`, `/build`, `/test`, `/review`, `/ship`
- boundary / role sensitivity:
  specialized skills, context-aware activation, interface-oriented design
- verification / quality gates:
  “tests are proof,” review before merge, quality gates, structured verification
- anti-rationalization / anti-shortcut posture:
  explicit workflow discipline against skipping steps

Most likely package contact points:

- `A`:
  precedence, sequencing, what must come first
- `B`:
  role-boundary organization, interface separation, worker/task distinction
- `C`:
  proof, review, gate, validation, anti-premature completion

## 6. comparison scene 1: Codex prepare case

Reference scene:

- `formation_movement_interface_codex_oneshot_validation_case_v0.md`

### what the internal scene says

- a Codex task should not jump from vague intent into execution
- `prepare_worker_packet` is not execution
- packet readiness depends on boundary, expected return, guardrail, and return hook

### what the external source adds

- stage discipline strongly supports the idea that preparation and execution must be separated
- “spec before code” and “tests are proof” reinforce the idea that bounded preparation is a legitimate stage, not friction

### comparison result

- strongest reading here:
  `defensive logic`
- secondary reading:
  `comparison frame`
- not justified:
  `direct evidence`

Reason:

- the source explains why stage separation and quality gates are healthy
- but it does not directly prove our specific `allowed_to_prepare` / `allowed_to_execute` split from inside our own system

### local verdict

```text
Codex prepare scene에서는 direct evidence보다 defensive logic이 강하다.
```

## 7. comparison scene 2: external ingest case

Reference scene:

- `formation_movement_interface_external_reference_ingest_validation_case_v0.md`

### what the internal scene says

- external material should enter as `unclassified` seed
- role is clarified later by VectorFL
- promotion stays blocked
- comparison-frame use may be legitimate before any stronger claim

### what the external source adds

- the source models a mature external artifact that packages roles, stages, and checks instead of free-form agent freedom
- this gives a useful comparison surface for asking:
  “when does structured external material clarify internal scenes, and when is it still just governance rhetoric?”

### comparison result

- strongest reading here:
  `comparison frame`
- secondary reading:
  `defensive logic`
- not justified:
  `direct evidence`

Reason:

- the source is itself an external packaged workflow
- this makes it especially useful as a comparative ingest frame
- but it still does not directly confirm the internal body of B or C

### local verdict

```text
external ingest scene에서는 comparison frame으로서의 힘이 가장 강하다.
```

## 8. comparison scene 3: validation gate / review grammar

Reference scene:

- package sections on validation return and movement qualification
- Codex case and external-ingest case return logic

### what the internal scene says

- results are not final by default
- validation return feeds the next formation loop
- quality and meaning are reread before promotion

### what the external source adds

- “tests are proof”
- “review before merge”
- structured verify/review phases
- anti-shortcut workflow discipline

### comparison result

- strongest reading here:
  `defensive logic`
- secondary reading:
  `comparison frame`
- not justified:
  `direct evidence`

Reason:

- the external source strongly reinforces why proof/review gates matter
- but our `validation_return` is not simply a software QA step; it is part of a broader formation-return loop
- therefore the source supports the need for gates, but does not fully cover the ontology of return

### local verdict

```text
validation gate 장면에서는 defensive logic이 강하지만, validation_return 전체를 직접 설명하지는 못한다.
```

## 9. aggregate split: direct evidence vs defensive logic vs comparison frame

### direct evidence

Current aggregate verdict:

`not supported`

Why:

- no internal repeated explanatory / relocation force has yet been shown
- the source remains external and generic enough that it cannot directly lock A/B/C claims

### defensive logic

Current aggregate verdict:

`strong`

Why:

- the source repeatedly argues for stage discipline, bounded roles, and proof/review gates
- this strongly supports why structures like A/B/C might be needed
- it is especially strong against premature freedom, premature execution, and unverified completion

### comparison frame

Current aggregate verdict:

`strong`

Why:

- the source is useful for rereading internal scenes involving prepare/execute separation, external ingest handling, and validation gate grammar
- it offers a practical comparison lens without needing immediate doctrinal import

## 10. A/B/C reread against the source

### A

Strong contact:

- `/spec`, `/plan`, stage ordering, “spec before code”

Interpretation:

- the source strongly supports precedence logic
- it reinforces that not everything should be opened at once

Current role:

`A-supportive defensive logic`

### B

Strong contact:

- role-sensitive skills
- interface design
- explicit workflow segmentation

Interpretation:

- the source supports role/boundary thinking
- but it does not by itself prove our more specific boundary-surface ontology

Current role:

`B-adjacent comparison frame + defensive logic`

### C

Strong contact:

- test/review/proof/quality gate language

Interpretation:

- the source strongly resonates with verification grammar
- but our package treats validation return as more than code QA

Current role:

`C-supportive defensive logic`

## 11. what this source is good for

- comparing whether an internal scene is opening too early
- comparing whether a Codex handoff is skipping bounded preparation
- comparing whether a result is being over-treated as complete without proof/gate structure
- comparing whether role/boundary thinking is being preserved or dissolved

## 12. what this source is not good for

- locking B as proved
- importing an external workflow as package doctrine
- replacing validation_return with generic test/review semantics
- proving the internal ontology of T/X/R/L

## 13. bounded next move

Healthy next move:

```text
keep as strong defensive_logic + comparison_frame candidate
use only in bounded compare contexts
do not upgrade to direct evidence yet
```

If reused later:

- compare against one ambiguous Codex-prepare case
- compare against one external-ingest reread case
- compare against one validation-return interpretation case

Expected safe output shape:

- scene-by-scene comparison
- where the source helps
- where the source overreaches
- unresolved boundary

## 14. short / full validation return judgment

Short validation return is enough for this note:

```yaml
observed_result: agent-skills behaves as strong defensive logic and strong comparison frame, but not as direct evidence
reread_trigger: internal repeated explanatory force is still missing
next_recommended_state: keep as bounded comparison source only
```

Full validation return becomes necessary if:

- the source starts changing B/A/C trust scope
- the source is proposed as package wording or doctrine
- bounded compare results begin shifting internal hierarchy claims
- someone tries to import the external lifecycle directly into the package

## 15. verdict

`PASS_WITH_NOTE`

Reason:

- the source is richer than a weak generic external reference
- but its productive use is still bounded reread, not promotion
- it is most valuable when used to compare internal preparation / ingest / validation scenes

## 16. intentionally not changed

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- `docs/reports/formation_movement_interface_codex_oneshot_validation_case_v0.md`
- `docs/reports/formation_movement_interface_external_reference_ingest_validation_case_v0.md`
- any package status, Core 7, or object family
- no baseline lock
- no schema enforcement
- no implementation
- no runtime manifest
- no validator/script

## 17. unresolved questions

- does a later scene-by-scene compare make this source stronger on A than on B/C?
- if reused repeatedly, does it stay comparison-frame-first or begin to justify `framing_candidate` status?
- where exactly does its software-QA review logic stop helping and start flattening our broader validation-return loop?
