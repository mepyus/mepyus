# codex_baseline_vectorfl_replica_intake_and_operation_v1

## 1. 문서 목적
이 문서는 `vectorfl_replica` 를 운영할 때 Codex가 흔들리지 않고 따라야 할
**입력 / 분류 / 실행 / 기록 / 정리 기준선**을 고정하기 위한 기준문이다.

이 기준문의 목적은 아래 5개다.

1. 입력기를 좁게 잠그지 않되, 입력마다 같은 방식으로 처리하지 않도록 한다.
2. 너와 사용자 사이에서 생성된 구조화 문서를 별도 우선 재료로 다루는 기준을 고정한다.
3. 문서 원문 / 엔진 재료 / 실행 티켓 / 실행 기록 / status 문서의 역할을 분리한다.
4. Codex가 모든 작업을 예쁜 markdown 수정으로 처리하지 않고, append-only 기록 후 compaction 하는 운영 원칙을 따른다.
5. 문서, 스크립트, 폴더, 결과물까지 엔진 대상로 다루되, 혼용을 막는 최소 규칙을 세운다.

## 2. 최상위 기준선
앞으로 Codex는 아래 문장을 최상위 운영 기준으로 삼는다.

**입력은 넓게 받되 차등 처리한다.
구조화 문서는 고밀도 우선 재료로 취급한다.
실행은 작은 사건 기록으로 남긴다.
status 문서는 나중에 정리되는 압축층으로 유지한다.**

## 3. 입력 기준선

### 3.1 입력기는 넓게 연다
입력기는 특정 형식만 받는 좁은 입구가 아니다.

받을 수 있는 입력 예시는 아래를 포함한다.

- 너와 사용자 사이에서 생성된 구조화 문서
- 회사 문서 일부
- 교육 자료
- 유튜브 대화 원문
- LM Notebook 정리본
- 외부 비교 메모
- 현장 메모
- reference 자산
- 실행 결과 리포트
- status 문서
- 스크립트 / 파일 / 폴더 관련 설명 자산

즉 원칙은
**“무엇만 받는다”** 가 아니라
**“다양한 입력을 받을 수 있다”** 이다.

### 3.2 모든 입력을 같은 방식으로 처리하지 않는다
입력은 넓게 받되,
아래 4축을 먼저 읽고 처리 레인을 다르게 한다.

- 출처(source)
- 정제도(refinement level)
- 역할(role)
- 우선도(priority)

즉 입력기는 단순 수집기가 아니라
**routing-aware intake layer** 여야 한다.

## 4. 입력 분류 기준선

### 4.1 input class
모든 입력에는 최소한 `input_class` 를 붙인다.

예시:
- `structured_internal_doc`
- `execution_directive`
- `baseline_doc`
- `external_company_doc`
- `training_material`
- `youtube_transcript`
- `youtube_curated_note`
- `reference_memo`
- `runtime_output_doc`
- `status_doc`

### 4.2 processing profile
모든 입력에는 처리 프로파일을 붙인다.

예시:
- `direct_ingest`
- `minimal_preprocess`
- `light_preprocess`
- `full_preprocess`
- `reference_only`
- `execution_coupled`
- `deferred_review`

### 4.3 material grade
모든 입력에는 재료 밀도 등급을 붙인다.

예시:
- `grade_a` = 너와 사용자 사이의 구조화 문서
- `grade_b` = 사용자가 가공한 정리 노트 / curated note
- `grade_c` = 회사 문서 일부 / 교육 자료 / 잘 정리된 외부 자료
- `grade_d` = raw transcript / raw note / 잡음 높은 입력

주의:
등급은 가치 판단이 아니라
**처리 우선도와 해석 비용을 구분하는 운영 값**이다.

## 5. structured internal docs 기준선
너와 사용자 사이에서 생성된 아래 문서들은 별도 우선 재료로 취급한다.

- 선언문
- 기준문
- 정리문
- 지시서
- 설명서
- 인계문
- 구조 메모
- 판단 메모

이 문서들에는 이미 아래가 응축되어 있다.

- 의도
- 흐름
- 맥락
- 과정
- 결과
- 범위
- 제한
- 다음 행동

따라서 아래 기준을 적용한다.

### 5.1 특별 마킹
- `input_class=structured_internal_doc`
- `material_grade=grade_a`
- `engine_priority=high`

### 5.2 원문 우선 보존
원문은 덮어쓰지 않는다.

### 5.3 최소 전처리 우선
이미 구조화되어 있으므로 과도한 재분해보다
필요 최소한의 전처리와 부착만 우선한다.

