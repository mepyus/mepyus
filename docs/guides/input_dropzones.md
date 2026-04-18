# input_dropzones

이 문서는 앞으로 입력 파일을 어디에 둘지 빠르게 확인하는 운영 가이드다.

## 기본 원칙
- raw 입력은 `inputs/` 아래에 둔다.
- 해석 결과는 `docs/`와 `runtime/`에 남긴다.
- 루트는 가능한 한 source 자산과 운영 핵심 파일만 남기고, 새 입력 적재함으로 쓰지 않는다.

## 어디에 넣나

### 외부 원문
- 위치: [inputs/external_cases](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases)
- 예:
  - 외부 강연 transcript
  - 회사/제품 사례 txt
  - 외부 기술 설명 raw text

### 내부 메모 / 초안
- 위치: [inputs/internal_notes](/Users/sungsookim/universe/vectorfl_replica/inputs/internal_notes)
- 예:
  - 생각 조각
  - 임시 메모
  - 빠른 정리 초안

### 구조화된 참고 문서
- 위치: [inputs/reference_docs](/Users/sungsookim/universe/vectorfl_replica/inputs/reference_docs)
- 예:
  - 보조 정리본
  - 참고용 structured note
  - 별도 reference asset 후보

## 운영 흐름
1. 입력 파일을 `inputs/` 아래 적절한 위치에 둔다.
2. Codex가 canonical source로 읽는다.
3. source asset, examples, observer, contracts, receipts로 분리 기록한다.
4. folder inventory와 status를 sync한다.

## note
- 기존에 루트에 있는 source 파일은 과거 기록을 위해 그대로 둘 수 있다.
- 새로 추가하는 입력은 기본적으로 `inputs/` 아래에 두는 것을 권장한다.
