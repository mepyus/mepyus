# delta_society structured intake v1

## 1. 목적

이 문서는 `inputs/external_cases/delta_society.md`가 실제 structured intake를 통과했다는 사실을 남기는 최소 기록이다.

핵심은 내용 요약이 아니라, 이 입력이 `process_structured_doc_with_routing.py`를 통해 receipt / label packet / origin map / observer ingest 흔적을 생성했다는 점이다.

## 2. 입력 자산

- [delta_society.md](/Users/sungsookim/universe/vectorfl_replica/inputs/external_cases/delta_society.md)
  - doc_id: `doc_delta_society`
  - role: `memo`
  - processing_profile: `minimal_preprocess`

## 3. 생성된 핵심 흔적

- [doc_delta_society_operation_receipt.md](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts/doc_delta_society_operation_receipt.md)
- [doc_delta_society_label_packet.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/label_packets/doc_delta_society_label_packet.json)
- [doc_delta_society_receipt_seed_origin_map.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/origin_maps/doc_delta_society_receipt_seed_origin_map.json)
- [source_manifest_delta_society_20260402_215911.json](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/generated/source_manifest_delta_society_20260402_215911.json)
- [split_units_delta_society_20260402_215911.json](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/generated/split_units_delta_society_20260402_215911.json)
- [operator_summary_delta_society_20260402_215911.md](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/generated/operator_summary_delta_society_20260402_215911.md)

## 4. 현재 상태

- `delta_society.md`는 단순 파일 존재 상태가 아니라 structured intake 완료 상태다.
- `structured_internal_docs_registry_v1.json`에 `doc_delta_society`로 등록됐다.
- receipt 기준 현재 읽기는:
  - `docrole=memo`
  - `runmode=ingest_only`
  - `priority=normal`
  - `execution_linkable=false`

## 5. 왜 이것이 중요한가

- `delta_society.md`를 이제 외부자료 입력층의 실제 intake 사례로 다시 사용할 수 있다.
- 이후 reread / first-pass / observer / provenance 계열 작업에서 이 파일을 “이미 입력기 통과한 문서”로 다룰 수 있다.
- 즉 지금 상태는 “추가 해석 전의 정식 입력 완료”다.
