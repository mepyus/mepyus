# gemini_cli_test_validation_execution_package_v0.md

## 역할
이 문서는 Gemini CLI 테스트/검증 실행 패키지의 메인 문서다.

## 패키지 목적
Gemini CLI는 다음 목적에 사용한다.
- 빠른 테스트
- 단순 검증
- 여러 재료 목록화
- source surface 후보 분류
- 4줄 카드 초안 생성
- trial note append 보조
- batch material 분리 처리
- self-check / HOLD 후보 탐지

Gemini CLI는 다음 목적에 사용하지 않는다.
- 최종 판단
- baseline lock
- controller 구현
- schema 설계
- runtime manifest 생성
- index/microspace 자동 업데이트
- helper/code 수정
- 공간 철학 재정의
- source surface 체계 변경

## 기본 운용 흐름
```text
User/Assistant decides task
-> Codex prepares bounded Gemini instruction or package
-> Gemini reads only allowed files
-> Gemini performs test/list/validation/card draft
-> Gemini returns result in fixed return contract
-> Assistant/Codex reads Gemini result as worker_return
-> only then decide next move
```
