# code_reference_ingest_policy_v1

## 1. 목적
이 정책은 코드/설계 초안/패치 결과를 reference_memory 로 재투입할 때의 최소 intake 기준을 정한다.

## 2. intake 대상
- Codex가 만든 패치
- ChatGPT/Gemini가 만든 코드 초안
- 수동 작성 utility / script
- 재사용 가치가 있는 설계 문서와 구현 예시

## 3. 필수 동반 정보
- 목적
- 문제 배경
- 관련 문서
- 관련 실행 또는 run id
- 변경 이유
- 상태

## 4. intake 금지 또는 보류
- 파일만 있고 문제 맥락이 없는 경우
- 회사 민감정보가 섞였는데 경계 레벨이 표시되지 않은 경우
- 외부 코드인데 provenance 가 불명확한 경우

## 5. 운영 원칙
- code reference 는 raw input 으로 위장하지 않는다.
- code reference 는 tested/applicable 여부를 status 로 남긴다.
- 동일 목적의 반복 시도는 supersede chain 으로 연결한다.
- reference asset 은 검색 가능한 anchor/flow handle 을 가져야 한다.

## 6. 현재 repo 에서 우선 후보
- [scripts](/Users/sungsookim/universe/vectorfl_replica/scripts)
- [app/runtime](/Users/sungsookim/universe/vectorfl_replica/app/runtime)
- [app/work/*/generated](/Users/sungsookim/universe/vectorfl_replica/app/work)
- [references](/Users/sungsookim/universe/vectorfl_replica/references) 안의 예시 구현/설계 조각

## 7. 추천 저장 구조
- registry:
  - `runtime/manifests/code_reference_assets_v1.json`
- related payloads:
  - `runtime/source_documents/code_reference_assets/`

## 8. 잠금 문장
코드 reference ingest 의 핵심은 파일 수집이 아니라, 나중에 왜 이 코드를 다시 꺼내야 하는지 설명 가능한 상태로 남기는 것이다.
