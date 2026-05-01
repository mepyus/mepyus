# Space Translation Language Base v0

## 1. status

```yaml
index_status: translation_language_base_candidate
purpose: extract reusable space-language data for later human/tool translation
baseline_lock: false
schema_enforcement: false
implementation: false
runtime_manifest: false
validator_or_script: false
final_glossary: false
```

## 2. why this exists

External tools can translate the space language, but translation becomes safer if the source base is the space's own language rather than a generic external wording layer.

This document extracts:

- repeated internal terms
- preserved meanings
- user-facing bridge phrases
- route/state words
- lens words
- flattening risks
- do-not-reduce boundaries

This is not a final glossary.

It is a translation base.

## 3. source documents

Primary sources:

- `docs/reports/integrated_engine_translation_bridge_lexicon_v1_candidate.md`
- `docs/reports/integrated_engine_common_language_extraction_round2_synthesis_v1.md`
- `docs/reports/integrated_engine_internal_language_grammar_candidate_v0.md`
- `docs/reports/integrated_engine_language_amplification_harvest_v0.md`
- `docs/reports/integrated_engine_common_language_stable_additions_round3_v1.md`
- `docs/reports/formation_movement_interface_usage_manual_v0.md`
- `docs/indexes/space_boundary_material_flow_map_v0.md`

Supporting current context:

- `docs/indexes/external_material_microspace_index_v0.md`
- `docs/reports/space_boundary_live_use_stabilization_closeout_v0.md`
- `docs/reports/external_material_microspace_feature_candidate_survey_v0.md`

## 4. translation stance

Translation should not start from:

```text
How do we make this easy?
```

It should start from:

```text
What meaning, route, authority, boundary, or maturation value must survive simplification?
```

Default rule:

```text
Preserve movement first. Simplify wording second.
```

## 5. core space metaphors

| Space language | Preserved meaning | Safe user-facing bridge | Flattening risk |
| --- | --- | --- | --- |
| `공간` | A formation field where traces, provisional objects, lines, residues, and reread paths remain available. | 생각 저장소가 아니라, 재료가 다시 읽히고 연결되는 작업장. | "메모장", "지식 저장소", "그냥 문서 폴더" |
| `형성층` | Space + VectorFL formation layer that rereads material and shapes provisional objects. | 바로 실행 전, 재료를 읽고 위치를 잡는 층. | "분석 단계", "기획 단계" |
| `운동층` | Engine/Codex/worker execution and return layer. | 제한된 작업을 실제로 움직이는 층. | "실행기", "자동화" |
| `공간-경계 연결 카메라` | Operating unit that reads boundary material through user intent and space context before movement. | 외부에서 들어온 재료를 어디에 둘지 보는 판독 장치. | "입력 파이프라인", "수집기" |
| `외부자료공간` | Microspace where external materials are made findable, mergeable, and reusable without promotion. | 외부 자료가 나중에 다시 떠오르게 보관되는 작은 reread 공간. | "링크 모음", "레퍼런스 폴더" |

## 6. three-surface language

| Internal term | Preserved meaning | Bridge wording | Do not reduce to |
| --- | --- | --- | --- |
| `사용자면` | Surface that opens purpose, scope, priority, and decision. | 지금 무엇을 위해 움직일지 여는 표면. | 단순 UI, 입력창, 승인 버튼 |
| `VectorFL면` | Line-first formation/mediation/validation surface. | 요청이 실행되기 전 line, relation, gap, pending, reflux를 읽는 중간 표면. | workflow hub, team board, engine executor |
| `엔진면` | Processing/execution/return-draft surface. | 모양 잡힌 입력을 처리하고 return material을 만드는 표면. | 판단 권한, 최종 완료자 |
| `Codex interpreter/output mode` | Default Codex role: read, interpret, output, and return to space without worker elevation. | Codex가 먼저 해석자/출력자로 읽고 돌려주는 상태. | no Codex, executor, auditor |
| `bounded worker-role elevation` | Codex/worker is elevated only for bounded comparer, packet preparer, executor, or return summarizer. | 조건이 붙을 때만 제한된 역할로 올리는 것. | 자동 실행, 전권 위임 |

## 7. route and movement language

| Internal term | Preserved meaning | Bridge wording | Flattening risk |
| --- | --- | --- | --- |
| `request -> return -> reflux` | Strong route triad from shaped request to processing output to maturation preservation. | 요청이 처리되고, 결과가 돌아오고, 아직 익을 재료는 다시 공간으로 흐른다. | task flow, workflow history |
| `return validation` | VectorFL-side validation of engine output before user decision, reflux, or reprocess. | 결과를 final로 보지 않고 다음 이동을 판정하는 회수 지점. | QA, 결과 확인 |
| `reflux` | Active route that sends maturation-worthy material back toward space with a reason. | 아직 가치가 있어서 공간으로 되돌리는 흐름. | archive, rollback, leftover |
| `validation_return` | Returned result as next formation-loop input, not final result. | 결과가 아니라 다음 판독 재료로 돌아온 것. | final result, 완료 보고 |
| `reprocess` | Structured correction route when validation or anchor drift requires another pass. | 검증 후 다시 처리해야 하는 방향 전환. | 실패 후 재시도 |
| `closeout` | Current round state is summarized and closed back into operating mode. | 이번 작업을 다음에 읽을 수 있게 닫는 기록. | 완전 종료, 영구 잠금 |

