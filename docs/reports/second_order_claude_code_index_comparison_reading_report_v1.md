[[A]] [[OBJ:second_order_claude_code_index_comparison_reading_report_v1]] [[SEM:comparison_domain_reading_for_second_order_accumulation_validation]]

# second-order claude_code_index comparison reading report v1

## 1. purpose

- 이번 비교의 목적은 `claude_code_index.txt`를 AI/에이전트 대화처럼 잘 읽히게 만드는 것이 아니다.
- 목적은 현재 2차 축적 구조를 그대로 적용했을 때 무엇이 유지되고, 무엇이 붕괴하고, 무엇이 새로 나타나는지 보는 것이다.
- 따라서 이번 문서는 `claude_code_index`를 잘 해석했다는 보고서가 아니라, `second_order_object_lift` 이전 전단 구조가 실제 비교 도메인을 받아낼 수 있는지 보는 검증 리포트다.

## 2. input and outputs

- input_asset: `inputs/external_cases/claude_code_index.txt`
- generated outputs:
  - `app/work/dialogue_loop_test/generated/dialogue_asset_purpose_synthesis_claude_code_index_v1_20260328.json`
  - `app/work/dialogue_loop_test/generated/question_inducing_block_candidates_claude_code_index_v1_20260328.json`
  - `app/work/dialogue_loop_test/generated/multi_pass_interpretation_training_claude_code_index_v1_20260328.json`
  - `app/work/dialogue_loop_test/generated/context_unit_candidates_claude_code_index_v1_20260328.json`
- related reports:
  - `docs/reports/claude_code_index_engine_purpose_reset_reading_v1.md`
  - `docs/reports/question_inducing_block_claude_code_index_review_v1.md`
  - `docs/reports/multi_pass_interpretation_claude_code_index_training_v1.md`

## 3. what stayed

- `object opening` 감각은 부분적으로 유지됐다.
  - `생산성/코딩`, `구현/자동화`, `전략/방향성` 같은 객체 opening은 여전히 출력되었다.
- `question opening`과 `relation movement`를 보려는 태도는 유지됐다.
  - `transition_hint`, `execution_shift_hint`, `specification_hint`, `question_generation_hint`가 여전히 뜬다.
- 공통 축적 필드는 실제 비교 판독에 도움이 됐다.
  - `supporting_first_pass_patterns`, `domain_specific_suspicion`, `reusable_attitude_hint`, `candidate_status`, `hold_reason`, `evidence_pointers`가 이번 비교를 설명하는 핵심 메타데이터로 작동했다.
- `summary-stage residue priority`라는 태도는 비교 도메인에서도 유지됐다.
  - residue를 hard suppression하지 않고 opening surface 우선순위 문제로 보는 태도는 계속 살아남았다.

## 4. what broke

- block/window 분해가 사실상 붕괴했다.
  - 현재 split 방식에서는 `claude_code_index.txt`가 거의 단일 block, 단일 window로 읽힌다.
  - 그 결과 `question-inducing candidate`도 `0_0` 하나로 수렴한다.
- paragraph role reading은 입력 구조 의존성이 그대로 드러났다.
  - `run_paragraph_role_interpretation_training.py`는 `Bundle-Unbundle 프레임워크` 같은 heading을 찾지 못해 실패했다.
  - 이는 paragraph-role layer가 아직 `youtube_03_22`식 문단/heading 구조에 강하게 묶여 있음을 보여준다.
- multi-pass context unit 재구성은 재사용 가능한 구조가 아니라 아직 youtube scaffold를 끌고 있다.
  - `agent_interface_transition_unit`, `future_of_work_supervisor_unit`, `model_eval_shift_unit`가 그대로 출력되지만 `present_window_refs`는 비어 있다.
  - 즉 context unit 발생 조건이 아니라 기존 자산의 역할 이름이 앞서고 있다.
- 일부 report wording은 여전히 AI/유튜브 대화에 과하게 고정돼 있다.
  - `claude_code_index` 리포트인데도 `youtube_03_22`용 해석 문장과 AI 시대 담론이 부분적으로 남아 있다.

## 5. what newly emerged

- `single operational block collapse`라는 새 비교 패턴이 드러났다.
  - 긴 대화 자산과 달리, 코드/도구 설명 자산은 현재 split에서 거대한 단일 운영 블록처럼 읽힌다.
