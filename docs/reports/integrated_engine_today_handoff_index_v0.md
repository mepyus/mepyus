# Integrated Engine Today Handoff Index v0

Date: 2026-04-15

## 0. purpose

이 문서는 오늘 만든 integrated-engine 관련 문서들을 다음 채팅에서 빠르게 이어 읽을 수 있도록 목적별로 묶은 handoff index다.

단순 파일 목록이 아니라, 왜 읽어야 하는지와 어디서 시작해야 하는지를 함께 기록한다.

## 1. friction / observation

### `docs/reports/integrated_engine_cross_scenario_translation_friction_audit_v0.md`

S1, S3, 실제 사용에 가까운 handoff에서 internal-to-user translation friction이 어디서 생기는지 관찰한 문서다.

읽는 이유:

- `reflux`, `anchor drift`, `return validation`, `workspace ownership` 같은 항목이 어디서 마찰을 만드는지 확인할 수 있다.

### `docs/reports/integrated_engine_translation_friction_log_v0.md`

friction 후보를 사례 단위로 기록한 log다.

읽는 이유:

- 어떤 마찰이 wording 문제가 아니라 support-dependent meaning, fixture-scope limitation, hold-feature expectation leak인지 구분할 수 있다.

### `docs/reports/integrated_engine_translation_friction_round1_closeout_note_v0.md`

translation friction round 1의 closeout이다.

읽는 이유:

- friction을 patch나 glossary로 바로 올리지 않고 carry-forward bridge material로 둔 이유를 빠르게 확인할 수 있다.

## 2. language amplification / grammar

### `docs/reports/integrated_engine_language_amplification_harvest_v0.md`

저장된 자료에서 내부 언어 재료를 넓게 수집한 문서다.

읽는 이유:

- 오늘 line / connection / axis를 다시 보려면 원재료가 어디에 있는지 확인해야 한다.

### `docs/reports/integrated_engine_internal_language_pattern_inventory_v0.md`

수집된 내부 언어를 route, authority, state transition, support dependency, collaboration handoff pattern으로 묶은 문서다.

읽는 이유:

- 단어보다 반복되는 관계와 연결을 보기 위한 중간 지도다.

### `docs/reports/integrated_engine_internal_language_grammar_candidate_v0.md`

route grammar, authority grammar, hold/watch grammar, validation grammar, reread/support grammar, bridge-before-flatten grammar를 후보 규칙으로 정리한 문서다.

읽는 이유:

- 다음 채팅에서 통합엔진을 현재 처리 규약으로 쓰려면 이 문서가 가장 중요한 문법 기준이다.

### `docs/reports/integrated_engine_human_bridge_seed_list_v0.md`

human bridge를 만들 때 보존해야 할 seed를 정리한 문서다.

읽는 이유:

- 최종 번역어가 아니라, 인간 가독 line을 만들 때 잃으면 안 되는 의미를 확인할 수 있다.

## 3. handoff / explanation trial

### `docs/reports/integrated_engine_real_gemini_handoff_artifact_v0.md`

`gemini/mock_test` 계열 material을 formal handoff artifact처럼 구성한 문서다.

읽는 이유:

- Gemini material이 proposal-only / needs Codex translation 상태로 어떻게 읽혀야 하는지 확인할 수 있다.

### `docs/reports/integrated_engine_real_handoff_grammar_classification_v0.md`

handoff artifact를 6개 internal grammar로 분류한 문서다.

읽는 이유:

- Gemini/Codex/User authority boundary와 carry-forward/reject/hold 구분을 다시 볼 수 있다.

### `docs/reports/integrated_engine_real_handoff_human_explanation_trial_v0.md`

handoff artifact를 사람이 읽기 쉬운 설명층으로 시험한 문서다.

읽는 이유:

- 쉬운 설명이 어디서 route/authority/state/boundary를 납작하게 만드는지 확인할 수 있다.

### `docs/reports/integrated_engine_real_handoff_retention_check_v0.md`

handoff explanation이 6개 grammar를 얼마나 보존했는지 점검한 문서다.

읽는 이유:

- `workspace ownership`, `hold/carry-forward`, `needs Codex translation`이 왜 계속 fragile한지 볼 수 있다.

## 4. bridge lexicon / guide

### `docs/reports/integrated_engine_translation_bridge_lexicon_v1_candidate.md`

internal term을 최종 번역어가 아니라 preservation note / flattening risk / boundary reminder로 정리한 provisional lexicon이다.

읽는 이유:

- 사용자-facing 치환어가 아니라 보존 조건을 확인하기 위한 문서다.

