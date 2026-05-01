# Formation-Movement Interface Weak-Signal Case Library Seed v0

## 1. status

```yaml
status: case_library_seed
recreated_after_source_gap_audit: true
package_candidate_support: true
verdict: PASS_WITH_SOURCE_NOTE-aware
baseline_lock: no
schema_enforcement: no
implementation: no
core7_expansion: no
object_family_expansion: no
```

Status note:

- This document recreates the missing seed library after the source-gap audit.
- This document is not a baseline.
- This document is not a rule set.
- This document is a seed layer for accumulating weak-signal threshold examples.
- This document reflects the source-gap judgment recorded in `docs/reports/formation_movement_interface_weak_signal_source_gap_audit_v0.md`.

## 2. source lineage

Primary source inputs:

- `docs/reports/formation_movement_interface_weak_signal_stress_test_v0.md`
- `docs/reports/formation_movement_interface_weak_signal_examples_round1_v0.md`
- `docs/reports/formation_movement_interface_weak_signal_source_gap_audit_v0.md`
- `docs/reports/formation_movement_interface_package_draft_v0.md`
- current conversation summary / supervisor relay context

Source note:

- `examples_round1` was produced without direct seed-library reference and therefore remained provisional source-gap output.
- This document exists to repair that lineage gap.
- `examples_round1` is not discarded; it is absorbed here as provisional seed material.

## 3. why this library exists

- The weak-signal stress test showed that the package structure itself held under weak or ambiguous input.
- The remaining weakness is not missing structure; it is threshold/example scarcity.
- `examples_round1` is valid example material, but its source lineage was incomplete.
- Therefore this document serves as a seed anchor for repeated weak-signal threshold examples.

## 4. case families

### A. acceptable simplification vs R loss

Purpose:

Distinguish between user-surface explanations that remain acceptably simplified and explanations that flatten away too much structural residue.

Key risk:

- user readability can be mistaken for good explanation even when intermediate layer and reread trace disappear

Judgment questions:

- Does at least one of intermediate layer, reread, provisionality, or residue survive?
- Has the explanation flattened into “just a thought-organizing tool” or “just an AI automation tool”?
- Is there risk of reuse as final definition?
- Is short validation return enough, or is full validation return needed?

Healthy branch candidates:

- `refine`
- `hold`
- `no promotion`

What not to do:

- Do not treat easy readability as sufficient proof of acceptable simplification.
- Do not reuse draft wording as baseline or slogan too early.

### B. direct evidence vs defensive logic vs comparison frame

Purpose:

Distinguish the role of external references, especially B-adjacent references, without premature evidence promotion.

Direct evidence:

- directly reinforces repeated internal explanatory / relocation force
- requires internal reread

Defensive logic:

- explains why a principle may be needed
- does not itself prove that principle as body

Comparison frame:

- helps reread internal scenes
- supports comparison without becoming evidence by itself

Reread_priority retention conditions:

- role is still unclear
- external text looks relevant but has not yet shown internal explanatory force
- overlap with multiple candidates remains unresolved

Judgment questions:

- Does the reference directly reinforce repeated internal structure?
- Is it merely defending why a principle may be needed?
- Is it only useful as a comparison lens?
- Does the reference by itself tempt false evidence reading?

What not to do:

- Do not promote external references into evidence without internal reread.
- Do not over-promote defensive logic into axis evidence.

### C. ambiguous prepare HOLD cases

Purpose:

Identify when a Codex/worker request is too underspecified even for `prepare_worker_packet`.

Boundary-lack types:

- no action scope
- unclear task object

Expected-return-lack types:

- no result shape
- no criteria for acceptable return

Guardrail-lack types:

- no no-go boundary
- no refusal boundary

Reread-return-hook-lack types:

- no return path
- no validation or reread expectation

Allowed_to_prepare HOLD direction:

- if boundary, expected return, or reread return path is missing, HOLD remains valid

Judgment questions:

