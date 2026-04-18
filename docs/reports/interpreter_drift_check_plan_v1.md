# interpreter_drift_check_plan_v1

## 1. 목적
이 계획은 같은 reference set 에 대해 입력기 변경 전후의 흔들림을 비교하는 최소 루프를 정의한다.

## 2. 비교 단위
- document level
- unit / fragment level
- label packet level
- anchor emission level
- origin/provenance seed level

## 3. 필요한 입력
- calibration reference set manifest
- interpreter version stamp
- run timestamp
- optional scenario tag

## 4. 산출물 제안
- `drift_summary_<reference_set_id>_<run_id>.md`
- `drift_diff_<reference_set_id>_<run_id>.json`
- `drift_metrics_<reference_set_id>_<run_id>.json`

## 5. 비교 항목
- label set added / removed
- anchor set added / removed
- processing profile changed / unchanged
- fragment count delta
- origin pointer stability
- noisy sections / stable sections

## 6. 최소 메트릭
- stable_label_ratio
- stable_anchor_ratio
- fragment_count_delta
- origin_pointer_change_count
- drift_hotspots

## 7. 실행 순서
1. reference set 선택
2. current interpreter version stamp 기록
3. baseline run 결과 고정
4. 변경된 interpreter rerun
5. diff 계산
6. 사람이 읽는 drift summary 작성

## 8. 주의
- drift 감소가 항상 의미 품질 향상을 뜻하지는 않는다.
- 특정 문서에서만 안정해지고 다른 문서에서 무너질 수 있다.
- drift report 는 판단 재료이지 자동 승격 기준이 아니다.

## 9. 다음 단계
- 현재 `labeler` 와 `observer_ingest_min` 산출을 기준으로 first reference set 을 만든다.
- 선언문/기준문/지시서류를 초기 calibration corpus 로 삼는다.
