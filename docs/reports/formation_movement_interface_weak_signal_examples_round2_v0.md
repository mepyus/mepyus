# Formation-Movement Interface Weak-Signal Examples Round 2 v0

## 1. status

```yaml
status: case_example_report
verdict: PASS_WITH_NOTE
purpose: collect additional weak-signal examples as threshold material using the recreated seed library as source anchor
baseline_lock: no
schema_enforcement: no
implementation: no
runtime_manifest: no
validator_or_script: no
core7_expansion: no
object_family_expansion: no
weak_signal_state_expansion: no
```

## 2. source note

This report is anchored to:

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- `docs/reports/formation_movement_interface_weak_signal_case_library_seed_v0.md`
- `docs/reports/formation_movement_interface_weak_signal_examples_round1_v0.md`
- `docs/reports/formation_movement_interface_weak_signal_source_gap_audit_v0.md`

This document does not add rules. It accumulates example material for later threshold comparison only.

## 3. included families

- acceptable simplification vs R loss
- direct evidence vs defensive logic vs comparison frame
- ambiguous prepare HOLD cases
- A/C/T/X/R/L overlap hold cases

## 4. examples

### Example ID: WS-R2-01

- Family: acceptable simplification vs R loss
- Situation:
  A user asks, "통합엔진이 뭐야?" and the explanation draft is:
  "통합엔진은 네가 모아둔 내용을 지금 필요한 작업으로 꺼내서 AI가 처리하게 연결해주는 도구야."
- Why it is weak / ambiguous:
  It is clearer than an internal-language answer, but it still risks flattening formation into simple tool orchestration.
- Initial safe object_type:
  `bounded_action_candidate`

User Surface judgment card:

```text
현재 판정: 설명은 비교적 usable하지만 그대로 고정하긴 이릅니다.
이유: 현재 작업 연결은 남아 있지만 reread와 잠정성의 결이 약합니다.
다음 이동: 더 얇은 설명과 비교해 acceptable simplification인지 refine합니다.
금지선: final definition, baseline wording, product slogan으로 쓰지 않습니다.
```

VectorFL reading:

- relevant lenses: `L`, `R`, `X`
- instability reason: user-fit is decent, but formation residue is only partially preserved
- promotion barrier: wording may be reused as canonical engine definition before residue-preserving comparison

- Recommended next_allowed_move:
  `refine`
- Short vs full validation return:
  short is enough for draft comparison; full is needed if this wording starts functioning as canonical explanation
- Healthy branch:
  `refine`
- What not to do:
  do not treat partial readability as proof that R-loss is solved; do not promote this into stable package wording
- Relation to existing seed/example:
  touches `WSC-SEED-B` and `WS-R1-01`, but is slightly less flattened than both

### Example ID: WS-R2-02

- Family: direct evidence vs defensive logic vs comparison frame
- Situation:
  An external reference says:
  "Without clear role boundaries and checkpoint reviews, multi-agent systems become noisy and unreliable."
- Why it is weak / ambiguous:
  It touches B and C strongly, but it still reads more like a risk-defense argument than direct internal evidence.
- Initial safe object_type:
  `reread_priority`

User Surface judgment card:

```text
현재 판정: 관련성은 있지만 아직 직접 증거로 읽기 어렵습니다.
이유: 역할 경계와 검토 필요성을 말하지만, 내부 장면의 설명력은 아직 확인되지 않았습니다.
다음 이동: defensive logic인지 comparison frame인지 먼저 가릅니다.
금지선: B나 C의 direct evidence, operating rule로 승격하지 않습니다.
```

VectorFL reading:

- relevant lenses: `B`, `C`, `T`
- instability reason: statement defends disciplined structure, but does not yet reinforce repeated internal relocation force
- promotion barrier: external text alone cannot decide whether it is body evidence or only supporting governance logic

- Recommended next_allowed_move:
  `reread_only`
- Short vs full validation return:
  short is enough while role classification remains local; full is needed if internal reread begins shifting B/C trust scope
- Healthy branch:
  `hold`
