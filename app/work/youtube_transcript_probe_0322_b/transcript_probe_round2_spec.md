# transcript probe round2 spec

## 1. 목적
- `youtube_03_18.md` 를 round1과 같은 probe 규칙으로 통과시키고, repeated anchor survival / mixed hold / transition-led closure weakness가 다시 나타나는지 비교한다.

## 2. 입력 파일 정보
- input file: `/Users/sungsookim/universe/vectorfl_replica/youtube_03_18.md`
- comparison baseline:
  - `/Users/sungsookim/universe/vectorfl_replica/app/work/youtube_transcript_probe_0322/generated/youtube_03_22_anchor_linkage_report.json`
  - `/Users/sungsookim/universe/vectorfl_replica/app/work/youtube_transcript_probe_0322/generated/youtube_03_22_stage_passage_summary.json`
- explicit timestamp가 없으면 round1과 동일하게 `section order + segment order + local_source_ref` 를 source position spine으로 사용한다.

## 3. 동일 규칙 유지 항목
- segment parsing: `## heading + speaker turn`
- overlap window: section window size 6, overlap 1
- linkage type:
  - `direct_repeat`
  - `semantic_repeat`
  - `translated_repeat`
  - `weak_echo`
- stage passage fields:
  - `source_survival`
  - `translation_survival`
  - `join_closure`
  - `repeated_anchor_support`
  - `workbench_reading_category`
  - `workbench_reading_status`
  - `key_gap`
  - `why_this_reading`

## 4. round2 추가 산출물
- `probe_delta_compare_round1_vs_round2.md`
- `probe_fix_candidates_round2.md`

## 5. 사람 판독용 목표
- round2 입력만 읽는 report가 아니라
- round1과 비교했을 때
  - 어떤 강점이 반복되는지
  - 어떤 전환부 weakness가 재현되는지
  - 어떤 것은 fix candidate로 올릴 수 있는지
  를 사용자 관점에서 바로 읽을 수 있게 한다.

## 6. 이번 턴의 비목표
- 코어 수정
- mixed canonicalization
- 새로운 ontology
- point/ribbon plotting
- 보기 좋게 만들기 위한 후처리