- `setup / usage / tooling surface`가 하나의 큰 context-preserving block으로 붙는 경향이 보였다.
  - 이는 질문 seed가 문단 간 전이보다 단일 operational surface에서 발생할 수 있음을 시사한다.
- `AI object vocabulary overfire`도 새 비교 신호다.
  - 원문에 없는 `AI의 미래`, `일의 미래`, `에이전트 애플리케이션`이 여전히 전면에 뜨는 것은, 현재 object opening layer가 AI 대화 자산에서 배운 이름을 코드 인덱스에도 과투영하고 있음을 보여준다.

## 6. domain-specific vs reusable clues

### reusable-looking attitudes

- 객체가 여러 개 함께 살아남을 때 question opening을 본다
- relation movement를 설명층 아래의 전이로 읽는다
- residue를 삭제 대신 summary-stage priority 문제로 본다
- 2차 결과를 `collect_only` / `hold` 상태로 남긴다

### domain-specific leaning signals

- `생산성/코딩`, `에이전트 애플리케이션`, `AI의 미래`, `일의 미래` 같은 이름은 `claude_code_index`에서도 과하게 전면화됐다
- `pivot`, `question seed`, `compression node`는 그대로 쓰이지만, 이들이 실제로 page flow에서 발생한 것인지 기존 AI dialogue scaffold를 가져온 것인지 구분이 더 필요하다
- heading-driven paragraph role reading은 현재 도메인/포맷 특화 의존성이 높다

## 7. common accumulation fields review

- `input_asset_type`
  - 현재는 `high_density_dialogue`로 남았는데, `claude_code_index`에는 어색하다
  - 비교용으로는 유용하지만, asset type 분류 기준은 더 세밀해질 필요가 있다
- `supporting_first_pass_patterns`
  - 어떤 1차 조건 위에서 2차 판독이 나왔는지 이해하는 데 실제로 도움이 됐다
- `second_order_reading_type`, `rereading_mode`
  - 동일 스크립트가 어떤 재독해 태도를 수행하는지 비교할 수 있게 해줬다
- `domain_specific_suspicion`, `reusable_attitude_hint`
  - 이번 비교의 핵심 필드였다
  - 무엇이 AI 도메인 특화인지, 무엇이 재사용 가능한 태도인지 나누는 데 직접 도움을 줬다
- `candidate_status`, `hold_reason`
  - object lift를 보류해야 하는 이유를 명시적으로 남길 수 있었다
- `evidence_pointers`
  - 비교 리포트가 감상문이 아니라 generated output 기반 읽기라는 점을 보증해줬다

## 8. why object lift is still premature

- `business_power_shift`, `orchestration`, `domain_to_component_reframing` 같은 이름은 이번 비교 도메인에서 반복 재등장하지 않았다.
- 오히려 이번 비교는 객체 이름보다 `그런 이름이 떠오르는 조건`을 더 분명하게 만들었다.
- 따라서 지금은 object lift가 아니라:
  - repeated pattern table 보강
  - reusable attitude vs domain-specific naming 분리
  - candidate registry의 hold reason 정교화
  를 먼저 해야 한다.

## 9. implications for pre-object-lift notes

- pattern table에는 `single operational block collapse`와 `AI object vocabulary overfire`를 비교 패턴으로 추가할 수 있다.
- split note에는 `이름은 깨져도 태도는 유지되는 경우`와 `태도도 함께 깨지는 경우`를 더 분리해 적을 수 있다.
- candidate registry에는 새 상위 객체를 바로 넣기보다, `claude_code_index`가 object lift를 보류하게 만드는 비교 증거로 기록하는 편이 맞다.
- operating surface에는 `domain-specific suspicion`과 `context-unit collapse`를 직접 보여주는 panel이 추가로 필요하다.

## 10. status

- status: `PASS_WITH_NOTE`
- one-line verdict: `claude_code_index` 비교 투입은 2차 축적 구조가 완전히 깨지지 않는다는 점과, 동시에 현재 문맥 scaffold와 도메인 투영이 얼마나 강한지도 같이 드러내 주었다.

## 11. one-line summary

> `claude_code_index.txt` 비교 투입 결과, 2차 보정의 재사용 가능한 태도는 일부 유지됐지만 context-unit 재구성과 객체 naming은 여전히 AI dialogue scaffold에 강하게 묶여 있었고, 바로 object lift로 가면 안 되는 이유가 더 선명해졌다.
