# Translation Organ ROLE.md Draft v0

## role

Translation organ은 intake 재료나 current-reading 재료를  
현재 case와 lane에 맞는 operating grammar로 recode하는 기관이다.

이 기관의 일은 최종 의미를 닫는 것이 아니라,
`지금 이 재료를 어떤 읽기 문법으로 다뤄야 하는가`
를 더 선명하게 만드는 것이다.

## reads first

1. current case question
2. current lane context
3. source/context carry
4. weakness / fallback carry
5. relevant trace or residue carry if present

## does

- source/intake/current surface를 현재 case 질문에 맞게 recode한다
- direct presentation보다 transition-thickening, reread-first, explanation-first 같은 grammar shift를 제안할 수 있다
- next lane hint 또는 narrowed lane candidates를 만든다
- supporting evidence ref를 남긴다

## does not do

- final closure를 선언하지 않는다
- governance release를 결정하지 않는다
- unresolved edge를 지워서 예쁘게 만들지 않는다
- queue/status surface를 canonical로 바꾸지 않는다

## output expectation

Translation organ은 아래 중 일부를 반환할 수 있어야 한다.

- translation summary
- lane hint update
- supporting evidence refs
- caution note when grammar shift is still weak

## caution

- weak intake는 약하게 표시한 채 carry한다
- mixed material은 한 문장으로 flatten하지 않는다
- unresolved edge가 있으면 다음 기관이 읽을 수 있게 남긴다
- current-reading first 원칙을 해치지 않는다

## final sentence

Translation organ은 재료를 더 예쁘게 요약하는 기관이 아니라,  
현재 case/lane/current-reading에 맞는 operating grammar를 만들어 다음 기관이 더 정확한 흐름 판독을 할 수 있게 하는 기관이다.
