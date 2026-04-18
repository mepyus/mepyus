# memory_layer_separation_map_v1

## 1. 목적
이 문서는 `vectorfl_replica` 를 기억층 기준으로 읽기 위한 최소 분리 지도를 고정한다.

## 2. 분리 원칙
- raw 는 원문과 사건 원본을 보존한다.
- interpretation 은 입력기에 의해 부여된 해석 결과를 담는다.
- observation 은 질문 기반 read-only 판독 결과를 담는다.
- reference 는 재사용 가능한 코드/설계/예시 자산을 담는다.
- enrichment 는 부족한 연결을 이유와 출처와 함께 보강한 층이다.

## 3. 기억층 정의

### A. raw_input_memory
- 정의:
  - 아직 판독 결론으로 굳지 않은 원문/메모/실행 원본
- 포함 필드 예:
  - source_ref
  - captured_at
  - source_type
  - source_session
  - raw_text_pointer

### B. interpretation_memory
- 정의:
  - 입력기가 만든 축/라벨/앵커/위치값과 provenance seed
- 포함 필드 예:
  - input_ref
  - interpreter_version
  - axis_values
  - labels
  - anchors
  - origin_map_ref
  - interpreted_at

### C. observation_memory
- 정의:
  - 질문/응결핵/관측기 기준으로 읽은 결과
- 포함 필드 예:
  - query
  - nucleus_id
  - output_ref
  - confidence
  - exceptions
  - source_pointer
  - observed_at

### D. reference_memory
- 정의:
  - 코드, 설계안, 템플릿, 예시 구현, 외부/내부 참고 자산
- 포함 필드 예:
  - reference_id
  - source_type
  - purpose
  - related_problem
  - file_paths
  - linked_anchor
  - status

### E. enrichment_memory
- 정의:
  - 약한 연결, 누락 이유, 보강 출처를 남기며 append 한 결과
- 포함 필드 예:
  - attached_to
  - gap_type
  - reason
  - source_ref
  - effect_type
  - confidence
  - enriched_at

## 4. 운영 규칙
- raw -> interpretation 으로 갈 수 있어도 raw 를 덮어쓰지 않는다.
- observation 은 raw 나 interpretation 을 정답처럼 대체하지 않는다.
- reference 는 구현 자산이지 원본 입력이 아니다.
- enrichment 는 추측/보강의 이유를 반드시 남긴다.

## 5. 현재 repo 기준 권장 배치
- raw_input_memory
  - [runtime/source_documents](/Users/sungsookim/universe/vectorfl_replica/runtime/source_documents)
  - 원본 structured doc 파일 자체
- interpretation_memory
  - [runtime/manifests/label_packets](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/label_packets)
  - [runtime/manifests/origin_maps](/Users/sungsookim/universe/vectorfl_replica/runtime/manifests/origin_maps)
  - [runtime/fragments](/Users/sungsookim/universe/vectorfl_replica/runtime/fragments)
- observation_memory
  - [runtime/measurements](/Users/sungsookim/universe/vectorfl_replica/runtime/measurements)
  - [runtime/reports](/Users/sungsookim/universe/vectorfl_replica/runtime/reports)
  - [app/work/observer_ingest_min/generated](/Users/sungsookim/universe/vectorfl_replica/app/work/observer_ingest_min/generated)
- reference_memory
  - [references](/Users/sungsookim/universe/vectorfl_replica/references)
  - future code reference registry
- enrichment_memory
  - 현재 전용 폴더 부재
  - 신규 namespace 후보: `runtime/review_ledgers/enrichment/` 또는 `runtime/manifests/enrichment/`

## 6. 현재 혼선
- `runtime/reports` 는 observation summary 와 운영 review 가 섞여 있다.
- `app/work/*/generated` 는 observation output, 실험 산출, reference 성격이 같이 존재한다.
- structured doc 원문이 root 에 놓일 때 raw input 이면서 governance 문서 역할도 함께 가진다.
- enrichment 전용 저장층이 없어 observation 과 혼합될 가능성이 높다.

## 7. 잠금 문장
기억층 분리의 핵심은 폴더 미학이 아니라, 원문과 해석과 관측과 참조와 보강이 서로 원본 행세를 하지 못하게 막는 데 있다.