- What not to do:
  do not over-read governance language as proof that B is locked; do not skip internal comparison scenes
- Relation to existing seed/example:
  touches `WSC-SEED-A` and `WS-R1-02`, but is a slightly stronger defensive-logic candidate

### Example ID: WS-R2-03

- Family: ambiguous prepare HOLD cases
- Situation:
  A user says:
  "이거 Codex에게 맡겨서 보기 좋게 정리해줘. 너무 길지만 않게."
- Why it is weak / ambiguous:
  There is intent and a style preference, but no stable boundary, expected return form, guardrail, or reread return hook.
- Initial safe object_type:
  `reread_priority`

User Surface judgment card:

```text
현재 판정: 아직 prepare 단계로 올리기 어렵습니다.
이유: 무엇을 얼마나 줄일지, 어떤 출력 형태가 필요한지, 넘기면 안 되는 범위가 비어 있습니다.
다음 이동: 범위와 기대 반환 형식을 먼저 붙입니다.
금지선: 지금 packet 준비나 execution으로 넘기지 않습니다.
```

VectorFL reading:

- relevant lenses: `B`, `X`, `L`
- instability reason: intent exists, but packet-shaping structure is too underspecified
- promotion barrier: missing boundary, expected_return_form, guardrail, and reread_return_hook make even allowed_to_prepare unsafe

- Recommended next_allowed_move:
  `reread_only`
- Short vs full validation return:
  short is enough because this is still a stop/clarification judgment; full is needed only if someone attempts packetization anyway
- Healthy branch:
  `hold`
- What not to do:
  do not infer a worker packet from tone preference alone; do not treat "보기 좋게" as an expected return contract
- Relation to existing seed/example:
  touches `WSC-SEED-C` and `WS-R1-03`, but adds ambiguity around formatting preference masquerading as boundary

### Example ID: WS-R2-04

- Family: A/C/T/X/R/L overlap hold cases
- Situation:
  An internal note says:
  "이건 원리를 먼저 세워야 하는 것 같긴 한데 아직 익지 않았고, 지금 사용자 설명으로 내리면 이상하게 번역될 것 같아서 검증 전에는 남겨두는 편이 낫다."
- Why it is weak / ambiguous:
  A, C, T, X, L, and R all contribute at once, and the sentence itself is mostly about why reduction is unsafe.
- Initial safe object_type:
  `reread_priority`

User Surface judgment card:

```text
현재 판정: 지금은 정리보다 보류가 더 안전합니다.
이유: 선행 구조, 미성숙, 번역 실패, 설명 손실 위험이 동시에 강합니다.
다음 이동: A/C/T/X/R/L로 나눠 reread하고 중심 렌즈를 다시 봅니다.
금지선: 하나의 축으로 정리하거나 승격하지 않습니다.
```

VectorFL reading:

- relevant lenses: `A`, `C`, `T`, `X`, `R`, `L`
- instability reason: central explanatory lens remains unresolved and user-surface translation risk is part of the overlap itself
- promotion barrier: any single-axis reading would collapse important ambiguity and may distort hierarchy claims

- Recommended next_allowed_move:
  `reread_against_A_C_T_X_R_L`
- Short vs full validation return:
  full is more likely needed than in ordinary overlap notes, because translation risk and hierarchy ambiguity are both active
- Healthy branch:
  `hold`
- What not to do:
  do not reduce this to A-only discipline or T-only ripeness; do not treat the note as evidence that one lens has already won
- Relation to existing seed/example:
  touches `WSC-SEED-D` and `WS-R1-04`, but adds stronger L/X pressure on user-surface translation

## 5. cross-example checks

### user burden

- In all four examples, user-provided input remains at roughly 3 fields:
  - current purpose
  - source trace
  - initial boundary or why-now
- The user does not choose `object_type`.
- Core 7 is not required at creation time.

### anti-promotion

- no external reference becomes evidence
- no explanation becomes final definition
- no Codex request becomes packet-ready execution
- no overlap note becomes axis lock

### non-promotion branches

