# code_reference_asset_schema_v1

## 1. 목적
이 계약은 코드/패치/설계 초안이 공간 안에서 단순 파일이 아니라 reference asset 으로 읽히도록 최소 필드를 고정한다.

## 2. 필수 필드
- `reference_id`
- `source_type`
- `purpose`
- `problem_context`
- `linked_company_flow_or_anchor`
- `related_docs`
- `related_runs`
- `change_reason`
- `result_status`
- `file_paths`
- `created_at`
- `updated_at`

## 3. 권장 필드
- `summary`
- `owner`
- `namespace`
- `confidence`
- `notes`
- `supersedes`
- `derived_from_reference`
- `review_receipt`

## 4. enum 가이드
- `source_type`
  - `chatgpt`
  - `gemini`
  - `codex`
  - `manual`
  - `imported_repo`
- `result_status`
  - `draft`
  - `tested`
  - `applied`
  - `superseded`
  - `discarded`

## 5. JSON 예시
```json
{
  "reference_id": "code_ref_picklist_ui_v1",
  "source_type": "codex",
  "purpose": "warehouse picking support sub-app",
  "problem_context": "existing picking flow hides hold/recheck loop",
  "linked_company_flow_or_anchor": ["picking", "hold_loop", "recheck"],
  "related_docs": ["docs/reports/example.md"],
  "related_runs": ["run_20260325_001"],
  "change_reason": "surface hold causes before dispatch confirmation",
  "result_status": "draft",
  "file_paths": ["app/runtime/example.py"],
  "created_at": "2026-03-25T12:00:00+09:00",
  "updated_at": "2026-03-25T12:00:00+09:00"
}
```

## 6. 해석 규칙
- `file_paths` 만 있고 `problem_context` 가 없으면 reference asset 으로는 불충분하다.
- `source_type` 는 출처 책임을 구분하기 위한 값이지 품질 등급이 아니다.
- `linked_company_flow_or_anchor` 는 검색/회수 포인트다.

## 7. 저장 위치 제안
- manifest:
  - `runtime/manifests/code_reference_assets_v1.json`
- optional payload/body:
  - `runtime/source_documents/code_reference_assets/`

## 8. 잠금 문장
코드는 파일 자체보다 목적, 문제, 연결 앵커, 수정 이유가 함께 남을 때 비로소 공간 reference asset 이 된다.
