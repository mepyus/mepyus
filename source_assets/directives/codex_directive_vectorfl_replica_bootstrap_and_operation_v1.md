# codex_directive_vectorfl_replica_bootstrap_and_operation_v1

## 1. 문서 목적
이번 작업의 목적은 `vectorfl_replica` 를 즉시 대규모 재설계하는 것이 아니다.

목표는 아래 4개다.

1. `vectorfl_replica` 전체를 하나의 엔진 작업공간으로 읽을 수 있도록 최소 운영 골격을 세운다.
2. 구조화 문서 / 외부 입력 / 실행 결과 / 폴더 / 스크립트가 서로 다른 역할로 다뤄지도록 최소 메타/기록 구조를 도입한다.
3. Codex의 실제 작업이 append-only 사건 기록으로 남도록 최소 ledger/event 구조를 만든다.
4. `*_status.md` 는 매번 직접 대수술하지 말고, 기록을 바탕으로 나중에 정리(compaction)할 수 있는 구조로 전환한다.

즉 이번 턴은
**정교한 완성**이 아니라
**혼용을 줄이는 최소 운영 골격의 설치**가 목적이다.

## 2. 이번 턴의 최우선 원칙
Codex는 이번 작업에서 아래 원칙을 반드시 지킨다.

### 2.1 원문 우선
문서 원문은 덮어쓰지 않는다.

### 2.2 append-only first
무언가 실행되면 먼저 작은 사건 기록을 남긴다.

### 2.3 status direct-edit 최소화
매 실행마다 status 문서를 크게 고치지 않는다.

### 2.4 역할 혼용 금지
label / ticket / event / status 역할을 섞지 않는다.

### 2.5 과도한 전면 개편 금지
이번 턴은 큰 리팩터링보다
**최소 운영 구조를 추가하는 방향**으로 간다.

## 3. 이번 턴 산출물 목표
이번 턴에서 Codex가 만들어야 할 산출물은 최소 아래 범주를 포함한다.

### A. 상위 운영 문서
- 이번 선언문/기준문/지시서를 저장하고 참조 가능한 위치에 배치
- 문서 역할이 드러나는 간단한 index 또는 pointer 보강

### B. 이벤트/활동 기록 구조
- append-only ledger/event 기록 파일 또는 폴더 구조
- 최소 이벤트 스키마 정의
- 폴더 단위 활동 기록 경로 마련

### C. 입력 분류 골격
- input class / processing profile / material grade / provenance 를 담을 최소 구조
- 문서형 입력의 메타 sidecar 또는 registry 골격

### D. status 운영 전환
- 각 폴더 status 문서를 “즉시 운영 장부”가 아니라 “정리 문서”로 볼 수 있도록
  기록 반영 전략 추가
- status 반영 후보를 나중에 compaction 가능한 형태로 남길 수 있는 연결점 마련

### E. 최소 추적성
- 어떤 문서가 어떤 실행 티켓/사건/결과와 연결되는지 추적 가능한 최소 연결 구조

## 4. 이번 턴에서 건드릴 핵심 대상
이번 턴에서 Codex가 우선적으로 점검/작성해야 할 대상은 아래다.

### 4.1 문서 계층
- 선언문 / 기준문 / 지시서 저장 위치
- 구조화 문서의 역할 분류 위치
- later provenance 연결 가능 위치

### 4.2 status 계층
- 루트 또는 주요 폴더의 `*_status.md`
- status가 설명층이라는 점을 명시할 보강 위치
- status에 즉시 대량 반영 대신 “최근 이벤트/반영 대기”를 가리킬 연결 지점

### 4.3 scripts / runtime / references / app
이 4개는 엔진 구성요소로 다시 읽어야 한다.
각 폴더에 대해 최소한 아래 질문에 답할 수 있어야 한다.

- 이 폴더는 엔진에서 무슨 역할인가?
- 이 폴더 아래 활동은 어떤 ledger에 남아야 하는가?
- 생성/수정/실행 사건을 어떤 식으로 기록할 것인가?

## 5. 반드시 도입할 최소 개념
Codex는 이번 턴에서 아래 개념을 코드/문서/구조 중 적절한 위치에 최소 도입한다.

### 5.1 input class
예:
- structured_internal_doc
- execution_directive
- baseline_doc
- external_company_doc
- training_material
- youtube_transcript
- youtube_curated_note
- reference_memo
- runtime_output_doc
- status_doc

### 5.2 processing profile
예:
- direct_ingest
- minimal_preprocess
- light_preprocess
- full_preprocess
- reference_only
- execution_coupled
- deferred_review

### 5.3 material grade
예:
- grade_a
- grade_b
- grade_c
- grade_d

