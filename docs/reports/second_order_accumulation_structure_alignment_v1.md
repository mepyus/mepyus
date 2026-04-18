[[A]] [[OBJ:second_order_accumulation_structure_alignment_v1]] [[SEM:reframing_second_order_scripts_from_readers_to_accumulators]]

# second-order accumulation structure alignment v1

## 1. purpose

- 이번 문서의 목적은 현재 2차 보정 스크립트를 판정기보다 축적기로 다시 읽는 것이다.
- 핵심은 결과 문장보다 `어떤 조건에서 그런 2차 판독이 나왔는가`를 남기는 구조로 이동하는 데 있다.

## 2. current script reinterpretation

- `run_dialogue_asset_purpose_synthesis.py`
  - 기존: 객체/층위/관계/시대 질문 번역기
  - 현재 재정의: object opening / question opening / layer translation 패턴 수집기
- `run_question_inducing_block_review.py`
  - 기존: 질문 유도 block 재선별기
  - 현재 재정의: question opening 조건과 summary-stage residue 후순위 패턴 수집기
- `run_multi_pass_interpretation_training.py`
  - 기존: multi-pass 재독해와 context unit 재구성기
  - 현재 재정의: pass 차이, 해석 이동, context unit 발생 조건 수집기
- `run_paragraph_role_interpretation_training.py`
  - 기존: paragraph role 판독기
  - 현재 재정의: 맥락에 따른 role shift 사례 수집기

## 3. common accumulation fields

- `input_asset_type`
- `source_asset_ref`
- `supporting_first_pass_patterns`
- `second_order_reading_type`
- `rereading_mode`
- `scope_local_page_comparison`
- `domain_specific_suspicion`
- `reusable_attitude_hint`
- `candidate_status`
- `hold_reason`
- `evidence_pointers`

## 4. why this matters

- 지금 필요한 것은 더 강한 판정문이 아니라, 나중에 일반화 검토 때 다시 읽을 수 있는 관측 메타데이터다.
- 2차 값이 `무엇인지`만 남기면 나중에 과잉 일반화를 막기 어렵다.
- 반대로 `어떤 입력 / 어떤 1차 조건 / 어떤 재독해 모드`에서 2차 값이 나왔는지 남기면 도메인 특화성과 재사용 가능한 태도를 분리할 수 있다.

## 5. bounded result

- 이번 정렬은 2차 스크립트를 약화시키는 것이 아니다.
- 오히려 지금 단계의 역할을 더 명확하게 한다:
  - 지금은 **generalizer** 가 아니라 **collector**
  - 지금은 **object lock** 이 아니라 **pattern accumulation**

## 6. one-line summary

> 현재 2차 보정 스크립트는 더 많이 맞히는 기관이 아니라, 미래 일반화를 위해 rereading 조건과 second-order pattern을 구조적으로 남기는 축적 기관으로 재정렬된다.
