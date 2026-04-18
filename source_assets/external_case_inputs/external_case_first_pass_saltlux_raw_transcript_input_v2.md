[[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]]
[[A]] [[OBJ:external_case_first_pass_raw_transcript]] [[SEM:saltlux_canonical_raw_transcript_first_pass]]

# CODEx 입력문 v2 — saltlux.txt canonical first pass
# 목적: 상위 폴더의 `saltlux.txt`를 이번 외부 사례의 SSOT로 고정하고,
# raw transcript 기준으로 exploration observation / core promotion checklist /
# refinement trigger rules를 실제 적용한다.

## 0. 기준 입력 고정
이번 솔트룩스 사례의 canonical source는 아래 파일이다.
- `saltlux.txt`

### source meta
- case_name: `saltlux_agentic_ai_ontology_raw_transcript_v1`
- source_ref: `saltlux.txt`
- source_type: `external_case_primary_transcript`
- source_origin: `raw_youtube_talk_transcript`
- source_status: `primary_transcript_with_asr_noise`
- stance: `observe_and_separate_before_adopt`
- companion_note: `claude_secondary_summary_available_for_comparison`

## 1. 이번 턴의 성격
이번 턴은 솔트룩스 강연을 믿고 채택하는 턴이 아니다.

이번 턴은 아래를 검증하는 턴이다.
1. raw transcript를 observation layer에 기록할 수 있는가
2. transcript 안의 요소를 core / outer / defer / observer_only 로 분리할 수 있는가
3. refinement trigger rules 기준에서 현재 상태를 읽을 수 있는가

## 2. raw transcript 처리 원칙
`saltlux.txt`는 정제된 보고서가 아니라 raw transcript다.

반드시 아래 4층으로 분리해서 본다.
- 구조 프레임
- 제품/비즈니스 주장
- 강연 수사 / 포지셔닝
- 실무 전개 힌트

## 3. observation layer 기록 지시
산출물:
- `docs/examples/external_case_first_pass_saltlux_raw_transcript_v1.md`
- `runtime/observer/exploration/json/external_case_first_pass_saltlux_raw_transcript_v1.json`
- `runtime/observer/exploration/md/external_case_first_pass_saltlux_raw_transcript_v1.md`
- `runtime/contracts/core_promotion_reading_saltlux_raw_transcript_v1.json`
- `runtime/contracts/refinement_trigger_reading_saltlux_raw_transcript_v1.json`

## 4. observation 필수 메타
- exploration_id
- session_id
- run_id
- observed_at
- source_ref = `saltlux.txt`
- source_type = `external_case_primary_transcript`
- source_origin = `raw_youtube_talk_transcript`
- source_status = `primary_transcript_with_asr_noise`

## 5. core promotion checklist 적용 지시
체크 항목:
- repeat_frequency
- cross_context_reappearance
- cross_session_or_run_presence
- actual_reuse_evidence
- outer_only_sufficiency
- explanatory_axis_role
- premature_generalization_risk

상태값:
- core_candidate
- outer_candidate
- defer
- observer_only

## 6. 판독 후보 예시
- 후보 1:
  `온톨로지를 추론엔진 중심이 아니라 semantic interoperability / data fabric 관점으로 읽는 프레임`
- 후보 2:
  `LLM 단독이 아니라 grounding + symbolic expression layer 결합이 필요하다는 프레임`
- 후보 3:
  `에이전틱 AI = reasoning + planning + tool use + multi-agent coordination 프레임`
- 후보 4:
  `제품 성과 수치 / 운영비 / 도입 사례 / 할루시네이션 제로류 강한 주장`
- 후보 5:
  `팔란티어 vs 솔트룩스 비교를 통한 시장 포지셔닝 및 소버린 AI framing`

## 7. 주의할 분리 규칙
- defer 우선:
  - 할루시네이션 제로
  - 특정 사용자 수 / 운영비 / 도입 규모 수치
  - 경쟁사 열위/우위 단정
  - 소버린 AI 가능/불가의 강한 결론
- outer 또는 관측 가치:
  - semantic interoperability
  - data fabric / mashup 읽기
  - grounding 필요성
  - symbolic 표현층의 필요성
  - agentic workflow 프레임
- observer_only 가능:
  - 강연 수사
  - 자사 브랜딩/포지셔닝
  - 미래 전망 문장

## 8. refinement trigger 읽기 지시
기존 trigger rules 기준으로
`no_trigger / watch / refinement_candidate / refinement_recommended`
중 하나를 읽는다.

## 9. 작성 문서의 중심
강연 소개문이 아니라
이 transcript를 넣었을 때 우리 운영 슬롯이 어떻게 작동했는가를 중심으로 쓴다.

## 10. 한 줄 요약
이번 턴은 `saltlux.txt` 를 canonical raw transcript로 고정하고,
구조는 관측하고, 강한 주장과 수치는 defer하며,
core/outer/defer/observer_only 분리가 실제로 작동하는지 검증하는 1차 판독 턴이다.