- Can this request really become a one-shot draft yet?
- What exactly is missing?
- Is more user input needed, or can VectorFL shape a boundary safely?
- Would opening `allowed_to_prepare` already be risky?

What not to do:

- Do not confuse task intent with packet readiness.
- Do not let VectorFL invent too much missing structure without bounded context.

### D. A/C/T/X/R/L overlap hold cases

Purpose:

Preserve overlap-heavy cases without forcing them into a single-axis reading too early.

Overlap risk:

- one case may strongly activate multiple lenses at once
- single-axis framing can absorb neighboring candidates prematurely

Hold/reread retention conditions:

- central lens is unclear
- multiple lenses explain the same material strongly
- explanatory force is not yet separable

Full validation return need conditions:

- overlap begins affecting hierarchy claims
- trust scope or candidate centrality changes
- short return would hide ambiguity

Judgment questions:

- Would single-axis framing absorb other candidates?
- Is the central lens still unclear?
- Is short validation return enough?
- Is full validation return needed?
- Should `next_allowed_move` remain `compare_only` or `reread_against_A_C_T_X_R_L`?

What not to do:

- Do not treat overlap discomfort as proof that one lens must be central.
- Do not resolve hierarchy before repeated reread.

## 5. seed examples from weak-signal stress-test

### Case A. weak B-adjacent external reference

- Example ID: `WSC-SEED-A`
- Family: direct evidence vs defensive logic vs comparison frame
- Situation:
  A generic external statement says good agent systems should have clear roles.
- Why it is weak / ambiguous:
  It touches B but does not directly explain internal structure.
- Initial safe object_type:
  `reread_priority`

User Surface judgment card:

```text
현재 판정: B와 닿아 보이지만 아직 약한 일반론입니다.
이유: 내부 장면 설명력과 재배치력이 아직 없습니다.
다음 이동: reread 대상으로 보관하고 나중에 비교합니다.
금지선: B 증거, 축 확정, operating rule 승격은 금지입니다.
```

VectorFL reading:

- relevant lenses: `B`, `X`
- instability reason: relevance exists, but evidence role is too weak
- promotion barrier: no internal explanatory force shown

- Recommended next_allowed_move:
  `reread_only`
- Short vs full validation return:
  short is enough unless a future comparison tries to elevate it into B evidence
- Healthy branch:
  `hold` / `archive_as_residue`
- What not to do:
  do not classify generic role language as direct B evidence

### Case B. too-smooth user surface explanation

- Example ID: `WSC-SEED-B`
- Family: acceptable simplification vs R loss
- Situation:
  "통합엔진은 네 생각을 정리하고 AI 작업을 도와주는 시스템이야."
- Why it is weak / ambiguous:
  Readable but overly flattening.
- Initial safe object_type:
  `bounded_action_candidate`

User Surface judgment card:

```text
현재 판정: 이해는 쉽지만 그대로 쓰기엔 너무 납작합니다.
이유: 중간 구조와 reread의 결이 거의 사라졌습니다.
다음 이동: 더 균형 잡힌 draft와 비교해 refine합니다.
금지선: final definition이나 baseline wording으로 쓰지 않습니다.
```

VectorFL reading:

- relevant lenses: `R`, `L`, `X`
- instability reason: high flattening risk
- promotion barrier: cannot be reused as canonical wording

- Recommended next_allowed_move:
  `refine`
- Short vs full validation return:
  short is enough for draft review; full is needed if reuse risk rises
- Healthy branch:
  `refine`
- What not to do:
  do not accept readability alone as success

### Case C. ambiguous Codex request without boundary

- Example ID: `WSC-SEED-C`
- Family: ambiguous prepare HOLD cases
- Situation:
  "이거 Codex에게 시켜서 정리해줘."
- Why it is weak / ambiguous:
  intent exists, but boundary and return shape are missing
- Initial safe object_type:
  `reread_priority`

User Surface judgment card:

```text
현재 판정: 아직 Codex 준비 단계로 올리기 이릅니다.
이유: 범위, 반환 형식, guardrail이 비어 있습니다.
다음 이동: 무엇을 어디까지 정리할지 다시 잡습니다.
금지선: 지금 packet 준비나 실행으로 넘기지 않습니다.
```