- `refine` appears as the healthy branch for partial but risky explanation drafts
- `hold` remains healthy for weak external references, ambiguous prepare cases, and overlap-heavy notes
- `archive_as_residue` remains available for weak reference material if later reread force stays low

### short / full validation

- short is enough:
  - `WS-R2-01` at draft-comparison level
  - `WS-R2-02` before trust-scope movement
  - `WS-R2-03` while the request is still blocked at clarification
- full becomes more likely:
  - `WS-R2-04`, because overlap and translation risk together may affect hierarchy judgment
  - `WS-R2-01` if wording starts circulating as canonical explanation
  - `WS-R2-02` if B/C trust scope changes during internal reread

## 6. overall verdict

`PASS_WITH_NOTE`

Reason:

- The seed-library families remain usable as source anchors for additional weak examples.
- The package still handles weak signals without forcing premature execution, promotion, or rule creation.
- The main remaining issue is not structural failure; it is threshold sharpness.

## 7. added examples summary

- added example count: `4`
- included families:
  - acceptable simplification vs R loss
  - direct evidence vs defensive logic vs comparison frame
  - ambiguous prepare HOLD cases
  - A/C/T/X/R/L overlap hold cases

One-line summary:

- `WS-R2-01`: usable but still residue-thin engine explanation draft should stay in `refine`
- `WS-R2-02`: stronger governance language still reads as defensive logic candidate, not evidence
- `WS-R2-03`: tone/style preference does not supply enough structure for `allowed_to_prepare`
- `WS-R2-04`: overlap note with explicit translation risk should stay in `hold` and lean toward full return

## 8. threshold movement

### clearer after round 2

- acceptable simplification can preserve some movement sense and still remain too weak for stable wording
- governance / discipline language remains defensive-logic-heavy unless internal repeated explanatory force is shown
- style preference does not count as boundary or expected return form in ambiguous Codex requests
- overlap plus user-surface translation risk raises the chance that full validation return is needed

### still ambiguous

- how much residue is enough for an explanation to cross from refine into acceptable simplification
- when repeated governance language becomes comparison frame rather than mere defensive logic
- how much boundary shaping VectorFL may safely infer before `allowed_to_prepare` should open
- whether overlap with strong L/X pressure should default to full return sooner than other overlap cases

### should not be patched yet

- Core 7 expansion
- object family expansion
- weak-signal-specific state names
- new structural fields for prepare/execute

### may become patch candidate after more examples

- acceptable simplification vs R-loss comparison note
- defensive logic vs comparison frame threshold note
- ambiguous prepare HOLD threshold note
- overlap-to-full-return threshold note

## 9. pattern repetition check

Patterns repeated across round 1 and round 2:

- readability alone keeps failing as a sufficient standard for user-surface quality
- generic governance language keeps landing in reread/hold rather than evidence
- vague Codex requests keep failing before `allowed_to_prepare`
- overlap-heavy notes keep preferring hold/reread over clean framing

Interpretation:

- repetition is now visible, but still at threshold-material level
- repetition alone is not yet enough to justify a package patch

## 10. recommended future patch 여부

`not_yet`

Reason:

- repeated patterns exist, but examples still clarify thresholds more than they justify structural edits

## 11. intentionally not changed

- `docs/reports/formation_movement_interface_package_draft_v0.md`
- `docs/reports/formation_movement_interface_weak_signal_case_library_seed_v0.md`
- `docs/reports/formation_movement_interface_weak_signal_examples_round1_v0.md`
- Core 7
- object family 5종
- baseline lock / schema enforcement / implementation / runtime manifest / validator or script generation

## 12. unresolved questions

- at what point does a residue-thin explanation become acceptable simplification instead of merely less-bad flattening
- when does repeated governance language become comparison frame strong enough to leave `reread_priority`
- how much missing packet structure may VectorFL safely infer without overreaching in ambiguous prepare cases
- should overlap cases with explicit user-surface translation risk default to full validation return earlier than other overlap cases

## 13. next recommended move

`prepare threshold comparison note`

Supporting direction:

- one more small batch of examples may help, but the next useful bounded action is likely a comparison note that contrasts round 1 and round 2 thresholds without patching package structure
