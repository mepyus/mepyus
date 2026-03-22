# observer_ingest_min spec

## 1. 목적
- 입력을 쉽게 넣고
- 어떻게 나뉘었는지 바로 보고
- 처리 흔적을 최소 trace로 남기고
- 사람이 md 한 장으로 빠르게 확인할 수 있게 한다.

## 2. 현재 단계 정의
- deep linkage engine 아님
- corridor / re-entry / specificity 계산 아님
- `easy ingest + visible split + readable trace` 만 수행

## 3. 지원 모드
- direct mode
  - `--input`
  - `--label` optional
  - `--profile auto`
- registry mode
  - `--registry <json path>`

## 4. split 우선순위
- `auto`:
  1. timestamp
  2. heading
  3. paragraph

## 5. output contract 요약
- `source_manifest_<run_id>.json`
- `split_units_<run_id>.json`
- `processing_trace_<run_id>.json`
- `readable_input_board_<run_id>.md`
- `operator_summary_<run_id>.md`

## 6. trace 최소 원칙
- 무엇을 기준으로 쪼갰는지 남기면 충분
- 복잡한 내부 판단 로그는 남기지 않음

## 7. 비목표
- canonical / mixed 판독
- bridge admission
- source_local_ref 생성
- corridor/axis 분석

## 8. 성공 조건
- direct mode로 파일 하나 넣을 수 있음
- split mode가 자동 선택됨
- manifest / split_units / processing_trace / readable board / operator summary 생성
- md 두 파일만 읽어도 입력/분해/흐름을 이해 가능
