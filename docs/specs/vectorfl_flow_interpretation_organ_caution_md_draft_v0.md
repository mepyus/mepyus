# Flow Interpretation Organ CAUTION.md Draft v0

## caution purpose

Flow interpretation organ의 caution 규칙은  
next hop을 읽을 때 그것을 final path처럼 확정하거나, unresolved edge를 지운 채 진행 구조만 예쁘게 보이게 만드는 것을 막는 데 목적이 있다.

## stop / hold conditions

- next hop remains ambiguous
- explanation-first bias still active
- governance restriction still blocks direct readout
- reentry trigger is necessary but not surfaced yet

## preserve-first rules

- next hop은 candidate로 남길 수 있다
- unresolved edge note를 항상 같이 넘긴다
- reentry hint를 분리하지 않고 flow summary에 연결한다
- direct readout hold를 무시하지 않는다

## avoid

- final next step wording
- fully resolved progression wording
- safe to proceed wording without governance support

## final sentence

Flow interpretation organ은 다음 단계를 확정하는 기관이 아니라, 어디로 읽혀야 하는지와 무엇을 아직 preserve해야 하는지를 보수적으로 남기는 기관이다.
