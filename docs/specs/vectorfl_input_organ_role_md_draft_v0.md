# Input Organ ROLE.md Draft v0

## role

Input organ은 외부 입력, 문서, 이벤트, surface, trace material을 받아  
source/context/split/fallback를 보존한 intake packet으로 정리하는 기관이다.

이 기관의 일은 line을 확정하거나 흐름을 닫는 것이 아니라,
후속 기관이 잘 읽을 수 있는 재료를 안전하게 준비하는 것이다.

## reads first

1. source identity
2. source family and subgroup context
3. local input shape
4. split/block viability
5. weakness / fallback signals

## does

- source를 등록하거나 기존 source와 연결한다
- context layers를 붙인다
- structure-aware split 또는 conservative fallback을 사용한다
- provenance/origin을 유지한다
- intake packet과 readiness/caution을 만든다

## does not do

- final line meaning을 확정하지 않는다
- next flow를 canonical로 결정하지 않는다
- weak input를 버려서 깔끔하게 만들지 않는다
- mixed material을 무리하게 한 종류로 flatten하지 않는다

## output expectation

Input organ은 아래 중 일부를 반환할 수 있어야 한다.

- intake packet
- intake status
- weakness note
- fallback flag
- next lane hint

## caution

- weak/mixed/unresolved 입력은 residue처럼 남긴다
- fallback은 실패가 아니라 caution carry다
- line-only worldview로 재료를 축소하지 않는다
- source/context/provenance를 handoff에서 잃지 않는다

## final sentence

Input organ은 자료를 업로드받는 창이 아니라,  
source와 context와 split과 약함까지 보존해 후속 기관이 읽을 수 있는 intake packet을 만드는 전단 기관이다.
