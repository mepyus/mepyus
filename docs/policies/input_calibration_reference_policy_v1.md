# input_calibration_reference_policy_v1

## 1. 목적
이 정책은 raw input 자유를 막지 않으면서 입력기 흔들림 점검용 calibration reference set 을 별도로 유지하는 기준을 고정한다.

## 2. 핵심 원칙
- raw input lane 은 계속 열린다.
- calibration reference set 은 입력 제한 장치가 아니다.
- calibration 은 의미를 새로 발명하는 과정이 아니라 해석 흔들림을 줄이는 점검 루프다.

## 3. calibration reference 포함 대상
- 선언문
- 기준문
- 지시서
- 정리문 / 요약문 중 의미 흐름이 잘 드러나는 문서
- 같은 입력기를 반복 시험하기 좋은 비교적 안정된 문서군

## 4. 제외 또는 후순위 대상
- 민감 회사 raw 원문 전체
- 포맷이 자주 바뀌는 임시 메모
- 외부 reference 전체 덤프
- meaning-rich 하더라도 저작권/보안 이유로 재실행이 곤란한 문서

## 5. 저장 위치 제안
- manifest
  - `runtime/manifests/calibration_reference_sets_v1.json`
- source snapshots
  - `runtime/source_documents/calibration_reference/`
- drift reports
  - `runtime/reports/calibration/`

## 6. 최소 저장 필드
- reference_set_id
- title
- doc_refs
- intended_use
- interpreter_family
- locked_at
- maintainer
- notes

## 7. 운영 규칙
- 같은 reference set 은 동일 interpreter version 에서 반복 재실행 가능해야 한다.
- 결과 비교는 accuracy claim 보다 stability claim 을 우선한다.
- reference set 수정은 append log 를 남긴다.
- calibration 결과는 raw input lane 에 gate 를 만들지 않는다.

## 8. 판정 기준
- 같은 문서에서 축/라벨/앵커 결과가 얼마나 덜 흔들리는지 본다.
- drift 는 good/bad 이분법보다 변화 설명 가능성으로 평가한다.

## 9. 잠금 문장
calibration reference 는 입력을 고르는 문턱이 아니라, 입력기가 얼마나 재현 가능하게 동작하는지 보여주는 기준 코퍼스다.