### 5.4 Codex 연동 허용
이 문서는 엔진 재료이면서 동시에 실행 출발점이 될 수 있다.

## 6. 원문 / 파생물 분리 기준선
Codex는 아래 둘을 절대 혼동하지 않는다.

### 6.1 원문 문서
- 사용자가 제공하거나
- 너와 사용자가 함께 만든
의미가 응축된 원래 문서

### 6.2 파생물
원문으로부터 생성된 아래 요소들
- fragment
- sidecar
- label
- anchor
- axis summary
- ticket
- event record
- summary artifact

원문은 원문으로 남아야 하고,
파생물은 원문을 대체하면 안 된다.

즉 기본 구조는 아래다.

`원문 보존 + 파생물 부착`

## 7. 역할 분리 기준선
다음 네 가지는 절대 같은 것으로 쓰지 않는다.

### 7.1 label
이 대상이 무엇인지 붙이는 정체성/분류 값

예:
- `directive`
- `baseline`
- `engine_component`
- `script`
- `status_doc`
- `runtime_output`

### 7.2 ticket
무엇을 해야 하는지 붙이는 작업 값

예:
- `expand_folder_status`
- `create_new_script`
- `review_runtime_output`
- `attach_component_labels`

### 7.3 event record
실제로 무엇이 일어났는지 남기는 사실 값

예:
- script_created
- file_updated
- script_run
- report_generated
- ticket_closed
- status_compacted

### 7.4 status document
사람이 읽는 현재 상태 설명 문서

즉 아래처럼 고정한다.

- `label = 정체성`
- `ticket = 해야 할 일`
- `event = 일어난 일`
- `status.md = 사람이 읽는 요약 설명`

## 8. 엔진 대상 기준선
앞으로 엔진이 다루는 대상은 fragment만이 아니다.
아래 모두를 엔진 대상으로 취급할 수 있다.

- 문서
- fragment
- file
- folder
- script
- runtime output
- report
- status document
- reference asset
- label
- ticket
- event log

즉 engine space는 단순 텍스트 공간이 아니라
**운영 객체 공간**으로 본다.

## 9. 실행 기록 기준선

### 9.1 append-only first
Codex는 매번 예쁜 markdown 수정부터 하지 않는다.
실행이 발생하면 먼저 작은 기록을 남긴다.

예:
- 새 스크립트 생성
- 스크립트 실행
- 결과물 산출
- 특정 파일 수정
- 특정 폴더 대상 반영
- status 업데이트 필요 발생

### 9.2 small factual records
기록은 가능한 한 작고 사실 중심이어야 한다.

예시 필드:
- `event_id`
- `event_type`
- `timestamp`
- `actor`
- `target_ref`
- `source_doc_ref`
- `ticket_ref`
- `status`
- `notes`

### 9.3 failure also recorded
성공뿐 아니라 실패, 중단, 부분 완료도 기록한다.

이유:
실패/중간상태도 엔진 재료이기 때문이다.

## 10. status 문서 운영 기준선

### 10.1 status 문서는 즉시 운영 장부가 아니다
status.md는 매 실행마다 직접 대규모로 수정하는 장부가 아니다.

### 10.2 status 문서는 compaction 결과다
event log와 실행 흔적이 쌓인 뒤,
필요 시 사람이 읽기 좋은 구조 문서로 정리한다.

### 10.3 status 문서의 역할
- 폴더/영역의 현재 역할 설명
- 중요한 파일의 역할 설명
- 최근 중요 변화 요약
- 엔진 구성요소 이해를 위한 기준 문서

### 10.4 status 문서는 유지한다
label/ticket이 많아져도 status.md를 없애지 않는다.
label/ticket은 조회 손잡이이고,
status.md는 구조 설명 기준 문서다.

## 11. 폴더 기록 기준선
각 주요 폴더에는 실행 흔적을 남길 수 있는 작은 기록면이 필요하다.

추천 예시:
- `folder_events.jsonl`
- `folder_activity_log.jsonl`

용도 예시:
- file_created
- file_updated
- script_registered
- run_executed
- output_generated
- status_compaction_needed
- status_compacted

즉 폴더는 정적인 보관함이 아니라
**활동 흔적이 남는 엔진 기관**으로 본다.

## 12. 티켓 기준선

### 12.1 티켓은 실행용이다
티켓은 분류가 아니라 작업 추적용이다.

### 12.2 티켓은 문서에서 파생될 수 있다
구조화 문서 안에서 실행 가능한 항목이 보이면
티켓으로 분리할 수 있다.

