# readable input board / interview_residue_interference_reduction_review_v1_20260328_094939

## 1. 입력 정보
- input_id: `interview_residue_interference_reduction_review_v1`
- label: `interview_residue_interference_reduction_review_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/interview_residue_interference_reduction_review_v1.md`
- input_kind: `mixed`
- detected_profile: `note`

## 2. split 결과
- split_mode_used: `heading`
- raw_line_count: `339`
- unit_count: `38`

## 3. unit 목록 요약
- unit_001 — heading_block / interview_residue_interference_reduction_review_v1.md ~ interview_residue_interference_reduction_review_v1.md — "# interview_residue_interference_reduction_review_v1.md..."
- unit_002 — heading_block / 1. review target ~ 1. review target — "## 1. review target - primary: - `app/work/archive_review/interview_support/middle_layer_experiments/generated/middle_layer_interview_probe_20260328T0027..."
- unit_003 — heading_block / 2. key finding ~ 2. key finding — "## 2. key finding 문제는 단순히 discourse term이 많다는 것이 아니다. interview류에서는 아래가 겹쳐서 user-layer translation을 방해한다. - discourse co..."
- unit_004 — heading_block / 3. residue vocabulary draft ~ 3. residue vocabulary draft — "## 3. residue vocabulary draft 이번 턴에서는 hard rule로 잠그지 않고, 아래 review vocabulary로 본다...."
- unit_005 — heading_block / 3-1. discourse_connective_residue ~ 3-1. discourse_connective_residue — "### 3-1. discourse_connective_residue 예: - `우리가` - `하지만` - `그리고` - `겁니다` - `있습니다` 특징: - 발화 연결과 강조를 담당한다 - anchor 경쟁 상위에 ..."
- unit_006 — heading_block / 3-2. speaker_or_source_residue ~ 3-2. speaker_or_source_residue — "### 3-2. speaker_or_source_residue 예: - `CEO` - `Highlights` - 화자명 / source-specific proper noun 특징: - source identity 흔..."
- unit_007 — heading_block / 3-3. conversational_filler_residue ~ 3-3. conversational_filler_residue — "### 3-3. conversational_filler_residue 예: - `말입니다` - `볼까요` - `저는` - `제가` 특징: - 구어체 인터뷰에서 자연스럽게 반복된다 - 의미 운동을 직접 열지 못한다 -..."
- unit_008 — heading_block / 3-4. generic_abstraction_residue ~ 3-4. generic_abstraction_residue — "### 3-4. generic_abstraction_residue 예: - `모델이` - `완벽히` - `수많은` - `기술적` 특징: - topic-like하게 보이지만 너무 일반적이다 - role gloss는 유..."
- unit_009 — heading_block / 3-5. quasi_topic_residue ~ 3-5. quasi_topic_residue — "### 3-5. quasi_topic_residue 예: - `LRM` - `Sector` 특징: - topic처럼 보이지만 사용자 층위 힌트로는 너무 좁거나 맥락 의존적이다 - raw signal로는 유의미할 수 ..."
- unit_010 — heading_block / 3-6. observer_transition_residue ~ 3-6. observer_transition_residue — "### 3-6. observer_transition_residue 예: - `Opening` - `챕터` - `질문 하나` - `본격적인 대담에 앞서` 특징: - 발화 구조 전환에는 유용하다 - 하지만 user-la..."
- unit_011 — heading_block / 4. where interference happens ~ 4. where interference happens — "## 4. where interference happens..."
- unit_012 — heading_block / 4-1. anchor extraction stage ~ 4-1. anchor extraction stage — "## 4-1. anchor extraction stage 여기서는 residue가 아직 제거되지 않는다. 문제: - interview 텍스트의 발화체 반복이 토큰으로 잘 살아남는다 - 그래서 `우리가`, `하지만`,..."
- unit_013 — heading_block / 4-2. anchor bucket stage ~ 4-2. anchor bucket stage — "## 4-2. anchor bucket stage 여기서 residue는 이미 일부 분리되지만, 여전히 bucket 내부 질감 차이가 남아 있다. 예: - discourse residue 안에서도 - 단순 접속어 -..."
- unit_014 — heading_block / 4-3. opening summary stage ~ 4-3. opening summary stage — "## 4-3. opening summary stage concept probe에서는 여기서 비교적 안정적이다. 하지만 interview-only probe에서는 - Dario - Alex 둘 다 `명확한 사용자 층위..."
- unit_015 — heading_block / 4-4. user-facing summary stage ~ 4-4. user-facing summary stage — "## 4-4. user-facing summary stage middle-layer packet에서는 여기서 가장 큰 간섭이 보인다. 예: - Dario: - `모델이, 완벽히, 수많은, 기술적` - Andrej: ..."
- unit_016 — heading_block / 5. case-by-case interference ~ 5. case-by-case interference — "## 5. case-by-case interference..."
- unit_017 — heading_block / 5-1. Dario ~ 5-1. Dario — "## 5-1. Dario..."
- unit_018 — heading_block / 실제 topic-bearing signal ~ 실제 topic-bearing signal — "### 실제 topic-bearing signal - scaling / compute / training / verification 쪽..."
- unit_019 — heading_block / 가리는 residue ~ 가리는 residue — "### 가리는 residue - discourse_connective: - `우리가`, `하지만`, `있습니다` - generic_abstraction: - `모델이`, `완벽히`, `수많은`, `기술적` - con..."
- unit_020 — heading_block / 간섭 방식 ~ 간섭 방식 — "### 간섭 방식 - role은 `mechanism + verification`로 잘 보이는데 - case-specific signal이 너무 일반 추상어로 밀려 사용자가 다음 질문을 떠올리기 어렵다..."
- unit_021 — heading_block / 5-2. Andrej ~ 5-2. Andrej — "## 5-2. Andrej..."
- unit_022 — heading_block / 실제 topic-bearing signal ~ 실제 topic-bearing signal — "### 실제 topic-bearing signal - reflection / RL / gap / human comparison 쪽..."
- unit_023 — heading_block / 가리는 residue ~ 가리는 residue — "### 가리는 residue - discourse_connective: - `우리가`, `하지만`, `겁니다` - quasi_topic: - `LRM` - conversational_filler: - `봅니다` - ..."
- unit_024 — heading_block / 간섭 방식 ~ 간섭 방식 — "### 간섭 방식 - role mix는 잘 산다 - 하지만 summary signal에서 `LRM`과 발화 습관어가 사용자 층위보다 먼저 보인다..."
- unit_025 — heading_block / 5-3. Alex ~ 5-3. Alex — "## 5-3. Alex..."
- unit_026 — heading_block / 실제 topic-bearing signal ~ 실제 topic-bearing signal — "### 실제 topic-bearing signal - deployment / control / security / national-scale operation 쪽..."
- unit_027 — heading_block / 가리는 residue ~ 가리는 residue — "### 가리는 residue - discourse_connective: - `우리가`, `그리고`, `겁니다` - speaker/source residue: - `Highlights`, `CEO` - quasi_to..."
- unit_028 — heading_block / 간섭 방식 ~ 간섭 방식 — "### 간섭 방식 - `문제/제약 + 운영/배치` role은 잘 보인다 - 하지만 front summary에 quasi-topic과 conversational residue가 섞여 사용자 층위 힌트가 약해진다 ---..."
- unit_029 — heading_block / 6. what should not be suppressed ~ 6. what should not be suppressed — "## 6. what should not be suppressed 무조건 억제하면 안 되는 값도 있다...."
- unit_030 — heading_block / do-not-suppress candidate ~ do-not-suppress candidate — "### do-not-suppress candidate - `security` - `verification` - `deployment` - `automation` - `통제` - `운영` - `검증` - `신뢰` - ..."
- unit_031 — heading_block / borderline candidate ~ borderline candidate — "### borderline candidate - `model` - `structure` - `future` - `sector` - `LRM` 이들은 맥락에 따라 - topic-bearing signal일 수도 있고 ..."
- unit_032 — heading_block / 7. provisional candidates only ~ 7. provisional candidates only — "## 7. provisional candidates only 이번 턴은 suppression을 실행하지 않는다. 대신 아래 후보만 남긴다...."
- unit_033 — heading_block / provisional down-weight candidate ~ provisional down-weight candidate — "### provisional down-weight candidate - `우리가` - `하지만` - `그리고` - `겁니다` - `있습니다` - `봅니다` - `말입니다`..."
- unit_034 — heading_block / observer-only candidate ~ observer-only candidate — "### observer-only candidate - `챕터` - `Opening` - `Highlights` - `질문 하나`..."
- unit_035 — heading_block / summary deprioritization candidate ~ summary deprioritization candidate — "### summary deprioritization candidate - `모델이` - `완벽히` - `수많은` - `기술적` - `그들은` - `실제로` - `있다는` - `아니라`..."
- unit_036 — heading_block / do-not-suppress candidate ~ do-not-suppress candidate — "### do-not-suppress candidate - `verification` - `deployment` - `security` - `검증` - `통제` - `운영` - `안보` ---..."
- unit_037 — heading_block / 8. next bounded step ~ 8. next bounded step — "## 8. next bounded step 다음 단계는 아래 쪽이 맞다. - interview summary 생성 단계에서 - generic abstraction residue - quasi-topic residue..."
- unit_038 — heading_block / 9. final judgment ~ 9. final judgment — "## 9. final judgment - status: `PASS` 한 줄로 요약하면: - interview류 residue는 하나의 noise가 아니라 `discourse connective / generic ab..."

## 4. 당장 읽히는 흐름
- 앞쪽은 소개/문제제기, 중간은 설명 확장, 뒤로 갈수록 주제 전환이 생기는 흐름으로 읽힌다.