### 5.4 event type
최소 예:
- doc_registered
- ticket_created
- file_created
- file_updated
- script_registered
- script_run
- output_generated
- run_failed
- status_compaction_needed
- status_compacted

### 5.5 provenance link
최소 예:
- source_doc_ref
- ticket_ref
- target_ref
- output_ref
- derived_from

주의:
이번 턴의 목적은 모든 enum을 완벽히 잠그는 것이 아니라,
**혼용을 막는 최소 슬롯을 만드는 것**이다.

## 6. 작업 방식: 큰 문서 수정 대신 작은 기록
Codex는 앞으로 아래 철학을 적용한다.

### 잘못된 방식
- 작업할 때마다 `status.md` 를 직접 예쁘게 대규모 수정
- 실행 흔적이 문서에만 녹아들고 원시 사건 기록이 남지 않음

### 이번에 도입할 방식
- 작업 발생
- 작은 사건 기록 append
- 필요 시 대상 메타(label/ticket/provenance) 부착
- 나중에 status 문서로 압축

즉 구조는 아래다.

`작업 -> event log -> 필요 시 메타 부착 -> 나중 compaction -> status 반영`

## 7. 이번 턴의 실작업 지시

## Phase 1. 현재 구조 스캔 및 최소 분류 표면 설치
### 목적
현재 저장소의 주요 폴더를 엔진 구성요소로 다시 읽기 위한 최소 표면 확보

### 할 일
1. `app/`, `scripts/`, 루트 `runtime/`, `references/` 를 최우선 핵심 엔진 구성요소로 고정한다.
2. 각 핵심 폴더에 대해 현재 status 문서 존재 여부와 상태를 점검한다.
3. 각 폴더의 status 문서 또는 별도 메모에 아래를 명시할 수 있도록 준비한다.
   - folder role
   - expected event types
   - key files or subareas
   - compaction target 여부

### 산출 기대
- 주요 폴더별 역할이 흔들리지 않는 최소 분류면
- “이 폴더는 엔진의 어떤 기관인가”가 드러나는 기준점

## Phase 2. 이벤트 기록 골격 도입
### 목적
실행/생성/수정/산출을 append-only로 남길 수 있는 최소 ledger 구조 설치

### 할 일
1. 루트 또는 적절한 운영 위치에 event ledger 저장 위치를 정한다.
2. 폴더 단위 활동 기록이 가능한 구조를 정한다.
3. 최소 이벤트 스키마를 문서화하거나 코드상 구조로 명시한다.
4. 적어도 아래 유형을 남길 수 있는 형태를 만든다.
   - file created
   - file updated
   - script registered
   - script run
   - output generated
   - status compaction needed
   - status compacted

### 최소 이벤트 필드 예시
- event_id
- event_type
- timestamp
- actor
- target_ref
- source_doc_ref
- ticket_ref
- status
- notes

### 주의
- 지금 단계에서 UI나 복잡한 분석기 만들지 말 것
- 먼저 기록 자체가 남도록 할 것

## Phase 3. 문서 입력 메타 골격 도입
### 목적
문서를 엔진 핵심 재료로 저장할 때 최소 class/profile/grade/provenance를 붙일 수 있도록 함

### 할 일
1. 구조화 문서 전용 최소 메타 구조를 만든다.
2. 아래 필드를 최소 수용하도록 한다.
   - doc_id
   - input_class
   - processing_profile
   - material_grade
   - source_session or source_ref
   - role
   - derived_from
   - execution_linkable
3. structured internal docs 를 별도 high-grade 처리할 수 있는 표시를 마련한다.

### 특별 규칙
너와 사용자 사이의 선언문/기준문/지시서/정리문은 기본적으로 아래 값이 들어갈 수 있어야 한다.
- input_class=structured_internal_doc
- material_grade=grade_a
- processing_profile=minimal_preprocess 또는 execution_coupled
- execution_linkable=yes

## Phase 4. 티켓/라벨/이벤트 역할 분리 표면 도입
### 목적
혼용을 막기 위한 최소 구획 설치

### 할 일
1. label의 역할을 “정체성/조회용”으로 고정한다.
2. ticket의 역할을 “실행/추적용”으로 고정한다.
3. event는 “실제 발생 사실 기록”으로 고정한다.
4. status 문서는 “설명/압축층”으로 고정한다.
5. 이 구분이 흔들리지 않도록 기준 메모 또는 status 문서에 분명히 적는다.

### 최소 예시
- label: engine_component, script, status_doc, baseline, directive
- ticket: expand_folder_status, register_script_events, attach_doc_metadata
- event: script_run, file_created, output_generated, status_compacted

## Phase 5. status 운영 방식 전환
### 목적
status 문서를 실시간 로그가 아니라 compaction 결과로 전환

