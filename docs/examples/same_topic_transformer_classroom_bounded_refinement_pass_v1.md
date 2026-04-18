# same_topic_transformer_classroom_bounded_refinement_pass_v1

## 1. canonical inputs
- case A: [choi_ai_classroom_transformer1.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/choi_ai_classroom_transformer1.txt)
- case B: [choi_ai_classroom_transformer2.txt](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/choi_ai_classroom_transformer2.txt)

## 2. refined frame candidate
- constraint / problem background
  - 기존 순차 처리 방식의 제약, 병렬성 부족, 미래 참조 제어 같은 배경 문제가 먼저 제시된다.
- transformer structure entry
  - encoder 또는 decoder 관문으로 들어가며 전체 블록 구조와 역할이 먼저 잡힌다.
- major operating mechanism explanation
  - self-attention, positional encoding, autoregressive decoding, causal mask처럼 실제 작동 메커니즘 설명으로 이어진다.

## 3. refined emphasis split candidate
- encoder-side explanatory emphasis
  - transformer1은 구조 진입과 개념 접지에 더 가깝다.
  - self-attention, QKV, positional encoding을 입문 설명축으로 둔다.

- decoder / generation-side explanatory emphasis
  - transformer2는 생성 흐름과 시간 순서 제약 설명에 더 가깝다.
  - autoregressive decoding, causal mask, conditional probability를 강조한다.

## 4. refined defer bucket
- teaching convenience simplification
  - 학습 편의를 위해 메커니즘을 단순화하거나 매끈하게 잇는 문장들
- presenter-style emphasis
  - `중요하다`, `머릿속에 담아둬야 한다` 같은 강의 진행 강조
- observer-only transitions
  - 구조 자체보다 강의 연결과 설명 리듬을 위한 전환 문장

## 5. refinement note
- repeated frame candidate retained: YES
- emphasis split clarified: YES
- defer bucket clarified: YES
- later promotion still premature: YES
- further refinement useful: YES
