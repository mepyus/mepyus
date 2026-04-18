[[A]] [[OBJ:segmentation_support_probe_design_v1]] [[SEM:minimal_segmentation_assist_design_before_pointer_and_heading]]

# segmentation support probe design v1

## 1. purpose

- 이번 설계의 목적은 splitter를 다시 만드는 것이 아니다.
- 목적은 `claude_code_index.txt` 같은 입력에서 single block collapse를 완화할 수 있는 최소 segmentation support를 probe 단계에 얇게 추가하는 것이다.

## 2. baseline problem

- 현재 기본 splitter는 `## ` heading과 빈 줄 위주로 block를 나눈다.
- `claude_code_index.txt`는 긴 대화형 markdown이 아니라:
  - 짧은 제목줄
  - 타임스탬프 줄
  - 전사 줄
  가 반복되는 인덱스형 transcript에 가깝다.
- 그 결과 baseline에서는:
  - block_count: `1`
  - window_count: `1`
  - downstream에서 question seed / pivot / context unit이 모두 `0_0` 한 덩어리에 묶였다.

## 3. minimal support hypothesis

- 현재 입력은 완전히 structureless한 텍스트가 아니다.
- `타임스탬프 줄`과 `짧은 제목줄`이 이미 segmentation hint로 존재한다.
- 따라서 이번 최소 개입은:
  - 제목줄 + 바로 뒤 타임스탬프를 heading으로 읽고
  - 타임스탬프 줄을 block boundary hint로만 쓰는
  얇은 assist면 충분한지 보는 것이다.

## 4. actual support applied

- changed script:
  - `scripts/run_dialogue_asset_probe.py`
- changed behavior:
  - `--segment-assist index_support` 옵션 추가
  - `^\d{1,2}:\d{2}$` 형태의 타임스탬프는 block boundary hint로 처리
  - 다음 줄이 타임스탬프인 짧은 제목줄은 assist heading으로 처리
- intentionally not changed:
  - core splitter 전체 구조
  - 2차 판독 스크립트 본체
  - pointer / heading-independent role logic

## 5. why this still counts as minimal

- 특정 파일 전용 hardcoded heading 목록을 넣지 않았다.
- `index-like transcript`라는 형식 단서만 썼다.
- 결과가 좋아질 때까지 규칙을 계속 덧붙이지 않았다.
- segmentation support를 parser 전체 교체로 밀지 않았다.

## 6. expected evaluation points

- single block collapse가 완화되는가
- window diversity가 생기는가
- question opening / relation movement / residue priority shift가 더 넓은 입력 범위에서 유지되는가
- context unit / pivot / compression이 segmentation만으로 일부라도 회복되는가
- 아니면 pointer / heading 축이 다음 우선순위라는 점만 더 선명해지는가

## 7. one-line summary

> 이번 segmentation support는 splitter 재설계가 아니라, 인덱스형 transcript에 이미 있는 `짧은 제목줄 + 타임스탬프`를 segmentation hint로 읽어 single block collapse를 완화해 보는 최소 probe다.
