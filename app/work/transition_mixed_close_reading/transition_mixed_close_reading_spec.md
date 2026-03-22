# transition mixed close reading spec

## 1. 목적
- round1 / round2에서 `mixed / confirmed_hold` 로 판정된 유닛만 다시 좁혀 읽어, 왜 hold가 되었는지와 어디까지 수정 후보인지를 사용자 판독 가능한 수준으로 드러낸다.

## 2. 입력 자산
- round1:
  - `app/work/youtube_transcript_probe_0322/generated/youtube_03_22_source_manifest.json`
  - `app/work/youtube_transcript_probe_0322/generated/youtube_03_22_window_packets.json`
  - `app/work/youtube_transcript_probe_0322/generated/youtube_03_22_anchor_linkage_report.json`
  - `app/work/youtube_transcript_probe_0322/generated/youtube_03_22_stage_passage_summary.json`
- round2:
  - `app/work/youtube_transcript_probe_0322_b/generated/source_manifest_round2.json`
  - `app/work/youtube_transcript_probe_0322_b/generated/window_packets_round2.json`
  - `app/work/youtube_transcript_probe_0322_b/generated/anchor_linkage_report_round2.json`
  - `app/work/youtube_transcript_probe_0322_b/generated/stage_passage_summary_round2.json`

## 3. 산출물
- `mixed_unit_index.json`
- `mixed_transition_detail_packets.json`
- `mixed_transition_bridge_map.json`
- `mixed_transition_gap_ledger.json`
- `mixed_transition_readable_cards.md`
- `mixed_transition_compare_board.md`
- `mixed_transition_fix_boundary_note.md`

## 4. close reading 기준
- 새 transcript 추가 금지
- mixed 유닛만 읽는다
- `왜 mixed인가` 뿐 아니라 `왜 hold할 가치가 있는가`를 함께 적는다
- gap을 전부 코어 문제로 몰지 않고 `core_candidate / meaning_layer_candidate / observer_only` 로 나눈다

## 5. 이번 턴의 비목표
- 코어 수정
- canonical/mixed 문법 변경
- ontology 추가
- plotting / viewer 확장