### 할 일
1. 각 주요 폴더 status 문서에 아래 성격을 분명히 한다.
   - 구조 설명 문서
   - 중요 파일 설명 문서
   - 최근 중요 변화 요약 문서
2. 매 실행마다 직접 대수술하지 않고, “이벤트가 충분히 쌓였을 때 정리”한다는 운영 원칙을 기록한다.
3. status에 아래 성격의 섹션을 둘 수 있는지 검토한다.
   - recent important changes
   - compaction note
   - last summarized event range
4. 가능하면 status와 event ledger 사이의 연결점을 남긴다.

### 주의
- 이번 턴에서 모든 status를 완벽하게 정리하려고 하지 말 것
- compaction 가능한 구조만 먼저 깔 것

## Phase 6. 최소 문서 -> 실행 -> 결과 추적선 설치
### 목적
문서가 실행으로 이어지고 결과가 다시 추적될 수 있도록 최소 lineage 확보

### 할 일
1. 문서에서 파생된 티켓을 추적 가능하게 한다.
2. 티켓이 생성한 파일/스크립트/결과물을 추적 가능하게 한다.
3. 결과물에 source_doc_ref / ticket_ref / derived_from 같은 최소 provenance를 붙일 수 있는 자리를 만든다.
4. 나중에 아래 질문에 답할 수 있게 한다.
   - 이 결과는 어떤 문서에서 시작되었는가?
   - 이 파일은 어떤 티켓으로 생성되었는가?
   - 이 status 반영은 어떤 이벤트들을 요약한 것인가?

## 8. 이번 턴의 우선순위
Codex는 아래 우선순위를 따른다.

### 우선순위 1
작은 event 기록 구조 설치

### 우선순위 2
structured internal docs 메타 골격 설치

### 우선순위 3
label / ticket / event / status 역할 분리 문서화

### 우선순위 4
주요 폴더 status 문서에 compaction 운영 원칙 반영

### 우선순위 5
문서 -> 티켓 -> 결과 추적선 최소 설치

주의:
모든 것을 한 번에 완성하려고 하지 말고,
**기록이 먼저 남는 구조**를 가장 먼저 만든다.

## 9. 하지 말아야 할 것
이번 턴에서 Codex는 아래를 하지 않는다.

1. 저장소 전체 대규모 리팩터링
2. 모든 status 문서 전면 재작성
3. 완전한 온톨로지 설계 고정
4. 모든 입력 타입의 완벽한 처리기 구현
5. label/ticket/event/status를 한 파일에 뒤섞는 방식
6. 원문 문서를 파생물로 덮어쓰기
7. event 기록 없이 결과만 남기기

## 10. 결과 보고 방식
이번 턴 종료 시 Codex는 아래 형식으로 보고 가능해야 한다.

### A. 무엇을 추가했는가
- event ledger 관련 구조
- 문서 메타 관련 구조
- status compaction 관련 보강
- provenance 연결점

### B. 어디에 추가했는가
- 파일/폴더 경로
- 새 파일인지 수정 파일인지

### C. 왜 그 위치에 두었는가
- 엔진 구조상 의미
- later expansion 가능성

### D. 다음 단계는 무엇인가
- 아직 미완성인 부분
- 다음 compaction 필요 영역
- 후속 설계 필요 포인트

## 11. 성공 조건
이번 지시서 작업이 성공한 것으로 보려면 최소한 아래가 성립해야 한다.

1. `vectorfl_replica` 의 주요 폴더를 엔진 구성요소로 읽는 표면이 생긴다.
2. 문서/실행/결과를 잇는 append-only 사건 기록의 최소 구조가 생긴다.
3. 구조화 문서를 high-grade material 로 별도 취급할 수 있는 메타 구조가 생긴다.
4. label / ticket / event / status 역할 분리가 문서상/구조상 드러난다.
5. status 문서가 즉시 운영 장부가 아니라 나중 compaction 결과라는 방향이 반영된다.
6. 나중에 문서 -> 티켓 -> 파일/스크립트/결과 추적이 가능해질 최소 provenance 자리가 생긴다.

## 12. 마지막 지시
Codex는 이번 턴에서
**“완벽한 체계”를 만들려고 하지 말고,
문서 재료와 실행 사건이 섞이지 않도록 하는 최소 운영 골격을 먼저 설치하라.**

특히 아래를 잊지 말 것.

- 문서는 먼저 재료다.
- 실행은 사건이다.
- 결과는 추적 가능한 산출물이다.
- status는 사건들의 정리층이다.

그리고 모든 작업은
**예쁜 최종 문서 수정보다, 작은 사실 기록을 남기는 방향**을 우선하라.
