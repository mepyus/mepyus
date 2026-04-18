# existing_assets_to_memory_layers_map_v1

## 1. 목적
이 문서는 현재 저장소 자산을 기억층 기준으로 우선 매핑한 첫 버전이다.

## 2. 매핑

### raw_input_memory
- [codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md](/Users/sungsookim/universe/vectorfl_replica/codex_directive_vectorfl_engine_lock_preset_setup_bundle_v1.md)
- [vectorfl_replica_space_natural_aging_input_consistency_memory_first_declaration_v1.md](/Users/sungsookim/universe/vectorfl_replica/vectorfl_replica_space_natural_aging_input_consistency_memory_first_declaration_v1.md)
- root structured docs generally
- [runtime/source_documents](/Users/sungsookim/universe/vectorfl_replica/runtime/source_documents)

### interpretation_memory
- [runtime/manifests/label_packets](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/label_packets)
- [runtime/manifests/origin_maps](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/origin_maps)
- [runtime/manifests/structured_internal_docs_registry_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/structured_internal_docs_registry_v1.json)
- [app/input_layer](/Users/sungsookim/universe/vectorfl_replica/app/input_layer)

### observation_memory
- [app/work/observer_ingest_min/generated](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/generated)
- [runtime/reports](/Users/sungsookim/universe/vectorfl_replica/runtime/reports)
- [runtime/measurements](/Users/sungsookim/universe/vectorfl_replica/runtime/measurements)
- [runtime/views/operation_board_latest.md](/Users/sungsookim/universe/vectorfl_replica/runtime/views/operation_board_latest.md)

### reference_memory
- [references](/Users/sungsookim/universe/vectorfl_replica/references)
- [docs/templates](/Users/sungsookim/universe/vectorfl_replica/docs/templates)
- [docs/prompts](/Users/sungsookim/universe/vectorfl_replica/docs/prompts)
- selected `app/work/*/generated` outputs that become reusable design/code examples

### enrichment_memory
- current explicit home: none
- nearest placeholders:
  - [runtime/review_ledgers](/Users/sungsookim/universe/vectorfl_replica/runtime/review_ledgers)
  - [runtime/logs/corrections](/Users/sungsookim/universe/vectorfl_replica/runtime/logs/corrections)

## 3. 혼선 구간
- [runtime/manifests/provenance_link_index_v1.json](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/provenance_link_index_v1.json)
  - interpretation provenance 이면서 운영 연결 ledger 역할도 수행
- [runtime/receipts](/Users/sungsookim/universe/vectorfl_replica/runtime/receipts)
  - operation summary 이자 observation-like trace
- [app/work](/Users/sungsookim/universe/vectorfl_replica/app/work)
  - 실험, spec, generated, reference 가 섞여 있음
- [runtime/views](/Users/sungsookim/universe/vectorfl_replica/runtime/views)
  - current operation surface 이지만 일부는 관측/운영 summary 혼합

## 4. 최소 정리 방향
- provenance index 는 interpretation-provenance 로 명시하고 operation links 와 구분한다.
- receipts 는 operation memory 로 읽되 observation_memory 와 직접 혼동하지 않게 한다.
- enrichment 전용 위치를 새로 만든다.
- code reference asset 은 reference_memory 로 별도 등록한다.

## 5. 결론
현재 저장소는 이미 기억층의 씨앗을 갖고 있지만, observation/reference/enrichment 분리가 아직 약하다. 이번 셋업의 핵심은 새 폴더를 무조건 늘리는 것이 아니라 역할 명칭을 먼저 잠그는 데 있다.
