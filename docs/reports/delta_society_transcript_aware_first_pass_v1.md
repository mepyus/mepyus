# delta_society transcript-aware first pass v1

## 1. 사례 개요

- 사례명: `delta_society_ai_native_company_workflow_transcript_v1`
- source_ref: [delta_society.md](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/delta_society.md)
- source_type: `external_case_primary_transcript`
- source_origin: `raw_podcast_or_talk_transcript`
- source_status: `primary_transcript_with_asr_noise`

raw transcript로 두는 이유:

- 인터뷰 진행, 시연, 자기 해설, 운영 주장, 도구 사용 장면이 한 파일 안에 섞여 있다.
- 시점 표기와 챕터 헤더는 많지만 문단 경계는 거칠다.
- 따라서 polished article처럼 요약하기보다, transcript-aware first pass로 운영 구조를 먼저 분리하는 편이 맞다.

## 2. transcript에서 실제로 관측한 구조

- 델타소사이어티는 `돈을 투자하는 VC`보다 `지식 / 네트워크 / AI-native operating method`를 함께 설계하는 조직으로 자신을 설명한다.
- 캠프/커뮤니티/클로드 코드 실습을 통해 같은 고민을 가진 사람들을 모으고, 각자 문제를 직접 풀고 공유하는 구조가 반복된다.
- 업무 운영 쪽에서는 `end-to-end ownership`, `dependency decomposition`, `결과물 중심 커뮤니케이션`이 강하게 반복된다.
- 에이전트 사용은 단순 보조가 아니라 `사람이 하던 디지털 업무를 위임 가능한지 계속 시험하는 운영 감각`으로 읽힌다.
- Slack recording -> concept extraction -> 글감 생성 -> triage -> Linear -> Compound 저장 같은 surface transition이 매우 직접적으로 나온다.
- GitHub 기반 SSoT 구축과 의사결정 기록 정리는 `빠른 의사결정이 많아질수록 기록면이 중요해진다`는 운영 감각과 연결된다.

## 3. outer로 둔 프레임

- AI-native company as operating-structure frame
- knowledge/community as company-building substrate frame
- end-to-end ownership with dependency decomposition frame
- agent delegation plus triage routing frame
- GitHub-based decision transparency / SSoT frame

## 4. defer로 보낸 강한 주장

- AI 시대에는 스타트업에 큰 돈이 덜 필요할 것이라는 일반화
- 소수 인원으로도 큰 기업 가치를 만들 수 있다는 방향성 일반화
- 사람이 예전처럼 역할별로 나뉘지 않아도 된다는 강한 전망
- “누구나 프로덕트를 만들 수 있는 환경”이 빠르게 일반화될 것이라는 주장

## 5. observer_only로 남긴 수사 / 포지셔닝

- 델타소사이어티 소개와 출연자/호스트의 분위기성 문답
- 캠프/커뮤니티에 대한 인상, 감탄, 홍보 톤
- “멋있다”, “재밌다” 같은 반응성 문장
- 자기 사례를 설득력 있게 보이게 하는 장면 연출

## 6. core / outer / defer / observer_only 1차 판독 결과

### 후보 1. end-to-end ownership with dependency decomposition
- status: `outer_candidate`
- reason:
  - `프로젝트를 시작한 사람이 끝까지 책임진다`
  - `책임지지 못하는 부분만 정확히 분리해서 요청한다`
  - `결과물 중심으로 대화한다`
  - 이 구조는 현재 공간의 operating/agent boundary reading과 직접 닿는다.

### 후보 2. Slack recording -> concept extraction -> idea triage -> task routing -> result deposit
- status: `outer_candidate`
- reason:
  - 입력이 바로 읽기 재료가 되고, 읽기 결과가 triage/task/result surface로 계속 이동한다.
  - 현재 공간의 `input_to_reading_organ`과 `transition_over_surface`에 매우 직접적으로 닿는 사례다.

### 후보 3. GitHub-based decision transparency / SSoT
- status: `outer_candidate`
- reason:
  - 빠른 결정이 많아질수록 기록면과 진실 장부를 분리해야 한다는 감각이 있다.
  - 현재 공간의 append-only / summary / source-of-truth discipline과 비교 가치가 높다.

### 후보 4. community/camp as operating multiplication layer
- status: `watch`
- reason:
  - 훈련과 지식 공유가 단순 교육이 아니라 operating method diffusion으로 읽힌다.
  - 다만 현재 line thickening 코어보다 외부 운영 맥락의 반복 축으로 더 보는 편이 안전하다.

### 후보 5. AI-native company / VC role redefinition 큰 가설
- status: `defer`
- reason:
  - 흥미롭지만 구조 일반화가 빠르다.
  - 현재는 operating structure를 읽는 보조 프레임으로만 두고, 코어 승격은 이르다.

## 7. 이번 사례에서 강하게 뜬 line 접점

- `input_to_reading_organ`
  - raw meeting / recording / transcript가 바로 아이디어, 글감, triage input으로 재가공되는 장면이 많다.
- `transition_over_surface`
  - recording -> extraction -> writing prompt -> Linear -> Compound 같은 surface transition이 매우 명시적이다.
- `pre_read_eye`
  - transcript의 챕터/시점/ASR 노이즈 때문에, 실제 reread 전에 먼저 구조를 잡아야 한다는 필요가 분명하다.

## 8. refinement trigger 현재 상태

- status: `watch`
- reason:
  - 이 사례는 현재 strong line들을 설명하는 외부 corroboration으로는 유효하다.
  - 다만 지금은 새로운 strong line을 추가로 잠그기보다, 이미 있는 line이 외부 사례에서 어떻게 재등장하는지 누적하는 편이 맞다.

## 9. 다음 액션 힌트

- transcript-aware watchpoint를 한 번 더 남겨, 이 자료의 segmentation 얇음이 어디서 오는지 분리한다.
- 그 다음 현재 strong lines와의 접점을 `support / caution / weakness`로 나눠 읽는다.
