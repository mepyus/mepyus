# Integrated Engine Exploration Question Set v1.1

Date: 2026-04-14

## purpose

이 질문 세트는 공간 전체를 막연히 요약하기 위한 것이 아니다.

현재 통합엔진 셋업에 필요한 언어와 assistant 해석 안정성에 필요한 입력 문법을 공간에서 목적형으로 채집하기 위한 반복 실행 질문 세트다.

이 문서는 일회성 질문지가 아니라, 공간 숙성과 함께 반복 실행되는 `language harvest protocol`로 사용한다.

## provisional footing

현재는 아래를 임시 발판으로 둔다.

- 사용자면 = 요청/목적과 범위를 세우는 면
- 벡터플면 = 그 요청을 판독/정리/번역하는 면
- 엔진면 = 처리/수행/출력/반환하는 면
- CLI/에이전트 = 본체를 대체하지 않는 선택적 도구층
- 지금은 더 잠그는 단계보다 언어를 적립하는 단계
- 잠금은 출발점이 아니라 반복 운용 뒤의 결과

중요:

- 이 기준은 final schema가 아니라 탐색 발판이다.
- team relay / handoff / external research / CLI calls / automatic routing / standing worker assignment는 현재 본체 골격이 아니라 운영 확장층으로 읽는다.
- 현재 extraction dataset은 language material이지 final schema가 아니다.

## current operating map note

현재 통합엔진 자산 지도 기준:

- User surface = goal / scope / material-context start surface
- VectorFL surface = intermediate-formation reading / translation surface
- Engine surface = ingest / process / validate / trace-memory / return surface

현재 canonical current assets, runtime records, checkpoint reports, lineage assets가 이미 구분되어 있으므로, 이번 질문 세트 실행도 반드시 source priority를 가지고 진행한다.

## source priority

### priority 1. current integrated-engine reading lock / language material

- `docs/reports/vectorfl_integrated_engine_3_surface_cli_handoff_lock_v1.md`
- `docs/reports/integrated_engine_common_language_extraction_v1.md`
- `docs/reports/integrated_engine_vectorfl_surface_elevated_direction_note_v1.md`
- `docs/reports/integrated_engine_exploration_question_set_v1.md`

### priority 2. current integrated-engine code / surfaces

- `app/runtime/vectorfl_integrated_engine_api.py`
- `app/runtime/vectorfl_integrated_engine_shell.py`
- `app/core/runtime/viewer_server.py`
- `runtime/views/vectorfl_dual_surface.tsx`
- `runtime/views/vectorfl_dual_surface_app/README.md`
- `runtime/views/vectorfl_dual_surface_app/src/styles.css`

### priority 3. latest runtime records

- `runtime/manifests/vectorfl_integrated_engine_*_latest_v0.json`

### priority 4. checkpoint / lineage reports

- current checkpoint reports
- paper/proper/operable/page-shell lineage
- paperclip-related readings

Rule:

- priority 1 and 2 must be read first.
- priority 3 is runtime evidence, not a source of permanent truth without freshness checks.
- priority 4 is lineage / reinforcement / contrast material, not the current body lock by itself.

## execution scope

Prioritize:

- recent integrated-engine / three-surface / line / axis / reflux documents
- directive / baseline / spec / report / handoff documents
- documents with repeated expressions
- current React user/VectorFL surface and Python engine surface role boundaries

Avoid:

- shallow log-only reading
- irrelevant implementation details
- treating generated output as canonical source
- treating old latest execution as current truth without freshness gate

## common instruction prefix

이번 탐색은 공간 전체 요약이 아니라, 현재 통합엔진 셋업과 assistant 해석 안정성에 필요한 언어를 적립하기 위한 목적형 탐색이다.
반드시 raw 표현을 먼저 보존하고, 그 표현이 왜 지금 유용한지 설명하고, 사람이 이해할 수 있는 문장으로 다시 써라.
반복적으로 살아남는 표현은 표시하고, 애매한 것은 unresolved로 남겨라.
generated/test surfaces와 canonical surfaces를 혼동하지 마라.
language material은 final schema처럼 승격하지 마라.

## Track A. three-surface language

- Q1. 현재 공간 안에서 사용자면을 설명할 때 반복적으로 살아남는 문장은 무엇인가?
- Q2. 현재 공간 안에서 벡터플면을 설명할 때 반복적으로 살아남는 문장은 무엇인가?
- Q3. 현재 공간 안에서 엔진면을 설명할 때 반복적으로 살아남는 문장은 무엇인가?
- Q4. 세 면의 차이를 분명히 드러내는 문장은 무엇인가?
- Q5. 세 면이 하나의 흐름으로 이어진다는 것을 보여주는 문장은 무엇인가?

Expected output:

- 사용자면 설명 후보 3-5개
- 벡터플면 설명 후보 3-5개
- 엔진면 설명 후보 3-5개
- 3면 순환 전체 설명 후보 3개 내외

## Track B. line / axis language

- Q6. 현재 공간 안에서 "line이 무엇인가"를 가장 잘 설명하는 문장은 무엇인가?
- Q7. 현재 공간 안에서 relation / gap / pending / reflux를 설명하는 반복 문장은 무엇인가?
- Q8. 현재 공간 안에서 current_stage와 maturity_level을 분리해서 설명하는 문장은 무엇인가?
- Q9. 현재 공간 안에서 hold / reflux / promoted를 단순 성공/실패가 아닌 다른 방식으로 읽은 문장은 무엇인가?
- Q10. 현재 공간 안에서 line이 왜 중요한지 설명하는 문장은 무엇인가?

