## 11. repo-wide read / gemini-only write rule

이 섹션은 Gemini CLI를 사용할 때의 추가 고정 규칙이다.

핵심 원칙은 아래 두 줄이다.

- **읽기는 repo 전체 가능**
- **쓰기는 `gemini/` 폴더 내부만 가능**

즉 Gemini CLI는 엔진 전체를 읽고 분석할 수는 있지만,
어떤 경우에도 `gemini/` 폴더 바깥 파일을 생성/수정/삭제하면 안 된다.

### 11.1 read scope
Gemini CLI는 아래 목적에 한해 repo 전체를 읽을 수 있다.

- 전체 폴더 트리 파악
- 상위 구조 분류
- 스크립트 목록 수집
- 스크립트 역할 분류
- 파일 간 연결 관계 추정
- 보고서/계약/정책/기준선/실행 entrypoint 파악
- 최근 작업 흐름 복원
- 점검/검토/비교를 위한 근거 수집

허용:
- repo 전체 파일 read
- 폴더 구조 탐색
- 스크립트 목록 정리
- 파일 경로 인용
- 분석 리포트 작성용 내용 수집

### 11.2 write scope
Gemini CLI가 파일을 써도 되는 유일한 위치는 `gemini/` 폴더 내부다.

예시:
- `gemini/reports/`
- `gemini/inventories/`
- `gemini/briefs/`
- `gemini/checklists/`
- `gemini/tmp/`

주의:
- 위 경로는 예시이며, 실제 생성/정리는 User 또는 Codex 승인 흐름에 따른다.
- 어떤 경우에도 `gemini/` 바깥 파일 touch 금지

절대 금지:
- `app/` 수정
- `scripts/` 수정
- `runtime/` 수정
- `docs/` 수정
- `source_assets/` 수정
- `inputs/` 수정
- `references/` 수정
- 기준선/정책/계약/기록 파일 수정
- repo 루트 파일 수정
- 기존 파일 overwrite
- 자동 patch 적용

## 12. repo inventory / tree / script analysis mode

Gemini CLI는 아래와 같은 **read-only 전역 분석 모드**로 사용할 수 있다.

목적:
- 전체 폴더 구조를 읽는다
- 폴더 트리를 만든다
- 스크립트 목록을 만든다
- 스크립트 역할/entrypoint/입출력 대상을 분류한다
- 엔진 흐름을 사람이 빨리 파악할 수 있게 요약한다

### 12.1 허용 출력물
Gemini CLI는 아래 산출물을 만들 수 있다.
단, 모두 `gemini/` 폴더 내부에만 기록한다.

- 전체 폴더 트리 문서
- 상위 폴더 역할 요약
- 스크립트 inventory
- 실행 entrypoint 리스트
- 스크립트별 역할 분류표
- 위험 수정 가능 경로 표시
- read-only 브리핑 문서
- 점검 checklist
- 구조 설명문
- 추정 흐름도용 텍스트 요약

### 12.2 금지 출력물
Gemini CLI는 아래를 만들면 안 된다.

- repo 본체를 바꾸는 patch
- 구조 개편 제안 초안
- 기준선 교체안
- 정책 overwrite 문안
- 자동 수정 스크립트
- 수정 실행 명령
- 코어 rewrite 제안

### 12.3 권장 inventory 형식
가능하면 아래 형식으로 출력한다.

- 상위 폴더 트리
- 폴더별 역할 요약
- 핵심 스크립트 리스트
- 스크립트별 입력 / 출력 / 의존 경로
- 실행 entrypoint 후보
- 점검 필요 경로
- 수정 금지 핵심 경로
- 불확실한 연결 지점

## 13. gemini analysis-only dispatch rule

Gemini CLI에 전역 분석을 맡길 때는 아래 원칙을 같이 준다.

- 너는 수정자가 아니라 read-only 분석기다
- repo 전체를 읽어도 된다
- 그러나 `gemini/` 폴더 바깥은 절대 수정하지 마라
- 결과는 요약/비교/점검/리스트 형태로만 내라
- 구조 개조 제안은 강하게 하지 마라
- 확정 판단 대신 후보/의심/점검 포인트 형태를 우선하라
- 가능하면 근거 경로를 함께 적어라
- 불확실하면 불확실하다고 적어라

## 14. global scan task template

Gemini CLI에 전체 폴더 분석을 맡길 때 아래 템플릿을 기본 패턴으로 쓴다.

### 목적
- repo 전체를 read-only로 스캔
- 폴더 트리 생성
- 스크립트 inventory 생성
- 스크립트 역할 분석
- 실행 흐름 추정
- 수정 금지 핵심 경로 표시

### 절대 규칙
- `gemini/` 폴더 이외 수정 금지
- 가능하면 결과도 `gemini/` 내부 보고서로만 남길 것
- repo 바깥/코어 파일 touch 금지
- 확정적 구조 변경 제안 금지

### 기본 출력 형식
- 전체 폴더 트리
- 상위 폴더 역할 요약
- 핵심 스크립트 리스트
- 스크립트별 역할 분류
- entrypoint 후보
- 점검 포인트
- 수정 금지 핵심 경로
- 불확실성 메모

## 15. final lock for gemini repo scan mode

Gemini CLI는 **repo 전체를 읽을 수 있다.**
하지만 그것은 엔진 본체를 건드리기 위한 권한이 아니라,
**후단 분석/점검/리스트업을 위한 읽기 권한**이다.

최종 잠금:

- **읽기 범위 = repo 전체**
- **쓰기 범위 = `gemini/` 폴더 내부만**
- **역할 = 분석 / 점검 / 요약 / 리스트업**
- **엔진 본체 수정 권한 = 없음**