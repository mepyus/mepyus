# Document Fragment Sheet Template

문서 하나를 비교 실험에 넣기 전에 아래 시트로 원문 메타만 고정한다.
fragment 절단은 기본적으로 각 처리자가 스스로 수행한다.

## 문서 메타

- input_doc_id: `doc_001`
- input_bundle_id: `bundle_compare_v1`
- source_type: `planning_note`
- fragment_version: `v1`

## Source Text

`여기에 원문 전체를 넣거나 source_docs 경로를 적는다`

## 체크 규칙

- 세 처리자는 같은 원문과 같은 입력 메타를 사용해야 한다.
- fragment 절단은 처리자 자율이지만 원문 바깥 내용을 추가하면 안 된다.
- 비교기는 후매칭으로 유사 fragment를 다시 맞춘다.