Expected output:

- line 정의 후보 5개 내외
- relation / gap / pending / reflux 설명 후보
- stage / maturity 분리 설명 후보
- 사람이 이해하기 쉬운 재서술 문장

## Track C. return / reflux language

- Q11. 현재 공간 안에서 return / validation / hold / reflux / reingest / promoted를 설명하는 문장은 무엇인가?
- Q12. 현재 공간 안에서 반환이 왜 단순 결과가 아닌지 설명하는 문장은 무엇인가?
- Q13. 현재 공간 안에서 반환이 다시 사용자면/벡터플면 재료가 된다는 것을 보여주는 문장은 무엇인가?
- Q14. 현재 공간 안에서 trace / memory / 흔적 / 기억이 왜 중요한지 설명하는 문장은 무엇인가?
- Q15. 현재 공간 안에서 "결과"보다 "재배치/환류"에 가까운 표현은 무엇인가?

Expected output:

- hold / reflux / reingest / promoted / accepted 설명 후보
- 환류/재배치 해석 문장 후보
- 사람이 이해할 수 있는 쉬운 재서술 문장
- 나중에 CLI나 문서에 바로 쓸 운영 문장

## Track D. assistant input grammar

- Q16. 현재 공간 안에서 공간 / 엔진 / 외부도구 / 운용층의 경계를 분명히 하는 문장은 무엇인가?
- Q17. 현재 공간 안에서 목적 / 범위 / 하지 않을 것을 분명히 하는 문장은 무엇인가?
- Q18. 현재 공간 안에서 지금 단계, 즉 사고 실험 / 언어 적립 / 셋업 / 테스트 / 반복 후 잠금을 드러내는 문장은 무엇인가?
- Q19. 현재 공간 안에서 잠금 / 기록 / 보류 / 미래층 / 참조층 / 임시 발판 같은 판단 강도를 드러내는 문장은 무엇인가?
- Q20. 현재 공간 안에서 시스템 말과 쉬운 말을 함께 두는 번역 문장은 무엇인가?

Expected output:

- 경계 문장 후보
- 목적/범위/금지선 문장 후보
- 단계 문장 후보
- 판정 강도 문장 후보
- 시스템 언어 <-> 쉬운 말 번역 후보

## required item fields

각 항목은 아래 형식으로 정리한다.

- `raw_expression`
- `interpreted_meaning`
- `bucket_or_grammar_type`
- `related_surface`
- `related_line_or_axis`
- `human_rewrite`
- `why_useful_now`
- `unresolved`
- `source_refs`
- `repetition_signal`
- `source_priority`
- `freshness_note`
- `overlap_with_previous_run`

## run metadata

각 실행마다 아래 metadata를 남긴다.

- `run_id`
- `date`
- `scope`
- `primary_focus`
- `source_priority_used`
- `compared_against_previous_run`
- `new_expressions_found`
- `stronger_rewrites_found`
- `stable_candidates_promoted`
- `unresolved_carried_forward`

## candidate judgment rule

### stable_candidate로 올릴 수 있는 조건

- 서로 다른 문맥에서 반복 출현할 것
- 현재 셋업 목적에 직접 유용할 것
- 사람 언어로도 무리 없이 재서술 가능할 것
- current body reading과 충돌하지 않을 것

### stable_candidate로 올리면 안 되는 경우

- 한두 문맥에서만 예쁘게 보이는 표현
- lineage material에는 있으나 current body reading과 거리가 있는 표현
- workflow-hub / team-relay / automatic routing 같은 운영 확장층 표현을 본체 언어로 오인한 경우
- generated/test artifact에서만 강하게 보이는 표현

그 외는 unresolved 또는 future-layer candidate로 둔다.

## final deliverables

Each execution should produce:

1. extracted dataset
   - Track A/B/C/D 전체 항목
   - raw expression 중심
   - source refs 포함
2. short synthesis report
   - 이번 실행에서 반복 출현한 핵심 표현
   - 지금 바로 셋업에 쓸 수 있는 문장 후보
   - assistant 입력 문법으로 적립할 수 있는 문장 후보
   - 아직 잠그면 안 되는 표현
   - 추가 탐색이 필요한 빈칸
3. stable candidates
   - 이번 실행에서 stable_candidate로 올릴 수 있는 표현
   - 왜 안정 후보인지 이유 포함
4. unresolved / future-layer list
   - 현재 보류해야 하는 표현
   - future-layer candidate
   - lineage-only candidate
   - additional evidence needed

## shortest execution prompt

현재 통합엔진 셋업과 assistant 해석 안정성에 필요한 공통 언어층을 만들기 위해, 3면 설명 언어(A), line/축 설명 언어(B), 반환/환류 설명 언어(C), 그리고 경계/목적/단계/판정/번역 문법(D)을 공간에서 깊게 탐색해 번역/해석 데이터로 추출하라.

## current execution note

The first execution result for this question set is currently stored in:

- `docs/reports/integrated_engine_common_language_extraction_v1.md`

Use that report as:

- harvest_round_1
- first language material
- comparison baseline for future runs

Do not use it as:

- final schema
- permanent lock
- canonical state machine
- permanent workflow-hub proof

Future runs should compare against it to detect:

- repeated expressions
- stronger rewrites
- new candidate grammar
- stale or weak expressions that should not be promoted