## 8. state and gate language

| Internal term | Preserved meaning | Bridge wording | Do not reduce to |
| --- | --- | --- | --- |
| `unclassified seed` | Initial material before object_type is assigned. | 아직 무엇인지 확정하지 않고 안전하게 잡아둔 씨앗. | 미분류 쓰레기, 부족한 입력 |
| `reread_priority` | Material should stay in formation-side reread before movement. | 더 읽어야 해서 바로 움직이지 않는 상태. | 보류만, 나중에 함 |
| `framing_candidate` | Candidate useful as a frame or comparison, not yet evidence. | 비교 프레임으로 쓸 수 있는 후보. | 증거, 확정 원리 |
| `bounded_action_candidate` | Limited action can be prepared, not executed. | 제한된 작업으로 준비할 수 있는 상태. | 실행 준비 완료 |
| `guarded_execution` | Execution allowed only with constraints, fallback, trust scope, and return conditions. | 제약을 붙인 뒤에만 실행 가능한 상태. | 실행 허가 전반 |
| `hold` | Active boundary preserving material outside current core/package. | 지금은 움직이지 않지만 읽을 가치가 있어 붙잡아 둠. | 버림, backlog |
| `carry-forward` | Future-readable preservation without current authority. | 지금 권한은 없지만 다음에 다시 읽을 재료로 가져감. | approved later, roadmap |
| `not promoted` | Promotion gate has not opened; material can still remain readable. | 승격되지 않았지만 사라진 것은 아님. | rejected, forgotten |
| `watch keep` | Keep observing without patch/build mode. | 더 보되 아직 고치거나 만들지는 않음. | TODO, bug watch |
| `reject / conflict` | Current-baseline conflict, not universal badness. | 현재 기준에서는 충돌함. | 나쁜 아이디어, 실패 |
| `PASS_WITH_NOTE` | Usable with explicit thinness, watch, or guardrail. | 통과지만 조건과 주의가 남아 있음. | PASS, 확정 |

## 9. lens language

| Lens | Space question | Bridge wording |
| --- | --- | --- |
| `technical lens` | What structure or mechanism does the material show? | 기술적으로 어떤 구조를 보여주는가? |
| `maker-intent lens` | What pain or bottleneck caused this material to exist? | 만든 사람은 어떤 병목을 풀려고 했는가? |
| `user-intent lens` | Why did the user bring this in now? | 사용자는 왜 지금 이걸 가져왔는가? |
| `line/axis lens` | Which existing lines or axes does it touch? | 기존 공간의 어떤 선/축과 닿는가? |
| `feature-direction lens` | What possible feature, purpose, or direction does this imply? | 어떤 기능/목적/방향 후보를 암시하는가? |
| `risk lens` | What would be over-promoted, over-executed, or over-imported? | 무엇을 너무 빨리 승격/실행/수입하면 위험한가? |
| `residue lens` | How should this remain available for future re-emergence? | 나중에 다시 떠오르려면 어떤 흔적으로 남겨야 하는가? |
| `narrative-mechanism-operational path lens` | Is this claim narrative, mechanism, or operationally verified path? | 이 주장은 서사인가, 구현인가, 실제 운영 경로인가? |

## 10. line / axis / maturity language

| Internal phrase | Preserved meaning | Bridge wording | Guardrail |
| --- | --- | --- | --- |
| `line-first surface` | VectorFL reads line/relation/gap before workflow routing. | 먼저 선과 관계를 읽는 표면. | not team board |
| `line` | Reading lens or repeated connection, not necessarily operating anchor. | 여러 재료에서 반복되는 읽기 선. | do not promote every line |
| `axis` | Stronger organizing direction that survives multiple readings. | 여러 장면을 묶는 더 강한 방향축. | do not infer from one case |
| `LineHealth` | Surface language for line thickness. | 선이 얼마나 두껍게 보이는지의 화면 언어. | not maturity |
| `current_stage` | Flow/time position. | 지금 흐름상 어디쯤인가. | not maturity |
| `maturity` | Ripeness / qualification judgment. | 얼마나 익었는가. | not stage |
| `residue` | Material kept for future reread and line growth. | 나중에 다시 읽을 수 있게 남긴 흔적. | not waste |

## 11. user-facing card language

Default card:

```text
현재 판정:
이유:
다음 이동:
금지선:
```

Direction-relevant card:

```text
현재 판정:
이유:
선택 렌즈:
다음 이동:
금지선:
기능/목적/방향 후보:
공간에 남길 버퍼:
```