VectorFL reading:

- relevant lenses: `B`, `X`
- instability reason: underspecified request
- promotion barrier: no boundary / expected return / reread hook

- Recommended next_allowed_move:
  `reread_only`
- Short vs full validation return:
  short is enough unless someone forces packetization
- Healthy branch:
  `hold`
- What not to do:
  do not open `prepare_worker_packet` from vague intent alone

### Case D. A/C/T/X/R/L overlap case

- Example ID: `WSC-SEED-D`
- Family: A/C/T/X/R/L overlap hold cases
- Situation:
  "이건 먼저 구조를 세워야 하는데 아직 익지 않았고, 지금 설명하면 다 뭉개질 것 같으니 당장은 보류하자."
- Why it is weak / ambiguous:
  strong overlap across A/C/T/X/R
- Initial safe object_type:
  `reread_priority`

User Surface judgment card:

```text
현재 판정: 아직 하나의 원리로 묶기보다 보류가 안전합니다.
이유: 구조, 미성숙, 번역, 손실 위험이 동시에 강합니다.
다음 이동: A/C/T/X/R 쪽을 나눠 reread하고 중심을 다시 봅니다.
금지선: 지금 한 축으로 잠그거나 승격하지 않습니다.
```

VectorFL reading:

- relevant lenses: `A`, `C`, `T`, `X`, `R`
- instability reason: no clear central lens yet
- promotion barrier: any single-axis framing would absorb others too early

- Recommended next_allowed_move:
  `reread_against_A_C_T_X_R`
- Short vs full validation return:
  full becomes more likely if hierarchy claims begin to move
- Healthy branch:
  `hold`
- What not to do:
  do not reduce overlap into a single clean candidate too early

## 6. examples_round1 as provisional material

The following entries from `docs/reports/formation_movement_interface_weak_signal_examples_round1_v0.md` are accepted here as provisional seed material:

- `WS-R1-01`: understandable but too-thin user-surface explanation
- `WS-R1-02`: governance/checkpoint external reference
- `WS-R1-03`: boundary-less Codex bundling request
- `WS-R1-04`: overlap note with A/C/T/X/R

Status applied to all four:

```yaml
source_status: provisional_source_gap_material
reuse_status: usable_as_example_material
rule_status: not_rule
patch_status: not_patch_yet
```

## 7. current threshold notes

- acceptable simplification vs R loss still lacks sharp threshold
- generic B-adjacent language is not evidence by default
- a boundary-less Codex request may justify HOLD even before `allowed_to_prepare`
- strong overlap may be healthier as hold/reread than as framing
- full validation return becomes necessary under promotion risk, baseline risk, trust-scope change, object-type change, or R loss
- `examples_round1` had a source gap and should be re-linked through this recreated seed library before more accumulation continues

## 8. do-not-change guardrails

- This library does not expand Core 7.
- This library does not add object families.
- This library does not create weak-signal-specific state names.
- Examples are not rules.
- Examples are evidence material for future clarification.
- Repeated `PASS_WITH_NOTE` does not auto-trigger a patch.
- Patch work should happen only after repeated evidence accumulates in a separate bounded action.
- `examples_round1` is not discarded.
- The earlier source gap is not hidden.
- Recreating this seed library is not baseline lock.

## 9. relationship to examples_round1

- `examples_round1` was not a clean continuation because the seed library was missing.
- Its content remains aligned with the stress-test and package draft, so it is not discarded.
- This recreated seed library accepts `examples_round1` as provisional material.
- Future weak-example accumulation should use this recreated seed library as the source anchor.

## 10. recommended next move

- now that the seed library has been recreated, `examples_round1` can later receive a relink note or reassessment in a separate bounded action
- after that, collect 3-5 more weak examples
- only after repeated patterns accumulate should clarification patch candidates be drafted
- for now, prioritize restored lineage plus example accumulation over package expansion
