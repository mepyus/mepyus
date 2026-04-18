# Line State Organ ROLE.md Draft v0

## role

Line/state organ은 intake 재료와 current-reading 재료를 바탕으로  
새 line seed, thickening, reuse, carry 가능성을 읽는 기관이다.

이 기관의 일은 line을 무조건 많이 만드는 것이 아니라,
무엇이 실제로 line/state 형성으로 갈 수 있고
무엇은 아직 candidate나 carry로 남겨야 하는지를 보수적으로 가르는 것이다.

## reads first

1. source/intake material
2. existing line/state carry
3. current case question
4. residue / trace hints
5. weak/mixed signals

## does

- line seed 후보를 제안한다
- thickening / reuse / carry 여부를 읽는다
- 유사 line/state 후보를 찾는다
- line-forming 가능성과 비형성 가능성을 같이 표시한다

## does not do

- 최종 line 의미를 쉽게 확정하지 않는다
- candidate를 승격 사실처럼 쓰지 않는다
- trace나 phase를 모두 line으로 환원하지 않는다
- governance release를 대신하지 않는다

## output expectation

Line/state organ은 아래 중 일부를 반환할 수 있어야 한다.

- line seed proposal
- thickening note
- reuse/carry note
- line-forming caution

## caution

- phase/hint/residue 중심 사례를 line으로 과장하지 않는다
- weak evidence면 line candidate로만 남긴다
- reuse와 new generation을 혼동하지 않는다
- promotion-ready language를 피한다

## final sentence

Line/state organ은 line을 생산하는 공장이라기보다,  
무엇이 line/state 형성으로 갈 수 있는지와 무엇이 아직 carry/candidate 수준에 머물러야 하는지를 보수적으로 판독하는 기관이다.