External material cockpit candidate:

```text
source:
cluster:
selected_lenses:
state:
next_move:
do_not:
re_emergence_trigger:
```

Translation note:

```text
The card is a surface output. It is not the whole sidecar, schema, or final decision record.
```

## 12. transformation language

| Internal term | Preserved meaning | Bridge wording |
| --- | --- | --- |
| `review` | VectorFL attaches directionality, anchors, related objects, validation points, and route judgment before execution. | 실행 전 의미와 방향을 잡는 판독. |
| `organization` | User surface turns signal into shaped request. | 신호를 작업 가능한 요청으로 정리함. |
| `processing` | Engine executes shaped input and creates return material. | 모양 잡힌 입력을 처리해 반환 재료를 만듦. |
| `decision` | User surface opens or closes next operating route. | 다음 작업 경로를 열지 말지 정함. |
| `recheck` | Route remains open for reread after return or drift. | 결과 후 다시 확인할 여지를 남김. |
| `bridge-before-flatten` | Preserve route, authority, state, boundary, and support before simplifying. | 쉽게 말하기 전에 먼저 무엇을 보존해야 하는지 확인함. |

## 13. authority / boundary language

| Internal term | Preserved meaning | Safe translation |
| --- | --- | --- |
| `workspace ownership` | Path, write permission, artifact status, and promotion path are tied together. | 파일 위치는 권한과 상태를 함께 뜻한다. |
| `proposal-only` | Valuable possible input with no direct core authority. | 쓸모는 있지만 아직 본체 권한은 없는 제안 재료. |
| `needs Codex translation` | Material must be converted/classified into baseline-safe form before core use. | Codex가 현재 기준에 맞게 상태를 판정해야 들어올 수 있음. |
| `collision stop condition` | Route stops when continuing would mix authority or drift core. | 계속 가면 경계가 섞이므로 멈추는 조건. |
| `user decision / package opening authority` | User opens or keeps closed the operating route. | 사용자가 다음 작업 경로를 열 권한을 가짐. |
| `anchor drift` | Anchor-fit mismatch can brake closure and trigger reprocess. | 기준점과 어긋나서 진행을 멈추거나 되돌리는 신호. |
| `support reread recovery` | Supported reread can recover intended route without structural change. | 보조 자료를 순서대로 읽으면 의미가 회복되는 상태. |

## 14. external material translation language

| Space phrase | Preserved meaning | Bridge wording |
| --- | --- | --- |
| `재료를 넣는다` | Trigger space-boundary material flow, not just save/summarize. | 자료를 공간의 흐름에 태운다. |
| `external material microspace` | Small reread space for external material re-emergence. | 외부자료가 나중에 다시 떠오르게 하는 작은 공간. |
| `comparison frame` | Useful reread frame, not direct evidence. | 바로 증거가 아니라 비교 렌즈. |
| `direct evidence` | External material directly strengthens repeated internal patterns after reread. | 내부 반복 구조를 직접 보강하는 증거. |
| `defensive logic` | Explains why a principle is needed, without proving the principle's body. | 원리가 필요한 이유를 방어하는 논리. |
| `operational path` | Training/execution/evaluation path supporting capability, beyond narrative/mechanism. | 실제로 돌아가는 경로. |
| `README-as-validation risk` | Narrative or AI summary may look like proof. | 설명이 검증처럼 보이는 위험. |

## 15. do-not-reduce list

These reductions damage the space language:

- `hold` → backlog / discard
- `reflux` → archive / rollback
- `validation_return` → final result
- `PASS_WITH_NOTE` → pass / done
- `proposal-only` → draft / pending approval
- `workspace ownership` → folder owner
- `return validation` → QA
- `Codex interpreter/output mode` → no Codex
- `bounded_action_candidate` → execution-ready
- `external material microspace` → link collection
- `line` → final doctrine
- `axis` → one-case theme
- `residue` → leftover
- `watch keep` → TODO

## 16. extraction verdict

```yaml
verdict: PASS_WITH_NOTE
best_use: source language base for external tool translation and Codex bridge wording
not_ready_for:
  - final glossary
  - UI copy replacement
  - schema
  - automation
  - baseline lock
strongest_current_base:
  - route/state language
  - hold/reflux/validation_return distinction
  - surface role language
  - lens language
  - user-facing card language
main_risk:
  - easy translations flatten authority, route, and maturation boundaries
next_allowed_move:
  - run one translation trial using this base on a real external-material card
```

## 17. unresolved questions

- Which terms should remain bilingual because English internal labels carry operational precision?
- Should the user-facing bridge prefer Korean terms or mixed Korean/English for `reread`, `reflux`, `validation_return`, and `framing_candidate`?
- How much of this base should an external tool receive at once without becoming confused by internal density?
- Should future external tool packets include only a small subset by source type, such as external material, Codex handoff, or user-surface explanation?

