# observation_probe_contract_v1

## 1. 목적
이 계약은 관측기/응결핵/탐색기를 공간 본체가 아닌 detachable read-only 부품으로 고정한다.

## 2. 관측기 핵심 계약
- raw overwrite 금지
- interpretation overwrite 금지
- read-only scan only
- append-only result write
- query / nucleus / result / confidence / exception 을 기록

## 3. 입력 계약
- `observation_query`
- `nucleus_id`
- `nucleus_label`
- `scenario_domain`
- `purpose`
- `test_window`
- `input_refs`

## 4. 출력 계약
- `observation_id`
- `query`
- `nucleus_id`
- `matched_refs`
- `output_pointer`
- `confidence`
- `exceptions`
- `observed_at`
- `observer_version`

## 5. 응결핵 메타데이터
- `nucleus_id`
- `nucleus_label`
- `scenario_domain`
- `purpose`
- `attached_query`
- `test_window`
- `output_pointer`

## 6. 예외 처리
- 근거 부족 시 `low_confidence` 로 기록
- 반례가 크면 `counterexample_present` 를 남긴다
- 관측 실패도 event 로 남긴다

## 7. 현재 repo 연결점
- 관측 산출 후보:
  - [app/work/observer_ingest_min/generated](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/generated)
  - [runtime/reports](/Users/sungsookim/universe/vectorfl_replica/runtime/reports)
- 장기 observation memory 후보:
  - `runtime/measurements/observations/`

## 8. 잠금 문장
응결핵과 관측기는 “이번에 이렇게 보였다”를 append 하는 장치이지, “원래 이렇다”를 본체에 새겨 넣는 장치가 아니다.