### `docs/reports/integrated_engine_translation_bridge_high_risk_entry_note_v0.md`

high-risk entry 6개를 따로 분석한 문서다.

읽는 이유:

- `workspace ownership`, `hold`, `carry-forward`, `reject / conflict`, `collision stop condition`, `watch keep`이 어떻게 납작해지는지 빠르게 볼 수 있다.

### `docs/reports/integrated_engine_provisional_human_explanation_guide_v0.md`

human explanation의 5-step order를 잠근 guide다.

읽는 이유:

- 설명 순서가 왜 보존 장치인지 확인할 수 있다.

### `docs/reports/integrated_engine_provisional_human_explanation_guide_usage_trial_round2_v0.md`

guide v0를 Gemini/Codex handoff 맥락에 적용한 round 2 trial이다.

읽는 이유:

- handoff 설명에서 guide가 어디까지 버티고 어디서 얇아지는지 볼 수 있다.

### `docs/reports/integrated_engine_provisional_human_explanation_handoff_retention_check_v0.md`

handoff trial에서 fragile/supporting entries를 retention 기준으로 판정한 문서다.

읽는 이유:

- `workspace ownership`, `carry-forward`, `reject / conflict`가 여전히 retained_with_thinness인 이유를 확인할 수 있다.

### `docs/reports/integrated_engine_provisional_human_explanation_guide_usage_trial_round2_closeout_note_v0.md`

guide usage trial round 2의 closeout이다.

읽는 이유:

- guide는 버텼지만, external harvest/final wording으로 가지 않고 S3 또는 방향 재점검이 필요하다는 판단을 볼 수 있다.

## 5. direction reset / current conclusion

### `docs/reports/integrated_engine_direction_reset_note_v0.md`

오늘 드러난 핵심 방향 수정 사항을 잠근 문서다.

읽는 이유:

- 다음 채팅에서 가장 먼저 읽어야 한다. 목적이 engine language 치환이 아니라 내부 공간에서 line / connection / axis를 읽고 사용자 고정 인터페이스를 찾는 것임을 다시 잡아준다.

### `docs/reports/integrated_engine_today_closeout_summary_v0.md`

오늘의 논의를 목적 순서로 요약한 closeout 문서다.

읽는 이유:

- 오늘 만든 friction, grammar, handoff, lexicon, guide 문서들이 최종적으로 어떻게 재해석되었는지 빠르게 볼 수 있다.

### `docs/reports/integrated_engine_today_handoff_index_v0.md`

현재 문서다.

읽는 이유:

- 다음 채팅에서 읽을 순서와 목적을 빠르게 잡는 지도 역할을 한다.

## 6. 다음 채팅에서 먼저 읽을 최소 세트

최소 세트:

1. `docs/reports/integrated_engine_direction_reset_note_v0.md`
   - 오늘 방향 수정의 기준점이다.

2. `docs/reports/integrated_engine_today_closeout_summary_v0.md`
   - 오늘 작업 전체를 목적별로 압축해서 이어준다.

3. `docs/reports/integrated_engine_internal_language_grammar_candidate_v0.md`
   - 통합엔진을 다음 채팅의 처리 규약으로 쓰기 위한 문법 기준이다.

4. `docs/reports/integrated_engine_translation_bridge_lexicon_v1_candidate.md`
   - 최종 번역어가 아니라 보존 조건을 확인하기 위한 bridge 기준이다.

5. `docs/reports/integrated_engine_provisional_human_explanation_guide_usage_trial_round2_closeout_note_v0.md`
   - guide가 어디까지 버텼고 무엇이 아직 fragile한지 확인하는 최근 closeout이다.

## 7. 다음 채팅 시작 문장 후보

다음 채팅은 이렇게 시작하면 된다.

```text
direction reset note와 today closeout summary 기준으로,
internal space에서 line / connection / axis가 어떻게 자라고 있는지 먼저 reread하고,
그 축에서 user surface가 다룰 수 있는 고정 interface 후보를 찾는다.
CLI는 본체가 아니라 필요한 경우 보조 실행기로만 붙인다.
```

## 8. still closed

계속 닫힘:

- final glossary
- UI copy
- wording patch
- external translation rule harvest
- 내부 lexicon 추가 증식
- scaffold 수정
- runtime/views 수정
- manifest shape / read-map 변경
- selected-object behavior
- trace UI
- runtime binding
- extension promotion

## 9. handoff closeout

이 index의 목적은 오늘 만든 문서를 더 늘리는 것이 아니라, 다음 채팅에서 바로 현재 위치를 회복하게 하는 것이다.

다음 시작점은 translation이 아니라 line / connection / axis reread다.