### 12.3 티켓은 later lineage를 가져야 한다
티켓은 아래와 연결 가능해야 한다.

- source document
- affected files
- created scripts
- generated outputs
- closed events
- status compaction

즉 티켓은 고립된 task가 아니라
**문서와 결과 사이를 잇는 실행 연결자**다.

## 13. 라벨 기준선

### 13.1 라벨은 조회와 군집의 손잡이다
라벨은 작업 추적보다
정체성 / 군집 / 빠른 참조를 위해 쓴다.

### 13.2 라벨은 문서에도 붙고 결과에도 붙는다
라벨은 아래 모두에 붙을 수 있다.

- 문서
- 스크립트
- 폴더
- 결과물
- status 문서
- reference 자산

### 13.3 라벨 예시
- `structured_internal_doc`
- `engine_component`
- `script`
- `generated_output`
- `baseline`
- `reference_material`
- `status_doc`
- `needs_review`

## 14. provenance 기준선
모든 중요한 대상은 가능한 한 provenance를 가진다.

최소한 아래를 추적할 수 있어야 한다.

- 이 문서는 어디서 왔는가
- 이 티켓은 어떤 문서에서 나왔는가
- 이 파일은 어떤 실행으로 생성되었는가
- 이 결과물은 어떤 스크립트 run에서 나왔는가
- 이 status 반영은 어떤 이벤트들을 압축한 것인가

즉 provenance는 선택이 아니라
장기 숙성을 위한 핵심 기준이다.

## 15. Codex 작업 흐름 기준선
문서가 들어오면 Codex는 기본적으로 아래 순서를 따른다.

### 15.1 receive
문서 원문을 수신한다.

### 15.2 mark
문서 역할 / 입력 클래스 / 재료 등급 / 처리 프로파일을 마킹한다.

### 15.3 preserve
원문을 보존한다.

### 15.4 ingest
엔진 재료로 저장 가능한 형태를 만든다.

### 15.5 derive tickets
실행 가능한 내용을 티켓으로 분리한다.

### 15.6 execute
필요한 코드/문서/스크립트 작업을 수행한다.

### 15.7 record events
실행 결과를 append-only로 기록한다.

### 15.8 attach metadata
생성/수정된 대상에 label / ticket / provenance 를 부착한다.

### 15.9 compact later
필요 시 status 문서나 요약 문서로 정리한다.

## 16. 금지 기준선

### 금지 1
구조화 문서를 단순 일회성 프롬프트로 취급하는 것

### 금지 2
모든 입력을 동일한 강도로 전처리하는 것

### 금지 3
label을 ticket처럼 쓰는 것

### 금지 4
ticket을 label처럼 쓰는 것

### 금지 5
event log 없이 바로 status.md만 예쁘게 수정하는 것

### 금지 6
원문을 파생물로 덮어쓰는 것

### 금지 7
결과물/스크립트/폴더를 엔진 바깥 부산물처럼 취급하는 것

## 17. 최소 성공 조건
이 기준선이 제대로 적용되려면 최소한 아래가 가능해야 한다.

1. 구조화 문서가 high-grade material 로 마킹된다.
2. 외부 자료도 입력기로 받을 수 있다.
3. 문서 / 티켓 / 실행 / 결과 / status 사이의 경로를 추적할 수 있다.
4. Codex가 매번 status.md를 직접 대수술하지 않고 작은 기록을 남긴다.
5. 라벨과 티켓으로 빠르게 대상을 조회할 수 있다.
6. 필요할 때 status.md를 열어 구조를 확인할 수 있다.

## 18. 최종 기준선 요약
앞으로 Codex는 `vectorfl_replica` 를 아래처럼 운영한다.

- 입력은 넓게 받는다.
- 입력마다 클래스와 처리 프로파일을 다르게 준다.
- 구조화 문서는 high-grade 우선 재료로 본다.
- 원문과 파생물을 분리한다.
- label / ticket / event / status 역할을 분리한다.
- 실행은 append-only 기록으로 먼저 남긴다.
- status 문서는 나중에 compaction 한다.
- 문서, 스크립트, 폴더, 결과물을 모두 엔진 대상으로 본다.
- provenance를 가능한 한 유지한다.

## 19. 마지막 한 줄
Codex는 앞으로
**입력을 좁게 막지 말고, 넓게 받되 다르게 처리하라.
문서는 원문으로 보존하고, 실행은 작은 기록으로 남기고, status는 나중에 정리하라.**
