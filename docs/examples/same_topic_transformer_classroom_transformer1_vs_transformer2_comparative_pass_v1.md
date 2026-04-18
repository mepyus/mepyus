# same_topic_transformer_classroom_transformer1_vs_transformer2_comparative_pass_v1

## 1. canonical inputs
- case A: [choi_ai_classroom_transformer1.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/choi_ai_classroom_transformer1.txt)
- case B: [choi_ai_classroom_transformer2.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/choi_ai_classroom_transformer2.txt)

## 2. repeated explanatory outer frame
- previous limitation -> transformer structure -> key mechanism explanation
  - 두 문서 모두 기존 방식의 한계나 제약을 먼저 짚고, 트랜스포머 구조를 꺼낸 뒤 핵심 메커니즘 설명으로 들어간다.
- classroom decomposition frame
  - 둘 다 강의형 자료답게 전체 구조를 블록 단위로 쪼개서 용어를 단계적으로 풀어준다.
- architecture-to-operation frame
  - 한 문서가 구조를 설명하면 그 구조가 실제 어떻게 동작하는지, 어떤 흐름을 갖는지까지 연결한다.

## 3. case-specific emphasis
- transformer1 emphasis
  - encoder-side explanation
  - 병렬 처리, positional encoding, self-attention, query/key/value 입문 설명
  - 개념 진입과 비유형 설명이 더 강하다

- transformer2 emphasis
  - decoder-side explanation
  - autoregressive decoding, conditional probability, causal mask, generation flow
  - 생성 과정과 학습/추론 차이를 더 강하게 드러낸다

## 4. defer / observer-only notes
- presenter-style rhetoric separated: YES
  - `굉장히 중요하다`, `머릿속에 담아둬야 한다` 같은 강의 진행 문장은 reusable frame보다 presenter style에 가깝다.
- defer-worthy simplification present: YES
  - 교육 편의를 위해 구조를 단순화한 문장들이 있어, 이를 곧바로 보편 기준선으로 올리면 과잉 일반화 위험이 있다.

## 5. refinement note
- later refinement pass useful: YES
- note:
  - refinement 후보는 `explanatory outer frame for same-topic classroom architecture materials` 정도로는 가치가 있다.
  - 다만 아직은 트랜스포머 강의 일반론으로 고정할 수준은 아니다.
