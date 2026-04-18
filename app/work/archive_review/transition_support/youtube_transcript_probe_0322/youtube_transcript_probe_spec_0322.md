# youtube transcript probe 0322 spec

## 1. 목적
- `youtube_03_22.md` 를 현재 엔진 관점에서 read-only input passage probe로 통과시키고, 시간 흐름과 반복 앵커, 구간별 canonical/mixed 판독을 사용자가 직접 대조 가능한 보고물로 만든다.

## 2. 입력 파일 정보
- input file: `/Users/sungsookim/universe/vectorfl_replica/youtube_03_22.md`
- current finding: explicit `HH:MM:SS` timestamp is not present
- source-side spine policy: preserve `section order + segment order + local_source_ref` as the stable local position spine

## 3. 타임스탬프 보존 규칙
- explicit timestamp가 있으면 `timestamp_start/end`에 그대로 둔다
- explicit timestamp가 없으면 `timestamp_start/end = null` 로 두고
- `local_source_ref = youtube_03_22.md::secXX::segYYYY`
- `prev_segment_id / next_segment_id / section_index / segment_index` 로 순서 spine을 보존한다

## 4. fragment/window 분해 규칙
- split unit: 문장 하나가 아니라 `speaker turn + section context`
- heading(`##`) 기준으로 section을 유지한다
- speaker paragraph는 하나의 segment로 유지하고, 비화자 continuation은 직전 speaker segment에 붙인다
- window는 section 기반 overlap window로 만든다
- target: 6 windows, section size 6, overlap 1

## 5. anchor linkage 관찰 기준
- repeated anchor는 window 간 반복되는 핵심 개념/핸들/표현군으로 본다
- linkage type:
  - `direct_repeat`
  - `semantic_repeat`
  - `translated_repeat`
  - `weak_echo`
- 기술 축, 비즈니스 축, 전환 축을 같이 본다

## 6. stage passage 판독 기준
- `source_survival`: kept / partial / weak / lost
- `translation_survival`: formed / weak / none
- `join_closure`: closed / partial / gap_dominant / none
- `workbench_reading_category`:
  - `canonical`
  - `mixed`
  - `unreadable_yet`
  - `weak_link_only`
- `workbench_reading_status`:
  - `stable_reading`
  - `confirmed_hold`
  - empty when category is unreadable/weak only

## 7. 사람 판독용 보고 형식
- timeline report
- anchor report
- passage report
- final reading board
- 각 md는 JSON 기계 산출물과 직접 대조 가능해야 한다

## 8. 이번 턴의 비목표
- 코어 규칙 수정
- source_local_ref 규칙 보정
- translated_handles 생성 규칙 변경
- bridge 로직 변경
- point/ribbon plotting
- viewer/graph beautification
