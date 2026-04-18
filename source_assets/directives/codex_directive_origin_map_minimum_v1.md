[[A]] [[DOCROLE:directive]] [[RUNMODE:ingest_then_execute]] [[PRIORITY:high]]

# codex_directive_origin_map_minimum_v1

## 0. 목적
이번 작업의 목적은 원본 보관층과 파생 운영층을 분리한 상태에서,
파생물(fragment / summary / receipt 후보 등)이
나중에 원본의 어느 위치에서 왔는지 다시 복귀할 수 있도록
**origin map 최소 좌표를 가볍게 도입**하는 것이다.

중요:
- origin map은 원본 전체를 다시 저장하는 구조가 아니다.
- origin map은 원본 복귀용 최소 provenance 손잡이다.
- 입력층을 무겁게 만들지 않는다.
- 사용자가 입력 시 모든 필드를 수동으로 채우게 하지 않는다.

## 1. 이번 턴의 고정 기준
1. `RUNMODE`가 없으면 기본은 `ingest_only`다.
2. 모든 문서에 full flow를 적용하지 않는다.
3. origin map은 "입력 순간 필수 수동 입력"이 아니라 "파생 시점 자동 부착"으로 본다.
4. 원본은 archive / source layer에 두고, 운영은 경량 파생물 중심으로 처리한다.
5. 이번 턴에서는 receipt/board UI 강화까지 가지 않는다.

## 2. 이번 턴 범위
이번 턴에서 할 일은 아래 3개만 한다.
- STEP 1. origin map 최소 스펙 문서 고정
- STEP 2. 파생 시점 자동 부착 helper / mapper 추가
- STEP 3. 샘플 산출물과 최소 검증 추가

## 3. origin map 최소 필드 v1
필수 필드:
- `source_doc_id`
- `heading_path`
- `source_locator`
- `source_preview`
- `derived_at`
- `derived_from_kind`

세부 규칙:
1. `source_doc_id` 는 원본 문서 안정 식별자
2. `heading_path` 는 원본 내부 섹션 경로
3. `source_locator` 는 `block_id` 또는 `char_span(start,end)` 중 하나면 통과
4. `source_preview` 는 사람 검증용 짧은 미리보기
5. `derived_at` 는 파생 시점 timestamp
6. `derived_from_kind` 는 `fragment / summary / receipt_seed / ticket_seed` 등

## 4. 실행 전 점검
실행 하기전에 점검 및 분석 후 실행한다.
문제가 없다면 `RUNMODE=ingest_then_execute`, `DOCROLE=directive` 로 처리한다.
