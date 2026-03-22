# Naming Convention

비교 파이프라인에서 파일명은 공통 문서 키다. `fragment_id`는 처리자 내부 로컬 id여도 된다.

## 파일명 규칙

- 문서 단위 raw 파일명: `doc_001.jsonl`
- 같은 문서는 세 처리자 폴더에서 동일한 파일명을 사용한다.

예:
- `processor_outputs/raw/codex/doc_001.jsonl`
- `processor_outputs/raw/chatgpt/doc_001.jsonl`
- `processor_outputs/raw/gemini/doc_001.jsonl`

## 내부 필드 규칙

- `input_doc_id`: `doc_001`
- `input_bundle_id`: `bundle_compare_v1`
- `fragment_id`: 처리자 내부 고유 id
- `fragment_version`: 기본 `v1`

## 중요 원칙

- 세 처리자는 같은 문서에 대해 동일한 파일명을 사용한다.
- 한 파일 안에는 해당 문서를 각 처리자가 자른 fragment들을 모두 넣는다.
- 여러 처리자 간 `fragment_id`가 일치할 필요는 없다.
- 비교기는 같은 파일명과 같은 원문 문맥 안에서 fragment_text 유사도로 후매칭한다.
