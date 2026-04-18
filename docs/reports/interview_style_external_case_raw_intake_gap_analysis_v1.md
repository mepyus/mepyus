# interview_style_external_case_raw_intake_gap_analysis_v1

## 1. purpose
- 이번 문서는 인터뷰형 외부자료 3건을 내가 먼저 사례 기준으로 정리한 pass와,
  raw txt를 그대로 `inputter + labeler` 경로에 넣은 probe 사이의 gap을 비교한다.
- 목적은 승격이 아니라,
  현재 입력기가 어디까지 자동으로 잡고 어디서부터 사람이 구조를 읽어줘야 하는지 확인하는 것이다.

## 2. canonical inputs
- [dario_amodei_youtube.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/dario_amodei_youtube.txt)
- [andrej_karpathy_youtube.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/andrej_karpathy_youtube.txt)
- [alexkarp_youtube.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/alexkarp_youtube.txt)

## 3. raw intake probe result

### dario raw probe
- dust_count: `471`
- dominant scene: `review 453`
- dominant flow: `compare 446`
- avg D/I/S: `0.491 / 0.529 / 0.505`
- top anchors:
  - `domain_term:우리가`
  - `domain_term:당신이`
  - `domain_term:거대한`
  - `domain_term:모델이`
  - `domain_term:소프트웨어`

### andrej raw probe
- dust_count: `483`
- dominant scene: `review 466`
- dominant flow: `compare 466`
- avg D/I/S: `0.494 / 0.517 / 0.502`
- top anchors:
  - `domain_term:우리가`
  - `domain_term:겁니다`
  - `domain_term:LRM`
  - `domain_term:우리는`
  - `domain_term:거대한`

### alex raw probe
- dust_count: `560`
- dominant scene: `review 551`
- dominant flow: `compare 542`
- avg D/I/S: `0.488 / 0.528 / 0.504`
- top anchors:
  - `domain_term:우리가`
  - `domain_term:있습니다`
  - `domain_term:겁니다`
  - `domain_term:거대한`
  - `domain_term:그래서`

## 4. already-known manual first-pass result

### dario manual first-pass
- ref: [external_case_first_pass_dario_amodei_youtube_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/examples/external_case_first_pass_dario_amodei_youtube_v1.md)
- extracted outer frames:
  - scaling variables as main progress frame
  - verifiable-vs-nonverifiable task split frame
  - coding automation threshold frame

### andrej manual first-pass
- ref: [external_case_first_pass_andrej_karpathy_youtube_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/examples/external_case_first_pass_andrej_karpathy_youtube_v1.md)
- extracted outer frames:
  - non-animal / ghost-like learning contrast
  - RL inefficiency and noisy signal
  - reflection / process supervision gap

### alex manual first-pass
- ref: [external_case_first_pass_alexkarp_youtube_v1.md](/Users/sungsookim/universe/vectorfl_replica/docs/examples/external_case_first_pass_alexkarp_youtube_v1.md)
- extracted outer frames:
  - domain controlled software layer
  - generic LLM insufficiency for regulated work
  - harsh environment reliability
  - trusted operator / training bottleneck

## 5. gap reading

### gap A. raw intake는 문장을 많이 만들지만 구조를 거의 못 올린다
- raw probe는 3건 모두를 `470~560` dust 수준으로 잘게 쪼갰다.
- 하지만 scene/flow는 거의 전부 `review / compare` 로 평평하게 수렴했다.
- 즉 현재 입력기는 인터뷰 transcript를 “많은 단위”로는 자르지만,
  그 단위를 상위 설명 구조로 다시 묶는 힘은 약하다.

### gap B. generic anchor noise가 너무 강하다
- 상위 anchor가 `우리가`, `있습니다`, `겁니다`, `거대한`, `그래서` 같은 generic term으로 뜬다.
- 이는 인터뷰형 한국어 전사본에서
  발표자 말버릇 / 구어체 / 연결어가 anchor 상위를 오염시키고 있다는 뜻이다.
- 반대로 manual first-pass는 이런 표현을 observer/defer 쪽으로 밀고,
  case-level frame만 남겼다.

### gap C. 현재 labeler 값은 3건을 거의 비슷한 문서로 본다
- avg D/I/S가 세 케이스 모두 `약 0.49 / 0.52 / 0.50` 근처에 몰려 있다.
- 즉 현재 score는
  - dario의 scaling/verification
  - andrej의 learning critique
  - alex의 deployment/control
  차이를 거의 만들지 못한다.
- 이 값은 지금 단계에서 “문서별 operating character”보다
  “인터뷰형 텍스트 일반”을 더 강하게 반영한다.

### gap D. raw probe는 interview-style commonality는 잡지만 topic-specific frame은 못 잡는다
- 세 문서 모두 인터뷰형이라 question-answer 흐름과 설명 톤이 있다.
- 현재 inputter + labeler는 이 공통 형식 때문에 세 문서를 비슷하게 읽는다.
- 하지만 manual pass는 같은 인터뷰 형식 아래에서도
  topic-specific frame이 크게 갈린다는 점을 드러냈다.

## 6. interpretation
- step 1만 보면:
  - “이 세 문서는 다 인터뷰형 review/compare 문서다” 수준에서 멈춘다.
- step 2까지 가면:
  - dario = scaling / verification / automation threshold
  - andrej = RL inefficiency / reflection gap / learning critique
  - alex = control layer / regulated deployment / trusted operator bottleneck
  같이 case-level frame 차이가 보인다.

- 그래서 지금 입력기에서 가장 큰 gap은:
  - raw split/label 단계와
  - case-level frame extraction 단계
  사이의 중간 계층이 비어 있다는 점이다.

## 7. what this means for scripting
- 지금 스크립트화의 핵심은 곧바로 promotion logic이 아니다.
- 먼저 필요한 것은 다음 두 층이다.

### layer 1. interview transcript pre-normalizer
- speaker / timestamp / chapter marker 정리
- generic Korean discourse term downweight
- pronoun / filler / presenter-style connector 억제

### layer 2. case-level frame aggregator
- dust hundreds 개를 그대로 보지 않고
- paragraph or topic block 단위로 재묶기
- repeated high-signal term cluster를 outer frame 후보로 올리고
- generic rhetoric은 defer / observer bucket으로 내리기

## 8. current lock
- raw intake only로는 이 3건의 핵심 차이를 충분히 읽지 못한다.
- manual first-pass는 여전히 필요하다.
- 하지만 raw probe는
  - 현재 labeler가 어디서 평평해지는지
  - 어떤 generic anchor가 오염을 만드는지
  를 보여주는 좋은 diagnostic 이다.

## 9. one-line conclusion
- 인터뷰형 외부자료 3건에 대해 raw intake는 형식 공통성만 강하게 잡고 topic-specific frame은 거의 못 올렸고, 바로 그 gap이 앞으로 스크립트화해야 할 핵심 구간이다.
