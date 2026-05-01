# Scriptable Unit Candidate Discovery Note (v0)

## 개요
Package 023에서는 기존의 'Small Execution Unit' 개념을 보다 구체적이고 도구 중심적인 'Scriptable Unit'으로 재정의하고, 현재의 패키지 루프 내에서 자동화 가능한 새로운 후보군을 관찰했습니다.

## 1. 기존 도구의 재조망: `package_metadata_scan.sh`
현재 유일하게 구현된 `package_metadata_scan.sh`는 'Scriptable Unit'의 전형적인 사례로 평가됩니다.

- **역할:** 패키지 내 파일 구조 및 헤더 정보를 수집하여 리뷰어의 '어포던스(Affordance)'를 돕는 발견 도구.
- **성격:** 무상태성(Stateless), 한정된 범위(Bounded), 낮은 위험도(Low-risk).
- **효과:** 수동 파일 목록 조회 및 헤더 독해의 반복적 병목을 해결함.

## 2. 신규 Scriptable Unit 후보 발굴 (Observed Candidates)

패키지 001~022의 역사적 맥락을 분석한 결과, 다음과 같은 반복적 수동 작업 지점이 'Scriptable Unit' 후보로 식별되었습니다.

### A. `package_brief_template.sh` (브리프 생성 보조)
- **병목:** 매 패키지 시작 시 `package_brief.md`를 처음부터 작성하거나 이전 파일을 복사/수정하는 수동 작업.
- **역할:** 패키지 번호, 이름, 표준 섹션(Purpose, Boundaries, Review Questions)을 포함한 최소한의 스켈레톤 마크다운 생성.
- **위험도:** Low. (내용을 결정하는 것이 아니라 틀만 제공)

### B. `session_artifact_collector.sh` (세션 결과 수집 보조)
- **병목:** 여러 세션 폴더(session_01, 02...)에 흩어진 `gemini_packet.md`나 `handoff_log.md`를 패키지 루트의 `codex_review_bundle.md` 등으로 모으는 작업.
- **역할:** 세션별 주요 아티팩트를 패키지 루트로 복사하거나 요약 목록을 생성함.
- **위험도:** Medium. (수집 대상 선택 시 판단 개입 위험)

### C. `user_summary_signal_extractor.sh` (피드백 신호 추출 보조)
- **병목:** 패키지 종료 시 `raw/`, `stderr/`, `outbox/` 파일들로부터 에러나 특정 키워드를 찾아 `user_summary.md`에 반영할 신호를 수집하는 작업.
- **역할:** 에러 로그나 모델 재시도 메시지 등 '반복되는 수동 검색 패턴'을 텍스트로 추출함.
- **위험도:** Medium. (분류 및 판단이 포함될 경우 Tone Guard 준수 필요)

## 3. Scriptable Unit의 핵심 정의 (Provisional Definition)
관찰 결과를 바탕으로 정의한 Scriptable Unit은 다음과 같은 특성을 가집니다.

- **Single-Purpose:** 하나의 구체적인 수동 병목을 해결한다.
- **Input-Bounded:** 하나의 패키지 디렉토리만 입력으로 받는다.
- **Discovery-First:** 판단(Judgment)을 내리기보다, 판단을 돕는 재료(Signal/Affordance)를 제공한다.
- **Linear Trace:** 실행 과정이 투명하게 드러난다.

## 4. 잠정적 권장 (Provisional Recommendation)
현재 가장 유망한 후보는 **`package_brief_template.sh`**입니다. 이는 구현 난이도가 낮으면서도 패키지 생성의 일관성을 높이고 초기 병목을 줄여주는 '손잡이' 역할을 충실히 수행할 수 있을 것으로 추정됩니다.
