# readable input board / segmentation_support_probe_design_v1_20260328_191115

## 1. 입력 정보
- input_id: `segmentation_support_probe_design_v1`
- label: `segmentation_support_probe_design_v1`
- source_path: `/Users/sungsookim/universe/vectorfl_replica/docs/reports/segmentation_support_probe_design_v1.md`
- input_kind: `mixed`
- detected_profile: `note`

## 2. split 결과
- split_mode_used: `heading`
- raw_line_count: `62`
- unit_count: `9`

## 3. unit 목록 요약
- unit_001 — heading_block / preamble ~ preamble — "[[A]] [[OBJ:segmentation_support_probe_design_v1]] [[SEM:minimal_segmentation_assist_design_before_pointer_and_heading]]..."
- unit_002 — heading_block / segmentation support probe design v1 ~ segmentation support probe design v1 — "# segmentation support probe design v1..."
- unit_003 — heading_block / 1. purpose ~ 1. purpose — "## 1. purpose - 이번 설계의 목적은 splitter를 다시 만드는 것이 아니다. - 목적은 `claude_code_index.txt` 같은 입력에서 single block collapse를 완화할 수 있..."
- unit_004 — heading_block / 2. baseline problem ~ 2. baseline problem — "## 2. baseline problem - 현재 기본 splitter는 `## ` heading과 빈 줄 위주로 block를 나눈다. - `claude_code_index.txt`는 긴 대화형 markdown이 아..."
- unit_005 — heading_block / 3. minimal support hypothesis ~ 3. minimal support hypothesis — "## 3. minimal support hypothesis - 현재 입력은 완전히 structureless한 텍스트가 아니다. - `타임스탬프 줄`과 `짧은 제목줄`이 이미 segmentation hint로 존재한다..."
- unit_006 — heading_block / 4. actual support applied ~ 4. actual support applied — "## 4. actual support applied - changed script: - `scripts/run_dialogue_asset_probe.py` - changed behavior: - `--segment-..."
- unit_007 — heading_block / 5. why this still counts as minimal ~ 5. why this still counts as minimal — "## 5. why this still counts as minimal - 특정 파일 전용 hardcoded heading 목록을 넣지 않았다. - `index-like transcript`라는 형식 단서만 썼다. -..."
- unit_008 — heading_block / 6. expected evaluation points ~ 6. expected evaluation points — "## 6. expected evaluation points - single block collapse가 완화되는가 - window diversity가 생기는가 - question opening / relation m..."
- unit_009 — heading_block / 7. one-line summary ~ 7. one-line summary — "## 7. one-line summary > 이번 segmentation support는 splitter 재설계가 아니라, 인덱스형 transcript에 이미 있는 `짧은 제목줄 + 타임스탬프`를 segmentati..."

## 4. 당장 읽히는 흐름
- 앞쪽은 소개/문제제기, 중간은 설명 확장, 뒤로 갈수록 주제 전환이 생기는 흐름으로 읽힌다.

